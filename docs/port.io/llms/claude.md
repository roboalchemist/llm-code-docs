# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/ai-agents/claude.md

# Claude AI

Custom Ocean integration

This integration was created using the [custom Ocean integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) builder.<br /><!-- -->Please note that:

1. This integration will not be listed in the `Data sources` page of your Port application, and must be installed manually using the instructions on this page.
2. This integration will not create components (e.g. `blueprints`, `mapping`, etc.) in your portal automatically, you will need to create them manually using the instructions on this page.

Port's Claude AI integration allows you to ingest Claude API usage metrics into your software catalog using the [Ocean Custom Integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) framework. After installing the integration, you can create dashboards to monitor API usage, track costs, analyze model performance, and measure workspace-level metrics using Port's dashboard widgets.

![](/img/ai-agents/claudeDashboard.png)

## Supported metrics[â](#supported-metrics "Direct link to Supported metrics")

The Claude AI integration can ingest usage metrics from the [Anthropic Admin API](https://docs.anthropic.com/en/api/admin-api) into Port. The Admin API provides two distinct types of usage tracking:

### Claude API usage (programmatic)[â](#claude-api-usage-programmatic "Direct link to Claude API usage (programmatic)")

These endpoints track usage from programmatic API calls made with API keys:

* `claude_usage_record` - Daily usage metrics from `/v1/organizations/usage_report/messages` including token consumption (uncached input, output, cache read, cache creation) and web search requests.
* `claude_cost_record` - Cost tracking from `/v1/organizations/cost_report` for monitoring organizational spending.
* `claude_workspace_usage` - Usage metrics grouped by `workspace_id`.
* `claude_model_usage` - Usage metrics grouped by `model`.

### Claude Code usage (CLI/IDE)[â](#claude-code-usage-cliide "Direct link to Claude Code usage (CLI/IDE)")

This endpoint tracks usage from the Claude Code CLI and IDE extensions:

* `claude_code_analytics` - Claude Code usage metrics from `/v1/organizations/usage_report/claude_code` including sessions, lines of code added/removed, commits, pull requests, tool actions, and per-actor breakdowns.

Important distinctions

* **API usage** tracks programmatic calls made via API keys (e.g., applications calling the Messages API).
* **Claude Code usage** tracks developer activity through the Claude Code CLI or IDE extensions.
* **Web console usage** (Claude.ai) is included in API usage metrics.
* The Anthropic Admin API does not provide request counts (success/failure) - only token consumption metrics are available.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To use this integration, you need:

* An [Anthropic Admin API key](https://docs.anthropic.com/en/api/admin-api) generated from the Admin section of the Anthropic Console.
* The API key should have permissions to read usage data and billing information.

## API limitations[â](#api-limitations "Direct link to API limitations")

The Anthropic Admin API has the following constraints that affect how you configure the integration:

| Constraint             | Details                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `starting_at` required | All usage and cost endpoints require a `starting_at` date parameter.                                                     |
| Daily bucket limit     | When using `bucket_width=1d`, the maximum `limit` is 31 days per request.                                                |
| Date format            | Messages and cost endpoints use RFC 3339 format (`2026-01-01T00:00:00Z`). Claude Code endpoint uses `YYYY-MM-DD` format. |
| Pagination             | Large datasets require handling `has_more` and `next_page` tokens for complete data retrieval.                           |
| No request counts      | The API does not provide request success/failure counts - only token consumption metrics.                                |
| No organization info   | Usage responses do not include `organization_id` or `organization_name` fields.                                          |
| Grouping fields        | Fields like `workspace_id`, `model`, `api_key_id` are only populated when using corresponding `group_by[]` parameters.   |

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

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_ANTHROPIC_ADMIN_API_KEY`.

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install my-ocean-claude-integration port-labs/port-ocean \
  --set port.clientId="YOUR_PORT_CLIENT_ID" \
  --set port.clientSecret="YOUR_PORT_CLIENT_SECRET" \
  --set port.baseUrl="https://api.port.io" \
  --set initializePortResources=true \
  --set scheduledResyncInterval=120 \
  --set integration.identifier="my-ocean-claude-integration" \
  --set integration.type="custom" \
  --set integration.eventListener.type="POLLING" \
  --set integration.config.baseUrl="https://api.anthropic.com" \
  --set integration.config.authType="api_key" \
  --set integration.config.apiKeyHeader="x-api-key" \
  --set integration.secrets.apiKey="YOUR_ANTHROPIC_ADMIN_API_KEY"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Configuration parameters

This table summarizes the available parameters for the installation.

| Parameter                         | Description                                                                                                                                                                                                                                    | Example                     | Required |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------- |
| `port.clientId`                   | Your Port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials).                                                                                                                    |                             | â       |
| `port.clientSecret`               | Your Port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials).                                                                                                                |                             | â       |
| `port.baseUrl`                    | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US.                                                                                                                                                             |                             | â       |
| `integration.config.baseUrl`      | The base URL of the Anthropic API.                                                                                                                                                                                                             | <https://api.anthropic.com> | â       |
| `integration.config.authType`     | The authentication type for the API (use `api_key` for Anthropic).                                                                                                                                                                             | api\_key                    | â       |
| `integration.config.apiKeyHeader` | The header name for the API key authentication.                                                                                                                                                                                                | x-api-key                   | â       |
| `integration.secrets.apiKey`      | Your Anthropic Admin API key from the Anthropic Console.                                                                                                                                                                                       | sk-ant-admin01-...          | â       |
| `integration.eventListener.type`  | The event listener type. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener).                                                                                                                        | POLLING                     | â       |
| `integration.type`                | The integration type (must be `custom` for Ocean Custom Integration).                                                                                                                                                                          | custom                      | â       |
| `integration.identifier`          | Unique identifier for the integration instance.                                                                                                                                                                                                | my-ocean-claude-integration | â       |
| `scheduledResyncInterval`         | The number of minutes between each resync. When not set the integration will resync for each event listener resync event. Read more about [scheduledResyncInterval](https://ocean.port.io/developing-an-integration/trigger-your-integration). | 120                         | â       |
| `initializePortResources`         | Default true. When set to true the integration will create default blueprints and the port App config Mapping.                                                                                                                                 | true                        | â       |
| `sendRawDataExamples`             | Enable sending raw data examples from the third party API to Port for testing and managing the integration mapping. Default is true.                                                                                                           | true                        | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

To run the integration using Docker for a one-time sync:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_ANTHROPIC_ADMIN_API_KEY`.

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://api.anthropic.com" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="api_key" \
  -e OCEAN__INTEGRATION__CONFIG__API_KEY_HEADER="x-api-key" \
  -e OCEAN__INTEGRATION__SECRETS__API_KEY="YOUR_ANTHROPIC_ADMIN_API_KEY" \
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

Before the integration can sync data, you need to create the required blueprints in Port. These blueprints define the data model for your Claude metrics.

**To create the blueprints:**

1. Go to your [Builder page](https://app.getport.io/settings/data-model).

2. Click on the `+ Blueprint` button.

3. Copy and paste each blueprint JSON from the sections below.

   **Claude AI usage record blueprint (click to expand)**

   Daily usage metrics from the Messages API:

   Create in Port

   ```
   {
     "identifier": "claude_usage_record",
     "description": "Daily Claude AI API usage metrics",
     "title": "Claude AI Usage Record",
     "icon": "Claude",
     "schema": {
       "properties": {
         "record_date": {
           "type": "string",
           "format": "date-time",
           "title": "Record Date (UTC)"
         },
         "uncached_input_tokens": {
           "type": "number",
           "title": "Uncached Input Tokens"
         },
         "output_tokens": {
           "type": "number",
           "title": "Output Tokens"
         },
         "cache_read_input_tokens": {
           "type": "number",
           "title": "Cache Read Input Tokens"
         },
         "cache_creation_5m_tokens": {
           "type": "number",
           "title": "Cache Creation (5min) Tokens"
         },
         "cache_creation_1h_tokens": {
           "type": "number",
           "title": "Cache Creation (1hr) Tokens"
         },
         "web_search_requests": {
           "type": "number",
           "title": "Web Search Requests"
         }
       },
       "required": ["record_date"]
     },
     "mirrorProperties": {},
     "calculationProperties": {
       "total_input_tokens": {
         "title": "Total Input Tokens",
         "description": "Sum of uncached input and cache read tokens",
         "calculation": ".properties.uncached_input_tokens + .properties.cache_read_input_tokens",
         "type": "number"
       },
       "total_tokens": {
         "title": "Total Tokens",
         "description": "Sum of all input and output tokens",
         "calculation": ".properties.uncached_input_tokens + .properties.cache_read_input_tokens + .properties.output_tokens",
         "type": "number"
       }
     },
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Claude AI cost record blueprint (click to expand)**

   Cost tracking for organizational spending:

   Create in Port

   ```
   {
     "identifier": "claude_cost_record",
     "description": "Daily cost tracking for Claude API usage",
     "title": "Claude AI Cost Record",
     "icon": "Claude",
     "schema": {
       "properties": {
         "record_date": {
           "type": "string",
           "format": "date-time",
           "title": "Record Date (UTC)"
         },
         "amount": {
           "type": "number",
           "title": "Cost Amount"
         },
         "currency": {
           "type": "string",
           "title": "Currency"
         }
       },
       "required": ["record_date"]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Claude AI workspace usage blueprint (click to expand)**

   Usage metrics grouped by workspace:

   Create in Port

   ```
   {
     "identifier": "claude_workspace_usage",
     "description": "Usage metrics broken down by workspace",
     "title": "Claude AI Workspace Usage",
     "icon": "Claude",
     "schema": {
       "properties": {
         "record_date": {
           "type": "string",
           "format": "date-time",
           "title": "Record Date (UTC)"
         },
         "workspace_id": {
           "type": "string",
           "title": "Workspace ID"
         },
         "uncached_input_tokens": {
           "type": "number",
           "title": "Uncached Input Tokens"
         },
         "output_tokens": {
           "type": "number",
           "title": "Output Tokens"
         },
         "cache_read_input_tokens": {
           "type": "number",
           "title": "Cache Read Input Tokens"
         },
         "cache_creation_5m_tokens": {
           "type": "number",
           "title": "Cache Creation (5min) Tokens"
         },
         "cache_creation_1h_tokens": {
           "type": "number",
           "title": "Cache Creation (1hr) Tokens"
         },
         "web_search_requests": {
           "type": "number",
           "title": "Web Search Requests"
         }
       },
       "required": ["record_date", "workspace_id"]
     },
     "mirrorProperties": {},
     "calculationProperties": {
       "total_tokens": {
         "title": "Total Tokens",
         "calculation": ".properties.uncached_input_tokens + .properties.cache_read_input_tokens + .properties.output_tokens",
         "type": "number"
       }
     },
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Claude AI model usage blueprint (click to expand)**

   Usage metrics grouped by model:

   Create in Port

   ```
   {
     "identifier": "claude_model_usage",
     "description": "Usage metrics broken down by Claude model type",
     "title": "Claude AI Model Usage",
     "icon": "Claude",
     "schema": {
       "properties": {
         "record_date": {
           "type": "string",
           "format": "date-time",
           "title": "Record Date (UTC)"
         },
         "model": {
           "type": "string",
           "title": "Model"
         },
         "uncached_input_tokens": {
           "type": "number",
           "title": "Uncached Input Tokens"
         },
         "output_tokens": {
           "type": "number",
           "title": "Output Tokens"
         },
         "cache_read_input_tokens": {
           "type": "number",
           "title": "Cache Read Input Tokens"
         },
         "cache_creation_5m_tokens": {
           "type": "number",
           "title": "Cache Creation (5min) Tokens"
         },
         "cache_creation_1h_tokens": {
           "type": "number",
           "title": "Cache Creation (1hr) Tokens"
         },
         "web_search_requests": {
           "type": "number",
           "title": "Web Search Requests"
         }
       },
       "required": ["record_date", "model"]
     },
     "mirrorProperties": {},
     "calculationProperties": {
       "total_tokens": {
         "title": "Total Tokens",
         "calculation": ".properties.uncached_input_tokens + .properties.cache_read_input_tokens + .properties.output_tokens",
         "type": "number"
       }
     },
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Claude Code analytics blueprint (click to expand)**

   Claude Code usage metrics for tracking development activity:

   Create in Port

   ```
   {
     "identifier": "claude_code_analytics",
     "description": "Daily Claude Code usage metrics including sessions, lines of code, commits, and PRs",
     "title": "Claude Code Analytics",
     "icon": "Claude",
     "schema": {
       "properties": {
         "record_date": {
           "type": "string",
           "format": "date-time",
           "title": "Record Date (UTC)"
         },
         "organization_id": {
           "type": "string",
           "title": "Organization ID"
         },
         "actor_type": {
           "type": "string",
           "title": "Actor Type"
         },
         "actor_name": {
           "type": "string",
           "title": "Actor Name"
         },
         "terminal_type": {
           "type": "string",
           "title": "Terminal Type"
         },
         "num_sessions": {
           "type": "number",
           "title": "Sessions"
         },
         "lines_added": {
           "type": "number",
           "title": "Lines Added"
         },
         "lines_removed": {
           "type": "number",
           "title": "Lines Removed"
         },
         "commits": {
           "type": "number",
           "title": "Commits by Claude Code"
         },
         "pull_requests": {
           "type": "number",
           "title": "Pull Requests by Claude Code"
         },
         "edit_tool_accepted": {
           "type": "number",
           "title": "Edit Tool Accepted"
         },
         "edit_tool_rejected": {
           "type": "number",
           "title": "Edit Tool Rejected"
         },
         "write_tool_accepted": {
           "type": "number",
           "title": "Write Tool Accepted"
         },
         "write_tool_rejected": {
           "type": "number",
           "title": "Write Tool Rejected"
         },
         "model_breakdown": {
           "type": "array",
           "title": "Model Breakdown"
         }
       },
       "required": ["record_date", "organization_id"]
     },
     "mirrorProperties": {},
     "calculationProperties": {
       "total_lines_changed": {
         "title": "Total Lines Changed",
         "calculation": ".properties.lines_added + .properties.lines_removed",
         "type": "number"
       },
       "edit_acceptance_rate": {
         "title": "Edit Acceptance Rate",
         "calculation": "if (.properties.edit_tool_accepted + .properties.edit_tool_rejected) > 0 then (.properties.edit_tool_accepted / (.properties.edit_tool_accepted + .properties.edit_tool_rejected)) * 100 else 0 end",
         "type": "number"
       }
     },
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

2. Find your Claude AI integration in the list.

3. Click on the integration to open the mapping editor.

4. Add the resource mapping configurations below.

   **Organization usage metrics mapping (click to expand)**

   This endpoint provides detailed usage metrics including token consumption:

   ```
   resources:
     - kind: /v1/organizations/usage_report/messages
       selector:
         query: 'true'
         method: GET
         headers:
           anthropic-version: "2023-06-01"
         query_params:
           starting_at: "2025-01-01T00:00:00Z"
           bucket_width: "1d"
         data_path: .data[]
       port:
         entity:
           mappings:
             identifier: .starting_at[:10] + "-usage"
             title: '"Claude Usage - " + .starting_at[:10]'
             blueprint: '"claude_usage_record"'
             properties:
               record_date: .starting_at
               uncached_input_tokens: (.results[0].uncached_input_tokens // 0)
               output_tokens: (.results[0].output_tokens // 0)
               cache_read_input_tokens: (.results[0].cache_read_input_tokens // 0)
               cache_creation_5m_tokens: (.results[0].cache_creation.ephemeral_5m_input_tokens // 0)
               cache_creation_1h_tokens: (.results[0].cache_creation.ephemeral_1h_input_tokens // 0)
               web_search_requests: (.results[0].server_tool_use.web_search_requests // 0)
   ```

   Response structure

   The API returns data in daily buckets. Each bucket has `starting_at`, `ending_at`, and a `results[]` array. Days with no usage will have an empty `results` array.

   **Date range:** Replace `starting_at` with your desired start date. The API requires this parameter and returns a maximum of 31 days per request with daily buckets.

   **Pagination:** For date ranges exceeding 31 days, use the `next_page` token from the response to fetch additional data.

   **Cost report mapping (click to expand)**

   This endpoint provides cost data for monitoring organizational spending:

   ```
   resources:
     - kind: /v1/organizations/cost_report
       selector:
         query: 'true'
         method: GET
         headers:
           anthropic-version: "2023-06-01"
         query_params:
           starting_at: "2025-01-01T00:00:00Z"
           bucket_width: "1d"
         data_path: .data[]
       port:
         entity:
           mappings:
             identifier: .starting_at[:10] + "-cost"
             title: '"Claude Cost - " + .starting_at[:10]'
             blueprint: '"claude_cost_record"'
             properties:
               record_date: .starting_at
               amount: ((.results[0].amount // "0") | tonumber)
               currency: (.results[0].currency // "USD")
   ```

   Cost data format

   The API returns cost amounts as strings (e.g., `"0.057"`). The mapping converts this to a number using `tonumber`.

   **Workspace-level usage metrics mapping (click to expand)**

   Track usage metrics at the workspace level by grouping the usage report by `workspace_id`:

   ```
   resources:
     - kind: /v1/organizations/usage_report/messages
       selector:
         query: 'true'
         method: GET
         headers:
           anthropic-version: "2023-06-01"
         query_params:
           starting_at: "2025-01-01T00:00:00Z"
           bucket_width: "1d"
           group_by[]: "workspace_id"
         data_path: '.data[] | select(.results | length > 0) | . as $bucket | .results[] | . + {bucket_date: $bucket.starting_at}'
       port:
         entity:
           mappings:
             identifier: (.workspace_id // "default") + "-" + .bucket_date[:10]
             title: (.workspace_id // "default") + " - " + .bucket_date[:10]
             blueprint: '"claude_workspace_usage"'
             properties:
               record_date: .bucket_date
               workspace_id: (.workspace_id // "default")
               uncached_input_tokens: (.uncached_input_tokens // 0)
               output_tokens: (.output_tokens // 0)
               cache_read_input_tokens: (.cache_read_input_tokens // 0)
               cache_creation_5m_tokens: (.cache_creation.ephemeral_5m_input_tokens // 0)
               cache_creation_1h_tokens: (.cache_creation.ephemeral_1h_input_tokens // 0)
               web_search_requests: (.server_tool_use.web_search_requests // 0)
   ```

   Workspace grouping

   When using `group_by[]=workspace_id`, results are broken down per workspace within each daily bucket. The `data_path` uses JQ to:

   * Filter out buckets with empty results using `select(.results | length > 0)`.

   * Store the bucket in a variable `$bucket` to preserve the date.

   * Flatten results and inject `bucket_date` from the parent bucket.

   Usage not associated with a workspace will have `workspace_id: null`.

   **Model-level usage metrics mapping (click to expand)**

   Track usage metrics at the model level by grouping the usage report by `model`:

   ```
   resources:
     - kind: /v1/organizations/usage_report/messages
       selector:
         query: 'true'
         method: GET
         headers:
           anthropic-version: "2023-06-01"
         query_params:
           starting_at: "2025-01-01T00:00:00Z"
           bucket_width: "1d"
           group_by[]: "model"
         data_path: '.data[] | select(.results | length > 0) | . as $bucket | .results[] | . + {bucket_date: $bucket.starting_at}'
       port:
         entity:
           mappings:
             identifier: .model + "-" + .bucket_date[:10]
             title: .model + " - " + .bucket_date[:10]
             blueprint: '"claude_model_usage"'
             properties:
               record_date: .bucket_date
               model: .model
               uncached_input_tokens: (.uncached_input_tokens // 0)
               output_tokens: (.output_tokens // 0)
               cache_read_input_tokens: (.cache_read_input_tokens // 0)
               cache_creation_5m_tokens: (.cache_creation.ephemeral_5m_input_tokens // 0)
               cache_creation_1h_tokens: (.cache_creation.ephemeral_1h_input_tokens // 0)
               web_search_requests: (.server_tool_use.web_search_requests // 0)
   ```

   Model grouping

   When using `group_by[]=model`, results show token usage per model (e.g., `claude-opus-4-5-20251101`, `claude-haiku-4-5-20251001`). The `data_path` uses JQ to:

   * Filter out buckets with empty results using `select(.results | length > 0)`.
   * Store the bucket in a variable `$bucket` to preserve the date.
   * Flatten results and inject `bucket_date` from the parent bucket.

   **Claude Code analytics mapping (click to expand)**

   Track Claude Code usage metrics including sessions, lines of code, commits, and pull requests:

   Requires Claude Code access

   This endpoint requires access to Claude Code. You'll receive an error if your organization doesn't have Claude Code enabled.

   ```
   resources:
     - kind: /v1/organizations/usage_report/claude_code
       selector:
         query: 'true'
         method: GET
         headers:
           anthropic-version: "2023-06-01"
         query_params:
           starting_at: "2025-01-01"
         data_path: .data[]
       port:
         entity:
           mappings:
             identifier: .organization_id + "-" + (.actor.api_key_name // .actor.email // "unknown") + "-" + .date[:10]
             title: (.actor.api_key_name // .actor.email // "unknown") + " - " + .date[:10]
             blueprint: '"claude_code_analytics"'
             properties:
               record_date: .date
               organization_id: .organization_id
               actor_type: .actor.type
               actor_name: (.actor.api_key_name // .actor.email // "unknown")
               terminal_type: .terminal_type
               num_sessions: (.core_metrics.num_sessions // 0)
               lines_added: (.core_metrics.lines_of_code.added // 0)
               lines_removed: (.core_metrics.lines_of_code.removed // 0)
               commits: (.core_metrics.commits_by_claude_code // 0)
               pull_requests: (.core_metrics.pull_requests_by_claude_code // 0)
               edit_tool_accepted: (.tool_actions.edit_tool.accepted // 0)
               edit_tool_rejected: (.tool_actions.edit_tool.rejected // 0)
               write_tool_accepted: (.tool_actions.write_tool.accepted // 0)
               write_tool_rejected: (.tool_actions.write_tool.rejected // 0)
               model_breakdown: .model_breakdown
   ```

   Claude Code response structure

   The Claude Code endpoint returns per-actor records. Each record includes:

   * **Actor**: Either a user (with email) or an API key (with name).

   * **Core metrics**: Sessions, lines of code, commits, and pull requests.

   * **Tool actions**: Acceptance/rejection counts for edit and write tools.

   * **Model breakdown**: Token usage and estimated cost per model.

   **Date format:** This endpoint uses `YYYY-MM-DD` format (not RFC 3339).

5. Click `Save` to save the mapping.

## Customization[â](#customization "Direct link to Customization")

If you want to customize your setup or test different API endpoints before committing to a configuration, use the [interactive builder](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration.md).

**The interactive builder helps you:**

1. Test your Claude API endpoints with live data.
2. Automatically detect the data structure and field types.
3. Generate blueprints and resource mappings tailored to your preferences.
4. Get installation commands with your configuration pre-filled.

Simply provide your Anthropic API details, and the builder will generate everything you need to install and create the integration in Port.

## Related guide[â](#related-guide "Direct link to Related guide")

* [Visualize Claude metrics](/guides/all/visualize-claude-metrics.md)
