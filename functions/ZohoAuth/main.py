import os
import json
import requests
from crowdstrike.foundry.function import APIError, Function, Request, Response

AUTHORIZA_URL = os.environ["AuthorizeURL"]
TOKEN_URL = os.environ["TokenURL"]
SCOPE = os.environ["Scope"]
CALLBACK_URL = os.environ["CallbackURL"]
CLIENT_ID = os.environ["ClientID"]
CLIENT_SECRET = os.environ["ClientSecret"]

func = Function.instance()

@func.handler(method='POST', path='/auth')
def get_access_code(request: Request, config):
    refresh_token = request.body.get('refresh_token', '').strip()
    if refresh_token == '':
        return Response(
            errors=[APIError(code=400, message='Refresh token missing from request')]
        )
    data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'scope': SCOPE, 'redirect_uri': CALLBACK_URL}
    access_token_response = requests.post(TOKEN_URL, data=data, allow_redirects=True, verify=True, timeout=300)
    tokens = json.loads(access_token_response.text)
    if 'access_token' not in tokens:
        return Response(
            errors=[APIError(code=400, message=f'Failed to get access token from Zoho OAuth2. Received: {tokens}')]
        )
    
    return Response(
        body={'access_token': tokens['access_token']},
        code=200,
    )

if __name__ == '__main__':
    func.run()