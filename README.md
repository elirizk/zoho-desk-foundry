# Zoho Desk Integration for CrowdStrike Foundry

This repository holds a custom Zoho Desk Integration as a CrowdStrike Foundry application. The app enhances functionality and workflow by integrating with the Zoho Desk API to create tickets and add tags to a ticket. This app allows users to interact with Zoho Desk features, including OAuth2 authentication and data transformation, directly from the CrowdStrike platform.

---

## Features

- **Zoho OAuth2 Authentication**  
  Authenticate and obtain access tokens from a refresh token for Zoho Desk API with the `get_access_code` in _ZohoAuth_ function.

- **Data Processing Functions**  
  Process and transform data for integration between Zoho Desk and CrowdStrike:
  - Map CrowdStrike severity to Zoho Desk priority.
  - Clean and standardize sensor tags.
  - Format incident names.

---

## App Structure

This app is structured based on the CrowdStrike Foundry framework and includes the following components:

### API Integrations

- **Zoho Desk API**  
  Defined in `api-integrations/Zoho_Desk.json`.

### Functions

1. **ZohoAuth**  
   Handles OAuth2 authentication for Zoho Desk.

   - **Endpoint**: `/auth`
   - **Handler**: `get_access_code`
   - **Environment Variables**:
     - `AuthorizeURL`: Zoho OAuth authorization URL.
     - `TokenURL`: Token URL to obtain an access token.
     - `BaseURL`: Base URL for Zoho Desk API.
     - `CallbackURL`: Callback URL configured for the Zoho Desk API credentials.
     - `ClientID`: Client ID of the Zoho Desk API instance.
     - `ClientSecret`: Client secret of the Zoho Desk API instance.
     - `Scope`: Scope of the requested API access, configured to Desk.tickets.ALL,Desk.contacts.READ,Desk.settings.READ.

2. **DataProcessing**  
   Handles data transformations for better interoperability.
   - **Endpoints**:
     - `get_priority`: Map severity to priority.
     - `get_sensor_tags`: Clean and return sensor tags.
     - `get_incident_name`: Generate formatted incident names.

### Schemas

All request and response schemas are available under the `schemas/` directory for structured data exchange. This is required to allow proper user input and data handling within the Fusion SOAR platform to automate workflows.

---

## Deployment

To deploy this app:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/elirizk/zoho-desk-foundry.git
   cd zoho-desk-foundry
   ```

2. **Configure Environment Variables**  
   Update the environment variables in the `ZohoAuth` function configuration:
   - AuthorizeURL: https://accounts.zoho.com/oauth/v2/auth
   - BaseURL: https://desk.zoho.com/api/v1
   - CallbackURL: YOUR_CALLBACK_URL
   - ClientID: YOUR_CLIENT_ID
   - ClientSecret: YOUR_CLIENT_SECRET
   - Scope: Desk.tickets.ALL,Desk.contacts.READ,Desk.settings.READ
   - TokenURL: https://accounts.zoho.com/oauth/v2/token
3. **Deploy the Foundry app**
  You can deploy the app by importing the folder in the CrowdStrike Foundry platform under *Import app* or using the Foundry CLI to deploy it with `foundry apps deploy`.