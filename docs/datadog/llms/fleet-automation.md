# Source: https://docs.datadoghq.com/api/latest/fleet-automation.md

---
title: Fleet Automation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Fleet Automation
---

# Fleet Automation

Manage automated deployments across your fleet of hosts.

Fleet Automation provides two types of deployments:

Configuration Deployments (`/configure`):

- Apply configuration file changes to target hosts
- Support merge-patch operations to update specific configuration fields
- Support delete operations to remove configuration files
- Useful for updating Datadog Agent settings, integration configs, and more

Package Upgrade Deployments (`/upgrade`):

- Upgrade the Datadog Agent to specific versions

## List all available Agent versions{% #list-all-available-agent-versions %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/unstable/fleet/agent_versions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/unstable/fleet/agent_versions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/unstable/fleet/agent_versions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/unstable/fleet/agent_versions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/unstable/fleet/agent_versions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/unstable/fleet/agent_versions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/unstable/fleet/agent_versions |

### Overview



Retrieve a list of all available Datadog Agent versions.

This endpoint returns the available Agent versions that can be deployed to your fleet. These versions are used when creating deployments or configuring schedules for automated Agent upgrades.
This endpoint requires the `hosts_read` permission.


### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of available Agent versions.

| Parent field | Field                  | Type     | Description                                                              |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------------ |
|              | data [*required*] | [object] | Array of available Agent versions.                                       |
| data         | attributes             | object   |
| attributes   | version                | string   | The Agent version string.                                                |
| data         | id [*required*]   | string   | Unique identifier for the Agent version (same as version).               |
| data         | type [*required*] | enum     | The type of Agent version resource. Allowed enum values: `agent_version` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "version": "7.50.0"
      },
      "id": "7.50.0",
      "type": "agent_version"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/agent_versions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List all available Agent versions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["list_fleet_agent_versions"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.list_fleet_agent_versions()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List all available Agent versions returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_fleet_agent_versions".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.list_fleet_agent_versions()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List all available Agent versions returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListFleetAgentVersions", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.ListFleetAgentVersions(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.ListFleetAgentVersions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.ListFleetAgentVersions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List all available Agent versions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetAgentVersionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listFleetAgentVersions", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetAgentVersionsResponse result = apiInstance.listFleetAgentVersions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#listFleetAgentVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List all available Agent versions returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListFleetAgentVersions", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.list_fleet_agent_versions().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List all available Agent versions returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listFleetAgentVersions"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

apiInstance
  .listFleetAgentVersions()
  .then((data: v2.FleetAgentVersionsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List all Datadog Agents{% #list-all-datadog-agents %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/unstable/fleet/agents |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/unstable/fleet/agents |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/unstable/fleet/agents      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/unstable/fleet/agents      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/unstable/fleet/agents     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/unstable/fleet/agents |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/unstable/fleet/agents |

### Overview

Retrieve a paginated list of all Datadog Agents. This endpoint returns a paginated list of all Datadog Agents with support for pagination, sorting, and filtering. Use the `page_number` and `page_size` query parameters to paginate through results. This endpoint requires the `hosts_read` permission.

### Arguments

#### Query Strings

| Name            | Type    | Description                                                                        |
| --------------- | ------- | ---------------------------------------------------------------------------------- |
| page_number     | integer | Page number for pagination (starts at 0).                                          |
| page_size       | integer | Number of results per page (must be greater than 0 and less than or equal to 100). |
| sort_attribute  | string  | Attribute to sort by.                                                              |
| sort_descending | boolean | Sort order (true for descending, false for ascending).                             |
| tags            | string  | Comma-separated list of tags to filter agents.                                     |
| filter          | string  | Filter string for narrowing down agent results.                                    |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a paginated list of Datadog Agents.

| Parent field | Field                                  | Type     | Description                                                           |
| ------------ | -------------------------------------- | -------- | --------------------------------------------------------------------- |
|              | data [*required*]                 | object   | The response data containing status and agents array.                 |
| data         | attributes [*required*]           | object   |
| attributes   | agents                                 | [object] | Array of agents matching the query criteria.                          |
| agents       | agent_version                          | string   | The Datadog Agent version.                                            |
| agents       | api_key_name                           | string   | The API key name (if available and not redacted).                     |
| agents       | api_key_uuid                           | string   | The API key UUID.                                                     |
| agents       | cloud_provider                         | string   | The cloud provider where the agent is running.                        |
| agents       | cluster_name                           | string   | Kubernetes cluster name (if applicable).                              |
| agents       | datadog_agent_key                      | string   | The unique agent key identifier.                                      |
| agents       | enabled_products                       | [string] | Datadog products enabled on the agent.                                |
| agents       | envs                                   | [string] | Environments the agent is reporting from.                             |
| agents       | first_seen_at                          | int64    | Timestamp when the agent was first seen.                              |
| agents       | hostname                               | string   | The hostname of the agent.                                            |
| agents       | ip_addresses                           | [string] | IP addresses of the agent.                                            |
| agents       | is_single_step_instrumentation_enabled | boolean  | Whether single-step instrumentation is enabled.                       |
| agents       | last_restart_at                        | int64    | Timestamp of the last agent restart.                                  |
| agents       | os                                     | string   | The operating system.                                                 |
| agents       | otel_collector_version                 | string   | OpenTelemetry collector version (if applicable).                      |
| agents       | otel_collector_versions                | [string] | List of OpenTelemetry collector versions (if applicable).             |
| agents       | pod_name                               | string   | Kubernetes pod name (if applicable).                                  |
| agents       | remote_agent_management                | string   | Remote agent management status.                                       |
| agents       | remote_config_status                   | string   | Remote configuration status.                                          |
| agents       | services                               | [string] | Services running on the agent.                                        |
| agents       | tags                                   | [object] | Tags associated with the agent.                                       |
| tags         | key                                    | string   |
| tags         | value                                  | string   |
| agents       | team                                   | string   | Team associated with the agent.                                       |
| data         | id [*required*]                   | string   | Status identifier.                                                    |
| data         | type [*required*]                 | string   | Resource type.                                                        |
|              | meta                                   | object   | Metadata for the list of agents response.                             |
| meta         | total_filtered_count                   | int64    | Total number of agents matching the filter criteria across all pages. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "agents": [
        {
          "agent_version": "7.50.0",
          "api_key_name": "Production API Key",
          "api_key_uuid": "a1b2c3d4-e5f6-4321-a123-123456789abc",
          "cloud_provider": "aws",
          "cluster_name": "string",
          "datadog_agent_key": "my-agent-hostname",
          "enabled_products": [],
          "envs": [],
          "first_seen_at": "integer",
          "hostname": "my-hostname",
          "ip_addresses": [],
          "is_single_step_instrumentation_enabled": false,
          "last_restart_at": "integer",
          "os": "linux",
          "otel_collector_version": "string",
          "otel_collector_versions": [],
          "pod_name": "string",
          "remote_agent_management": "enabled",
          "remote_config_status": "connected",
          "services": [],
          "tags": [
            {
              "key": "string",
              "value": "string"
            }
          ],
          "team": "string"
        }
      ]
    },
    "id": "done",
    "type": "status"
  },
  "meta": {
    "total_filtered_count": 150
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/agents" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List all Datadog Agents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["list_fleet_agents"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.list_fleet_agents()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List all Datadog Agents returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_fleet_agents".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.list_fleet_agents()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List all Datadog Agents returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListFleetAgents", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.ListFleetAgents(ctx, *datadogV2.NewListFleetAgentsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.ListFleetAgents`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.ListFleetAgents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List all Datadog Agents returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetAgentsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listFleetAgents", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetAgentsResponse result = apiInstance.listFleetAgents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#listFleetAgents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List all Datadog Agents returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;
use datadog_api_client::datadogV2::api_fleet_automation::ListFleetAgentsOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListFleetAgents", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api
        .list_fleet_agents(ListFleetAgentsOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List all Datadog Agents returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listFleetAgents"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

apiInstance
  .listFleetAgents()
  .then((data: v2.FleetAgentsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get detailed information about an agent{% #get-detailed-information-about-an-agent %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/unstable/fleet/agents/{agent_key} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/unstable/fleet/agents/{agent_key} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/unstable/fleet/agents/{agent_key}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/unstable/fleet/agents/{agent_key}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/unstable/fleet/agents/{agent_key}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/unstable/fleet/agents/{agent_key} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/unstable/fleet/agents/{agent_key} |

### Overview



Retrieve detailed information about a specific Datadog Agent. This endpoint returns comprehensive information about an agent including:

- Agent details and metadata
- Configured integrations organized by status (working, warning, error, missing)
- Detected integrations
- Configuration files and layers
This endpoint requires the `hosts_read` permission.


### Arguments

#### Path Parameters

| Name                        | Type   | Description                                              |
| --------------------------- | ------ | -------------------------------------------------------- |
| agent_key [*required*] | string | The unique identifier (agent key) for the Datadog Agent. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing detailed information about a specific agent.

| Parent field          | Field                                  | Type     | Description                                                               |
| --------------------- | -------------------------------------- | -------- | ------------------------------------------------------------------------- |
|                       | data [*required*]                 | object   | Represents detailed information about a specific Datadog Agent.           |
| data                  | attributes [*required*]           | object   | Attributes for agent information.                                         |
| attributes            | agent_infos                            | object   | Detailed information about a Datadog Agent.                               |
| agent_infos           | agent_version                          | string   | The Datadog Agent version.                                                |
| agent_infos           | api_key_name                           | string   | The API key name (if available and not redacted).                         |
| agent_infos           | api_key_uuid                           | string   | The API key UUID.                                                         |
| agent_infos           | cloud_provider                         | string   | The cloud provider where the agent is running.                            |
| agent_infos           | cluster_name                           | string   | Kubernetes cluster name (if applicable).                                  |
| agent_infos           | datadog_agent_key                      | string   | The unique agent key identifier.                                          |
| agent_infos           | enabled_products                       | [string] | Datadog products enabled on the agent.                                    |
| agent_infos           | env                                    | [string] | Environments the agent is reporting from.                                 |
| agent_infos           | first_seen_at                          | int64    | Timestamp when the agent was first seen.                                  |
| agent_infos           | hostname                               | string   | The hostname of the agent.                                                |
| agent_infos           | hostname_aliases                       | [string] | Alternative hostname list for the agent.                                  |
| agent_infos           | install_method_installer_version       | string   | The version of the installer used.                                        |
| agent_infos           | install_method_tool                    | string   | The tool used to install the agent.                                       |
| agent_infos           | ip_addresses                           | [string] | IP addresses of the agent.                                                |
| agent_infos           | is_single_step_instrumentation_enabled | boolean  | Whether single-step instrumentation is enabled.                           |
| agent_infos           | last_restart_at                        | int64    | Timestamp of the last agent restart.                                      |
| agent_infos           | os                                     | string   | The operating system.                                                     |
| agent_infos           | os_version                             | string   | The operating system version.                                             |
| agent_infos           | otel_collector_version                 | string   | OpenTelemetry collector version (if applicable).                          |
| agent_infos           | otel_collector_versions                | [string] | List of OpenTelemetry collector versions (if applicable).                 |
| agent_infos           | otel_collectors                        | [object] | OpenTelemetry collectors associated with the agent (if applicable).       |
| agent_infos           | pod_name                               | string   | Kubernetes pod name (if applicable).                                      |
| agent_infos           | python_version                         | string   | The Python version used by the agent.                                     |
| agent_infos           | region                                 | [string] | Regions where the agent is running.                                       |
| agent_infos           | remote_agent_management                | string   | Remote agent management status.                                           |
| agent_infos           | remote_config_status                   | string   | Remote configuration status.                                              |
| agent_infos           | services                               | [string] | Services running on the agent.                                            |
| agent_infos           | tags                                   | [string] | Tags associated with the agent.                                           |
| agent_infos           | team                                   | string   | Team associated with the agent.                                           |
| attributes            | configuration_files                    | object   | Configuration information organized by layers.                            |
| configuration_files   | compiled_configuration                 | string   | The final compiled configuration.                                         |
| configuration_files   | env_configuration                      | string   | Configuration from environment variables.                                 |
| configuration_files   | file_configuration                     | string   | Configuration from files.                                                 |
| configuration_files   | parsed_configuration                   | string   | Parsed configuration output.                                              |
| configuration_files   | remote_configuration                   | string   | Remote configuration settings.                                            |
| configuration_files   | runtime_configuration                  | string   | Runtime configuration.                                                    |
| attributes            | detected_integrations                  | [object] | List of detected integrations.                                            |
| detected_integrations | escaped_name                           | string   | Escaped integration name.                                                 |
| detected_integrations | prefix                                 | string   | Integration prefix identifier.                                            |
| attributes            | integrations                           | object   | Integrations organized by their status.                                   |
| integrations          | configuration_files                    | [object] | Configuration files for integrations.                                     |
| configuration_files   | file_content                           | string   | The raw content of the configuration file.                                |
| configuration_files   | file_path                              | string   | Path to the configuration file.                                           |
| configuration_files   | filename                               | string   | Name of the configuration file.                                           |
| integrations          | datadog_agent_key                      | string   | The unique agent key identifier.                                          |
| integrations          | error_integrations                     | [object] | Integrations with errors.                                                 |
| error_integrations    | data_type                              | string   | Type of data collected (metrics, logs).                                   |
| error_integrations    | error_messages                         | [string] | Error messages if the integration has issues.                             |
| error_integrations    | init_config                            | string   | Initialization configuration (YAML format).                               |
| error_integrations    | instance_config                        | string   | Instance-specific configuration (YAML format).                            |
| error_integrations    | is_custom_check                        | boolean  | Whether this is a custom integration.                                     |
| error_integrations    | log_config                             | string   | Log collection configuration (YAML format).                               |
| error_integrations    | name                                   | string   | Name of the integration instance.                                         |
| error_integrations    | source_index                           | int64    | Index in the configuration file.                                          |
| error_integrations    | source_path                            | string   | Path to the configuration file.                                           |
| error_integrations    | type                                   | string   | Integration type.                                                         |
| integrations          | missing_integrations                   | [object] | Detected but not configured integrations.                                 |
| missing_integrations  | escaped_name                           | string   | Escaped integration name.                                                 |
| missing_integrations  | prefix                                 | string   | Integration prefix identifier.                                            |
| integrations          | warning_integrations                   | [object] | Integrations with warnings.                                               |
| warning_integrations  | data_type                              | string   | Type of data collected (metrics, logs).                                   |
| warning_integrations  | error_messages                         | [string] | Error messages if the integration has issues.                             |
| warning_integrations  | init_config                            | string   | Initialization configuration (YAML format).                               |
| warning_integrations  | instance_config                        | string   | Instance-specific configuration (YAML format).                            |
| warning_integrations  | is_custom_check                        | boolean  | Whether this is a custom integration.                                     |
| warning_integrations  | log_config                             | string   | Log collection configuration (YAML format).                               |
| warning_integrations  | name                                   | string   | Name of the integration instance.                                         |
| warning_integrations  | source_index                           | int64    | Index in the configuration file.                                          |
| warning_integrations  | source_path                            | string   | Path to the configuration file.                                           |
| warning_integrations  | type                                   | string   | Integration type.                                                         |
| integrations          | working_integrations                   | [object] | Integrations that are working correctly.                                  |
| working_integrations  | data_type                              | string   | Type of data collected (metrics, logs).                                   |
| working_integrations  | error_messages                         | [string] | Error messages if the integration has issues.                             |
| working_integrations  | init_config                            | string   | Initialization configuration (YAML format).                               |
| working_integrations  | instance_config                        | string   | Instance-specific configuration (YAML format).                            |
| working_integrations  | is_custom_check                        | boolean  | Whether this is a custom integration.                                     |
| working_integrations  | log_config                             | string   | Log collection configuration (YAML format).                               |
| working_integrations  | name                                   | string   | Name of the integration instance.                                         |
| working_integrations  | source_index                           | int64    | Index in the configuration file.                                          |
| working_integrations  | source_path                            | string   | Path to the configuration file.                                           |
| working_integrations  | type                                   | string   | Integration type.                                                         |
| data                  | id [*required*]                   | string   | The unique agent key identifier.                                          |
| data                  | type [*required*]                 | enum     | The type of Agent info resource. Allowed enum values: `datadog_agent_key` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "agent_infos": {
        "agent_version": "7.50.0",
        "api_key_name": "Production API Key",
        "api_key_uuid": "a1b2c3d4-e5f6-4321-a123-123456789abc",
        "cloud_provider": "aws",
        "cluster_name": "string",
        "datadog_agent_key": "my-agent-hostname",
        "enabled_products": [],
        "env": [],
        "first_seen_at": "integer",
        "hostname": "my-hostname",
        "hostname_aliases": [],
        "install_method_installer_version": "1.2.3",
        "install_method_tool": "chef",
        "ip_addresses": [],
        "is_single_step_instrumentation_enabled": false,
        "last_restart_at": "integer",
        "os": "linux",
        "os_version": "Ubuntu 20.04",
        "otel_collector_version": "string",
        "otel_collector_versions": [],
        "otel_collectors": [],
        "pod_name": "string",
        "python_version": "3.9.5",
        "region": [],
        "remote_agent_management": "enabled",
        "remote_config_status": "connected",
        "services": [],
        "tags": [],
        "team": "string"
      },
      "configuration_files": {
        "compiled_configuration": "string",
        "env_configuration": "string",
        "file_configuration": "string",
        "parsed_configuration": "string",
        "remote_configuration": "string",
        "runtime_configuration": "string"
      },
      "detected_integrations": [
        {
          "escaped_name": "postgresql",
          "prefix": "postgres"
        }
      ],
      "integrations": {
        "configuration_files": [
          {
            "file_content": "string",
            "file_path": "/conf.d/postgres.d/postgres.yaml",
            "filename": "postgres.yaml"
          }
        ],
        "datadog_agent_key": "string",
        "error_integrations": [
          {
            "data_type": "metrics",
            "error_messages": [],
            "init_config": "string",
            "instance_config": "string",
            "is_custom_check": false,
            "log_config": "string",
            "name": "string",
            "source_index": "integer",
            "source_path": "string",
            "type": "postgres"
          }
        ],
        "missing_integrations": [
          {
            "escaped_name": "postgresql",
            "prefix": "postgres"
          }
        ],
        "warning_integrations": [
          {
            "data_type": "metrics",
            "error_messages": [],
            "init_config": "string",
            "instance_config": "string",
            "is_custom_check": false,
            "log_config": "string",
            "name": "string",
            "source_index": "integer",
            "source_path": "string",
            "type": "postgres"
          }
        ],
        "working_integrations": [
          {
            "data_type": "metrics",
            "error_messages": [],
            "init_config": "string",
            "instance_config": "string",
            "is_custom_check": false,
            "log_config": "string",
            "name": "string",
            "source_index": "integer",
            "source_path": "string",
            "type": "postgres"
          }
        ]
      }
    },
    "id": "my-agent-hostname",
    "type": "datadog_agent_key"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport agent_key="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/agents/${agent_key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get detailed information about an agent returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["get_fleet_agent_info"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.get_fleet_agent_info(
        agent_key="agent_key",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get detailed information about an agent returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_fleet_agent_info".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.get_fleet_agent_info("agent_key")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get detailed information about an agent returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetFleetAgentInfo", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.GetFleetAgentInfo(ctx, "agent_key")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.GetFleetAgentInfo`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.GetFleetAgentInfo`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get detailed information about an agent returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetAgentInfoResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getFleetAgentInfo", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetAgentInfoResponse result = apiInstance.getFleetAgentInfo("agent_key");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#getFleetAgentInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Get detailed information about an agent returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetFleetAgentInfo", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.get_fleet_agent_info("agent_key".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get detailed information about an agent returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getFleetAgentInfo"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiGetFleetAgentInfoRequest = {
  agentKey: "agent_key",
};

apiInstance
  .getFleetAgentInfo(params)
  .then((data: v2.FleetAgentInfoResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List all deployments{% #list-all-deployments %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/unstable/fleet/deployments |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/unstable/fleet/deployments |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/unstable/fleet/deployments      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/unstable/fleet/deployments      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/unstable/fleet/deployments     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/unstable/fleet/deployments |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/unstable/fleet/deployments |

### Overview

Retrieve a list of all deployments for fleet automation. Use the `page_size` and `page_offset` parameters to paginate results. This endpoint requires the `hosts_read` permission.

### Arguments

#### Query Strings

| Name        | Type    | Description                                                                                     |
| ----------- | ------- | ----------------------------------------------------------------------------------------------- |
| page_size   | integer | Number of deployments to return per page. Maximum value is 100.                                 |
| page_offset | integer | Index of the first deployment to return. Use this with `page_size` to paginate through results. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a paginated list of deployments.

| Parent field      | Field                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                   | data [*required*]       | [object] | Array of deployments matching the query criteria.                                                                                                                                                                                                                                                                                                                                                                  |
| data              | attributes [*required*] | object   | Attributes of a deployment in the response.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes        | config_operations            | [object] | Ordered list of configuration file operations to perform on the target hosts.                                                                                                                                                                                                                                                                                                                                      |
| config_operations | file_op [*required*]    | enum     | Type of file operation to perform on the target configuration file.                                                                                                                                                                                                                                                                                                                                                |
| config_operations | file_path [*required*]  | string   | Absolute path to the target configuration file on the host.                                                                                                                                                                                                                                                                                                                                                        |
| config_operations | patch                        | object   | Patch data in JSON format to apply to the configuration file. When using `merge-patch`, this object is merged with the existing configuration, allowing you to add, update, or override specific fields without replacing the entire file. The structure must match the target configuration file format (for example, YAML structure for Datadog Agent config). Not applicable when using the `delete` operation. |
| attributes        | estimated_end_time_unix      | int64    | Estimated completion time of the deployment as a Unix timestamp (seconds since epoch).                                                                                                                                                                                                                                                                                                                             |
| attributes        | filter_query                 | string   | Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.                                                                                                                                                                                                                                                                                                                    |
| attributes        | high_level_status            | string   | Current high-level status of the deployment (for example, "pending", "running", "completed", "failed").                                                                                                                                                                                                                                                                                                            |
| attributes        | hosts                        | [object] | Paginated list of hosts in this deployment with their individual statuses. Only included when fetching a single deployment by ID. Use the `limit` and `page` query parameters to navigate through pages. Pagination metadata is included in the response `meta.hosts` field.                                                                                                                                       |
| hosts             | error                        | string   | Error message if the deployment failed on this host.                                                                                                                                                                                                                                                                                                                                                               |
| hosts             | hostname                     | string   | The hostname of the agent.                                                                                                                                                                                                                                                                                                                                                                                         |
| hosts             | status                       | string   | Current deployment status for this specific host.                                                                                                                                                                                                                                                                                                                                                                  |
| hosts             | versions                     | [object] | List of packages and their versions currently installed on this host.                                                                                                                                                                                                                                                                                                                                              |
| versions          | current_version              | string   | The current version of the package on the host.                                                                                                                                                                                                                                                                                                                                                                    |
| versions          | initial_version              | string   | The initial version of the package on the host before the deployment started.                                                                                                                                                                                                                                                                                                                                      |
| versions          | package_name                 | string   | The name of the package.                                                                                                                                                                                                                                                                                                                                                                                           |
| versions          | target_version               | string   | The target version that the deployment is attempting to install.                                                                                                                                                                                                                                                                                                                                                   |
| attributes        | packages                     | [object] | List of packages to deploy to target hosts. Present only for package upgrade deployments.                                                                                                                                                                                                                                                                                                                          |
| packages          | name [*required*]       | string   | The name of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                                 |
| packages          | version [*required*]    | string   | The target version of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes        | total_hosts                  | int64    | Total number of hosts targeted by this deployment.                                                                                                                                                                                                                                                                                                                                                                 |
| data              | id [*required*]         | string   | Unique identifier for the deployment.                                                                                                                                                                                                                                                                                                                                                                              |
| data              | type [*required*]       | enum     | The type of deployment resource. Allowed enum values: `deployment`                                                                                                                                                                                                                                                                                                                                                 |
|                   | meta                         | object   | Metadata for the list of deployments, including pagination information.                                                                                                                                                                                                                                                                                                                                            |
| meta              | page                         | object   | Pagination details for the list of deployments.                                                                                                                                                                                                                                                                                                                                                                    |
| page              | total_count                  | int64    | Total number of deployments available across all pages.                                                                                                                                                                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "config_operations": [
          {
            "file_op": "merge-patch",
            "file_path": "/datadog.yaml",
            "patch": {
              "apm_config": {
                "enabled": true
              },
              "log_level": "debug",
              "logs_enabled": true
            }
          }
        ],
        "estimated_end_time_unix": 1699999999,
        "filter_query": "env:prod AND service:web",
        "high_level_status": "pending",
        "hosts": [
          {
            "error": "",
            "hostname": "web-server-01.example.com",
            "status": "succeeded",
            "versions": [
              {
                "current_version": "7.51.0",
                "initial_version": "7.51.0",
                "package_name": "datadog-agent",
                "target_version": "7.52.0"
              }
            ]
          }
        ],
        "packages": [
          {
            "name": "datadog-agent",
            "version": "7.52.0"
          }
        ],
        "total_hosts": 42
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "deployment"
    }
  ],
  "meta": {
    "page": {
      "total_count": 25
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List all deployments returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["list_fleet_deployments"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.list_fleet_deployments()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List all deployments returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_fleet_deployments".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.list_fleet_deployments()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List all deployments returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListFleetDeployments", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.ListFleetDeployments(ctx, *datadogV2.NewListFleetDeploymentsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.ListFleetDeployments`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.ListFleetDeployments`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List all deployments returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetDeploymentsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listFleetDeployments", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetDeploymentsResponse result = apiInstance.listFleetDeployments();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#listFleetDeployments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List all deployments returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;
use datadog_api_client::datadogV2::api_fleet_automation::ListFleetDeploymentsOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListFleetDeployments", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api
        .list_fleet_deployments(ListFleetDeploymentsOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List all deployments returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listFleetDeployments"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

apiInstance
  .listFleetDeployments()
  .then((data: v2.FleetDeploymentsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create a configuration deployment{% #create-a-configuration-deployment %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/unstable/fleet/deployments/configure |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/unstable/fleet/deployments/configure |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/unstable/fleet/deployments/configure      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/unstable/fleet/deployments/configure      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/unstable/fleet/deployments/configure     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/unstable/fleet/deployments/configure |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/unstable/fleet/deployments/configure |

### Overview



Create a new deployment to apply configuration changes to a fleet of hosts matching the specified filter query.

This endpoint supports two types of configuration operations:

- `merge-patch`: Merges the provided patch data with the existing configuration file, creating the file if it doesn't exist
- `delete`: Removes the specified configuration file from the target hosts

The deployment is created and started automatically. You can specify multiple configuration operations that will be executed in order on each target host. Use the filter query to target specific hosts using the Datadog query syntax.
This endpoint requires all of the following permissions:`agent_upgrade_write``fleet_policies_write`


### Request

#### Body Data (required)

Request payload containing the deployment details.

{% tab title="Model" %}

| Parent field      | Field                               | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ----------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                   | data [*required*]              | object   | Data for creating a new configuration deployment.                                                                                                                                                                                                                                                                                                                                                                  |
| data              | attributes [*required*]        | object   | Attributes for creating a new configuration deployment.                                                                                                                                                                                                                                                                                                                                                            |
| attributes        | config_operations [*required*] | [object] | Ordered list of configuration file operations to perform on the target hosts.                                                                                                                                                                                                                                                                                                                                      |
| config_operations | file_op [*required*]           | enum     | Type of file operation to perform on the target configuration file.                                                                                                                                                                                                                                                                                                                                                |
| config_operations | file_path [*required*]         | string   | Absolute path to the target configuration file on the host.                                                                                                                                                                                                                                                                                                                                                        |
| config_operations | patch                               | object   | Patch data in JSON format to apply to the configuration file. When using `merge-patch`, this object is merged with the existing configuration, allowing you to add, update, or override specific fields without replacing the entire file. The structure must match the target configuration file format (for example, YAML structure for Datadog Agent config). Not applicable when using the `delete` operation. |
| attributes        | filter_query                        | string   | Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.                                                                                                                                                                                                                                                                                                                    |
| data              | type [*required*]              | enum     | The type of deployment resource. Allowed enum values: `deployment`                                                                                                                                                                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "apm_config": {
              "enabled": true
            },
            "log_level": "debug",
            "logs_enabled": true
          }
        }
      ],
      "filter_query": "env:prod AND service:web"
    },
    "type": "deployment"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response containing a single deployment.

| Parent field      | Field                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                   | data                         | object   | A deployment that defines automated configuration changes for a fleet of hosts.                                                                                                                                                                                                                                                                                                                                    |
| data              | attributes [*required*] | object   | Attributes of a deployment in the response.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes        | config_operations            | [object] | Ordered list of configuration file operations to perform on the target hosts.                                                                                                                                                                                                                                                                                                                                      |
| config_operations | file_op [*required*]    | enum     | Type of file operation to perform on the target configuration file.                                                                                                                                                                                                                                                                                                                                                |
| config_operations | file_path [*required*]  | string   | Absolute path to the target configuration file on the host.                                                                                                                                                                                                                                                                                                                                                        |
| config_operations | patch                        | object   | Patch data in JSON format to apply to the configuration file. When using `merge-patch`, this object is merged with the existing configuration, allowing you to add, update, or override specific fields without replacing the entire file. The structure must match the target configuration file format (for example, YAML structure for Datadog Agent config). Not applicable when using the `delete` operation. |
| attributes        | estimated_end_time_unix      | int64    | Estimated completion time of the deployment as a Unix timestamp (seconds since epoch).                                                                                                                                                                                                                                                                                                                             |
| attributes        | filter_query                 | string   | Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.                                                                                                                                                                                                                                                                                                                    |
| attributes        | high_level_status            | string   | Current high-level status of the deployment (for example, "pending", "running", "completed", "failed").                                                                                                                                                                                                                                                                                                            |
| attributes        | hosts                        | [object] | Paginated list of hosts in this deployment with their individual statuses. Only included when fetching a single deployment by ID. Use the `limit` and `page` query parameters to navigate through pages. Pagination metadata is included in the response `meta.hosts` field.                                                                                                                                       |
| hosts             | error                        | string   | Error message if the deployment failed on this host.                                                                                                                                                                                                                                                                                                                                                               |
| hosts             | hostname                     | string   | The hostname of the agent.                                                                                                                                                                                                                                                                                                                                                                                         |
| hosts             | status                       | string   | Current deployment status for this specific host.                                                                                                                                                                                                                                                                                                                                                                  |
| hosts             | versions                     | [object] | List of packages and their versions currently installed on this host.                                                                                                                                                                                                                                                                                                                                              |
| versions          | current_version              | string   | The current version of the package on the host.                                                                                                                                                                                                                                                                                                                                                                    |
| versions          | initial_version              | string   | The initial version of the package on the host before the deployment started.                                                                                                                                                                                                                                                                                                                                      |
| versions          | package_name                 | string   | The name of the package.                                                                                                                                                                                                                                                                                                                                                                                           |
| versions          | target_version               | string   | The target version that the deployment is attempting to install.                                                                                                                                                                                                                                                                                                                                                   |
| attributes        | packages                     | [object] | List of packages to deploy to target hosts. Present only for package upgrade deployments.                                                                                                                                                                                                                                                                                                                          |
| packages          | name [*required*]       | string   | The name of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                                 |
| packages          | version [*required*]    | string   | The target version of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes        | total_hosts                  | int64    | Total number of hosts targeted by this deployment.                                                                                                                                                                                                                                                                                                                                                                 |
| data              | id [*required*]         | string   | Unique identifier for the deployment.                                                                                                                                                                                                                                                                                                                                                                              |
| data              | type [*required*]       | enum     | The type of deployment resource. Allowed enum values: `deployment`                                                                                                                                                                                                                                                                                                                                                 |
|                   | meta                         | object   | Metadata for a single deployment response, including pagination information for hosts.                                                                                                                                                                                                                                                                                                                             |
| meta              | hosts                        | object   | Pagination details for the list of hosts in a deployment.                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | current_page                 | int64    | Current page index (zero-based).                                                                                                                                                                                                                                                                                                                                                                                   |
| hosts             | page_size                    | int64    | Number of hosts returned per page.                                                                                                                                                                                                                                                                                                                                                                                 |
| hosts             | total_hosts                  | int64    | Total number of hosts in this deployment.                                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | total_pages                  | int64    | Total number of pages available.                                                                                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "apm_config": {
              "enabled": true
            },
            "log_level": "debug",
            "logs_enabled": true
          }
        }
      ],
      "estimated_end_time_unix": 1699999999,
      "filter_query": "env:prod AND service:web",
      "high_level_status": "pending",
      "hosts": [
        {
          "error": "",
          "hostname": "web-server-01.example.com",
          "status": "succeeded",
          "versions": [
            {
              "current_version": "7.51.0",
              "initial_version": "7.51.0",
              "package_name": "datadog-agent",
              "target_version": "7.52.0"
            }
          ]
        }
      ],
      "packages": [
        {
          "name": "datadog-agent",
          "version": "7.52.0"
        }
      ],
      "total_hosts": 42
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "deployment"
  },
  "meta": {
    "hosts": {
      "current_page": 0,
      "page_size": 50,
      "total_hosts": 150,
      "total_pages": 3
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \## Add log integrations for multiple services
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/configure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/conf.d/postgres.d/logs.yaml",
          "patch": {
            "logs": [
              {
                "path": "/var/log/postgres.log",
                "service": "postgres1",
                "source": "postgres",
                "type": "file"
              }
            ]
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/conf.d/kafka.d/logs.yaml",
          "patch": {
            "logs": [
              {
                "path": "/var/log/kafka.log",
                "service": "kafka1",
                "source": "kafka",
                "type": "file"
              }
            ]
          }
        }
      ],
      "filter_query": "env:prod"
    },
    "type": "deployment"
  }
}
EOF\## Comprehensive example with multiple configuration file types
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/configure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "apm_config": {
              "apm_dd_url": "https://trace.agent.datadoghq.com",
              "enabled": true
            },
            "log_level": "info",
            "logs_enabled": true,
            "process_config": {
              "enabled": true
            }
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/security-agent.yaml",
          "patch": {
            "runtime_security_config": {
              "enabled": true,
              "fim_enabled": true
            }
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/system-probe.yaml",
          "patch": {
            "network_config": {
              "enabled": true
            },
            "service_monitoring_config": {
              "enabled": true
            }
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/application_monitoring.yaml",
          "patch": {
            "enabled": true,
            "server": {
              "host": "0.0.0.0",
              "port": 8126
            }
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/conf.d/logs.d/custom-app.yaml",
          "patch": {
            "logs": [
              {
                "path": "/var/log/custom-app/*.log",
                "service": "custom-app",
                "source": "custom",
                "type": "file"
              }
            ]
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/conf.d/docker.d/docker-logs.yaml",
          "patch": {
            "logs": [
              {
                "service": "docker",
                "source": "docker",
                "type": "docker"
              }
            ]
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/conf.d/snmp.d/network-devices.yaml",
          "patch": {
            "init_config": {
              "loader": "core"
            },
            "instances": [
              {
                "community_string": "public",
                "ip_address": "192.168.1.1"
              }
            ]
          }
        },
        {
          "file_op": "merge-patch",
          "file_path": "/conf.d/postgres.d/conf.yaml",
          "patch": {
            "instances": [
              {
                "dbname": "postgres",
                "host": "localhost",
                "port": 5432,
                "username": "datadog"
              }
            ]
          }
        },
        {
          "file_op": "delete",
          "file_path": "/conf.d/deprecated-integration.yaml"
        }
      ],
      "filter_query": "env:prod AND datacenter:us-east-1"
    },
    "type": "deployment"
  }
}
EOF\## Delete a configuration file
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/configure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "delete",
          "file_path": "/conf.d/old-integration.yaml"
        }
      ],
      "filter_query": "env:dev"
    },
    "type": "deployment"
  }
}
EOF\## Enable APM and Logs products
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/configure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "apm_config": {
              "enabled": true
            },
            "log_level": "debug",
            "logs_enabled": true
          }
        }
      ],
      "filter_query": "env:prod AND service:web"
    },
    "type": "deployment"
  }
}
EOF\## Set log level to info
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/configure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "log_level": "info"
          }
        }
      ],
      "filter_query": "env:staging"
    },
    "type": "deployment"
  }
}
EOF

#####

```python
"""
Create a configuration deployment returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_deployment_configure_attributes import FleetDeploymentConfigureAttributes
from datadog_api_client.v2.model.fleet_deployment_configure_create import FleetDeploymentConfigureCreate
from datadog_api_client.v2.model.fleet_deployment_configure_create_request import FleetDeploymentConfigureCreateRequest
from datadog_api_client.v2.model.fleet_deployment_file_op import FleetDeploymentFileOp
from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation
from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

body = FleetDeploymentConfigureCreateRequest(
    data=FleetDeploymentConfigureCreate(
        attributes=FleetDeploymentConfigureAttributes(
            config_operations=[
                FleetDeploymentOperation(
                    file_op=FleetDeploymentFileOp.MERGE_PATCH,
                    file_path="/datadog.yaml",
                    patch=dict([("apm_config", "{'enabled': True}"), ("log_level", "debug"), ("logs_enabled", "True")]),
                ),
            ],
            filter_query="env:prod AND service:web",
        ),
        type=FleetDeploymentResourceType.DEPLOYMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_fleet_deployment_configure"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_deployment_configure(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a configuration deployment returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_fleet_deployment_configure".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new

body = DatadogAPIClient::V2::FleetDeploymentConfigureCreateRequest.new({
  data: DatadogAPIClient::V2::FleetDeploymentConfigureCreate.new({
    attributes: DatadogAPIClient::V2::FleetDeploymentConfigureAttributes.new({
      config_operations: [
        DatadogAPIClient::V2::FleetDeploymentOperation.new({
          file_op: DatadogAPIClient::V2::FleetDeploymentFileOp::MERGE_PATCH,
          file_path: "/datadog.yaml",
          patch: {
            "apm_config": "{'enabled': True}", "log_level": "debug", "logs_enabled": "True",
          },
        }),
      ],
      filter_query: "env:prod AND service:web",
    }),
    type: DatadogAPIClient::V2::FleetDeploymentResourceType::DEPLOYMENT,
  }),
})
p api_instance.create_fleet_deployment_configure(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create a configuration deployment returns "CREATED" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.FleetDeploymentConfigureCreateRequest{
        Data: datadogV2.FleetDeploymentConfigureCreate{
            Attributes: datadogV2.FleetDeploymentConfigureAttributes{
                ConfigOperations: []datadogV2.FleetDeploymentOperation{
                    {
                        FileOp:   datadogV2.FLEETDEPLOYMENTFILEOP_MERGE_PATCH,
                        FilePath: "/datadog.yaml",
                        Patch: map[string]interface{}{
                            "apm_config":   "{'enabled': True}",
                            "log_level":    "debug",
                            "logs_enabled": "True",
                        },
                    },
                },
                FilterQuery: datadog.PtrString("env:prod AND service:web"),
            },
            Type: datadogV2.FLEETDEPLOYMENTRESOURCETYPE_DEPLOYMENT,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateFleetDeploymentConfigure", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.CreateFleetDeploymentConfigure(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.CreateFleetDeploymentConfigure`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.CreateFleetDeploymentConfigure`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a configuration deployment returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetDeploymentConfigureAttributes;
import com.datadog.api.client.v2.model.FleetDeploymentConfigureCreate;
import com.datadog.api.client.v2.model.FleetDeploymentConfigureCreateRequest;
import com.datadog.api.client.v2.model.FleetDeploymentFileOp;
import com.datadog.api.client.v2.model.FleetDeploymentOperation;
import com.datadog.api.client.v2.model.FleetDeploymentResourceType;
import com.datadog.api.client.v2.model.FleetDeploymentResponse;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createFleetDeploymentConfigure", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    FleetDeploymentConfigureCreateRequest body =
        new FleetDeploymentConfigureCreateRequest()
            .data(
                new FleetDeploymentConfigureCreate()
                    .attributes(
                        new FleetDeploymentConfigureAttributes()
                            .configOperations(
                                Collections.singletonList(
                                    new FleetDeploymentOperation()
                                        .fileOp(FleetDeploymentFileOp.MERGE_PATCH)
                                        .filePath("/datadog.yaml")
                                        .patch(
                                            Map.ofEntries(
                                                Map.entry("apm_config", "{'enabled': True}"),
                                                Map.entry("log_level", "debug"),
                                                Map.entry("logs_enabled", "True")))))
                            .filterQuery("env:prod AND service:web"))
                    .type(FleetDeploymentResourceType.DEPLOYMENT));

    try {
      FleetDeploymentResponse result = apiInstance.createFleetDeploymentConfigure(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling FleetAutomationApi#createFleetDeploymentConfigure");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Create a configuration deployment returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;
use datadog_api_client::datadogV2::model::FleetDeploymentConfigureAttributes;
use datadog_api_client::datadogV2::model::FleetDeploymentConfigureCreate;
use datadog_api_client::datadogV2::model::FleetDeploymentConfigureCreateRequest;
use datadog_api_client::datadogV2::model::FleetDeploymentFileOp;
use datadog_api_client::datadogV2::model::FleetDeploymentOperation;
use datadog_api_client::datadogV2::model::FleetDeploymentResourceType;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = FleetDeploymentConfigureCreateRequest::new(FleetDeploymentConfigureCreate::new(
        FleetDeploymentConfigureAttributes::new(vec![FleetDeploymentOperation::new(
            FleetDeploymentFileOp::MERGE_PATCH,
            "/datadog.yaml".to_string(),
        )
        .patch(BTreeMap::from([
            ("log_level".to_string(), Value::from("debug")),
            ("logs_enabled".to_string(), Value::from("True")),
        ]))])
        .filter_query("env:prod AND service:web".to_string()),
        FleetDeploymentResourceType::DEPLOYMENT,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateFleetDeploymentConfigure", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.create_fleet_deployment_configure(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create a configuration deployment returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createFleetDeploymentConfigure"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiCreateFleetDeploymentConfigureRequest = {
  body: {
    data: {
      attributes: {
        configOperations: [
          {
            fileOp: "merge-patch",
            filePath: "/datadog.yaml",
            patch: {
              apm_config: "{'enabled': True}",
              log_level: "debug",
              logs_enabled: "True",
            },
          },
        ],
        filterQuery: "env:prod AND service:web",
      },
      type: "deployment",
    },
  },
};

apiInstance
  .createFleetDeploymentConfigure(params)
  .then((data: v2.FleetDeploymentResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Upgrade hosts{% #upgrade-hosts %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/unstable/fleet/deployments/upgrade |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/unstable/fleet/deployments/upgrade |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/unstable/fleet/deployments/upgrade      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/unstable/fleet/deployments/upgrade      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/unstable/fleet/deployments/upgrade     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/unstable/fleet/deployments/upgrade |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/unstable/fleet/deployments/upgrade |

### Overview



Create and immediately start a new package upgrade on hosts matching the specified filter query.

This endpoint allows you to upgrade the Datadog Agent to a specific version on hosts matching the specified filter query.

The deployment is created and started automatically. The system will:

1. Identify all hosts matching the filter query
1. Validate that the specified version is available
1. Begin rolling out the package upgrade to the target hosts
This endpoint requires all of the following permissions:`agent_upgrade_write``fleet_policies_write`


### Request

#### Body Data (required)

Request payload containing the package upgrade details.

{% tab title="Model" %}

| Parent field    | Field                             | Type     | Description                                                                                     |
| --------------- | --------------------------------- | -------- | ----------------------------------------------------------------------------------------------- |
|                 | data [*required*]            | object   | Data for creating a new package upgrade deployment.                                             |
| data            | attributes [*required*]      | object   | Attributes for creating a new package upgrade deployment.                                       |
| attributes      | filter_query                      | string   | Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax. |
| attributes      | target_packages [*required*] | [object] | List of packages and their target versions to deploy to the selected hosts.                     |
| target_packages | name [*required*]            | string   | The name of the package to deploy.                                                              |
| target_packages | version [*required*]         | string   | The target version of the package to deploy.                                                    |
| data            | type [*required*]            | enum     | The type of deployment resource. Allowed enum values: `deployment`                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "filter_query": "env:prod AND service:web",
      "target_packages": [
        {
          "name": "datadog-agent",
          "version": "7.52.0"
        }
      ]
    },
    "type": "deployment"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response containing a single deployment.

| Parent field      | Field                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                   | data                         | object   | A deployment that defines automated configuration changes for a fleet of hosts.                                                                                                                                                                                                                                                                                                                                    |
| data              | attributes [*required*] | object   | Attributes of a deployment in the response.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes        | config_operations            | [object] | Ordered list of configuration file operations to perform on the target hosts.                                                                                                                                                                                                                                                                                                                                      |
| config_operations | file_op [*required*]    | enum     | Type of file operation to perform on the target configuration file.                                                                                                                                                                                                                                                                                                                                                |
| config_operations | file_path [*required*]  | string   | Absolute path to the target configuration file on the host.                                                                                                                                                                                                                                                                                                                                                        |
| config_operations | patch                        | object   | Patch data in JSON format to apply to the configuration file. When using `merge-patch`, this object is merged with the existing configuration, allowing you to add, update, or override specific fields without replacing the entire file. The structure must match the target configuration file format (for example, YAML structure for Datadog Agent config). Not applicable when using the `delete` operation. |
| attributes        | estimated_end_time_unix      | int64    | Estimated completion time of the deployment as a Unix timestamp (seconds since epoch).                                                                                                                                                                                                                                                                                                                             |
| attributes        | filter_query                 | string   | Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.                                                                                                                                                                                                                                                                                                                    |
| attributes        | high_level_status            | string   | Current high-level status of the deployment (for example, "pending", "running", "completed", "failed").                                                                                                                                                                                                                                                                                                            |
| attributes        | hosts                        | [object] | Paginated list of hosts in this deployment with their individual statuses. Only included when fetching a single deployment by ID. Use the `limit` and `page` query parameters to navigate through pages. Pagination metadata is included in the response `meta.hosts` field.                                                                                                                                       |
| hosts             | error                        | string   | Error message if the deployment failed on this host.                                                                                                                                                                                                                                                                                                                                                               |
| hosts             | hostname                     | string   | The hostname of the agent.                                                                                                                                                                                                                                                                                                                                                                                         |
| hosts             | status                       | string   | Current deployment status for this specific host.                                                                                                                                                                                                                                                                                                                                                                  |
| hosts             | versions                     | [object] | List of packages and their versions currently installed on this host.                                                                                                                                                                                                                                                                                                                                              |
| versions          | current_version              | string   | The current version of the package on the host.                                                                                                                                                                                                                                                                                                                                                                    |
| versions          | initial_version              | string   | The initial version of the package on the host before the deployment started.                                                                                                                                                                                                                                                                                                                                      |
| versions          | package_name                 | string   | The name of the package.                                                                                                                                                                                                                                                                                                                                                                                           |
| versions          | target_version               | string   | The target version that the deployment is attempting to install.                                                                                                                                                                                                                                                                                                                                                   |
| attributes        | packages                     | [object] | List of packages to deploy to target hosts. Present only for package upgrade deployments.                                                                                                                                                                                                                                                                                                                          |
| packages          | name [*required*]       | string   | The name of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                                 |
| packages          | version [*required*]    | string   | The target version of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes        | total_hosts                  | int64    | Total number of hosts targeted by this deployment.                                                                                                                                                                                                                                                                                                                                                                 |
| data              | id [*required*]         | string   | Unique identifier for the deployment.                                                                                                                                                                                                                                                                                                                                                                              |
| data              | type [*required*]       | enum     | The type of deployment resource. Allowed enum values: `deployment`                                                                                                                                                                                                                                                                                                                                                 |
|                   | meta                         | object   | Metadata for a single deployment response, including pagination information for hosts.                                                                                                                                                                                                                                                                                                                             |
| meta              | hosts                        | object   | Pagination details for the list of hosts in a deployment.                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | current_page                 | int64    | Current page index (zero-based).                                                                                                                                                                                                                                                                                                                                                                                   |
| hosts             | page_size                    | int64    | Number of hosts returned per page.                                                                                                                                                                                                                                                                                                                                                                                 |
| hosts             | total_hosts                  | int64    | Total number of hosts in this deployment.                                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | total_pages                  | int64    | Total number of pages available.                                                                                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "apm_config": {
              "enabled": true
            },
            "log_level": "debug",
            "logs_enabled": true
          }
        }
      ],
      "estimated_end_time_unix": 1699999999,
      "filter_query": "env:prod AND service:web",
      "high_level_status": "pending",
      "hosts": [
        {
          "error": "",
          "hostname": "web-server-01.example.com",
          "status": "succeeded",
          "versions": [
            {
              "current_version": "7.51.0",
              "initial_version": "7.51.0",
              "package_name": "datadog-agent",
              "target_version": "7.52.0"
            }
          ]
        }
      ],
      "packages": [
        {
          "name": "datadog-agent",
          "version": "7.52.0"
        }
      ],
      "total_hosts": 42
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "deployment"
  },
  "meta": {
    "hosts": {
      "current_page": 0,
      "page_size": 50,
      "total_hosts": 150,
      "total_pages": 3
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \## Upgrade Datadog Agent to version 7.52.0
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/upgrade" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter_query": "env:prod AND service:web",
      "target_packages": [
        {
          "name": "datadog-agent",
          "version": "7.52.0"
        }
      ]
    },
    "type": "deployment"
  }
}
EOF\## Upgrade multiple packages
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/upgrade" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter_query": "env:staging",
      "target_packages": [
        {
          "name": "datadog-agent",
          "version": "7.52.0-1"
        },
        {
          "name": "datadog-apm-inject",
          "version": "0.10.0"
        }
      ]
    },
    "type": "deployment"
  }
}
EOF

#####

```python
"""
Upgrade hosts returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_deployment_package import FleetDeploymentPackage
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_attributes import (
    FleetDeploymentPackageUpgradeAttributes,
)
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_create import FleetDeploymentPackageUpgradeCreate
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_create_request import (
    FleetDeploymentPackageUpgradeCreateRequest,
)
from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

body = FleetDeploymentPackageUpgradeCreateRequest(
    data=FleetDeploymentPackageUpgradeCreate(
        attributes=FleetDeploymentPackageUpgradeAttributes(
            filter_query="env:prod AND service:web",
            target_packages=[
                FleetDeploymentPackage(
                    name="datadog-agent",
                    version="7.52.0",
                ),
            ],
        ),
        type=FleetDeploymentResourceType.DEPLOYMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_fleet_deployment_upgrade"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_deployment_upgrade(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Upgrade hosts returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_fleet_deployment_upgrade".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new

body = DatadogAPIClient::V2::FleetDeploymentPackageUpgradeCreateRequest.new({
  data: DatadogAPIClient::V2::FleetDeploymentPackageUpgradeCreate.new({
    attributes: DatadogAPIClient::V2::FleetDeploymentPackageUpgradeAttributes.new({
      filter_query: "env:prod AND service:web",
      target_packages: [
        DatadogAPIClient::V2::FleetDeploymentPackage.new({
          name: "datadog-agent",
          version: "7.52.0",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::FleetDeploymentResourceType::DEPLOYMENT,
  }),
})
p api_instance.create_fleet_deployment_upgrade(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Upgrade hosts returns "CREATED" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.FleetDeploymentPackageUpgradeCreateRequest{
        Data: datadogV2.FleetDeploymentPackageUpgradeCreate{
            Attributes: datadogV2.FleetDeploymentPackageUpgradeAttributes{
                FilterQuery: datadog.PtrString("env:prod AND service:web"),
                TargetPackages: []datadogV2.FleetDeploymentPackage{
                    {
                        Name:    "datadog-agent",
                        Version: "7.52.0",
                    },
                },
            },
            Type: datadogV2.FLEETDEPLOYMENTRESOURCETYPE_DEPLOYMENT,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateFleetDeploymentUpgrade", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.CreateFleetDeploymentUpgrade(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.CreateFleetDeploymentUpgrade`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.CreateFleetDeploymentUpgrade`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Upgrade hosts returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetDeploymentPackage;
import com.datadog.api.client.v2.model.FleetDeploymentPackageUpgradeAttributes;
import com.datadog.api.client.v2.model.FleetDeploymentPackageUpgradeCreate;
import com.datadog.api.client.v2.model.FleetDeploymentPackageUpgradeCreateRequest;
import com.datadog.api.client.v2.model.FleetDeploymentResourceType;
import com.datadog.api.client.v2.model.FleetDeploymentResponse;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createFleetDeploymentUpgrade", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    FleetDeploymentPackageUpgradeCreateRequest body =
        new FleetDeploymentPackageUpgradeCreateRequest()
            .data(
                new FleetDeploymentPackageUpgradeCreate()
                    .attributes(
                        new FleetDeploymentPackageUpgradeAttributes()
                            .filterQuery("env:prod AND service:web")
                            .targetPackages(
                                Collections.singletonList(
                                    new FleetDeploymentPackage()
                                        .name("datadog-agent")
                                        .version("7.52.0"))))
                    .type(FleetDeploymentResourceType.DEPLOYMENT));

    try {
      FleetDeploymentResponse result = apiInstance.createFleetDeploymentUpgrade(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#createFleetDeploymentUpgrade");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Upgrade hosts returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;
use datadog_api_client::datadogV2::model::FleetDeploymentPackage;
use datadog_api_client::datadogV2::model::FleetDeploymentPackageUpgradeAttributes;
use datadog_api_client::datadogV2::model::FleetDeploymentPackageUpgradeCreate;
use datadog_api_client::datadogV2::model::FleetDeploymentPackageUpgradeCreateRequest;
use datadog_api_client::datadogV2::model::FleetDeploymentResourceType;

#[tokio::main]
async fn main() {
    let body =
        FleetDeploymentPackageUpgradeCreateRequest::new(FleetDeploymentPackageUpgradeCreate::new(
            FleetDeploymentPackageUpgradeAttributes::new(vec![FleetDeploymentPackage::new(
                "datadog-agent".to_string(),
                "7.52.0".to_string(),
            )])
            .filter_query("env:prod AND service:web".to_string()),
            FleetDeploymentResourceType::DEPLOYMENT,
        ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateFleetDeploymentUpgrade", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.create_fleet_deployment_upgrade(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Upgrade hosts returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createFleetDeploymentUpgrade"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiCreateFleetDeploymentUpgradeRequest = {
  body: {
    data: {
      attributes: {
        filterQuery: "env:prod AND service:web",
        targetPackages: [
          {
            name: "datadog-agent",
            version: "7.52.0",
          },
        ],
      },
      type: "deployment",
    },
  },
};

apiInstance
  .createFleetDeploymentUpgrade(params)
  .then((data: v2.FleetDeploymentResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a configuration deployment by ID{% #get-a-configuration-deployment-by-id %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/unstable/fleet/deployments/{deployment_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/unstable/fleet/deployments/{deployment_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/unstable/fleet/deployments/{deployment_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/unstable/fleet/deployments/{deployment_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/unstable/fleet/deployments/{deployment_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/unstable/fleet/deployments/{deployment_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/unstable/fleet/deployments/{deployment_id} |

### Overview



Retrieve detailed information about a specific deployment using its unique identifier. This endpoint returns comprehensive information about a deployment, including:

- Deployment metadata (ID, type, filter query)
- Total number of target hosts
- Current high-level status (pending, running, succeeded, failed)
- Estimated completion time
- Configuration operations that were or are being applied
- Detailed host list: A paginated array of hosts included in this deployment with individual host status, current package versions, and any errors

The host list provides visibility into the per-host execution status, allowing you to:

- Monitor which hosts have completed successfully
- Identify hosts that are still in progress
- Investigate failures on specific hosts
- View current package versions installed on each host (including initial, target, and current versions for each package)

Pagination: Use the `limit` and `page` query parameters to paginate through hosts. The response includes pagination metadata in the `meta.hosts` field with information about the current page, total pages, and total host count. The default page size is 50 hosts, with a maximum of 100.
This endpoint requires the `hosts_read` permission.


### Arguments

#### Path Parameters

| Name                            | Type   | Description                                          |
| ------------------------------- | ------ | ---------------------------------------------------- |
| deployment_id [*required*] | string | The unique identifier of the deployment to retrieve. |

#### Query Strings

| Name  | Type    | Description                                                                             |
| ----- | ------- | --------------------------------------------------------------------------------------- |
| limit | integer | Maximum number of hosts to return per page. Default is 50, maximum is 100.              |
| page  | integer | Page index for pagination (zero-based). Use this to retrieve subsequent pages of hosts. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single deployment.

| Parent field      | Field                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                   | data                         | object   | A deployment that defines automated configuration changes for a fleet of hosts.                                                                                                                                                                                                                                                                                                                                    |
| data              | attributes [*required*] | object   | Attributes of a deployment in the response.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes        | config_operations            | [object] | Ordered list of configuration file operations to perform on the target hosts.                                                                                                                                                                                                                                                                                                                                      |
| config_operations | file_op [*required*]    | enum     | Type of file operation to perform on the target configuration file.                                                                                                                                                                                                                                                                                                                                                |
| config_operations | file_path [*required*]  | string   | Absolute path to the target configuration file on the host.                                                                                                                                                                                                                                                                                                                                                        |
| config_operations | patch                        | object   | Patch data in JSON format to apply to the configuration file. When using `merge-patch`, this object is merged with the existing configuration, allowing you to add, update, or override specific fields without replacing the entire file. The structure must match the target configuration file format (for example, YAML structure for Datadog Agent config). Not applicable when using the `delete` operation. |
| attributes        | estimated_end_time_unix      | int64    | Estimated completion time of the deployment as a Unix timestamp (seconds since epoch).                                                                                                                                                                                                                                                                                                                             |
| attributes        | filter_query                 | string   | Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.                                                                                                                                                                                                                                                                                                                    |
| attributes        | high_level_status            | string   | Current high-level status of the deployment (for example, "pending", "running", "completed", "failed").                                                                                                                                                                                                                                                                                                            |
| attributes        | hosts                        | [object] | Paginated list of hosts in this deployment with their individual statuses. Only included when fetching a single deployment by ID. Use the `limit` and `page` query parameters to navigate through pages. Pagination metadata is included in the response `meta.hosts` field.                                                                                                                                       |
| hosts             | error                        | string   | Error message if the deployment failed on this host.                                                                                                                                                                                                                                                                                                                                                               |
| hosts             | hostname                     | string   | The hostname of the agent.                                                                                                                                                                                                                                                                                                                                                                                         |
| hosts             | status                       | string   | Current deployment status for this specific host.                                                                                                                                                                                                                                                                                                                                                                  |
| hosts             | versions                     | [object] | List of packages and their versions currently installed on this host.                                                                                                                                                                                                                                                                                                                                              |
| versions          | current_version              | string   | The current version of the package on the host.                                                                                                                                                                                                                                                                                                                                                                    |
| versions          | initial_version              | string   | The initial version of the package on the host before the deployment started.                                                                                                                                                                                                                                                                                                                                      |
| versions          | package_name                 | string   | The name of the package.                                                                                                                                                                                                                                                                                                                                                                                           |
| versions          | target_version               | string   | The target version that the deployment is attempting to install.                                                                                                                                                                                                                                                                                                                                                   |
| attributes        | packages                     | [object] | List of packages to deploy to target hosts. Present only for package upgrade deployments.                                                                                                                                                                                                                                                                                                                          |
| packages          | name [*required*]       | string   | The name of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                                 |
| packages          | version [*required*]    | string   | The target version of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes        | total_hosts                  | int64    | Total number of hosts targeted by this deployment.                                                                                                                                                                                                                                                                                                                                                                 |
| data              | id [*required*]         | string   | Unique identifier for the deployment.                                                                                                                                                                                                                                                                                                                                                                              |
| data              | type [*required*]       | enum     | The type of deployment resource. Allowed enum values: `deployment`                                                                                                                                                                                                                                                                                                                                                 |
|                   | meta                         | object   | Metadata for a single deployment response, including pagination information for hosts.                                                                                                                                                                                                                                                                                                                             |
| meta              | hosts                        | object   | Pagination details for the list of hosts in a deployment.                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | current_page                 | int64    | Current page index (zero-based).                                                                                                                                                                                                                                                                                                                                                                                   |
| hosts             | page_size                    | int64    | Number of hosts returned per page.                                                                                                                                                                                                                                                                                                                                                                                 |
| hosts             | total_hosts                  | int64    | Total number of hosts in this deployment.                                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | total_pages                  | int64    | Total number of pages available.                                                                                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "apm_config": {
              "enabled": true
            },
            "log_level": "debug",
            "logs_enabled": true
          }
        }
      ],
      "estimated_end_time_unix": 1699999999,
      "filter_query": "env:prod AND service:web",
      "high_level_status": "pending",
      "hosts": [
        {
          "error": "",
          "hostname": "web-server-01.example.com",
          "status": "succeeded",
          "versions": [
            {
              "current_version": "7.51.0",
              "initial_version": "7.51.0",
              "package_name": "datadog-agent",
              "target_version": "7.52.0"
            }
          ]
        }
      ],
      "packages": [
        {
          "name": "datadog-agent",
          "version": "7.52.0"
        }
      ],
      "total_hosts": 42
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "deployment"
  },
  "meta": {
    "hosts": {
      "current_page": 0,
      "page_size": 50,
      "total_hosts": 150,
      "total_pages": 3
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport deployment_id="abc-def-ghi"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/${deployment_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a configuration deployment by ID returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["get_fleet_deployment"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.get_fleet_deployment(
        deployment_id="deployment_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a configuration deployment by ID returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_fleet_deployment".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.get_fleet_deployment("deployment_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a configuration deployment by ID returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetFleetDeployment", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.GetFleetDeployment(ctx, "deployment_id", *datadogV2.NewGetFleetDeploymentOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.GetFleetDeployment`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.GetFleetDeployment`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a configuration deployment by ID returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetDeploymentResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getFleetDeployment", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetDeploymentResponse result = apiInstance.getFleetDeployment("abc-def-ghi");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#getFleetDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Get a configuration deployment by ID returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;
use datadog_api_client::datadogV2::api_fleet_automation::GetFleetDeploymentOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetFleetDeployment", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api
        .get_fleet_deployment(
            "deployment_id".to_string(),
            GetFleetDeploymentOptionalParams::default(),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get a configuration deployment by ID returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getFleetDeployment"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiGetFleetDeploymentRequest = {
  deploymentId: "deployment_id",
};

apiInstance
  .getFleetDeployment(params)
  .then((data: v2.FleetDeploymentResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Cancel a deployment{% #cancel-a-deployment %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/unstable/fleet/deployments/{deployment_id}/cancel |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/unstable/fleet/deployments/{deployment_id}/cancel |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/unstable/fleet/deployments/{deployment_id}/cancel      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/unstable/fleet/deployments/{deployment_id}/cancel      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/unstable/fleet/deployments/{deployment_id}/cancel     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/unstable/fleet/deployments/{deployment_id}/cancel |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/unstable/fleet/deployments/{deployment_id}/cancel |

### Overview



Cancel an active deployment and stop all pending operations. When you cancel a deployment:

- All pending operations on hosts that haven't started yet are stopped
- Operations currently in progress on hosts may complete or be interrupted, depending on their current state
- Configuration changes or package upgrades already applied to hosts are not rolled back

After cancellation, you can view the final state of the deployment using the GET endpoint to see which hosts were successfully updated before the cancellation.
This endpoint requires all of the following permissions:`agent_upgrade_write``fleet_policies_write`


### Arguments

#### Path Parameters

| Name                            | Type   | Description                                        |
| ------------------------------- | ------ | -------------------------------------------------- |
| deployment_id [*required*] | string | The unique identifier of the deployment to cancel. |

### Response

{% tab title="204" %}
Deployment successfully canceled.
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport deployment_id="abc-def-ghi"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/deployments/${deployment_id}/cancel" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Cancel a deployment returns "Deployment successfully canceled." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["cancel_fleet_deployment"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    api_instance.cancel_fleet_deployment(
        deployment_id="deployment_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Cancel a deployment returns "Deployment successfully canceled." response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.cancel_fleet_deployment".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
api_instance.cancel_fleet_deployment("deployment_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Cancel a deployment returns "Deployment successfully canceled." response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CancelFleetDeployment", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    r, err := api.CancelFleetDeployment(ctx, "deployment_id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.CancelFleetDeployment`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Cancel a deployment returns "Deployment successfully canceled." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.cancelFleetDeployment", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      apiInstance.cancelFleetDeployment("abc-def-ghi");
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#cancelFleetDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Cancel a deployment returns "Deployment successfully canceled." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CancelFleetDeployment", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api
        .cancel_fleet_deployment("deployment_id".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Cancel a deployment returns "Deployment successfully canceled." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.cancelFleetDeployment"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiCancelFleetDeploymentRequest = {
  deploymentId: "deployment_id",
};

apiInstance
  .cancelFleetDeployment(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List all schedules{% #list-all-schedules %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/unstable/fleet/schedules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/unstable/fleet/schedules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/unstable/fleet/schedules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/unstable/fleet/schedules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/unstable/fleet/schedules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/unstable/fleet/schedules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/unstable/fleet/schedules |

### Overview



Retrieve a list of all schedules for automated fleet deployments.

Schedules allow you to automate package upgrades by defining maintenance windows and recurrence rules. Each schedule automatically creates deployments based on its configuration.
This endpoint requires the `hosts_read` permission.


### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of schedules.

| Parent field | Field                                         | Type     | Description                                                                                                                                 |
| ------------ | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                        | [object] | Array of schedules.                                                                                                                         |
| data         | attributes [*required*]                  | object   | Attributes of a schedule in the response.                                                                                                   |
| attributes   | created_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was created.                                                                         |
| attributes   | created_by                                    | string   | User handle of the person who created the schedule.                                                                                         |
| attributes   | name                                          | string   | Human-readable name for the schedule.                                                                                                       |
| attributes   | query                                         | string   | Query used to filter and select target hosts for scheduled deployments. Uses the Datadog query syntax.                                      |
| attributes   | rule                                          | object   | Defines the recurrence pattern for the schedule. Specifies when deployments should be automatically triggered based on maintenance windows. |
| rule         | days_of_week [*required*]                | [string] | List of days of the week when the schedule should trigger. Valid values are: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".               |
| rule         | maintenance_window_duration [*required*] | int64    | Duration of the maintenance window in minutes.                                                                                              |
| rule         | start_maintenance_window [*required*]    | string   | Start time of the maintenance window in 24-hour clock format (HH:MM). Deployments will be triggered at this time on the specified days.     |
| rule         | timezone [*required*]                    | string   | Timezone for the schedule in IANA Time Zone Database format (e.g., "America/New_York", "UTC").                                              |
| attributes   | status                                        | enum     | The status of the schedule.                                                                                                                 |
| attributes   | updated_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was last updated.                                                                    |
| attributes   | updated_by                                    | string   | User handle of the person who last updated the schedule.                                                                                    |
| attributes   | version_to_latest                             | int64    | Number of major versions behind the latest to target for upgrades.                                                                          |
| data         | id [*required*]                          | string   | Unique identifier for the schedule.                                                                                                         |
| data         | type [*required*]                        | enum     | The type of schedule resource. Allowed enum values: `schedule`                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at_unix": 1699999999,
        "created_by": "user@example.com",
        "name": "Weekly Production Agent Updates",
        "query": "env:prod AND service:web",
        "rule": {
          "days_of_week": [
            "Mon",
            "Wed",
            "Fri"
          ],
          "maintenance_window_duration": 1200,
          "start_maintenance_window": "02:00",
          "timezone": "America/New_York"
        },
        "status": "active",
        "updated_at_unix": 1699999999,
        "updated_by": "user@example.com",
        "version_to_latest": 0
      },
      "id": "abc-def-ghi-123",
      "type": "schedule"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List all schedules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["list_fleet_schedules"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.list_fleet_schedules()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List all schedules returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_fleet_schedules".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.list_fleet_schedules()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List all schedules returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListFleetSchedules", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.ListFleetSchedules(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.ListFleetSchedules`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.ListFleetSchedules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List all schedules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetSchedulesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listFleetSchedules", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetSchedulesResponse result = apiInstance.listFleetSchedules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#listFleetSchedules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List all schedules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListFleetSchedules", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.list_fleet_schedules().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List all schedules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listFleetSchedules"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

apiInstance
  .listFleetSchedules()
  .then((data: v2.FleetSchedulesResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create a schedule{% #create-a-schedule %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/unstable/fleet/schedules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/unstable/fleet/schedules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/unstable/fleet/schedules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/unstable/fleet/schedules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/unstable/fleet/schedules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/unstable/fleet/schedules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/unstable/fleet/schedules |

### Overview



Create a new schedule for automated package upgrades.

Schedules define when and how often to automatically deploy package upgrades to a fleet of hosts. Each schedule includes:

- A filter query to select target hosts
- A recurrence rule defining maintenance windows
- A version strategy (e.g., always latest, or N versions behind latest)

When the schedule triggers during a maintenance window, it automatically creates a deployment that upgrades the Datadog Agent to the specified version on all matching hosts.
This endpoint requires the `agent_upgrade_write` permission.


### Request

#### Body Data (required)

Request payload containing the schedule details.

{% tab title="Model" %}

| Parent field | Field                                         | Type     | Description                                                                                                                                 |
| ------------ | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                        | object   | Data for creating a new schedule.                                                                                                           |
| data         | attributes [*required*]                  | object   | Attributes for creating a new schedule.                                                                                                     |
| attributes   | name [*required*]                        | string   | Human-readable name for the schedule.                                                                                                       |
| attributes   | query [*required*]                       | string   | Query used to filter and select target hosts for scheduled deployments. Uses the Datadog query syntax.                                      |
| attributes   | rule [*required*]                        | object   | Defines the recurrence pattern for the schedule. Specifies when deployments should be automatically triggered based on maintenance windows. |
| rule         | days_of_week [*required*]                | [string] | List of days of the week when the schedule should trigger. Valid values are: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".               |
| rule         | maintenance_window_duration [*required*] | int64    | Duration of the maintenance window in minutes.                                                                                              |
| rule         | start_maintenance_window [*required*]    | string   | Start time of the maintenance window in 24-hour clock format (HH:MM). Deployments will be triggered at this time on the specified days.     |
| rule         | timezone [*required*]                    | string   | Timezone for the schedule in IANA Time Zone Database format (e.g., "America/New_York", "UTC").                                              |
| attributes   | status                                        | enum     | The status of the schedule.                                                                                                                 |
| attributes   | version_to_latest                             | int64    | Number of major versions behind the latest to target for upgrades.                                                                          |
| data         | type [*required*]                        | enum     | The type of schedule resource. Allowed enum values: `schedule`                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Weekly Production Agent Updates",
      "query": "env:prod AND service:web",
      "rule": {
        "days_of_week": [
          "Mon",
          "Wed",
          "Fri"
        ],
        "maintenance_window_duration": 1200,
        "start_maintenance_window": "02:00",
        "timezone": "America/New_York"
      },
      "status": "active",
      "version_to_latest": 0
    },
    "type": "schedule"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response containing a single schedule.

| Parent field | Field                                         | Type     | Description                                                                                                                                 |
| ------------ | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                                          | object   | A schedule that automatically creates deployments based on a recurrence rule.                                                               |
| data         | attributes [*required*]                  | object   | Attributes of a schedule in the response.                                                                                                   |
| attributes   | created_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was created.                                                                         |
| attributes   | created_by                                    | string   | User handle of the person who created the schedule.                                                                                         |
| attributes   | name                                          | string   | Human-readable name for the schedule.                                                                                                       |
| attributes   | query                                         | string   | Query used to filter and select target hosts for scheduled deployments. Uses the Datadog query syntax.                                      |
| attributes   | rule                                          | object   | Defines the recurrence pattern for the schedule. Specifies when deployments should be automatically triggered based on maintenance windows. |
| rule         | days_of_week [*required*]                | [string] | List of days of the week when the schedule should trigger. Valid values are: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".               |
| rule         | maintenance_window_duration [*required*] | int64    | Duration of the maintenance window in minutes.                                                                                              |
| rule         | start_maintenance_window [*required*]    | string   | Start time of the maintenance window in 24-hour clock format (HH:MM). Deployments will be triggered at this time on the specified days.     |
| rule         | timezone [*required*]                    | string   | Timezone for the schedule in IANA Time Zone Database format (e.g., "America/New_York", "UTC").                                              |
| attributes   | status                                        | enum     | The status of the schedule.                                                                                                                 |
| attributes   | updated_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was last updated.                                                                    |
| attributes   | updated_by                                    | string   | User handle of the person who last updated the schedule.                                                                                    |
| attributes   | version_to_latest                             | int64    | Number of major versions behind the latest to target for upgrades.                                                                          |
| data         | id [*required*]                          | string   | Unique identifier for the schedule.                                                                                                         |
| data         | type [*required*]                        | enum     | The type of schedule resource. Allowed enum values: `schedule`                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at_unix": 1699999999,
      "created_by": "user@example.com",
      "name": "Weekly Production Agent Updates",
      "query": "env:prod AND service:web",
      "rule": {
        "days_of_week": [
          "Mon",
          "Wed",
          "Fri"
        ],
        "maintenance_window_duration": 1200,
        "start_maintenance_window": "02:00",
        "timezone": "America/New_York"
      },
      "status": "active",
      "updated_at_unix": 1699999999,
      "updated_by": "user@example.com",
      "version_to_latest": 0
    },
    "id": "abc-def-ghi-123",
    "type": "schedule"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \## Conservative staging updates (N-1 version)
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Staging Environment - Conservative Updates",
      "query": "env:staging",
      "rule": {
        "days_of_week": [
          "Fri"
        ],
        "maintenance_window_duration": 240,
        "start_maintenance_window": "22:00",
        "timezone": "UTC"
      },
      "status": "active",
      "version_to_latest": 1
    },
    "type": "schedule"
  }
}
EOF\## Weekly production agent updates
#
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Weekly Production Agent Updates",
      "query": "env:prod",
      "rule": {
        "days_of_week": [
          "Mon",
          "Wed"
        ],
        "maintenance_window_duration": 180,
        "start_maintenance_window": "02:00",
        "timezone": "America/New_York"
      },
      "status": "active",
      "version_to_latest": 0
    },
    "type": "schedule"
  }
}
EOF

#####

```python
"""
Create a schedule returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_schedule_create import FleetScheduleCreate
from datadog_api_client.v2.model.fleet_schedule_create_attributes import FleetScheduleCreateAttributes
from datadog_api_client.v2.model.fleet_schedule_create_request import FleetScheduleCreateRequest
from datadog_api_client.v2.model.fleet_schedule_recurrence_rule import FleetScheduleRecurrenceRule
from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType
from datadog_api_client.v2.model.fleet_schedule_status import FleetScheduleStatus

body = FleetScheduleCreateRequest(
    data=FleetScheduleCreate(
        attributes=FleetScheduleCreateAttributes(
            name="Weekly Production Agent Updates",
            query="env:prod AND service:web",
            rule=FleetScheduleRecurrenceRule(
                days_of_week=[
                    "Mon",
                    "Wed",
                    "Fri",
                ],
                maintenance_window_duration=1200,
                start_maintenance_window="02:00",
                timezone="America/New_York",
            ),
            status=FleetScheduleStatus.ACTIVE,
            version_to_latest=0,
        ),
        type=FleetScheduleResourceType.SCHEDULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_fleet_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_schedule(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a schedule returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_fleet_schedule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new

body = DatadogAPIClient::V2::FleetScheduleCreateRequest.new({
  data: DatadogAPIClient::V2::FleetScheduleCreate.new({
    attributes: DatadogAPIClient::V2::FleetScheduleCreateAttributes.new({
      name: "Weekly Production Agent Updates",
      query: "env:prod AND service:web",
      rule: DatadogAPIClient::V2::FleetScheduleRecurrenceRule.new({
        days_of_week: [
          "Mon",
          "Wed",
          "Fri",
        ],
        maintenance_window_duration: 1200,
        start_maintenance_window: "02:00",
        timezone: "America/New_York",
      }),
      status: DatadogAPIClient::V2::FleetScheduleStatus::ACTIVE,
      version_to_latest: 0,
    }),
    type: DatadogAPIClient::V2::FleetScheduleResourceType::SCHEDULE,
  }),
})
p api_instance.create_fleet_schedule(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create a schedule returns "CREATED" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.FleetScheduleCreateRequest{
        Data: datadogV2.FleetScheduleCreate{
            Attributes: datadogV2.FleetScheduleCreateAttributes{
                Name:  "Weekly Production Agent Updates",
                Query: "env:prod AND service:web",
                Rule: datadogV2.FleetScheduleRecurrenceRule{
                    DaysOfWeek: []string{
                        "Mon",
                        "Wed",
                        "Fri",
                    },
                    MaintenanceWindowDuration: 1200,
                    StartMaintenanceWindow:    "02:00",
                    Timezone:                  "America/New_York",
                },
                Status:          datadogV2.FLEETSCHEDULESTATUS_ACTIVE.Ptr(),
                VersionToLatest: datadog.PtrInt64(0),
            },
            Type: datadogV2.FLEETSCHEDULERESOURCETYPE_SCHEDULE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateFleetSchedule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.CreateFleetSchedule(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.CreateFleetSchedule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.CreateFleetSchedule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a schedule returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetScheduleCreate;
import com.datadog.api.client.v2.model.FleetScheduleCreateAttributes;
import com.datadog.api.client.v2.model.FleetScheduleCreateRequest;
import com.datadog.api.client.v2.model.FleetScheduleRecurrenceRule;
import com.datadog.api.client.v2.model.FleetScheduleResourceType;
import com.datadog.api.client.v2.model.FleetScheduleResponse;
import com.datadog.api.client.v2.model.FleetScheduleStatus;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createFleetSchedule", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    FleetScheduleCreateRequest body =
        new FleetScheduleCreateRequest()
            .data(
                new FleetScheduleCreate()
                    .attributes(
                        new FleetScheduleCreateAttributes()
                            .name("Weekly Production Agent Updates")
                            .query("env:prod AND service:web")
                            .rule(
                                new FleetScheduleRecurrenceRule()
                                    .daysOfWeek(Arrays.asList("Mon", "Wed", "Fri"))
                                    .maintenanceWindowDuration(1200L)
                                    .startMaintenanceWindow("02:00")
                                    .timezone("America/New_York"))
                            .status(FleetScheduleStatus.ACTIVE)
                            .versionToLatest(0L))
                    .type(FleetScheduleResourceType.SCHEDULE));

    try {
      FleetScheduleResponse result = apiInstance.createFleetSchedule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#createFleetSchedule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Create a schedule returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;
use datadog_api_client::datadogV2::model::FleetScheduleCreate;
use datadog_api_client::datadogV2::model::FleetScheduleCreateAttributes;
use datadog_api_client::datadogV2::model::FleetScheduleCreateRequest;
use datadog_api_client::datadogV2::model::FleetScheduleRecurrenceRule;
use datadog_api_client::datadogV2::model::FleetScheduleResourceType;
use datadog_api_client::datadogV2::model::FleetScheduleStatus;

#[tokio::main]
async fn main() {
    let body = FleetScheduleCreateRequest::new(FleetScheduleCreate::new(
        FleetScheduleCreateAttributes::new(
            "Weekly Production Agent Updates".to_string(),
            "env:prod AND service:web".to_string(),
            FleetScheduleRecurrenceRule::new(
                vec!["Mon".to_string(), "Wed".to_string(), "Fri".to_string()],
                1200,
                "02:00".to_string(),
                "America/New_York".to_string(),
            ),
        )
        .status(FleetScheduleStatus::ACTIVE)
        .version_to_latest(0),
        FleetScheduleResourceType::SCHEDULE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateFleetSchedule", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.create_fleet_schedule(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create a schedule returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createFleetSchedule"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiCreateFleetScheduleRequest = {
  body: {
    data: {
      attributes: {
        name: "Weekly Production Agent Updates",
        query: "env:prod AND service:web",
        rule: {
          daysOfWeek: ["Mon", "Wed", "Fri"],
          maintenanceWindowDuration: 1200,
          startMaintenanceWindow: "02:00",
          timezone: "America/New_York",
        },
        status: "active",
        versionToLatest: 0,
      },
      type: "schedule",
    },
  },
};

apiInstance
  .createFleetSchedule(params)
  .then((data: v2.FleetScheduleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a schedule by ID{% #get-a-schedule-by-id %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/unstable/fleet/schedules/{id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/unstable/fleet/schedules/{id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/unstable/fleet/schedules/{id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/unstable/fleet/schedules/{id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/unstable/fleet/schedules/{id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/unstable/fleet/schedules/{id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/unstable/fleet/schedules/{id} |

### Overview



Retrieve detailed information about a specific schedule using its unique identifier.

This endpoint returns comprehensive information about a schedule, including:

- Schedule metadata (ID, name, creation/update timestamps)
- Filter query for selecting target hosts
- Recurrence rule defining when deployments are triggered
- Version strategy for package upgrades
- Current status (active or inactive)
This endpoint requires the `hosts_read` permission.


### Arguments

#### Path Parameters

| Name                 | Type   | Description                                        |
| -------------------- | ------ | -------------------------------------------------- |
| id [*required*] | string | The unique identifier of the schedule to retrieve. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single schedule.

| Parent field | Field                                         | Type     | Description                                                                                                                                 |
| ------------ | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                                          | object   | A schedule that automatically creates deployments based on a recurrence rule.                                                               |
| data         | attributes [*required*]                  | object   | Attributes of a schedule in the response.                                                                                                   |
| attributes   | created_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was created.                                                                         |
| attributes   | created_by                                    | string   | User handle of the person who created the schedule.                                                                                         |
| attributes   | name                                          | string   | Human-readable name for the schedule.                                                                                                       |
| attributes   | query                                         | string   | Query used to filter and select target hosts for scheduled deployments. Uses the Datadog query syntax.                                      |
| attributes   | rule                                          | object   | Defines the recurrence pattern for the schedule. Specifies when deployments should be automatically triggered based on maintenance windows. |
| rule         | days_of_week [*required*]                | [string] | List of days of the week when the schedule should trigger. Valid values are: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".               |
| rule         | maintenance_window_duration [*required*] | int64    | Duration of the maintenance window in minutes.                                                                                              |
| rule         | start_maintenance_window [*required*]    | string   | Start time of the maintenance window in 24-hour clock format (HH:MM). Deployments will be triggered at this time on the specified days.     |
| rule         | timezone [*required*]                    | string   | Timezone for the schedule in IANA Time Zone Database format (e.g., "America/New_York", "UTC").                                              |
| attributes   | status                                        | enum     | The status of the schedule.                                                                                                                 |
| attributes   | updated_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was last updated.                                                                    |
| attributes   | updated_by                                    | string   | User handle of the person who last updated the schedule.                                                                                    |
| attributes   | version_to_latest                             | int64    | Number of major versions behind the latest to target for upgrades.                                                                          |
| data         | id [*required*]                          | string   | Unique identifier for the schedule.                                                                                                         |
| data         | type [*required*]                        | enum     | The type of schedule resource. Allowed enum values: `schedule`                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at_unix": 1699999999,
      "created_by": "user@example.com",
      "name": "Weekly Production Agent Updates",
      "query": "env:prod AND service:web",
      "rule": {
        "days_of_week": [
          "Mon",
          "Wed",
          "Fri"
        ],
        "maintenance_window_duration": 1200,
        "start_maintenance_window": "02:00",
        "timezone": "America/New_York"
      },
      "status": "active",
      "updated_at_unix": 1699999999,
      "updated_by": "user@example.com",
      "version_to_latest": 0
    },
    "id": "abc-def-ghi-123",
    "type": "schedule"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport id="abc-def-ghi-123"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a schedule by ID returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["get_fleet_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.get_fleet_schedule(
        id="id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a schedule by ID returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_fleet_schedule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.get_fleet_schedule("id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a schedule by ID returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetFleetSchedule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.GetFleetSchedule(ctx, "id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.GetFleetSchedule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.GetFleetSchedule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a schedule by ID returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetScheduleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getFleetSchedule", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetScheduleResponse result = apiInstance.getFleetSchedule("abc-def-ghi-123");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#getFleetSchedule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Get a schedule by ID returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetFleetSchedule", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.get_fleet_schedule("id".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get a schedule by ID returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getFleetSchedule"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiGetFleetScheduleRequest = {
  id: "id",
};

apiInstance
  .getFleetSchedule(params)
  .then((data: v2.FleetScheduleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update a schedule{% #update-a-schedule %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/unstable/fleet/schedules/{id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/unstable/fleet/schedules/{id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/unstable/fleet/schedules/{id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/unstable/fleet/schedules/{id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/unstable/fleet/schedules/{id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/unstable/fleet/schedules/{id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/unstable/fleet/schedules/{id} |

### Overview



Partially update a schedule by providing only the fields you want to change.

This endpoint allows you to modify specific attributes of a schedule without affecting other fields. Common use cases include:

- Changing the schedule status between active and inactive
- Updating the maintenance window times
- Modifying the filter query to target different hosts
- Adjusting the version strategy

Only include the fields you want to update in the request body. All fields are optional in a PATCH request.
This endpoint requires the `agent_upgrade_write` permission.


### Arguments

#### Path Parameters

| Name                 | Type   | Description                                      |
| -------------------- | ------ | ------------------------------------------------ |
| id [*required*] | string | The unique identifier of the schedule to update. |

### Request

#### Body Data (required)

Request payload containing the fields to update.

{% tab title="Model" %}

| Parent field | Field                                         | Type     | Description                                                                                                                                 |
| ------------ | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                        | object   | Data for partially updating a schedule.                                                                                                     |
| data         | attributes                                    | object   | Attributes for partially updating a schedule. All fields are optional.                                                                      |
| attributes   | name                                          | string   | Human-readable name for the schedule.                                                                                                       |
| attributes   | query                                         | string   | Query used to filter and select target hosts for scheduled deployments. Uses the Datadog query syntax.                                      |
| attributes   | rule                                          | object   | Defines the recurrence pattern for the schedule. Specifies when deployments should be automatically triggered based on maintenance windows. |
| rule         | days_of_week [*required*]                | [string] | List of days of the week when the schedule should trigger. Valid values are: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".               |
| rule         | maintenance_window_duration [*required*] | int64    | Duration of the maintenance window in minutes.                                                                                              |
| rule         | start_maintenance_window [*required*]    | string   | Start time of the maintenance window in 24-hour clock format (HH:MM). Deployments will be triggered at this time on the specified days.     |
| rule         | timezone [*required*]                    | string   | Timezone for the schedule in IANA Time Zone Database format (e.g., "America/New_York", "UTC").                                              |
| attributes   | status                                        | enum     | The status of the schedule.                                                                                                                 |
| attributes   | version_to_latest                             | int64    | Number of major versions behind the latest to target for upgrades.                                                                          |
| data         | type [*required*]                        | enum     | The type of schedule resource. Allowed enum values: `schedule`                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Weekly Production Agent Updates",
      "query": "env:prod AND service:web",
      "rule": {
        "days_of_week": [
          "Mon",
          "Wed",
          "Fri"
        ],
        "maintenance_window_duration": 1200,
        "start_maintenance_window": "02:00",
        "timezone": "America/New_York"
      },
      "status": "active",
      "version_to_latest": 0
    },
    "type": "schedule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single schedule.

| Parent field | Field                                         | Type     | Description                                                                                                                                 |
| ------------ | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                                          | object   | A schedule that automatically creates deployments based on a recurrence rule.                                                               |
| data         | attributes [*required*]                  | object   | Attributes of a schedule in the response.                                                                                                   |
| attributes   | created_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was created.                                                                         |
| attributes   | created_by                                    | string   | User handle of the person who created the schedule.                                                                                         |
| attributes   | name                                          | string   | Human-readable name for the schedule.                                                                                                       |
| attributes   | query                                         | string   | Query used to filter and select target hosts for scheduled deployments. Uses the Datadog query syntax.                                      |
| attributes   | rule                                          | object   | Defines the recurrence pattern for the schedule. Specifies when deployments should be automatically triggered based on maintenance windows. |
| rule         | days_of_week [*required*]                | [string] | List of days of the week when the schedule should trigger. Valid values are: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".               |
| rule         | maintenance_window_duration [*required*] | int64    | Duration of the maintenance window in minutes.                                                                                              |
| rule         | start_maintenance_window [*required*]    | string   | Start time of the maintenance window in 24-hour clock format (HH:MM). Deployments will be triggered at this time on the specified days.     |
| rule         | timezone [*required*]                    | string   | Timezone for the schedule in IANA Time Zone Database format (e.g., "America/New_York", "UTC").                                              |
| attributes   | status                                        | enum     | The status of the schedule.                                                                                                                 |
| attributes   | updated_at_unix                               | int64    | Unix timestamp (seconds since epoch) when the schedule was last updated.                                                                    |
| attributes   | updated_by                                    | string   | User handle of the person who last updated the schedule.                                                                                    |
| attributes   | version_to_latest                             | int64    | Number of major versions behind the latest to target for upgrades.                                                                          |
| data         | id [*required*]                          | string   | Unique identifier for the schedule.                                                                                                         |
| data         | type [*required*]                        | enum     | The type of schedule resource. Allowed enum values: `schedule`                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at_unix": 1699999999,
      "created_by": "user@example.com",
      "name": "Weekly Production Agent Updates",
      "query": "env:prod AND service:web",
      "rule": {
        "days_of_week": [
          "Mon",
          "Wed",
          "Fri"
        ],
        "maintenance_window_duration": 1200,
        "start_maintenance_window": "02:00",
        "timezone": "America/New_York"
      },
      "status": "active",
      "updated_at_unix": 1699999999,
      "updated_by": "user@example.com",
      "version_to_latest": 0
    },
    "id": "abc-def-ghi-123",
    "type": "schedule"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \## Change maintenance window time
#
\# Path parametersexport id="abc-def-ghi-123"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "rule": {
        "days_of_week": [
          "Mon",
          "Wed",
          "Fri"
        ],
        "maintenance_window_duration": 240,
        "start_maintenance_window": "03:00",
        "timezone": "America/New_York"
      }
    },
    "type": "schedule"
  }
}
EOF\## Pause a schedule
#
\# Path parametersexport id="abc-def-ghi-123"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "status": "inactive"
    },
    "type": "schedule"
  }
}
EOF\## Update target hosts query
#
\# Path parametersexport id="abc-def-ghi-123"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "query": "env:prod AND service:api"
    },
    "type": "schedule"
  }
}
EOF

#####

```python
"""
Update a schedule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_schedule_patch import FleetSchedulePatch
from datadog_api_client.v2.model.fleet_schedule_patch_attributes import FleetSchedulePatchAttributes
from datadog_api_client.v2.model.fleet_schedule_patch_request import FleetSchedulePatchRequest
from datadog_api_client.v2.model.fleet_schedule_recurrence_rule import FleetScheduleRecurrenceRule
from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType
from datadog_api_client.v2.model.fleet_schedule_status import FleetScheduleStatus

body = FleetSchedulePatchRequest(
    data=FleetSchedulePatch(
        attributes=FleetSchedulePatchAttributes(
            name="Weekly Production Agent Updates",
            query="env:prod AND service:web",
            rule=FleetScheduleRecurrenceRule(
                days_of_week=[
                    "Mon",
                    "Wed",
                    "Fri",
                ],
                maintenance_window_duration=1200,
                start_maintenance_window="02:00",
                timezone="America/New_York",
            ),
            status=FleetScheduleStatus.ACTIVE,
            version_to_latest=0,
        ),
        type=FleetScheduleResourceType.SCHEDULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_fleet_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.update_fleet_schedule(id="id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update a schedule returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_fleet_schedule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new

body = DatadogAPIClient::V2::FleetSchedulePatchRequest.new({
  data: DatadogAPIClient::V2::FleetSchedulePatch.new({
    attributes: DatadogAPIClient::V2::FleetSchedulePatchAttributes.new({
      name: "Weekly Production Agent Updates",
      query: "env:prod AND service:web",
      rule: DatadogAPIClient::V2::FleetScheduleRecurrenceRule.new({
        days_of_week: [
          "Mon",
          "Wed",
          "Fri",
        ],
        maintenance_window_duration: 1200,
        start_maintenance_window: "02:00",
        timezone: "America/New_York",
      }),
      status: DatadogAPIClient::V2::FleetScheduleStatus::ACTIVE,
      version_to_latest: 0,
    }),
    type: DatadogAPIClient::V2::FleetScheduleResourceType::SCHEDULE,
  }),
})
p api_instance.update_fleet_schedule("id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Update a schedule returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.FleetSchedulePatchRequest{
        Data: datadogV2.FleetSchedulePatch{
            Attributes: &datadogV2.FleetSchedulePatchAttributes{
                Name:  datadog.PtrString("Weekly Production Agent Updates"),
                Query: datadog.PtrString("env:prod AND service:web"),
                Rule: &datadogV2.FleetScheduleRecurrenceRule{
                    DaysOfWeek: []string{
                        "Mon",
                        "Wed",
                        "Fri",
                    },
                    MaintenanceWindowDuration: 1200,
                    StartMaintenanceWindow:    "02:00",
                    Timezone:                  "America/New_York",
                },
                Status:          datadogV2.FLEETSCHEDULESTATUS_ACTIVE.Ptr(),
                VersionToLatest: datadog.PtrInt64(0),
            },
            Type: datadogV2.FLEETSCHEDULERESOURCETYPE_SCHEDULE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.UpdateFleetSchedule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.UpdateFleetSchedule(ctx, "id", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.UpdateFleetSchedule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.UpdateFleetSchedule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update a schedule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetSchedulePatch;
import com.datadog.api.client.v2.model.FleetSchedulePatchAttributes;
import com.datadog.api.client.v2.model.FleetSchedulePatchRequest;
import com.datadog.api.client.v2.model.FleetScheduleRecurrenceRule;
import com.datadog.api.client.v2.model.FleetScheduleResourceType;
import com.datadog.api.client.v2.model.FleetScheduleResponse;
import com.datadog.api.client.v2.model.FleetScheduleStatus;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateFleetSchedule", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    FleetSchedulePatchRequest body =
        new FleetSchedulePatchRequest()
            .data(
                new FleetSchedulePatch()
                    .attributes(
                        new FleetSchedulePatchAttributes()
                            .name("Weekly Production Agent Updates")
                            .query("env:prod AND service:web")
                            .rule(
                                new FleetScheduleRecurrenceRule()
                                    .daysOfWeek(Arrays.asList("Mon", "Wed", "Fri"))
                                    .maintenanceWindowDuration(1200L)
                                    .startMaintenanceWindow("02:00")
                                    .timezone("America/New_York"))
                            .status(FleetScheduleStatus.ACTIVE)
                            .versionToLatest(0L))
                    .type(FleetScheduleResourceType.SCHEDULE));

    try {
      FleetScheduleResponse result = apiInstance.updateFleetSchedule("abc-def-ghi-123", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#updateFleetSchedule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Update a schedule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;
use datadog_api_client::datadogV2::model::FleetSchedulePatch;
use datadog_api_client::datadogV2::model::FleetSchedulePatchAttributes;
use datadog_api_client::datadogV2::model::FleetSchedulePatchRequest;
use datadog_api_client::datadogV2::model::FleetScheduleRecurrenceRule;
use datadog_api_client::datadogV2::model::FleetScheduleResourceType;
use datadog_api_client::datadogV2::model::FleetScheduleStatus;

#[tokio::main]
async fn main() {
    let body = FleetSchedulePatchRequest::new(
        FleetSchedulePatch::new(FleetScheduleResourceType::SCHEDULE).attributes(
            FleetSchedulePatchAttributes::new()
                .name("Weekly Production Agent Updates".to_string())
                .query("env:prod AND service:web".to_string())
                .rule(FleetScheduleRecurrenceRule::new(
                    vec!["Mon".to_string(), "Wed".to_string(), "Fri".to_string()],
                    1200,
                    "02:00".to_string(),
                    "America/New_York".to_string(),
                ))
                .status(FleetScheduleStatus::ACTIVE)
                .version_to_latest(0),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateFleetSchedule", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.update_fleet_schedule("id".to_string(), body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Update a schedule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateFleetSchedule"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiUpdateFleetScheduleRequest = {
  body: {
    data: {
      attributes: {
        name: "Weekly Production Agent Updates",
        query: "env:prod AND service:web",
        rule: {
          daysOfWeek: ["Mon", "Wed", "Fri"],
          maintenanceWindowDuration: 1200,
          startMaintenanceWindow: "02:00",
          timezone: "America/New_York",
        },
        status: "active",
        versionToLatest: 0,
      },
      type: "schedule",
    },
  },
  id: "id",
};

apiInstance
  .updateFleetSchedule(params)
  .then((data: v2.FleetScheduleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete a schedule{% #delete-a-schedule %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/unstable/fleet/schedules/{id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/unstable/fleet/schedules/{id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/unstable/fleet/schedules/{id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/unstable/fleet/schedules/{id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/unstable/fleet/schedules/{id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/unstable/fleet/schedules/{id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/unstable/fleet/schedules/{id} |

### Overview



Delete a schedule permanently.

When you delete a schedule:

- The schedule is permanently removed and will no longer create deployments
- Any deployments already created by this schedule are not affected
- This action cannot be undone

If you want to temporarily stop a schedule from creating deployments, consider updating its status to "inactive" instead of deleting it.
This endpoint requires the `agent_upgrade_write` permission.


### Arguments

#### Path Parameters

| Name                 | Type   | Description                                      |
| -------------------- | ------ | ------------------------------------------------ |
| id [*required*] | string | The unique identifier of the schedule to delete. |

### Response

{% tab title="204" %}
Schedule successfully deleted.
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport id="abc-def-ghi-123"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a schedule returns "Schedule successfully deleted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["delete_fleet_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    api_instance.delete_fleet_schedule(
        id="id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete a schedule returns "Schedule successfully deleted." response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_fleet_schedule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
api_instance.delete_fleet_schedule("id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete a schedule returns "Schedule successfully deleted." response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.DeleteFleetSchedule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    r, err := api.DeleteFleetSchedule(ctx, "id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.DeleteFleetSchedule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete a schedule returns "Schedule successfully deleted." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteFleetSchedule", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      apiInstance.deleteFleetSchedule("abc-def-ghi-123");
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#deleteFleetSchedule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Delete a schedule returns "Schedule successfully deleted." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteFleetSchedule", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.delete_fleet_schedule("id".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Delete a schedule returns "Schedule successfully deleted." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteFleetSchedule"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiDeleteFleetScheduleRequest = {
  id: "id",
};

apiInstance
  .deleteFleetSchedule(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Trigger a schedule deployment{% #trigger-a-schedule-deployment %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/unstable/fleet/schedules/{id}/trigger |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/unstable/fleet/schedules/{id}/trigger |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/unstable/fleet/schedules/{id}/trigger      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/unstable/fleet/schedules/{id}/trigger      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/unstable/fleet/schedules/{id}/trigger     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/unstable/fleet/schedules/{id}/trigger |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/unstable/fleet/schedules/{id}/trigger |

### Overview



Manually trigger a schedule to immediately create and start a deployment.

This endpoint allows you to manually initiate a deployment using the schedule's configuration, without waiting for the next scheduled maintenance window. This is useful for:

- Testing a schedule before it runs automatically
- Performing an emergency update outside the regular maintenance window
- Creating an ad-hoc deployment with the same settings as a schedule

The deployment is created immediately with:

- The same filter query as the schedule
- The package version determined by the schedule's version strategy
- All matching hosts as targets

The manually triggered deployment is independent of the schedule and does not affect the schedule's normal recurrence pattern.
This endpoint requires the `agent_upgrade_write` permission.


### Arguments

#### Path Parameters

| Name                 | Type   | Description                                       |
| -------------------- | ------ | ------------------------------------------------- |
| id [*required*] | string | The unique identifier of the schedule to trigger. |

### Response

{% tab title="201" %}
CREATED - Deployment successfully created and started.
{% tab title="Model" %}
Response containing a single deployment.

| Parent field      | Field                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                   | data                         | object   | A deployment that defines automated configuration changes for a fleet of hosts.                                                                                                                                                                                                                                                                                                                                    |
| data              | attributes [*required*] | object   | Attributes of a deployment in the response.                                                                                                                                                                                                                                                                                                                                                                        |
| attributes        | config_operations            | [object] | Ordered list of configuration file operations to perform on the target hosts.                                                                                                                                                                                                                                                                                                                                      |
| config_operations | file_op [*required*]    | enum     | Type of file operation to perform on the target configuration file.                                                                                                                                                                                                                                                                                                                                                |
| config_operations | file_path [*required*]  | string   | Absolute path to the target configuration file on the host.                                                                                                                                                                                                                                                                                                                                                        |
| config_operations | patch                        | object   | Patch data in JSON format to apply to the configuration file. When using `merge-patch`, this object is merged with the existing configuration, allowing you to add, update, or override specific fields without replacing the entire file. The structure must match the target configuration file format (for example, YAML structure for Datadog Agent config). Not applicable when using the `delete` operation. |
| attributes        | estimated_end_time_unix      | int64    | Estimated completion time of the deployment as a Unix timestamp (seconds since epoch).                                                                                                                                                                                                                                                                                                                             |
| attributes        | filter_query                 | string   | Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.                                                                                                                                                                                                                                                                                                                    |
| attributes        | high_level_status            | string   | Current high-level status of the deployment (for example, "pending", "running", "completed", "failed").                                                                                                                                                                                                                                                                                                            |
| attributes        | hosts                        | [object] | Paginated list of hosts in this deployment with their individual statuses. Only included when fetching a single deployment by ID. Use the `limit` and `page` query parameters to navigate through pages. Pagination metadata is included in the response `meta.hosts` field.                                                                                                                                       |
| hosts             | error                        | string   | Error message if the deployment failed on this host.                                                                                                                                                                                                                                                                                                                                                               |
| hosts             | hostname                     | string   | The hostname of the agent.                                                                                                                                                                                                                                                                                                                                                                                         |
| hosts             | status                       | string   | Current deployment status for this specific host.                                                                                                                                                                                                                                                                                                                                                                  |
| hosts             | versions                     | [object] | List of packages and their versions currently installed on this host.                                                                                                                                                                                                                                                                                                                                              |
| versions          | current_version              | string   | The current version of the package on the host.                                                                                                                                                                                                                                                                                                                                                                    |
| versions          | initial_version              | string   | The initial version of the package on the host before the deployment started.                                                                                                                                                                                                                                                                                                                                      |
| versions          | package_name                 | string   | The name of the package.                                                                                                                                                                                                                                                                                                                                                                                           |
| versions          | target_version               | string   | The target version that the deployment is attempting to install.                                                                                                                                                                                                                                                                                                                                                   |
| attributes        | packages                     | [object] | List of packages to deploy to target hosts. Present only for package upgrade deployments.                                                                                                                                                                                                                                                                                                                          |
| packages          | name [*required*]       | string   | The name of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                                 |
| packages          | version [*required*]    | string   | The target version of the package to deploy.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes        | total_hosts                  | int64    | Total number of hosts targeted by this deployment.                                                                                                                                                                                                                                                                                                                                                                 |
| data              | id [*required*]         | string   | Unique identifier for the deployment.                                                                                                                                                                                                                                                                                                                                                                              |
| data              | type [*required*]       | enum     | The type of deployment resource. Allowed enum values: `deployment`                                                                                                                                                                                                                                                                                                                                                 |
|                   | meta                         | object   | Metadata for a single deployment response, including pagination information for hosts.                                                                                                                                                                                                                                                                                                                             |
| meta              | hosts                        | object   | Pagination details for the list of hosts in a deployment.                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | current_page                 | int64    | Current page index (zero-based).                                                                                                                                                                                                                                                                                                                                                                                   |
| hosts             | page_size                    | int64    | Number of hosts returned per page.                                                                                                                                                                                                                                                                                                                                                                                 |
| hosts             | total_hosts                  | int64    | Total number of hosts in this deployment.                                                                                                                                                                                                                                                                                                                                                                          |
| hosts             | total_pages                  | int64    | Total number of pages available.                                                                                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_operations": [
        {
          "file_op": "merge-patch",
          "file_path": "/datadog.yaml",
          "patch": {
            "apm_config": {
              "enabled": true
            },
            "log_level": "debug",
            "logs_enabled": true
          }
        }
      ],
      "estimated_end_time_unix": 1699999999,
      "filter_query": "env:prod AND service:web",
      "high_level_status": "pending",
      "hosts": [
        {
          "error": "",
          "hostname": "web-server-01.example.com",
          "status": "succeeded",
          "versions": [
            {
              "current_version": "7.51.0",
              "initial_version": "7.51.0",
              "package_name": "datadog-agent",
              "target_version": "7.52.0"
            }
          ]
        }
      ],
      "packages": [
        {
          "name": "datadog-agent",
          "version": "7.52.0"
        }
      ],
      "total_hosts": 42
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "deployment"
  },
  "meta": {
    "hosts": {
      "current_page": 0,
      "page_size": 50,
      "total_hosts": 150,
      "total_pages": 3
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport id="abc-def-ghi-123"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/unstable/fleet/schedules/${id}/trigger" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Trigger a schedule deployment returns "CREATED - Deployment successfully created and started." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["trigger_fleet_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.trigger_fleet_schedule(
        id="id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Trigger a schedule deployment returns "CREATED - Deployment successfully created and started." response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.trigger_fleet_schedule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::FleetAutomationAPI.new
p api_instance.trigger_fleet_schedule("id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Trigger a schedule deployment returns "CREATED - Deployment successfully created and started." response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.TriggerFleetSchedule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewFleetAutomationApi(apiClient)
    resp, r, err := api.TriggerFleetSchedule(ctx, "id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `FleetAutomationApi.TriggerFleetSchedule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `FleetAutomationApi.TriggerFleetSchedule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Trigger a schedule deployment returns "CREATED - Deployment successfully created and started."
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FleetAutomationApi;
import com.datadog.api.client.v2.model.FleetDeploymentResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.triggerFleetSchedule", true);
    FleetAutomationApi apiInstance = new FleetAutomationApi(defaultClient);

    try {
      FleetDeploymentResponse result = apiInstance.triggerFleetSchedule("abc-def-ghi-123");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetAutomationApi#triggerFleetSchedule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Trigger a schedule deployment returns "CREATED - Deployment successfully
// created and started." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fleet_automation::FleetAutomationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.TriggerFleetSchedule", true);
    let api = FleetAutomationAPI::with_config(configuration);
    let resp = api.trigger_fleet_schedule("id".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Trigger a schedule deployment returns "CREATED - Deployment successfully created and started." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.triggerFleetSchedule"] = true;
const apiInstance = new v2.FleetAutomationApi(configuration);

const params: v2.FleetAutomationApiTriggerFleetScheduleRequest = {
  id: "id",
};

apiInstance
  .triggerFleetSchedule(params)
  .then((data: v2.FleetDeploymentResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
