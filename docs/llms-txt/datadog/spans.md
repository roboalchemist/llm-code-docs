# Source: https://docs.datadoghq.com/api/latest/spans.md

---
title: Spans
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Spans
---

# Spans

Search and aggregate your spans from your Datadog platform over HTTP.

## Get a list of spans{% #get-a-list-of-spans %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/spans/events |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/spans/events |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/spans/events      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/spans/events      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/spans/events     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/spans/events |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/spans/events |

### Overview



List endpoint returns spans that match a span search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination?tab=v2api).

Use this endpoint to see your latest spans. This endpoint is rate limited to `300` requests per hour.

OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#spans) to access this endpoint.



### Arguments

#### Query Strings

| Name          | Type    | Description                                                                                                          |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| filter[query] | string  | Search query following spans syntax.                                                                                 |
| filter[from]  | string  | Minimum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds). |
| filter[to]    | string  | Maximum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds). |
| sort          | enum    | Order of spans in results.Allowed enum values: `timestamp, -timestamp`                                               |
| page[cursor]  | string  | List following results with a cursor provided in the previous query.                                                 |
| page[limit]   | integer | Maximum number of spans in the response.                                                                             |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all spans matching the request and pagination information.

| Parent field | Field            | Type      | Description                                                                                                                                                                  |
| ------------ | ---------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | [object]  | Array of spans matching the request.                                                                                                                                         |
| data         | attributes       | object    | JSON object containing all span attributes and their associated values.                                                                                                      |
| attributes   | attributes       | object    | JSON object of attributes from your span.                                                                                                                                    |
| attributes   | custom           | object    | JSON object of custom spans data.                                                                                                                                            |
| attributes   | end_timestamp    | date-time | End timestamp of your span.                                                                                                                                                  |
| attributes   | env              | string    | Name of the environment from where the spans are being sent.                                                                                                                 |
| attributes   | host             | string    | Name of the machine from where the spans are being sent.                                                                                                                     |
| attributes   | ingestion_reason | string    | The reason why the span was ingested.                                                                                                                                        |
| attributes   | parent_id        | string    | Id of the span that's parent of this span.                                                                                                                                   |
| attributes   | resource_hash    | string    | Unique identifier of the resource.                                                                                                                                           |
| attributes   | resource_name    | string    | The name of the resource.                                                                                                                                                    |
| attributes   | retained_by      | string    | The reason why the span was indexed.                                                                                                                                         |
| attributes   | service          | string    | The name of the application or service generating the span events. It is used to switch from APM to Logs, so make sure you define the same value when you use both products. |
| attributes   | single_span      | boolean   | Whether or not the span was collected as a stand-alone span. Always associated to "single_span" ingestion_reason if true.                                                    |
| attributes   | span_id          | string    | Id of the span.                                                                                                                                                              |
| attributes   | start_timestamp  | date-time | Start timestamp of your span.                                                                                                                                                |
| attributes   | tags             | [string]  | Array of tags associated with your span.                                                                                                                                     |
| attributes   | trace_id         | string    | Id of the trace to which the span belongs.                                                                                                                                   |
| attributes   | type             | string    | The type of the span.                                                                                                                                                        |
| data         | id               | string    | Unique ID of the Span.                                                                                                                                                       |
| data         | type             | enum      | Type of the span. Allowed enum values: `spans`                                                                                                                               |
|              | links            | object    | Links attributes.                                                                                                                                                            |
| links        | next             | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                            |
|              | meta             | object    | The metadata associated with a request.                                                                                                                                      |
| meta         | elapsed          | int64     | The time elapsed in milliseconds.                                                                                                                                            |
| meta         | page             | object    | Paging attributes.                                                                                                                                                           |
| page         | after            | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.                                |
| meta         | request_id       | string    | The identifier of the request.                                                                                                                                               |
| meta         | status           | enum      | The status of the response. Allowed enum values: `done,timeout`                                                                                                              |
| meta         | warnings         | [object]  | A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.                                                |
| warnings     | code             | string    | A unique code for this type of warning.                                                                                                                                      |
| warnings     | detail           | string    | A detailed explanation of this specific warning.                                                                                                                             |
| warnings     | title            | string    | A short human-readable summary of the warning.                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "custom": {},
        "end_timestamp": "2023-01-02T09:42:36.420Z",
        "env": "prod",
        "host": "i-0123",
        "ingestion_reason": "rule",
        "parent_id": "0",
        "resource_hash": "a12345678b91c23d",
        "resource_name": "agent",
        "retained_by": "retention_filter",
        "service": "agent",
        "single_span": true,
        "span_id": "1234567890987654321",
        "start_timestamp": "2023-01-02T09:42:36.320Z",
        "tags": [
          "team:A"
        ],
        "trace_id": "1234567890987654321",
        "type": "web"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "spans"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/spans/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden: Access denied.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="422" %}
Unprocessable Entity.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests: The rate limit set by the API has been exceeded.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a list of spans returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansApi(api_client)
    response = api_instance.list_spans_get()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a list of spans returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansAPI.new
p api_instance.list_spans_get()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```java
// Get a list of spans returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansApi;
import com.datadog.api.client.v2.model.SpansListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansApi apiInstance = new SpansApi(defaultClient);

    try {
      SpansListResponse result = apiInstance.listSpansGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansApi#listSpansGet");
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
// Get a list of spans returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans::ListSpansGetOptionalParams;
use datadog_api_client::datadogV2::api_spans::SpansAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SpansAPI::with_config(configuration);
    let resp = api
        .list_spans_get(ListSpansGetOptionalParams::default())
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
 * Get a list of spans returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansApi(configuration);

apiInstance
  .listSpansGet()
  .then((data: v2.SpansListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
##### 

```go
// Get a list of spans returns "OK" response

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
	api := datadogV2.NewSpansApi(apiClient)
	resp, r, err := api.ListSpansGet(ctx, *datadogV2.NewListSpansGetOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpansApi.ListSpansGet`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SpansApi.ListSpansGet`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
{% /tab %}

## Search spans{% #search-spans %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/spans/events/search |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/spans/events/search |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/spans/events/search      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/spans/events/search      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/spans/events/search     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/spans/events/search |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/spans/events/search |

### Overview



List endpoint returns spans that match a span search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination?tab=v2api).

Use this endpoint to build complex spans filtering and search. This endpoint is rate limited to `300` requests per hour.

OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#spans) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field      | Type   | Description                                                                                                                                           |
| ------------ | ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | object | The object containing the query content.                                                                                                              |
| data         | attributes | object | The object containing all the query parameters.                                                                                                       |
| attributes   | filter     | object | The search and filter query settings.                                                                                                                 |
| filter       | from       | string | The minimum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).                               |
| filter       | query      | string | The search query - following the span search syntax.                                                                                                  |
| filter       | to         | string | The maximum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).                               |
| attributes   | options    | object | Global query options that are used during the query. Note: You should only supply timezone or time offset but not both otherwise the query will fail. |
| options      | timeOffset | int64  | The time offset (in seconds) to apply to the query.                                                                                                   |
| options      | timezone   | string | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).             |
| attributes   | page       | object | Paging attributes for listing spans.                                                                                                                  |
| page         | cursor     | string | List following results with a cursor provided in the previous query.                                                                                  |
| page         | limit      | int32  | Maximum number of spans in the response.                                                                                                              |
| attributes   | sort       | enum   | Sort parameters when querying spans. Allowed enum values: `timestamp,-timestamp`                                                                      |
| data         | type       | enum   | The type of resource. The value should always be search_request. Allowed enum values: `search_request`                                                |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "data": {
    "attributes": {
      "filter": {
        "from": "now-15m",
        "query": "*",
        "to": "now"
      },
      "options": {
        "timezone": "GMT"
      },
      "page": {
        "limit": 25
      },
      "sort": "timestamp"
    },
    "type": "search_request"
  }
}
```

##### 

```json
{
  "data": {
    "attributes": {
      "filter": {
        "from": "now-15m",
        "query": "service:python*",
        "to": "now"
      },
      "options": {
        "timezone": "GMT"
      },
      "page": {
        "limit": 2
      },
      "sort": "timestamp"
    },
    "type": "search_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all spans matching the request and pagination information.

| Parent field | Field            | Type      | Description                                                                                                                                                                  |
| ------------ | ---------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | [object]  | Array of spans matching the request.                                                                                                                                         |
| data         | attributes       | object    | JSON object containing all span attributes and their associated values.                                                                                                      |
| attributes   | attributes       | object    | JSON object of attributes from your span.                                                                                                                                    |
| attributes   | custom           | object    | JSON object of custom spans data.                                                                                                                                            |
| attributes   | end_timestamp    | date-time | End timestamp of your span.                                                                                                                                                  |
| attributes   | env              | string    | Name of the environment from where the spans are being sent.                                                                                                                 |
| attributes   | host             | string    | Name of the machine from where the spans are being sent.                                                                                                                     |
| attributes   | ingestion_reason | string    | The reason why the span was ingested.                                                                                                                                        |
| attributes   | parent_id        | string    | Id of the span that's parent of this span.                                                                                                                                   |
| attributes   | resource_hash    | string    | Unique identifier of the resource.                                                                                                                                           |
| attributes   | resource_name    | string    | The name of the resource.                                                                                                                                                    |
| attributes   | retained_by      | string    | The reason why the span was indexed.                                                                                                                                         |
| attributes   | service          | string    | The name of the application or service generating the span events. It is used to switch from APM to Logs, so make sure you define the same value when you use both products. |
| attributes   | single_span      | boolean   | Whether or not the span was collected as a stand-alone span. Always associated to "single_span" ingestion_reason if true.                                                    |
| attributes   | span_id          | string    | Id of the span.                                                                                                                                                              |
| attributes   | start_timestamp  | date-time | Start timestamp of your span.                                                                                                                                                |
| attributes   | tags             | [string]  | Array of tags associated with your span.                                                                                                                                     |
| attributes   | trace_id         | string    | Id of the trace to which the span belongs.                                                                                                                                   |
| attributes   | type             | string    | The type of the span.                                                                                                                                                        |
| data         | id               | string    | Unique ID of the Span.                                                                                                                                                       |
| data         | type             | enum      | Type of the span. Allowed enum values: `spans`                                                                                                                               |
|              | links            | object    | Links attributes.                                                                                                                                                            |
| links        | next             | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                            |
|              | meta             | object    | The metadata associated with a request.                                                                                                                                      |
| meta         | elapsed          | int64     | The time elapsed in milliseconds.                                                                                                                                            |
| meta         | page             | object    | Paging attributes.                                                                                                                                                           |
| page         | after            | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.                                |
| meta         | request_id       | string    | The identifier of the request.                                                                                                                                               |
| meta         | status           | enum      | The status of the response. Allowed enum values: `done,timeout`                                                                                                              |
| meta         | warnings         | [object]  | A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.                                                |
| warnings     | code             | string    | A unique code for this type of warning.                                                                                                                                      |
| warnings     | detail           | string    | A detailed explanation of this specific warning.                                                                                                                             |
| warnings     | title            | string    | A short human-readable summary of the warning.                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "custom": {},
        "end_timestamp": "2023-01-02T09:42:36.420Z",
        "env": "prod",
        "host": "i-0123",
        "ingestion_reason": "rule",
        "parent_id": "0",
        "resource_hash": "a12345678b91c23d",
        "resource_name": "agent",
        "retained_by": "retention_filter",
        "service": "agent",
        "single_span": true,
        "span_id": "1234567890987654321",
        "start_timestamp": "2023-01-02T09:42:36.320Z",
        "tags": [
          "team:A"
        ],
        "trace_id": "1234567890987654321",
        "type": "web"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "spans"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/spans/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden: Access denied.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="422" %}
Unprocessable Entity.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests: The rate limit set by the API has been exceeded.
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "from": "now-15m",
        "query": "*",
        "to": "now"
      },
      "options": {
        "timezone": "GMT"
      },
      "page": {
        "limit": 25
      },
      "sort": "timestamp"
    },
    "type": "search_request"
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "from": "now-15m",
        "query": "service:python*",
        "to": "now"
      },
      "options": {
        "timezone": "GMT"
      },
      "page": {
        "limit": 2
      },
      "sort": "timestamp"
    },
    "type": "search_request"
  }
}
EOF
                        
##### 

```go
// Search spans returns "OK" response

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
	body := datadogV2.SpansListRequest{
		Data: &datadogV2.SpansListRequestData{
			Attributes: &datadogV2.SpansListRequestAttributes{
				Filter: &datadogV2.SpansQueryFilter{
					From:  datadog.PtrString("now-15m"),
					Query: datadog.PtrString("*"),
					To:    datadog.PtrString("now"),
				},
				Options: &datadogV2.SpansQueryOptions{
					Timezone: datadog.PtrString("GMT"),
				},
				Page: &datadogV2.SpansListRequestPage{
					Limit: datadog.PtrInt32(25),
				},
				Sort: datadogV2.SPANSSORT_TIMESTAMP_ASCENDING.Ptr(),
			},
			Type: datadogV2.SPANSLISTREQUESTTYPE_SEARCH_REQUEST.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSpansApi(apiClient)
	resp, r, err := api.ListSpans(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpansApi.ListSpans`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SpansApi.ListSpans`:\n%s\n", responseContent)
}
```

##### 

```go
// Search spans returns "OK" response with pagination

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
	body := datadogV2.SpansListRequest{
		Data: &datadogV2.SpansListRequestData{
			Attributes: &datadogV2.SpansListRequestAttributes{
				Filter: &datadogV2.SpansQueryFilter{
					From:  datadog.PtrString("now-15m"),
					Query: datadog.PtrString("service:python*"),
					To:    datadog.PtrString("now"),
				},
				Options: &datadogV2.SpansQueryOptions{
					Timezone: datadog.PtrString("GMT"),
				},
				Page: &datadogV2.SpansListRequestPage{
					Limit: datadog.PtrInt32(2),
				},
				Sort: datadogV2.SPANSSORT_TIMESTAMP_ASCENDING.Ptr(),
			},
			Type: datadogV2.SPANSLISTREQUESTTYPE_SEARCH_REQUEST.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSpansApi(apiClient)
	resp, _ := api.ListSpansWithPagination(ctx, body)

	for paginationResult := range resp {
		if paginationResult.Error != nil {
			fmt.Fprintf(os.Stderr, "Error when calling `SpansApi.ListSpans`: %v\n", paginationResult.Error)
		}
		responseContent, _ := json.MarshalIndent(paginationResult.Item, "", "  ")
		fmt.Fprintf(os.Stdout, "%s\n", responseContent)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Search spans returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansApi;
import com.datadog.api.client.v2.model.SpansListRequest;
import com.datadog.api.client.v2.model.SpansListRequestAttributes;
import com.datadog.api.client.v2.model.SpansListRequestData;
import com.datadog.api.client.v2.model.SpansListRequestPage;
import com.datadog.api.client.v2.model.SpansListRequestType;
import com.datadog.api.client.v2.model.SpansListResponse;
import com.datadog.api.client.v2.model.SpansQueryFilter;
import com.datadog.api.client.v2.model.SpansQueryOptions;
import com.datadog.api.client.v2.model.SpansSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansApi apiInstance = new SpansApi(defaultClient);

    SpansListRequest body =
        new SpansListRequest()
            .data(
                new SpansListRequestData()
                    .attributes(
                        new SpansListRequestAttributes()
                            .filter(new SpansQueryFilter().from("now-15m").query("*").to("now"))
                            .options(new SpansQueryOptions().timezone("GMT"))
                            .page(new SpansListRequestPage().limit(25))
                            .sort(SpansSort.TIMESTAMP_ASCENDING))
                    .type(SpansListRequestType.SEARCH_REQUEST));

    try {
      SpansListResponse result = apiInstance.listSpans(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansApi#listSpans");
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
// Search spans returns "OK" response with pagination

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.PaginationIterable;
import com.datadog.api.client.v2.api.SpansApi;
import com.datadog.api.client.v2.model.Span;
import com.datadog.api.client.v2.model.SpansListRequest;
import com.datadog.api.client.v2.model.SpansListRequestAttributes;
import com.datadog.api.client.v2.model.SpansListRequestData;
import com.datadog.api.client.v2.model.SpansListRequestPage;
import com.datadog.api.client.v2.model.SpansListRequestType;
import com.datadog.api.client.v2.model.SpansQueryFilter;
import com.datadog.api.client.v2.model.SpansQueryOptions;
import com.datadog.api.client.v2.model.SpansSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansApi apiInstance = new SpansApi(defaultClient);

    SpansListRequest body =
        new SpansListRequest()
            .data(
                new SpansListRequestData()
                    .attributes(
                        new SpansListRequestAttributes()
                            .filter(
                                new SpansQueryFilter()
                                    .from("now-15m")
                                    .query("service:python*")
                                    .to("now"))
                            .options(new SpansQueryOptions().timezone("GMT"))
                            .page(new SpansListRequestPage().limit(2))
                            .sort(SpansSort.TIMESTAMP_ASCENDING))
                    .type(SpansListRequestType.SEARCH_REQUEST));

    try {
      PaginationIterable<Span> iterable = apiInstance.listSpansWithPagination(body);

      for (Span item : iterable) {
        System.out.println(item);
      }
    } catch (RuntimeException e) {
      System.err.println("Exception when calling SpansApi#listSpansWithPagination");
      System.err.println("Reason: " + e.getMessage());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
"""
Search spans returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi
from datadog_api_client.v2.model.spans_list_request import SpansListRequest
from datadog_api_client.v2.model.spans_list_request_attributes import SpansListRequestAttributes
from datadog_api_client.v2.model.spans_list_request_data import SpansListRequestData
from datadog_api_client.v2.model.spans_list_request_page import SpansListRequestPage
from datadog_api_client.v2.model.spans_list_request_type import SpansListRequestType
from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions
from datadog_api_client.v2.model.spans_sort import SpansSort

body = SpansListRequest(
    data=SpansListRequestData(
        attributes=SpansListRequestAttributes(
            filter=SpansQueryFilter(
                _from="now-15m",
                query="*",
                to="now",
            ),
            options=SpansQueryOptions(
                timezone="GMT",
            ),
            page=SpansListRequestPage(
                limit=25,
            ),
            sort=SpansSort.TIMESTAMP_ASCENDING,
        ),
        type=SpansListRequestType.SEARCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansApi(api_client)
    response = api_instance.list_spans(body=body)

    print(response)
```

##### 

```python
"""
Search spans returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi
from datadog_api_client.v2.model.spans_list_request import SpansListRequest
from datadog_api_client.v2.model.spans_list_request_attributes import SpansListRequestAttributes
from datadog_api_client.v2.model.spans_list_request_data import SpansListRequestData
from datadog_api_client.v2.model.spans_list_request_page import SpansListRequestPage
from datadog_api_client.v2.model.spans_list_request_type import SpansListRequestType
from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions
from datadog_api_client.v2.model.spans_sort import SpansSort

body = SpansListRequest(
    data=SpansListRequestData(
        attributes=SpansListRequestAttributes(
            filter=SpansQueryFilter(
                _from="now-15m",
                query="service:python*",
                to="now",
            ),
            options=SpansQueryOptions(
                timezone="GMT",
            ),
            page=SpansListRequestPage(
                limit=2,
            ),
            sort=SpansSort.TIMESTAMP_ASCENDING,
        ),
        type=SpansListRequestType.SEARCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansApi(api_client)
    items = api_instance.list_spans_with_pagination(body=body)
    for item in items:
        print(item)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Search spans returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansAPI.new

body = DatadogAPIClient::V2::SpansListRequest.new({
  data: DatadogAPIClient::V2::SpansListRequestData.new({
    attributes: DatadogAPIClient::V2::SpansListRequestAttributes.new({
      filter: DatadogAPIClient::V2::SpansQueryFilter.new({
        from: "now-15m",
        query: "*",
        to: "now",
      }),
      options: DatadogAPIClient::V2::SpansQueryOptions.new({
        timezone: "GMT",
      }),
      page: DatadogAPIClient::V2::SpansListRequestPage.new({
        limit: 25,
      }),
      sort: DatadogAPIClient::V2::SpansSort::TIMESTAMP_ASCENDING,
    }),
    type: DatadogAPIClient::V2::SpansListRequestType::SEARCH_REQUEST,
  }),
})
p api_instance.list_spans(body)
```

##### 

```ruby
# Search spans returns "OK" response with pagination

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansAPI.new

body = DatadogAPIClient::V2::SpansListRequest.new({
  data: DatadogAPIClient::V2::SpansListRequestData.new({
    attributes: DatadogAPIClient::V2::SpansListRequestAttributes.new({
      filter: DatadogAPIClient::V2::SpansQueryFilter.new({
        from: "now-15m",
        query: "service:python*",
        to: "now",
      }),
      options: DatadogAPIClient::V2::SpansQueryOptions.new({
        timezone: "GMT",
      }),
      page: DatadogAPIClient::V2::SpansListRequestPage.new({
        limit: 2,
      }),
      sort: DatadogAPIClient::V2::SpansSort::TIMESTAMP_ASCENDING,
    }),
    type: DatadogAPIClient::V2::SpansListRequestType::SEARCH_REQUEST,
  }),
})
api_instance.list_spans_with_pagination(body) { |item| puts item }
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Search spans returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans::SpansAPI;
use datadog_api_client::datadogV2::model::SpansListRequest;
use datadog_api_client::datadogV2::model::SpansListRequestAttributes;
use datadog_api_client::datadogV2::model::SpansListRequestData;
use datadog_api_client::datadogV2::model::SpansListRequestPage;
use datadog_api_client::datadogV2::model::SpansListRequestType;
use datadog_api_client::datadogV2::model::SpansQueryFilter;
use datadog_api_client::datadogV2::model::SpansQueryOptions;
use datadog_api_client::datadogV2::model::SpansSort;

#[tokio::main]
async fn main() {
    let body = SpansListRequest::new().data(
        SpansListRequestData::new()
            .attributes(
                SpansListRequestAttributes::new()
                    .filter(
                        SpansQueryFilter::new()
                            .from("now-15m".to_string())
                            .query("*".to_string())
                            .to("now".to_string()),
                    )
                    .options(SpansQueryOptions::new().timezone("GMT".to_string()))
                    .page(SpansListRequestPage::new().limit(25))
                    .sort(SpansSort::TIMESTAMP_ASCENDING),
            )
            .type_(SpansListRequestType::SEARCH_REQUEST),
    );
    let configuration = datadog::Configuration::new();
    let api = SpansAPI::with_config(configuration);
    let resp = api.list_spans(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Search spans returns "OK" response with pagination
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans::SpansAPI;
use datadog_api_client::datadogV2::model::SpansListRequest;
use datadog_api_client::datadogV2::model::SpansListRequestAttributes;
use datadog_api_client::datadogV2::model::SpansListRequestData;
use datadog_api_client::datadogV2::model::SpansListRequestPage;
use datadog_api_client::datadogV2::model::SpansListRequestType;
use datadog_api_client::datadogV2::model::SpansQueryFilter;
use datadog_api_client::datadogV2::model::SpansQueryOptions;
use datadog_api_client::datadogV2::model::SpansSort;
use futures_util::pin_mut;
use futures_util::stream::StreamExt;

#[tokio::main]
async fn main() {
    let body = SpansListRequest::new().data(
        SpansListRequestData::new()
            .attributes(
                SpansListRequestAttributes::new()
                    .filter(
                        SpansQueryFilter::new()
                            .from("now-15m".to_string())
                            .query("service:python*".to_string())
                            .to("now".to_string()),
                    )
                    .options(SpansQueryOptions::new().timezone("GMT".to_string()))
                    .page(SpansListRequestPage::new().limit(2))
                    .sort(SpansSort::TIMESTAMP_ASCENDING),
            )
            .type_(SpansListRequestType::SEARCH_REQUEST),
    );
    let configuration = datadog::Configuration::new();
    let api = SpansAPI::with_config(configuration);
    let response = api.list_spans_with_pagination(body);
    pin_mut!(response);
    while let Some(resp) = response.next().await {
        if let Ok(value) = resp {
            println!("{:#?}", value);
        } else {
            println!("{:#?}", resp.unwrap_err());
        }
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Search spans returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansApi(configuration);

const params: v2.SpansApiListSpansRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          from: "now-15m",
          query: "*",
          to: "now",
        },
        options: {
          timezone: "GMT",
        },
        page: {
          limit: 25,
        },
        sort: "timestamp",
      },
      type: "search_request",
    },
  },
};

apiInstance
  .listSpans(params)
  .then((data: v2.SpansListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Search spans returns "OK" response with pagination
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansApi(configuration);

const params: v2.SpansApiListSpansRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          from: "now-15m",
          query: "service:python*",
          to: "now",
        },
        options: {
          timezone: "GMT",
        },
        page: {
          limit: 2,
        },
        sort: "timestamp",
      },
      type: "search_request",
    },
  },
};

(async () => {
  try {
    for await (const item of apiInstance.listSpansWithPagination(params)) {
      console.log(item);
    }
  } catch (error) {
    console.error(error);
  }
})();
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Aggregate spans{% #aggregate-spans %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/spans/analytics/aggregate |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/spans/analytics/aggregate |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/spans/analytics/aggregate      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/spans/analytics/aggregate      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/spans/analytics/aggregate     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/spans/analytics/aggregate |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/spans/analytics/aggregate |

### Overview

The API endpoint to aggregate spans into buckets and compute metrics and timeseries. This endpoint is rate limited to `300` requests per hour. This endpoint requires the `apm_read` permission.

OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#spans) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                         | Type          | Description                                                                                                                                              |
| ------------ | ----------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                          | object        | The object containing the query content.                                                                                                                 |
| data         | attributes                    | object        | The object containing all the query parameters.                                                                                                          |
| attributes   | compute                       | [object]      | The list of metrics or timeseries to compute for the retrieved buckets.                                                                                  |
| compute      | aggregation [*required*] | enum          | An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`                                        |
| compute      | interval                      | string        | The time buckets' size (only used for type=timeseries) Defaults to a resolution of 150 points.                                                           |
| compute      | metric                        | string        | The metric to use.                                                                                                                                       |
| compute      | type                          | enum          | The type of compute. Allowed enum values: `timeseries,total`                                                                                             |
| attributes   | filter                        | object        | The search and filter query settings.                                                                                                                    |
| filter       | from                          | string        | The minimum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).                                  |
| filter       | query                         | string        | The search query - following the span search syntax.                                                                                                     |
| filter       | to                            | string        | The maximum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).                                  |
| attributes   | group_by                      | [object]      | The rules for the group by.                                                                                                                              |
| group_by     | facet [*required*]       | string        | The name of the facet to use (required).                                                                                                                 |
| group_by     | histogram                     | object        | Used to perform a histogram computation (only for measure facets). Note: At most 100 buckets are allowed, the number of buckets is (max - min)/interval. |
| histogram    | interval [*required*]    | double        | The bin size of the histogram buckets.                                                                                                                   |
| histogram    | max [*required*]         | double        | The maximum value for the measure used in the histogram (values greater than this one are filtered out).                                                 |
| histogram    | min [*required*]         | double        | The minimum value for the measure used in the histogram (values smaller than this one are filtered out).                                                 |
| group_by     | limit                         | int64         | The maximum buckets to return for this group by.                                                                                                         |
| group_by     | missing                       |  <oneOf> | The value to use for spans that don't have the facet used to group by.                                                                                   |
| missing      | Option 1                      | string        | The missing value to use if there is string valued facet.                                                                                                |
| missing      | Option 2                      | double        | The missing value to use if there is a number valued facet.                                                                                              |
| group_by     | sort                          | object        | A sort rule.                                                                                                                                             |
| sort         | aggregation                   | enum          | An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`                                        |
| sort         | metric                        | string        | The metric to sort by (only used for `type=measure`).                                                                                                    |
| sort         | order                         | enum          | The order to use, ascending or descending. Allowed enum values: `asc,desc`                                                                               |
| sort         | type                          | enum          | The type of sorting algorithm. Allowed enum values: `alphabetical,measure`                                                                               |
| group_by     | total                         |  <oneOf> | A resulting object to put the given computes in over all the matching records.                                                                           |
| total        | Option 1                      | boolean       | If set to true, creates an additional bucket labeled "$facet_total".                                                                                     |
| total        | Option 2                      | string        | A string to use as the key value for the total bucket.                                                                                                   |
| total        | Option 3                      | double        | A number to use as the key value for the total bucket.                                                                                                   |
| attributes   | options                       | object        | Global query options that are used during the query. Note: You should only supply timezone or time offset but not both otherwise the query will fail.    |
| options      | timeOffset                    | int64         | The time offset (in seconds) to apply to the query.                                                                                                      |
| options      | timezone                      | string        | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).                |
| data         | type                          | enum          | The type of resource. The value should always be aggregate_request. Allowed enum values: `aggregate_request`                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": [
        {
          "aggregation": "count",
          "interval": "5m",
          "type": "timeseries"
        }
      ],
      "filter": {
        "from": "now-15m",
        "query": "*",
        "to": "now"
      }
    },
    "type": "aggregate_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object for the spans aggregate API endpoint.

| Parent field         | Field      | Type          | Description                                                                                                                   |
| -------------------- | ---------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------- |
|                      | data       | [object]      | The list of matching buckets, one item per bucket.                                                                            |
| data                 | attributes | object        | A bucket values.                                                                                                              |
| attributes           | by         | object        | The key, value pairs for each group by.                                                                                       |
| additionalProperties | <any-key>  |               | The values for each group by.                                                                                                 |
| attributes           | compute    | object        | The compute data.                                                                                                             |
| attributes           | computes   | object        | A map of the metric name -> value for regular compute or list of values for a timeseries.                                     |
| additionalProperties | <any-key>  |  <oneOf> | A bucket value, can be either a timeseries or a single value.                                                                 |
| <any-key>            | Option 1   | string        | A single string value.                                                                                                        |
| <any-key>            | Option 2   | double        | A single number value.                                                                                                        |
| <any-key>            | Option 3   | [object]      | A timeseries array.                                                                                                           |
| Option 3             | time       | string        | The time value for this point.                                                                                                |
| Option 3             | value      | double        | The value for this point.                                                                                                     |
| data                 | id         | string        | ID of the spans aggregate.                                                                                                    |
| data                 | type       | enum          | The spans aggregate bucket type. Allowed enum values: `bucket`                                                                |
|                      | meta       | object        | The metadata associated with a request.                                                                                       |
| meta                 | elapsed    | int64         | The time elapsed in milliseconds.                                                                                             |
| meta                 | request_id | string        | The identifier of the request.                                                                                                |
| meta                 | status     | enum          | The status of the response. Allowed enum values: `done,timeout`                                                               |
| meta                 | warnings   | [object]      | A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response. |
| warnings             | code       | string        | A unique code for this type of warning.                                                                                       |
| warnings             | detail     | string        | A detailed explanation of this specific warning.                                                                              |
| warnings             | title      | string        | A short human-readable summary of the warning.                                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "by": {
          "<any-key>": "undefined"
        },
        "compute": {},
        "computes": {
          "<any-key>": {
            "description": "undefined",
            "type": "undefined"
          }
        }
      },
      "id": "string",
      "type": "bucket"
    }
  ],
  "meta": {
    "elapsed": 132,
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/analytics/aggregate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "compute": [
        {
          "aggregation": "count",
          "interval": "5m",
          "type": "timeseries"
        }
      ],
      "filter": {
        "from": "now-15m",
        "query": "*",
        "to": "now"
      }
    },
    "type": "aggregate_request"
  }
}
EOF
                        
##### 

```go
// Aggregate spans returns "OK" response

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
	body := datadogV2.SpansAggregateRequest{
		Data: &datadogV2.SpansAggregateData{
			Attributes: &datadogV2.SpansAggregateRequestAttributes{
				Compute: []datadogV2.SpansCompute{
					{
						Aggregation: datadogV2.SPANSAGGREGATIONFUNCTION_COUNT,
						Interval:    datadog.PtrString("5m"),
						Type:        datadogV2.SPANSCOMPUTETYPE_TIMESERIES.Ptr(),
					},
				},
				Filter: &datadogV2.SpansQueryFilter{
					From:  datadog.PtrString("now-15m"),
					Query: datadog.PtrString("*"),
					To:    datadog.PtrString("now"),
				},
			},
			Type: datadogV2.SPANSAGGREGATEREQUESTTYPE_AGGREGATE_REQUEST.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSpansApi(apiClient)
	resp, r, err := api.AggregateSpans(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpansApi.AggregateSpans`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SpansApi.AggregateSpans`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Aggregate spans returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansApi;
import com.datadog.api.client.v2.model.SpansAggregateData;
import com.datadog.api.client.v2.model.SpansAggregateRequest;
import com.datadog.api.client.v2.model.SpansAggregateRequestAttributes;
import com.datadog.api.client.v2.model.SpansAggregateRequestType;
import com.datadog.api.client.v2.model.SpansAggregateResponse;
import com.datadog.api.client.v2.model.SpansAggregationFunction;
import com.datadog.api.client.v2.model.SpansCompute;
import com.datadog.api.client.v2.model.SpansComputeType;
import com.datadog.api.client.v2.model.SpansQueryFilter;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansApi apiInstance = new SpansApi(defaultClient);

    SpansAggregateRequest body =
        new SpansAggregateRequest()
            .data(
                new SpansAggregateData()
                    .attributes(
                        new SpansAggregateRequestAttributes()
                            .compute(
                                Collections.singletonList(
                                    new SpansCompute()
                                        .aggregation(SpansAggregationFunction.COUNT)
                                        .interval("5m")
                                        .type(SpansComputeType.TIMESERIES)))
                            .filter(new SpansQueryFilter().from("now-15m").query("*").to("now")))
                    .type(SpansAggregateRequestType.AGGREGATE_REQUEST));

    try {
      SpansAggregateResponse result = apiInstance.aggregateSpans(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansApi#aggregateSpans");
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

```python
"""
Aggregate spans returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi
from datadog_api_client.v2.model.spans_aggregate_data import SpansAggregateData
from datadog_api_client.v2.model.spans_aggregate_request import SpansAggregateRequest
from datadog_api_client.v2.model.spans_aggregate_request_attributes import SpansAggregateRequestAttributes
from datadog_api_client.v2.model.spans_aggregate_request_type import SpansAggregateRequestType
from datadog_api_client.v2.model.spans_aggregation_function import SpansAggregationFunction
from datadog_api_client.v2.model.spans_compute import SpansCompute
from datadog_api_client.v2.model.spans_compute_type import SpansComputeType
from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

body = SpansAggregateRequest(
    data=SpansAggregateData(
        attributes=SpansAggregateRequestAttributes(
            compute=[
                SpansCompute(
                    aggregation=SpansAggregationFunction.COUNT,
                    interval="5m",
                    type=SpansComputeType.TIMESERIES,
                ),
            ],
            filter=SpansQueryFilter(
                _from="now-15m",
                query="*",
                to="now",
            ),
        ),
        type=SpansAggregateRequestType.AGGREGATE_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansApi(api_client)
    response = api_instance.aggregate_spans(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Aggregate spans returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansAPI.new

body = DatadogAPIClient::V2::SpansAggregateRequest.new({
  data: DatadogAPIClient::V2::SpansAggregateData.new({
    attributes: DatadogAPIClient::V2::SpansAggregateRequestAttributes.new({
      compute: [
        DatadogAPIClient::V2::SpansCompute.new({
          aggregation: DatadogAPIClient::V2::SpansAggregationFunction::COUNT,
          interval: "5m",
          type: DatadogAPIClient::V2::SpansComputeType::TIMESERIES,
        }),
      ],
      filter: DatadogAPIClient::V2::SpansQueryFilter.new({
        from: "now-15m",
        query: "*",
        to: "now",
      }),
    }),
    type: DatadogAPIClient::V2::SpansAggregateRequestType::AGGREGATE_REQUEST,
  }),
})
p api_instance.aggregate_spans(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Aggregate spans returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans::SpansAPI;
use datadog_api_client::datadogV2::model::SpansAggregateData;
use datadog_api_client::datadogV2::model::SpansAggregateRequest;
use datadog_api_client::datadogV2::model::SpansAggregateRequestAttributes;
use datadog_api_client::datadogV2::model::SpansAggregateRequestType;
use datadog_api_client::datadogV2::model::SpansAggregationFunction;
use datadog_api_client::datadogV2::model::SpansCompute;
use datadog_api_client::datadogV2::model::SpansComputeType;
use datadog_api_client::datadogV2::model::SpansQueryFilter;

#[tokio::main]
async fn main() {
    let body = SpansAggregateRequest::new().data(
        SpansAggregateData::new()
            .attributes(
                SpansAggregateRequestAttributes::new()
                    .compute(vec![SpansCompute::new(SpansAggregationFunction::COUNT)
                        .interval("5m".to_string())
                        .type_(SpansComputeType::TIMESERIES)])
                    .filter(
                        SpansQueryFilter::new()
                            .from("now-15m".to_string())
                            .query("*".to_string())
                            .to("now".to_string()),
                    ),
            )
            .type_(SpansAggregateRequestType::AGGREGATE_REQUEST),
    );
    let configuration = datadog::Configuration::new();
    let api = SpansAPI::with_config(configuration);
    let resp = api.aggregate_spans(body).await;
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
 * Aggregate spans returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansApi(configuration);

const params: v2.SpansApiAggregateSpansRequest = {
  body: {
    data: {
      attributes: {
        compute: [
          {
            aggregation: "count",
            interval: "5m",
            type: "timeseries",
          },
        ],
        filter: {
          from: "now-15m",
          query: "*",
          to: "now",
        },
      },
      type: "aggregate_request",
    },
  },
};

apiInstance
  .aggregateSpans(params)
  .then((data: v2.SpansAggregateResponse) => {
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
