# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/ai-agents/n8n.md

# n8n

Custom Ocean integration

This integration was created using the [custom Ocean integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) builder.<br /><!-- -->Please note that:

1. This integration will not be listed in the `Data sources` page of your Port application, and must be installed manually using the instructions on this page.
2. This integration will not create components (e.g. `blueprints`, `mapping`, etc.) in your portal automatically, you will need to create them manually using the instructions on this page.

Port's n8n integration ingests n8n resources into your software catalog using the [Ocean Custom Integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) framework. It focuses on three key data sources: users, projects, and workflows.

## Supported resources[â](#supported-resources "Direct link to Supported resources")

The n8n integration can ingest the following resources into Port:

* `n8nUser` â n8n users from `/v1/users`.
* `n8nProject` â n8n projects from `/v1/projects`.
* `n8nWorkflow` â n8n workflows from `/v1/workflows`.

These resources provide visibility into your n8n automation platform, including user management, project organization, and workflow definitions.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To use this integration, you need:

1. Port credentials (`CLIENT_ID` and `CLIENT_SECRET`)
2. n8n instance URL (e.g., `https://your-instance.com/api`)
3. n8n API key (see [n8n API docs](https://docs.n8n.io/api/authentication/))

**To create an n8n API key:**

1. Navigate to your n8n instance and sign in to your account.
2. Go to **Settings** â **API**.
3. Click **Create API Key**.
4. Give your key a name (e.g., "Port Integration") and copy the API key.
5. Store the API key securely.

API key security

Store your API key securely and never share it. The key provides access to your n8n instance data.

Review the [n8n API reference](https://docs.n8n.io/api/api-reference/) to understand the exact response structure returned by each endpoint.

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

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, `YOUR_N8N_INSTANCE_URL`, and `YOUR_N8N_API_KEY`.

```
helm repo add port-labs https://port-labs.github.io/helm-charts
helm repo update

helm install n8n-integration port-labs/port-ocean \
--set initializePortResources=true \
--set scheduledResyncInterval=120 \
--set sendRawDataExamples=true \
--set integration.type="custom" \
--set integration.eventListener.type="POLLING" \
--set integration.identifier=n8n-integration \
--set integration.config.baseUrl=https://your-instance.com/api \
--set integration.config.authType=api_key \
--set integration.config.apiKeyHeader=X-N8N-API-KEY \
--set integration.secrets.apiKey=YOUR_N8N_API_KEY \
--set integration.config.paginationType=cursor \
--set integration.config.paginationParam=cursor \
--set integration.config.sizeParam=limit \
--set integration.config.pageSize=100 \
--set integration.config.cursorPath=nextCursor \
--set integration.config.hasMorePath=nextCursor \
--set port.clientId=YOUR_PORT_CLIENT_ID \
--set port.clientSecret=YOUR_PORT_CLIENT_SECRET \
--set port.baseUrl="https://api.port.io"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Configuration parameters

| Parameter                            | Description                                                                                                                     | Example                         | Required |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | -------- |
| `port.clientId`                      | Your Port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials).     |                                 | â       |
| `port.clientSecret`                  | Your Port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials). |                                 | â       |
| `port.baseUrl`                       | Your Port API URL (`https://api.port.io` for EU, `https://api.us.port.io` for US).                                              |                                 | â       |
| `integration.config.baseUrl`         | Base URL for your n8n instance API.                                                                                             | <https://your-instance.com/api> | â       |
| `integration.config.authType`        | Authentication type for n8n (use `api_key` for n8n).                                                                            | api\_key                        | â       |
| `integration.config.apiKeyHeader`    | Header name for the API key.                                                                                                    | X-N8N-API-KEY                   | â       |
| `integration.secrets.apiKey`         | n8n API key.                                                                                                                    |                                 | â       |
| `integration.config.paginationType`  | Pagination type used by n8n API.                                                                                                | cursor                          | â       |
| `integration.config.paginationParam` | Query parameter name for pagination cursor.                                                                                     | cursor                          | â       |
| `integration.config.sizeParam`       | Query parameter name for page size.                                                                                             | limit                           | â       |
| `integration.config.pageSize`        | Number of items per page.                                                                                                       | 100                             | â       |
| `integration.config.cursorPath`      | JSON path to cursor value in response.                                                                                          | nextCursor                      | â       |
| `integration.config.hasMorePath`     | JSON path to check if more pages exist.                                                                                         | nextCursor                      | â       |
| `integration.eventListener.type`     | The event listener type. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener)          | POLLING                         | â       |
| `integration.type`                   | The integration type (must be `custom` for Ocean Custom Integration).                                                           | custom                          | â       |
| `integration.identifier`             | Unique identifier for this integration instance.                                                                                | n8n-integration                 | â       |
| `initializePortResources`            | Create default blueprints and mappings on first run.                                                                            | true                            | â       |
| `sendRawDataExamples`                | Send sample payloads for easier mapping.                                                                                        | true                            | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

To run the integration using Docker for a one-time sync:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, `YOUR_N8N_INSTANCE_URL`, and `YOUR_N8N_API_KEY`.

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__INTEGRATION__IDENTIFIER=n8n-integration \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://your-instance.com/api" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="api_key" \
  -e OCEAN__INTEGRATION__CONFIG__API_KEY_HEADER="X-N8N-API-KEY" \
  -e OCEAN__INTEGRATION__CONFIG__API_KEY="YOUR_N8N_API_KEY" \
  -e OCEAN__INTEGRATION__CONFIG__PAGINATION_TYPE="cursor" \
  -e OCEAN__INTEGRATION__CONFIG__PAGINATION_PARAM="cursor" \
  -e OCEAN__INTEGRATION__CONFIG__SIZE_PARAM="limit" \
  -e OCEAN__INTEGRATION__CONFIG__PAGE_SIZE="100" \
  -e OCEAN__INTEGRATION__CONFIG__CURSOR_PATH="nextCursor" \
  -e OCEAN__INTEGRATION__CONFIG__HAS_MORE_PATH="nextCursor" \
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

Before syncing data, create the blueprints that define your n8n entities (users, projects, and workflows).

**To create the blueprints:**

1. Go to your [Builder page](https://app.getport.io/settings/data-model).

2. Click the `+ Blueprint` button.

3. Copy each blueprint JSON from the sections below.

   **n8n User blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "n8nUser",
     "description": "This blueprint represents an n8n user",
     "title": "n8n User",
     "icon": "User",
     "schema": {
       "properties": {
         "created_at": {
           "type": "string",
           "title": "Created At",
           "format": "date-time"
         },
         "is_active": {
           "type": "boolean",
           "title": "Is Active"
         },
         "email": {
           "type": "string",
           "title": "Email"
         },
         "full_name": {
           "type": "string",
           "title": "Full Name"
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

   **n8n Project blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "n8nProject",
     "description": "This blueprint represents an n8n project",
     "title": "n8n Project",
     "icon": "OpenFolder",
     "schema": {
       "properties": {},
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **n8n Workflow blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "n8nWorkflow",
     "description": "This blueprint represents an n8n workflow",
     "title": "n8n Workflow",
     "icon": "Pipeline",
     "schema": {
       "properties": {
         "created_at": {
           "type": "string",
           "title": "Created At",
           "format": "date-time"
         },
         "updated_at": {
           "type": "string",
           "title": "Updated At",
           "format": "date-time"
         },
         "is_active": {
           "type": "boolean",
           "title": "Is Active"
         },
         "is_archived": {
           "type": "boolean",
           "title": "Is Archived"
         },
         "nodes": {
           "items": {
             "type": "object"
           },
           "icon": "DefaultProperty",
           "type": "array",
           "title": "Nodes"
         },
         "connections": {
           "type": "object",
           "title": "Connections"
         },
         "trigger_count": {
           "type": "number",
           "title": "Trigger Count"
         },
         "tags": {
           "items": {
             "type": "string"
           },
           "type": "array",
           "title": "Tags"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "project": {
         "title": "Project",
         "target": "n8nProject",
         "required": false,
         "many": false
       }
     }
   }
   ```

4. Click `Save` after each blueprint is added.

## Configuration[â](#configuration "Direct link to Configuration")

Each resource maps an n8n endpoint to the Port entities defined above.

**Key mapping components:**

* **`kind`** â API endpoint path appended to your n8n base URL.
* **`selector`** â Request payload, pagination controls, and data selection logic.
* **`port.entity.mappings`** â JQ expressions that transform the API payload into Port entities.

To configure the mapping:

1. Go to the [data sources page](https://app.getport.io/settings/data-sources) of your portal.

2. Find your n8n integration in the list.

3. Click on the integration to open the mapping editor.

4. Add the resource mapping configurations below.

   **Complete n8n mapping configuration (Click to expand)**

   ```
   deleteDependentEntities: true
   createMissingRelatedEntities: true
   enableMergeEntity: true
   resources:
     - kind: /v1/users
       selector:
         query: 'true'
         data_path: .data
       port:
         entity:
           mappings:
             identifier: .id
             title: .email
             blueprint: '"n8nUser"'
             properties:
               full_name: >-
                 if (.firstName // null) != null or (.lastName // null) != null
                 then ((.firstName // "") + " " + (.lastName // "")) else .email
                 end
               is_active: (.isPending | not)
               created_at: .createdAt
               email: .email
     - kind: /v1/projects
       selector:
         query: 'true'
         data_path: .data
       port:
         entity:
           mappings:
             identifier: .id
             title: .name
             blueprint: '"n8nProject"'
             properties: {}
     - kind: /v1/workflows
       selector:
         query: 'true'
         data_path: .data
       port:
         entity:
           mappings:
             identifier: .id
             title: .name
             blueprint: '"n8nWorkflow"'
             properties:
               nodes: .nodes
               connections: .connections
               trigger_count: .triggerCount
               is_active: .active
               is_archived: .isArchived
               tags: (.tags | map(.name))
               created_at: .createdAt
               updated_at: .updatedAt
             relations:
               project: .shared[0].projectId
   ```

5. Click `Save` to save the mapping.

## Customization[â](#customization "Direct link to Customization")

If you want to expand beyond the starter resources, use the [interactive builder](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration.md) to:

1. Test additional n8n endpoints.
2. Explore the response shape and detected property types.
3. Generate blueprint JSON and mapping snippets automatically.
4. Export installation commands with your configuration pre-filled.

Start with the users, projects, and workflows entities above, then add more resources (such as executions or credentials) once you verify the value.

## API Reference[â](#api-reference "Direct link to API Reference")

* [n8n Projects API](https://docs.n8n.io/api/api-reference/#tag/projects/get/projects)
* [n8n Users API](https://docs.n8n.io/api/api-reference/#tag/user/get/users)
* [n8n Workflows API](https://docs.n8n.io/api/api-reference/#tag/workflow/get/workflows)
