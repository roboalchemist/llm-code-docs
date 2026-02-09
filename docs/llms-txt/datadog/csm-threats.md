# Source: https://docs.datadoghq.com/api/latest/csm-threats.md

---
title: CSM Threats
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > CSM Threats
---

# CSM Threats

Workload Protection monitors file, network, and process activity across your environment to detect real-time threats to your infrastructure. See [Workload Protection](https://docs.datadoghq.com/security/workload_protection/) for more information on setting up Workload Protection.

**Note**: These endpoints are split based on whether you are using the US1-FED site or not. Please reference the specific resource for the site you are using.

## Get all Workload Protection agent rules{% #get-all-workload-protection-agent-rules %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/cws/agent_rules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/cws/agent_rules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/cws/agent_rules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |

### Overview



Get the list of Workload Protection agent rules.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Arguments

#### Query Strings

| Name      | Type   | Description                |
| --------- | ------ | -------------------------- |
| policy_id | string | The ID of the Agent policy |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | [object]      | A list of Agent rules objects                                                           |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "actions": [
          {
            "filter": "string",
            "hash": {
              "field": "string"
            },
            "kill": {
              "signal": "string"
            },
            "metadata": {
              "image_tag": "string",
              "service": "string",
              "short_image": "string"
            },
            "set": {
              "append": false,
              "default_value": "string",
              "expression": "string",
              "field": "string",
              "inherited": false,
              "name": "string",
              "scope": "string",
              "size": "integer",
              "ttl": "integer",
              "value": {
                "type": "undefined"
              }
            }
          }
        ],
        "agentConstraint": "string",
        "blocking": [],
        "category": "Process Activity",
        "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
        "creationDate": 1624366480320,
        "creator": {
          "handle": "datadog.user@example.com",
          "name": "Datadog User"
        },
        "defaultRule": false,
        "description": "My Agent rule",
        "disabled": [],
        "enabled": true,
        "expression": "exec.file.name == \"sh\"",
        "filters": [],
        "monitoring": [],
        "name": "my_agent_rule",
        "product_tags": [],
        "silent": false,
        "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
        "updateDate": 1624366480320,
        "updatedAt": 1624366480320,
        "updater": {
          "handle": "datadog.user@example.com",
          "name": "Datadog User"
        },
        "version": 23
      },
      "id": "3dd-0uc-h1s",
      "type": "agent_rule"
    }
  ]
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all Workload Protection agent rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.list_csm_threats_agent_rules()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all Workload Protection agent rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new
p api_instance.list_csm_threats_agent_rules()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all Workload Protection agent rules returns "OK" response

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
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.ListCSMThreatsAgentRules(ctx, *datadogV2.NewListCSMThreatsAgentRulesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.ListCSMThreatsAgentRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.ListCSMThreatsAgentRules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all Workload Protection agent rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRulesListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    try {
      CloudWorkloadSecurityAgentRulesListResponse result = apiInstance.listCSMThreatsAgentRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#listCSMThreatsAgentRules");
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
// Get all Workload Protection agent rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::api_csm_threats::ListCSMThreatsAgentRulesOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .list_csm_threats_agent_rules(ListCSMThreatsAgentRulesOptionalParams::default())
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
 * Get all Workload Protection agent rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

apiInstance
  .listCSMThreatsAgentRules()
  .then((data: v2.CloudWorkloadSecurityAgentRulesListResponse) => {
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

## Get a Workload Protection agent rule{% #get-a-workload-protection-agent-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |

### Overview



Get the details of a specific Workload Protection agent rule.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Arguments

#### Path Parameters

| Name                            | Type   | Description              |
| ------------------------------- | ------ | ------------------------ |
| agent_rule_id [*required*] | string | The ID of the Agent rule |

#### Query Strings

| Name      | Type   | Description                |
| --------- | ------ | -------------------------- |
| policy_id | string | The ID of the Agent policy |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | object        | Object for a single Agent rule                                                          |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "actions": [
        {
          "filter": "string",
          "hash": {
            "field": "string"
          },
          "kill": {
            "signal": "string"
          },
          "metadata": {
            "image_tag": "string",
            "service": "string",
            "short_image": "string"
          },
          "set": {
            "append": false,
            "default_value": "string",
            "expression": "string",
            "field": "string",
            "inherited": false,
            "name": "string",
            "scope": "string",
            "size": "integer",
            "ttl": "integer",
            "value": {
              "type": "undefined"
            }
          }
        }
      ],
      "agentConstraint": "string",
      "blocking": [],
      "category": "Process Activity",
      "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "creationDate": 1624366480320,
      "creator": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "defaultRule": false,
      "description": "My Agent rule",
      "disabled": [],
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "monitoring": [],
      "name": "my_agent_rule",
      "product_tags": [],
      "silent": false,
      "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "version": 23
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
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
                  \# Path parametersexport agent_rule_id="3b5-v82-ns6"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/${agent_rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a Workload Protection agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.get_csm_threats_agent_rule(
        agent_rule_id=AGENT_RULE_DATA_ID,
        policy_id=POLICY_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a Workload Protection agent rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = ENV["AGENT_RULE_DATA_ID"]

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]
opts = {
  policy_id: POLICY_DATA_ID,
}
p api_instance.get_csm_threats_agent_rule(AGENT_RULE_DATA_ID, opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a Workload Protection agent rule returns "OK" response

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
	// there is a valid "agent_rule_rc" in the system
	AgentRuleDataID := os.Getenv("AGENT_RULE_DATA_ID")

	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.GetCSMThreatsAgentRule(ctx, AgentRuleDataID, *datadogV2.NewGetCSMThreatsAgentRuleOptionalParameters().WithPolicyId(PolicyDataID))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.GetCSMThreatsAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.GetCSMThreatsAgentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a Workload Protection agent rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.api.CsmThreatsApi.GetCSMThreatsAgentRuleOptionalParameters;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "agent_rule_rc" in the system
    String AGENT_RULE_DATA_ID = System.getenv("AGENT_RULE_DATA_ID");

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    try {
      CloudWorkloadSecurityAgentRuleResponse result =
          apiInstance.getCSMThreatsAgentRule(
              AGENT_RULE_DATA_ID,
              new GetCSMThreatsAgentRuleOptionalParameters().policyId(POLICY_DATA_ID));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#getCSMThreatsAgentRule");
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
// Get a Workload Protection agent rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::api_csm_threats::GetCSMThreatsAgentRuleOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "agent_rule_rc" in the system
    let agent_rule_data_id = std::env::var("AGENT_RULE_DATA_ID").unwrap();

    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .get_csm_threats_agent_rule(
            agent_rule_data_id.clone(),
            GetCSMThreatsAgentRuleOptionalParams::default().policy_id(policy_data_id.clone()),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Get a Workload Protection agent rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "agent_rule_rc" in the system
const AGENT_RULE_DATA_ID = process.env.AGENT_RULE_DATA_ID as string;

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiGetCSMThreatsAgentRuleRequest = {
  agentRuleId: AGENT_RULE_DATA_ID,
  policyId: POLICY_DATA_ID,
};

apiInstance
  .getCSMThreatsAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
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

## Create a Workload Protection agent rule{% #create-a-workload-protection-agent-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/remote_config/products/cws/agent_rules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/remote_config/products/cws/agent_rules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/remote_config/products/cws/agent_rules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules |

### Overview



Create a new Workload Protection agent rule with the given parameters.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Request

#### Body Data (required)

The definition of the new agent rule

{% tab title="Model" %}

| Parent field | Field                        | Type          | Description                                                                             |
| ------------ | ---------------------------- | ------------- | --------------------------------------------------------------------------------------- |
|              | data [*required*]       | object        | Object for a single Agent rule                                                          |
| data         | attributes [*required*] | object        | Create a new Cloud Workload Security Agent rule.                                        |
| attributes   | actions                      | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter                       | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash                         | object        | Hash file specified by the field attribute                                              |
| hash         | field                        | string        | The field of the hash action                                                            |
| actions      | kill                         | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal                       | string        | Supported signals for the kill system call                                              |
| actions      | metadata                     | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag                    | string        | The image tag of the metadata action                                                    |
| metadata     | service                      | string        | The service of the metadata action                                                      |
| metadata     | short_image                  | string        | The short image of the metadata action                                                  |
| actions      | set                          | object        | The set action applied on the scope matching the rule                                   |
| set          | append                       | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value                | string        | The default value of the set action                                                     |
| set          | expression                   | string        | The expression of the set action.                                                       |
| set          | field                        | string        | The field of the set action                                                             |
| set          | inherited                    | boolean       | Whether the value should be inherited.                                                  |
| set          | name                         | string        | The name of the set action                                                              |
| set          | scope                        | string        | The scope of the set action.                                                            |
| set          | size                         | int64         | The size of the set action.                                                             |
| set          | ttl                          | int64         | The time to live of the set action.                                                     |
| set          | value                        |  <oneOf> | The value of the set action                                                             |
| value        | Option 1                     | string        |
| value        | Option 2                     | integer       |
| value        | Option 3                     | boolean       |
| attributes   | agent_version                | string        | Constrain the rule to specific versions of the Datadog Agent.                           |
| attributes   | blocking                     | [string]      | The blocking policies that the rule belongs to.                                         |
| attributes   | description                  | string        | The description of the Agent rule.                                                      |
| attributes   | disabled                     | [string]      | The disabled policies that the rule belongs to.                                         |
| attributes   | enabled                      | boolean       | Whether the Agent rule is enabled.                                                      |
| attributes   | expression [*required*] | string        | The SECL expression of the Agent rule.                                                  |
| attributes   | filters                      | [string]      | The platforms the Agent rule is supported on.                                           |
| attributes   | monitoring                   | [string]      | The monitoring policies that the rule belongs to.                                       |
| attributes   | name [*required*]       | string        | The name of the Agent rule.                                                             |
| attributes   | policy_id                    | string        | The ID of the policy where the Agent rule is saved.                                     |
| attributes   | product_tags                 | [string]      | The list of product tags associated with the rule.                                      |
| attributes   | silent                       | boolean       | Whether the rule is silent.                                                             |
| data         | type [*required*]       | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "data": {
    "attributes": {
      "description": "My Agent rule",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "agent_version": "> 7.60",
      "filters": [],
      "name": "examplecsmthreat",
      "policy_id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
      "product_tags": []
    },
    "type": "agent_rule"
  }
}
```

##### 

```json
{
  "data": {
    "attributes": {
      "description": "My Agent rule with set action",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "name": "examplecsmthreat",
      "policy_id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
      "product_tags": [],
      "actions": [
        {
          "set": {
            "name": "test_set",
            "value": "test_value",
            "scope": "process",
            "inherited": true
          }
        },
        {
          "hash": {
            "field": "exec.file"
          }
        }
      ]
    },
    "type": "agent_rule"
  }
}
```

##### 

```json
{
  "data": {
    "attributes": {
      "description": "My Agent rule with set action with expression",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "name": "examplecsmthreat",
      "policy_id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
      "product_tags": [],
      "actions": [
        {
          "set": {
            "name": "test_set",
            "expression": "exec.file.path",
            "default_value": "/dev/null",
            "scope": "process"
          }
        }
      ]
    },
    "type": "agent_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | object        | Object for a single Agent rule                                                          |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "actions": [
        {
          "filter": "string",
          "hash": {
            "field": "string"
          },
          "kill": {
            "signal": "string"
          },
          "metadata": {
            "image_tag": "string",
            "service": "string",
            "short_image": "string"
          },
          "set": {
            "append": false,
            "default_value": "string",
            "expression": "string",
            "field": "string",
            "inherited": false,
            "name": "string",
            "scope": "string",
            "size": "integer",
            "ttl": "integer",
            "value": {
              "type": "undefined"
            }
          }
        }
      ],
      "agentConstraint": "string",
      "blocking": [],
      "category": "Process Activity",
      "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "creationDate": 1624366480320,
      "creator": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "defaultRule": false,
      "description": "My Agent rule",
      "disabled": [],
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "monitoring": [],
      "name": "my_agent_rule",
      "product_tags": [],
      "silent": false,
      "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "version": 23
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
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

{% tab title="409" %}
Conflict
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "My Agent rule",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "agent_version": "> 7.60",
      "filters": [],
      "name": "examplecsmthreat",
      "policy_id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
      "product_tags": []
    },
    "type": "agent_rule"
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "My Agent rule with set action",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "name": "examplecsmthreat",
      "policy_id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
      "product_tags": [],
      "actions": [
        {
          "set": {
            "name": "test_set",
            "value": "test_value",
            "scope": "process",
            "inherited": true
          }
        },
        {
          "hash": {
            "field": "exec.file"
          }
        }
      ]
    },
    "type": "agent_rule"
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "My Agent rule with set action with expression",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "name": "examplecsmthreat",
      "policy_id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
      "product_tags": [],
      "actions": [
        {
          "set": {
            "name": "test_set",
            "expression": "exec.file.path",
            "default_value": "/dev/null",
            "scope": "process"
          }
        }
      ]
    },
    "type": "agent_rule"
  }
}
EOF
                        
##### 

```go
// Create a Workload Protection agent rule returns "OK" response

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
	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	body := datadogV2.CloudWorkloadSecurityAgentRuleCreateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentRuleCreateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentRuleCreateAttributes{
				Description:  datadog.PtrString("My Agent rule"),
				Enabled:      datadog.PtrBool(true),
				Expression:   `exec.file.name == "sh"`,
				AgentVersion: datadog.PtrString("> 7.60"),
				Filters:      []string{},
				Name:         "examplecsmthreat",
				PolicyId:     datadog.PtrString(PolicyDataID),
				ProductTags:  []string{},
			},
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTRULETYPE_AGENT_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.CreateCSMThreatsAgentRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.CreateCSMThreatsAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.CreateCSMThreatsAgentRule`:\n%s\n", responseContent)
}
```

##### 

```go
// Create a Workload Protection agent rule with set action returns "OK" response

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
	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	body := datadogV2.CloudWorkloadSecurityAgentRuleCreateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentRuleCreateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentRuleCreateAttributes{
				Description: datadog.PtrString("My Agent rule with set action"),
				Enabled:     datadog.PtrBool(true),
				Expression:  `exec.file.name == "sh"`,
				Filters:     []string{},
				Name:        "examplecsmthreat",
				PolicyId:    datadog.PtrString(PolicyDataID),
				ProductTags: []string{},
				Actions: []datadogV2.CloudWorkloadSecurityAgentRuleAction{
					{
						Set: &datadogV2.CloudWorkloadSecurityAgentRuleActionSet{
							Name: datadog.PtrString("test_set"),
							Value: &datadogV2.CloudWorkloadSecurityAgentRuleActionSetValue{
								String: datadog.PtrString("test_value")},
							Scope:     datadog.PtrString("process"),
							Inherited: datadog.PtrBool(true),
						},
					},
					{
						Hash: &datadogV2.CloudWorkloadSecurityAgentRuleActionHash{
							Field: datadog.PtrString("exec.file"),
						},
					},
				},
			},
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTRULETYPE_AGENT_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.CreateCSMThreatsAgentRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.CreateCSMThreatsAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.CreateCSMThreatsAgentRule`:\n%s\n", responseContent)
}
```

##### 

```go
// Create a Workload Protection agent rule with set action with expression returns "OK" response

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
	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	body := datadogV2.CloudWorkloadSecurityAgentRuleCreateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentRuleCreateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentRuleCreateAttributes{
				Description: datadog.PtrString("My Agent rule with set action with expression"),
				Enabled:     datadog.PtrBool(true),
				Expression:  `exec.file.name == "sh"`,
				Filters:     []string{},
				Name:        "examplecsmthreat",
				PolicyId:    datadog.PtrString(PolicyDataID),
				ProductTags: []string{},
				Actions: []datadogV2.CloudWorkloadSecurityAgentRuleAction{
					{
						Set: &datadogV2.CloudWorkloadSecurityAgentRuleActionSet{
							Name:         datadog.PtrString("test_set"),
							Expression:   datadog.PtrString("exec.file.path"),
							DefaultValue: datadog.PtrString("/dev/null"),
							Scope:        datadog.PtrString("process"),
						},
					},
				},
			},
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTRULETYPE_AGENT_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.CreateCSMThreatsAgentRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.CreateCSMThreatsAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.CreateCSMThreatsAgentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a Workload Protection agent rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateRequest;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    CloudWorkloadSecurityAgentRuleCreateRequest body =
        new CloudWorkloadSecurityAgentRuleCreateRequest()
            .data(
                new CloudWorkloadSecurityAgentRuleCreateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentRuleCreateAttributes()
                            .description("My Agent rule")
                            .enabled(true)
                            .expression("""
exec.file.name == "sh"
""")
                            .agentVersion("> 7.60")
                            .name("examplecsmthreat")
                            .policyId(POLICY_DATA_ID))
                    .type(CloudWorkloadSecurityAgentRuleType.AGENT_RULE));

    try {
      CloudWorkloadSecurityAgentRuleResponse result = apiInstance.createCSMThreatsAgentRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#createCSMThreatsAgentRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Create a Workload Protection agent rule with set action returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleAction;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleActionHash;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleActionSet;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleActionSetValue;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateRequest;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    CloudWorkloadSecurityAgentRuleCreateRequest body =
        new CloudWorkloadSecurityAgentRuleCreateRequest()
            .data(
                new CloudWorkloadSecurityAgentRuleCreateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentRuleCreateAttributes()
                            .description("My Agent rule with set action")
                            .enabled(true)
                            .expression("""
exec.file.name == "sh"
""")
                            .name("examplecsmthreat")
                            .policyId(POLICY_DATA_ID)
                            .actions(
                                Arrays.asList(
                                    new CloudWorkloadSecurityAgentRuleAction()
                                        .set(
                                            new CloudWorkloadSecurityAgentRuleActionSet()
                                                .name("test_set")
                                                .value(
                                                    new CloudWorkloadSecurityAgentRuleActionSetValue(
                                                        "test_value"))
                                                .scope("process")
                                                .inherited(true)),
                                    new CloudWorkloadSecurityAgentRuleAction()
                                        .hash(
                                            new CloudWorkloadSecurityAgentRuleActionHash()
                                                .field("exec.file")))))
                    .type(CloudWorkloadSecurityAgentRuleType.AGENT_RULE));

    try {
      CloudWorkloadSecurityAgentRuleResponse result = apiInstance.createCSMThreatsAgentRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#createCSMThreatsAgentRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Create a Workload Protection agent rule with set action with expression returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleAction;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleActionSet;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateRequest;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    CloudWorkloadSecurityAgentRuleCreateRequest body =
        new CloudWorkloadSecurityAgentRuleCreateRequest()
            .data(
                new CloudWorkloadSecurityAgentRuleCreateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentRuleCreateAttributes()
                            .description("My Agent rule with set action with expression")
                            .enabled(true)
                            .expression("""
exec.file.name == "sh"
""")
                            .name("examplecsmthreat")
                            .policyId(POLICY_DATA_ID)
                            .actions(
                                Collections.singletonList(
                                    new CloudWorkloadSecurityAgentRuleAction()
                                        .set(
                                            new CloudWorkloadSecurityAgentRuleActionSet()
                                                .name("test_set")
                                                .expression("exec.file.path")
                                                .defaultValue("/dev/null")
                                                .scope("process")))))
                    .type(CloudWorkloadSecurityAgentRuleType.AGENT_RULE));

    try {
      CloudWorkloadSecurityAgentRuleResponse result = apiInstance.createCSMThreatsAgentRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#createCSMThreatsAgentRule");
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

```python
"""
Create a Workload Protection agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_attributes import (
    CloudWorkloadSecurityAgentRuleCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_data import (
    CloudWorkloadSecurityAgentRuleCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleCreateRequest(
    data=CloudWorkloadSecurityAgentRuleCreateData(
        attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
            description="My Agent rule",
            enabled=True,
            expression='exec.file.name == "sh"',
            agent_version="> 7.60",
            filters=[],
            name="examplecsmthreat",
            policy_id=POLICY_DATA_ID,
            product_tags=[],
        ),
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_csm_threats_agent_rule(body=body)

    print(response)
```

##### 

```python
"""
Create a Workload Protection agent rule with set action returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action import CloudWorkloadSecurityAgentRuleAction
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_hash import (
    CloudWorkloadSecurityAgentRuleActionHash,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set import (
    CloudWorkloadSecurityAgentRuleActionSet,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_attributes import (
    CloudWorkloadSecurityAgentRuleCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_data import (
    CloudWorkloadSecurityAgentRuleCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleCreateRequest(
    data=CloudWorkloadSecurityAgentRuleCreateData(
        attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
            description="My Agent rule with set action",
            enabled=True,
            expression='exec.file.name == "sh"',
            filters=[],
            name="examplecsmthreat",
            policy_id=POLICY_DATA_ID,
            product_tags=[],
            actions=[
                CloudWorkloadSecurityAgentRuleAction(
                    set=CloudWorkloadSecurityAgentRuleActionSet(
                        name="test_set",
                        value="test_value",
                        scope="process",
                        inherited=True,
                    ),
                ),
                CloudWorkloadSecurityAgentRuleAction(
                    hash=CloudWorkloadSecurityAgentRuleActionHash(
                        field="exec.file",
                    ),
                ),
            ],
        ),
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_csm_threats_agent_rule(body=body)

    print(response)
```

##### 

```python
"""
Create a Workload Protection agent rule with set action with expression returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action import CloudWorkloadSecurityAgentRuleAction
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set import (
    CloudWorkloadSecurityAgentRuleActionSet,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_attributes import (
    CloudWorkloadSecurityAgentRuleCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_data import (
    CloudWorkloadSecurityAgentRuleCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleCreateRequest(
    data=CloudWorkloadSecurityAgentRuleCreateData(
        attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
            description="My Agent rule with set action with expression",
            enabled=True,
            expression='exec.file.name == "sh"',
            filters=[],
            name="examplecsmthreat",
            policy_id=POLICY_DATA_ID,
            product_tags=[],
            actions=[
                CloudWorkloadSecurityAgentRuleAction(
                    set=CloudWorkloadSecurityAgentRuleActionSet(
                        name="test_set",
                        expression="exec.file.path",
                        default_value="/dev/null",
                        scope="process",
                    ),
                ),
            ],
        ),
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_csm_threats_agent_rule(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a Workload Protection agent rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateAttributes.new({
      description: "My Agent rule",
      enabled: true,
      expression: 'exec.file.name == "sh"',
      agent_version: "> 7.60",
      filters: [],
      name: "examplecsmthreat",
      policy_id: POLICY_DATA_ID,
      product_tags: [],
    }),
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
  }),
})
p api_instance.create_csm_threats_agent_rule(body)
```

##### 

```ruby
# Create a Workload Protection agent rule with set action returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateAttributes.new({
      description: "My Agent rule with set action",
      enabled: true,
      expression: 'exec.file.name == "sh"',
      filters: [],
      name: "examplecsmthreat",
      policy_id: POLICY_DATA_ID,
      product_tags: [],
      actions: [
        DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleAction.new({
          set: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleActionSet.new({
            name: "test_set",
            value: "test_value",
            scope: "process",
            inherited: true,
          }),
        }),
        DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleAction.new({
          _hash: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleActionHash.new({
            field: "exec.file",
          }),
        }),
      ],
    }),
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
  }),
})
p api_instance.create_csm_threats_agent_rule(body)
```

##### 

```ruby
# Create a Workload Protection agent rule with set action with expression returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateAttributes.new({
      description: "My Agent rule with set action with expression",
      enabled: true,
      expression: 'exec.file.name == "sh"',
      filters: [],
      name: "examplecsmthreat",
      policy_id: POLICY_DATA_ID,
      product_tags: [],
      actions: [
        DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleAction.new({
          set: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleActionSet.new({
            name: "test_set",
            expression: "exec.file.path",
            default_value: "/dev/null",
            scope: "process",
          }),
        }),
      ],
    }),
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
  }),
})
p api_instance.create_csm_threats_agent_rule(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a Workload Protection agent rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateRequest;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleType;

#[tokio::main]
async fn main() {
    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let body = CloudWorkloadSecurityAgentRuleCreateRequest::new(
        CloudWorkloadSecurityAgentRuleCreateData::new(
            CloudWorkloadSecurityAgentRuleCreateAttributes::new(
                r#"exec.file.name == "sh""#.to_string(),
                "examplecsmthreat".to_string(),
            )
            .agent_version("> 7.60".to_string())
            .description("My Agent rule".to_string())
            .enabled(true)
            .filters(vec![])
            .policy_id(policy_data_id.clone())
            .product_tags(vec![]),
            CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.create_csm_threats_agent_rule(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Create a Workload Protection agent rule with set action returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleAction;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleActionHash;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleActionSet;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleActionSetValue;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateRequest;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleType;

#[tokio::main]
async fn main() {
    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let body = CloudWorkloadSecurityAgentRuleCreateRequest::new(
        CloudWorkloadSecurityAgentRuleCreateData::new(
            CloudWorkloadSecurityAgentRuleCreateAttributes::new(
                r#"exec.file.name == "sh""#.to_string(),
                "examplecsmthreat".to_string(),
            )
            .actions(Some(vec![
                CloudWorkloadSecurityAgentRuleAction::new().set(
                    CloudWorkloadSecurityAgentRuleActionSet::new()
                        .inherited(true)
                        .name("test_set".to_string())
                        .scope("process".to_string())
                        .value(CloudWorkloadSecurityAgentRuleActionSetValue::String(
                            "test_value".to_string(),
                        )),
                ),
                CloudWorkloadSecurityAgentRuleAction::new().hash(
                    CloudWorkloadSecurityAgentRuleActionHash::new().field("exec.file".to_string()),
                ),
            ]))
            .description("My Agent rule with set action".to_string())
            .enabled(true)
            .filters(vec![])
            .policy_id(policy_data_id.clone())
            .product_tags(vec![]),
            CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.create_csm_threats_agent_rule(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Create a Workload Protection agent rule with set action with expression returns
// "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleAction;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleActionSet;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateRequest;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleType;

#[tokio::main]
async fn main() {
    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let body = CloudWorkloadSecurityAgentRuleCreateRequest::new(
        CloudWorkloadSecurityAgentRuleCreateData::new(
            CloudWorkloadSecurityAgentRuleCreateAttributes::new(
                r#"exec.file.name == "sh""#.to_string(),
                "examplecsmthreat".to_string(),
            )
            .actions(Some(vec![CloudWorkloadSecurityAgentRuleAction::new().set(
                CloudWorkloadSecurityAgentRuleActionSet::new()
                    .default_value("/dev/null".to_string())
                    .expression("exec.file.path".to_string())
                    .name("test_set".to_string())
                    .scope("process".to_string()),
            )]))
            .description("My Agent rule with set action with expression".to_string())
            .enabled(true)
            .filters(vec![])
            .policy_id(policy_data_id.clone())
            .product_tags(vec![]),
            CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.create_csm_threats_agent_rule(body).await;
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
 * Create a Workload Protection agent rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiCreateCSMThreatsAgentRuleRequest = {
  body: {
    data: {
      attributes: {
        description: "My Agent rule",
        enabled: true,
        expression: `exec.file.name == "sh"`,
        agentVersion: "> 7.60",
        filters: [],
        name: "examplecsmthreat",
        policyId: POLICY_DATA_ID,
        productTags: [],
      },
      type: "agent_rule",
    },
  },
};

apiInstance
  .createCSMThreatsAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Create a Workload Protection agent rule with set action returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiCreateCSMThreatsAgentRuleRequest = {
  body: {
    data: {
      attributes: {
        description: "My Agent rule with set action",
        enabled: true,
        expression: `exec.file.name == "sh"`,
        filters: [],
        name: "examplecsmthreat",
        policyId: POLICY_DATA_ID,
        productTags: [],
        actions: [
          {
            set: {
              name: "test_set",
              value: "test_value",
              scope: "process",
              inherited: true,
            },
          },
          {
            hash: {
              field: "exec.file",
            },
          },
        ],
      },
      type: "agent_rule",
    },
  },
};

apiInstance
  .createCSMThreatsAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Create a Workload Protection agent rule with set action with expression returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiCreateCSMThreatsAgentRuleRequest = {
  body: {
    data: {
      attributes: {
        description: "My Agent rule with set action with expression",
        enabled: true,
        expression: `exec.file.name == "sh"`,
        filters: [],
        name: "examplecsmthreat",
        policyId: POLICY_DATA_ID,
        productTags: [],
        actions: [
          {
            set: {
              name: "test_set",
              expression: "exec.file.path",
              defaultValue: "/dev/null",
              scope: "process",
            },
          },
        ],
      },
      type: "agent_rule",
    },
  },
};

apiInstance
  .createCSMThreatsAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
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

## Update a Workload Protection agent rule{% #update-a-workload-protection-agent-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |

### Overview



Update a specific Workload Protection Agent rule. Returns the agent rule object when the request is successful.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Arguments

#### Path Parameters

| Name                            | Type   | Description              |
| ------------------------------- | ------ | ------------------------ |
| agent_rule_id [*required*] | string | The ID of the Agent rule |

#### Query Strings

| Name      | Type   | Description                |
| --------- | ------ | -------------------------- |
| policy_id | string | The ID of the Agent policy |

### Request

#### Body Data (required)

New definition of the agent rule

{% tab title="Model" %}

| Parent field | Field                        | Type          | Description                                                                             |
| ------------ | ---------------------------- | ------------- | --------------------------------------------------------------------------------------- |
|              | data [*required*]       | object        | Object for a single Agent rule                                                          |
| data         | attributes [*required*] | object        | Update an existing Cloud Workload Security Agent rule                                   |
| attributes   | actions                      | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter                       | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash                         | object        | Hash file specified by the field attribute                                              |
| hash         | field                        | string        | The field of the hash action                                                            |
| actions      | kill                         | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal                       | string        | Supported signals for the kill system call                                              |
| actions      | metadata                     | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag                    | string        | The image tag of the metadata action                                                    |
| metadata     | service                      | string        | The service of the metadata action                                                      |
| metadata     | short_image                  | string        | The short image of the metadata action                                                  |
| actions      | set                          | object        | The set action applied on the scope matching the rule                                   |
| set          | append                       | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value                | string        | The default value of the set action                                                     |
| set          | expression                   | string        | The expression of the set action.                                                       |
| set          | field                        | string        | The field of the set action                                                             |
| set          | inherited                    | boolean       | Whether the value should be inherited.                                                  |
| set          | name                         | string        | The name of the set action                                                              |
| set          | scope                        | string        | The scope of the set action.                                                            |
| set          | size                         | int64         | The size of the set action.                                                             |
| set          | ttl                          | int64         | The time to live of the set action.                                                     |
| set          | value                        |  <oneOf> | The value of the set action                                                             |
| value        | Option 1                     | string        |
| value        | Option 2                     | integer       |
| value        | Option 3                     | boolean       |
| attributes   | agent_version                | string        | Constrain the rule to specific versions of the Datadog Agent                            |
| attributes   | blocking                     | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | description                  | string        | The description of the Agent rule                                                       |
| attributes   | disabled                     | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled                      | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression                   | string        | The SECL expression of the Agent rule                                                   |
| attributes   | monitoring                   | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | policy_id                    | string        | The ID of the policy where the Agent rule is saved                                      |
| attributes   | product_tags                 | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent                       | boolean       | Whether the rule is silent.                                                             |
| data         | id                           | string        | The ID of the Agent rule                                                                |
| data         | type [*required*]       | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Test Agent rule",
      "enabled": true,
      "expression": "exec.file.name == \"sh\""
    },
    "type": "agent_rule",
    "id": "3dd-0uc-h1s"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | object        | Object for a single Agent rule                                                          |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "actions": [
        {
          "filter": "string",
          "hash": {
            "field": "string"
          },
          "kill": {
            "signal": "string"
          },
          "metadata": {
            "image_tag": "string",
            "service": "string",
            "short_image": "string"
          },
          "set": {
            "append": false,
            "default_value": "string",
            "expression": "string",
            "field": "string",
            "inherited": false,
            "name": "string",
            "scope": "string",
            "size": "integer",
            "ttl": "integer",
            "value": {
              "type": "undefined"
            }
          }
        }
      ],
      "agentConstraint": "string",
      "blocking": [],
      "category": "Process Activity",
      "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "creationDate": 1624366480320,
      "creator": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "defaultRule": false,
      "description": "My Agent rule",
      "disabled": [],
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "monitoring": [],
      "name": "my_agent_rule",
      "product_tags": [],
      "silent": false,
      "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "version": 23
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
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

{% tab title="409" %}
Concurrent Modification
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
                  \# Path parametersexport agent_rule_id="3b5-v82-ns6"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/${agent_rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {},
    "type": "agent_rule"
  }
}
EOF
                
##### 

```python
"""
Update a Workload Protection agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_attributes import (
    CloudWorkloadSecurityAgentRuleUpdateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_data import (
    CloudWorkloadSecurityAgentRuleUpdateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_request import (
    CloudWorkloadSecurityAgentRuleUpdateRequest,
)

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleUpdateRequest(
    data=CloudWorkloadSecurityAgentRuleUpdateData(
        attributes=CloudWorkloadSecurityAgentRuleUpdateAttributes(
            description="My Agent rule",
            enabled=True,
            expression='exec.file.name == "sh"',
            policy_id=POLICY_DATA_ID,
            product_tags=[],
        ),
        id=AGENT_RULE_DATA_ID,
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.update_csm_threats_agent_rule(
        agent_rule_id=AGENT_RULE_DATA_ID, policy_id=POLICY_DATA_ID, body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a Workload Protection agent rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = ENV["AGENT_RULE_DATA_ID"]

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleUpdateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleUpdateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleUpdateAttributes.new({
      description: "My Agent rule",
      enabled: true,
      expression: 'exec.file.name == "sh"',
      policy_id: POLICY_DATA_ID,
      product_tags: [],
    }),
    id: AGENT_RULE_DATA_ID,
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
  }),
})
opts = {
  policy_id: POLICY_DATA_ID,
}
p api_instance.update_csm_threats_agent_rule(AGENT_RULE_DATA_ID, body, opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Update a Workload Protection agent rule returns "OK" response

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
	// there is a valid "agent_rule_rc" in the system
	AgentRuleDataID := os.Getenv("AGENT_RULE_DATA_ID")

	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	body := datadogV2.CloudWorkloadSecurityAgentRuleUpdateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentRuleUpdateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentRuleUpdateAttributes{
				Description: datadog.PtrString("My Agent rule"),
				Enabled:     datadog.PtrBool(true),
				Expression:  datadog.PtrString(`exec.file.name == "sh"`),
				PolicyId:    datadog.PtrString(PolicyDataID),
				ProductTags: []string{},
			},
			Id:   datadog.PtrString(AgentRuleDataID),
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTRULETYPE_AGENT_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.UpdateCSMThreatsAgentRule(ctx, AgentRuleDataID, body, *datadogV2.NewUpdateCSMThreatsAgentRuleOptionalParameters().WithPolicyId(PolicyDataID))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.UpdateCSMThreatsAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.UpdateCSMThreatsAgentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a Workload Protection agent rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.api.CsmThreatsApi.UpdateCSMThreatsAgentRuleOptionalParameters;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleType;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleUpdateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleUpdateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "agent_rule_rc" in the system
    String AGENT_RULE_DATA_ID = System.getenv("AGENT_RULE_DATA_ID");

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    CloudWorkloadSecurityAgentRuleUpdateRequest body =
        new CloudWorkloadSecurityAgentRuleUpdateRequest()
            .data(
                new CloudWorkloadSecurityAgentRuleUpdateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentRuleUpdateAttributes()
                            .description("My Agent rule")
                            .enabled(true)
                            .expression("""
exec.file.name == "sh"
""")
                            .policyId(POLICY_DATA_ID))
                    .id(AGENT_RULE_DATA_ID)
                    .type(CloudWorkloadSecurityAgentRuleType.AGENT_RULE));

    try {
      CloudWorkloadSecurityAgentRuleResponse result =
          apiInstance.updateCSMThreatsAgentRule(
              AGENT_RULE_DATA_ID,
              body,
              new UpdateCSMThreatsAgentRuleOptionalParameters().policyId(POLICY_DATA_ID));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#updateCSMThreatsAgentRule");
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
// Update a Workload Protection agent rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::api_csm_threats::UpdateCSMThreatsAgentRuleOptionalParams;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleType;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleUpdateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleUpdateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "agent_rule_rc" in the system
    let agent_rule_data_id = std::env::var("AGENT_RULE_DATA_ID").unwrap();

    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let body = CloudWorkloadSecurityAgentRuleUpdateRequest::new(
        CloudWorkloadSecurityAgentRuleUpdateData::new(
            CloudWorkloadSecurityAgentRuleUpdateAttributes::new()
                .description("My Agent rule".to_string())
                .enabled(true)
                .expression(r#"exec.file.name == "sh""#.to_string())
                .policy_id(policy_data_id.clone())
                .product_tags(vec![]),
            CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
        )
        .id(agent_rule_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .update_csm_threats_agent_rule(
            agent_rule_data_id.clone(),
            body,
            UpdateCSMThreatsAgentRuleOptionalParams::default().policy_id(policy_data_id.clone()),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Update a Workload Protection agent rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "agent_rule_rc" in the system
const AGENT_RULE_DATA_ID = process.env.AGENT_RULE_DATA_ID as string;

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiUpdateCSMThreatsAgentRuleRequest = {
  body: {
    data: {
      attributes: {
        description: "My Agent rule",
        enabled: true,
        expression: `exec.file.name == "sh"`,
        policyId: POLICY_DATA_ID,
        productTags: [],
      },
      id: AGENT_RULE_DATA_ID,
      type: "agent_rule",
    },
  },
  agentRuleId: AGENT_RULE_DATA_ID,
  policyId: POLICY_DATA_ID,
};

apiInstance
  .updateCSMThreatsAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
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

## Delete a Workload Protection agent rule{% #delete-a-workload-protection-agent-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id} |

### Overview



Delete a specific Workload Protection agent rule.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Arguments

#### Path Parameters

| Name                            | Type   | Description              |
| ------------------------------- | ------ | ------------------------ |
| agent_rule_id [*required*] | string | The ID of the Agent rule |

#### Query Strings

| Name      | Type   | Description                |
| --------- | ------ | -------------------------- |
| policy_id | string | The ID of the Agent policy |

### Response

{% tab title="204" %}
OK
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
                  \# Path parametersexport agent_rule_id="3b5-v82-ns6"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/agent_rules/${agent_rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a Workload Protection agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    api_instance.delete_csm_threats_agent_rule(
        agent_rule_id=AGENT_RULE_DATA_ID,
        policy_id=POLICY_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a Workload Protection agent rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = ENV["AGENT_RULE_DATA_ID"]

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]
opts = {
  policy_id: POLICY_DATA_ID,
}
api_instance.delete_csm_threats_agent_rule(AGENT_RULE_DATA_ID, opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a Workload Protection agent rule returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "agent_rule_rc" in the system
	AgentRuleDataID := os.Getenv("AGENT_RULE_DATA_ID")

	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	r, err := api.DeleteCSMThreatsAgentRule(ctx, AgentRuleDataID, *datadogV2.NewDeleteCSMThreatsAgentRuleOptionalParameters().WithPolicyId(PolicyDataID))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.DeleteCSMThreatsAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a Workload Protection agent rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.api.CsmThreatsApi.DeleteCSMThreatsAgentRuleOptionalParameters;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "agent_rule_rc" in the system
    String AGENT_RULE_DATA_ID = System.getenv("AGENT_RULE_DATA_ID");

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    try {
      apiInstance.deleteCSMThreatsAgentRule(
          AGENT_RULE_DATA_ID,
          new DeleteCSMThreatsAgentRuleOptionalParameters().policyId(POLICY_DATA_ID));
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#deleteCSMThreatsAgentRule");
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
// Delete a Workload Protection agent rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::api_csm_threats::DeleteCSMThreatsAgentRuleOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "agent_rule_rc" in the system
    let agent_rule_data_id = std::env::var("AGENT_RULE_DATA_ID").unwrap();

    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .delete_csm_threats_agent_rule(
            agent_rule_data_id.clone(),
            DeleteCSMThreatsAgentRuleOptionalParams::default().policy_id(policy_data_id.clone()),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Delete a Workload Protection agent rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "agent_rule_rc" in the system
const AGENT_RULE_DATA_ID = process.env.AGENT_RULE_DATA_ID as string;

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiDeleteCSMThreatsAgentRuleRequest = {
  agentRuleId: AGENT_RULE_DATA_ID,
  policyId: POLICY_DATA_ID,
};

apiInstance
  .deleteCSMThreatsAgentRule(params)
  .then((data: any) => {
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

## Get all Workload Protection policies{% #get-all-workload-protection-policies %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/policy |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/policy |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/cws/policy      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/cws/policy      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/cws/policy     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/policy |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy |

### Overview



Get the list of Workload Protection policies.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of Agent policies

| Parent field | Field                | Type     | Description                                                                                                                     |
| ------------ | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
|              | data                 | [object] | A list of Agent policy objects                                                                                                  |
| data         | attributes           | object   | A Cloud Workload Security Agent policy returned by the API                                                                      |
| attributes   | blockingRulesCount   | int32    | The number of rules with the blocking feature in this policy                                                                    |
| attributes   | datadogManaged       | boolean  | Whether the policy is managed by Datadog                                                                                        |
| attributes   | description          | string   | The description of the policy                                                                                                   |
| attributes   | disabledRulesCount   | int32    | The number of rules that are disabled in this policy                                                                            |
| attributes   | enabled              | boolean  | Whether the Agent policy is enabled                                                                                             |
| attributes   | hostTags             | [string] | The host tags defining where this policy is deployed                                                                            |
| attributes   | hostTagsLists        | [array]  | The host tags defining where this policy is deployed, the inner values are linked with AND, the outer values are linked with OR |
| attributes   | monitoringRulesCount | int32    | The number of rules in the monitoring state in this policy                                                                      |
| attributes   | name                 | string   | The name of the policy                                                                                                          |
| attributes   | pinned               | boolean  | Whether the policy is pinned                                                                                                    |
| attributes   | policyType           | string   | The type of the policy                                                                                                          |
| attributes   | policyVersion        | string   | The version of the policy                                                                                                       |
| attributes   | priority             | int64    | The priority of the policy                                                                                                      |
| attributes   | ruleCount            | int32    | The number of rules in this policy                                                                                              |
| attributes   | updateDate           | int64    | Timestamp in milliseconds when the policy was last updated                                                                      |
| attributes   | updatedAt            | int64    | When the policy was last updated, timestamp in milliseconds                                                                     |
| attributes   | updater              | object   | The attributes of the user who last updated the policy                                                                          |
| updater      | handle               | string   | The handle of the user                                                                                                          |
| updater      | name                 | string   | The name of the user                                                                                                            |
| attributes   | versions             | [object] | The versions of the policy                                                                                                      |
| versions     | date                 | string   | The date and time the version was created                                                                                       |
| versions     | name                 | string   | The version of the policy                                                                                                       |
| data         | id                   | string   | The ID of the Agent policy                                                                                                      |
| data         | type                 | enum     | The type of the resource, must always be `policy` Allowed enum values: `policy`                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "blockingRulesCount": 100,
        "datadogManaged": false,
        "description": "My agent policy",
        "disabledRulesCount": 100,
        "enabled": true,
        "hostTags": [],
        "hostTagsLists": [],
        "monitoringRulesCount": 100,
        "name": "my_agent_policy",
        "pinned": false,
        "policyType": "policy",
        "policyVersion": "1",
        "priority": 10,
        "ruleCount": 100,
        "updateDate": 1624366480320,
        "updatedAt": 1624366480320,
        "updater": {
          "handle": "datadog.user@example.com",
          "name": "Datadog User"
        },
        "versions": [
          {
            "date": "string",
            "name": "1.47.0-rc2"
          }
        ]
      },
      "id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
      "type": "policy"
    }
  ]
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all Workload Protection policies returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.list_csm_threats_agent_policies()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all Workload Protection policies returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new
p api_instance.list_csm_threats_agent_policies()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all Workload Protection policies returns "OK" response

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
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.ListCSMThreatsAgentPolicies(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.ListCSMThreatsAgentPolicies`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.ListCSMThreatsAgentPolicies`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all Workload Protection policies returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPoliciesListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    try {
      CloudWorkloadSecurityAgentPoliciesListResponse result =
          apiInstance.listCSMThreatsAgentPolicies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#listCSMThreatsAgentPolicies");
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
// Get all Workload Protection policies returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.list_csm_threats_agent_policies().await;
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
 * Get all Workload Protection policies returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

apiInstance
  .listCSMThreatsAgentPolicies()
  .then((data: v2.CloudWorkloadSecurityAgentPoliciesListResponse) => {
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

## Get a Workload Protection policy{% #get-a-workload-protection-policy %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                           |
| ----------------- | -------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/cws/policy/{policy_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/cws/policy/{policy_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |

### Overview



Get the details of a specific Workload Protection policy.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Arguments

#### Path Parameters

| Name                        | Type   | Description                |
| --------------------------- | ------ | -------------------------- |
| policy_id [*required*] | string | The ID of the Agent policy |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent policy

| Parent field | Field                | Type     | Description                                                                                                                     |
| ------------ | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
|              | data                 | object   | Object for a single Agent policy                                                                                                |
| data         | attributes           | object   | A Cloud Workload Security Agent policy returned by the API                                                                      |
| attributes   | blockingRulesCount   | int32    | The number of rules with the blocking feature in this policy                                                                    |
| attributes   | datadogManaged       | boolean  | Whether the policy is managed by Datadog                                                                                        |
| attributes   | description          | string   | The description of the policy                                                                                                   |
| attributes   | disabledRulesCount   | int32    | The number of rules that are disabled in this policy                                                                            |
| attributes   | enabled              | boolean  | Whether the Agent policy is enabled                                                                                             |
| attributes   | hostTags             | [string] | The host tags defining where this policy is deployed                                                                            |
| attributes   | hostTagsLists        | [array]  | The host tags defining where this policy is deployed, the inner values are linked with AND, the outer values are linked with OR |
| attributes   | monitoringRulesCount | int32    | The number of rules in the monitoring state in this policy                                                                      |
| attributes   | name                 | string   | The name of the policy                                                                                                          |
| attributes   | pinned               | boolean  | Whether the policy is pinned                                                                                                    |
| attributes   | policyType           | string   | The type of the policy                                                                                                          |
| attributes   | policyVersion        | string   | The version of the policy                                                                                                       |
| attributes   | priority             | int64    | The priority of the policy                                                                                                      |
| attributes   | ruleCount            | int32    | The number of rules in this policy                                                                                              |
| attributes   | updateDate           | int64    | Timestamp in milliseconds when the policy was last updated                                                                      |
| attributes   | updatedAt            | int64    | When the policy was last updated, timestamp in milliseconds                                                                     |
| attributes   | updater              | object   | The attributes of the user who last updated the policy                                                                          |
| updater      | handle               | string   | The handle of the user                                                                                                          |
| updater      | name                 | string   | The name of the user                                                                                                            |
| attributes   | versions             | [object] | The versions of the policy                                                                                                      |
| versions     | date                 | string   | The date and time the version was created                                                                                       |
| versions     | name                 | string   | The version of the policy                                                                                                       |
| data         | id                   | string   | The ID of the Agent policy                                                                                                      |
| data         | type                 | enum     | The type of the resource, must always be `policy` Allowed enum values: `policy`                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "blockingRulesCount": 100,
      "datadogManaged": false,
      "description": "My agent policy",
      "disabledRulesCount": 100,
      "enabled": true,
      "hostTags": [],
      "hostTagsLists": [],
      "monitoringRulesCount": 100,
      "name": "my_agent_policy",
      "pinned": false,
      "policyType": "policy",
      "policyVersion": "1",
      "priority": 10,
      "ruleCount": 100,
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "versions": [
        {
          "date": "string",
          "name": "1.47.0-rc2"
        }
      ]
    },
    "id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
    "type": "policy"
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
                  \# Path parametersexport policy_id="6517fcc1-cec7-4394-a655-8d6e9d085255"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/${policy_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a Workload Protection policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.get_csm_threats_agent_policy(
        policy_id=POLICY_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a Workload Protection policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]
p api_instance.get_csm_threats_agent_policy(POLICY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a Workload Protection policy returns "OK" response

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
	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.GetCSMThreatsAgentPolicy(ctx, PolicyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.GetCSMThreatsAgentPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.GetCSMThreatsAgentPolicy`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a Workload Protection policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    try {
      CloudWorkloadSecurityAgentPolicyResponse result =
          apiInstance.getCSMThreatsAgentPolicy(POLICY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#getCSMThreatsAgentPolicy");
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
// Get a Workload Protection policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .get_csm_threats_agent_policy(policy_data_id.clone())
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
 * Get a Workload Protection policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiGetCSMThreatsAgentPolicyRequest = {
  policyId: POLICY_DATA_ID,
};

apiInstance
  .getCSMThreatsAgentPolicy(params)
  .then((data: v2.CloudWorkloadSecurityAgentPolicyResponse) => {
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

## Create a Workload Protection policy{% #create-a-workload-protection-policy %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/policy |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/policy |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/remote_config/products/cws/policy      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/remote_config/products/cws/policy      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/remote_config/products/cws/policy     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/policy |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy |

### Overview



Create a new Workload Protection policy with the given parameters.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Request

#### Body Data (required)

The definition of the new Agent policy

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                     |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Object for a single Agent rule                                                                                                  |
| data         | attributes [*required*] | object   | Create a new Cloud Workload Security Agent policy                                                                               |
| attributes   | description                  | string   | The description of the policy                                                                                                   |
| attributes   | enabled                      | boolean  | Whether the policy is enabled                                                                                                   |
| attributes   | hostTags                     | [string] | The host tags defining where this policy is deployed                                                                            |
| attributes   | hostTagsLists                | [array]  | The host tags defining where this policy is deployed, the inner values are linked with AND, the outer values are linked with OR |
| attributes   | name [*required*]       | string   | The name of the policy                                                                                                          |
| data         | type [*required*]       | enum     | The type of the resource, must always be `policy` Allowed enum values: `policy`                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "My agent policy",
      "enabled": true,
      "hostTagsLists": [
        [
          "env:test"
        ]
      ],
      "name": "my_agent_policy_2"
    },
    "type": "policy"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent policy

| Parent field | Field                | Type     | Description                                                                                                                     |
| ------------ | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
|              | data                 | object   | Object for a single Agent policy                                                                                                |
| data         | attributes           | object   | A Cloud Workload Security Agent policy returned by the API                                                                      |
| attributes   | blockingRulesCount   | int32    | The number of rules with the blocking feature in this policy                                                                    |
| attributes   | datadogManaged       | boolean  | Whether the policy is managed by Datadog                                                                                        |
| attributes   | description          | string   | The description of the policy                                                                                                   |
| attributes   | disabledRulesCount   | int32    | The number of rules that are disabled in this policy                                                                            |
| attributes   | enabled              | boolean  | Whether the Agent policy is enabled                                                                                             |
| attributes   | hostTags             | [string] | The host tags defining where this policy is deployed                                                                            |
| attributes   | hostTagsLists        | [array]  | The host tags defining where this policy is deployed, the inner values are linked with AND, the outer values are linked with OR |
| attributes   | monitoringRulesCount | int32    | The number of rules in the monitoring state in this policy                                                                      |
| attributes   | name                 | string   | The name of the policy                                                                                                          |
| attributes   | pinned               | boolean  | Whether the policy is pinned                                                                                                    |
| attributes   | policyType           | string   | The type of the policy                                                                                                          |
| attributes   | policyVersion        | string   | The version of the policy                                                                                                       |
| attributes   | priority             | int64    | The priority of the policy                                                                                                      |
| attributes   | ruleCount            | int32    | The number of rules in this policy                                                                                              |
| attributes   | updateDate           | int64    | Timestamp in milliseconds when the policy was last updated                                                                      |
| attributes   | updatedAt            | int64    | When the policy was last updated, timestamp in milliseconds                                                                     |
| attributes   | updater              | object   | The attributes of the user who last updated the policy                                                                          |
| updater      | handle               | string   | The handle of the user                                                                                                          |
| updater      | name                 | string   | The name of the user                                                                                                            |
| attributes   | versions             | [object] | The versions of the policy                                                                                                      |
| versions     | date                 | string   | The date and time the version was created                                                                                       |
| versions     | name                 | string   | The version of the policy                                                                                                       |
| data         | id                   | string   | The ID of the Agent policy                                                                                                      |
| data         | type                 | enum     | The type of the resource, must always be `policy` Allowed enum values: `policy`                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "blockingRulesCount": 100,
      "datadogManaged": false,
      "description": "My agent policy",
      "disabledRulesCount": 100,
      "enabled": true,
      "hostTags": [],
      "hostTagsLists": [],
      "monitoringRulesCount": 100,
      "name": "my_agent_policy",
      "pinned": false,
      "policyType": "policy",
      "policyVersion": "1",
      "priority": 10,
      "ruleCount": 100,
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "versions": [
        {
          "date": "string",
          "name": "1.47.0-rc2"
        }
      ]
    },
    "id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
    "type": "policy"
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

{% tab title="409" %}
Conflict
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "My agent policy",
      "enabled": true,
      "hostTagsLists": [
        [
          "env:test"
        ]
      ],
      "name": "my_agent_policy_2"
    },
    "type": "policy"
  }
}
EOF
                        
##### 

```go
// Create a Workload Protection policy returns "OK" response

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
	body := datadogV2.CloudWorkloadSecurityAgentPolicyCreateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentPolicyCreateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentPolicyCreateAttributes{
				Description: datadog.PtrString("My agent policy"),
				Enabled:     datadog.PtrBool(true),
				HostTagsLists: [][]string{
					{
						"env:test",
					},
				},
				Name: "my_agent_policy_2",
			},
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTPOLICYTYPE_POLICY,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.CreateCSMThreatsAgentPolicy(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.CreateCSMThreatsAgentPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.CreateCSMThreatsAgentPolicy`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a Workload Protection policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyCreateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyCreateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyCreateRequest;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    CloudWorkloadSecurityAgentPolicyCreateRequest body =
        new CloudWorkloadSecurityAgentPolicyCreateRequest()
            .data(
                new CloudWorkloadSecurityAgentPolicyCreateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentPolicyCreateAttributes()
                            .description("My agent policy")
                            .enabled(true)
                            .hostTagsLists(
                                Collections.singletonList(Collections.singletonList("env:test")))
                            .name("my_agent_policy_2"))
                    .type(CloudWorkloadSecurityAgentPolicyType.POLICY));

    try {
      CloudWorkloadSecurityAgentPolicyResponse result =
          apiInstance.createCSMThreatsAgentPolicy(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#createCSMThreatsAgentPolicy");
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

```python
"""
Create a Workload Protection policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_attributes import (
    CloudWorkloadSecurityAgentPolicyCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_data import (
    CloudWorkloadSecurityAgentPolicyCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_request import (
    CloudWorkloadSecurityAgentPolicyCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import CloudWorkloadSecurityAgentPolicyType

body = CloudWorkloadSecurityAgentPolicyCreateRequest(
    data=CloudWorkloadSecurityAgentPolicyCreateData(
        attributes=CloudWorkloadSecurityAgentPolicyCreateAttributes(
            description="My agent policy",
            enabled=True,
            host_tags_lists=[
                [
                    "env:test",
                ],
            ],
            name="my_agent_policy_2",
        ),
        type=CloudWorkloadSecurityAgentPolicyType.POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_csm_threats_agent_policy(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a Workload Protection policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyCreateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyCreateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyCreateAttributes.new({
      description: "My agent policy",
      enabled: true,
      host_tags_lists: [
        [
          "env:test",
        ],
      ],
      name: "my_agent_policy_2",
    }),
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyType::POLICY,
  }),
})
p api_instance.create_csm_threats_agent_policy(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a Workload Protection policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyCreateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyCreateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyCreateRequest;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyType;

#[tokio::main]
async fn main() {
    let body = CloudWorkloadSecurityAgentPolicyCreateRequest::new(
        CloudWorkloadSecurityAgentPolicyCreateData::new(
            CloudWorkloadSecurityAgentPolicyCreateAttributes::new("my_agent_policy_2".to_string())
                .description("My agent policy".to_string())
                .enabled(true)
                .host_tags_lists(vec![vec!["env:test".to_string()]]),
            CloudWorkloadSecurityAgentPolicyType::POLICY,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.create_csm_threats_agent_policy(body).await;
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
 * Create a Workload Protection policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

const params: v2.CSMThreatsApiCreateCSMThreatsAgentPolicyRequest = {
  body: {
    data: {
      attributes: {
        description: "My agent policy",
        enabled: true,
        hostTagsLists: [["env:test"]],
        name: "my_agent_policy_2",
      },
      type: "policy",
    },
  },
};

apiInstance
  .createCSMThreatsAgentPolicy(params)
  .then((data: v2.CloudWorkloadSecurityAgentPolicyResponse) => {
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

## Update a Workload Protection policy{% #update-a-workload-protection-policy %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/remote_config/products/cws/policy/{policy_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/remote_config/products/cws/policy/{policy_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |

### Overview



Update a specific Workload Protection policy. Returns the policy object when the request is successful.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Arguments

#### Path Parameters

| Name                        | Type   | Description                |
| --------------------------- | ------ | -------------------------- |
| policy_id [*required*] | string | The ID of the Agent policy |

### Request

#### Body Data (required)

New definition of the Agent policy

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                     |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Object for a single Agent policy                                                                                                |
| data         | attributes [*required*] | object   | Update an existing Cloud Workload Security Agent policy                                                                         |
| attributes   | description                  | string   | The description of the policy                                                                                                   |
| attributes   | enabled                      | boolean  | Whether the policy is enabled                                                                                                   |
| attributes   | hostTags                     | [string] | The host tags defining where this policy is deployed                                                                            |
| attributes   | hostTagsLists                | [array]  | The host tags defining where this policy is deployed, the inner values are linked with AND, the outer values are linked with OR |
| attributes   | name                         | string   | The name of the policy                                                                                                          |
| data         | id                           | string   | The ID of the Agent policy                                                                                                      |
| data         | type [*required*]       | enum     | The type of the resource, must always be `policy` Allowed enum values: `policy`                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Updated agent policy",
      "enabled": true,
      "hostTagsLists": [
        [
          "env:test"
        ]
      ],
      "name": "updated_agent_policy"
    },
    "id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
    "type": "policy"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent policy

| Parent field | Field                | Type     | Description                                                                                                                     |
| ------------ | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
|              | data                 | object   | Object for a single Agent policy                                                                                                |
| data         | attributes           | object   | A Cloud Workload Security Agent policy returned by the API                                                                      |
| attributes   | blockingRulesCount   | int32    | The number of rules with the blocking feature in this policy                                                                    |
| attributes   | datadogManaged       | boolean  | Whether the policy is managed by Datadog                                                                                        |
| attributes   | description          | string   | The description of the policy                                                                                                   |
| attributes   | disabledRulesCount   | int32    | The number of rules that are disabled in this policy                                                                            |
| attributes   | enabled              | boolean  | Whether the Agent policy is enabled                                                                                             |
| attributes   | hostTags             | [string] | The host tags defining where this policy is deployed                                                                            |
| attributes   | hostTagsLists        | [array]  | The host tags defining where this policy is deployed, the inner values are linked with AND, the outer values are linked with OR |
| attributes   | monitoringRulesCount | int32    | The number of rules in the monitoring state in this policy                                                                      |
| attributes   | name                 | string   | The name of the policy                                                                                                          |
| attributes   | pinned               | boolean  | Whether the policy is pinned                                                                                                    |
| attributes   | policyType           | string   | The type of the policy                                                                                                          |
| attributes   | policyVersion        | string   | The version of the policy                                                                                                       |
| attributes   | priority             | int64    | The priority of the policy                                                                                                      |
| attributes   | ruleCount            | int32    | The number of rules in this policy                                                                                              |
| attributes   | updateDate           | int64    | Timestamp in milliseconds when the policy was last updated                                                                      |
| attributes   | updatedAt            | int64    | When the policy was last updated, timestamp in milliseconds                                                                     |
| attributes   | updater              | object   | The attributes of the user who last updated the policy                                                                          |
| updater      | handle               | string   | The handle of the user                                                                                                          |
| updater      | name                 | string   | The name of the user                                                                                                            |
| attributes   | versions             | [object] | The versions of the policy                                                                                                      |
| versions     | date                 | string   | The date and time the version was created                                                                                       |
| versions     | name                 | string   | The version of the policy                                                                                                       |
| data         | id                   | string   | The ID of the Agent policy                                                                                                      |
| data         | type                 | enum     | The type of the resource, must always be `policy` Allowed enum values: `policy`                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "blockingRulesCount": 100,
      "datadogManaged": false,
      "description": "My agent policy",
      "disabledRulesCount": 100,
      "enabled": true,
      "hostTags": [],
      "hostTagsLists": [],
      "monitoringRulesCount": 100,
      "name": "my_agent_policy",
      "pinned": false,
      "policyType": "policy",
      "policyVersion": "1",
      "priority": 10,
      "ruleCount": 100,
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "versions": [
        {
          "date": "string",
          "name": "1.47.0-rc2"
        }
      ]
    },
    "id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
    "type": "policy"
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

{% tab title="409" %}
Concurrent Modification
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
                          \# Path parametersexport policy_id="6517fcc1-cec7-4394-a655-8d6e9d085255"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/${policy_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Updated agent policy",
      "enabled": true,
      "hostTagsLists": [
        [
          "env:test"
        ]
      ],
      "name": "updated_agent_policy"
    },
    "id": "6517fcc1-cec7-4394-a655-8d6e9d085255",
    "type": "policy"
  }
}
EOF
                        
##### 

```go
// Update a Workload Protection policy returns "OK" response

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
	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	body := datadogV2.CloudWorkloadSecurityAgentPolicyUpdateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentPolicyUpdateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentPolicyUpdateAttributes{
				Description: datadog.PtrString("Updated agent policy"),
				Enabled:     datadog.PtrBool(true),
				HostTagsLists: [][]string{
					{
						"env:test",
					},
				},
				Name: datadog.PtrString("updated_agent_policy"),
			},
			Id:   datadog.PtrString(PolicyDataID),
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTPOLICYTYPE_POLICY,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.UpdateCSMThreatsAgentPolicy(ctx, PolicyDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.UpdateCSMThreatsAgentPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.UpdateCSMThreatsAgentPolicy`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a Workload Protection policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyType;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyUpdateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyUpdateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentPolicyUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    CloudWorkloadSecurityAgentPolicyUpdateRequest body =
        new CloudWorkloadSecurityAgentPolicyUpdateRequest()
            .data(
                new CloudWorkloadSecurityAgentPolicyUpdateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentPolicyUpdateAttributes()
                            .description("Updated agent policy")
                            .enabled(true)
                            .hostTagsLists(
                                Collections.singletonList(Collections.singletonList("env:test")))
                            .name("updated_agent_policy"))
                    .id(POLICY_DATA_ID)
                    .type(CloudWorkloadSecurityAgentPolicyType.POLICY));

    try {
      CloudWorkloadSecurityAgentPolicyResponse result =
          apiInstance.updateCSMThreatsAgentPolicy(POLICY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#updateCSMThreatsAgentPolicy");
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

```python
"""
Update a Workload Protection policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import CloudWorkloadSecurityAgentPolicyType
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_attributes import (
    CloudWorkloadSecurityAgentPolicyUpdateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_data import (
    CloudWorkloadSecurityAgentPolicyUpdateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_request import (
    CloudWorkloadSecurityAgentPolicyUpdateRequest,
)

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentPolicyUpdateRequest(
    data=CloudWorkloadSecurityAgentPolicyUpdateData(
        attributes=CloudWorkloadSecurityAgentPolicyUpdateAttributes(
            description="Updated agent policy",
            enabled=True,
            host_tags_lists=[
                [
                    "env:test",
                ],
            ],
            name="updated_agent_policy",
        ),
        id=POLICY_DATA_ID,
        type=CloudWorkloadSecurityAgentPolicyType.POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.update_csm_threats_agent_policy(policy_id=POLICY_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a Workload Protection policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyUpdateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyUpdateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyUpdateAttributes.new({
      description: "Updated agent policy",
      enabled: true,
      host_tags_lists: [
        [
          "env:test",
        ],
      ],
      name: "updated_agent_policy",
    }),
    id: POLICY_DATA_ID,
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentPolicyType::POLICY,
  }),
})
p api_instance.update_csm_threats_agent_policy(POLICY_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update a Workload Protection policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyType;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyUpdateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyUpdateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentPolicyUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let body = CloudWorkloadSecurityAgentPolicyUpdateRequest::new(
        CloudWorkloadSecurityAgentPolicyUpdateData::new(
            CloudWorkloadSecurityAgentPolicyUpdateAttributes::new()
                .description("Updated agent policy".to_string())
                .enabled(true)
                .host_tags_lists(vec![vec!["env:test".to_string()]])
                .name("updated_agent_policy".to_string()),
            CloudWorkloadSecurityAgentPolicyType::POLICY,
        )
        .id(policy_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .update_csm_threats_agent_policy(policy_data_id.clone(), body)
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
 * Update a Workload Protection policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiUpdateCSMThreatsAgentPolicyRequest = {
  body: {
    data: {
      attributes: {
        description: "Updated agent policy",
        enabled: true,
        hostTagsLists: [["env:test"]],
        name: "updated_agent_policy",
      },
      id: POLICY_DATA_ID,
      type: "policy",
    },
  },
  policyId: POLICY_DATA_ID,
};

apiInstance
  .updateCSMThreatsAgentPolicy(params)
  .then((data: v2.CloudWorkloadSecurityAgentPolicyResponse) => {
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

## Delete a Workload Protection policy{% #delete-a-workload-protection-policy %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/remote_config/products/cws/policy/{policy_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/remote_config/products/cws/policy/{policy_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/{policy_id} |

### Overview



Delete a specific Workload Protection policy.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Arguments

#### Path Parameters

| Name                        | Type   | Description                |
| --------------------------- | ------ | -------------------------- |
| policy_id [*required*] | string | The ID of the Agent policy |

### Response

{% tab title="202" %}
OK
{% /tab %}

{% tab title="204" %}
OK
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
                  \# Path parametersexport policy_id="6517fcc1-cec7-4394-a655-8d6e9d085255"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/${policy_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a Workload Protection policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    api_instance.delete_csm_threats_agent_policy(
        policy_id=POLICY_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a Workload Protection policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = ENV["POLICY_DATA_ID"]
api_instance.delete_csm_threats_agent_policy(POLICY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a Workload Protection policy returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "policy_rc" in the system
	PolicyDataID := os.Getenv("POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	r, err := api.DeleteCSMThreatsAgentPolicy(ctx, PolicyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.DeleteCSMThreatsAgentPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a Workload Protection policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "policy_rc" in the system
    String POLICY_DATA_ID = System.getenv("POLICY_DATA_ID");

    try {
      apiInstance.deleteCSMThreatsAgentPolicy(POLICY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#deleteCSMThreatsAgentPolicy");
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
// Delete a Workload Protection policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "policy_rc" in the system
    let policy_data_id = std::env::var("POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .delete_csm_threats_agent_policy(policy_data_id.clone())
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
 * Delete a Workload Protection policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "policy_rc" in the system
const POLICY_DATA_ID = process.env.POLICY_DATA_ID as string;

const params: v2.CSMThreatsApiDeleteCSMThreatsAgentPolicyRequest = {
  policyId: POLICY_DATA_ID,
};

apiInstance
  .deleteCSMThreatsAgentPolicy(params)
  .then((data: any) => {
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

## Download the Workload Protection policy{% #download-the-workload-protection-policy %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/cws/policy/download |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/cws/policy/download |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/cws/policy/download      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/cws/policy/download      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/cws/policy/download     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/cws/policy/download |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/download |

### Overview



The download endpoint generates a Workload Protection policy file from your currently active Workload Protection agent rules, and downloads them as a `.policy` file. This file can then be deployed to your agents to update the policy running in your environment.

**Note**: This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/cws/policy/download" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Download the Workload Protection policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.download_csm_threats_policy()

    print(response.read())
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Download the Workload Protection policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new
p api_instance.download_csm_threats_policy()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Download the Workload Protection policy returns "OK" response

package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.DownloadCSMThreatsPolicy(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.DownloadCSMThreatsPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := ioutil.ReadAll(resp)
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.DownloadCSMThreatsPolicy`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Download the Workload Protection policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import java.io.File;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    try {
      File result = apiInstance.downloadCSMThreatsPolicy();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#downloadCSMThreatsPolicy");
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
// Download the Workload Protection policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.download_csm_threats_policy().await;
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
 * Download the Workload Protection policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

apiInstance
  .downloadCSMThreatsPolicy()
  .then((data: client.HttpFile) => {
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

## Get all Workload Protection agent rules (US1-FED){% #get-all-workload-protection-agent-rules-us1-fed %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/security_monitoring/cloud_workload_security/agent_rules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/security_monitoring/cloud_workload_security/agent_rules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |

### Overview



Get the list of agent rules.

**Note**: This endpoint should only be used for the Government (US1-FED) site.
This endpoint requires the `security_monitoring_cws_agent_rules_read` permission.


### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | [object]      | A list of Agent rules objects                                                           |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "actions": [
          {
            "filter": "string",
            "hash": {
              "field": "string"
            },
            "kill": {
              "signal": "string"
            },
            "metadata": {
              "image_tag": "string",
              "service": "string",
              "short_image": "string"
            },
            "set": {
              "append": false,
              "default_value": "string",
              "expression": "string",
              "field": "string",
              "inherited": false,
              "name": "string",
              "scope": "string",
              "size": "integer",
              "ttl": "integer",
              "value": {
                "type": "undefined"
              }
            }
          }
        ],
        "agentConstraint": "string",
        "blocking": [],
        "category": "Process Activity",
        "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
        "creationDate": 1624366480320,
        "creator": {
          "handle": "datadog.user@example.com",
          "name": "Datadog User"
        },
        "defaultRule": false,
        "description": "My Agent rule",
        "disabled": [],
        "enabled": true,
        "expression": "exec.file.name == \"sh\"",
        "filters": [],
        "monitoring": [],
        "name": "my_agent_rule",
        "product_tags": [],
        "silent": false,
        "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
        "updateDate": 1624366480320,
        "updatedAt": 1624366480320,
        "updater": {
          "handle": "datadog.user@example.com",
          "name": "Datadog User"
        },
        "version": 23
      },
      "id": "3dd-0uc-h1s",
      "type": "agent_rule"
    }
  ]
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all Workload Protection agent rules (US1-FED) returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.list_cloud_workload_security_agent_rules()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all Workload Protection agent rules (US1-FED) returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new
p api_instance.list_cloud_workload_security_agent_rules()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all Workload Protection agent rules (US1-FED) returns "OK" response

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
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.ListCloudWorkloadSecurityAgentRules(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.ListCloudWorkloadSecurityAgentRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.ListCloudWorkloadSecurityAgentRules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all Workload Protection agent rules (US1-FED) returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRulesListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    try {
      CloudWorkloadSecurityAgentRulesListResponse result =
          apiInstance.listCloudWorkloadSecurityAgentRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CsmThreatsApi#listCloudWorkloadSecurityAgentRules");
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
// Get all Workload Protection agent rules (US1-FED) returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.list_cloud_workload_security_agent_rules().await;
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
 * Get all Workload Protection agent rules (US1-FED) returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

apiInstance
  .listCloudWorkloadSecurityAgentRules()
  .then((data: v2.CloudWorkloadSecurityAgentRulesListResponse) => {
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

## Get a Workload Protection agent rule (US1-FED){% #get-a-workload-protection-agent-rule-us1-fed %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                     |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |

### Overview



Get the details of a specific agent rule.

**Note**: This endpoint should only be used for the Government (US1-FED) site.
This endpoint requires the `security_monitoring_cws_agent_rules_read` permission.


### Arguments

#### Path Parameters

| Name                            | Type   | Description              |
| ------------------------------- | ------ | ------------------------ |
| agent_rule_id [*required*] | string | The ID of the Agent rule |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | object        | Object for a single Agent rule                                                          |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "actions": [
        {
          "filter": "string",
          "hash": {
            "field": "string"
          },
          "kill": {
            "signal": "string"
          },
          "metadata": {
            "image_tag": "string",
            "service": "string",
            "short_image": "string"
          },
          "set": {
            "append": false,
            "default_value": "string",
            "expression": "string",
            "field": "string",
            "inherited": false,
            "name": "string",
            "scope": "string",
            "size": "integer",
            "ttl": "integer",
            "value": {
              "type": "undefined"
            }
          }
        }
      ],
      "agentConstraint": "string",
      "blocking": [],
      "category": "Process Activity",
      "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "creationDate": 1624366480320,
      "creator": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "defaultRule": false,
      "description": "My Agent rule",
      "disabled": [],
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "monitoring": [],
      "name": "my_agent_rule",
      "product_tags": [],
      "silent": false,
      "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "version": 23
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
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
                  \# Path parametersexport agent_rule_id="3b5-v82-ns6"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/${agent_rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a Workload Protection agent rule (US1-FED) returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.get_cloud_workload_security_agent_rule(
        agent_rule_id=AGENT_RULE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a Workload Protection agent rule (US1-FED) returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = ENV["AGENT_RULE_DATA_ID"]
p api_instance.get_cloud_workload_security_agent_rule(AGENT_RULE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a Workload Protection agent rule (US1-FED) returns "OK" response

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
	// there is a valid "agent_rule" in the system
	AgentRuleDataID := os.Getenv("AGENT_RULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.GetCloudWorkloadSecurityAgentRule(ctx, AgentRuleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.GetCloudWorkloadSecurityAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.GetCloudWorkloadSecurityAgentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a Workload Protection agent rule (US1-FED) returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "agent_rule" in the system
    String AGENT_RULE_DATA_ID = System.getenv("AGENT_RULE_DATA_ID");

    try {
      CloudWorkloadSecurityAgentRuleResponse result =
          apiInstance.getCloudWorkloadSecurityAgentRule(AGENT_RULE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#getCloudWorkloadSecurityAgentRule");
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
// Get a Workload Protection agent rule (US1-FED) returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "agent_rule" in the system
    let agent_rule_data_id = std::env::var("AGENT_RULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .get_cloud_workload_security_agent_rule(agent_rule_data_id.clone())
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
 * Get a Workload Protection agent rule (US1-FED) returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "agent_rule" in the system
const AGENT_RULE_DATA_ID = process.env.AGENT_RULE_DATA_ID as string;

const params: v2.CSMThreatsApiGetCloudWorkloadSecurityAgentRuleRequest = {
  agentRuleId: AGENT_RULE_DATA_ID,
};

apiInstance
  .getCloudWorkloadSecurityAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
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

## Create a Workload Protection agent rule (US1-FED){% #create-a-workload-protection-agent-rule-us1-fed %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/security_monitoring/cloud_workload_security/agent_rules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/security_monitoring/cloud_workload_security/agent_rules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules |

### Overview



Create a new agent rule with the given parameters.

**Note**: This endpoint should only be used for the Government (US1-FED) site.
This endpoint requires the `security_monitoring_cws_agent_rules_write` permission.


### Request

#### Body Data (required)

The definition of the new agent rule

{% tab title="Model" %}

| Parent field | Field                        | Type          | Description                                                                             |
| ------------ | ---------------------------- | ------------- | --------------------------------------------------------------------------------------- |
|              | data [*required*]       | object        | Object for a single Agent rule                                                          |
| data         | attributes [*required*] | object        | Create a new Cloud Workload Security Agent rule.                                        |
| attributes   | actions                      | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter                       | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash                         | object        | Hash file specified by the field attribute                                              |
| hash         | field                        | string        | The field of the hash action                                                            |
| actions      | kill                         | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal                       | string        | Supported signals for the kill system call                                              |
| actions      | metadata                     | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag                    | string        | The image tag of the metadata action                                                    |
| metadata     | service                      | string        | The service of the metadata action                                                      |
| metadata     | short_image                  | string        | The short image of the metadata action                                                  |
| actions      | set                          | object        | The set action applied on the scope matching the rule                                   |
| set          | append                       | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value                | string        | The default value of the set action                                                     |
| set          | expression                   | string        | The expression of the set action.                                                       |
| set          | field                        | string        | The field of the set action                                                             |
| set          | inherited                    | boolean       | Whether the value should be inherited.                                                  |
| set          | name                         | string        | The name of the set action                                                              |
| set          | scope                        | string        | The scope of the set action.                                                            |
| set          | size                         | int64         | The size of the set action.                                                             |
| set          | ttl                          | int64         | The time to live of the set action.                                                     |
| set          | value                        |  <oneOf> | The value of the set action                                                             |
| value        | Option 1                     | string        |
| value        | Option 2                     | integer       |
| value        | Option 3                     | boolean       |
| attributes   | agent_version                | string        | Constrain the rule to specific versions of the Datadog Agent.                           |
| attributes   | blocking                     | [string]      | The blocking policies that the rule belongs to.                                         |
| attributes   | description                  | string        | The description of the Agent rule.                                                      |
| attributes   | disabled                     | [string]      | The disabled policies that the rule belongs to.                                         |
| attributes   | enabled                      | boolean       | Whether the Agent rule is enabled.                                                      |
| attributes   | expression [*required*] | string        | The SECL expression of the Agent rule.                                                  |
| attributes   | filters                      | [string]      | The platforms the Agent rule is supported on.                                           |
| attributes   | monitoring                   | [string]      | The monitoring policies that the rule belongs to.                                       |
| attributes   | name [*required*]       | string        | The name of the Agent rule.                                                             |
| attributes   | policy_id                    | string        | The ID of the policy where the Agent rule is saved.                                     |
| attributes   | product_tags                 | [string]      | The list of product tags associated with the rule.                                      |
| attributes   | silent                       | boolean       | Whether the rule is silent.                                                             |
| data         | type [*required*]       | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "My Agent rule",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "name": "examplecsmthreat"
    },
    "type": "agent_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | object        | Object for a single Agent rule                                                          |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "actions": [
        {
          "filter": "string",
          "hash": {
            "field": "string"
          },
          "kill": {
            "signal": "string"
          },
          "metadata": {
            "image_tag": "string",
            "service": "string",
            "short_image": "string"
          },
          "set": {
            "append": false,
            "default_value": "string",
            "expression": "string",
            "field": "string",
            "inherited": false,
            "name": "string",
            "scope": "string",
            "size": "integer",
            "ttl": "integer",
            "value": {
              "type": "undefined"
            }
          }
        }
      ],
      "agentConstraint": "string",
      "blocking": [],
      "category": "Process Activity",
      "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "creationDate": 1624366480320,
      "creator": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "defaultRule": false,
      "description": "My Agent rule",
      "disabled": [],
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "monitoring": [],
      "name": "my_agent_rule",
      "product_tags": [],
      "silent": false,
      "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "version": 23
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
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

{% tab title="409" %}
Conflict
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "My Agent rule",
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "name": "examplecsmthreat"
    },
    "type": "agent_rule"
  }
}
EOF
                        
##### 

```go
// Create a Workload Protection agent rule (US1-FED) returns "OK" response

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
	body := datadogV2.CloudWorkloadSecurityAgentRuleCreateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentRuleCreateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentRuleCreateAttributes{
				Description: datadog.PtrString("My Agent rule"),
				Enabled:     datadog.PtrBool(true),
				Expression:  `exec.file.name == "sh"`,
				Filters:     []string{},
				Name:        "examplecsmthreat",
			},
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTRULETYPE_AGENT_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.CreateCloudWorkloadSecurityAgentRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.CreateCloudWorkloadSecurityAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.CreateCloudWorkloadSecurityAgentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a Workload Protection agent rule (US1-FED) returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleCreateRequest;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    CloudWorkloadSecurityAgentRuleCreateRequest body =
        new CloudWorkloadSecurityAgentRuleCreateRequest()
            .data(
                new CloudWorkloadSecurityAgentRuleCreateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentRuleCreateAttributes()
                            .description("My Agent rule")
                            .enabled(true)
                            .expression("""
exec.file.name == "sh"
""")
                            .name("examplecsmthreat"))
                    .type(CloudWorkloadSecurityAgentRuleType.AGENT_RULE));

    try {
      CloudWorkloadSecurityAgentRuleResponse result =
          apiInstance.createCloudWorkloadSecurityAgentRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CsmThreatsApi#createCloudWorkloadSecurityAgentRule");
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

```python
"""
Create a Workload Protection agent rule (US1-FED) returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_attributes import (
    CloudWorkloadSecurityAgentRuleCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_data import (
    CloudWorkloadSecurityAgentRuleCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

body = CloudWorkloadSecurityAgentRuleCreateRequest(
    data=CloudWorkloadSecurityAgentRuleCreateData(
        attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
            description="My Agent rule",
            enabled=True,
            expression='exec.file.name == "sh"',
            filters=[],
            name="examplecsmthreat",
        ),
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_cloud_workload_security_agent_rule(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a Workload Protection agent rule (US1-FED) returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleCreateAttributes.new({
      description: "My Agent rule",
      enabled: true,
      expression: 'exec.file.name == "sh"',
      filters: [],
      name: "examplecsmthreat",
    }),
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
  }),
})
p api_instance.create_cloud_workload_security_agent_rule(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a Workload Protection agent rule (US1-FED) returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleCreateRequest;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleType;

#[tokio::main]
async fn main() {
    let body = CloudWorkloadSecurityAgentRuleCreateRequest::new(
        CloudWorkloadSecurityAgentRuleCreateData::new(
            CloudWorkloadSecurityAgentRuleCreateAttributes::new(
                r#"exec.file.name == "sh""#.to_string(),
                "examplecsmthreat".to_string(),
            )
            .description("My Agent rule".to_string())
            .enabled(true)
            .filters(vec![]),
            CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.create_cloud_workload_security_agent_rule(body).await;
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
 * Create a Workload Protection agent rule (US1-FED) returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

const params: v2.CSMThreatsApiCreateCloudWorkloadSecurityAgentRuleRequest = {
  body: {
    data: {
      attributes: {
        description: "My Agent rule",
        enabled: true,
        expression: `exec.file.name == "sh"`,
        filters: [],
        name: "examplecsmthreat",
      },
      type: "agent_rule",
    },
  },
};

apiInstance
  .createCloudWorkloadSecurityAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
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

## Update a Workload Protection agent rule (US1-FED){% #update-a-workload-protection-agent-rule-us1-fed %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |

### Overview



Update a specific agent rule. Returns the agent rule object when the request is successful.

**Note**: This endpoint should only be used for the Government (US1-FED) site.
This endpoint requires the `security_monitoring_cws_agent_rules_write` permission.


### Arguments

#### Path Parameters

| Name                            | Type   | Description              |
| ------------------------------- | ------ | ------------------------ |
| agent_rule_id [*required*] | string | The ID of the Agent rule |

### Request

#### Body Data (required)

New definition of the agent rule

{% tab title="Model" %}

| Parent field | Field                        | Type          | Description                                                                             |
| ------------ | ---------------------------- | ------------- | --------------------------------------------------------------------------------------- |
|              | data [*required*]       | object        | Object for a single Agent rule                                                          |
| data         | attributes [*required*] | object        | Update an existing Cloud Workload Security Agent rule                                   |
| attributes   | actions                      | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter                       | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash                         | object        | Hash file specified by the field attribute                                              |
| hash         | field                        | string        | The field of the hash action                                                            |
| actions      | kill                         | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal                       | string        | Supported signals for the kill system call                                              |
| actions      | metadata                     | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag                    | string        | The image tag of the metadata action                                                    |
| metadata     | service                      | string        | The service of the metadata action                                                      |
| metadata     | short_image                  | string        | The short image of the metadata action                                                  |
| actions      | set                          | object        | The set action applied on the scope matching the rule                                   |
| set          | append                       | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value                | string        | The default value of the set action                                                     |
| set          | expression                   | string        | The expression of the set action.                                                       |
| set          | field                        | string        | The field of the set action                                                             |
| set          | inherited                    | boolean       | Whether the value should be inherited.                                                  |
| set          | name                         | string        | The name of the set action                                                              |
| set          | scope                        | string        | The scope of the set action.                                                            |
| set          | size                         | int64         | The size of the set action.                                                             |
| set          | ttl                          | int64         | The time to live of the set action.                                                     |
| set          | value                        |  <oneOf> | The value of the set action                                                             |
| value        | Option 1                     | string        |
| value        | Option 2                     | integer       |
| value        | Option 3                     | boolean       |
| attributes   | agent_version                | string        | Constrain the rule to specific versions of the Datadog Agent                            |
| attributes   | blocking                     | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | description                  | string        | The description of the Agent rule                                                       |
| attributes   | disabled                     | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled                      | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression                   | string        | The SECL expression of the Agent rule                                                   |
| attributes   | monitoring                   | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | policy_id                    | string        | The ID of the policy where the Agent rule is saved                                      |
| attributes   | product_tags                 | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent                       | boolean       | Whether the rule is silent.                                                             |
| data         | id                           | string        | The ID of the Agent rule                                                                |
| data         | type [*required*]       | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Updated Agent rule",
      "expression": "exec.file.name == \"sh\""
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes an Agent rule

| Parent field | Field              | Type          | Description                                                                             |
| ------------ | ------------------ | ------------- | --------------------------------------------------------------------------------------- |
|              | data               | object        | Object for a single Agent rule                                                          |
| data         | attributes         | object        | A Cloud Workload Security Agent rule returned by the API                                |
| attributes   | actions            | [object]      | The array of actions the rule can perform if triggered                                  |
| actions      | filter             | string        | SECL expression used to target the container to apply the action on                     |
| actions      | hash               | object        | Hash file specified by the field attribute                                              |
| hash         | field              | string        | The field of the hash action                                                            |
| actions      | kill               | object        | Kill system call applied on the container matching the rule                             |
| kill         | signal             | string        | Supported signals for the kill system call                                              |
| actions      | metadata           | object        | The metadata action applied on the scope matching the rule                              |
| metadata     | image_tag          | string        | The image tag of the metadata action                                                    |
| metadata     | service            | string        | The service of the metadata action                                                      |
| metadata     | short_image        | string        | The short image of the metadata action                                                  |
| actions      | set                | object        | The set action applied on the scope matching the rule                                   |
| set          | append             | boolean       | Whether the value should be appended to the field.                                      |
| set          | default_value      | string        | The default value of the set action                                                     |
| set          | expression         | string        | The expression of the set action.                                                       |
| set          | field              | string        | The field of the set action                                                             |
| set          | inherited          | boolean       | Whether the value should be inherited.                                                  |
| set          | name               | string        | The name of the set action                                                              |
| set          | scope              | string        | The scope of the set action.                                                            |
| set          | size               | int64         | The size of the set action.                                                             |
| set          | ttl                | int64         | The time to live of the set action.                                                     |
| set          | value              |  <oneOf> | The value of the set action                                                             |
| value        | Option 1           | string        |
| value        | Option 2           | integer       |
| value        | Option 3           | boolean       |
| attributes   | agentConstraint    | string        | The version of the Agent                                                                |
| attributes   | blocking           | [string]      | The blocking policies that the rule belongs to                                          |
| attributes   | category           | string        | The category of the Agent rule                                                          |
| attributes   | creationAuthorUuId | string        | The ID of the user who created the rule                                                 |
| attributes   | creationDate       | int64         | When the Agent rule was created, timestamp in milliseconds                              |
| attributes   | creator            | object        | The attributes of the user who created the Agent rule                                   |
| creator      | handle             | string        | The handle of the user                                                                  |
| creator      | name               | string        | The name of the user                                                                    |
| attributes   | defaultRule        | boolean       | Whether the rule is included by default                                                 |
| attributes   | description        | string        | The description of the Agent rule                                                       |
| attributes   | disabled           | [string]      | The disabled policies that the rule belongs to                                          |
| attributes   | enabled            | boolean       | Whether the Agent rule is enabled                                                       |
| attributes   | expression         | string        | The SECL expression of the Agent rule                                                   |
| attributes   | filters            | [string]      | The platforms the Agent rule is supported on                                            |
| attributes   | monitoring         | [string]      | The monitoring policies that the rule belongs to                                        |
| attributes   | name               | string        | The name of the Agent rule                                                              |
| attributes   | product_tags       | [string]      | The list of product tags associated with the rule                                       |
| attributes   | silent             | boolean       | Whether the rule is silent.                                                             |
| attributes   | updateAuthorUuId   | string        | The ID of the user who updated the rule                                                 |
| attributes   | updateDate         | int64         | Timestamp in milliseconds when the Agent rule was last updated                          |
| attributes   | updatedAt          | int64         | When the Agent rule was last updated, timestamp in milliseconds                         |
| attributes   | updater            | object        | The attributes of the user who last updated the Agent rule                              |
| updater      | handle             | string        | The handle of the user                                                                  |
| updater      | name               | string        | The name of the user                                                                    |
| attributes   | version            | int64         | The version of the Agent rule                                                           |
| data         | id                 | string        | The ID of the Agent rule                                                                |
| data         | type               | enum          | The type of the resource, must always be `agent_rule` Allowed enum values: `agent_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "actions": [
        {
          "filter": "string",
          "hash": {
            "field": "string"
          },
          "kill": {
            "signal": "string"
          },
          "metadata": {
            "image_tag": "string",
            "service": "string",
            "short_image": "string"
          },
          "set": {
            "append": false,
            "default_value": "string",
            "expression": "string",
            "field": "string",
            "inherited": false,
            "name": "string",
            "scope": "string",
            "size": "integer",
            "ttl": "integer",
            "value": {
              "type": "undefined"
            }
          }
        }
      ],
      "agentConstraint": "string",
      "blocking": [],
      "category": "Process Activity",
      "creationAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "creationDate": 1624366480320,
      "creator": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "defaultRule": false,
      "description": "My Agent rule",
      "disabled": [],
      "enabled": true,
      "expression": "exec.file.name == \"sh\"",
      "filters": [],
      "monitoring": [],
      "name": "my_agent_rule",
      "product_tags": [],
      "silent": false,
      "updateAuthorUuId": "e51c9744-d158-11ec-ad23-da7ad0900002",
      "updateDate": 1624366480320,
      "updatedAt": 1624366480320,
      "updater": {
        "handle": "datadog.user@example.com",
        "name": "Datadog User"
      },
      "version": 23
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
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

{% tab title="409" %}
Concurrent Modification
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
                          \# Path parametersexport agent_rule_id="3b5-v82-ns6"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/${agent_rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Updated Agent rule",
      "expression": "exec.file.name == \"sh\""
    },
    "id": "3dd-0uc-h1s",
    "type": "agent_rule"
  }
}
EOF
                        
##### 

```go
// Update a Workload Protection agent rule (US1-FED) returns "OK" response

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
	// there is a valid "agent_rule" in the system
	AgentRuleDataID := os.Getenv("AGENT_RULE_DATA_ID")

	body := datadogV2.CloudWorkloadSecurityAgentRuleUpdateRequest{
		Data: datadogV2.CloudWorkloadSecurityAgentRuleUpdateData{
			Attributes: datadogV2.CloudWorkloadSecurityAgentRuleUpdateAttributes{
				Description: datadog.PtrString("Updated Agent rule"),
				Expression:  datadog.PtrString(`exec.file.name == "sh"`),
			},
			Id:   datadog.PtrString(AgentRuleDataID),
			Type: datadogV2.CLOUDWORKLOADSECURITYAGENTRULETYPE_AGENT_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.UpdateCloudWorkloadSecurityAgentRule(ctx, AgentRuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.UpdateCloudWorkloadSecurityAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.UpdateCloudWorkloadSecurityAgentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a Workload Protection agent rule (US1-FED) returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleResponse;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleType;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleUpdateAttributes;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleUpdateData;
import com.datadog.api.client.v2.model.CloudWorkloadSecurityAgentRuleUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "agent_rule" in the system
    String AGENT_RULE_DATA_ID = System.getenv("AGENT_RULE_DATA_ID");

    CloudWorkloadSecurityAgentRuleUpdateRequest body =
        new CloudWorkloadSecurityAgentRuleUpdateRequest()
            .data(
                new CloudWorkloadSecurityAgentRuleUpdateData()
                    .attributes(
                        new CloudWorkloadSecurityAgentRuleUpdateAttributes()
                            .description("Updated Agent rule")
                            .expression("""
exec.file.name == "sh"
"""))
                    .id(AGENT_RULE_DATA_ID)
                    .type(CloudWorkloadSecurityAgentRuleType.AGENT_RULE));

    try {
      CloudWorkloadSecurityAgentRuleResponse result =
          apiInstance.updateCloudWorkloadSecurityAgentRule(AGENT_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CsmThreatsApi#updateCloudWorkloadSecurityAgentRule");
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

```python
"""
Update a Workload Protection agent rule (US1-FED) returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_attributes import (
    CloudWorkloadSecurityAgentRuleUpdateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_data import (
    CloudWorkloadSecurityAgentRuleUpdateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_request import (
    CloudWorkloadSecurityAgentRuleUpdateRequest,
)

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleUpdateRequest(
    data=CloudWorkloadSecurityAgentRuleUpdateData(
        attributes=CloudWorkloadSecurityAgentRuleUpdateAttributes(
            description="Updated Agent rule",
            expression='exec.file.name == "sh"',
        ),
        id=AGENT_RULE_DATA_ID,
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.update_cloud_workload_security_agent_rule(agent_rule_id=AGENT_RULE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a Workload Protection agent rule (US1-FED) returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = ENV["AGENT_RULE_DATA_ID"]

body = DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleUpdateRequest.new({
  data: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleUpdateData.new({
    attributes: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleUpdateAttributes.new({
      description: "Updated Agent rule",
      expression: 'exec.file.name == "sh"',
    }),
    id: AGENT_RULE_DATA_ID,
    type: DatadogAPIClient::V2::CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
  }),
})
p api_instance.update_cloud_workload_security_agent_rule(AGENT_RULE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update a Workload Protection agent rule (US1-FED) returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleType;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleUpdateAttributes;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleUpdateData;
use datadog_api_client::datadogV2::model::CloudWorkloadSecurityAgentRuleUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "agent_rule" in the system
    let agent_rule_data_id = std::env::var("AGENT_RULE_DATA_ID").unwrap();
    let body = CloudWorkloadSecurityAgentRuleUpdateRequest::new(
        CloudWorkloadSecurityAgentRuleUpdateData::new(
            CloudWorkloadSecurityAgentRuleUpdateAttributes::new()
                .description("Updated Agent rule".to_string())
                .expression(r#"exec.file.name == "sh""#.to_string()),
            CloudWorkloadSecurityAgentRuleType::AGENT_RULE,
        )
        .id(agent_rule_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .update_cloud_workload_security_agent_rule(agent_rule_data_id.clone(), body)
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
 * Update a Workload Protection agent rule (US1-FED) returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "agent_rule" in the system
const AGENT_RULE_DATA_ID = process.env.AGENT_RULE_DATA_ID as string;

const params: v2.CSMThreatsApiUpdateCloudWorkloadSecurityAgentRuleRequest = {
  body: {
    data: {
      attributes: {
        description: "Updated Agent rule",
        expression: `exec.file.name == "sh"`,
      },
      id: AGENT_RULE_DATA_ID,
      type: "agent_rule",
    },
  },
  agentRuleId: AGENT_RULE_DATA_ID,
};

apiInstance
  .updateCloudWorkloadSecurityAgentRule(params)
  .then((data: v2.CloudWorkloadSecurityAgentRuleResponse) => {
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

## Delete a Workload Protection agent rule (US1-FED){% #delete-a-workload-protection-agent-rule-us1-fed %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} |

### Overview



Delete a specific agent rule.

**Note**: This endpoint should only be used for the Government (US1-FED) site.
This endpoint requires the `security_monitoring_cws_agent_rules_write` permission.


### Arguments

#### Path Parameters

| Name                            | Type   | Description              |
| ------------------------------- | ------ | ------------------------ |
| agent_rule_id [*required*] | string | The ID of the Agent rule |

### Response

{% tab title="204" %}
OK
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
                  \# Path parametersexport agent_rule_id="3b5-v82-ns6"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/security_monitoring/cloud_workload_security/agent_rules/${agent_rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a Workload Protection agent rule (US1-FED) returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    api_instance.delete_cloud_workload_security_agent_rule(
        agent_rule_id=AGENT_RULE_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a Workload Protection agent rule (US1-FED) returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = ENV["AGENT_RULE_DATA_ID"]
api_instance.delete_cloud_workload_security_agent_rule(AGENT_RULE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a Workload Protection agent rule (US1-FED) returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "agent_rule" in the system
	AgentRuleDataID := os.Getenv("AGENT_RULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	r, err := api.DeleteCloudWorkloadSecurityAgentRule(ctx, AgentRuleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.DeleteCloudWorkloadSecurityAgentRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a Workload Protection agent rule (US1-FED) returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    // there is a valid "agent_rule" in the system
    String AGENT_RULE_DATA_ID = System.getenv("AGENT_RULE_DATA_ID");

    try {
      apiInstance.deleteCloudWorkloadSecurityAgentRule(AGENT_RULE_DATA_ID);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CsmThreatsApi#deleteCloudWorkloadSecurityAgentRule");
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
// Delete a Workload Protection agent rule (US1-FED) returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "agent_rule" in the system
    let agent_rule_data_id = std::env::var("AGENT_RULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api
        .delete_cloud_workload_security_agent_rule(agent_rule_data_id.clone())
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
 * Delete a Workload Protection agent rule (US1-FED) returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

// there is a valid "agent_rule" in the system
const AGENT_RULE_DATA_ID = process.env.AGENT_RULE_DATA_ID as string;

const params: v2.CSMThreatsApiDeleteCloudWorkloadSecurityAgentRuleRequest = {
  agentRuleId: AGENT_RULE_DATA_ID,
};

apiInstance
  .deleteCloudWorkloadSecurityAgentRule(params)
  .then((data: any) => {
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

## Download the Workload Protection policy (US1-FED){% #download-the-workload-protection-policy-us1-fed %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/security/cloud_workload/policy/download |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/security/cloud_workload/policy/download |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/security/cloud_workload/policy/download      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/security/cloud_workload/policy/download      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/security/cloud_workload/policy/download     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/security/cloud_workload/policy/download |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/security/cloud_workload/policy/download |

### Overview



The download endpoint generates a Workload Protection policy file from your currently active Workload Protection agent rules, and downloads them as a `.policy` file. This file can then be deployed to your agents to update the policy running in your environment.

**Note**: This endpoint should only be used for the Government (US1-FED) site.
This endpoint requires the `security_monitoring_cws_agent_rules_read` permission.


### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/security/cloud_workload/policy/download" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Download the Workload Protection policy (US1-FED) returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.download_cloud_workload_policy_file()

    print(response.read())
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Download the Workload Protection policy (US1-FED) returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMThreatsAPI.new
p api_instance.download_cloud_workload_policy_file()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Download the Workload Protection policy (US1-FED) returns "OK" response

package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCSMThreatsApi(apiClient)
	resp, r, err := api.DownloadCloudWorkloadPolicyFile(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMThreatsApi.DownloadCloudWorkloadPolicyFile`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := ioutil.ReadAll(resp)
	fmt.Fprintf(os.Stdout, "Response from `CSMThreatsApi.DownloadCloudWorkloadPolicyFile`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Download the Workload Protection policy (US1-FED) returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmThreatsApi;
import java.io.File;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmThreatsApi apiInstance = new CsmThreatsApi(defaultClient);

    try {
      File result = apiInstance.downloadCloudWorkloadPolicyFile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CsmThreatsApi#downloadCloudWorkloadPolicyFile");
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
// Download the Workload Protection policy (US1-FED) returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_threats::CSMThreatsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMThreatsAPI::with_config(configuration);
    let resp = api.download_cloud_workload_policy_file().await;
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
 * Download the Workload Protection policy (US1-FED) returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMThreatsApi(configuration);

apiInstance
  .downloadCloudWorkloadPolicyFile()
  .then((data: client.HttpFile) => {
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
