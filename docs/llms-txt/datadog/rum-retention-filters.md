# Source: https://docs.datadoghq.com/api/latest/rum-retention-filters.md

---
title: Rum Retention Filters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Rum Retention Filters
---

# Rum Retention Filters

Manage retention filters through [Manage Applications](https://app.datadoghq.com/rum/list) of RUM for your organization.

## Get all RUM retention filters{% #get-all-rum-retention-filters %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/applications/{app_id}/retention_filters      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/applications/{app_id}/retention_filters      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |

### Overview

Get the list of RUM retention filters for a RUM application.

### Arguments

#### Path Parameters

| Name                     | Type   | Description         |
| ------------------------ | ------ | ------------------- |
| app_id [*required*] | string | RUM application ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
All RUM retention filters for a RUM application.

| Parent field | Field       | Type     | Description                                                                                                      |
| ------------ | ----------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data        | [object] | A list of RUM retention filters.                                                                                 |
| data         | attributes  | object   | The object describing attributes of a RUM retention filter.                                                      |
| attributes   | enabled     | boolean  | Whether the retention filter is enabled.                                                                         |
| attributes   | event_type  | enum     | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`   |
| attributes   | name        | string   | The name of a RUM retention filter.                                                                              |
| attributes   | query       | string   | The query string for a RUM retention filter.                                                                     |
| attributes   | sample_rate | double   | The sample rate for a RUM retention filter, between 0.1 and 100.                                                 |
| data         | id          | string   | ID of retention filter in UUID.                                                                                  |
| data         | type        | enum     | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "enabled": true,
        "event_type": "session",
        "name": "Retention filter for session",
        "query": "@session.has_replay:true",
        "sample_rate": 50.5
      },
      "id": "051601eb-54a0-abc0-03f9-cc02efa18892",
      "type": "retention_filters"
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
                  \# Path parametersexport app_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${app_id}/retention_filters" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all RUM retention filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.list_retention_filters(
        app_id="1d4b9c34-7ac4-423a-91cf-9902d926e9b3",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all RUM retention filters returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumRetentionFiltersAPI.new
p api_instance.list_retention_filters("1d4b9c34-7ac4-423a-91cf-9902d926e9b3")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all RUM retention filters returns "OK" response

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
	api := datadogV2.NewRumRetentionFiltersApi(apiClient)
	resp, r, err := api.ListRetentionFilters(ctx, "1d4b9c34-7ac4-423a-91cf-9902d926e9b3")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumRetentionFiltersApi.ListRetentionFilters`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumRetentionFiltersApi.ListRetentionFilters`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all RUM retention filters returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumRetentionFiltersApi;
import com.datadog.api.client.v2.model.RumRetentionFiltersResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumRetentionFiltersApi apiInstance = new RumRetentionFiltersApi(defaultClient);

    try {
      RumRetentionFiltersResponse result =
          apiInstance.listRetentionFilters("1d4b9c34-7ac4-423a-91cf-9902d926e9b3");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumRetentionFiltersApi#listRetentionFilters");
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
// Get all RUM retention filters returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_retention_filters::RumRetentionFiltersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .list_retention_filters("1d4b9c34-7ac4-423a-91cf-9902d926e9b3".to_string())
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
 * Get all RUM retention filters returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumRetentionFiltersApi(configuration);

const params: v2.RumRetentionFiltersApiListRetentionFiltersRequest = {
  appId: "1d4b9c34-7ac4-423a-91cf-9902d926e9b3",
};

apiInstance
  .listRetentionFilters(params)
  .then((data: v2.RumRetentionFiltersResponse) => {
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

## Get a RUM retention filter{% #get-a-rum-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |

### Overview

Get a RUM retention filter for a RUM application.

### Arguments

#### Path Parameters

| Name                     | Type   | Description          |
| ------------------------ | ------ | -------------------- |
| app_id [*required*] | string | RUM application ID.  |
| rf_id [*required*]  | string | Retention filter ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The RUM retention filter object.

| Parent field | Field       | Type    | Description                                                                                                      |
| ------------ | ----------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data        | object  | The RUM retention filter.                                                                                        |
| data         | attributes  | object  | The object describing attributes of a RUM retention filter.                                                      |
| attributes   | enabled     | boolean | Whether the retention filter is enabled.                                                                         |
| attributes   | event_type  | enum    | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`   |
| attributes   | name        | string  | The name of a RUM retention filter.                                                                              |
| attributes   | query       | string  | The query string for a RUM retention filter.                                                                     |
| attributes   | sample_rate | double  | The sample rate for a RUM retention filter, between 0.1 and 100.                                                 |
| data         | id          | string  | ID of retention filter in UUID.                                                                                  |
| data         | type        | enum    | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "event_type": "session",
      "name": "Retention filter for session",
      "query": "@session.has_replay:true",
      "sample_rate": 50.5
    },
    "id": "051601eb-54a0-abc0-03f9-cc02efa18892",
    "type": "retention_filters"
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
                  \# Path parametersexport app_id="CHANGE_ME"export rf_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${app_id}/retention_filters/${rf_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a RUM retention filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.get_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
        rf_id="4b95d361-f65d-4515-9824-c9aaeba5ac2a",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a RUM retention filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumRetentionFiltersAPI.new
p api_instance.get_retention_filter("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "4b95d361-f65d-4515-9824-c9aaeba5ac2a")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a RUM retention filter returns "OK" response

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
	api := datadogV2.NewRumRetentionFiltersApi(apiClient)
	resp, r, err := api.GetRetentionFilter(ctx, "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "4b95d361-f65d-4515-9824-c9aaeba5ac2a")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumRetentionFiltersApi.GetRetentionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumRetentionFiltersApi.GetRetentionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a RUM retention filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumRetentionFiltersApi;
import com.datadog.api.client.v2.model.RumRetentionFilterResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumRetentionFiltersApi apiInstance = new RumRetentionFiltersApi(defaultClient);

    try {
      RumRetentionFilterResponse result =
          apiInstance.getRetentionFilter(
              "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "4b95d361-f65d-4515-9824-c9aaeba5ac2a");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumRetentionFiltersApi#getRetentionFilter");
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
// Get a RUM retention filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_retention_filters::RumRetentionFiltersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .get_retention_filter(
            "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690".to_string(),
            "4b95d361-f65d-4515-9824-c9aaeba5ac2a".to_string(),
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
 * Get a RUM retention filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumRetentionFiltersApi(configuration);

const params: v2.RumRetentionFiltersApiGetRetentionFilterRequest = {
  appId: "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
  rfId: "4b95d361-f65d-4515-9824-c9aaeba5ac2a",
};

apiInstance
  .getRetentionFilter(params)
  .then((data: v2.RumRetentionFilterResponse) => {
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

## Create a RUM retention filter{% #create-a-rum-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/rum/applications/{app_id}/retention_filters      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/rum/applications/{app_id}/retention_filters      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters |

### Overview

Create a RUM retention filter for a RUM application. Returns RUM retention filter objects from the request body when the request is successful.

### Arguments

#### Path Parameters

| Name                     | Type   | Description         |
| ------------------------ | ------ | ------------------- |
| app_id [*required*] | string | RUM application ID. |

### Request

#### Body Data (required)

The definition of the new RUM retention filter.

{% tab title="Model" %}

| Parent field | Field                         | Type    | Description                                                                                                      |
| ------------ | ----------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]        | object  | The new RUM retention filter properties to create.                                                               |
| data         | attributes [*required*]  | object  | The object describing attributes of a RUM retention filter to create.                                            |
| attributes   | enabled                       | boolean | Whether the retention filter is enabled.                                                                         |
| attributes   | event_type [*required*]  | enum    | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`   |
| attributes   | name [*required*]        | string  | The name of a RUM retention filter.                                                                              |
| attributes   | query                         | string  | The query string for a RUM retention filter.                                                                     |
| attributes   | sample_rate [*required*] | double  | The sample rate for a RUM retention filter, between 0.1 and 100.                                                 |
| data         | type [*required*]        | enum    | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "retention_filters",
    "attributes": {
      "name": "Test creating retention filter",
      "event_type": "session",
      "query": "custom_query",
      "sample_rate": 50,
      "enabled": true
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
The RUM retention filter object.

| Parent field | Field       | Type    | Description                                                                                                      |
| ------------ | ----------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data        | object  | The RUM retention filter.                                                                                        |
| data         | attributes  | object  | The object describing attributes of a RUM retention filter.                                                      |
| attributes   | enabled     | boolean | Whether the retention filter is enabled.                                                                         |
| attributes   | event_type  | enum    | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`   |
| attributes   | name        | string  | The name of a RUM retention filter.                                                                              |
| attributes   | query       | string  | The query string for a RUM retention filter.                                                                     |
| attributes   | sample_rate | double  | The sample rate for a RUM retention filter, between 0.1 and 100.                                                 |
| data         | id          | string  | ID of retention filter in UUID.                                                                                  |
| data         | type        | enum    | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "event_type": "session",
      "name": "Retention filter for session",
      "query": "@session.has_replay:true",
      "sample_rate": 50.5
    },
    "id": "051601eb-54a0-abc0-03f9-cc02efa18892",
    "type": "retention_filters"
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
                          \# Path parametersexport app_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${app_id}/retention_filters" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "retention_filters",
    "attributes": {
      "name": "Test creating retention filter",
      "event_type": "session",
      "query": "custom_query",
      "sample_rate": 50,
      "enabled": true
    }
  }
}
EOF
                        
##### 

```go
// Create a RUM retention filter returns "Created" response

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
	body := datadogV2.RumRetentionFilterCreateRequest{
		Data: datadogV2.RumRetentionFilterCreateData{
			Type: datadogV2.RUMRETENTIONFILTERTYPE_RETENTION_FILTERS,
			Attributes: datadogV2.RumRetentionFilterCreateAttributes{
				Name:       "Test creating retention filter",
				EventType:  datadogV2.RUMRETENTIONFILTEREVENTTYPE_SESSION,
				Query:      datadog.PtrString("custom_query"),
				SampleRate: 50,
				Enabled:    datadog.PtrBool(true),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumRetentionFiltersApi(apiClient)
	resp, r, err := api.CreateRetentionFilter(ctx, "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumRetentionFiltersApi.CreateRetentionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumRetentionFiltersApi.CreateRetentionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a RUM retention filter returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumRetentionFiltersApi;
import com.datadog.api.client.v2.model.RumRetentionFilterCreateAttributes;
import com.datadog.api.client.v2.model.RumRetentionFilterCreateData;
import com.datadog.api.client.v2.model.RumRetentionFilterCreateRequest;
import com.datadog.api.client.v2.model.RumRetentionFilterEventType;
import com.datadog.api.client.v2.model.RumRetentionFilterResponse;
import com.datadog.api.client.v2.model.RumRetentionFilterType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumRetentionFiltersApi apiInstance = new RumRetentionFiltersApi(defaultClient);

    RumRetentionFilterCreateRequest body =
        new RumRetentionFilterCreateRequest()
            .data(
                new RumRetentionFilterCreateData()
                    .type(RumRetentionFilterType.RETENTION_FILTERS)
                    .attributes(
                        new RumRetentionFilterCreateAttributes()
                            .name("Test creating retention filter")
                            .eventType(RumRetentionFilterEventType.SESSION)
                            .query("custom_query")
                            .sampleRate(50L)
                            .enabled(true)));

    try {
      RumRetentionFilterResponse result =
          apiInstance.createRetentionFilter("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumRetentionFiltersApi#createRetentionFilter");
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
Create a RUM retention filter returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_retention_filter_create_attributes import RumRetentionFilterCreateAttributes
from datadog_api_client.v2.model.rum_retention_filter_create_data import RumRetentionFilterCreateData
from datadog_api_client.v2.model.rum_retention_filter_create_request import RumRetentionFilterCreateRequest
from datadog_api_client.v2.model.rum_retention_filter_event_type import RumRetentionFilterEventType
from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType

body = RumRetentionFilterCreateRequest(
    data=RumRetentionFilterCreateData(
        type=RumRetentionFilterType.RETENTION_FILTERS,
        attributes=RumRetentionFilterCreateAttributes(
            name="Test creating retention filter",
            event_type=RumRetentionFilterEventType.SESSION,
            query="custom_query",
            sample_rate=50,
            enabled=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.create_retention_filter(app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a RUM retention filter returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumRetentionFiltersAPI.new

body = DatadogAPIClient::V2::RumRetentionFilterCreateRequest.new({
  data: DatadogAPIClient::V2::RumRetentionFilterCreateData.new({
    type: DatadogAPIClient::V2::RumRetentionFilterType::RETENTION_FILTERS,
    attributes: DatadogAPIClient::V2::RumRetentionFilterCreateAttributes.new({
      name: "Test creating retention filter",
      event_type: DatadogAPIClient::V2::RumRetentionFilterEventType::SESSION,
      query: "custom_query",
      sample_rate: 50,
      enabled: true,
    }),
  }),
})
p api_instance.create_retention_filter("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a RUM retention filter returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_retention_filters::RumRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::RumRetentionFilterCreateAttributes;
use datadog_api_client::datadogV2::model::RumRetentionFilterCreateData;
use datadog_api_client::datadogV2::model::RumRetentionFilterCreateRequest;
use datadog_api_client::datadogV2::model::RumRetentionFilterEventType;
use datadog_api_client::datadogV2::model::RumRetentionFilterType;

#[tokio::main]
async fn main() {
    let body = RumRetentionFilterCreateRequest::new(RumRetentionFilterCreateData::new(
        RumRetentionFilterCreateAttributes::new(
            RumRetentionFilterEventType::SESSION,
            "Test creating retention filter".to_string(),
            50,
        )
        .enabled(true)
        .query("custom_query".to_string()),
        RumRetentionFilterType::RETENTION_FILTERS,
    ));
    let configuration = datadog::Configuration::new();
    let api = RumRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .create_retention_filter("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690".to_string(), body)
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
 * Create a RUM retention filter returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumRetentionFiltersApi(configuration);

const params: v2.RumRetentionFiltersApiCreateRetentionFilterRequest = {
  body: {
    data: {
      type: "retention_filters",
      attributes: {
        name: "Test creating retention filter",
        eventType: "session",
        query: "custom_query",
        sampleRate: 50,
        enabled: true,
      },
    },
  },
  appId: "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
};

apiInstance
  .createRetentionFilter(params)
  .then((data: v2.RumRetentionFilterResponse) => {
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

## Update a RUM retention filter{% #update-a-rum-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |

### Overview

Update a RUM retention filter for a RUM application. Returns RUM retention filter objects from the request body when the request is successful.

### Arguments

#### Path Parameters

| Name                     | Type   | Description          |
| ------------------------ | ------ | -------------------- |
| app_id [*required*] | string | RUM application ID.  |
| rf_id [*required*]  | string | Retention filter ID. |

### Request

#### Body Data (required)

New definition of the RUM retention filter.

{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                                                      |
| ------------ | ---------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object  | The new RUM retention filter properties to update.                                                               |
| data         | attributes [*required*] | object  | The object describing attributes of a RUM retention filter to update.                                            |
| attributes   | enabled                      | boolean | Whether the retention filter is enabled.                                                                         |
| attributes   | event_type                   | enum    | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`   |
| attributes   | name                         | string  | The name of a RUM retention filter.                                                                              |
| attributes   | query                        | string  | The query string for a RUM retention filter.                                                                     |
| attributes   | sample_rate                  | double  | The sample rate for a RUM retention filter, between 0.1 and 100.                                                 |
| data         | id [*required*]         | string  | ID of retention filter in UUID.                                                                                  |
| data         | type [*required*]       | enum    | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "4b95d361-f65d-4515-9824-c9aaeba5ac2a",
    "type": "retention_filters",
    "attributes": {
      "name": "Test updating retention filter",
      "event_type": "view",
      "query": "view_query",
      "sample_rate": 100,
      "enabled": true
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Updated
{% tab title="Model" %}
The RUM retention filter object.

| Parent field | Field       | Type    | Description                                                                                                      |
| ------------ | ----------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data        | object  | The RUM retention filter.                                                                                        |
| data         | attributes  | object  | The object describing attributes of a RUM retention filter.                                                      |
| attributes   | enabled     | boolean | Whether the retention filter is enabled.                                                                         |
| attributes   | event_type  | enum    | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`   |
| attributes   | name        | string  | The name of a RUM retention filter.                                                                              |
| attributes   | query       | string  | The query string for a RUM retention filter.                                                                     |
| attributes   | sample_rate | double  | The sample rate for a RUM retention filter, between 0.1 and 100.                                                 |
| data         | id          | string  | ID of retention filter in UUID.                                                                                  |
| data         | type        | enum    | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "event_type": "session",
      "name": "Retention filter for session",
      "query": "@session.has_replay:true",
      "sample_rate": 50.5
    },
    "id": "051601eb-54a0-abc0-03f9-cc02efa18892",
    "type": "retention_filters"
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
                          \# Path parametersexport app_id="CHANGE_ME"export rf_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${app_id}/retention_filters/${rf_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "4b95d361-f65d-4515-9824-c9aaeba5ac2a",
    "type": "retention_filters",
    "attributes": {
      "name": "Test updating retention filter",
      "event_type": "view",
      "query": "view_query",
      "sample_rate": 100,
      "enabled": true
    }
  }
}
EOF
                        
##### 

```go
// Update a RUM retention filter returns "Updated" response

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
	body := datadogV2.RumRetentionFilterUpdateRequest{
		Data: datadogV2.RumRetentionFilterUpdateData{
			Id:   "4b95d361-f65d-4515-9824-c9aaeba5ac2a",
			Type: datadogV2.RUMRETENTIONFILTERTYPE_RETENTION_FILTERS,
			Attributes: datadogV2.RumRetentionFilterUpdateAttributes{
				Name:       datadog.PtrString("Test updating retention filter"),
				EventType:  datadogV2.RUMRETENTIONFILTEREVENTTYPE_VIEW.Ptr(),
				Query:      datadog.PtrString("view_query"),
				SampleRate: datadog.PtrInt64(100),
				Enabled:    datadog.PtrBool(true),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumRetentionFiltersApi(apiClient)
	resp, r, err := api.UpdateRetentionFilter(ctx, "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "4b95d361-f65d-4515-9824-c9aaeba5ac2a", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumRetentionFiltersApi.UpdateRetentionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumRetentionFiltersApi.UpdateRetentionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a RUM retention filter returns "Updated" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumRetentionFiltersApi;
import com.datadog.api.client.v2.model.RumRetentionFilterEventType;
import com.datadog.api.client.v2.model.RumRetentionFilterResponse;
import com.datadog.api.client.v2.model.RumRetentionFilterType;
import com.datadog.api.client.v2.model.RumRetentionFilterUpdateAttributes;
import com.datadog.api.client.v2.model.RumRetentionFilterUpdateData;
import com.datadog.api.client.v2.model.RumRetentionFilterUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumRetentionFiltersApi apiInstance = new RumRetentionFiltersApi(defaultClient);

    RumRetentionFilterUpdateRequest body =
        new RumRetentionFilterUpdateRequest()
            .data(
                new RumRetentionFilterUpdateData()
                    .id("4b95d361-f65d-4515-9824-c9aaeba5ac2a")
                    .type(RumRetentionFilterType.RETENTION_FILTERS)
                    .attributes(
                        new RumRetentionFilterUpdateAttributes()
                            .name("Test updating retention filter")
                            .eventType(RumRetentionFilterEventType.VIEW)
                            .query("view_query")
                            .sampleRate(100L)
                            .enabled(true)));

    try {
      RumRetentionFilterResponse result =
          apiInstance.updateRetentionFilter(
              "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "4b95d361-f65d-4515-9824-c9aaeba5ac2a", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumRetentionFiltersApi#updateRetentionFilter");
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
Update a RUM retention filter returns "Updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_retention_filter_event_type import RumRetentionFilterEventType
from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType
from datadog_api_client.v2.model.rum_retention_filter_update_attributes import RumRetentionFilterUpdateAttributes
from datadog_api_client.v2.model.rum_retention_filter_update_data import RumRetentionFilterUpdateData
from datadog_api_client.v2.model.rum_retention_filter_update_request import RumRetentionFilterUpdateRequest

body = RumRetentionFilterUpdateRequest(
    data=RumRetentionFilterUpdateData(
        id="4b95d361-f65d-4515-9824-c9aaeba5ac2a",
        type=RumRetentionFilterType.RETENTION_FILTERS,
        attributes=RumRetentionFilterUpdateAttributes(
            name="Test updating retention filter",
            event_type=RumRetentionFilterEventType.VIEW,
            query="view_query",
            sample_rate=100,
            enabled=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.update_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", rf_id="4b95d361-f65d-4515-9824-c9aaeba5ac2a", body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a RUM retention filter returns "Updated" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumRetentionFiltersAPI.new

body = DatadogAPIClient::V2::RumRetentionFilterUpdateRequest.new({
  data: DatadogAPIClient::V2::RumRetentionFilterUpdateData.new({
    id: "4b95d361-f65d-4515-9824-c9aaeba5ac2a",
    type: DatadogAPIClient::V2::RumRetentionFilterType::RETENTION_FILTERS,
    attributes: DatadogAPIClient::V2::RumRetentionFilterUpdateAttributes.new({
      name: "Test updating retention filter",
      event_type: DatadogAPIClient::V2::RumRetentionFilterEventType::VIEW,
      query: "view_query",
      sample_rate: 100,
      enabled: true,
    }),
  }),
})
p api_instance.update_retention_filter("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "4b95d361-f65d-4515-9824-c9aaeba5ac2a", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update a RUM retention filter returns "Updated" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_retention_filters::RumRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::RumRetentionFilterEventType;
use datadog_api_client::datadogV2::model::RumRetentionFilterType;
use datadog_api_client::datadogV2::model::RumRetentionFilterUpdateAttributes;
use datadog_api_client::datadogV2::model::RumRetentionFilterUpdateData;
use datadog_api_client::datadogV2::model::RumRetentionFilterUpdateRequest;

#[tokio::main]
async fn main() {
    let body = RumRetentionFilterUpdateRequest::new(RumRetentionFilterUpdateData::new(
        RumRetentionFilterUpdateAttributes::new()
            .enabled(true)
            .event_type(RumRetentionFilterEventType::VIEW)
            .name("Test updating retention filter".to_string())
            .query("view_query".to_string())
            .sample_rate(100),
        "4b95d361-f65d-4515-9824-c9aaeba5ac2a".to_string(),
        RumRetentionFilterType::RETENTION_FILTERS,
    ));
    let configuration = datadog::Configuration::new();
    let api = RumRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .update_retention_filter(
            "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690".to_string(),
            "4b95d361-f65d-4515-9824-c9aaeba5ac2a".to_string(),
            body,
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
 * Update a RUM retention filter returns "Updated" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumRetentionFiltersApi(configuration);

const params: v2.RumRetentionFiltersApiUpdateRetentionFilterRequest = {
  body: {
    data: {
      id: "4b95d361-f65d-4515-9824-c9aaeba5ac2a",
      type: "retention_filters",
      attributes: {
        name: "Test updating retention filter",
        eventType: "view",
        query: "view_query",
        sampleRate: 100,
        enabled: true,
      },
    },
  },
  appId: "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
  rfId: "4b95d361-f65d-4515-9824-c9aaeba5ac2a",
};

apiInstance
  .updateRetentionFilter(params)
  .then((data: v2.RumRetentionFilterResponse) => {
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

## Delete a RUM retention filter{% #delete-a-rum-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/rum/applications/{app_id}/retention_filters/{rf_id} |

### Overview

Delete a RUM retention filter for a RUM application.

### Arguments

#### Path Parameters

| Name                     | Type   | Description          |
| ------------------------ | ------ | -------------------- |
| app_id [*required*] | string | RUM application ID.  |
| rf_id [*required*]  | string | Retention filter ID. |

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
                  \# Path parametersexport app_id="CHANGE_ME"export rf_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${app_id}/retention_filters/${rf_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a RUM retention filter returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    api_instance.delete_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
        rf_id="fe34ee09-14cf-4976-9362-08044c0dea80",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a RUM retention filter returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumRetentionFiltersAPI.new
api_instance.delete_retention_filter("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "fe34ee09-14cf-4976-9362-08044c0dea80")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a RUM retention filter returns "No Content" response

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
	api := datadogV2.NewRumRetentionFiltersApi(apiClient)
	r, err := api.DeleteRetentionFilter(ctx, "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "fe34ee09-14cf-4976-9362-08044c0dea80")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumRetentionFiltersApi.DeleteRetentionFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a RUM retention filter returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumRetentionFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumRetentionFiltersApi apiInstance = new RumRetentionFiltersApi(defaultClient);

    try {
      apiInstance.deleteRetentionFilter(
          "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "fe34ee09-14cf-4976-9362-08044c0dea80");
    } catch (ApiException e) {
      System.err.println("Exception when calling RumRetentionFiltersApi#deleteRetentionFilter");
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
// Delete a RUM retention filter returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_retention_filters::RumRetentionFiltersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .delete_retention_filter(
            "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690".to_string(),
            "fe34ee09-14cf-4976-9362-08044c0dea80".to_string(),
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
 * Delete a RUM retention filter returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumRetentionFiltersApi(configuration);

const params: v2.RumRetentionFiltersApiDeleteRetentionFilterRequest = {
  appId: "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
  rfId: "fe34ee09-14cf-4976-9362-08044c0dea80",
};

apiInstance
  .deleteRetentionFilter(params)
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

## Order RUM retention filters{% #order-rum-retention-filters %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/rum/applications/{app_id}/relationships/retention_filters |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/rum/applications/{app_id}/relationships/retention_filters |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/rum/applications/{app_id}/relationships/retention_filters      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/rum/applications/{app_id}/relationships/retention_filters      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/rum/applications/{app_id}/relationships/retention_filters     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/rum/applications/{app_id}/relationships/retention_filters |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/rum/applications/{app_id}/relationships/retention_filters |

### Overview

Order RUM retention filters for a RUM application. Returns RUM retention filter objects without attributes from the request body when the request is successful.

### Arguments

#### Path Parameters

| Name                     | Type   | Description         |
| ------------------------ | ------ | ------------------- |
| app_id [*required*] | string | RUM application ID. |

### Request

#### Body Data (required)

New definition of the RUM retention filter.

{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                      |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data                   | [object] | A list of RUM retention filter IDs along with type.                                                              |
| data         | id [*required*]   | string   | ID of retention filter in UUID.                                                                                  |
| data         | type [*required*] | enum     | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "type": "retention_filters",
      "id": "325631eb-94c9-49c0-93f9-ab7e4fd24529"
    },
    {
      "type": "retention_filters",
      "id": "42d89430-5b80-426e-a44b-ba3b417ece25"
    },
    {
      "type": "retention_filters",
      "id": "bff0bc34-99e9-4c16-adce-f47e71948c23"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
Ordered
{% tab title="Model" %}
The list of RUM retention filter IDs along with type.

| Parent field | Field                  | Type     | Description                                                                                                      |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
|              | data                   | [object] | A list of RUM retention filter IDs along with type.                                                              |
| data         | id [*required*]   | string   | ID of retention filter in UUID.                                                                                  |
| data         | type [*required*] | enum     | The type of the resource. The value should always be retention_filters. Allowed enum values: `retention_filters` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "051601eb-54a0-abc0-03f9-cc02efa18892",
      "type": "retention_filters"
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
                          \# Path parametersexport app_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${app_id}/relationships/retention_filters" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "type": "retention_filters",
      "id": "325631eb-94c9-49c0-93f9-ab7e4fd24529"
    },
    {
      "type": "retention_filters",
      "id": "42d89430-5b80-426e-a44b-ba3b417ece25"
    },
    {
      "type": "retention_filters",
      "id": "bff0bc34-99e9-4c16-adce-f47e71948c23"
    }
  ]
}
EOF
                        
##### 

```go
// Order RUM retention filters returns "Ordered" response

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
	body := datadogV2.RumRetentionFiltersOrderRequest{
		Data: []datadogV2.RumRetentionFiltersOrderData{
			{
				Type: datadogV2.RUMRETENTIONFILTERTYPE_RETENTION_FILTERS,
				Id:   "325631eb-94c9-49c0-93f9-ab7e4fd24529",
			},
			{
				Type: datadogV2.RUMRETENTIONFILTERTYPE_RETENTION_FILTERS,
				Id:   "42d89430-5b80-426e-a44b-ba3b417ece25",
			},
			{
				Type: datadogV2.RUMRETENTIONFILTERTYPE_RETENTION_FILTERS,
				Id:   "bff0bc34-99e9-4c16-adce-f47e71948c23",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumRetentionFiltersApi(apiClient)
	resp, r, err := api.OrderRetentionFilters(ctx, "1d4b9c34-7ac4-423a-91cf-9902d926e9b3", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumRetentionFiltersApi.OrderRetentionFilters`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumRetentionFiltersApi.OrderRetentionFilters`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Order RUM retention filters returns "Ordered" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumRetentionFiltersApi;
import com.datadog.api.client.v2.model.RumRetentionFilterType;
import com.datadog.api.client.v2.model.RumRetentionFiltersOrderData;
import com.datadog.api.client.v2.model.RumRetentionFiltersOrderRequest;
import com.datadog.api.client.v2.model.RumRetentionFiltersOrderResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumRetentionFiltersApi apiInstance = new RumRetentionFiltersApi(defaultClient);

    RumRetentionFiltersOrderRequest body =
        new RumRetentionFiltersOrderRequest()
            .data(
                Arrays.asList(
                    new RumRetentionFiltersOrderData()
                        .type(RumRetentionFilterType.RETENTION_FILTERS)
                        .id("325631eb-94c9-49c0-93f9-ab7e4fd24529"),
                    new RumRetentionFiltersOrderData()
                        .type(RumRetentionFilterType.RETENTION_FILTERS)
                        .id("42d89430-5b80-426e-a44b-ba3b417ece25"),
                    new RumRetentionFiltersOrderData()
                        .type(RumRetentionFilterType.RETENTION_FILTERS)
                        .id("bff0bc34-99e9-4c16-adce-f47e71948c23")));

    try {
      RumRetentionFiltersOrderResponse result =
          apiInstance.orderRetentionFilters("1d4b9c34-7ac4-423a-91cf-9902d926e9b3", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumRetentionFiltersApi#orderRetentionFilters");
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
Order RUM retention filters returns "Ordered" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType
from datadog_api_client.v2.model.rum_retention_filters_order_data import RumRetentionFiltersOrderData
from datadog_api_client.v2.model.rum_retention_filters_order_request import RumRetentionFiltersOrderRequest

body = RumRetentionFiltersOrderRequest(
    data=[
        RumRetentionFiltersOrderData(
            type=RumRetentionFilterType.RETENTION_FILTERS,
            id="325631eb-94c9-49c0-93f9-ab7e4fd24529",
        ),
        RumRetentionFiltersOrderData(
            type=RumRetentionFilterType.RETENTION_FILTERS,
            id="42d89430-5b80-426e-a44b-ba3b417ece25",
        ),
        RumRetentionFiltersOrderData(
            type=RumRetentionFilterType.RETENTION_FILTERS,
            id="bff0bc34-99e9-4c16-adce-f47e71948c23",
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.order_retention_filters(app_id="1d4b9c34-7ac4-423a-91cf-9902d926e9b3", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Order RUM retention filters returns "Ordered" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumRetentionFiltersAPI.new

body = DatadogAPIClient::V2::RumRetentionFiltersOrderRequest.new({
  data: [
    DatadogAPIClient::V2::RumRetentionFiltersOrderData.new({
      type: DatadogAPIClient::V2::RumRetentionFilterType::RETENTION_FILTERS,
      id: "325631eb-94c9-49c0-93f9-ab7e4fd24529",
    }),
    DatadogAPIClient::V2::RumRetentionFiltersOrderData.new({
      type: DatadogAPIClient::V2::RumRetentionFilterType::RETENTION_FILTERS,
      id: "42d89430-5b80-426e-a44b-ba3b417ece25",
    }),
    DatadogAPIClient::V2::RumRetentionFiltersOrderData.new({
      type: DatadogAPIClient::V2::RumRetentionFilterType::RETENTION_FILTERS,
      id: "bff0bc34-99e9-4c16-adce-f47e71948c23",
    }),
  ],
})
p api_instance.order_retention_filters("1d4b9c34-7ac4-423a-91cf-9902d926e9b3", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Order RUM retention filters returns "Ordered" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_retention_filters::RumRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::RumRetentionFilterType;
use datadog_api_client::datadogV2::model::RumRetentionFiltersOrderData;
use datadog_api_client::datadogV2::model::RumRetentionFiltersOrderRequest;

#[tokio::main]
async fn main() {
    let body = RumRetentionFiltersOrderRequest::new().data(vec![
        RumRetentionFiltersOrderData::new(
            "325631eb-94c9-49c0-93f9-ab7e4fd24529".to_string(),
            RumRetentionFilterType::RETENTION_FILTERS,
        ),
        RumRetentionFiltersOrderData::new(
            "42d89430-5b80-426e-a44b-ba3b417ece25".to_string(),
            RumRetentionFilterType::RETENTION_FILTERS,
        ),
        RumRetentionFiltersOrderData::new(
            "bff0bc34-99e9-4c16-adce-f47e71948c23".to_string(),
            RumRetentionFilterType::RETENTION_FILTERS,
        ),
    ]);
    let configuration = datadog::Configuration::new();
    let api = RumRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .order_retention_filters("1d4b9c34-7ac4-423a-91cf-9902d926e9b3".to_string(), body)
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
 * Order RUM retention filters returns "Ordered" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumRetentionFiltersApi(configuration);

const params: v2.RumRetentionFiltersApiOrderRetentionFiltersRequest = {
  body: {
    data: [
      {
        type: "retention_filters",
        id: "325631eb-94c9-49c0-93f9-ab7e4fd24529",
      },
      {
        type: "retention_filters",
        id: "42d89430-5b80-426e-a44b-ba3b417ece25",
      },
      {
        type: "retention_filters",
        id: "bff0bc34-99e9-4c16-adce-f47e71948c23",
      },
    ],
  },
  appId: "1d4b9c34-7ac4-423a-91cf-9902d926e9b3",
};

apiInstance
  .orderRetentionFilters(params)
  .then((data: v2.RumRetentionFiltersOrderResponse) => {
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
