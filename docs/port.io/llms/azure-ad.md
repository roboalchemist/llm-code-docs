# Source: https://docs.port.io/sso-rbac/sso-providers/saml/azure-ad.md

# Source: https://docs.port.io/sso-rbac/sso-providers/oidc/azure-ad.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/identity-providers/azure-ad.md

# Microsoft Entra ID

Custom Ocean integration

This integration was created using the [custom Ocean integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) builder.<br /><!-- -->Please note that:

1. This integration will not be listed in the `Data sources` page of your Port application, and must be installed manually using the instructions on this page.
2. This integration will not create components (e.g. `blueprints`, `mapping`, etc.) in your portal automatically, you will need to create them manually using the instructions on this page.

Port's Microsoft Entra ID (formerly Azure AD) integration allows you to model Entra ID resources in your software catalog and ingest data into them using the [Ocean Custom Integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) framework.

## Supported resources[â](#supported-resources "Direct link to Supported resources")

The Microsoft Entra ID integration can ingest the following resources into Port:

* `entra-id-user` - User accounts and their profile information from [`/users`](https://learn.microsoft.com/en-us/graph/api/user-list).
* `entra-id-group` - Security and Microsoft 365 groups from [`/groups`](https://learn.microsoft.com/en-us/graph/api/group-list).
* `entra-id-application` - Enterprise applications registered in Entra ID from [`/applications`](https://learn.microsoft.com/en-us/graph/api/application-list).
* `entra-id-service-principal` - Service principal objects representing applications from [`/servicePrincipals`](https://learn.microsoft.com/en-us/graph/api/serviceprincipal-list).

It is possible to reference any field that appears in the API responses linked above in the mapping configuration.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To use this integration, you need:

* A Microsoft Entra ID application registration with appropriate API permissions.
* A client secret for the application.
* Admin consent for the required permissions.
* An access token (bearer token) for Microsoft Graph API.

**To register an application in Microsoft Entra ID:**

1. Log in to the [Azure Portal](https://portal.azure.com).
2. Navigate to **Microsoft Entra ID** > **App registrations**.
3. Click **New registration**.
4. Provide a name for your application (e.g., "Port Integration").
5. Select **Accounts in this organizational directory only**.
6. Click **Register**.
7. Note the **Application (client) ID** and **Directory (tenant) ID**.

**To create a client secret:**

1. In your app registration, navigate to **Certificates & secrets**.
2. Click **New client secret**.
3. Provide a description (e.g., "Port Integration Secret").
4. Select an expiration period.
5. Click **Add**.
6. **Copy the secret value immediately** - it will not be shown again.

Secret security

Store your client secret securely and never share it. The secret provides access to your Entra ID data.

**To grant API permissions:**

1. In your app registration, navigate to **API permissions**.

2. Click **Add a permission**.

3. Select **Microsoft Graph**.

4. Select **Application permissions**.

5. Add the following permissions:

   <!-- -->

   * `User.Read.All` - Read all users' full profiles.
   * `Group.Read.All` - Read all groups.
   * `Application.Read.All` - Read all applications.
   * `Directory.Read.All` - Read directory data.

6. Click **Add permissions**.

7. Click **Grant admin consent for \[Your Organization]**.

Admin consent required

An Entra ID administrator must grant consent for these permissions before the integration can access the data.

**To get an access token (bearer token):**

You need to obtain an OAuth2 access token to authenticate with Microsoft Graph API. Use the following curl command to get a token:

```
curl -X POST "https://login.microsoftonline.com/YOUR_TENANT_ID/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "scope=https://graph.microsoft.com/.default" \
  -d "grant_type=client_credentials" | jq -r '.access_token'
```

Replace:

* `YOUR_TENANT_ID` with your Directory (tenant) ID.
* `YOUR_CLIENT_ID` with your Application (client) ID.
* `YOUR_CLIENT_SECRET` with your client secret value.

Token expiration

Access tokens typically expire after 1 hour. For production use, consider implementing automatic token refresh or using OAuth2 client credentials flow with automatic token management.

**To find your tenant ID:**

Your tenant ID is the **Directory (tenant) ID** from your app registration. You can also find it in the Microsoft Entra ID overview page.

## Installation[â](#installation "Direct link to Installation")

Choose one of the following installation methods to deploy the Ocean Custom Integration:

* Helm
* Docker

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

## Installation

1. Add Port's Helm repo and install the Ocean Custom Integration:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_BEARER_TOKEN`. Get your bearer token using the curl command in the Prerequisites section.

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install my-ocean-entra-id-integration port-labs/port-ocean \
  --set port.clientId="YOUR_PORT_CLIENT_ID" \
  --set port.clientSecret="YOUR_PORT_CLIENT_SECRET" \
  --set port.baseUrl="https://api.port.io" \
  --set initializePortResources=true \
  --set scheduledResyncInterval=120 \
  --set integration.identifier="entra-id-integration" \
  --set integration.type="custom" \
  --set integration.eventListener.type="POLLING" \
  --set integration.config.baseUrl="https://graph.microsoft.com/v1.0" \
  --set integration.config.authType="bearer_token" \
  --set integration.config.apiToken="YOUR_BEARER_TOKEN"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Configuration parameters

This table summarizes the available parameters for the installation.

| Parameter                           | Description                                                                                                                     | Example                            | Required |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| `port.clientId`                     | Your Port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials).     |                                    | â       |
| `port.clientSecret`                 | Your Port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials). |                                    | â       |
| `port.baseUrl`                      | Your Port API URL (`https://api.port.io` for EU, `https://api.us.port.io` for US).                                              |                                    | â       |
| `integration.config.baseUrl`        | Base URL of the Microsoft Graph API.                                                                                            | <https://graph.microsoft.com/v1.0> | â       |
| `integration.config.authType`       | Authentication type for the API (use `bearer_token` for Entra ID).                                                              | bearer\_token                      | â       |
| `integration.config.apiToken`       | Microsoft Graph API bearer token created via the OAuth2 client credentials flow.                                                | eyJ0eXAiOiJKV1QiLCJub25jZSI6...    | â       |
| `integration.config.paginationType` | How the API handles pagination (offset, page, cursor, skip\_token, or none).                                                    | skip\_token                        | â       |
| `integration.eventListener.type`    | Event listener type. See [event listeners](https://ocean.getport.io/framework/features/event-listener).                         | POLLING                            | â       |
| `integration.type`                  | Integration type (must be `custom`).                                                                                            | custom                             | â       |
| `integration.identifier`            | Unique identifier for the integration instance.                                                                                 | entra-id-integration               | â       |
| `scheduledResyncInterval`           | Minutes between scheduled syncs. When omitted, the event listener interval is used.                                             | 120                                | â       |
| `initializePortResources`           | When true, creates default blueprints and mappings on first run.                                                                | true                               | â       |
| `sendRawDataExamples`               | Sends sample payloads from the API to Port for easier mapping.                                                                  | true                               | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

To run the integration using Docker for a one-time sync:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_BEARER_TOKEN`. Get your bearer token using the curl command in the Prerequisites section.

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://graph.microsoft.com/v1.0" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="bearer_token" \
  -e OCEAN__INTEGRATION__CONFIG__API_TOKEN="YOUR_BEARER_TOKEN" \
  -e OCEAN__PORT__CLIENT_ID="YOUR_PORT_CLIENT_ID" \
  -e OCEAN__PORT__CLIENT_SECRET="YOUR_PORT_CLIENT_SECRET" \
  -e OCEAN__PORT__BASE_URL="https://api.port.io" \
  ghcr.io/port-labs/port-ocean-custom:latest
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

Before the integration can sync data, you need to create the required blueprints in Port. These blueprints define the data model for your Entra ID resources.

**To create the blueprints:**

Create the blueprints in the following order:

1. Go to your [Builder page](https://app.getport.io/settings/data-model).

2. Click on the `+ Blueprint` button.

3. Copy and paste each blueprint JSON from the sections below in order:

   **1. Entra ID Application Blueprint (Click to expand)**

   Enterprise applications registered in Entra ID:

   Create in Port

   ```
   {
     "identifier": "entra-id-application",
     "description": "An application registration in Microsoft Entra ID",
     "title": "Entra ID Application",
     "icon": "Microsoft",
     "schema": {
       "properties": {
         "displayName": {
           "title": "Display Name",
           "type": "string"
         },
         "appId": {
           "title": "Application ID",
           "type": "string"
         },
         "publisherDomain": {
           "title": "Publisher Domain",
           "type": "string"
         },
         "signInAudience": {
           "title": "Sign-In Audience",
           "type": "string"
         },
         "createdDateTime": {
           "title": "Created Date",
           "type": "string",
           "format": "date-time"
         }
       },
       "required": ["displayName"]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **2. Entra ID Service Principal Blueprint (Click to expand)**

   Service principal objects representing applications:

   Create in Port

   ```
   {
     "identifier": "entra-id-service-principal",
     "description": "A service principal object in Microsoft Entra ID",
     "title": "Entra ID Service Principal",
     "icon": "Microsoft",
     "schema": {
       "properties": {
         "displayName": {
           "title": "Display Name",
           "type": "string"
         },
         "appId": {
           "title": "Application ID",
           "type": "string"
         },
         "appOwnerOrganizationId": {
           "title": "Owner Organization",
           "type": "string"
         },
         "accountEnabled": {
           "title": "Account Enabled",
           "type": "boolean"
         },
         "appRoleAssignmentRequired": {
           "title": "App Role Assignment Required",
           "type": "boolean"
         },
         "createdDateTime": {
           "title": "Created Date",
           "type": "string",
           "format": "date-time"
         }
       },
       "required": ["displayName"]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **3. Entra ID User Blueprint (Click to expand)**

   User accounts and their profile information:

   Create in Port

   ```
   {
     "identifier": "entra-id-user",
     "description": "A Microsoft Entra ID user account",
     "title": "Entra ID User",
     "icon": "Microsoft",
     "schema": {
       "properties": {
         "userPrincipalName": {
           "title": "User Principal Name",
           "type": "string",
           "format": "email"
         },
         "displayName": {
           "title": "Display Name",
           "type": "string"
         },
         "givenName": {
           "title": "Given Name",
           "type": "string"
         },
         "surname": {
           "title": "Surname",
           "type": "string"
         },
         "mail": {
           "title": "Email",
           "type": "string",
           "format": "email"
         },
         "jobTitle": {
           "title": "Job Title",
           "type": "string"
         },
         "department": {
           "title": "Department",
           "type": "string"
         },
         "officeLocation": {
           "title": "Office Location",
           "type": "string"
         },
         "accountEnabled": {
           "title": "Account Enabled",
           "type": "boolean"
         },
         "createdDateTime": {
           "title": "Created Date",
           "type": "string",
           "format": "date-time"
         },
         "lastSignInDateTime": {
           "title": "Last Sign In",
           "type": "string",
           "format": "date-time"
         }
       },
       "required": ["userPrincipalName"]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **4. Entra ID Group Blueprint (Click to expand)**

   Security and Microsoft 365 groups:

   Create in Port

   ```
   {
     "identifier": "entra-id-group",
     "description": "A Microsoft Entra ID group (security or Microsoft 365)",
     "title": "Entra ID Group",
     "icon": "Microsoft",
     "schema": {
       "properties": {
         "displayName": {
           "title": "Display Name",
           "type": "string"
         },
         "description": {
           "title": "Description",
           "type": "string"
         },
         "groupTypes": {
           "title": "Group Types",
           "type": "array",
           "items": {
             "type": "string"
           }
         },
         "mailEnabled": {
           "title": "Mail Enabled",
           "type": "boolean"
         },
         "securityEnabled": {
           "title": "Security Enabled",
           "type": "boolean"
         },
         "createdDateTime": {
           "title": "Created Date",
           "type": "string",
           "format": "date-time"
         }
       },
       "required": ["displayName"]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "members": {
         "title": "Members",
         "target": "entra-id-user",
         "required": false,
         "many": true
       }
     }
   }
   ```

4. Click `Save` to save each blueprint after creating it.

Adding relations after creation

After creating both the User and Group blueprints, you can edit the User blueprint to add a relation to Group. In the User blueprint, add this to the `relations` section:

```
"groups": {
  "title": "Groups",
  "target": "entra-id-group",
  "required": false,
  "many": true
}
```

## Configuration[â](#configuration "Direct link to Configuration")

After installation, define which endpoints to sync in your integration configuration. Each resource maps an API endpoint to Port entities using [JQ expressions](https://stedolan.github.io/jq/manual/) to transform the data.

**Key mapping components:**

* **`kind`**: The API endpoint path (combined with your base URL).
* **`selector.query`**: JQ filter to include/exclude entities (use `'true'` to sync all).
* **`selector.data_path`**: JQ expression pointing to the array of items in the response.
* **`port.entity.mappings`**: How to map API fields to Port entity properties.

For more details on how the Ocean Custom Integration works, see the [How it works](https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/overview#how-it-works) section in the custom integration overview.

**Microsoft Graph API response format:**

Microsoft Graph API responses typically follow this structure:

```
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users",
  "value": [
    {
      "id": "00000000-0000-0000-0000-000000000000",
      "displayName": "John Doe",
      ...
    }
  ],
  "@odata.nextLink": "https://graph.microsoft.com/v1.0/users?$skiptoken=..."
}
```

The actual data array is in the `.value` property, and pagination information is in `@odata.nextLink` with a `$skiptoken` parameter.

**To configure the mappings:**

1. Go to your [data sources page](https://app.getport.io/settings/data-sources).

2. Find your Entra ID integration in the list.

3. Click on the integration to open the mapping editor.

4. Add the resource mapping configurations below.

   **Users mapping (Click to expand)**

   ```
   resources:
     - kind: /users
       selector:
         query: 'true'
         data_path: '.value'
         query_params:
           $top: "999"
       port:
         entity:
           mappings:
             identifier: .id
             title: .displayName // .userPrincipalName
             blueprint: '"entra-id-user"'
             properties:
               userPrincipalName: .userPrincipalName
               displayName: .displayName
               givenName: .givenName
               surname: .surname
               mail: .mail
               jobTitle: .jobTitle
               department: .department
               officeLocation: .officeLocation
               accountEnabled: .accountEnabled
               createdDateTime: .createdDateTime
               lastSignInDateTime: .signInActivity.lastSignInDateTime
   ```

   **Groups mapping (Click to expand)**

   ```
   resources:
     - kind: /groups
       selector:
         query: 'true'
         data_path: '.value'
         query_params:
           $top: "999"
           $expand: "members($select=id)"
       port:
         entity:
           mappings:
             identifier: .id
             title: .displayName
             blueprint: '"entra-id-group"'
             properties:
               displayName: .displayName
               description: .description
               groupTypes: .groupTypes
               mailEnabled: .mailEnabled
               securityEnabled: .securityEnabled
               createdDateTime: .createdDateTime
             relations:
               members: "[.members[]?.id]"
   ```

   **Applications mapping (Click to expand)**

   ```
   resources:
     - kind: /applications
       selector:
         query: 'true'
         data_path: '.value'
         query_params:
           $top: "999"
       port:
         entity:
           mappings:
             identifier: .id
             title: .displayName
             blueprint: '"entra-id-application"'
             properties:
               displayName: .displayName
               appId: .appId
               publisherDomain: .publisherDomain
               signInAudience: .signInAudience
               createdDateTime: .createdDateTime
   ```

   **Service principals mapping (Click to expand)**

   ```
   resources:
     - kind: /servicePrincipals
       selector:
         query: 'true'
         data_path: '.value'
         query_params:
           $top: "999"
       port:
         entity:
           mappings:
             identifier: .id
             title: .displayName
             blueprint: '"entra-id-service-principal"'
             properties:
               displayName: .displayName
               appId: .appId
               appOwnerOrganizationId: .appOwnerOrganizationId
               accountEnabled: .accountEnabled
               appRoleAssignmentRequired: .appRoleAssignmentRequired
               createdDateTime: .createdDateTime
   ```

5. Click `Save` to save the mapping.

## Customization[â](#customization "Direct link to Customization")

If you want to customize your setup or test different API endpoints before committing to a configuration, use the [interactive builder](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration.md).

**The interactive builder helps you:**

1. Test your Microsoft Graph API endpoints with live data.
2. Automatically detect the data structure and field types.
3. Generate blueprints and resource mappings tailored to your preferences.
4. Get installation commands with your configuration pre-filled.

Simply provide your Entra ID API details, and the builder will generate everything you need to install and create the integration in Port.
