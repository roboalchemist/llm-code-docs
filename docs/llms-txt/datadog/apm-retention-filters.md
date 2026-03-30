# Source: https://docs.datadoghq.com/api/latest/apm-retention-filters.md

---
title: APM Retention Filters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > APM Retention Filters
---

# APM Retention Filters

Manage configuration of [APM retention filters](https://app.datadoghq.com/apm/traces/retention-filters) for your organization. You need an API and application key with Admin rights to interact with this endpoint. See [retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#retention-filters) on the Trace Retention page for more information.

## List all APM retention filters{% #list-all-apm-retention-filters %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/apm/config/retention-filters |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/apm/config/retention-filters |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/apm/config/retention-filters      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/apm/config/retention-filters      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/apm/config/retention-filters     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/apm/config/retention-filters |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters |

### Overview

Get the list of APM retention filters. This endpoint requires the `apm_retention_filter_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An ordered list of retention filters.

| Parent field | Field                        | Type     | Description                                                                                                                                         |
| ------------ | ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | [object] | A list of retention filters objects.                                                                                                                |
| data         | attributes [*required*] | object   | The attributes of the retention filter.                                                                                                             |
| attributes   | created_at                   | int64    | The creation timestamp of the retention filter.                                                                                                     |
| attributes   | created_by                   | string   | The creator of the retention filter.                                                                                                                |
| attributes   | editable                     | boolean  | Shows whether the filter can be edited.                                                                                                             |
| attributes   | enabled                      | boolean  | The status of the retention filter (Enabled/Disabled).                                                                                              |
| attributes   | execution_order              | int64    | The execution order of the retention filter.                                                                                                        |
| attributes   | filter                       | object   | The spans filter used to index spans.                                                                                                               |
| filter       | query                        | string   | The search query - following the [span search syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).                             |
| attributes   | filter_type                  | enum     | The type of retention filter. Allowed enum values: `spans-sampling-processor,spans-errors-sampling-processor,spans-appsec-sampling-processor`       |
| attributes   | modified_at                  | int64    | The modification timestamp of the retention filter.                                                                                                 |
| attributes   | modified_by                  | string   | The modifier of the retention filter.                                                                                                               |
| attributes   | name                         | string   | The name of the retention filter.                                                                                                                   |
| attributes   | rate                         | double   | Sample rate to apply to spans going through this retention filter. A value of 1.0 keeps all spans matching the query.                               |
| attributes   | trace_rate                   | double   | Sample rate to apply to traces containing spans going through this retention filter. A value of 1.0 keeps all traces with spans matching the query. |
| data         | id [*required*]         | string   | The ID of the retention filter.                                                                                                                     |
| data         | type [*required*]       | enum     | The type of the resource. Allowed enum values: `apm_retention_filter`                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "integer",
        "created_by": "string",
        "editable": true,
        "enabled": true,
        "execution_order": "integer",
        "filter": {
          "query": "@http.status_code:200 service:my-service"
        },
        "filter_type": "spans-sampling-processor",
        "modified_at": "integer",
        "modified_by": "string",
        "name": "my retention filter",
        "rate": 1,
        "trace_rate": 1
      },
      "id": "7RBOb7dLSYWI01yc3pIH8w",
      "type": "apm_retention_filter"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List all APM retention filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.list_apm_retention_filters()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List all APM retention filters returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new
p api_instance.list_apm_retention_filters()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List all APM retention filters returns "OK" response

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
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    resp, r, err := api.ListApmRetentionFilters(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.ListApmRetentionFilters`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `APMRetentionFiltersApi.ListApmRetentionFilters`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List all APM retention filters returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;
import com.datadog.api.client.v2.model.RetentionFiltersResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    try {
      RetentionFiltersResponse result = apiInstance.listApmRetentionFilters();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmRetentionFiltersApi#listApmRetentionFilters");
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
// List all APM retention filters returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api.list_apm_retention_filters().await;
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
 * List all APM retention filters returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

apiInstance
  .listApmRetentionFilters()
  .then((data: v2.RetentionFiltersResponse) => {
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

## Create a retention filter{% #create-a-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/apm/config/retention-filters |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/apm/config/retention-filters |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/apm/config/retention-filters      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/apm/config/retention-filters      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/apm/config/retention-filters     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/apm/config/retention-filters |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters |

### Overview



Create a retention filter to index spans in your organization. Returns the retention filter definition when the request is successful.

Default filters with types spans-errors-sampling-processor and spans-appsec-sampling-processor cannot be created.
This endpoint requires the `apm_retention_filter_write` permission.


### Request

#### Body Data (required)

The definition of the new retention filter.

{% tab title="Model" %}

| Parent field | Field                         | Type    | Description                                                                                                                                         |
| ------------ | ----------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]        | object  | The body of the retention filter to be created.                                                                                                     |
| data         | attributes [*required*]  | object  | The object describing the configuration of the retention filter to create/update.                                                                   |
| attributes   | enabled [*required*]     | boolean | Enable/Disable the retention filter.                                                                                                                |
| attributes   | filter [*required*]      | object  | The spans filter. Spans matching this filter will be indexed and stored.                                                                            |
| filter       | query [*required*]       | string  | The search query - following the [span search syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).                             |
| attributes   | filter_type [*required*] | enum    | The type of retention filter. The value should always be spans-sampling-processor. Allowed enum values: `spans-sampling-processor`                  |
| attributes   | name [*required*]        | string  | The name of the retention filter.                                                                                                                   |
| attributes   | rate [*required*]        | double  | Sample rate to apply to spans going through this retention filter. A value of 1.0 keeps all spans matching the query.                               |
| attributes   | trace_rate                    | double  | Sample rate to apply to traces containing spans going through this retention filter. A value of 1.0 keeps all traces with spans matching the query. |
| data         | type [*required*]        | enum    | The type of the resource. Allowed enum values: `apm_retention_filter`                                                                               |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "filter_type": "spans-sampling-processor",
      "name": "my retention filter",
      "rate": 1.0
    },
    "type": "apm_retention_filter"
  }
}
```

#####

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "filter_type": "spans-sampling-processor",
      "name": "my retention filter",
      "rate": 1.0,
      "trace_rate": 1.0
    },
    "type": "apm_retention_filter"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The retention filters definition.

| Parent field | Field                        | Type    | Description                                                                                                                                         |
| ------------ | ---------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object  | The definition of the retention filter.                                                                                                             |
| data         | attributes [*required*] | object  | The attributes of the retention filter.                                                                                                             |
| attributes   | created_at                   | int64   | The creation timestamp of the retention filter.                                                                                                     |
| attributes   | created_by                   | string  | The creator of the retention filter.                                                                                                                |
| attributes   | editable                     | boolean | Shows whether the filter can be edited.                                                                                                             |
| attributes   | enabled                      | boolean | The status of the retention filter (Enabled/Disabled).                                                                                              |
| attributes   | execution_order              | int64   | The execution order of the retention filter.                                                                                                        |
| attributes   | filter                       | object  | The spans filter used to index spans.                                                                                                               |
| filter       | query                        | string  | The search query - following the [span search syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).                             |
| attributes   | filter_type                  | enum    | The type of retention filter. The value should always be spans-sampling-processor. Allowed enum values: `spans-sampling-processor`                  |
| attributes   | modified_at                  | int64   | The modification timestamp of the retention filter.                                                                                                 |
| attributes   | modified_by                  | string  | The modifier of the retention filter.                                                                                                               |
| attributes   | name                         | string  | The name of the retention filter.                                                                                                                   |
| attributes   | rate                         | double  | Sample rate to apply to spans going through this retention filter. A value of 1.0 keeps all spans matching the query.                               |
| attributes   | trace_rate                   | double  | Sample rate to apply to traces containing spans going through this retention filter. A value of 1.0 keeps all traces with spans matching the query. |
| data         | id [*required*]         | string  | The ID of the retention filter.                                                                                                                     |
| data         | type [*required*]       | enum    | The type of the resource. Allowed enum values: `apm_retention_filter`                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "integer",
      "created_by": "string",
      "editable": true,
      "enabled": true,
      "execution_order": "integer",
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "filter_type": "spans-sampling-processor",
      "modified_at": "integer",
      "modified_by": "string",
      "name": "my retention filter",
      "rate": 1,
      "trace_rate": 1
    },
    "id": "7RBOb7dLSYWI01yc3pIH8w",
    "type": "apm_retention_filter"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": true,
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "filter_type": "spans-sampling-processor",
      "name": "my retention filter",
      "rate": 1.0
    },
    "type": "apm_retention_filter"
  }
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": true,
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "filter_type": "spans-sampling-processor",
      "name": "my retention filter",
      "rate": 1.0,
      "trace_rate": 1.0
    },
    "type": "apm_retention_filter"
  }
}
EOF

#####

```go
// Create a retention filter returns "OK" response

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
    body := datadogV2.RetentionFilterCreateRequest{
        Data: datadogV2.RetentionFilterCreateData{
            Attributes: datadogV2.RetentionFilterCreateAttributes{
                Enabled: true,
                Filter: datadogV2.SpansFilterCreate{
                    Query: "@http.status_code:200 service:my-service",
                },
                FilterType: datadogV2.RETENTIONFILTERTYPE_SPANS_SAMPLING_PROCESSOR,
                Name:       "my retention filter",
                Rate:       1.0,
            },
            Type: datadogV2.APMRETENTIONFILTERTYPE_apm_retention_filter,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    resp, r, err := api.CreateApmRetentionFilter(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.CreateApmRetentionFilter`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `APMRetentionFiltersApi.CreateApmRetentionFilter`:\n%s\n", responseContent)
}
```

#####

```go
// Create a retention filter with trace rate returns "OK" response

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
    body := datadogV2.RetentionFilterCreateRequest{
        Data: datadogV2.RetentionFilterCreateData{
            Attributes: datadogV2.RetentionFilterCreateAttributes{
                Enabled: true,
                Filter: datadogV2.SpansFilterCreate{
                    Query: "@http.status_code:200 service:my-service",
                },
                FilterType: datadogV2.RETENTIONFILTERTYPE_SPANS_SAMPLING_PROCESSOR,
                Name:       "my retention filter",
                Rate:       1.0,
                TraceRate:  datadog.PtrFloat64(1.0),
            },
            Type: datadogV2.APMRETENTIONFILTERTYPE_apm_retention_filter,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    resp, r, err := api.CreateApmRetentionFilter(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.CreateApmRetentionFilter`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `APMRetentionFiltersApi.CreateApmRetentionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a retention filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;
import com.datadog.api.client.v2.model.ApmRetentionFilterType;
import com.datadog.api.client.v2.model.RetentionFilterCreateAttributes;
import com.datadog.api.client.v2.model.RetentionFilterCreateData;
import com.datadog.api.client.v2.model.RetentionFilterCreateRequest;
import com.datadog.api.client.v2.model.RetentionFilterCreateResponse;
import com.datadog.api.client.v2.model.RetentionFilterType;
import com.datadog.api.client.v2.model.SpansFilterCreate;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    RetentionFilterCreateRequest body =
        new RetentionFilterCreateRequest()
            .data(
                new RetentionFilterCreateData()
                    .attributes(
                        new RetentionFilterCreateAttributes()
                            .enabled(true)
                            .filter(
                                new SpansFilterCreate()
                                    .query("@http.status_code:200 service:my-service"))
                            .filterType(RetentionFilterType.SPANS_SAMPLING_PROCESSOR)
                            .name("my retention filter")
                            .rate(1.0))
                    .type(ApmRetentionFilterType.apm_retention_filter));

    try {
      RetentionFilterCreateResponse result = apiInstance.createApmRetentionFilter(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmRetentionFiltersApi#createApmRetentionFilter");
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
// Create a retention filter with trace rate returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;
import com.datadog.api.client.v2.model.ApmRetentionFilterType;
import com.datadog.api.client.v2.model.RetentionFilterCreateAttributes;
import com.datadog.api.client.v2.model.RetentionFilterCreateData;
import com.datadog.api.client.v2.model.RetentionFilterCreateRequest;
import com.datadog.api.client.v2.model.RetentionFilterCreateResponse;
import com.datadog.api.client.v2.model.RetentionFilterType;
import com.datadog.api.client.v2.model.SpansFilterCreate;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    RetentionFilterCreateRequest body =
        new RetentionFilterCreateRequest()
            .data(
                new RetentionFilterCreateData()
                    .attributes(
                        new RetentionFilterCreateAttributes()
                            .enabled(true)
                            .filter(
                                new SpansFilterCreate()
                                    .query("@http.status_code:200 service:my-service"))
                            .filterType(RetentionFilterType.SPANS_SAMPLING_PROCESSOR)
                            .name("my retention filter")
                            .rate(1.0)
                            .traceRate(1.0))
                    .type(ApmRetentionFilterType.apm_retention_filter));

    try {
      RetentionFilterCreateResponse result = apiInstance.createApmRetentionFilter(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmRetentionFiltersApi#createApmRetentionFilter");
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
Create a retention filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.retention_filter_create_attributes import RetentionFilterCreateAttributes
from datadog_api_client.v2.model.retention_filter_create_data import RetentionFilterCreateData
from datadog_api_client.v2.model.retention_filter_create_request import RetentionFilterCreateRequest
from datadog_api_client.v2.model.retention_filter_type import RetentionFilterType
from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate

body = RetentionFilterCreateRequest(
    data=RetentionFilterCreateData(
        attributes=RetentionFilterCreateAttributes(
            enabled=True,
            filter=SpansFilterCreate(
                query="@http.status_code:200 service:my-service",
            ),
            filter_type=RetentionFilterType.SPANS_SAMPLING_PROCESSOR,
            name="my retention filter",
            rate=1.0,
        ),
        type=ApmRetentionFilterType.apm_retention_filter,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.create_apm_retention_filter(body=body)

    print(response)
```

#####

```python
"""
Create a retention filter with trace rate returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.retention_filter_create_attributes import RetentionFilterCreateAttributes
from datadog_api_client.v2.model.retention_filter_create_data import RetentionFilterCreateData
from datadog_api_client.v2.model.retention_filter_create_request import RetentionFilterCreateRequest
from datadog_api_client.v2.model.retention_filter_type import RetentionFilterType
from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate

body = RetentionFilterCreateRequest(
    data=RetentionFilterCreateData(
        attributes=RetentionFilterCreateAttributes(
            enabled=True,
            filter=SpansFilterCreate(
                query="@http.status_code:200 service:my-service",
            ),
            filter_type=RetentionFilterType.SPANS_SAMPLING_PROCESSOR,
            name="my retention filter",
            rate=1.0,
            trace_rate=1.0,
        ),
        type=ApmRetentionFilterType.apm_retention_filter,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.create_apm_retention_filter(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a retention filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new

body = DatadogAPIClient::V2::RetentionFilterCreateRequest.new({
  data: DatadogAPIClient::V2::RetentionFilterCreateData.new({
    attributes: DatadogAPIClient::V2::RetentionFilterCreateAttributes.new({
      enabled: true,
      filter: DatadogAPIClient::V2::SpansFilterCreate.new({
        query: "@http.status_code:200 service:my-service",
      }),
      filter_type: DatadogAPIClient::V2::RetentionFilterType::SPANS_SAMPLING_PROCESSOR,
      name: "my retention filter",
      rate: 1.0,
    }),
    type: DatadogAPIClient::V2::ApmRetentionFilterType::APM_RETENTION_FILTER,
  }),
})
p api_instance.create_apm_retention_filter(body)
```

#####

```ruby
# Create a retention filter with trace rate returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new

body = DatadogAPIClient::V2::RetentionFilterCreateRequest.new({
  data: DatadogAPIClient::V2::RetentionFilterCreateData.new({
    attributes: DatadogAPIClient::V2::RetentionFilterCreateAttributes.new({
      enabled: true,
      filter: DatadogAPIClient::V2::SpansFilterCreate.new({
        query: "@http.status_code:200 service:my-service",
      }),
      filter_type: DatadogAPIClient::V2::RetentionFilterType::SPANS_SAMPLING_PROCESSOR,
      name: "my retention filter",
      rate: 1.0,
      trace_rate: 1.0,
    }),
    type: DatadogAPIClient::V2::ApmRetentionFilterType::APM_RETENTION_FILTER,
  }),
})
p api_instance.create_apm_retention_filter(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a retention filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::ApmRetentionFilterType;
use datadog_api_client::datadogV2::model::RetentionFilterCreateAttributes;
use datadog_api_client::datadogV2::model::RetentionFilterCreateData;
use datadog_api_client::datadogV2::model::RetentionFilterCreateRequest;
use datadog_api_client::datadogV2::model::RetentionFilterType;
use datadog_api_client::datadogV2::model::SpansFilterCreate;

#[tokio::main]
async fn main() {
    let body = RetentionFilterCreateRequest::new(RetentionFilterCreateData::new(
        RetentionFilterCreateAttributes::new(
            true,
            SpansFilterCreate::new("@http.status_code:200 service:my-service".to_string()),
            RetentionFilterType::SPANS_SAMPLING_PROCESSOR,
            "my retention filter".to_string(),
            1.0,
        ),
        ApmRetentionFilterType::apm_retention_filter,
    ));
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api.create_apm_retention_filter(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create a retention filter with trace rate returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::ApmRetentionFilterType;
use datadog_api_client::datadogV2::model::RetentionFilterCreateAttributes;
use datadog_api_client::datadogV2::model::RetentionFilterCreateData;
use datadog_api_client::datadogV2::model::RetentionFilterCreateRequest;
use datadog_api_client::datadogV2::model::RetentionFilterType;
use datadog_api_client::datadogV2::model::SpansFilterCreate;

#[tokio::main]
async fn main() {
    let body = RetentionFilterCreateRequest::new(RetentionFilterCreateData::new(
        RetentionFilterCreateAttributes::new(
            true,
            SpansFilterCreate::new("@http.status_code:200 service:my-service".to_string()),
            RetentionFilterType::SPANS_SAMPLING_PROCESSOR,
            "my retention filter".to_string(),
            1.0,
        )
        .trace_rate(1.0 as f64),
        ApmRetentionFilterType::apm_retention_filter,
    ));
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api.create_apm_retention_filter(body).await;
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
 * Create a retention filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

const params: v2.APMRetentionFiltersApiCreateApmRetentionFilterRequest = {
  body: {
    data: {
      attributes: {
        enabled: true,
        filter: {
          query: "@http.status_code:200 service:my-service",
        },
        filterType: "spans-sampling-processor",
        name: "my retention filter",
        rate: 1.0,
      },
      type: "apm_retention_filter",
    },
  },
};

apiInstance
  .createApmRetentionFilter(params)
  .then((data: v2.RetentionFilterCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create a retention filter with trace rate returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

const params: v2.APMRetentionFiltersApiCreateApmRetentionFilterRequest = {
  body: {
    data: {
      attributes: {
        enabled: true,
        filter: {
          query: "@http.status_code:200 service:my-service",
        },
        filterType: "spans-sampling-processor",
        name: "my retention filter",
        rate: 1.0,
        traceRate: 1.0,
      },
      type: "apm_retention_filter",
    },
  },
};

apiInstance
  .createApmRetentionFilter(params)
  .then((data: v2.RetentionFilterCreateResponse) => {
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

## Get a given APM retention filter{% #get-a-given-apm-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/apm/config/retention-filters/{filter_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/apm/config/retention-filters/{filter_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |

### Overview

Get an APM retention filter. This endpoint requires the `apm_retention_filter_read` permission.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                     |
| --------------------------- | ------ | ------------------------------- |
| filter_id [*required*] | string | The ID of the retention filter. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The retention filters definition.

| Parent field | Field                        | Type    | Description                                                                                                                                         |
| ------------ | ---------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object  | The definition of the retention filter.                                                                                                             |
| data         | attributes [*required*] | object  | The attributes of the retention filter.                                                                                                             |
| attributes   | created_at                   | int64   | The creation timestamp of the retention filter.                                                                                                     |
| attributes   | created_by                   | string  | The creator of the retention filter.                                                                                                                |
| attributes   | editable                     | boolean | Shows whether the filter can be edited.                                                                                                             |
| attributes   | enabled                      | boolean | The status of the retention filter (Enabled/Disabled).                                                                                              |
| attributes   | execution_order              | int64   | The execution order of the retention filter.                                                                                                        |
| attributes   | filter                       | object  | The spans filter used to index spans.                                                                                                               |
| filter       | query                        | string  | The search query - following the [span search syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).                             |
| attributes   | filter_type                  | enum    | The type of retention filter. Allowed enum values: `spans-sampling-processor,spans-errors-sampling-processor,spans-appsec-sampling-processor`       |
| attributes   | modified_at                  | int64   | The modification timestamp of the retention filter.                                                                                                 |
| attributes   | modified_by                  | string  | The modifier of the retention filter.                                                                                                               |
| attributes   | name                         | string  | The name of the retention filter.                                                                                                                   |
| attributes   | rate                         | double  | Sample rate to apply to spans going through this retention filter. A value of 1.0 keeps all spans matching the query.                               |
| attributes   | trace_rate                   | double  | Sample rate to apply to traces containing spans going through this retention filter. A value of 1.0 keeps all traces with spans matching the query. |
| data         | id [*required*]         | string  | The ID of the retention filter.                                                                                                                     |
| data         | type [*required*]       | enum    | The type of the resource. Allowed enum values: `apm_retention_filter`                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "integer",
      "created_by": "string",
      "editable": true,
      "enabled": true,
      "execution_order": "integer",
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "filter_type": "spans-sampling-processor",
      "modified_at": "integer",
      "modified_by": "string",
      "name": "my retention filter",
      "rate": 1,
      "trace_rate": 1
    },
    "id": "7RBOb7dLSYWI01yc3pIH8w",
    "type": "apm_retention_filter"
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
                  \# Path parametersexport filter_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters/${filter_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a given APM retention filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = environ["RETENTION_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.get_apm_retention_filter(
        filter_id=RETENTION_FILTER_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a given APM retention filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = ENV["RETENTION_FILTER_DATA_ID"]
p api_instance.get_apm_retention_filter(RETENTION_FILTER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a given APM retention filter returns "OK" response

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
    // there is a valid "retention_filter" in the system
    RetentionFilterDataID := os.Getenv("RETENTION_FILTER_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    resp, r, err := api.GetApmRetentionFilter(ctx, RetentionFilterDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.GetApmRetentionFilter`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `APMRetentionFiltersApi.GetApmRetentionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a given APM retention filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;
import com.datadog.api.client.v2.model.RetentionFilterResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    // there is a valid "retention_filter" in the system
    String RETENTION_FILTER_DATA_ID = System.getenv("RETENTION_FILTER_DATA_ID");

    try {
      RetentionFilterResponse result = apiInstance.getApmRetentionFilter(RETENTION_FILTER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmRetentionFiltersApi#getApmRetentionFilter");
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
// Get a given APM retention filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;

#[tokio::main]
async fn main() {
    // there is a valid "retention_filter" in the system
    let retention_filter_data_id = std::env::var("RETENTION_FILTER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .get_apm_retention_filter(retention_filter_data_id.clone())
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
 * Get a given APM retention filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

// there is a valid "retention_filter" in the system
const RETENTION_FILTER_DATA_ID = process.env.RETENTION_FILTER_DATA_ID as string;

const params: v2.APMRetentionFiltersApiGetApmRetentionFilterRequest = {
  filterId: RETENTION_FILTER_DATA_ID,
};

apiInstance
  .getApmRetentionFilter(params)
  .then((data: v2.RetentionFilterResponse) => {
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

## Update a retention filter{% #update-a-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/apm/config/retention-filters/{filter_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/apm/config/retention-filters/{filter_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |

### Overview



Update a retention filter from your organization.

Default filters (filters with types spans-errors-sampling-processor and spans-appsec-sampling-processor) cannot be renamed or removed.
This endpoint requires the `apm_retention_filter_write` permission.


### Arguments

#### Path Parameters

| Name                        | Type   | Description                     |
| --------------------------- | ------ | ------------------------------- |
| filter_id [*required*] | string | The ID of the retention filter. |

### Request

#### Body Data (required)

The updated definition of the retention filter.

{% tab title="Model" %}

| Parent field | Field                         | Type    | Description                                                                                                                                         |
| ------------ | ----------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]        | object  | The body of the retention filter to be updated.                                                                                                     |
| data         | attributes [*required*]  | object  | The object describing the configuration of the retention filter to create/update.                                                                   |
| attributes   | enabled [*required*]     | boolean | Enable/Disable the retention filter.                                                                                                                |
| attributes   | filter [*required*]      | object  | The spans filter. Spans matching this filter will be indexed and stored.                                                                            |
| filter       | query [*required*]       | string  | The search query - following the [span search syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).                             |
| attributes   | filter_type [*required*] | enum    | The type of retention filter. Allowed enum values: `spans-sampling-processor,spans-errors-sampling-processor,spans-appsec-sampling-processor`       |
| attributes   | name [*required*]        | string  | The name of the retention filter.                                                                                                                   |
| attributes   | rate [*required*]        | double  | Sample rate to apply to spans going through this retention filter. A value of 1.0 keeps all spans matching the query.                               |
| attributes   | trace_rate                    | double  | Sample rate to apply to traces containing spans going through this retention filter. A value of 1.0 keeps all traces with spans matching the query. |
| data         | id [*required*]          | string  | The ID of the retention filter.                                                                                                                     |
| data         | type [*required*]        | enum    | The type of the resource. Allowed enum values: `apm_retention_filter`                                                                               |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "name": "test",
      "rate": 0.9,
      "filter": {
        "query": "@_top_level:1 test:service-demo"
      },
      "enabled": true,
      "filter_type": "spans-sampling-processor"
    },
    "id": "test-id",
    "type": "apm_retention_filter"
  }
}
```

#####

```json
{
  "data": {
    "attributes": {
      "name": "test",
      "rate": 0.9,
      "trace_rate": 1.0,
      "filter": {
        "query": "@_top_level:1 test:service-demo"
      },
      "enabled": true,
      "filter_type": "spans-sampling-processor"
    },
    "id": "test-id",
    "type": "apm_retention_filter"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The retention filters definition.

| Parent field | Field                        | Type    | Description                                                                                                                                         |
| ------------ | ---------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object  | The definition of the retention filter.                                                                                                             |
| data         | attributes [*required*] | object  | The attributes of the retention filter.                                                                                                             |
| attributes   | created_at                   | int64   | The creation timestamp of the retention filter.                                                                                                     |
| attributes   | created_by                   | string  | The creator of the retention filter.                                                                                                                |
| attributes   | editable                     | boolean | Shows whether the filter can be edited.                                                                                                             |
| attributes   | enabled                      | boolean | The status of the retention filter (Enabled/Disabled).                                                                                              |
| attributes   | execution_order              | int64   | The execution order of the retention filter.                                                                                                        |
| attributes   | filter                       | object  | The spans filter used to index spans.                                                                                                               |
| filter       | query                        | string  | The search query - following the [span search syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).                             |
| attributes   | filter_type                  | enum    | The type of retention filter. Allowed enum values: `spans-sampling-processor,spans-errors-sampling-processor,spans-appsec-sampling-processor`       |
| attributes   | modified_at                  | int64   | The modification timestamp of the retention filter.                                                                                                 |
| attributes   | modified_by                  | string  | The modifier of the retention filter.                                                                                                               |
| attributes   | name                         | string  | The name of the retention filter.                                                                                                                   |
| attributes   | rate                         | double  | Sample rate to apply to spans going through this retention filter. A value of 1.0 keeps all spans matching the query.                               |
| attributes   | trace_rate                   | double  | Sample rate to apply to traces containing spans going through this retention filter. A value of 1.0 keeps all traces with spans matching the query. |
| data         | id [*required*]         | string  | The ID of the retention filter.                                                                                                                     |
| data         | type [*required*]       | enum    | The type of the resource. Allowed enum values: `apm_retention_filter`                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "integer",
      "created_by": "string",
      "editable": true,
      "enabled": true,
      "execution_order": "integer",
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "filter_type": "spans-sampling-processor",
      "modified_at": "integer",
      "modified_by": "string",
      "name": "my retention filter",
      "rate": 1,
      "trace_rate": 1
    },
    "id": "7RBOb7dLSYWI01yc3pIH8w",
    "type": "apm_retention_filter"
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
                          \# Path parametersexport filter_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters/${filter_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "test",
      "rate": 0.9,
      "filter": {
        "query": "@_top_level:1 test:service-demo"
      },
      "enabled": true,
      "filter_type": "spans-sampling-processor"
    },
    "id": "test-id",
    "type": "apm_retention_filter"
  }
}
EOF

#####
                          \# Path parametersexport filter_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters/${filter_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "test",
      "rate": 0.9,
      "trace_rate": 1.0,
      "filter": {
        "query": "@_top_level:1 test:service-demo"
      },
      "enabled": true,
      "filter_type": "spans-sampling-processor"
    },
    "id": "test-id",
    "type": "apm_retention_filter"
  }
}
EOF

#####

```go
// Update a retention filter returns "OK" response

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
    // there is a valid "retention_filter" in the system
    RetentionFilterDataID := os.Getenv("RETENTION_FILTER_DATA_ID")

    body := datadogV2.RetentionFilterUpdateRequest{
        Data: datadogV2.RetentionFilterUpdateData{
            Attributes: datadogV2.RetentionFilterUpdateAttributes{
                Name: "test",
                Rate: 0.9,
                Filter: datadogV2.SpansFilterCreate{
                    Query: "@_top_level:1 test:service-demo",
                },
                Enabled:    true,
                FilterType: datadogV2.RETENTIONFILTERALLTYPE_SPANS_SAMPLING_PROCESSOR,
            },
            Id:   "test-id",
            Type: datadogV2.APMRETENTIONFILTERTYPE_apm_retention_filter,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    resp, r, err := api.UpdateApmRetentionFilter(ctx, RetentionFilterDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.UpdateApmRetentionFilter`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `APMRetentionFiltersApi.UpdateApmRetentionFilter`:\n%s\n", responseContent)
}
```

#####

```go
// Update a retention filter with trace rate returns "OK" response

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
    // there is a valid "retention_filter" in the system
    RetentionFilterDataID := os.Getenv("RETENTION_FILTER_DATA_ID")

    body := datadogV2.RetentionFilterUpdateRequest{
        Data: datadogV2.RetentionFilterUpdateData{
            Attributes: datadogV2.RetentionFilterUpdateAttributes{
                Name:      "test",
                Rate:      0.9,
                TraceRate: datadog.PtrFloat64(1.0),
                Filter: datadogV2.SpansFilterCreate{
                    Query: "@_top_level:1 test:service-demo",
                },
                Enabled:    true,
                FilterType: datadogV2.RETENTIONFILTERALLTYPE_SPANS_SAMPLING_PROCESSOR,
            },
            Id:   "test-id",
            Type: datadogV2.APMRETENTIONFILTERTYPE_apm_retention_filter,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    resp, r, err := api.UpdateApmRetentionFilter(ctx, RetentionFilterDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.UpdateApmRetentionFilter`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `APMRetentionFiltersApi.UpdateApmRetentionFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a retention filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;
import com.datadog.api.client.v2.model.ApmRetentionFilterType;
import com.datadog.api.client.v2.model.RetentionFilterAllType;
import com.datadog.api.client.v2.model.RetentionFilterResponse;
import com.datadog.api.client.v2.model.RetentionFilterUpdateAttributes;
import com.datadog.api.client.v2.model.RetentionFilterUpdateData;
import com.datadog.api.client.v2.model.RetentionFilterUpdateRequest;
import com.datadog.api.client.v2.model.SpansFilterCreate;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    // there is a valid "retention_filter" in the system
    String RETENTION_FILTER_DATA_ID = System.getenv("RETENTION_FILTER_DATA_ID");

    RetentionFilterUpdateRequest body =
        new RetentionFilterUpdateRequest()
            .data(
                new RetentionFilterUpdateData()
                    .attributes(
                        new RetentionFilterUpdateAttributes()
                            .name("test")
                            .rate(0.9)
                            .filter(
                                new SpansFilterCreate().query("@_top_level:1 test:service-demo"))
                            .enabled(true)
                            .filterType(RetentionFilterAllType.SPANS_SAMPLING_PROCESSOR))
                    .id("test-id")
                    .type(ApmRetentionFilterType.apm_retention_filter));

    try {
      RetentionFilterResponse result =
          apiInstance.updateApmRetentionFilter(RETENTION_FILTER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmRetentionFiltersApi#updateApmRetentionFilter");
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
// Update a retention filter with trace rate returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;
import com.datadog.api.client.v2.model.ApmRetentionFilterType;
import com.datadog.api.client.v2.model.RetentionFilterAllType;
import com.datadog.api.client.v2.model.RetentionFilterResponse;
import com.datadog.api.client.v2.model.RetentionFilterUpdateAttributes;
import com.datadog.api.client.v2.model.RetentionFilterUpdateData;
import com.datadog.api.client.v2.model.RetentionFilterUpdateRequest;
import com.datadog.api.client.v2.model.SpansFilterCreate;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    // there is a valid "retention_filter" in the system
    String RETENTION_FILTER_DATA_ID = System.getenv("RETENTION_FILTER_DATA_ID");

    RetentionFilterUpdateRequest body =
        new RetentionFilterUpdateRequest()
            .data(
                new RetentionFilterUpdateData()
                    .attributes(
                        new RetentionFilterUpdateAttributes()
                            .name("test")
                            .rate(0.9)
                            .traceRate(1.0)
                            .filter(
                                new SpansFilterCreate().query("@_top_level:1 test:service-demo"))
                            .enabled(true)
                            .filterType(RetentionFilterAllType.SPANS_SAMPLING_PROCESSOR))
                    .id("test-id")
                    .type(ApmRetentionFilterType.apm_retention_filter));

    try {
      RetentionFilterResponse result =
          apiInstance.updateApmRetentionFilter(RETENTION_FILTER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmRetentionFiltersApi#updateApmRetentionFilter");
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
Update a retention filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.retention_filter_all_type import RetentionFilterAllType
from datadog_api_client.v2.model.retention_filter_update_attributes import RetentionFilterUpdateAttributes
from datadog_api_client.v2.model.retention_filter_update_data import RetentionFilterUpdateData
from datadog_api_client.v2.model.retention_filter_update_request import RetentionFilterUpdateRequest
from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = environ["RETENTION_FILTER_DATA_ID"]

body = RetentionFilterUpdateRequest(
    data=RetentionFilterUpdateData(
        attributes=RetentionFilterUpdateAttributes(
            name="test",
            rate=0.9,
            filter=SpansFilterCreate(
                query="@_top_level:1 test:service-demo",
            ),
            enabled=True,
            filter_type=RetentionFilterAllType.SPANS_SAMPLING_PROCESSOR,
        ),
        id="test-id",
        type=ApmRetentionFilterType.apm_retention_filter,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.update_apm_retention_filter(filter_id=RETENTION_FILTER_DATA_ID, body=body)

    print(response)
```

#####

```python
"""
Update a retention filter with trace rate returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.retention_filter_all_type import RetentionFilterAllType
from datadog_api_client.v2.model.retention_filter_update_attributes import RetentionFilterUpdateAttributes
from datadog_api_client.v2.model.retention_filter_update_data import RetentionFilterUpdateData
from datadog_api_client.v2.model.retention_filter_update_request import RetentionFilterUpdateRequest
from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = environ["RETENTION_FILTER_DATA_ID"]

body = RetentionFilterUpdateRequest(
    data=RetentionFilterUpdateData(
        attributes=RetentionFilterUpdateAttributes(
            name="test",
            rate=0.9,
            trace_rate=1.0,
            filter=SpansFilterCreate(
                query="@_top_level:1 test:service-demo",
            ),
            enabled=True,
            filter_type=RetentionFilterAllType.SPANS_SAMPLING_PROCESSOR,
        ),
        id="test-id",
        type=ApmRetentionFilterType.apm_retention_filter,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.update_apm_retention_filter(filter_id=RETENTION_FILTER_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a retention filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = ENV["RETENTION_FILTER_DATA_ID"]

body = DatadogAPIClient::V2::RetentionFilterUpdateRequest.new({
  data: DatadogAPIClient::V2::RetentionFilterUpdateData.new({
    attributes: DatadogAPIClient::V2::RetentionFilterUpdateAttributes.new({
      name: "test",
      rate: 0.9,
      filter: DatadogAPIClient::V2::SpansFilterCreate.new({
        query: "@_top_level:1 test:service-demo",
      }),
      enabled: true,
      filter_type: DatadogAPIClient::V2::RetentionFilterAllType::SPANS_SAMPLING_PROCESSOR,
    }),
    id: "test-id",
    type: DatadogAPIClient::V2::ApmRetentionFilterType::APM_RETENTION_FILTER,
  }),
})
p api_instance.update_apm_retention_filter(RETENTION_FILTER_DATA_ID, body)
```

#####

```ruby
# Update a retention filter with trace rate returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = ENV["RETENTION_FILTER_DATA_ID"]

body = DatadogAPIClient::V2::RetentionFilterUpdateRequest.new({
  data: DatadogAPIClient::V2::RetentionFilterUpdateData.new({
    attributes: DatadogAPIClient::V2::RetentionFilterUpdateAttributes.new({
      name: "test",
      rate: 0.9,
      trace_rate: 1.0,
      filter: DatadogAPIClient::V2::SpansFilterCreate.new({
        query: "@_top_level:1 test:service-demo",
      }),
      enabled: true,
      filter_type: DatadogAPIClient::V2::RetentionFilterAllType::SPANS_SAMPLING_PROCESSOR,
    }),
    id: "test-id",
    type: DatadogAPIClient::V2::ApmRetentionFilterType::APM_RETENTION_FILTER,
  }),
})
p api_instance.update_apm_retention_filter(RETENTION_FILTER_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update a retention filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::ApmRetentionFilterType;
use datadog_api_client::datadogV2::model::RetentionFilterAllType;
use datadog_api_client::datadogV2::model::RetentionFilterUpdateAttributes;
use datadog_api_client::datadogV2::model::RetentionFilterUpdateData;
use datadog_api_client::datadogV2::model::RetentionFilterUpdateRequest;
use datadog_api_client::datadogV2::model::SpansFilterCreate;

#[tokio::main]
async fn main() {
    // there is a valid "retention_filter" in the system
    let retention_filter_data_id = std::env::var("RETENTION_FILTER_DATA_ID").unwrap();
    let body = RetentionFilterUpdateRequest::new(RetentionFilterUpdateData::new(
        RetentionFilterUpdateAttributes::new(
            true,
            SpansFilterCreate::new("@_top_level:1 test:service-demo".to_string()),
            RetentionFilterAllType::SPANS_SAMPLING_PROCESSOR,
            "test".to_string(),
            0.9,
        ),
        "test-id".to_string(),
        ApmRetentionFilterType::apm_retention_filter,
    ));
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .update_apm_retention_filter(retention_filter_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Update a retention filter with trace rate returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::ApmRetentionFilterType;
use datadog_api_client::datadogV2::model::RetentionFilterAllType;
use datadog_api_client::datadogV2::model::RetentionFilterUpdateAttributes;
use datadog_api_client::datadogV2::model::RetentionFilterUpdateData;
use datadog_api_client::datadogV2::model::RetentionFilterUpdateRequest;
use datadog_api_client::datadogV2::model::SpansFilterCreate;

#[tokio::main]
async fn main() {
    // there is a valid "retention_filter" in the system
    let retention_filter_data_id = std::env::var("RETENTION_FILTER_DATA_ID").unwrap();
    let body = RetentionFilterUpdateRequest::new(RetentionFilterUpdateData::new(
        RetentionFilterUpdateAttributes::new(
            true,
            SpansFilterCreate::new("@_top_level:1 test:service-demo".to_string()),
            RetentionFilterAllType::SPANS_SAMPLING_PROCESSOR,
            "test".to_string(),
            0.9,
        )
        .trace_rate(1.0 as f64),
        "test-id".to_string(),
        ApmRetentionFilterType::apm_retention_filter,
    ));
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .update_apm_retention_filter(retention_filter_data_id.clone(), body)
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
 * Update a retention filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

// there is a valid "retention_filter" in the system
const RETENTION_FILTER_DATA_ID = process.env.RETENTION_FILTER_DATA_ID as string;

const params: v2.APMRetentionFiltersApiUpdateApmRetentionFilterRequest = {
  body: {
    data: {
      attributes: {
        name: "test",
        rate: 0.9,
        filter: {
          query: "@_top_level:1 test:service-demo",
        },
        enabled: true,
        filterType: "spans-sampling-processor",
      },
      id: "test-id",
      type: "apm_retention_filter",
    },
  },
  filterId: RETENTION_FILTER_DATA_ID,
};

apiInstance
  .updateApmRetentionFilter(params)
  .then((data: v2.RetentionFilterResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Update a retention filter with trace rate returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

// there is a valid "retention_filter" in the system
const RETENTION_FILTER_DATA_ID = process.env.RETENTION_FILTER_DATA_ID as string;

const params: v2.APMRetentionFiltersApiUpdateApmRetentionFilterRequest = {
  body: {
    data: {
      attributes: {
        name: "test",
        rate: 0.9,
        traceRate: 1.0,
        filter: {
          query: "@_top_level:1 test:service-demo",
        },
        enabled: true,
        filterType: "spans-sampling-processor",
      },
      id: "test-id",
      type: "apm_retention_filter",
    },
  },
  filterId: RETENTION_FILTER_DATA_ID,
};

apiInstance
  .updateApmRetentionFilter(params)
  .then((data: v2.RetentionFilterResponse) => {
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

## Delete a retention filter{% #delete-a-retention-filter %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/apm/config/retention-filters/{filter_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/apm/config/retention-filters/{filter_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters/{filter_id} |

### Overview



Delete a specific retention filter from your organization.

Default filters with types spans-errors-sampling-processor and spans-appsec-sampling-processor cannot be deleted.
This endpoint requires the `apm_retention_filter_write` permission.


### Arguments

#### Path Parameters

| Name                        | Type   | Description                     |
| --------------------------- | ------ | ------------------------------- |
| filter_id [*required*] | string | The ID of the retention filter. |

### Response

{% tab title="200" %}
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
                  \# Path parametersexport filter_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters/${filter_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a retention filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = environ["RETENTION_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    api_instance.delete_apm_retention_filter(
        filter_id=RETENTION_FILTER_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a retention filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = ENV["RETENTION_FILTER_DATA_ID"]
p api_instance.delete_apm_retention_filter(RETENTION_FILTER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a retention filter returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "retention_filter" in the system
    RetentionFilterDataID := os.Getenv("RETENTION_FILTER_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    r, err := api.DeleteApmRetentionFilter(ctx, RetentionFilterDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.DeleteApmRetentionFilter`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a retention filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    // there is a valid "retention_filter" in the system
    String RETENTION_FILTER_DATA_ID = System.getenv("RETENTION_FILTER_DATA_ID");

    try {
      apiInstance.deleteApmRetentionFilter(RETENTION_FILTER_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmRetentionFiltersApi#deleteApmRetentionFilter");
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
// Delete a retention filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;

#[tokio::main]
async fn main() {
    // there is a valid "retention_filter" in the system
    let retention_filter_data_id = std::env::var("RETENTION_FILTER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api
        .delete_apm_retention_filter(retention_filter_data_id.clone())
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
 * Delete a retention filter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

// there is a valid "retention_filter" in the system
const RETENTION_FILTER_DATA_ID = process.env.RETENTION_FILTER_DATA_ID as string;

const params: v2.APMRetentionFiltersApiDeleteApmRetentionFilterRequest = {
  filterId: RETENTION_FILTER_DATA_ID,
};

apiInstance
  .deleteApmRetentionFilter(params)
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

## Re-order retention filters{% #re-order-retention-filters %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/apm/config/retention-filters-execution-order |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/apm/config/retention-filters-execution-order |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/apm/config/retention-filters-execution-order      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/apm/config/retention-filters-execution-order      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/apm/config/retention-filters-execution-order     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/apm/config/retention-filters-execution-order |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters-execution-order |

### Overview

Re-order the execution order of retention filters. This endpoint requires the `apm_retention_filter_write` permission.

### Request

#### Body Data (required)

The list of retention filters in the new order.

{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                           |
| ------------ | ---------------------- | -------- | --------------------------------------------------------------------- |
|              | data [*required*] | [object] | A list of retention filters objects.                                  |
| data         | id [*required*]   | string   | The ID of the retention filter.                                       |
| data         | type [*required*] | enum     | The type of the resource. Allowed enum values: `apm_retention_filter` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "jdZrilSJQLqzb6Cu7aub9Q",
      "type": "apm_retention_filter"
    },
    {
      "id": "7RBOb7dLSYWI01yc3pIH8w",
      "type": "apm_retention_filter"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
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
                          \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/retention-filters-execution-order" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "id": "jdZrilSJQLqzb6Cu7aub9Q",
      "type": "apm_retention_filter"
    },
    {
      "id": "7RBOb7dLSYWI01yc3pIH8w",
      "type": "apm_retention_filter"
    }
  ]
}
EOF

#####

```go
// Re-order retention filters returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.ReorderRetentionFiltersRequest{
        Data: []datadogV2.RetentionFilterWithoutAttributes{
            {
                Id:   "jdZrilSJQLqzb6Cu7aub9Q",
                Type: datadogV2.APMRETENTIONFILTERTYPE_apm_retention_filter,
            },
            {
                Id:   "7RBOb7dLSYWI01yc3pIH8w",
                Type: datadogV2.APMRETENTIONFILTERTYPE_apm_retention_filter,
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewAPMRetentionFiltersApi(apiClient)
    r, err := api.ReorderApmRetentionFilters(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `APMRetentionFiltersApi.ReorderApmRetentionFilters`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Re-order retention filters returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmRetentionFiltersApi;
import com.datadog.api.client.v2.model.ApmRetentionFilterType;
import com.datadog.api.client.v2.model.ReorderRetentionFiltersRequest;
import com.datadog.api.client.v2.model.RetentionFilterWithoutAttributes;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmRetentionFiltersApi apiInstance = new ApmRetentionFiltersApi(defaultClient);

    ReorderRetentionFiltersRequest body =
        new ReorderRetentionFiltersRequest()
            .data(
                Arrays.asList(
                    new RetentionFilterWithoutAttributes()
                        .id("jdZrilSJQLqzb6Cu7aub9Q")
                        .type(ApmRetentionFilterType.apm_retention_filter),
                    new RetentionFilterWithoutAttributes()
                        .id("7RBOb7dLSYWI01yc3pIH8w")
                        .type(ApmRetentionFilterType.apm_retention_filter)));

    try {
      apiInstance.reorderApmRetentionFilters(body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ApmRetentionFiltersApi#reorderApmRetentionFilters");
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
Re-order retention filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.reorder_retention_filters_request import ReorderRetentionFiltersRequest
from datadog_api_client.v2.model.retention_filter_without_attributes import RetentionFilterWithoutAttributes

body = ReorderRetentionFiltersRequest(
    data=[
        RetentionFilterWithoutAttributes(
            id="jdZrilSJQLqzb6Cu7aub9Q",
            type=ApmRetentionFilterType.apm_retention_filter,
        ),
        RetentionFilterWithoutAttributes(
            id="7RBOb7dLSYWI01yc3pIH8w",
            type=ApmRetentionFilterType.apm_retention_filter,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    api_instance.reorder_apm_retention_filters(body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Re-order retention filters returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMRetentionFiltersAPI.new

body = DatadogAPIClient::V2::ReorderRetentionFiltersRequest.new({
  data: [
    DatadogAPIClient::V2::RetentionFilterWithoutAttributes.new({
      id: "jdZrilSJQLqzb6Cu7aub9Q",
      type: DatadogAPIClient::V2::ApmRetentionFilterType::APM_RETENTION_FILTER,
    }),
    DatadogAPIClient::V2::RetentionFilterWithoutAttributes.new({
      id: "7RBOb7dLSYWI01yc3pIH8w",
      type: DatadogAPIClient::V2::ApmRetentionFilterType::APM_RETENTION_FILTER,
    }),
  ],
})
p api_instance.reorder_apm_retention_filters(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Re-order retention filters returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm_retention_filters::APMRetentionFiltersAPI;
use datadog_api_client::datadogV2::model::ApmRetentionFilterType;
use datadog_api_client::datadogV2::model::ReorderRetentionFiltersRequest;
use datadog_api_client::datadogV2::model::RetentionFilterWithoutAttributes;

#[tokio::main]
async fn main() {
    let body = ReorderRetentionFiltersRequest::new(vec![
        RetentionFilterWithoutAttributes::new(
            "jdZrilSJQLqzb6Cu7aub9Q".to_string(),
            ApmRetentionFilterType::apm_retention_filter,
        ),
        RetentionFilterWithoutAttributes::new(
            "7RBOb7dLSYWI01yc3pIH8w".to_string(),
            ApmRetentionFilterType::apm_retention_filter,
        ),
    ]);
    let configuration = datadog::Configuration::new();
    let api = APMRetentionFiltersAPI::with_config(configuration);
    let resp = api.reorder_apm_retention_filters(body).await;
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
 * Re-order retention filters returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMRetentionFiltersApi(configuration);

const params: v2.APMRetentionFiltersApiReorderApmRetentionFiltersRequest = {
  body: {
    data: [
      {
        id: "jdZrilSJQLqzb6Cu7aub9Q",
        type: "apm_retention_filter",
      },
      {
        id: "7RBOb7dLSYWI01yc3pIH8w",
        type: "apm_retention_filter",
      },
    ],
  },
};

apiInstance
  .reorderApmRetentionFilters(params)
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
