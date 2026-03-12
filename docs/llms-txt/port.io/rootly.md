# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/rootly.md

# Rootly

Custom Ocean integration

This integration was created using the [custom Ocean integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) builder.<br /><!-- -->Please note that:

1. This integration will not be listed in the `Data sources` page of your Port application, and must be installed manually using the instructions on this page.
2. This integration will not create components (e.g. `blueprints`, `mapping`, etc.) in your portal automatically, you will need to create them manually using the instructions on this page.

Port's Rootly integration allows you to ingest Rootly incident management resources into your software catalog using the [Ocean Custom Integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) framework. After installing this integration, you would be able to visualize your Rootly incidents, services, teams, and on-call schedules using Port's dashboards.

## Supported resources[â](#supported-resources "Direct link to Supported resources")

The Rootly integration can ingest the following resources into Port. It is possible to reference any field that appears in the API responses in the mapping configuration. For detailed API documentation, see the [Rootly API documentation](https://docs.rootly.com/api-reference/overview).

* **Incidents** - Incident records and their details from [`/incidents`](https://docs.rootly.com/api-reference/incidents/list-incidents).
* **Services** - Service catalog entries from [`/services`](https://docs.rootly.com/api-reference/services/list-services).
* **Teams** - Team information from [`/teams`](https://docs.rootly.com/api-reference/teams/list-teams).
* **Users** - User accounts from [`/users`](https://docs.rootly.com/api-reference/users/list-users).
* **Environments** - Environment configurations from [`/environments`](https://docs.rootly.com/api-reference/environments/list-environments).
* **Severities** - Incident severity levels from [`/severities`](https://docs.rootly.com/api-reference/severities/list-severities).
* **Functionalities** - Functionality catalog from [`/functionalities`](https://docs.rootly.com/api-reference/functionalities/list-functionalities).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To use this integration, you need:

* A Rootly API key with appropriate permissions to access incident and catalog data.
* The API key should have read access to incidents, services, teams, and other resources you want to sync.

### Create a Rootly API key[â](#create-a-rootly-api-key "Direct link to Create a Rootly API key")

1. Log in to your Rootly account.

2. Click on your **Organization dropdown** in the top navigation.

3. Select **Organization Settings**.

4. Navigate to **API Keys** in the left sidebar.

5. Click **Generate New API Key**.

6. Select the appropriate API key type:

   <!-- -->

   * **Global API Key** - Full access to all entities (recommended for integration).
   * **Team API Key** - Limited to specific team resources.
   * **Personal API Key** - Inherits your user permissions.

7. Provide a name for your API key (e.g., "Port Integration").

8. Click **Generate**.

9. Copy the API key immediately and save it securely.

API key security

Store your API key securely and never share it. The key provides access to your Rootly data.

## Installation[â](#installation "Direct link to Installation")

Choose one of the following installation methods to deploy the Ocean Custom Integration:

* Helm
* Docker

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

## Installation

Add Port's Helm repo and install the Ocean Custom Integration:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_ROOTLY_API_KEY`.

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install my-ocean-rootly-integration port-labs/port-ocean \
  --set port.clientId="YOUR_PORT_CLIENT_ID" \
  --set port.clientSecret="YOUR_PORT_CLIENT_SECRET" \
  --set port.baseUrl="https://api.port.io" \
  --set initializePortResources=true \
  --set scheduledResyncInterval=120 \
  --set integration.identifier="my-ocean-rootly-integration" \
  --set integration.type="custom" \
  --set integration.eventListener.type="POLLING" \
  --set integration.config.baseUrl="https://api.rootly.com/v1" \
  --set integration.config.authType="bearer_token" \
  --set integration.config.paginationType="page" \
  --set integration.config.apiToken="YOUR_ROOTLY_API_KEY"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Configuration parameters

This table summarizes the available parameters for the installation.

| Parameter                           | Description                                                                                                                                                                                                                                   | Example                     | Required |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------- |
| `port.clientId`                     | Your Port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                    |                             | â       |
| `port.clientSecret`                 | Your Port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                |                             | â       |
| `port.baseUrl`                      | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                                                                             |                             | â       |
| `integration.config.baseUrl`        | The base URL of the Rootly API instance                                                                                                                                                                                                       | <https://api.rootly.com/v1> | â       |
| `integration.config.authType`       | The authentication type for the API (use `bearer_token` for Rootly)                                                                                                                                                                           | bearer\_token               | â       |
| `integration.config.apiToken`       | Your Rootly API key                                                                                                                                                                                                                           |                             | â       |
| `integration.config.paginationType` | How your API handles pagination (offset, page, cursor, or none)                                                                                                                                                                               | page                        | â       |
| `integration.eventListener.type`    | The event listener type. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener)                                                                                                                        | POLLING                     | â       |
| `integration.type`                  | The integration type (must be `custom` for Ocean Custom Integration)                                                                                                                                                                          | custom                      | â       |
| `integration.identifier`            | Unique identifier for the integration instance                                                                                                                                                                                                | my-ocean-rootly-integration | â       |
| `scheduledResyncInterval`           | The number of minutes between each resync. When not set the integration will resync for each event listener resync event. Read more about [scheduledResyncInterval](https://ocean.port.io/developing-an-integration/trigger-your-integration) | 120                         | â       |
| `initializePortResources`           | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                                                                                | true                        | â       |
| `sendRawDataExamples`               | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                                                                           | true                        | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

To run the integration using Docker for a one-time sync:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_ROOTLY_API_KEY`.

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://api.rootly.com/v1" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="bearer_token" \
  -e OCEAN__INTEGRATION__CONFIG__PAGINATION_TYPE="page" \
  -e OCEAN__INTEGRATION__CONFIG__API_TOKEN="YOUR_ROOTLY_API_KEY" \
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

Before the integration can sync data, you need to create the required blueprints in Port. These blueprints define the data model for your Rootly resources.

**To create the blueprints:**

1. Go to your [Builder page](https://app.getport.io/settings/data-model).

2. Click on the `+ Blueprint` button.

3. Copy and paste each blueprint JSON from the sections below.

   **Rootly Incident Blueprint (Click to expand)**

   Incident records and their details:

   Create in Port

   ```
   {
     "identifier": "rootly-incident",
     "title": "Rootly Incident",
     "icon": "Rootly",
     "schema": {
       "properties": {
         "title": {
           "title": "Title",
           "type": "string"
         },
         "status": {
           "title": "Status",
           "type": "string"
         },
         "severity": {
           "title": "Severity",
           "type": "string"
         },
         "started_at": {
           "title": "Started At",
           "type": "string",
           "format": "date-time"
         },
         "resolved_at": {
           "title": "Resolved At",
           "type": "string",
           "format": "date-time"
         },
         "url": {
           "title": "Incident URL",
           "type": "string",
           "format": "url"
         },
         "summary": {
           "title": "Summary",
           "type": "string"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Rootly Service Blueprint (Click to expand)**

   Service catalog entries:

   Create in Port

   ```
   {
     "identifier": "rootly-service",
     "title": "Rootly Service",
     "icon": "Rootly",
     "schema": {
       "properties": {
         "name": {
           "title": "Name",
           "type": "string"
         },
         "description": {
           "title": "Description",
           "type": "string"
         },
         "slug": {
           "title": "Slug",
           "type": "string"
         },
         "color": {
           "title": "Color",
           "type": "string"
         },
         "notify_emails": {
           "title": "Notify Emails",
           "type": "array",
           "items": {
             "type": "string"
           }
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Rootly Team Blueprint (Click to expand)**

   Team information:

   Create in Port

   ```
   {
     "identifier": "rootly-team",
     "title": "Rootly Team",
     "icon": "Team",
     "schema": {
       "properties": {
         "name": {
           "title": "Name",
           "type": "string"
         },
         "description": {
           "title": "Description",
           "type": "string"
         },
         "slug": {
           "title": "Slug",
           "type": "string"
         },
         "color": {
           "title": "Color",
           "type": "string"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Rootly User Blueprint (Click to expand)**

   User accounts:

   Create in Port

   ```
   {
     "identifier": "rootly-user",
     "title": "Rootly User",
     "icon": "User",
     "schema": {
       "properties": {
         "email": {
           "title": "Email",
           "type": "string",
           "format": "email"
         },
         "full_name": {
           "title": "Full Name",
           "type": "string"
         },
         "role": {
           "title": "Role",
           "type": "string"
         },
         "accepted_invite_at": {
           "title": "Accepted Invite At",
           "type": "string",
           "format": "date-time"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

4. Click `Save` to save the blueprint.

## Configuration[â](#configuration "Direct link to Configuration")

After installation, define which endpoints to sync in your integration configuration. Each resource maps an API endpoint to Port entities using [JQ expressions](https://stedolan.github.io/jq/manual/) to transform the data.

**Key mapping components:**

* **`kind`**: The API endpoint path (combined with your base URL).
* **`selector.query`**: JQ filter to include/exclude entities (use `'true'` to sync all).
* **`selector.data_path`**: JQ expression pointing to the array of items in the response.
* **`port.entity.mappings`**: How to map API fields to Port entity properties.

For more details on how the Ocean Custom Integration works, see the [How it works](https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/overview#how-it-works) section in the custom integration overview.

**To configure the mappings:**

1. Go to your [data sources page](https://app.getport.io/settings/data-sources).

2. Find your Rootly integration in the list.

3. Click on the integration to open the mapping editor.

4. Add the resource mapping configurations below.

   **Incidents mapping (Click to expand)**

   ```
   resources:
     - kind: /incidents
       selector:
         query: 'true'
         data_path: '.data'
         query_params:
           page[size]: "100"
       port:
         entity:
           mappings:
             identifier: .id
             title: .attributes.title
             blueprint: '"rootly-incident"'
             properties:
               title: .attributes.title
               status: .attributes.status
               severity: .attributes.severity.data.attributes.severity
               started_at: .attributes.started_at
               resolved_at: .attributes.resolved_at
               url: .attributes.url
               summary: .attributes.summary
   ```

   Rootly API response format

   Rootly uses the JSON<!-- -->:API<!-- --> specification, so responses are structured with `data` arrays containing objects with `id`, `type`, and `attributes` fields. Use `.data` as the `data_path` and reference fields via `.attributes.fieldName`.

   **Services mapping (Click to expand)**

   ```
   resources:
     - kind: /services
       selector:
         query: 'true'
         data_path: '.data'
         query_params:
           page[size]: "100"
       port:
         entity:
           mappings:
             identifier: .id
             title: .attributes.name
             blueprint: '"rootly-service"'
             properties:
               name: .attributes.name
               description: .attributes.description
               slug: .attributes.slug
               color: .attributes.color
               notify_emails: .attributes.notify_emails
   ```

   **Teams mapping (Click to expand)**

   ```
   resources:
     - kind: /teams
       selector:
         query: 'true'
         data_path: '.data'
         query_params:
           page[size]: "100"
       port:
         entity:
           mappings:
             identifier: .id
             title: .attributes.name
             blueprint: '"rootly-team"'
             properties:
               name: .attributes.name
               description: .attributes.description
               slug: .attributes.slug
               color: .attributes.color
   ```

   **Users mapping (Click to expand)**

   ```
   resources:
     - kind: /users
       selector:
         query: 'true'
         data_path: '.data'
         query_params:
           page[size]: "100"
       port:
         entity:
           mappings:
             identifier: .id
             title: .attributes.full_name // .attributes.email
             blueprint: '"rootly-user"'
             properties:
               email: .attributes.email
               full_name: .attributes.full_name
               role: .attributes.role
               accepted_invite_at: .attributes.accepted_invite_at
   ```

5. Click `Save` to save the mapping.

## Customization[â](#customization "Direct link to Customization")

If you want to customize your setup or test different API endpoints before committing to a configuration, use the [interactive builder](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration.md).

**The interactive builder helps you:**

1. Test your Rootly API endpoints with live data.
2. Automatically detect the data structure and field types.
3. Generate blueprints and resource mappings tailored to your preferences.
4. Get installation commands with your configuration pre-filled.

Simply provide your Rootly API details, and the builder will generate everything you need to install and create the integration in Port.

## Troubleshooting[â](#troubleshooting "Direct link to Troubleshooting")

### Common issues[â](#common-issues "Direct link to Common issues")

1. **Authentication Errors**: Verify your Rootly API key has the correct permissions and is not expired. Ensure you're using a Global API Key for full access to all resources.
2. **Rate Limiting**: Rootly has API rate limits (3000 requests per minute per API key). The integration handles this automatically with retries. If you encounter frequent rate limit errors, consider reducing the sync frequency.
3. **Data Path Issues**: Rootly uses the JSON
   <!-- -->
   :API
   <!-- -->
   specification, so all responses have a `data` array. Ensure your `data_path` is set to `.data` for all endpoints.
4. **Pagination**: Rootly uses page-based pagination with `page[number]` and `page[size]` parameters. The integration handles this automatically when `paginationType` is set to `page`.
5. **Empty Responses**: If you're getting empty data, verify that your Rootly account has the resources you're trying to sync (incidents, services, teams, etc.).

## Limitations[â](#limitations "Direct link to Limitations")

* The integration currently supports polling-based sync only (no real-time webhooks).
* Rate limits apply (3000 requests per minute per API key).
* Some Rootly resources may require specific permissions or subscription tiers.
* The integration uses the JSON
  <!-- -->
  :API
  <!-- -->
  specification format, which structures responses differently from standard REST APIs.
