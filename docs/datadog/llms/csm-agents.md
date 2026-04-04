# Source: https://docs.datadoghq.com/api/latest/csm-agents.md

---
title: CSM Agents
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > CSM Agents
---

# CSM Agents

Datadog Cloud Security Management (CSM) delivers real-time threat detection and continuous configuration audits across your entire cloud infrastructure, all in a unified view for seamless collaboration and faster remediation. Go to [https://docs.datadoghq.com/security/cloud_security_management](https://docs.datadoghq.com/security/cloud_security_management) to learn more

## Get all CSM Agents{% #get-all-csm-agents %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/agents |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/csm/onboarding/agents |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/csm/onboarding/agents      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/csm/onboarding/agents      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/csm/onboarding/agents     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/csm/onboarding/agents |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/csm/onboarding/agents |

### Overview

Get the list of all CSM Agents running on your hosts and containers.

### Arguments

#### Query Strings

| Name            | Type    | Description                                                                                                       |
| --------------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| page            | integer | The page index for pagination (zero-based).                                                                       |
| size            | integer | The number of items to include in a single page.                                                                  |
| query           | string  | A search query string to filter results (for example, `hostname:COMP-T2H4J27423`).                                |
| order_direction | enum    | The sort direction for results. Use `asc` for ascending or `desc` for descending.Allowed enum values: `asc, desc` |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of CSM Agents.

| Parent field | Field                               | Type     | Description                                                                                                |
| ------------ | ----------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                                | [object] | A list of Agents.                                                                                          |
| data         | attributes                          | object   | A CSM Agent returned by the API.                                                                           |
| attributes   | agent_version                       | string   | Version of the Datadog Agent.                                                                              |
| attributes   | aws_fargate                         | string   | AWS Fargate details.                                                                                       |
| attributes   | cluster_name                        | [string] | List of cluster names associated with the Agent.                                                           |
| attributes   | datadog_agent                       | string   | Unique identifier for the Datadog Agent.                                                                   |
| attributes   | ecs_fargate_task_arn                | string   | ARN of the ECS Fargate task.                                                                               |
| attributes   | envs                                | [string] | List of environments associated with the Agent.                                                            |
| attributes   | host_id                             | int64    | ID of the host.                                                                                            |
| attributes   | hostname                            | string   | Name of the host.                                                                                          |
| attributes   | install_method_installer_version    | string   | Version of the installer used for installing the Datadog Agent.                                            |
| attributes   | install_method_tool                 | string   | Tool used for installing the Datadog Agent.                                                                |
| attributes   | is_csm_vm_containers_enabled        | boolean  | Indicates if CSM VM Containers is enabled.                                                                 |
| attributes   | is_csm_vm_hosts_enabled             | boolean  | Indicates if CSM VM Hosts is enabled.                                                                      |
| attributes   | is_cspm_enabled                     | boolean  | Indicates if CSPM is enabled.                                                                              |
| attributes   | is_cws_enabled                      | boolean  | Indicates if CWS is enabled.                                                                               |
| attributes   | is_cws_remote_configuration_enabled | boolean  | Indicates if CWS Remote Configuration is enabled.                                                          |
| attributes   | is_remote_configuration_enabled     | boolean  | Indicates if Remote Configuration is enabled.                                                              |
| attributes   | os                                  | string   | Operating system of the host.                                                                              |
| data         | id                                  | string   | The ID of the Agent.                                                                                       |
| data         | type                                | enum     | The type of the resource. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent` |
|              | meta                                | object   | Metadata related to the paginated response.                                                                |
| meta         | page_index                          | int64    | The index of the current page in the paginated results.                                                    |
| meta         | page_size                           | int64    | The number of items per page in the paginated results.                                                     |
| meta         | total_filtered                      | int64    | Total number of items that match the filter criteria.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "agent_version": "string",
        "aws_fargate": "string",
        "cluster_name": [],
        "datadog_agent": "string",
        "ecs_fargate_task_arn": "string",
        "envs": [],
        "host_id": "integer",
        "hostname": "string",
        "install_method_installer_version": "string",
        "install_method_tool": "string",
        "is_csm_vm_containers_enabled": false,
        "is_csm_vm_hosts_enabled": false,
        "is_cspm_enabled": false,
        "is_cws_enabled": false,
        "is_cws_remote_configuration_enabled": false,
        "is_remote_configuration_enabled": false,
        "os": "string"
      },
      "id": "fffffc5505f6a006fdf7cf5aae053653",
      "type": "datadog_agent"
    }
  ],
  "meta": {
    "page_index": 0,
    "page_size": 10,
    "total_filtered": 128697
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/agents" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all CSM Agents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_agents_api import CSMAgentsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMAgentsApi(api_client)
    response = api_instance.list_all_csm_agents()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all CSM Agents returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMAgentsAPI.new
p api_instance.list_all_csm_agents()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all CSM Agents returns "OK" response

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
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewCSMAgentsApi(apiClient)
    resp, r, err := api.ListAllCSMAgents(ctx, *datadogV2.NewListAllCSMAgentsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `CSMAgentsApi.ListAllCSMAgents`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `CSMAgentsApi.ListAllCSMAgents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all CSM Agents returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmAgentsApi;
import com.datadog.api.client.v2.model.CsmAgentsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmAgentsApi apiInstance = new CsmAgentsApi(defaultClient);

    try {
      CsmAgentsResponse result = apiInstance.listAllCSMAgents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmAgentsApi#listAllCSMAgents");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get all CSM Agents returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_agents::CSMAgentsAPI;
use datadog_api_client::datadogV2::api_csm_agents::ListAllCSMAgentsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMAgentsAPI::with_config(configuration);
    let resp = api
        .list_all_csm_agents(ListAllCSMAgentsOptionalParams::default())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get all CSM Agents returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMAgentsApi(configuration);

apiInstance
  .listAllCSMAgents()
  .then((data: v2.CsmAgentsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get all CSM Serverless Agents{% #get-all-csm-serverless-agents %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/serverless/agents |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/csm/onboarding/serverless/agents |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/csm/onboarding/serverless/agents      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/csm/onboarding/serverless/agents      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/csm/onboarding/serverless/agents     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/csm/onboarding/serverless/agents |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/csm/onboarding/serverless/agents |

### Overview

Get the list of all CSM Serverless Agents running on your hosts and containers.

### Arguments

#### Query Strings

| Name            | Type    | Description                                                                                                       |
| --------------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| page            | integer | The page index for pagination (zero-based).                                                                       |
| size            | integer | The number of items to include in a single page.                                                                  |
| query           | string  | A search query string to filter results (for example, `hostname:COMP-T2H4J27423`).                                |
| order_direction | enum    | The sort direction for results. Use `asc` for ascending or `desc` for descending.Allowed enum values: `asc, desc` |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of CSM Agents.

| Parent field | Field                               | Type     | Description                                                                                                |
| ------------ | ----------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                                | [object] | A list of Agents.                                                                                          |
| data         | attributes                          | object   | A CSM Agent returned by the API.                                                                           |
| attributes   | agent_version                       | string   | Version of the Datadog Agent.                                                                              |
| attributes   | aws_fargate                         | string   | AWS Fargate details.                                                                                       |
| attributes   | cluster_name                        | [string] | List of cluster names associated with the Agent.                                                           |
| attributes   | datadog_agent                       | string   | Unique identifier for the Datadog Agent.                                                                   |
| attributes   | ecs_fargate_task_arn                | string   | ARN of the ECS Fargate task.                                                                               |
| attributes   | envs                                | [string] | List of environments associated with the Agent.                                                            |
| attributes   | host_id                             | int64    | ID of the host.                                                                                            |
| attributes   | hostname                            | string   | Name of the host.                                                                                          |
| attributes   | install_method_installer_version    | string   | Version of the installer used for installing the Datadog Agent.                                            |
| attributes   | install_method_tool                 | string   | Tool used for installing the Datadog Agent.                                                                |
| attributes   | is_csm_vm_containers_enabled        | boolean  | Indicates if CSM VM Containers is enabled.                                                                 |
| attributes   | is_csm_vm_hosts_enabled             | boolean  | Indicates if CSM VM Hosts is enabled.                                                                      |
| attributes   | is_cspm_enabled                     | boolean  | Indicates if CSPM is enabled.                                                                              |
| attributes   | is_cws_enabled                      | boolean  | Indicates if CWS is enabled.                                                                               |
| attributes   | is_cws_remote_configuration_enabled | boolean  | Indicates if CWS Remote Configuration is enabled.                                                          |
| attributes   | is_remote_configuration_enabled     | boolean  | Indicates if Remote Configuration is enabled.                                                              |
| attributes   | os                                  | string   | Operating system of the host.                                                                              |
| data         | id                                  | string   | The ID of the Agent.                                                                                       |
| data         | type                                | enum     | The type of the resource. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent` |
|              | meta                                | object   | Metadata related to the paginated response.                                                                |
| meta         | page_index                          | int64    | The index of the current page in the paginated results.                                                    |
| meta         | page_size                           | int64    | The number of items per page in the paginated results.                                                     |
| meta         | total_filtered                      | int64    | Total number of items that match the filter criteria.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "agent_version": "string",
        "aws_fargate": "string",
        "cluster_name": [],
        "datadog_agent": "string",
        "ecs_fargate_task_arn": "string",
        "envs": [],
        "host_id": "integer",
        "hostname": "string",
        "install_method_installer_version": "string",
        "install_method_tool": "string",
        "is_csm_vm_containers_enabled": false,
        "is_csm_vm_hosts_enabled": false,
        "is_cspm_enabled": false,
        "is_cws_enabled": false,
        "is_cws_remote_configuration_enabled": false,
        "is_remote_configuration_enabled": false,
        "os": "string"
      },
      "id": "fffffc5505f6a006fdf7cf5aae053653",
      "type": "datadog_agent"
    }
  ],
  "meta": {
    "page_index": 0,
    "page_size": 10,
    "total_filtered": 128697
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/serverless/agents" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all CSM Serverless Agents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_agents_api import CSMAgentsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMAgentsApi(api_client)
    response = api_instance.list_all_csm_serverless_agents()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all CSM Serverless Agents returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMAgentsAPI.new
p api_instance.list_all_csm_serverless_agents()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all CSM Serverless Agents returns "OK" response

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
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewCSMAgentsApi(apiClient)
    resp, r, err := api.ListAllCSMServerlessAgents(ctx, *datadogV2.NewListAllCSMServerlessAgentsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `CSMAgentsApi.ListAllCSMServerlessAgents`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `CSMAgentsApi.ListAllCSMServerlessAgents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all CSM Serverless Agents returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmAgentsApi;
import com.datadog.api.client.v2.model.CsmAgentsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmAgentsApi apiInstance = new CsmAgentsApi(defaultClient);

    try {
      CsmAgentsResponse result = apiInstance.listAllCSMServerlessAgents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmAgentsApi#listAllCSMServerlessAgents");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get all CSM Serverless Agents returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_agents::CSMAgentsAPI;
use datadog_api_client::datadogV2::api_csm_agents::ListAllCSMServerlessAgentsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMAgentsAPI::with_config(configuration);
    let resp = api
        .list_all_csm_serverless_agents(ListAllCSMServerlessAgentsOptionalParams::default())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get all CSM Serverless Agents returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMAgentsApi(configuration);

apiInstance
  .listAllCSMServerlessAgents()
  .then((data: v2.CsmAgentsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
