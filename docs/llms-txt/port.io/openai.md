# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/ai-agents/openai.md

# OpenAI

Custom Ocean integration

This integration was created using the [custom Ocean integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) builder.<br /><!-- -->Please note that:

1. This integration will not be listed in the `Data sources` page of your Port application, and must be installed manually using the instructions on this page.
2. This integration will not create components (e.g. `blueprints`, `mapping`, etc.) in your portal automatically, you will need to create them manually using the instructions on this page.

Port's OpenAI integration ingests foundational OpenAI usage metrics into your software catalog using the [Ocean Custom Integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) framework. It focuses on two reliable data sources: daily cost summaries and model-level usage statistics.

The integration tracks usage across all OpenAI models, including ChatGPT models (GPT-4, GPT-3.5, etc.) and other OpenAI API models.

## Supported resources[â](#supported-resources "Direct link to Supported resources")

The OpenAI integration can ingest the following resources into Port:

* `openai_daily_usage` â Daily totals for requests, tokens, and spend from `/dashboard/billing/usage`.
* `openai_model_usage` â Model-level request and token breakdowns from `/usage`.
* `openai_model` â Available OpenAI models and their details from `/models`.

These resources provide visibility into your OpenAI usage, costs, and available models.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To use this integration, you need:

* An OpenAI API key with access to the usage and billing endpoints.
* Network access from the Ocean integration to `api.openai.com`.

**To create an OpenAI API key:**

1. Navigate to the [OpenAI Platform](https://platform.openai.com/) and sign in to your account.
2. Click on your profile icon in the top right corner and select **API keys**.
3. Click **Create new secret key**.
4. Give your key a name (e.g., "Port Integration") and click **Create secret key**.
5. Copy the API key immediately (it starts with `sk-`). You won't be able to see it again after closing the dialog.

API key security

Store your API key securely and never share it. The key provides access to your OpenAI account usage and billing data.

Review the [OpenAI usage docs](https://platform.openai.com/docs/api-reference/usage) to understand the exact response structure returned by each endpoint.

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

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_OPENAI_API_KEY`.

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install my-ocean-openai-integration port-labs/port-ocean \
  --set port.clientId="YOUR_PORT_CLIENT_ID" \
  --set port.clientSecret="YOUR_PORT_CLIENT_SECRET" \
  --set port.baseUrl="https://api.port.io" \
  --set initializePortResources=true \
  --set integration.identifier="openai-integration" \
  --set integration.type="custom" \
  --set integration.eventListener.type="POLLING" \
  --set integration.config.baseUrl="https://api.openai.com/v1" \
  --set integration.config.authType="bearer_token" \
  --set integration.config.apiToken="YOUR_OPENAI_API_KEY"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Configuration parameters

| Parameter                        | Description                                                                                                                     | Example                     | Required |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------- |
| `port.clientId`                  | Your Port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials).     |                             | â       |
| `port.clientSecret`              | Your Port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials). |                             | â       |
| `port.baseUrl`                   | Your Port API URL (`https://api.port.io` for EU, `https://api.us.port.io` for US).                                              |                             | â       |
| `integration.config.baseUrl`     | Base URL for the OpenAI API.                                                                                                    | <https://api.openai.com/v1> | â       |
| `integration.config.authType`    | Authentication type for OpenAI (use `bearer_token` for OpenAI).                                                                 | bearer\_token               | â       |
| `integration.config.apiToken`    | OpenAI API key (starts with `sk-`).                                                                                             | sk-abc123                   | â       |
| `integration.eventListener.type` | Event listener type for the integration.                                                                                        | POLLING                     | â       |
| `integration.type`               | Integration type. Must be `custom`.                                                                                             | custom                      | â       |
| `integration.identifier`         | Unique identifier for this integration instance.                                                                                | openai-integration          | â       |
| `initializePortResources`        | Create default blueprints and mappings on first run.                                                                            | true                        | â       |
| `scheduledResyncInterval`        | Minutes between scheduled syncs. Defaults to event listener interval when omitted.                                              | 120                         | â       |
| `sendRawDataExamples`            | Send sample payloads for easier mapping.                                                                                        | true                        | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

To run the integration using Docker for a one-time sync:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_OPENAI_API_KEY`.

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://api.openai.com/v1" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="bearer_token" \
  -e OCEAN__INTEGRATION__CONFIG__API_TOKEN="YOUR_OPENAI_API_KEY" \
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

Before syncing data, create the blueprints that define your OpenAI entities (usage metrics and available models).

**To create the blueprints:**

1. Go to your [Builder page](https://app.getport.io/settings/data-model).

2. Click the `+ Blueprint` button.

3. Copy each blueprint JSON from the sections below.

   **OpenAI daily usage blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "openai_daily_usage",
     "title": "OpenAI Daily Usage",
     "icon": "OpenAI",
     "schema": {
       "properties": {
         "date": {
           "type": "string",
           "format": "date",
           "title": "Date"
         },
         "total_requests": {
           "type": "number",
           "title": "Total Requests"
         },
         "total_tokens": {
           "type": "number",
           "title": "Total Tokens"
         },
         "total_cost": {
           "type": "number",
           "title": "Total Cost (USD)"
         }
       },
       "required": [
         "date"
       ]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **OpenAI model usage blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "openai_model_usage",
     "title": "OpenAI Model Usage",
     "icon": "OpenAI",
     "schema": {
       "properties": {
         "model": {
           "type": "string",
           "title": "Model Name"
         },
         "date": {
           "type": "string",
           "format": "date",
           "title": "Date"
         },
         "requests": {
           "type": "number",
           "title": "Requests"
         },
         "tokens": {
           "type": "number",
           "title": "Tokens Used"
         }
       },
       "required": [
         "model",
         "date"
       ]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **OpenAI Model blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "openai_model",
     "title": "OpenAI Model",
     "icon": "Claude",
     "schema": {
       "properties": {
         "modelId": {
           "type": "string",
           "title": "Model ID"
         },
         "object": {
           "type": "string",
           "title": "Object Type"
         },
         "created": {
           "type": "number",
           "title": "Created Timestamp"
         },
         "ownedBy": {
           "type": "string",
           "title": "Owned By"
         },
         "permission": {
           "type": "array",
           "title": "Permissions"
         }
       },
       "required": [
         "modelId"
       ]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

4. Click `Save` after each blueprint is added.

## Configuration[â](#configuration "Direct link to Configuration")

Each resource maps an OpenAI endpoint to the Port entities defined above.

**Key mapping components:**

* **`kind`** â API endpoint path appended to `https://api.openai.com/v1`.
* **`selector`** â Request payload, pagination controls, and data selection logic.
* **`port.entity.mappings`** â JQ expressions that transform the API payload into Port entities.

**Daily usage summary mapping (Click to expand)**

```
resources:
  - kind: /dashboard/billing/usage
    selector:
      query: 'true'
      query_params:
        start_date: '((now | floor) - (86400 * 30)) | strftime("%Y-%m-%d")'
        end_date: '(now | floor) | strftime("%Y-%m-%d")'
    port:
      entity:
        mappings:
          identifier: "daily-" + (.timestamp // .aggregation_timestamp // "unknown")
          title: "OpenAI Usage " + (.timestamp // .aggregation_timestamp // "unknown")
          blueprint: '"openai_daily_usage"'
          properties:
            date: (.timestamp // .aggregation_timestamp // "" | split("T")[0])
            total_requests: .total_requests // 0
            total_tokens: .total_tokens // 0
            total_cost: (.total_usage // 0) / 100
```

Cost units

`/dashboard/billing/usage` returns costs in cents. Divide by `100` to store USD.

**Model usage breakdown mapping (Click to expand)**

```
resources:
  - kind: /usage
    selector:
      query: 'true'
      query_params:
        date: '(now | floor) | strftime("%Y-%m-%d")'
    port:
      entity:
        mappings:
          identifier: .snapshot_id + "-" + ((.aggregation_timestamp // 0) | tostring)
          title: .snapshot_id + " usage"
          blueprint: '"openai_model_usage"'
          properties:
            model: .snapshot_id
            date: (.aggregation_timestamp // 0 | strftime("%Y-%m-%d"))
            requests: .n_requests // 0
            tokens: (.n_context_tokens_total // 0) + (.n_generated_tokens_total // 0)
```

Snapshot identifiers

`snapshot_id` typically corresponds to the model name (for example, `gpt-4o`). Use it for both the identifier and the model property to keep the mapping simple.

**OpenAI Models mapping (Click to expand)**

```
resources:
  - kind: /models
    selector:
      query: 'true'
      data_path: '.data'
    port:
      entity:
        mappings:
          identifier: .id
          title: .id
          blueprint: '"openai_model"'
          properties:
            modelId: .id
            object: .object
            ownedBy: .owned_by
            permission: .permission
```

Models endpoint

The `/models` endpoint returns a list of all available OpenAI models. This is useful for cataloging which models are available in your account and tracking model availability over time.

5. Click `Save` to persist the mapping.

## Customization[â](#customization "Direct link to Customization")

If you want to expand beyond the starter resources, use the [interactive builder](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration.md) to:

1. Test additional OpenAI endpoints.
2. Explore the response shape and detected property types.
3. Generate blueprint JSON and mapping snippets automatically.
4. Export installation commands with your configuration pre-filled.

Start with the daily and model usage entities above, then add more resources (such as per-organization or per-team reports) once you verify the value.
