from crowdstrike.foundry.function import APIError, Function, Request, Response
from typing import Dict, Union

func = Function.instance()


@func.handler(method='POST', path='/priority')
def get_priority(request: Request, config: Union[Dict[str, any], None]) -> Response:
    severity = request.body.get('severity', '').strip()
    if severity == '':
        return Response(
            errors=[APIError(code=400, message='Severity parameter missing from request')]
        )
    SEVERITY_MAP = {
        "1": "Informational",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Critical"
    }
    if severity in SEVERITY_MAP.keys():
        priority = SEVERITY_MAP[severity]
    else:
        priority = severity
    return Response(
        body={'priority': priority},
        code=200,
    )

@func.handler(method='POST', path='/sensor_tags')
def get_sensor_tags(request: Request, config: Union[Dict[str, any], None]) -> Response:
    if 'sensor_tags' not in request.body:
        return Response(
            errors=[APIError(code=400, message='Refresh token missing from request')]
        )
    sensor_tags = request.body.get('sensor_tags', [])
    tags = []
    for tag in sensor_tags:
        tags.append(tag.split('/')[-1].lower())
    tag_name = '/'.join(tags)
    return Response(
        body={'tags': tags, 'tag_name': tag_name},
        code=200,
    )
    
@func.handler(method='POST', path='/incident_name')
def get_incident_name(request: Request, config: Union[Dict[str, any], None]) -> Response:
    incident_name = request.body.get('incident_name', '').strip()
    if incident_name == '':
        return Response(
            errors=[APIError(code=400, message='Incident name missing from request')]
        )
    before_at, at_keyword, timestamp = incident_name.partition("at")
    formatted_timestamp = timestamp.replace("T", " ").replace("Z", "")
    formatted_name = f"{before_at}{at_keyword}{formatted_timestamp}"
    return Response(
        body={'formatted_incident_name': formatted_name},
        code=200,
    )

if __name__ == '__main__':
    func.run()