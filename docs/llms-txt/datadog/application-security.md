# Source: https://docs.datadoghq.com/api/latest/application-security.md

---
title: Application Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Application Security
---

# Application Security

[Datadog Application Security](https://docs.datadoghq.com/security/application_security/) provides protection against application-level attacks that aim to exploit code-level vulnerabilities, such as Server-Side-Request-Forgery (SSRF), SQL injection, Log4Shell, and Reflected Cross-Site-Scripting (XSS). You can monitor and protect apps hosted directly on a server, Docker, Kubernetes, Amazon ECS, and (for supported languages) AWS Fargate.

## Get a WAF exclusion filter{% #get-a-waf-exclusion-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |

### Overview

Retrieve a specific WAF exclusion filter using its identifier. This endpoint requires the `appsec_protect_read` permission.

### Arguments

#### Path Parameters

| Name                                  | Type   | Description                                 |
| ------------------------------------- | ------ | ------------------------------------------- |
| exclusion_filter_id [*required*] | string | The identifier of the WAF exclusion filter. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a single WAF exclusion filter.

| Parent field | Field            | Type      | Description                                                                                                                                                                                                                                           |
| ------------ | ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | object    | A JSON:API resource for an WAF exclusion filter.                                                                                                                                                                                                      |
| data         | attributes       | object    | Attributes describing a WAF exclusion filter.                                                                                                                                                                                                         |
| attributes   | description      | string    | A description for the exclusion filter.                                                                                                                                                                                                               |
| attributes   | enabled          | boolean   | Indicates whether the exclusion filter is enabled.                                                                                                                                                                                                    |
| attributes   | event_query      | string    | The event query matched by the legacy exclusion filter. Cannot be created nor updated.                                                                                                                                                                |
| attributes   | ip_list          | [string]  | The client IP addresses matched by the exclusion filter (CIDR notation is supported).                                                                                                                                                                 |
| attributes   | metadata         | object    | Extra information about the exclusion filter.                                                                                                                                                                                                         |
| metadata     | added_at         | date-time | The creation date of the exclusion filter.                                                                                                                                                                                                            |
| metadata     | added_by         | string    | The handle of the user who created the exclusion filter.                                                                                                                                                                                              |
| metadata     | added_by_name    | string    | The name of the user who created the exclusion filter.                                                                                                                                                                                                |
| metadata     | modified_at      | date-time | The last modification date of the exclusion filter.                                                                                                                                                                                                   |
| metadata     | modified_by      | string    | The handle of the user who last modified the exclusion filter.                                                                                                                                                                                        |
| metadata     | modified_by_name | string    | The name of the user who last modified the exclusion filter.                                                                                                                                                                                          |
| attributes   | on_match         | enum      | The action taken when the exclusion filter matches. When set to `monitor`, security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked. Allowed enum values: `monitor` |
| attributes   | parameters       | [string]  | A list of parameters matched by the exclusion filter in the HTTP query string and HTTP request body. Nested parameters can be matched by joining fields with a dot character.                                                                         |
| attributes   | path_glob        | string    | The HTTP path glob expression matched by the exclusion filter.                                                                                                                                                                                        |
| attributes   | rules_target     | [object]  | The WAF rules targeted by the exclusion filter.                                                                                                                                                                                                       |
| rules_target | rule_id          | string    | Target a single WAF rule based on its identifier.                                                                                                                                                                                                     |
| rules_target | tags             | object    | Target multiple WAF rules based on their tags.                                                                                                                                                                                                        |
| tags         | category         | string    | The category of the targeted WAF rules.                                                                                                                                                                                                               |
| tags         | type             | string    | The type of the targeted WAF rules.                                                                                                                                                                                                                   |
| attributes   | scope            | [object]  | The services where the exclusion filter is deployed.                                                                                                                                                                                                  |
| scope        | env              | string    | Deploy on this environment.                                                                                                                                                                                                                           |
| scope        | service          | string    | Deploy on this service.                                                                                                                                                                                                                               |
| attributes   | search_query     | string    | Generated event search query for traces matching the exclusion filter.                                                                                                                                                                                |
| data         | id               | string    | The identifier of the WAF exclusion filter.                                                                                                                                                                                                           |
| data         | type             | enum      | Type of the resource. The value should always be `exclusion_filter`. Allowed enum values: `exclusion_filter`                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Exclude false positives on a path",
      "enabled": true,
      "event_query": "string",
      "ip_list": [
        "198.51.100.72"
      ],
      "metadata": {
        "added_at": "2019-09-19T10:00:00.000Z",
        "added_by": "string",
        "added_by_name": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "modified_by": "string",
        "modified_by_name": "string"
      },
      "on_match": "string",
      "parameters": [
        "list.search.query"
      ],
      "path_glob": "/accounts/*",
      "rules_target": [
        {
          "rule_id": "dog-913-009",
          "tags": {
            "category": "attack_attempt",
            "type": "lfi"
          }
        }
      ],
      "scope": [
        {
          "env": "www",
          "service": "prod"
        }
      ],
      "search_query": "string"
    },
    "id": "3dd-0uc-h1s",
    "type": "exclusion_filter"
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
                  \# Path parametersexport exclusion_filter_id="3b5-v82-ns6"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/${exclusion_filter_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a WAF exclusion filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = environ["EXCLUSION_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.get_application_security_waf_exclusion_filter(
        exclusion_filter_id=EXCLUSION_FILTER_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a WAF exclusion filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = ENV["EXCLUSION_FILTER_DATA_ID"]
p api_instance.get_application_security_waf_exclusion_filter(EXCLUSION_FILTER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a WAF exclusion filter returns "OK" response

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
	// there is a valid "exclusion_filter" in the system
	ExclusionFilterDataID := os.Getenv("EXCLUSION_FILTER_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.GetApplicationSecurityWafExclusionFilter(ctx, ExclusionFilterDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.GetApplicationSecurityWafExclusionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.GetApplicationSecurityWafExclusionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a WAF exclusion filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    // there is a valid "exclusion_filter" in the system
    String EXCLUSION_FILTER_DATA_ID = System.getenv("EXCLUSION_FILTER_DATA_ID");

    try {
      ApplicationSecurityWafExclusionFilterResponse result =
          apiInstance.getApplicationSecurityWafExclusionFilter(EXCLUSION_FILTER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ApplicationSecurityApi#getApplicationSecurityWafExclusionFilter");
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
// Get a WAF exclusion filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;

#[tokio::main]
async fn main() {
    // there is a valid "exclusion_filter" in the system
    let exclusion_filter_data_id = std::env::var("EXCLUSION_FILTER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api
        .get_application_security_waf_exclusion_filter(exclusion_filter_data_id.clone())
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
 * Get a WAF exclusion filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

// there is a valid "exclusion_filter" in the system
const EXCLUSION_FILTER_DATA_ID = process.env.EXCLUSION_FILTER_DATA_ID as string;

const params: v2.ApplicationSecurityApiGetApplicationSecurityWafExclusionFilterRequest =
  {
    exclusionFilterId: EXCLUSION_FILTER_DATA_ID,
  };

apiInstance
  .getApplicationSecurityWafExclusionFilter(params)
  .then((data: v2.ApplicationSecurityWafExclusionFilterResponse) => {
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

## Create a WAF exclusion filter{% #create-a-waf-exclusion-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/exclusion_filters      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/exclusion_filters      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |

### Overview



Create a new WAF exclusion filter with the given parameters.

A request matched by an exclusion filter will be ignored by the Application Security WAF product. Go to [https://app.datadoghq.com/security/appsec/passlist](https://app.datadoghq.com/security/appsec/passlist) to review existing exclusion filters (also called passlist entries).
This endpoint requires the `appsec_protect_write` permission.


### Request

#### Body Data (required)

The definition of the new WAF exclusion filter.

{% tab title="Model" %}

| Parent field | Field                         | Type     | Description                                                                                                                                                                                                                                           |
| ------------ | ----------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]        | object   | Object for creating a single WAF exclusion filter.                                                                                                                                                                                                    |
| data         | attributes [*required*]  | object   | Attributes for creating a WAF exclusion filter.                                                                                                                                                                                                       |
| attributes   | description [*required*] | string   | A description for the exclusion filter.                                                                                                                                                                                                               |
| attributes   | enabled [*required*]     | boolean  | Indicates whether the exclusion filter is enabled.                                                                                                                                                                                                    |
| attributes   | ip_list                       | [string] | The client IP addresses matched by the exclusion filter (CIDR notation is supported).                                                                                                                                                                 |
| attributes   | on_match                      | enum     | The action taken when the exclusion filter matches. When set to `monitor`, security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked. Allowed enum values: `monitor` |
| attributes   | parameters                    | [string] | A list of parameters matched by the exclusion filter in the HTTP query string and HTTP request body. Nested parameters can be matched by joining fields with a dot character.                                                                         |
| attributes   | path_glob                     | string   | The HTTP path glob expression matched by the exclusion filter.                                                                                                                                                                                        |
| attributes   | rules_target                  | [object] | The WAF rules targeted by the exclusion filter.                                                                                                                                                                                                       |
| rules_target | rule_id                       | string   | Target a single WAF rule based on its identifier.                                                                                                                                                                                                     |
| rules_target | tags                          | object   | Target multiple WAF rules based on their tags.                                                                                                                                                                                                        |
| tags         | category                      | string   | The category of the targeted WAF rules.                                                                                                                                                                                                               |
| tags         | type                          | string   | The type of the targeted WAF rules.                                                                                                                                                                                                                   |
| attributes   | scope                         | [object] | The services where the exclusion filter is deployed.                                                                                                                                                                                                  |
| scope        | env                           | string   | Deploy on this environment.                                                                                                                                                                                                                           |
| scope        | service                       | string   | Deploy on this service.                                                                                                                                                                                                                               |
| data         | type [*required*]        | enum     | Type of the resource. The value should always be `exclusion_filter`. Allowed enum values: `exclusion_filter`                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Exclude false positives on a path",
      "enabled": true,
      "parameters": [
        "list.search.query"
      ],
      "path_glob": "/accounts/*",
      "rules_target": [
        {
          "tags": {
            "category": "attack_attempt",
            "type": "lfi"
          }
        }
      ],
      "scope": [
        {
          "env": "www",
          "service": "prod"
        }
      ]
    },
    "type": "exclusion_filter"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a single WAF exclusion filter.

| Parent field | Field            | Type      | Description                                                                                                                                                                                                                                           |
| ------------ | ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | object    | A JSON:API resource for an WAF exclusion filter.                                                                                                                                                                                                      |
| data         | attributes       | object    | Attributes describing a WAF exclusion filter.                                                                                                                                                                                                         |
| attributes   | description      | string    | A description for the exclusion filter.                                                                                                                                                                                                               |
| attributes   | enabled          | boolean   | Indicates whether the exclusion filter is enabled.                                                                                                                                                                                                    |
| attributes   | event_query      | string    | The event query matched by the legacy exclusion filter. Cannot be created nor updated.                                                                                                                                                                |
| attributes   | ip_list          | [string]  | The client IP addresses matched by the exclusion filter (CIDR notation is supported).                                                                                                                                                                 |
| attributes   | metadata         | object    | Extra information about the exclusion filter.                                                                                                                                                                                                         |
| metadata     | added_at         | date-time | The creation date of the exclusion filter.                                                                                                                                                                                                            |
| metadata     | added_by         | string    | The handle of the user who created the exclusion filter.                                                                                                                                                                                              |
| metadata     | added_by_name    | string    | The name of the user who created the exclusion filter.                                                                                                                                                                                                |
| metadata     | modified_at      | date-time | The last modification date of the exclusion filter.                                                                                                                                                                                                   |
| metadata     | modified_by      | string    | The handle of the user who last modified the exclusion filter.                                                                                                                                                                                        |
| metadata     | modified_by_name | string    | The name of the user who last modified the exclusion filter.                                                                                                                                                                                          |
| attributes   | on_match         | enum      | The action taken when the exclusion filter matches. When set to `monitor`, security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked. Allowed enum values: `monitor` |
| attributes   | parameters       | [string]  | A list of parameters matched by the exclusion filter in the HTTP query string and HTTP request body. Nested parameters can be matched by joining fields with a dot character.                                                                         |
| attributes   | path_glob        | string    | The HTTP path glob expression matched by the exclusion filter.                                                                                                                                                                                        |
| attributes   | rules_target     | [object]  | The WAF rules targeted by the exclusion filter.                                                                                                                                                                                                       |
| rules_target | rule_id          | string    | Target a single WAF rule based on its identifier.                                                                                                                                                                                                     |
| rules_target | tags             | object    | Target multiple WAF rules based on their tags.                                                                                                                                                                                                        |
| tags         | category         | string    | The category of the targeted WAF rules.                                                                                                                                                                                                               |
| tags         | type             | string    | The type of the targeted WAF rules.                                                                                                                                                                                                                   |
| attributes   | scope            | [object]  | The services where the exclusion filter is deployed.                                                                                                                                                                                                  |
| scope        | env              | string    | Deploy on this environment.                                                                                                                                                                                                                           |
| scope        | service          | string    | Deploy on this service.                                                                                                                                                                                                                               |
| attributes   | search_query     | string    | Generated event search query for traces matching the exclusion filter.                                                                                                                                                                                |
| data         | id               | string    | The identifier of the WAF exclusion filter.                                                                                                                                                                                                           |
| data         | type             | enum      | Type of the resource. The value should always be `exclusion_filter`. Allowed enum values: `exclusion_filter`                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Exclude false positives on a path",
      "enabled": true,
      "event_query": "string",
      "ip_list": [
        "198.51.100.72"
      ],
      "metadata": {
        "added_at": "2019-09-19T10:00:00.000Z",
        "added_by": "string",
        "added_by_name": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "modified_by": "string",
        "modified_by_name": "string"
      },
      "on_match": "string",
      "parameters": [
        "list.search.query"
      ],
      "path_glob": "/accounts/*",
      "rules_target": [
        {
          "rule_id": "dog-913-009",
          "tags": {
            "category": "attack_attempt",
            "type": "lfi"
          }
        }
      ],
      "scope": [
        {
          "env": "www",
          "service": "prod"
        }
      ],
      "search_query": "string"
    },
    "id": "3dd-0uc-h1s",
    "type": "exclusion_filter"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Exclude false positives on a path",
      "enabled": true,
      "parameters": [
        "list.search.query"
      ],
      "path_glob": "/accounts/*",
      "rules_target": [
        {
          "tags": {
            "category": "attack_attempt",
            "type": "lfi"
          }
        }
      ],
      "scope": [
        {
          "env": "www",
          "service": "prod"
        }
      ]
    },
    "type": "exclusion_filter"
  }
}
EOF
                        
##### 

```go
// Create a WAF exclusion filter returns "OK" response

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
	body := datadogV2.ApplicationSecurityWafExclusionFilterCreateRequest{
		Data: datadogV2.ApplicationSecurityWafExclusionFilterCreateData{
			Attributes: datadogV2.ApplicationSecurityWafExclusionFilterCreateAttributes{
				Description: "Exclude false positives on a path",
				Enabled:     true,
				Parameters: []string{
					"list.search.query",
				},
				PathGlob: datadog.PtrString("/accounts/*"),
				RulesTarget: []datadogV2.ApplicationSecurityWafExclusionFilterRulesTarget{
					{
						Tags: &datadogV2.ApplicationSecurityWafExclusionFilterRulesTargetTags{
							Category: datadog.PtrString("attack_attempt"),
							Type:     datadog.PtrString("lfi"),
						},
					},
				},
				Scope: []datadogV2.ApplicationSecurityWafExclusionFilterScope{
					{
						Env:     datadog.PtrString("www"),
						Service: datadog.PtrString("prod"),
					},
				},
			},
			Type: datadogV2.APPLICATIONSECURITYWAFEXCLUSIONFILTERTYPE_EXCLUSION_FILTER,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.CreateApplicationSecurityWafExclusionFilter(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.CreateApplicationSecurityWafExclusionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.CreateApplicationSecurityWafExclusionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a WAF exclusion filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterCreateAttributes;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterCreateData;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterCreateRequest;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterResponse;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterRulesTarget;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterRulesTargetTags;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterScope;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    ApplicationSecurityWafExclusionFilterCreateRequest body =
        new ApplicationSecurityWafExclusionFilterCreateRequest()
            .data(
                new ApplicationSecurityWafExclusionFilterCreateData()
                    .attributes(
                        new ApplicationSecurityWafExclusionFilterCreateAttributes()
                            .description("Exclude false positives on a path")
                            .enabled(true)
                            .parameters(Collections.singletonList("list.search.query"))
                            .pathGlob("/accounts/*")
                            .rulesTarget(
                                Collections.singletonList(
                                    new ApplicationSecurityWafExclusionFilterRulesTarget()
                                        .tags(
                                            new ApplicationSecurityWafExclusionFilterRulesTargetTags()
                                                .category("attack_attempt")
                                                .type("lfi"))))
                            .scope(
                                Collections.singletonList(
                                    new ApplicationSecurityWafExclusionFilterScope()
                                        .env("www")
                                        .service("prod"))))
                    .type(ApplicationSecurityWafExclusionFilterType.EXCLUSION_FILTER));

    try {
      ApplicationSecurityWafExclusionFilterResponse result =
          apiInstance.createApplicationSecurityWafExclusionFilter(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling"
              + " ApplicationSecurityApi#createApplicationSecurityWafExclusionFilter");
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
Create a WAF exclusion filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_attributes import (
    ApplicationSecurityWafExclusionFilterCreateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_data import (
    ApplicationSecurityWafExclusionFilterCreateData,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_request import (
    ApplicationSecurityWafExclusionFilterCreateRequest,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target import (
    ApplicationSecurityWafExclusionFilterRulesTarget,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target_tags import (
    ApplicationSecurityWafExclusionFilterRulesTargetTags,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_scope import (
    ApplicationSecurityWafExclusionFilterScope,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
    ApplicationSecurityWafExclusionFilterType,
)

body = ApplicationSecurityWafExclusionFilterCreateRequest(
    data=ApplicationSecurityWafExclusionFilterCreateData(
        attributes=ApplicationSecurityWafExclusionFilterCreateAttributes(
            description="Exclude false positives on a path",
            enabled=True,
            parameters=[
                "list.search.query",
            ],
            path_glob="/accounts/*",
            rules_target=[
                ApplicationSecurityWafExclusionFilterRulesTarget(
                    tags=ApplicationSecurityWafExclusionFilterRulesTargetTags(
                        category="attack_attempt",
                        type="lfi",
                    ),
                ),
            ],
            scope=[
                ApplicationSecurityWafExclusionFilterScope(
                    env="www",
                    service="prod",
                ),
            ],
        ),
        type=ApplicationSecurityWafExclusionFilterType.EXCLUSION_FILTER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.create_application_security_waf_exclusion_filter(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a WAF exclusion filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new

body = DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterCreateRequest.new({
  data: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterCreateData.new({
    attributes: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterCreateAttributes.new({
      description: "Exclude false positives on a path",
      enabled: true,
      parameters: [
        "list.search.query",
      ],
      path_glob: "/accounts/*",
      rules_target: [
        DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterRulesTarget.new({
          tags: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterRulesTargetTags.new({
            category: "attack_attempt",
            type: "lfi",
          }),
        }),
      ],
      scope: [
        DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterScope.new({
          env: "www",
          service: "prod",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterType::EXCLUSION_FILTER,
  }),
})
p api_instance.create_application_security_waf_exclusion_filter(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a WAF exclusion filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterCreateAttributes;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterCreateData;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterCreateRequest;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterRulesTarget;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterRulesTargetTags;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterScope;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterType;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = ApplicationSecurityWafExclusionFilterCreateRequest::new(
        ApplicationSecurityWafExclusionFilterCreateData::new(
            ApplicationSecurityWafExclusionFilterCreateAttributes::new(
                "Exclude false positives on a path".to_string(),
                true,
            )
            .parameters(vec!["list.search.query".to_string()])
            .path_glob("/accounts/*".to_string())
            .rules_target(vec![ApplicationSecurityWafExclusionFilterRulesTarget::new(
            )
            .tags(
                ApplicationSecurityWafExclusionFilterRulesTargetTags::new()
                    .category("attack_attempt".to_string())
                    .type_("lfi".to_string())
                    .additional_properties(BTreeMap::from([])),
            )])
            .scope(vec![ApplicationSecurityWafExclusionFilterScope::new()
                .env("www".to_string())
                .service("prod".to_string())]),
            ApplicationSecurityWafExclusionFilterType::EXCLUSION_FILTER,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api
        .create_application_security_waf_exclusion_filter(body)
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
 * Create a WAF exclusion filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

const params: v2.ApplicationSecurityApiCreateApplicationSecurityWafExclusionFilterRequest =
  {
    body: {
      data: {
        attributes: {
          description: "Exclude false positives on a path",
          enabled: true,
          parameters: ["list.search.query"],
          pathGlob: "/accounts/*",
          rulesTarget: [
            {
              tags: {
                category: "attack_attempt",
                type: "lfi",
              },
            },
          ],
          scope: [
            {
              env: "www",
              service: "prod",
            },
          ],
        },
        type: "exclusion_filter",
      },
    },
  };

apiInstance
  .createApplicationSecurityWafExclusionFilter(params)
  .then((data: v2.ApplicationSecurityWafExclusionFilterResponse) => {
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

## List all WAF exclusion filters{% #list-all-waf-exclusion-filters %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/exclusion_filters      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/exclusion_filters      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters |

### Overview

Retrieve a list of WAF exclusion filters. This endpoint requires the `appsec_protect_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for multiple WAF exclusion filters.

| Parent field | Field            | Type      | Description                                                                                                                                                                                                                                           |
| ------------ | ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | [object]  | A list of WAF exclusion filters.                                                                                                                                                                                                                      |
| data         | attributes       | object    | Attributes describing a WAF exclusion filter.                                                                                                                                                                                                         |
| attributes   | description      | string    | A description for the exclusion filter.                                                                                                                                                                                                               |
| attributes   | enabled          | boolean   | Indicates whether the exclusion filter is enabled.                                                                                                                                                                                                    |
| attributes   | event_query      | string    | The event query matched by the legacy exclusion filter. Cannot be created nor updated.                                                                                                                                                                |
| attributes   | ip_list          | [string]  | The client IP addresses matched by the exclusion filter (CIDR notation is supported).                                                                                                                                                                 |
| attributes   | metadata         | object    | Extra information about the exclusion filter.                                                                                                                                                                                                         |
| metadata     | added_at         | date-time | The creation date of the exclusion filter.                                                                                                                                                                                                            |
| metadata     | added_by         | string    | The handle of the user who created the exclusion filter.                                                                                                                                                                                              |
| metadata     | added_by_name    | string    | The name of the user who created the exclusion filter.                                                                                                                                                                                                |
| metadata     | modified_at      | date-time | The last modification date of the exclusion filter.                                                                                                                                                                                                   |
| metadata     | modified_by      | string    | The handle of the user who last modified the exclusion filter.                                                                                                                                                                                        |
| metadata     | modified_by_name | string    | The name of the user who last modified the exclusion filter.                                                                                                                                                                                          |
| attributes   | on_match         | enum      | The action taken when the exclusion filter matches. When set to `monitor`, security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked. Allowed enum values: `monitor` |
| attributes   | parameters       | [string]  | A list of parameters matched by the exclusion filter in the HTTP query string and HTTP request body. Nested parameters can be matched by joining fields with a dot character.                                                                         |
| attributes   | path_glob        | string    | The HTTP path glob expression matched by the exclusion filter.                                                                                                                                                                                        |
| attributes   | rules_target     | [object]  | The WAF rules targeted by the exclusion filter.                                                                                                                                                                                                       |
| rules_target | rule_id          | string    | Target a single WAF rule based on its identifier.                                                                                                                                                                                                     |
| rules_target | tags             | object    | Target multiple WAF rules based on their tags.                                                                                                                                                                                                        |
| tags         | category         | string    | The category of the targeted WAF rules.                                                                                                                                                                                                               |
| tags         | type             | string    | The type of the targeted WAF rules.                                                                                                                                                                                                                   |
| attributes   | scope            | [object]  | The services where the exclusion filter is deployed.                                                                                                                                                                                                  |
| scope        | env              | string    | Deploy on this environment.                                                                                                                                                                                                                           |
| scope        | service          | string    | Deploy on this service.                                                                                                                                                                                                                               |
| attributes   | search_query     | string    | Generated event search query for traces matching the exclusion filter.                                                                                                                                                                                |
| data         | id               | string    | The identifier of the WAF exclusion filter.                                                                                                                                                                                                           |
| data         | type             | enum      | Type of the resource. The value should always be `exclusion_filter`. Allowed enum values: `exclusion_filter`                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "description": "Exclude false positives on a path",
        "enabled": true,
        "event_query": "string",
        "ip_list": [
          "198.51.100.72"
        ],
        "metadata": {
          "added_at": "2019-09-19T10:00:00.000Z",
          "added_by": "string",
          "added_by_name": "string",
          "modified_at": "2019-09-19T10:00:00.000Z",
          "modified_by": "string",
          "modified_by_name": "string"
        },
        "on_match": "string",
        "parameters": [
          "list.search.query"
        ],
        "path_glob": "/accounts/*",
        "rules_target": [
          {
            "rule_id": "dog-913-009",
            "tags": {
              "category": "attack_attempt",
              "type": "lfi"
            }
          }
        ],
        "scope": [
          {
            "env": "www",
            "service": "prod"
          }
        ],
        "search_query": "string"
      },
      "id": "3dd-0uc-h1s",
      "type": "exclusion_filter"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List all WAF exclusion filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.list_application_security_waf_exclusion_filters()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List all WAF exclusion filters returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new
p api_instance.list_application_security_waf_exclusion_filters()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List all WAF exclusion filters returns "OK" response

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
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.ListApplicationSecurityWafExclusionFilters(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.ListApplicationSecurityWafExclusionFilters`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.ListApplicationSecurityWafExclusionFilters`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List all WAF exclusion filters returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFiltersResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    try {
      ApplicationSecurityWafExclusionFiltersResponse result =
          apiInstance.listApplicationSecurityWafExclusionFilters();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling"
              + " ApplicationSecurityApi#listApplicationSecurityWafExclusionFilters");
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
// List all WAF exclusion filters returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api.list_application_security_waf_exclusion_filters().await;
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
 * List all WAF exclusion filters returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

apiInstance
  .listApplicationSecurityWafExclusionFilters()
  .then((data: v2.ApplicationSecurityWafExclusionFiltersResponse) => {
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

## Update a WAF exclusion filter{% #update-a-waf-exclusion-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |

### Overview

Update a specific WAF exclusion filter using its identifier. Returns the exclusion filter object when the request is successful. This endpoint requires the `appsec_protect_write` permission.

### Arguments

#### Path Parameters

| Name                                  | Type   | Description                                 |
| ------------------------------------- | ------ | ------------------------------------------- |
| exclusion_filter_id [*required*] | string | The identifier of the WAF exclusion filter. |

### Request

#### Body Data (required)

The exclusion filter to update.

{% tab title="Model" %}

| Parent field | Field                         | Type     | Description                                                                                                                                                                                                                                           |
| ------------ | ----------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]        | object   | Object for updating a single WAF exclusion filter.                                                                                                                                                                                                    |
| data         | attributes [*required*]  | object   | Attributes for updating a WAF exclusion filter.                                                                                                                                                                                                       |
| attributes   | description [*required*] | string   | A description for the exclusion filter.                                                                                                                                                                                                               |
| attributes   | enabled [*required*]     | boolean  | Indicates whether the exclusion filter is enabled.                                                                                                                                                                                                    |
| attributes   | ip_list                       | [string] | The client IP addresses matched by the exclusion filter (CIDR notation is supported).                                                                                                                                                                 |
| attributes   | on_match                      | enum     | The action taken when the exclusion filter matches. When set to `monitor`, security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked. Allowed enum values: `monitor` |
| attributes   | parameters                    | [string] | A list of parameters matched by the exclusion filter in the HTTP query string and HTTP request body. Nested parameters can be matched by joining fields with a dot character.                                                                         |
| attributes   | path_glob                     | string   | The HTTP path glob expression matched by the exclusion filter.                                                                                                                                                                                        |
| attributes   | rules_target                  | [object] | The WAF rules targeted by the exclusion filter.                                                                                                                                                                                                       |
| rules_target | rule_id                       | string   | Target a single WAF rule based on its identifier.                                                                                                                                                                                                     |
| rules_target | tags                          | object   | Target multiple WAF rules based on their tags.                                                                                                                                                                                                        |
| tags         | category                      | string   | The category of the targeted WAF rules.                                                                                                                                                                                                               |
| tags         | type                          | string   | The type of the targeted WAF rules.                                                                                                                                                                                                                   |
| attributes   | scope                         | [object] | The services where the exclusion filter is deployed.                                                                                                                                                                                                  |
| scope        | env                           | string   | Deploy on this environment.                                                                                                                                                                                                                           |
| scope        | service                       | string   | Deploy on this service.                                                                                                                                                                                                                               |
| data         | type [*required*]        | enum     | Type of the resource. The value should always be `exclusion_filter`. Allowed enum values: `exclusion_filter`                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Exclude false positives on a path",
      "enabled": false,
      "ip_list": [
        "198.51.100.72"
      ],
      "on_match": "monitor"
    },
    "type": "exclusion_filter"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a single WAF exclusion filter.

| Parent field | Field            | Type      | Description                                                                                                                                                                                                                                           |
| ------------ | ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | object    | A JSON:API resource for an WAF exclusion filter.                                                                                                                                                                                                      |
| data         | attributes       | object    | Attributes describing a WAF exclusion filter.                                                                                                                                                                                                         |
| attributes   | description      | string    | A description for the exclusion filter.                                                                                                                                                                                                               |
| attributes   | enabled          | boolean   | Indicates whether the exclusion filter is enabled.                                                                                                                                                                                                    |
| attributes   | event_query      | string    | The event query matched by the legacy exclusion filter. Cannot be created nor updated.                                                                                                                                                                |
| attributes   | ip_list          | [string]  | The client IP addresses matched by the exclusion filter (CIDR notation is supported).                                                                                                                                                                 |
| attributes   | metadata         | object    | Extra information about the exclusion filter.                                                                                                                                                                                                         |
| metadata     | added_at         | date-time | The creation date of the exclusion filter.                                                                                                                                                                                                            |
| metadata     | added_by         | string    | The handle of the user who created the exclusion filter.                                                                                                                                                                                              |
| metadata     | added_by_name    | string    | The name of the user who created the exclusion filter.                                                                                                                                                                                                |
| metadata     | modified_at      | date-time | The last modification date of the exclusion filter.                                                                                                                                                                                                   |
| metadata     | modified_by      | string    | The handle of the user who last modified the exclusion filter.                                                                                                                                                                                        |
| metadata     | modified_by_name | string    | The name of the user who last modified the exclusion filter.                                                                                                                                                                                          |
| attributes   | on_match         | enum      | The action taken when the exclusion filter matches. When set to `monitor`, security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked. Allowed enum values: `monitor` |
| attributes   | parameters       | [string]  | A list of parameters matched by the exclusion filter in the HTTP query string and HTTP request body. Nested parameters can be matched by joining fields with a dot character.                                                                         |
| attributes   | path_glob        | string    | The HTTP path glob expression matched by the exclusion filter.                                                                                                                                                                                        |
| attributes   | rules_target     | [object]  | The WAF rules targeted by the exclusion filter.                                                                                                                                                                                                       |
| rules_target | rule_id          | string    | Target a single WAF rule based on its identifier.                                                                                                                                                                                                     |
| rules_target | tags             | object    | Target multiple WAF rules based on their tags.                                                                                                                                                                                                        |
| tags         | category         | string    | The category of the targeted WAF rules.                                                                                                                                                                                                               |
| tags         | type             | string    | The type of the targeted WAF rules.                                                                                                                                                                                                                   |
| attributes   | scope            | [object]  | The services where the exclusion filter is deployed.                                                                                                                                                                                                  |
| scope        | env              | string    | Deploy on this environment.                                                                                                                                                                                                                           |
| scope        | service          | string    | Deploy on this service.                                                                                                                                                                                                                               |
| attributes   | search_query     | string    | Generated event search query for traces matching the exclusion filter.                                                                                                                                                                                |
| data         | id               | string    | The identifier of the WAF exclusion filter.                                                                                                                                                                                                           |
| data         | type             | enum      | Type of the resource. The value should always be `exclusion_filter`. Allowed enum values: `exclusion_filter`                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Exclude false positives on a path",
      "enabled": true,
      "event_query": "string",
      "ip_list": [
        "198.51.100.72"
      ],
      "metadata": {
        "added_at": "2019-09-19T10:00:00.000Z",
        "added_by": "string",
        "added_by_name": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "modified_by": "string",
        "modified_by_name": "string"
      },
      "on_match": "string",
      "parameters": [
        "list.search.query"
      ],
      "path_glob": "/accounts/*",
      "rules_target": [
        {
          "rule_id": "dog-913-009",
          "tags": {
            "category": "attack_attempt",
            "type": "lfi"
          }
        }
      ],
      "scope": [
        {
          "env": "www",
          "service": "prod"
        }
      ],
      "search_query": "string"
    },
    "id": "3dd-0uc-h1s",
    "type": "exclusion_filter"
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
                          \# Path parametersexport exclusion_filter_id="3b5-v82-ns6"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/${exclusion_filter_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Exclude false positives on a path",
      "enabled": false,
      "ip_list": [
        "198.51.100.72"
      ],
      "on_match": "monitor"
    },
    "type": "exclusion_filter"
  }
}
EOF
                        
##### 

```go
// Update a WAF exclusion filter returns "OK" response

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
	// there is a valid "exclusion_filter" in the system
	ExclusionFilterDataID := os.Getenv("EXCLUSION_FILTER_DATA_ID")

	body := datadogV2.ApplicationSecurityWafExclusionFilterUpdateRequest{
		Data: datadogV2.ApplicationSecurityWafExclusionFilterUpdateData{
			Attributes: datadogV2.ApplicationSecurityWafExclusionFilterUpdateAttributes{
				Description: "Exclude false positives on a path",
				Enabled:     false,
				IpList: []string{
					"198.51.100.72",
				},
				OnMatch: datadogV2.APPLICATIONSECURITYWAFEXCLUSIONFILTERONMATCH_MONITOR.Ptr(),
			},
			Type: datadogV2.APPLICATIONSECURITYWAFEXCLUSIONFILTERTYPE_EXCLUSION_FILTER,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.UpdateApplicationSecurityWafExclusionFilter(ctx, ExclusionFilterDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.UpdateApplicationSecurityWafExclusionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.UpdateApplicationSecurityWafExclusionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a WAF exclusion filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterOnMatch;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterResponse;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterType;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterUpdateAttributes;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterUpdateData;
import com.datadog.api.client.v2.model.ApplicationSecurityWafExclusionFilterUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    // there is a valid "exclusion_filter" in the system
    String EXCLUSION_FILTER_DATA_ID = System.getenv("EXCLUSION_FILTER_DATA_ID");

    ApplicationSecurityWafExclusionFilterUpdateRequest body =
        new ApplicationSecurityWafExclusionFilterUpdateRequest()
            .data(
                new ApplicationSecurityWafExclusionFilterUpdateData()
                    .attributes(
                        new ApplicationSecurityWafExclusionFilterUpdateAttributes()
                            .description("Exclude false positives on a path")
                            .enabled(false)
                            .ipList(Collections.singletonList("198.51.100.72"))
                            .onMatch(ApplicationSecurityWafExclusionFilterOnMatch.MONITOR))
                    .type(ApplicationSecurityWafExclusionFilterType.EXCLUSION_FILTER));

    try {
      ApplicationSecurityWafExclusionFilterResponse result =
          apiInstance.updateApplicationSecurityWafExclusionFilter(EXCLUSION_FILTER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling"
              + " ApplicationSecurityApi#updateApplicationSecurityWafExclusionFilter");
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
Update a WAF exclusion filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_on_match import (
    ApplicationSecurityWafExclusionFilterOnMatch,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
    ApplicationSecurityWafExclusionFilterType,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_update_attributes import (
    ApplicationSecurityWafExclusionFilterUpdateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_update_data import (
    ApplicationSecurityWafExclusionFilterUpdateData,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_update_request import (
    ApplicationSecurityWafExclusionFilterUpdateRequest,
)

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = environ["EXCLUSION_FILTER_DATA_ID"]

body = ApplicationSecurityWafExclusionFilterUpdateRequest(
    data=ApplicationSecurityWafExclusionFilterUpdateData(
        attributes=ApplicationSecurityWafExclusionFilterUpdateAttributes(
            description="Exclude false positives on a path",
            enabled=False,
            ip_list=[
                "198.51.100.72",
            ],
            on_match=ApplicationSecurityWafExclusionFilterOnMatch.MONITOR,
        ),
        type=ApplicationSecurityWafExclusionFilterType.EXCLUSION_FILTER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.update_application_security_waf_exclusion_filter(
        exclusion_filter_id=EXCLUSION_FILTER_DATA_ID, body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a WAF exclusion filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = ENV["EXCLUSION_FILTER_DATA_ID"]

body = DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterUpdateRequest.new({
  data: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterUpdateData.new({
    attributes: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterUpdateAttributes.new({
      description: "Exclude false positives on a path",
      enabled: false,
      ip_list: [
        "198.51.100.72",
      ],
      on_match: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterOnMatch::MONITOR,
    }),
    type: DatadogAPIClient::V2::ApplicationSecurityWafExclusionFilterType::EXCLUSION_FILTER,
  }),
})
p api_instance.update_application_security_waf_exclusion_filter(EXCLUSION_FILTER_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update a WAF exclusion filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterOnMatch;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterType;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterUpdateAttributes;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterUpdateData;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafExclusionFilterUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "exclusion_filter" in the system
    let exclusion_filter_data_id = std::env::var("EXCLUSION_FILTER_DATA_ID").unwrap();
    let body = ApplicationSecurityWafExclusionFilterUpdateRequest::new(
        ApplicationSecurityWafExclusionFilterUpdateData::new(
            ApplicationSecurityWafExclusionFilterUpdateAttributes::new(
                "Exclude false positives on a path".to_string(),
                false,
            )
            .ip_list(vec!["198.51.100.72".to_string()])
            .on_match(ApplicationSecurityWafExclusionFilterOnMatch::MONITOR),
            ApplicationSecurityWafExclusionFilterType::EXCLUSION_FILTER,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api
        .update_application_security_waf_exclusion_filter(exclusion_filter_data_id.clone(), body)
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
 * Update a WAF exclusion filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

// there is a valid "exclusion_filter" in the system
const EXCLUSION_FILTER_DATA_ID = process.env.EXCLUSION_FILTER_DATA_ID as string;

const params: v2.ApplicationSecurityApiUpdateApplicationSecurityWafExclusionFilterRequest =
  {
    body: {
      data: {
        attributes: {
          description: "Exclude false positives on a path",
          enabled: false,
          ipList: ["198.51.100.72"],
          onMatch: "monitor",
        },
        type: "exclusion_filter",
      },
    },
    exclusionFilterId: EXCLUSION_FILTER_DATA_ID,
  };

apiInstance
  .updateApplicationSecurityWafExclusionFilter(params)
  .then((data: v2.ApplicationSecurityWafExclusionFilterResponse) => {
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

## Delete a WAF exclusion filter{% #delete-a-waf-exclusion-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id} |

### Overview

Delete a specific WAF exclusion filter using its identifier. This endpoint requires the `appsec_protect_write` permission.

### Arguments

#### Path Parameters

| Name                                  | Type   | Description                                 |
| ------------------------------------- | ------ | ------------------------------------------- |
| exclusion_filter_id [*required*] | string | The identifier of the WAF exclusion filter. |

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
                  \# Path parametersexport exclusion_filter_id="3b5-v82-ns6"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/exclusion_filters/${exclusion_filter_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a WAF exclusion filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = environ["EXCLUSION_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    api_instance.delete_application_security_waf_exclusion_filter(
        exclusion_filter_id=EXCLUSION_FILTER_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a WAF exclusion filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = ENV["EXCLUSION_FILTER_DATA_ID"]
api_instance.delete_application_security_waf_exclusion_filter(EXCLUSION_FILTER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a WAF exclusion filter returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "exclusion_filter" in the system
	ExclusionFilterDataID := os.Getenv("EXCLUSION_FILTER_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	r, err := api.DeleteApplicationSecurityWafExclusionFilter(ctx, ExclusionFilterDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.DeleteApplicationSecurityWafExclusionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a WAF exclusion filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    // there is a valid "exclusion_filter" in the system
    String EXCLUSION_FILTER_DATA_ID = System.getenv("EXCLUSION_FILTER_DATA_ID");

    try {
      apiInstance.deleteApplicationSecurityWafExclusionFilter(EXCLUSION_FILTER_DATA_ID);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling"
              + " ApplicationSecurityApi#deleteApplicationSecurityWafExclusionFilter");
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
// Delete a WAF exclusion filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;

#[tokio::main]
async fn main() {
    // there is a valid "exclusion_filter" in the system
    let exclusion_filter_data_id = std::env::var("EXCLUSION_FILTER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api
        .delete_application_security_waf_exclusion_filter(exclusion_filter_data_id.clone())
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
 * Delete a WAF exclusion filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

// there is a valid "exclusion_filter" in the system
const EXCLUSION_FILTER_DATA_ID = process.env.EXCLUSION_FILTER_DATA_ID as string;

const params: v2.ApplicationSecurityApiDeleteApplicationSecurityWafExclusionFilterRequest =
  {
    exclusionFilterId: EXCLUSION_FILTER_DATA_ID,
  };

apiInstance
  .deleteApplicationSecurityWafExclusionFilter(params)
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

## Get a WAF custom rule{% #get-a-waf-custom-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |

### Overview

Retrieve a WAF custom rule by ID.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| custom_rule_id [*required*] | string | The ID of the custom rule. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a single WAF custom rule.

| Parent field | Field                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object    | Object for a single WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| data         | attributes                   | object    | A WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| attributes   | action                       | object    | The definition of `ApplicationSecurityWafCustomRuleAction` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| action       | action                       | enum      | Override the default action to take when the WAF custom rule would block. Allowed enum values: `redirect_request,block_request`                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| action       | parameters                   | object    | The definition of `ApplicationSecurityWafCustomRuleActionParameters` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | location                     | string    | The location to redirect to when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| parameters   | status_code                  | int64     | The status code to return when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes   | blocking [*required*]   | boolean   | Indicates whether the WAF custom rule will block the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | conditions [*required*] | [object]  | Conditions for which the WAF Custom Rule will triggers, all conditions needs to match in order for the WAF rule to trigger.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| conditions   | operator [*required*]   | enum      | Operator to use for the WAF Condition. Allowed enum values: `match_regex,!match_regex,phrase_match,!phrase_match,is_xss,is_sqli,exact_match,!exact_match,ip_match,!ip_match,capture_data`                                                                                                                                                                                                                                                                                                                                                                                           |
| conditions   | parameters [*required*] | object    | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| parameters   | data                         | string    | Identifier of a list of data from the denylist. Can only be used as substitution from the list parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parameters   | inputs [*required*]     | [object]  | List of inputs on which at least one should match with the given operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| inputs       | address [*required*]    | enum      | Input from the request on which the condition should apply. Allowed enum values: `server.db.statement,server.io.fs.file,server.io.net.url,server.sys.shell.cmd,server.request.method,server.request.uri.raw,server.request.path_params,server.request.query,server.request.headers.no_cookies,server.request.cookies,server.request.trailers,server.request.body,server.response.status,server.response.headers.no_cookies,server.response.trailers,grpc.server.request.metadata,grpc.server.request.message,grpc.server.method,graphql.server.all_resolvers,usr.id,http.client_ip` |
| inputs       | key_path                     | [string]  | Specific path for the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | list                         | [string]  | List of value to use with the condition. Only used with the phrase_match, !phrase_match, exact_match and !exact_match operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| parameters   | options                      | object    | Options for the operator of this condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| options      | case_sensitive               | boolean   | Evaluate the value as case sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options      | min_length                   | int64     | Only evaluate this condition if the value has a minimum amount of characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| parameters   | regex                        | string    | Regex to use with the condition. Only used with match_regex and !match_regex operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| parameters   | value                        | string    | Store the captured value in the specified tag name. Only used with the capture_data operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | enabled [*required*]    | boolean   | Indicates whether the WAF custom rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes   | metadata                     | object    | Metadata associated with the WAF Custom Rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| metadata     | added_at                     | date-time | The date and time the WAF custom rule was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| metadata     | added_by                     | string    | The handle of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | added_by_name                | string    | The name of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| metadata     | modified_at                  | date-time | The date and time the WAF custom rule was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | modified_by                  | string    | The handle of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| metadata     | modified_by_name             | string    | The name of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | name [*required*]       | string    | The Name of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| attributes   | path_glob                    | string    | The path glob for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes   | scope                        | [object]  | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| scope        | env [*required*]        | string    | The environment scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scope        | service [*required*]    | string    | The service scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | tags [*required*]       | object    | Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security activity field associated with the traces.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags         | category [*required*]   | enum      | The category of the WAF Rule, can be either `business_logic`, `attack_attempt` or `security_response`. Allowed enum values: `attack_attempt,business_logic,security_response`                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags         | type [*required*]       | string    | The type of the WAF rule, associated with the category will form the security activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| data         | id                           | string    | The ID of the custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| data         | type                         | enum      | The type of the resource. The value should always be `custom_rule`. Allowed enum values: `custom_rule`                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "action": {
        "action": "block_request",
        "parameters": {
          "location": "/blocking",
          "status_code": 403
        }
      },
      "blocking": false,
      "conditions": [
        {
          "operator": "match_regex",
          "parameters": {
            "data": "blocked_users",
            "inputs": [
              {
                "address": "server.db.statement",
                "key_path": []
              }
            ],
            "list": [],
            "options": {
              "case_sensitive": false,
              "min_length": "integer"
            },
            "regex": "path.*",
            "value": "custom_tag"
          }
        }
      ],
      "enabled": false,
      "metadata": {
        "added_at": "2021-01-01T00:00:00Z",
        "added_by": "john.doe@datadoghq.com",
        "added_by_name": "John Doe",
        "modified_at": "2021-01-01T00:00:00Z",
        "modified_by": "john.doe@datadoghq.com",
        "modified_by_name": "John Doe"
      },
      "name": "Block request from bad useragent",
      "path_glob": "/api/search/*",
      "scope": [
        {
          "env": "prod",
          "service": "billing-service"
        }
      ],
      "tags": {
        "category": "business_logic",
        "type": "users.login.success"
      }
    },
    "id": "2857c47d-1e3a-4300-8b2f-dc24089c084b",
    "type": "custom_rule"
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
                  \# Path parametersexport custom_rule_id="3b5-v82-ns6"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/${custom_rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a WAF custom rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.get_application_security_waf_custom_rule(
        custom_rule_id="custom_rule_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a WAF custom rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new
p api_instance.get_application_security_waf_custom_rule("custom_rule_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a WAF custom rule returns "OK" response

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
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.GetApplicationSecurityWafCustomRule(ctx, "custom_rule_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.GetApplicationSecurityWafCustomRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.GetApplicationSecurityWafCustomRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a WAF custom rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    try {
      ApplicationSecurityWafCustomRuleResponse result =
          apiInstance.getApplicationSecurityWafCustomRule("3b5-v82-ns6");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ApplicationSecurityApi#getApplicationSecurityWafCustomRule");
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
// Get a WAF custom rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api
        .get_application_security_waf_custom_rule("custom_rule_id".to_string())
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
 * Get a WAF custom rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

const params: v2.ApplicationSecurityApiGetApplicationSecurityWafCustomRuleRequest =
  {
    customRuleId: "custom_rule_id",
  };

apiInstance
  .getApplicationSecurityWafCustomRule(params)
  .then((data: v2.ApplicationSecurityWafCustomRuleResponse) => {
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

## Create a WAF custom rule{% #create-a-waf-custom-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/custom_rules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/custom_rules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |

### Overview

Create a new WAF custom rule with the given parameters.

### Request

#### Body Data (required)

The definition of the new WAF Custom Rule.

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Object for a single WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| data         | attributes [*required*] | object   | Create a new WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | action                       | object   | The definition of `ApplicationSecurityWafCustomRuleAction` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| action       | action                       | enum     | Override the default action to take when the WAF custom rule would block. Allowed enum values: `redirect_request,block_request`                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| action       | parameters                   | object   | The definition of `ApplicationSecurityWafCustomRuleActionParameters` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | location                     | string   | The location to redirect to when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| parameters   | status_code                  | int64    | The status code to return when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes   | blocking [*required*]   | boolean  | Indicates whether the WAF custom rule will block the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | conditions [*required*] | [object] | Conditions for which the WAF Custom Rule will triggers, all conditions needs to match in order for the WAF rule to trigger                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| conditions   | operator [*required*]   | enum     | Operator to use for the WAF Condition. Allowed enum values: `match_regex,!match_regex,phrase_match,!phrase_match,is_xss,is_sqli,exact_match,!exact_match,ip_match,!ip_match,capture_data`                                                                                                                                                                                                                                                                                                                                                                                           |
| conditions   | parameters [*required*] | object   | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| parameters   | data                         | string   | Identifier of a list of data from the denylist. Can only be used as substitution from the list parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parameters   | inputs [*required*]     | [object] | List of inputs on which at least one should match with the given operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| inputs       | address [*required*]    | enum     | Input from the request on which the condition should apply. Allowed enum values: `server.db.statement,server.io.fs.file,server.io.net.url,server.sys.shell.cmd,server.request.method,server.request.uri.raw,server.request.path_params,server.request.query,server.request.headers.no_cookies,server.request.cookies,server.request.trailers,server.request.body,server.response.status,server.response.headers.no_cookies,server.response.trailers,grpc.server.request.metadata,grpc.server.request.message,grpc.server.method,graphql.server.all_resolvers,usr.id,http.client_ip` |
| inputs       | key_path                     | [string] | Specific path for the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | list                         | [string] | List of value to use with the condition. Only used with the phrase_match, !phrase_match, exact_match and !exact_match operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| parameters   | options                      | object   | Options for the operator of this condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| options      | case_sensitive               | boolean  | Evaluate the value as case sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options      | min_length                   | int64    | Only evaluate this condition if the value has a minimum amount of characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| parameters   | regex                        | string   | Regex to use with the condition. Only used with match_regex and !match_regex operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| parameters   | value                        | string   | Store the captured value in the specified tag name. Only used with the capture_data operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | enabled [*required*]    | boolean  | Indicates whether the WAF custom rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes   | name [*required*]       | string   | The Name of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| attributes   | path_glob                    | string   | The path glob for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes   | scope                        | [object] | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| scope        | env [*required*]        | string   | The environment scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scope        | service [*required*]    | string   | The service scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | tags [*required*]       | object   | Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security activity field associated with the traces.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags         | category [*required*]   | enum     | The category of the WAF Rule, can be either `business_logic`, `attack_attempt` or `security_response`. Allowed enum values: `attack_attempt,business_logic,security_response`                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags         | type [*required*]       | string   | The type of the WAF rule, associated with the category will form the security activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| data         | type [*required*]       | enum     | The type of the resource. The value should always be `custom_rule`. Allowed enum values: `custom_rule`                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "action": {
        "action": "block_request",
        "parameters": {
          "location": "/blocking",
          "status_code": 403
        }
      },
      "blocking": false,
      "conditions": [
        {
          "operator": "match_regex",
          "parameters": {
            "data": "blocked_users",
            "inputs": [
              {
                "address": "server.db.statement",
                "key_path": []
              }
            ],
            "list": [],
            "options": {
              "case_sensitive": false,
              "min_length": "integer"
            },
            "regex": "path.*",
            "value": "custom_tag"
          }
        }
      ],
      "enabled": false,
      "name": "Block request from a bad useragent",
      "path_glob": "/api/search/*",
      "scope": [
        {
          "env": "prod",
          "service": "billing-service"
        }
      ],
      "tags": {
        "category": "business_logic",
        "type": "users.login.success"
      }
    },
    "type": "custom_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response object that includes a single WAF custom rule.

| Parent field | Field                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object    | Object for a single WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| data         | attributes                   | object    | A WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| attributes   | action                       | object    | The definition of `ApplicationSecurityWafCustomRuleAction` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| action       | action                       | enum      | Override the default action to take when the WAF custom rule would block. Allowed enum values: `redirect_request,block_request`                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| action       | parameters                   | object    | The definition of `ApplicationSecurityWafCustomRuleActionParameters` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | location                     | string    | The location to redirect to when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| parameters   | status_code                  | int64     | The status code to return when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes   | blocking [*required*]   | boolean   | Indicates whether the WAF custom rule will block the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | conditions [*required*] | [object]  | Conditions for which the WAF Custom Rule will triggers, all conditions needs to match in order for the WAF rule to trigger.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| conditions   | operator [*required*]   | enum      | Operator to use for the WAF Condition. Allowed enum values: `match_regex,!match_regex,phrase_match,!phrase_match,is_xss,is_sqli,exact_match,!exact_match,ip_match,!ip_match,capture_data`                                                                                                                                                                                                                                                                                                                                                                                           |
| conditions   | parameters [*required*] | object    | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| parameters   | data                         | string    | Identifier of a list of data from the denylist. Can only be used as substitution from the list parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parameters   | inputs [*required*]     | [object]  | List of inputs on which at least one should match with the given operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| inputs       | address [*required*]    | enum      | Input from the request on which the condition should apply. Allowed enum values: `server.db.statement,server.io.fs.file,server.io.net.url,server.sys.shell.cmd,server.request.method,server.request.uri.raw,server.request.path_params,server.request.query,server.request.headers.no_cookies,server.request.cookies,server.request.trailers,server.request.body,server.response.status,server.response.headers.no_cookies,server.response.trailers,grpc.server.request.metadata,grpc.server.request.message,grpc.server.method,graphql.server.all_resolvers,usr.id,http.client_ip` |
| inputs       | key_path                     | [string]  | Specific path for the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | list                         | [string]  | List of value to use with the condition. Only used with the phrase_match, !phrase_match, exact_match and !exact_match operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| parameters   | options                      | object    | Options for the operator of this condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| options      | case_sensitive               | boolean   | Evaluate the value as case sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options      | min_length                   | int64     | Only evaluate this condition if the value has a minimum amount of characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| parameters   | regex                        | string    | Regex to use with the condition. Only used with match_regex and !match_regex operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| parameters   | value                        | string    | Store the captured value in the specified tag name. Only used with the capture_data operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | enabled [*required*]    | boolean   | Indicates whether the WAF custom rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes   | metadata                     | object    | Metadata associated with the WAF Custom Rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| metadata     | added_at                     | date-time | The date and time the WAF custom rule was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| metadata     | added_by                     | string    | The handle of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | added_by_name                | string    | The name of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| metadata     | modified_at                  | date-time | The date and time the WAF custom rule was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | modified_by                  | string    | The handle of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| metadata     | modified_by_name             | string    | The name of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | name [*required*]       | string    | The Name of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| attributes   | path_glob                    | string    | The path glob for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes   | scope                        | [object]  | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| scope        | env [*required*]        | string    | The environment scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scope        | service [*required*]    | string    | The service scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | tags [*required*]       | object    | Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security activity field associated with the traces.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags         | category [*required*]   | enum      | The category of the WAF Rule, can be either `business_logic`, `attack_attempt` or `security_response`. Allowed enum values: `attack_attempt,business_logic,security_response`                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags         | type [*required*]       | string    | The type of the WAF rule, associated with the category will form the security activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| data         | id                           | string    | The ID of the custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| data         | type                         | enum      | The type of the resource. The value should always be `custom_rule`. Allowed enum values: `custom_rule`                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "action": {
        "action": "block_request",
        "parameters": {
          "location": "/blocking",
          "status_code": 403
        }
      },
      "blocking": false,
      "conditions": [
        {
          "operator": "match_regex",
          "parameters": {
            "data": "blocked_users",
            "inputs": [
              {
                "address": "server.db.statement",
                "key_path": []
              }
            ],
            "list": [],
            "options": {
              "case_sensitive": false,
              "min_length": "integer"
            },
            "regex": "path.*",
            "value": "custom_tag"
          }
        }
      ],
      "enabled": false,
      "metadata": {
        "added_at": "2021-01-01T00:00:00Z",
        "added_by": "john.doe@datadoghq.com",
        "added_by_name": "John Doe",
        "modified_at": "2021-01-01T00:00:00Z",
        "modified_by": "john.doe@datadoghq.com",
        "modified_by_name": "John Doe"
      },
      "name": "Block request from bad useragent",
      "path_glob": "/api/search/*",
      "scope": [
        {
          "env": "prod",
          "service": "billing-service"
        }
      ],
      "tags": {
        "category": "business_logic",
        "type": "users.login.success"
      }
    },
    "id": "2857c47d-1e3a-4300-8b2f-dc24089c084b",
    "type": "custom_rule"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "blocking": false,
      "conditions": [
        {
          "operator": "match_regex",
          "parameters": {
            "inputs": [
              {
                "address": "server.db.statement"
              }
            ]
          }
        }
      ],
      "enabled": false,
      "name": "Block request from a bad useragent",
      "scope": [
        {
          "env": "prod",
          "service": "billing-service"
        }
      ],
      "tags": {
        "category": "business_logic",
        "type": "users.login.success"
      }
    },
    "type": "custom_rule"
  }
}
EOF
                
##### 

```python
"""
Create a WAF custom rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_custom_rule_action import (
    ApplicationSecurityWafCustomRuleAction,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_action_action import (
    ApplicationSecurityWafCustomRuleActionAction,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_action_parameters import (
    ApplicationSecurityWafCustomRuleActionParameters,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition import (
    ApplicationSecurityWafCustomRuleCondition,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input import (
    ApplicationSecurityWafCustomRuleConditionInput,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input_address import (
    ApplicationSecurityWafCustomRuleConditionInputAddress,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_operator import (
    ApplicationSecurityWafCustomRuleConditionOperator,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_options import (
    ApplicationSecurityWafCustomRuleConditionOptions,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_parameters import (
    ApplicationSecurityWafCustomRuleConditionParameters,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_create_attributes import (
    ApplicationSecurityWafCustomRuleCreateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_create_data import (
    ApplicationSecurityWafCustomRuleCreateData,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_create_request import (
    ApplicationSecurityWafCustomRuleCreateRequest,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_scope import ApplicationSecurityWafCustomRuleScope
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags import ApplicationSecurityWafCustomRuleTags
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags_category import (
    ApplicationSecurityWafCustomRuleTagsCategory,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_type import ApplicationSecurityWafCustomRuleType

body = ApplicationSecurityWafCustomRuleCreateRequest(
    data=ApplicationSecurityWafCustomRuleCreateData(
        attributes=ApplicationSecurityWafCustomRuleCreateAttributes(
            action=ApplicationSecurityWafCustomRuleAction(
                action=ApplicationSecurityWafCustomRuleActionAction.BLOCK_REQUEST,
                parameters=ApplicationSecurityWafCustomRuleActionParameters(
                    location="/blocking",
                    status_code=403,
                ),
            ),
            blocking=False,
            conditions=[
                ApplicationSecurityWafCustomRuleCondition(
                    operator=ApplicationSecurityWafCustomRuleConditionOperator.MATCH_REGEX,
                    parameters=ApplicationSecurityWafCustomRuleConditionParameters(
                        data="blocked_users",
                        inputs=[
                            ApplicationSecurityWafCustomRuleConditionInput(
                                address=ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_DB_STATEMENT,
                                key_path=[],
                            ),
                        ],
                        list=[],
                        options=ApplicationSecurityWafCustomRuleConditionOptions(
                            case_sensitive=False,
                            min_length=0,
                        ),
                        regex="path.*",
                        value="custom_tag",
                    ),
                ),
            ],
            enabled=False,
            name="Block request from a bad useragent",
            path_glob="/api/search/*",
            scope=[
                ApplicationSecurityWafCustomRuleScope(
                    env="prod",
                    service="billing-service",
                ),
            ],
            tags=ApplicationSecurityWafCustomRuleTags(
                category=ApplicationSecurityWafCustomRuleTagsCategory.BUSINESS_LOGIC,
                type="users.login.success",
            ),
        ),
        type=ApplicationSecurityWafCustomRuleType.CUSTOM_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.create_application_security_waf_custom_rule(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a WAF custom rule returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new

body = DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleCreateRequest.new({
  data: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleCreateData.new({
    attributes: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleCreateAttributes.new({
      action: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleAction.new({
        action: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleActionAction::BLOCK_REQUEST,
        parameters: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleActionParameters.new({
          location: "/blocking",
          status_code: 403,
        }),
      }),
      blocking: false,
      conditions: [
        DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleCondition.new({
          operator: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionOperator::MATCH_REGEX,
          parameters: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionParameters.new({
            data: "blocked_users",
            inputs: [
              DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionInput.new({
                address: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionInputAddress::SERVER_DB_STATEMENT,
                key_path: [],
              }),
            ],
            list: [],
            options: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionOptions.new({
              case_sensitive: false,
              min_length: 0,
            }),
            regex: "path.*",
            value: "custom_tag",
          }),
        }),
      ],
      enabled: false,
      name: "Block request from a bad useragent",
      path_glob: "/api/search/*",
      scope: [
        DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleScope.new({
          env: "prod",
          service: "billing-service",
        }),
      ],
      tags: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleTags.new({
        category: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleTagsCategory::BUSINESS_LOGIC,
        type: "users.login.success",
      }),
    }),
    type: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleType::CUSTOM_RULE,
  }),
})
p api_instance.create_application_security_waf_custom_rule(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Create a WAF custom rule returns "Created" response

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
	body := datadogV2.ApplicationSecurityWafCustomRuleCreateRequest{
		Data: datadogV2.ApplicationSecurityWafCustomRuleCreateData{
			Attributes: datadogV2.ApplicationSecurityWafCustomRuleCreateAttributes{
				Action: &datadogV2.ApplicationSecurityWafCustomRuleAction{
					Action: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULEACTIONACTION_BLOCK_REQUEST.Ptr(),
					Parameters: &datadogV2.ApplicationSecurityWafCustomRuleActionParameters{
						Location:   datadog.PtrString("/blocking"),
						StatusCode: datadog.PtrInt64(403),
					},
				},
				Blocking: false,
				Conditions: []datadogV2.ApplicationSecurityWafCustomRuleCondition{
					{
						Operator: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULECONDITIONOPERATOR_MATCH_REGEX,
						Parameters: datadogV2.ApplicationSecurityWafCustomRuleConditionParameters{
							Data: datadog.PtrString("blocked_users"),
							Inputs: []datadogV2.ApplicationSecurityWafCustomRuleConditionInput{
								{
									Address: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULECONDITIONINPUTADDRESS_SERVER_DB_STATEMENT,
									KeyPath: []string{},
								},
							},
							List: []string{},
							Options: &datadogV2.ApplicationSecurityWafCustomRuleConditionOptions{
								CaseSensitive: datadog.PtrBool(false),
								MinLength:     datadog.PtrInt64(0),
							},
							Regex: datadog.PtrString("path.*"),
							Value: datadog.PtrString("custom_tag"),
						},
					},
				},
				Enabled:  false,
				Name:     "Block request from a bad useragent",
				PathGlob: datadog.PtrString("/api/search/*"),
				Scope: []datadogV2.ApplicationSecurityWafCustomRuleScope{
					{
						Env:     "prod",
						Service: "billing-service",
					},
				},
				Tags: datadogV2.ApplicationSecurityWafCustomRuleTags{
					Category: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULETAGSCATEGORY_BUSINESS_LOGIC,
					Type:     "users.login.success",
				},
			},
			Type: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULETYPE_CUSTOM_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.CreateApplicationSecurityWafCustomRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.CreateApplicationSecurityWafCustomRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.CreateApplicationSecurityWafCustomRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a WAF custom rule returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleAction;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleActionAction;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleActionParameters;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleCondition;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionInput;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionInputAddress;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionOperator;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionOptions;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionParameters;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleCreateAttributes;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleCreateData;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleCreateRequest;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleResponse;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleScope;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleTags;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleTagsCategory;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    ApplicationSecurityWafCustomRuleCreateRequest body =
        new ApplicationSecurityWafCustomRuleCreateRequest()
            .data(
                new ApplicationSecurityWafCustomRuleCreateData()
                    .attributes(
                        new ApplicationSecurityWafCustomRuleCreateAttributes()
                            .action(
                                new ApplicationSecurityWafCustomRuleAction()
                                    .action(
                                        ApplicationSecurityWafCustomRuleActionAction.BLOCK_REQUEST)
                                    .parameters(
                                        new ApplicationSecurityWafCustomRuleActionParameters()
                                            .location("/blocking")
                                            .statusCode(403L)))
                            .blocking(false)
                            .conditions(
                                Collections.singletonList(
                                    new ApplicationSecurityWafCustomRuleCondition()
                                        .operator(
                                            ApplicationSecurityWafCustomRuleConditionOperator
                                                .MATCH_REGEX)
                                        .parameters(
                                            new ApplicationSecurityWafCustomRuleConditionParameters()
                                                .data("blocked_users")
                                                .inputs(
                                                    Collections.singletonList(
                                                        new ApplicationSecurityWafCustomRuleConditionInput()
                                                            .address(
                                                                ApplicationSecurityWafCustomRuleConditionInputAddress
                                                                    .SERVER_DB_STATEMENT)))
                                                .options(
                                                    new ApplicationSecurityWafCustomRuleConditionOptions()
                                                        .caseSensitive(false)
                                                        .minLength(0L))
                                                .regex("path.*")
                                                .value("custom_tag"))))
                            .enabled(false)
                            .name("Block request from a bad useragent")
                            .pathGlob("/api/search/*")
                            .scope(
                                Collections.singletonList(
                                    new ApplicationSecurityWafCustomRuleScope()
                                        .env("prod")
                                        .service("billing-service")))
                            .tags(
                                new ApplicationSecurityWafCustomRuleTags()
                                    .category(
                                        ApplicationSecurityWafCustomRuleTagsCategory.BUSINESS_LOGIC)
                                    .type("users.login.success")))
                    .type(ApplicationSecurityWafCustomRuleType.CUSTOM_RULE));

    try {
      ApplicationSecurityWafCustomRuleResponse result =
          apiInstance.createApplicationSecurityWafCustomRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ApplicationSecurityApi#createApplicationSecurityWafCustomRule");
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
// Create a WAF custom rule returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleAction;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleActionAction;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleActionParameters;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleCondition;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionInput;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionInputAddress;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionOperator;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionOptions;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionParameters;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleCreateAttributes;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleCreateData;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleCreateRequest;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleScope;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleTags;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleTagsCategory;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleType;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body =
        ApplicationSecurityWafCustomRuleCreateRequest::new(
            ApplicationSecurityWafCustomRuleCreateData::new(
                ApplicationSecurityWafCustomRuleCreateAttributes::new(
                    false,
                    vec![
                        ApplicationSecurityWafCustomRuleCondition::new(
                            ApplicationSecurityWafCustomRuleConditionOperator::MATCH_REGEX,
                            ApplicationSecurityWafCustomRuleConditionParameters::new(
                                vec![
                                    ApplicationSecurityWafCustomRuleConditionInput::new(
                                        ApplicationSecurityWafCustomRuleConditionInputAddress::SERVER_DB_STATEMENT,
                                    ).key_path(vec![])
                                ],
                            )
                                .data("blocked_users".to_string())
                                .list(vec![])
                                .options(
                                    ApplicationSecurityWafCustomRuleConditionOptions::new()
                                        .case_sensitive(false)
                                        .min_length(0),
                                )
                                .regex("path.*".to_string())
                                .value("custom_tag".to_string()),
                        )
                    ],
                    false,
                    "Block request from a bad useragent".to_string(),
                    ApplicationSecurityWafCustomRuleTags::new(
                        ApplicationSecurityWafCustomRuleTagsCategory::BUSINESS_LOGIC,
                        "users.login.success".to_string(),
                    ).additional_properties(BTreeMap::from([])),
                )
                    .action(
                        ApplicationSecurityWafCustomRuleAction::new()
                            .action(ApplicationSecurityWafCustomRuleActionAction::BLOCK_REQUEST)
                            .parameters(
                                ApplicationSecurityWafCustomRuleActionParameters::new()
                                    .location("/blocking".to_string())
                                    .status_code(403),
                            ),
                    )
                    .path_glob("/api/search/*".to_string())
                    .scope(
                        vec![
                            ApplicationSecurityWafCustomRuleScope::new(
                                "prod".to_string(),
                                "billing-service".to_string(),
                            )
                        ],
                    ),
                ApplicationSecurityWafCustomRuleType::CUSTOM_RULE,
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api.create_application_security_waf_custom_rule(body).await;
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
 * Create a WAF custom rule returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

const params: v2.ApplicationSecurityApiCreateApplicationSecurityWafCustomRuleRequest =
  {
    body: {
      data: {
        attributes: {
          action: {
            action: "block_request",
            parameters: {
              location: "/blocking",
              statusCode: 403,
            },
          },
          blocking: false,
          conditions: [
            {
              operator: "match_regex",
              parameters: {
                data: "blocked_users",
                inputs: [
                  {
                    address: "server.db.statement",
                    keyPath: [],
                  },
                ],
                list: [],
                options: {
                  caseSensitive: false,
                  minLength: 0,
                },
                regex: "path.*",
                value: "custom_tag",
              },
            },
          ],
          enabled: false,
          name: "Block request from a bad useragent",
          pathGlob: "/api/search/*",
          scope: [
            {
              env: "prod",
              service: "billing-service",
            },
          ],
          tags: {
            category: "business_logic",
            type: "users.login.success",
          },
        },
        type: "custom_rule",
      },
    },
  };

apiInstance
  .createApplicationSecurityWafCustomRule(params)
  .then((data: v2.ApplicationSecurityWafCustomRuleResponse) => {
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

## List all WAF custom rules{% #list-all-waf-custom-rules %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/custom_rules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/custom_rules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules |

### Overview

Retrieve a list of WAF custom rule.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a list of WAF custom rules.

| Parent field | Field                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | [object]  | The WAF custom rule data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| data         | attributes                   | object    | A WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| attributes   | action                       | object    | The definition of `ApplicationSecurityWafCustomRuleAction` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| action       | action                       | enum      | Override the default action to take when the WAF custom rule would block. Allowed enum values: `redirect_request,block_request`                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| action       | parameters                   | object    | The definition of `ApplicationSecurityWafCustomRuleActionParameters` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | location                     | string    | The location to redirect to when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| parameters   | status_code                  | int64     | The status code to return when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes   | blocking [*required*]   | boolean   | Indicates whether the WAF custom rule will block the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | conditions [*required*] | [object]  | Conditions for which the WAF Custom Rule will triggers, all conditions needs to match in order for the WAF rule to trigger.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| conditions   | operator [*required*]   | enum      | Operator to use for the WAF Condition. Allowed enum values: `match_regex,!match_regex,phrase_match,!phrase_match,is_xss,is_sqli,exact_match,!exact_match,ip_match,!ip_match,capture_data`                                                                                                                                                                                                                                                                                                                                                                                           |
| conditions   | parameters [*required*] | object    | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| parameters   | data                         | string    | Identifier of a list of data from the denylist. Can only be used as substitution from the list parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parameters   | inputs [*required*]     | [object]  | List of inputs on which at least one should match with the given operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| inputs       | address [*required*]    | enum      | Input from the request on which the condition should apply. Allowed enum values: `server.db.statement,server.io.fs.file,server.io.net.url,server.sys.shell.cmd,server.request.method,server.request.uri.raw,server.request.path_params,server.request.query,server.request.headers.no_cookies,server.request.cookies,server.request.trailers,server.request.body,server.response.status,server.response.headers.no_cookies,server.response.trailers,grpc.server.request.metadata,grpc.server.request.message,grpc.server.method,graphql.server.all_resolvers,usr.id,http.client_ip` |
| inputs       | key_path                     | [string]  | Specific path for the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | list                         | [string]  | List of value to use with the condition. Only used with the phrase_match, !phrase_match, exact_match and !exact_match operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| parameters   | options                      | object    | Options for the operator of this condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| options      | case_sensitive               | boolean   | Evaluate the value as case sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options      | min_length                   | int64     | Only evaluate this condition if the value has a minimum amount of characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| parameters   | regex                        | string    | Regex to use with the condition. Only used with match_regex and !match_regex operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| parameters   | value                        | string    | Store the captured value in the specified tag name. Only used with the capture_data operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | enabled [*required*]    | boolean   | Indicates whether the WAF custom rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes   | metadata                     | object    | Metadata associated with the WAF Custom Rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| metadata     | added_at                     | date-time | The date and time the WAF custom rule was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| metadata     | added_by                     | string    | The handle of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | added_by_name                | string    | The name of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| metadata     | modified_at                  | date-time | The date and time the WAF custom rule was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | modified_by                  | string    | The handle of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| metadata     | modified_by_name             | string    | The name of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | name [*required*]       | string    | The Name of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| attributes   | path_glob                    | string    | The path glob for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes   | scope                        | [object]  | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| scope        | env [*required*]        | string    | The environment scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scope        | service [*required*]    | string    | The service scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | tags [*required*]       | object    | Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security activity field associated with the traces.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags         | category [*required*]   | enum      | The category of the WAF Rule, can be either `business_logic`, `attack_attempt` or `security_response`. Allowed enum values: `attack_attempt,business_logic,security_response`                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags         | type [*required*]       | string    | The type of the WAF rule, associated with the category will form the security activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| data         | id                           | string    | The ID of the custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| data         | type                         | enum      | The type of the resource. The value should always be `custom_rule`. Allowed enum values: `custom_rule`                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "action": {
          "action": "block_request",
          "parameters": {
            "location": "/blocking",
            "status_code": 403
          }
        },
        "blocking": false,
        "conditions": [
          {
            "operator": "match_regex",
            "parameters": {
              "data": "blocked_users",
              "inputs": [
                {
                  "address": "server.db.statement",
                  "key_path": []
                }
              ],
              "list": [],
              "options": {
                "case_sensitive": false,
                "min_length": "integer"
              },
              "regex": "path.*",
              "value": "custom_tag"
            }
          }
        ],
        "enabled": false,
        "metadata": {
          "added_at": "2021-01-01T00:00:00Z",
          "added_by": "john.doe@datadoghq.com",
          "added_by_name": "John Doe",
          "modified_at": "2021-01-01T00:00:00Z",
          "modified_by": "john.doe@datadoghq.com",
          "modified_by_name": "John Doe"
        },
        "name": "Block request from bad useragent",
        "path_glob": "/api/search/*",
        "scope": [
          {
            "env": "prod",
            "service": "billing-service"
          }
        ],
        "tags": {
          "category": "business_logic",
          "type": "users.login.success"
        }
      },
      "id": "2857c47d-1e3a-4300-8b2f-dc24089c084b",
      "type": "custom_rule"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List all WAF custom rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.list_application_security_waf_custom_rules()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List all WAF custom rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new
p api_instance.list_application_security_waf_custom_rules()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List all WAF custom rules returns "OK" response

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
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.ListApplicationSecurityWAFCustomRules(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.ListApplicationSecurityWAFCustomRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.ListApplicationSecurityWAFCustomRules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List all WAF custom rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    try {
      ApplicationSecurityWafCustomRuleListResponse result =
          apiInstance.listApplicationSecurityWAFCustomRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ApplicationSecurityApi#listApplicationSecurityWAFCustomRules");
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
// List all WAF custom rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api.list_application_security_waf_custom_rules().await;
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
 * List all WAF custom rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

apiInstance
  .listApplicationSecurityWAFCustomRules()
  .then((data: v2.ApplicationSecurityWafCustomRuleListResponse) => {
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

## Update a WAF Custom Rule{% #update-a-waf-custom-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |

### Overview

Update a specific WAF custom Rule. Returns the Custom Rule object when the request is successful.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| custom_rule_id [*required*] | string | The ID of the custom rule. |

### Request

#### Body Data (required)

New definition of the WAF Custom Rule.

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Object for a single WAF Custom Rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| data         | attributes [*required*] | object   | Update a WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| attributes   | action                       | object   | The definition of `ApplicationSecurityWafCustomRuleAction` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| action       | action                       | enum     | Override the default action to take when the WAF custom rule would block. Allowed enum values: `redirect_request,block_request`                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| action       | parameters                   | object   | The definition of `ApplicationSecurityWafCustomRuleActionParameters` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | location                     | string   | The location to redirect to when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| parameters   | status_code                  | int64    | The status code to return when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes   | blocking [*required*]   | boolean  | Indicates whether the WAF custom rule will block the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | conditions [*required*] | [object] | Conditions for which the WAF Custom Rule will triggers, all conditions needs to match in order for the WAF rule to trigger.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| conditions   | operator [*required*]   | enum     | Operator to use for the WAF Condition. Allowed enum values: `match_regex,!match_regex,phrase_match,!phrase_match,is_xss,is_sqli,exact_match,!exact_match,ip_match,!ip_match,capture_data`                                                                                                                                                                                                                                                                                                                                                                                           |
| conditions   | parameters [*required*] | object   | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| parameters   | data                         | string   | Identifier of a list of data from the denylist. Can only be used as substitution from the list parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parameters   | inputs [*required*]     | [object] | List of inputs on which at least one should match with the given operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| inputs       | address [*required*]    | enum     | Input from the request on which the condition should apply. Allowed enum values: `server.db.statement,server.io.fs.file,server.io.net.url,server.sys.shell.cmd,server.request.method,server.request.uri.raw,server.request.path_params,server.request.query,server.request.headers.no_cookies,server.request.cookies,server.request.trailers,server.request.body,server.response.status,server.response.headers.no_cookies,server.response.trailers,grpc.server.request.metadata,grpc.server.request.message,grpc.server.method,graphql.server.all_resolvers,usr.id,http.client_ip` |
| inputs       | key_path                     | [string] | Specific path for the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | list                         | [string] | List of value to use with the condition. Only used with the phrase_match, !phrase_match, exact_match and !exact_match operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| parameters   | options                      | object   | Options for the operator of this condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| options      | case_sensitive               | boolean  | Evaluate the value as case sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options      | min_length                   | int64    | Only evaluate this condition if the value has a minimum amount of characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| parameters   | regex                        | string   | Regex to use with the condition. Only used with match_regex and !match_regex operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| parameters   | value                        | string   | Store the captured value in the specified tag name. Only used with the capture_data operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | enabled [*required*]    | boolean  | Indicates whether the WAF custom rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes   | name [*required*]       | string   | The Name of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| attributes   | path_glob                    | string   | The path glob for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes   | scope                        | [object] | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| scope        | env [*required*]        | string   | The environment scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scope        | service [*required*]    | string   | The service scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | tags [*required*]       | object   | Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security activity field associated with the traces.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags         | category [*required*]   | enum     | The category of the WAF Rule, can be either `business_logic`, `attack_attempt` or `security_response`. Allowed enum values: `attack_attempt,business_logic,security_response`                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags         | type [*required*]       | string   | The type of the WAF rule, associated with the category will form the security activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| data         | type [*required*]       | enum     | The type of the resource. The value should always be `custom_rule`. Allowed enum values: `custom_rule`                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "custom_rule",
    "attributes": {
      "blocking": false,
      "conditions": [
        {
          "operator": "match_regex",
          "parameters": {
            "inputs": [
              {
                "address": "server.request.query",
                "key_path": [
                  "id"
                ]
              }
            ],
            "regex": "badactor"
          }
        }
      ],
      "enabled": false,
      "name": "test",
      "path_glob": "/test",
      "scope": [
        {
          "env": "test",
          "service": "test"
        }
      ],
      "tags": {
        "category": "attack_attempt",
        "type": "test"
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object that includes a single WAF custom rule.

| Parent field | Field                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object    | Object for a single WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| data         | attributes                   | object    | A WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| attributes   | action                       | object    | The definition of `ApplicationSecurityWafCustomRuleAction` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| action       | action                       | enum      | Override the default action to take when the WAF custom rule would block. Allowed enum values: `redirect_request,block_request`                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| action       | parameters                   | object    | The definition of `ApplicationSecurityWafCustomRuleActionParameters` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | location                     | string    | The location to redirect to when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| parameters   | status_code                  | int64     | The status code to return when the WAF custom rule triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| attributes   | blocking [*required*]   | boolean   | Indicates whether the WAF custom rule will block the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | conditions [*required*] | [object]  | Conditions for which the WAF Custom Rule will triggers, all conditions needs to match in order for the WAF rule to trigger.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| conditions   | operator [*required*]   | enum      | Operator to use for the WAF Condition. Allowed enum values: `match_regex,!match_regex,phrase_match,!phrase_match,is_xss,is_sqli,exact_match,!exact_match,ip_match,!ip_match,capture_data`                                                                                                                                                                                                                                                                                                                                                                                           |
| conditions   | parameters [*required*] | object    | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| parameters   | data                         | string    | Identifier of a list of data from the denylist. Can only be used as substitution from the list parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parameters   | inputs [*required*]     | [object]  | List of inputs on which at least one should match with the given operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| inputs       | address [*required*]    | enum      | Input from the request on which the condition should apply. Allowed enum values: `server.db.statement,server.io.fs.file,server.io.net.url,server.sys.shell.cmd,server.request.method,server.request.uri.raw,server.request.path_params,server.request.query,server.request.headers.no_cookies,server.request.cookies,server.request.trailers,server.request.body,server.response.status,server.response.headers.no_cookies,server.response.trailers,grpc.server.request.metadata,grpc.server.request.message,grpc.server.method,graphql.server.all_resolvers,usr.id,http.client_ip` |
| inputs       | key_path                     | [string]  | Specific path for the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parameters   | list                         | [string]  | List of value to use with the condition. Only used with the phrase_match, !phrase_match, exact_match and !exact_match operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| parameters   | options                      | object    | Options for the operator of this condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| options      | case_sensitive               | boolean   | Evaluate the value as case sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options      | min_length                   | int64     | Only evaluate this condition if the value has a minimum amount of characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| parameters   | regex                        | string    | Regex to use with the condition. Only used with match_regex and !match_regex operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| parameters   | value                        | string    | Store the captured value in the specified tag name. Only used with the capture_data operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| attributes   | enabled [*required*]    | boolean   | Indicates whether the WAF custom rule is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| attributes   | metadata                     | object    | Metadata associated with the WAF Custom Rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| metadata     | added_at                     | date-time | The date and time the WAF custom rule was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| metadata     | added_by                     | string    | The handle of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | added_by_name                | string    | The name of the user who created the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| metadata     | modified_at                  | date-time | The date and time the WAF custom rule was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata     | modified_by                  | string    | The handle of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| metadata     | modified_by_name             | string    | The name of the user who last updated the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | name [*required*]       | string    | The Name of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| attributes   | path_glob                    | string    | The path glob for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attributes   | scope                        | [object]  | The scope of the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| scope        | env [*required*]        | string    | The environment scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scope        | service [*required*]    | string    | The service scope for the WAF custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| attributes   | tags [*required*]       | object    | Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security activity field associated with the traces.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags         | category [*required*]   | enum      | The category of the WAF Rule, can be either `business_logic`, `attack_attempt` or `security_response`. Allowed enum values: `attack_attempt,business_logic,security_response`                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags         | type [*required*]       | string    | The type of the WAF rule, associated with the category will form the security activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| data         | id                           | string    | The ID of the custom rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| data         | type                         | enum      | The type of the resource. The value should always be `custom_rule`. Allowed enum values: `custom_rule`                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "action": {
        "action": "block_request",
        "parameters": {
          "location": "/blocking",
          "status_code": 403
        }
      },
      "blocking": false,
      "conditions": [
        {
          "operator": "match_regex",
          "parameters": {
            "data": "blocked_users",
            "inputs": [
              {
                "address": "server.db.statement",
                "key_path": []
              }
            ],
            "list": [],
            "options": {
              "case_sensitive": false,
              "min_length": "integer"
            },
            "regex": "path.*",
            "value": "custom_tag"
          }
        }
      ],
      "enabled": false,
      "metadata": {
        "added_at": "2021-01-01T00:00:00Z",
        "added_by": "john.doe@datadoghq.com",
        "added_by_name": "John Doe",
        "modified_at": "2021-01-01T00:00:00Z",
        "modified_by": "john.doe@datadoghq.com",
        "modified_by_name": "John Doe"
      },
      "name": "Block request from bad useragent",
      "path_glob": "/api/search/*",
      "scope": [
        {
          "env": "prod",
          "service": "billing-service"
        }
      ],
      "tags": {
        "category": "business_logic",
        "type": "users.login.success"
      }
    },
    "id": "2857c47d-1e3a-4300-8b2f-dc24089c084b",
    "type": "custom_rule"
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
                          \# Path parametersexport custom_rule_id="3b5-v82-ns6"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/${custom_rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "custom_rule",
    "attributes": {
      "blocking": false,
      "conditions": [
        {
          "operator": "match_regex",
          "parameters": {
            "inputs": [
              {
                "address": "server.request.query",
                "key_path": [
                  "id"
                ]
              }
            ],
            "regex": "badactor"
          }
        }
      ],
      "enabled": false,
      "name": "test",
      "path_glob": "/test",
      "scope": [
        {
          "env": "test",
          "service": "test"
        }
      ],
      "tags": {
        "category": "attack_attempt",
        "type": "test"
      }
    }
  }
}
EOF
                        
##### 

```go
// Update a WAF Custom Rule returns "OK" response

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
	// there is a valid "custom_rule" in the system
	CustomRuleDataID := os.Getenv("CUSTOM_RULE_DATA_ID")

	body := datadogV2.ApplicationSecurityWafCustomRuleUpdateRequest{
		Data: datadogV2.ApplicationSecurityWafCustomRuleUpdateData{
			Type: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULETYPE_CUSTOM_RULE,
			Attributes: datadogV2.ApplicationSecurityWafCustomRuleUpdateAttributes{
				Blocking: false,
				Conditions: []datadogV2.ApplicationSecurityWafCustomRuleCondition{
					{
						Operator: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULECONDITIONOPERATOR_MATCH_REGEX,
						Parameters: datadogV2.ApplicationSecurityWafCustomRuleConditionParameters{
							Inputs: []datadogV2.ApplicationSecurityWafCustomRuleConditionInput{
								{
									Address: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULECONDITIONINPUTADDRESS_SERVER_REQUEST_QUERY,
									KeyPath: []string{
										"id",
									},
								},
							},
							Regex: datadog.PtrString("badactor"),
						},
					},
				},
				Enabled:  false,
				Name:     "test",
				PathGlob: datadog.PtrString("/test"),
				Scope: []datadogV2.ApplicationSecurityWafCustomRuleScope{
					{
						Env:     "test",
						Service: "test",
					},
				},
				Tags: datadogV2.ApplicationSecurityWafCustomRuleTags{
					Category: datadogV2.APPLICATIONSECURITYWAFCUSTOMRULETAGSCATEGORY_ATTACK_ATTEMPT,
					Type:     "test",
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	resp, r, err := api.UpdateApplicationSecurityWafCustomRule(ctx, CustomRuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.UpdateApplicationSecurityWafCustomRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ApplicationSecurityApi.UpdateApplicationSecurityWafCustomRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a WAF Custom Rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleCondition;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionInput;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionInputAddress;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionOperator;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleConditionParameters;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleResponse;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleScope;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleTags;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleTagsCategory;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleType;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleUpdateAttributes;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleUpdateData;
import com.datadog.api.client.v2.model.ApplicationSecurityWafCustomRuleUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    // there is a valid "custom_rule" in the system
    String CUSTOM_RULE_DATA_ID = System.getenv("CUSTOM_RULE_DATA_ID");

    ApplicationSecurityWafCustomRuleUpdateRequest body =
        new ApplicationSecurityWafCustomRuleUpdateRequest()
            .data(
                new ApplicationSecurityWafCustomRuleUpdateData()
                    .type(ApplicationSecurityWafCustomRuleType.CUSTOM_RULE)
                    .attributes(
                        new ApplicationSecurityWafCustomRuleUpdateAttributes()
                            .blocking(false)
                            .conditions(
                                Collections.singletonList(
                                    new ApplicationSecurityWafCustomRuleCondition()
                                        .operator(
                                            ApplicationSecurityWafCustomRuleConditionOperator
                                                .MATCH_REGEX)
                                        .parameters(
                                            new ApplicationSecurityWafCustomRuleConditionParameters()
                                                .inputs(
                                                    Collections.singletonList(
                                                        new ApplicationSecurityWafCustomRuleConditionInput()
                                                            .address(
                                                                ApplicationSecurityWafCustomRuleConditionInputAddress
                                                                    .SERVER_REQUEST_QUERY)
                                                            .keyPath(
                                                                Collections.singletonList("id"))))
                                                .regex("badactor"))))
                            .enabled(false)
                            .name("test")
                            .pathGlob("/test")
                            .scope(
                                Collections.singletonList(
                                    new ApplicationSecurityWafCustomRuleScope()
                                        .env("test")
                                        .service("test")))
                            .tags(
                                new ApplicationSecurityWafCustomRuleTags()
                                    .category(
                                        ApplicationSecurityWafCustomRuleTagsCategory.ATTACK_ATTEMPT)
                                    .type("test"))));

    try {
      ApplicationSecurityWafCustomRuleResponse result =
          apiInstance.updateApplicationSecurityWafCustomRule(CUSTOM_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ApplicationSecurityApi#updateApplicationSecurityWafCustomRule");
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
Update a WAF Custom Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition import (
    ApplicationSecurityWafCustomRuleCondition,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input import (
    ApplicationSecurityWafCustomRuleConditionInput,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input_address import (
    ApplicationSecurityWafCustomRuleConditionInputAddress,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_operator import (
    ApplicationSecurityWafCustomRuleConditionOperator,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_parameters import (
    ApplicationSecurityWafCustomRuleConditionParameters,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_scope import ApplicationSecurityWafCustomRuleScope
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags import ApplicationSecurityWafCustomRuleTags
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags_category import (
    ApplicationSecurityWafCustomRuleTagsCategory,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_type import ApplicationSecurityWafCustomRuleType
from datadog_api_client.v2.model.application_security_waf_custom_rule_update_attributes import (
    ApplicationSecurityWafCustomRuleUpdateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_update_data import (
    ApplicationSecurityWafCustomRuleUpdateData,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_update_request import (
    ApplicationSecurityWafCustomRuleUpdateRequest,
)

# there is a valid "custom_rule" in the system
CUSTOM_RULE_DATA_ID = environ["CUSTOM_RULE_DATA_ID"]

body = ApplicationSecurityWafCustomRuleUpdateRequest(
    data=ApplicationSecurityWafCustomRuleUpdateData(
        type=ApplicationSecurityWafCustomRuleType.CUSTOM_RULE,
        attributes=ApplicationSecurityWafCustomRuleUpdateAttributes(
            blocking=False,
            conditions=[
                ApplicationSecurityWafCustomRuleCondition(
                    operator=ApplicationSecurityWafCustomRuleConditionOperator.MATCH_REGEX,
                    parameters=ApplicationSecurityWafCustomRuleConditionParameters(
                        inputs=[
                            ApplicationSecurityWafCustomRuleConditionInput(
                                address=ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_QUERY,
                                key_path=[
                                    "id",
                                ],
                            ),
                        ],
                        regex="badactor",
                    ),
                ),
            ],
            enabled=False,
            name="test",
            path_glob="/test",
            scope=[
                ApplicationSecurityWafCustomRuleScope(
                    env="test",
                    service="test",
                ),
            ],
            tags=ApplicationSecurityWafCustomRuleTags(
                category=ApplicationSecurityWafCustomRuleTagsCategory.ATTACK_ATTEMPT,
                type="test",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.update_application_security_waf_custom_rule(custom_rule_id=CUSTOM_RULE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a WAF Custom Rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new

# there is a valid "custom_rule" in the system
CUSTOM_RULE_DATA_ID = ENV["CUSTOM_RULE_DATA_ID"]

body = DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleUpdateRequest.new({
  data: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleUpdateData.new({
    type: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleType::CUSTOM_RULE,
    attributes: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleUpdateAttributes.new({
      blocking: false,
      conditions: [
        DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleCondition.new({
          operator: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionOperator::MATCH_REGEX,
          parameters: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionParameters.new({
            inputs: [
              DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionInput.new({
                address: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleConditionInputAddress::SERVER_REQUEST_QUERY,
                key_path: [
                  "id",
                ],
              }),
            ],
            regex: "badactor",
          }),
        }),
      ],
      enabled: false,
      name: "test",
      path_glob: "/test",
      scope: [
        DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleScope.new({
          env: "test",
          service: "test",
        }),
      ],
      tags: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleTags.new({
        category: DatadogAPIClient::V2::ApplicationSecurityWafCustomRuleTagsCategory::ATTACK_ATTEMPT,
        type: "test",
      }),
    }),
  }),
})
p api_instance.update_application_security_waf_custom_rule(CUSTOM_RULE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update a WAF Custom Rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleCondition;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionInput;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionInputAddress;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionOperator;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleConditionParameters;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleScope;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleTags;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleTagsCategory;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleType;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleUpdateAttributes;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleUpdateData;
use datadog_api_client::datadogV2::model::ApplicationSecurityWafCustomRuleUpdateRequest;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "custom_rule" in the system
    let custom_rule_data_id = std::env::var("CUSTOM_RULE_DATA_ID").unwrap();
    let body =
        ApplicationSecurityWafCustomRuleUpdateRequest::new(
            ApplicationSecurityWafCustomRuleUpdateData::new(
                ApplicationSecurityWafCustomRuleUpdateAttributes::new(
                    false,
                    vec![
                        ApplicationSecurityWafCustomRuleCondition::new(
                            ApplicationSecurityWafCustomRuleConditionOperator::MATCH_REGEX,
                            ApplicationSecurityWafCustomRuleConditionParameters::new(
                                vec![
                                    ApplicationSecurityWafCustomRuleConditionInput::new(
                                        ApplicationSecurityWafCustomRuleConditionInputAddress::SERVER_REQUEST_QUERY,
                                    ).key_path(vec!["id".to_string()])
                                ],
                            ).regex("badactor".to_string()),
                        )
                    ],
                    false,
                    "test".to_string(),
                    ApplicationSecurityWafCustomRuleTags::new(
                        ApplicationSecurityWafCustomRuleTagsCategory::ATTACK_ATTEMPT,
                        "test".to_string(),
                    ).additional_properties(BTreeMap::from([])),
                )
                    .path_glob("/test".to_string())
                    .scope(vec![ApplicationSecurityWafCustomRuleScope::new("test".to_string(), "test".to_string())]),
                ApplicationSecurityWafCustomRuleType::CUSTOM_RULE,
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api
        .update_application_security_waf_custom_rule(custom_rule_data_id.clone(), body)
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
 * Update a WAF Custom Rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

// there is a valid "custom_rule" in the system
const CUSTOM_RULE_DATA_ID = process.env.CUSTOM_RULE_DATA_ID as string;

const params: v2.ApplicationSecurityApiUpdateApplicationSecurityWafCustomRuleRequest =
  {
    body: {
      data: {
        type: "custom_rule",
        attributes: {
          blocking: false,
          conditions: [
            {
              operator: "match_regex",
              parameters: {
                inputs: [
                  {
                    address: "server.request.query",
                    keyPath: ["id"],
                  },
                ],
                regex: "badactor",
              },
            },
          ],
          enabled: false,
          name: "test",
          pathGlob: "/test",
          scope: [
            {
              env: "test",
              service: "test",
            },
          ],
          tags: {
            category: "attack_attempt",
            type: "test",
          },
        },
      },
    },
    customRuleId: CUSTOM_RULE_DATA_ID,
  };

apiInstance
  .updateApplicationSecurityWafCustomRule(params)
  .then((data: v2.ApplicationSecurityWafCustomRuleResponse) => {
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

## Delete a WAF Custom Rule{% #delete-a-waf-custom-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id} |

### Overview

Delete a specific WAF custom rule.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| custom_rule_id [*required*] | string | The ID of the custom rule. |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport custom_rule_id="3b5-v82-ns6"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/asm/waf/custom_rules/${custom_rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a WAF Custom Rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    api_instance.delete_application_security_waf_custom_rule(
        custom_rule_id="custom_rule_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a WAF Custom Rule returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ApplicationSecurityAPI.new
api_instance.delete_application_security_waf_custom_rule("custom_rule_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a WAF Custom Rule returns "No Content" response

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
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewApplicationSecurityApi(apiClient)
	r, err := api.DeleteApplicationSecurityWafCustomRule(ctx, "custom_rule_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationSecurityApi.DeleteApplicationSecurityWafCustomRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a WAF Custom Rule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApplicationSecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApplicationSecurityApi apiInstance = new ApplicationSecurityApi(defaultClient);

    try {
      apiInstance.deleteApplicationSecurityWafCustomRule("3b5-v82-ns6");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ApplicationSecurityApi#deleteApplicationSecurityWafCustomRule");
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
// Delete a WAF Custom Rule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_application_security::ApplicationSecurityAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ApplicationSecurityAPI::with_config(configuration);
    let resp = api
        .delete_application_security_waf_custom_rule("custom_rule_id".to_string())
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
 * Delete a WAF Custom Rule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ApplicationSecurityApi(configuration);

const params: v2.ApplicationSecurityApiDeleteApplicationSecurityWafCustomRuleRequest =
  {
    customRuleId: "custom_rule_id",
  };

apiInstance
  .deleteApplicationSecurityWafCustomRule(params)
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
