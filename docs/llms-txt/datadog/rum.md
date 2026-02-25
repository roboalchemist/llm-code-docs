# Source: https://docs.datadoghq.com/api/latest/rum.md

---
title: RUM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > RUM
---

# RUM

Manage your Real User Monitoring (RUM) applications, and search or aggregate your RUM events over HTTP. See the [RUM & Session Replay page](https://docs.datadoghq.com/real_user_monitoring/) for more information

## Search RUM events{% #search-rum-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/rum/events/search |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/rum/events/search |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/rum/events/search      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/rum/events/search      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/rum/events/search     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/rum/events/search |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/rum/events/search |

### Overview



List endpoint returns RUM events that match a RUM search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to build complex RUM events filtering and search.
This endpoint requires the `rum_apps_read` permission.


### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field       | Type   | Description                                                                                                                                                                                                                                                                   |
| ------------ | ----------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | filter      | object | The search and filter query settings.                                                                                                                                                                                                                                         |
| filter       | from        | string | The minimum time for the requested events; supports date (in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format with full date, hours, minutes, and the `Z` UTC indicator - seconds and fractional seconds are optional), math, and regular timestamps (in milliseconds). |
| filter       | query       | string | The search query following the RUM search syntax.                                                                                                                                                                                                                             |
| filter       | to          | string | The maximum time for the requested events; supports date (in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format with full date, hours, minutes, and the `Z` UTC indicator - seconds and fractional seconds are optional), math, and regular timestamps (in milliseconds). |
|              | options     | object | Global query options that are used during the query. Note: Only supply timezone or time offset, not both. Otherwise, the query fails.                                                                                                                                         |
| options      | time_offset | int64  | The time offset (in seconds) to apply to the query.                                                                                                                                                                                                                           |
| options      | timezone    | string | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).                                                                                                                                     |
|              | page        | object | Paging attributes for listing events.                                                                                                                                                                                                                                         |
| page         | cursor      | string | List following results with a cursor provided in the previous query.                                                                                                                                                                                                          |
| page         | limit       | int32  | Maximum number of events in the response.                                                                                                                                                                                                                                     |
|              | sort        | enum   | Sort parameters when querying events. Allowed enum values: `timestamp,-timestamp`                                                                                                                                                                                             |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "filter": {
    "from": "now-15m",
    "query": "@type:session AND @session.type:user",
    "to": "now"
  },
  "options": {
    "time_offset": 0,
    "timezone": "GMT"
  },
  "page": {
    "limit": 25
  },
  "sort": "timestamp"
}
```text

#####

```json
{
  "filter": {
    "from": "now-15m",
    "query": "@type:session AND @session.type:user",
    "to": "now"
  },
  "options": {
    "time_offset": 0,
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
```text

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all events matching the request and pagination information.

| Parent field | Field      | Type      | Description                                                                                                                                                            |
| ------------ | ---------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | [object]  | Array of events matching the request.                                                                                                                                  |
| data         | attributes | object    | JSON object containing all event attributes and their associated values.                                                                                               |
| attributes   | attributes | object    | JSON object of attributes from RUM events.                                                                                                                             |
| attributes   | service    | string    | The name of the application or service generating RUM events. It is used to switch from RUM to APM, so make sure you define the same value when you use both products. |
| attributes   | tags       | [string]  | Array of tags associated with your event.                                                                                                                              |
| attributes   | timestamp  | date-time | Timestamp of your event.                                                                                                                                               |
| data         | id         | string    | Unique ID of the event.                                                                                                                                                |
| data         | type       | enum      | Type of the event. Allowed enum values: `rum`                                                                                                                          |
|              | links      | object    | Links attributes.                                                                                                                                                      |
| links        | next       | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                      |
|              | meta       | object    | The metadata associated with a request.                                                                                                                                |
| meta         | elapsed    | int64     | The time elapsed in milliseconds.                                                                                                                                      |
| meta         | page       | object    | Paging attributes.                                                                                                                                                     |
| page         | after      | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`.                              |
| meta         | request_id | string    | The identifier of the request.                                                                                                                                         |
| meta         | status     | enum      | The status of the response. Allowed enum values: `done,timeout`                                                                                                        |
| meta         | warnings   | [object]  | A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response.                                                 |
| warnings     | code       | string    | A unique code for this type of warning.                                                                                                                                |
| warnings     | detail     | string    | A detailed explanation of this specific warning.                                                                                                                       |
| warnings     | title      | string    | A short human-readable summary of the warning.                                                                                                                         |

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
        "service": "web-app",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "rum"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/rum/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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
```text

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
```text

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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "query": "@type:session AND @session.type:user",
    "to": "now"
  },
  "options": {
    "time_offset": 0,
    "timezone": "GMT"
  },
  "page": {
    "limit": 25
  },
  "sort": "timestamp"
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "query": "@type:session AND @session.type:user",
    "to": "now"
  },
  "options": {
    "time_offset": 0,
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
EOF

#####

```go
// Search RUM events returns "OK" response

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
    body := datadogV2.RUMSearchEventsRequest{
        Filter: &datadogV2.RUMQueryFilter{
            From:  datadog.PtrString("now-15m"),
            Query: datadog.PtrString("@type:session AND @session.type:user"),
            To:    datadog.PtrString("now"),
        },
        Options: &datadogV2.RUMQueryOptions{
            TimeOffset: datadog.PtrInt64(0),
            Timezone:   datadog.PtrString("GMT"),
        },
        Page: &datadogV2.RUMQueryPageOptions{
            Limit: datadog.PtrInt32(25),
        },
        Sort: datadogV2.RUMSORT_TIMESTAMP_ASCENDING.Ptr(),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.SearchRUMEvents(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.SearchRUMEvents`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.SearchRUMEvents`:\n%s\n", responseContent)
}
```text

#####

```go
// Search RUM events returns "OK" response with pagination

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
    body := datadogV2.RUMSearchEventsRequest{
        Filter: &datadogV2.RUMQueryFilter{
            From:  datadog.PtrString("now-15m"),
            Query: datadog.PtrString("@type:session AND @session.type:user"),
            To:    datadog.PtrString("now"),
        },
        Options: &datadogV2.RUMQueryOptions{
            TimeOffset: datadog.PtrInt64(0),
            Timezone:   datadog.PtrString("GMT"),
        },
        Page: &datadogV2.RUMQueryPageOptions{
            Limit: datadog.PtrInt32(2),
        },
        Sort: datadogV2.RUMSORT_TIMESTAMP_ASCENDING.Ptr(),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, _ := api.SearchRUMEventsWithPagination(ctx, body)

    for paginationResult := range resp {
        if paginationResult.Error != nil {
            fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.SearchRUMEvents`: %v\n", paginationResult.Error)
        }
        responseContent, _ := json.MarshalIndent(paginationResult.Item, "", "  ")
        fmt.Fprintf(os.Stdout, "%s\n", responseContent)
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Search RUM events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMEventsResponse;
import com.datadog.api.client.v2.model.RUMQueryFilter;
import com.datadog.api.client.v2.model.RUMQueryOptions;
import com.datadog.api.client.v2.model.RUMQueryPageOptions;
import com.datadog.api.client.v2.model.RUMSearchEventsRequest;
import com.datadog.api.client.v2.model.RUMSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    RUMSearchEventsRequest body =
        new RUMSearchEventsRequest()
            .filter(
                new RUMQueryFilter()
                    .from("now-15m")
                    .query("@type:session AND @session.type:user")
                    .to("now"))
            .options(new RUMQueryOptions().timeOffset(0L).timezone("GMT"))
            .page(new RUMQueryPageOptions().limit(25))
            .sort(RUMSort.TIMESTAMP_ASCENDING);

    try {
      RUMEventsResponse result = apiInstance.searchRUMEvents(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#searchRUMEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#####

```java
// Search RUM events returns "OK" response with pagination

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.PaginationIterable;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMEvent;
import com.datadog.api.client.v2.model.RUMQueryFilter;
import com.datadog.api.client.v2.model.RUMQueryOptions;
import com.datadog.api.client.v2.model.RUMQueryPageOptions;
import com.datadog.api.client.v2.model.RUMSearchEventsRequest;
import com.datadog.api.client.v2.model.RUMSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    RUMSearchEventsRequest body =
        new RUMSearchEventsRequest()
            .filter(
                new RUMQueryFilter()
                    .from("now-15m")
                    .query("@type:session AND @session.type:user")
                    .to("now"))
            .options(new RUMQueryOptions().timeOffset(0L).timezone("GMT"))
            .page(new RUMQueryPageOptions().limit(2))
            .sort(RUMSort.TIMESTAMP_ASCENDING);

    try {
      PaginationIterable<RUMEvent> iterable = apiInstance.searchRUMEventsWithPagination(body);

      for (RUMEvent item : iterable) {
        System.out.println(item);
      }
    } catch (RuntimeException e) {
      System.err.println("Exception when calling RumApi#searchRUMEventsWithPagination");
      System.err.println("Reason: " + e.getMessage());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
"""
Search RUM events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_query_filter import RUMQueryFilter
from datadog_api_client.v2.model.rum_query_options import RUMQueryOptions
from datadog_api_client.v2.model.rum_query_page_options import RUMQueryPageOptions
from datadog_api_client.v2.model.rum_search_events_request import RUMSearchEventsRequest
from datadog_api_client.v2.model.rum_sort import RUMSort

body = RUMSearchEventsRequest(
    filter=RUMQueryFilter(
        _from="now-15m",
        query="@type:session AND @session.type:user",
        to="now",
    ),
    options=RUMQueryOptions(
        time_offset=0,
        timezone="GMT",
    ),
    page=RUMQueryPageOptions(
        limit=25,
    ),
    sort=RUMSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.search_rum_events(body=body)

    print(response)
```text

#####

```python
"""
Search RUM events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_query_filter import RUMQueryFilter
from datadog_api_client.v2.model.rum_query_options import RUMQueryOptions
from datadog_api_client.v2.model.rum_query_page_options import RUMQueryPageOptions
from datadog_api_client.v2.model.rum_search_events_request import RUMSearchEventsRequest
from datadog_api_client.v2.model.rum_sort import RUMSort

body = RUMSearchEventsRequest(
    filter=RUMQueryFilter(
        _from="now-15m",
        query="@type:session AND @session.type:user",
        to="now",
    ),
    options=RUMQueryOptions(
        time_offset=0,
        timezone="GMT",
    ),
    page=RUMQueryPageOptions(
        limit=2,
    ),
    sort=RUMSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    items = api_instance.search_rum_events_with_pagination(body=body)
    for item in items:
        print(item)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Search RUM events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

body = DatadogAPIClient::V2::RUMSearchEventsRequest.new({
  filter: DatadogAPIClient::V2::RUMQueryFilter.new({
    from: "now-15m",
    query: "@type:session AND @session.type:user",
    to: "now",
  }),
  options: DatadogAPIClient::V2::RUMQueryOptions.new({
    time_offset: 0,
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::RUMQueryPageOptions.new({
    limit: 25,
  }),
  sort: DatadogAPIClient::V2::RUMSort::TIMESTAMP_ASCENDING,
})
p api_instance.search_rum_events(body)
```text

#####

```ruby
# Search RUM events returns "OK" response with pagination

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

body = DatadogAPIClient::V2::RUMSearchEventsRequest.new({
  filter: DatadogAPIClient::V2::RUMQueryFilter.new({
    from: "now-15m",
    query: "@type:session AND @session.type:user",
    to: "now",
  }),
  options: DatadogAPIClient::V2::RUMQueryOptions.new({
    time_offset: 0,
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::RUMQueryPageOptions.new({
    limit: 2,
  }),
  sort: DatadogAPIClient::V2::RUMSort::TIMESTAMP_ASCENDING,
})
api_instance.search_rum_events_with_pagination(body) { |item| puts item }
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Search RUM events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;
use datadog_api_client::datadogV2::model::RUMQueryFilter;
use datadog_api_client::datadogV2::model::RUMQueryOptions;
use datadog_api_client::datadogV2::model::RUMQueryPageOptions;
use datadog_api_client::datadogV2::model::RUMSearchEventsRequest;
use datadog_api_client::datadogV2::model::RUMSort;

#[tokio::main]
async fn main() {
    let body = RUMSearchEventsRequest::new()
        .filter(
            RUMQueryFilter::new()
                .from("now-15m".to_string())
                .query("@type:session AND @session.type:user".to_string())
                .to("now".to_string()),
        )
        .options(
            RUMQueryOptions::new()
                .time_offset(0)
                .timezone("GMT".to_string()),
        )
        .page(RUMQueryPageOptions::new().limit(25))
        .sort(RUMSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api.search_rum_events(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#####

```rust
// Search RUM events returns "OK" response with pagination
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;
use datadog_api_client::datadogV2::model::RUMQueryFilter;
use datadog_api_client::datadogV2::model::RUMQueryOptions;
use datadog_api_client::datadogV2::model::RUMQueryPageOptions;
use datadog_api_client::datadogV2::model::RUMSearchEventsRequest;
use datadog_api_client::datadogV2::model::RUMSort;
use futures_util::pin_mut;
use futures_util::stream::StreamExt;

#[tokio::main]
async fn main() {
    let body = RUMSearchEventsRequest::new()
        .filter(
            RUMQueryFilter::new()
                .from("now-15m".to_string())
                .query("@type:session AND @session.type:user".to_string())
                .to("now".to_string()),
        )
        .options(
            RUMQueryOptions::new()
                .time_offset(0)
                .timezone("GMT".to_string()),
        )
        .page(RUMQueryPageOptions::new().limit(2))
        .sort(RUMSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let response = api.search_rum_events_with_pagination(body);
    pin_mut!(response);
    while let Some(resp) = response.next().await {
        if let Ok(value) = resp {
            println!("{:#?}", value);
        } else {
            println!("{:#?}", resp.unwrap_err());
        }
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Search RUM events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

const params: v2.RUMApiSearchRUMEventsRequest = {
  body: {
    filter: {
      from: "now-15m",
      query: "@type:session AND @session.type:user",
      to: "now",
    },
    options: {
      timeOffset: 0,
      timezone: "GMT",
    },
    page: {
      limit: 25,
    },
    sort: "timestamp",
  },
};

apiInstance
  .searchRUMEvents(params)
  .then((data: v2.RUMEventsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#####

```typescript
/**
 * Search RUM events returns "OK" response with pagination
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

const params: v2.RUMApiSearchRUMEventsRequest = {
  body: {
    filter: {
      from: "now-15m",
      query: "@type:session AND @session.type:user",
      to: "now",
    },
    options: {
      timeOffset: 0,
      timezone: "GMT",
    },
    page: {
      limit: 2,
    },
    sort: "timestamp",
  },
};

(async () => {
  try {
    for await (const item of apiInstance.searchRUMEventsWithPagination(
      params
    )) {
      console.log(item);
    }
  } catch (error) {
    console.error(error);
  }
})();
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get a list of RUM events{% #get-a-list-of-rum-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/events |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/events |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/events      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/events      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/events     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/events |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/events |

### Overview



List endpoint returns events that match a RUM search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to see your latest RUM events.
This endpoint requires the `rum_apps_read` permission.


### Arguments

#### Query Strings

| Name          | Type    | Description                                                             |
| ------------- | ------- | ----------------------------------------------------------------------- |
| filter[query] | string  | Search query following RUM syntax.                                      |
| filter[from]  | string  | Minimum timestamp for requested events.                                 |
| filter[to]    | string  | Maximum timestamp for requested events.                                 |
| sort          | enum    | Order of events in results.Allowed enum values: `timestamp, -timestamp` |
| page[cursor]  | string  | List following results with a cursor provided in the previous query.    |
| page[limit]   | integer | Maximum number of events in the response.                               |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all events matching the request and pagination information.

| Parent field | Field      | Type      | Description                                                                                                                                                            |
| ------------ | ---------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | [object]  | Array of events matching the request.                                                                                                                                  |
| data         | attributes | object    | JSON object containing all event attributes and their associated values.                                                                                               |
| attributes   | attributes | object    | JSON object of attributes from RUM events.                                                                                                                             |
| attributes   | service    | string    | The name of the application or service generating RUM events. It is used to switch from RUM to APM, so make sure you define the same value when you use both products. |
| attributes   | tags       | [string]  | Array of tags associated with your event.                                                                                                                              |
| attributes   | timestamp  | date-time | Timestamp of your event.                                                                                                                                               |
| data         | id         | string    | Unique ID of the event.                                                                                                                                                |
| data         | type       | enum      | Type of the event. Allowed enum values: `rum`                                                                                                                          |
|              | links      | object    | Links attributes.                                                                                                                                                      |
| links        | next       | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                      |
|              | meta       | object    | The metadata associated with a request.                                                                                                                                |
| meta         | elapsed    | int64     | The time elapsed in milliseconds.                                                                                                                                      |
| meta         | page       | object    | Paging attributes.                                                                                                                                                     |
| page         | after      | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`.                              |
| meta         | request_id | string    | The identifier of the request.                                                                                                                                         |
| meta         | status     | enum      | The status of the response. Allowed enum values: `done,timeout`                                                                                                        |
| meta         | warnings   | [object]  | A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response.                                                 |
| warnings     | code       | string    | A unique code for this type of warning.                                                                                                                                |
| warnings     | detail     | string    | A detailed explanation of this specific warning.                                                                                                                       |
| warnings     | title      | string    | A short human-readable summary of the warning.                                                                                                                         |

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
        "service": "web-app",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "rum"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/rum/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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
```text

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
```text

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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a list of RUM events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.list_rum_events()

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a list of RUM events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new
p api_instance.list_rum_events()
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a list of RUM events returns "OK" response

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
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.ListRUMEvents(ctx, *datadogV2.NewListRUMEventsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.ListRUMEvents`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.ListRUMEvents`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a list of RUM events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMEventsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    try {
      RUMEventsResponse result = apiInstance.listRUMEvents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#listRUMEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get a list of RUM events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::ListRUMEventsOptionalParams;
use datadog_api_client::datadogV2::api_rum::RUMAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api
        .list_rum_events(ListRUMEventsOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get a list of RUM events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

apiInstance
  .listRUMEvents()
  .then((data: v2.RUMEventsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Aggregate RUM events{% #aggregate-rum-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/rum/analytics/aggregate |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/rum/analytics/aggregate |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/rum/analytics/aggregate      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/rum/analytics/aggregate      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/rum/analytics/aggregate     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/rum/analytics/aggregate |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/rum/analytics/aggregate |

### Overview

The API endpoint to aggregate RUM events into buckets of computed metrics and timeseries. This endpoint requires the `rum_apps_read` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                         | Type          | Description                                                                                                                                                                                                                                                                   |
| ------------ | ----------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | compute                       | [object]      | The list of metrics or timeseries to compute for the retrieved buckets.                                                                                                                                                                                                       |
| compute      | aggregation [*required*] | enum          | An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`                                                                                                                                                             |
| compute      | interval                      | string        | The time buckets' size (only used for type=timeseries) Defaults to a resolution of 150 points.                                                                                                                                                                                |
| compute      | metric                        | string        | The metric to use.                                                                                                                                                                                                                                                            |
| compute      | type                          | enum          | The type of compute. Allowed enum values: `timeseries,total`                                                                                                                                                                                                                  |
|              | filter                        | object        | The search and filter query settings.                                                                                                                                                                                                                                         |
| filter       | from                          | string        | The minimum time for the requested events; supports date (in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format with full date, hours, minutes, and the `Z` UTC indicator - seconds and fractional seconds are optional), math, and regular timestamps (in milliseconds). |
| filter       | query                         | string        | The search query following the RUM search syntax.                                                                                                                                                                                                                             |
| filter       | to                            | string        | The maximum time for the requested events; supports date (in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format with full date, hours, minutes, and the `Z` UTC indicator - seconds and fractional seconds are optional), math, and regular timestamps (in milliseconds). |
|              | group_by                      | [object]      | The rules for the group by.                                                                                                                                                                                                                                                   |
| group_by     | facet [*required*]       | string        | The name of the facet to use (required).                                                                                                                                                                                                                                      |
| group_by     | histogram                     | object        | Used to perform a histogram computation (only for measure facets). Note: At most 100 buckets are allowed, the number of buckets is (max - min)/interval.                                                                                                                      |
| histogram    | interval [*required*]    | double        | The bin size of the histogram buckets.                                                                                                                                                                                                                                        |
| histogram    | max [*required*]         | double        | The maximum value for the measure used in the histogram (values greater than this one are filtered out).                                                                                                                                                                      |
| histogram    | min [*required*]         | double        | The minimum value for the measure used in the histogram (values smaller than this one are filtered out).                                                                                                                                                                      |
| group_by     | limit                         | int64         | The maximum buckets to return for this group-by.                                                                                                                                                                                                                              |
| group_by     | missing                       |  <oneOf> | The value to use for logs that don't have the facet used to group by.                                                                                                                                                                                                         |
| missing      | Option 1                      | string        | The missing value to use if there is string valued facet.                                                                                                                                                                                                                     |
| missing      | Option 2                      | double        | The missing value to use if there is a number valued facet.                                                                                                                                                                                                                   |
| group_by     | sort                          | object        | A sort rule.                                                                                                                                                                                                                                                                  |
| sort         | aggregation                   | enum          | An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`                                                                                                                                                             |
| sort         | metric                        | string        | The metric to sort by (only used for `type=measure`).                                                                                                                                                                                                                         |
| sort         | order                         | enum          | The order to use, ascending or descending. Allowed enum values: `asc,desc`                                                                                                                                                                                                    |
| sort         | type                          | enum          | The type of sorting algorithm. Allowed enum values: `alphabetical,measure`                                                                                                                                                                                                    |
| group_by     | total                         |  <oneOf> | A resulting object to put the given computes in over all the matching records.                                                                                                                                                                                                |
| total        | Option 1                      | boolean       | If set to true, creates an additional bucket labeled "$facet_total".                                                                                                                                                                                                          |
| total        | Option 2                      | string        | A string to use as the key value for the total bucket.                                                                                                                                                                                                                        |
| total        | Option 3                      | double        | A number to use as the key value for the total bucket.                                                                                                                                                                                                                        |
|              | options                       | object        | Global query options that are used during the query. Note: Only supply timezone or time offset, not both. Otherwise, the query fails.                                                                                                                                         |
| options      | time_offset                   | int64         | The time offset (in seconds) to apply to the query.                                                                                                                                                                                                                           |
| options      | timezone                      | string        | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).                                                                                                                                     |
|              | page                          | object        | Paging attributes for listing events.                                                                                                                                                                                                                                         |
| page         | cursor                        | string        | List following results with a cursor provided in the previous query.                                                                                                                                                                                                          |
| page         | limit                         | int32         | Maximum number of events in the response.                                                                                                                                                                                                                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "compute": [
    {
      "aggregation": "pc90",
      "metric": "@view.time_spent",
      "type": "total"
    }
  ],
  "filter": {
    "from": "now-15m",
    "query": "@type:view AND @session.type:user",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "@view.time_spent",
      "limit": 10,
      "total": false
    }
  ],
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 25
  }
}
```text

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object for the RUM events aggregate API endpoint.

| Parent field         | Field      | Type          | Description                                                                                                                               |
| -------------------- | ---------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data       | object        | The query results.                                                                                                                        |
| data                 | buckets    | [object]      | The list of matching buckets, one item per bucket.                                                                                        |
| buckets              | by         | object        | The key-value pairs for each group-by.                                                                                                    |
| additionalProperties | <any-key>  | string        | The values for each group-by.                                                                                                             |
| buckets              | computes   | object        | A map of the metric name to value for regular compute, or a list of values for a timeseries.                                              |
| additionalProperties | <any-key>  |  <oneOf> | A bucket value, can be either a timeseries or a single value.                                                                             |
| <any-key>            | Option 1   | string        | A single string value.                                                                                                                    |
| <any-key>            | Option 2   | double        | A single number value.                                                                                                                    |
| <any-key>            | Option 3   | [object]      | A timeseries array.                                                                                                                       |
| Option 3             | time       | date-time     | The time value for this point.                                                                                                            |
| Option 3             | value      | double        | The value for this point.                                                                                                                 |
|                      | links      | object        | Links attributes.                                                                                                                         |
| links                | next       | string        | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                         |
|                      | meta       | object        | The metadata associated with a request.                                                                                                   |
| meta                 | elapsed    | int64         | The time elapsed in milliseconds.                                                                                                         |
| meta                 | page       | object        | Paging attributes.                                                                                                                        |
| page                 | after      | string        | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`. |
| meta                 | request_id | string        | The identifier of the request.                                                                                                            |
| meta                 | status     | enum          | The status of the response. Allowed enum values: `done,timeout`                                                                           |
| meta                 | warnings   | [object]      | A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response.                    |
| warnings             | code       | string        | A unique code for this type of warning.                                                                                                   |
| warnings             | detail     | string        | A detailed explanation of this specific warning.                                                                                          |
| warnings             | title      | string        | A short human-readable summary of the warning.                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "buckets": [
      {
        "by": {
          "<any-key>": "string"
        },
        "computes": {
          "<any-key>": {
            "description": "undefined",
            "type": "undefined"
          }
        }
      }
    ]
  },
  "links": {
    "next": "https://app.datadoghq.com/api/v2/rum/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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
```text

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
```text

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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/analytics/aggregate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "compute": [
    {
      "aggregation": "pc90",
      "metric": "@view.time_spent",
      "type": "total"
    }
  ],
  "filter": {
    "from": "now-15m",
    "query": "@type:view AND @session.type:user",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "@view.time_spent",
      "limit": 10,
      "total": false
    }
  ],
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 25
  }
}
EOF

#####

```go
// Aggregate RUM events returns "OK" response

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
    body := datadogV2.RUMAggregateRequest{
        Compute: []datadogV2.RUMCompute{
            {
                Aggregation: datadogV2.RUMAGGREGATIONFUNCTION_PERCENTILE_90,
                Metric:      datadog.PtrString("@view.time_spent"),
                Type:        datadogV2.RUMCOMPUTETYPE_TOTAL.Ptr(),
            },
        },
        Filter: &datadogV2.RUMQueryFilter{
            From:  datadog.PtrString("now-15m"),
            Query: datadog.PtrString("@type:view AND @session.type:user"),
            To:    datadog.PtrString("now"),
        },
        GroupBy: []datadogV2.RUMGroupBy{
            {
                Facet: "@view.time_spent",
                Limit: datadog.PtrInt64(10),
                Total: &datadogV2.RUMGroupByTotal{
                    RUMGroupByTotalBoolean: datadog.PtrBool(false)},
            },
        },
        Options: &datadogV2.RUMQueryOptions{
            Timezone: datadog.PtrString("GMT"),
        },
        Page: &datadogV2.RUMQueryPageOptions{
            Limit: datadog.PtrInt32(25),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.AggregateRUMEvents(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.AggregateRUMEvents`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.AggregateRUMEvents`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Aggregate RUM events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMAggregateRequest;
import com.datadog.api.client.v2.model.RUMAggregationFunction;
import com.datadog.api.client.v2.model.RUMAnalyticsAggregateResponse;
import com.datadog.api.client.v2.model.RUMCompute;
import com.datadog.api.client.v2.model.RUMComputeType;
import com.datadog.api.client.v2.model.RUMGroupBy;
import com.datadog.api.client.v2.model.RUMGroupByTotal;
import com.datadog.api.client.v2.model.RUMQueryFilter;
import com.datadog.api.client.v2.model.RUMQueryOptions;
import com.datadog.api.client.v2.model.RUMQueryPageOptions;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    RUMAggregateRequest body =
        new RUMAggregateRequest()
            .compute(
                Collections.singletonList(
                    new RUMCompute()
                        .aggregation(RUMAggregationFunction.PERCENTILE_90)
                        .metric("@view.time_spent")
                        .type(RUMComputeType.TOTAL)))
            .filter(
                new RUMQueryFilter()
                    .from("now-15m")
                    .query("@type:view AND @session.type:user")
                    .to("now"))
            .groupBy(
                Collections.singletonList(
                    new RUMGroupBy()
                        .facet("@view.time_spent")
                        .limit(10L)
                        .total(new RUMGroupByTotal(false))))
            .options(new RUMQueryOptions().timezone("GMT"))
            .page(new RUMQueryPageOptions().limit(25));

    try {
      RUMAnalyticsAggregateResponse result = apiInstance.aggregateRUMEvents(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#aggregateRUMEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
"""
Aggregate RUM events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_aggregate_request import RUMAggregateRequest
from datadog_api_client.v2.model.rum_aggregation_function import RUMAggregationFunction
from datadog_api_client.v2.model.rum_compute import RUMCompute
from datadog_api_client.v2.model.rum_compute_type import RUMComputeType
from datadog_api_client.v2.model.rum_group_by import RUMGroupBy
from datadog_api_client.v2.model.rum_query_filter import RUMQueryFilter
from datadog_api_client.v2.model.rum_query_options import RUMQueryOptions
from datadog_api_client.v2.model.rum_query_page_options import RUMQueryPageOptions

body = RUMAggregateRequest(
    compute=[
        RUMCompute(
            aggregation=RUMAggregationFunction.PERCENTILE_90,
            metric="@view.time_spent",
            type=RUMComputeType.TOTAL,
        ),
    ],
    filter=RUMQueryFilter(
        _from="now-15m",
        query="@type:view AND @session.type:user",
        to="now",
    ),
    group_by=[
        RUMGroupBy(
            facet="@view.time_spent",
            limit=10,
            total=False,
        ),
    ],
    options=RUMQueryOptions(
        timezone="GMT",
    ),
    page=RUMQueryPageOptions(
        limit=25,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.aggregate_rum_events(body=body)

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Aggregate RUM events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

body = DatadogAPIClient::V2::RUMAggregateRequest.new({
  compute: [
    DatadogAPIClient::V2::RUMCompute.new({
      aggregation: DatadogAPIClient::V2::RUMAggregationFunction::PERCENTILE_90,
      metric: "@view.time_spent",
      type: DatadogAPIClient::V2::RUMComputeType::TOTAL,
    }),
  ],
  filter: DatadogAPIClient::V2::RUMQueryFilter.new({
    from: "now-15m",
    query: "@type:view AND @session.type:user",
    to: "now",
  }),
  group_by: [
    DatadogAPIClient::V2::RUMGroupBy.new({
      facet: "@view.time_spent",
      limit: 10,
      total: false,
    }),
  ],
  options: DatadogAPIClient::V2::RUMQueryOptions.new({
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::RUMQueryPageOptions.new({
    limit: 25,
  }),
})
p api_instance.aggregate_rum_events(body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Aggregate RUM events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;
use datadog_api_client::datadogV2::model::RUMAggregateRequest;
use datadog_api_client::datadogV2::model::RUMAggregationFunction;
use datadog_api_client::datadogV2::model::RUMCompute;
use datadog_api_client::datadogV2::model::RUMComputeType;
use datadog_api_client::datadogV2::model::RUMGroupBy;
use datadog_api_client::datadogV2::model::RUMGroupByTotal;
use datadog_api_client::datadogV2::model::RUMQueryFilter;
use datadog_api_client::datadogV2::model::RUMQueryOptions;
use datadog_api_client::datadogV2::model::RUMQueryPageOptions;

#[tokio::main]
async fn main() {
    let body = RUMAggregateRequest::new()
        .compute(vec![RUMCompute::new(RUMAggregationFunction::PERCENTILE_90)
            .metric("@view.time_spent".to_string())
            .type_(RUMComputeType::TOTAL)])
        .filter(
            RUMQueryFilter::new()
                .from("now-15m".to_string())
                .query("@type:view AND @session.type:user".to_string())
                .to("now".to_string()),
        )
        .group_by(vec![RUMGroupBy::new("@view.time_spent".to_string())
            .limit(10)
            .total(RUMGroupByTotal::RUMGroupByTotalBoolean(false))])
        .options(RUMQueryOptions::new().timezone("GMT".to_string()))
        .page(RUMQueryPageOptions::new().limit(25));
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api.aggregate_rum_events(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Aggregate RUM events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

const params: v2.RUMApiAggregateRUMEventsRequest = {
  body: {
    compute: [
      {
        aggregation: "pc90",
        metric: "@view.time_spent",
        type: "total",
      },
    ],
    filter: {
      from: "now-15m",
      query: "@type:view AND @session.type:user",
      to: "now",
    },
    groupBy: [
      {
        facet: "@view.time_spent",
        limit: 10,
        total: false,
      },
    ],
    options: {
      timezone: "GMT",
    },
    page: {
      limit: 25,
    },
  },
};

apiInstance
  .aggregateRUMEvents(params)
  .then((data: v2.RUMAnalyticsAggregateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update a RUM application{% #update-a-rum-application %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/rum/applications/{id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/rum/applications/{id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/rum/applications/{id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/rum/applications/{id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/rum/applications/{id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/rum/applications/{id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/rum/applications/{id} |

### Overview

Update the RUM application with given ID in your organization. This endpoint requires the `rum_apps_write` permission.

### Arguments

#### Path Parameters

| Name                 | Type   | Description         |
| -------------------- | ------ | ------------------- |
| id [*required*] | string | RUM application ID. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                             | Type   | Description                                                                                                                                                    |
| ------------ | --------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]            | object | RUM application update.                                                                                                                                        |
| data         | attributes                        | object | RUM application update attributes.                                                                                                                             |
| attributes   | name                              | string | Name of the RUM application.                                                                                                                                   |
| attributes   | product_analytics_retention_state | enum   | Controls the retention policy for Product Analytics data derived from RUM events. Allowed enum values: `MAX,NONE`                                              |
| attributes   | rum_event_processing_state        | enum   | Configures which RUM events are processed and stored for the application. Allowed enum values: `ALL,ERROR_FOCUSED_MODE,NONE`                                   |
| attributes   | type                              | string | Type of the RUM application. Supported values are `browser`, `ios`, `android`, `react-native`, `flutter`, `roku`, `electron`, `unity`, `kotlin-multiplatform`. |
| data         | id [*required*]              | string | RUM application ID.                                                                                                                                            |
| data         | type [*required*]            | enum   | RUM application update type. Allowed enum values: `rum_application_update`                                                                                     |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "name": "updated_name_for_my_existing_rum_application",
      "type": "browser"
    },
    "id": "abcd1234-0000-0000-abcd-1234abcd5678",
    "type": "rum_application_update"
  }
}
```text

#####

```json
{
  "data": {
    "attributes": {
      "name": "updated_rum_with_product_scales",
      "rum_event_processing_state": "ALL",
      "product_analytics_retention_state": "MAX"
    },
    "id": "abcd1234-0000-0000-abcd-1234abcd5678",
    "type": "rum_application_update"
  }
}
```text

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
RUM application response.

| Parent field                      | Field                               | Type    | Description                                                                                                                                                    |
| --------------------------------- | ----------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                   | data                                | object  | RUM application.                                                                                                                                               |
| data                              | attributes [*required*]        | object  | RUM application attributes.                                                                                                                                    |
| attributes                        | api_key_id                          | int32   | ID of the API key associated with the application.                                                                                                             |
| attributes                        | application_id [*required*]    | string  | ID of the RUM application.                                                                                                                                     |
| attributes                        | client_token [*required*]      | string  | Client token of the RUM application.                                                                                                                           |
| attributes                        | created_at [*required*]        | int64   | Timestamp in ms of the creation date.                                                                                                                          |
| attributes                        | created_by_handle [*required*] | string  | Handle of the creator user.                                                                                                                                    |
| attributes                        | hash                                | string  | Hash of the RUM application. Optional.                                                                                                                         |
| attributes                        | is_active                           | boolean | Indicates if the RUM application is active.                                                                                                                    |
| attributes                        | name [*required*]              | string  | Name of the RUM application.                                                                                                                                   |
| attributes                        | org_id [*required*]            | int32   | Org ID of the RUM application.                                                                                                                                 |
| attributes                        | product_scales                      | object  | Product Scales configuration for the RUM application.                                                                                                          |
| product_scales                    | product_analytics_retention_scale   | object  | Product Analytics retention scale configuration.                                                                                                               |
| product_analytics_retention_scale | last_modified_at                    | int64   | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| product_analytics_retention_scale | state                               | enum    | Controls the retention policy for Product Analytics data derived from RUM events. Allowed enum values: `MAX,NONE`                                              |
| product_scales                    | rum_event_processing_scale          | object  | RUM event processing scale configuration.                                                                                                                      |
| rum_event_processing_scale        | last_modified_at                    | int64   | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| rum_event_processing_scale        | state                               | enum    | Configures which RUM events are processed and stored for the application. Allowed enum values: `ALL,ERROR_FOCUSED_MODE,NONE`                                   |
| attributes                        | type [*required*]              | string  | Type of the RUM application. Supported values are `browser`, `ios`, `android`, `react-native`, `flutter`, `roku`, `electron`, `unity`, `kotlin-multiplatform`. |
| attributes                        | updated_at [*required*]        | int64   | Timestamp in ms of the last update date.                                                                                                                       |
| attributes                        | updated_by_handle [*required*] | string  | Handle of the updater user.                                                                                                                                    |
| data                              | id [*required*]                | string  | RUM application ID.                                                                                                                                            |
| data                              | type [*required*]              | enum    | RUM application response type. Allowed enum values: `rum_application`                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key_id": 123456789,
      "application_id": "abcd1234-0000-0000-abcd-1234abcd5678",
      "client_token": "abcd1234efgh5678ijkl90abcd1234efgh0",
      "created_at": 1659479836169,
      "created_by_handle": "john.doe",
      "hash": "string",
      "is_active": true,
      "name": "my_rum_application",
      "org_id": 999,
      "product_scales": {
        "product_analytics_retention_scale": {
          "last_modified_at": 1747922145974,
          "state": "MAX"
        },
        "rum_event_processing_scale": {
          "last_modified_at": 1721897494108,
          "state": "ALL"
        }
      },
      "type": "browser",
      "updated_at": 1659479836169,
      "updated_by_handle": "jane.doe"
    },
    "id": "abcd1234-0000-0000-abcd-1234abcd5678",
    "type": "rum_application"
  }
}
```text

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
```text

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
```text

{% /tab %}

{% /tab %}

{% tab title="422" %}
Unprocessable Entity.
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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "updated_name_for_my_existing_rum_application",
      "type": "browser"
    },
    "id": "abcd1234-0000-0000-abcd-1234abcd5678",
    "type": "rum_application_update"
  }
}
EOF

#####
                          \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "updated_rum_with_product_scales",
      "rum_event_processing_state": "ALL",
      "product_analytics_retention_state": "MAX"
    },
    "id": "abcd1234-0000-0000-abcd-1234abcd5678",
    "type": "rum_application_update"
  }
}
EOF

#####

```go
// Update a RUM application returns "OK" response

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
    // there is a valid "rum_application" in the system
    RumApplicationDataID := os.Getenv("RUM_APPLICATION_DATA_ID")

    body := datadogV2.RUMApplicationUpdateRequest{
        Data: datadogV2.RUMApplicationUpdate{
            Attributes: &datadogV2.RUMApplicationUpdateAttributes{
                Name: datadog.PtrString("updated_name_for_my_existing_rum_application"),
                Type: datadog.PtrString("browser"),
            },
            Id:   RumApplicationDataID,
            Type: datadogV2.RUMAPPLICATIONUPDATETYPE_RUM_APPLICATION_UPDATE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.UpdateRUMApplication(ctx, RumApplicationDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.UpdateRUMApplication`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.UpdateRUMApplication`:\n%s\n", responseContent)
}
```text

#####

```go
// Update a RUM application with Product Scales returns "OK" response

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
    // there is a valid "rum_application" in the system
    RumApplicationDataID := os.Getenv("RUM_APPLICATION_DATA_ID")

    body := datadogV2.RUMApplicationUpdateRequest{
        Data: datadogV2.RUMApplicationUpdate{
            Attributes: &datadogV2.RUMApplicationUpdateAttributes{
                Name:                           datadog.PtrString("updated_rum_with_product_scales"),
                RumEventProcessingState:        datadogV2.RUMEVENTPROCESSINGSTATE_ALL.Ptr(),
                ProductAnalyticsRetentionState: datadogV2.RUMPRODUCTANALYTICSRETENTIONSTATE_MAX.Ptr(),
            },
            Id:   RumApplicationDataID,
            Type: datadogV2.RUMAPPLICATIONUPDATETYPE_RUM_APPLICATION_UPDATE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.UpdateRUMApplication(ctx, RumApplicationDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.UpdateRUMApplication`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.UpdateRUMApplication`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a RUM application returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMApplicationResponse;
import com.datadog.api.client.v2.model.RUMApplicationUpdate;
import com.datadog.api.client.v2.model.RUMApplicationUpdateAttributes;
import com.datadog.api.client.v2.model.RUMApplicationUpdateRequest;
import com.datadog.api.client.v2.model.RUMApplicationUpdateType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    // there is a valid "rum_application" in the system
    String RUM_APPLICATION_DATA_ID = System.getenv("RUM_APPLICATION_DATA_ID");

    RUMApplicationUpdateRequest body =
        new RUMApplicationUpdateRequest()
            .data(
                new RUMApplicationUpdate()
                    .attributes(
                        new RUMApplicationUpdateAttributes()
                            .name("updated_name_for_my_existing_rum_application")
                            .type("browser"))
                    .id(RUM_APPLICATION_DATA_ID)
                    .type(RUMApplicationUpdateType.RUM_APPLICATION_UPDATE));

    try {
      RUMApplicationResponse result =
          apiInstance.updateRUMApplication(RUM_APPLICATION_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#updateRUMApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#####

```java
// Update a RUM application with Product Scales returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMApplicationResponse;
import com.datadog.api.client.v2.model.RUMApplicationUpdate;
import com.datadog.api.client.v2.model.RUMApplicationUpdateAttributes;
import com.datadog.api.client.v2.model.RUMApplicationUpdateRequest;
import com.datadog.api.client.v2.model.RUMApplicationUpdateType;
import com.datadog.api.client.v2.model.RUMEventProcessingState;
import com.datadog.api.client.v2.model.RUMProductAnalyticsRetentionState;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    // there is a valid "rum_application" in the system
    String RUM_APPLICATION_DATA_ID = System.getenv("RUM_APPLICATION_DATA_ID");

    RUMApplicationUpdateRequest body =
        new RUMApplicationUpdateRequest()
            .data(
                new RUMApplicationUpdate()
                    .attributes(
                        new RUMApplicationUpdateAttributes()
                            .name("updated_rum_with_product_scales")
                            .rumEventProcessingState(RUMEventProcessingState.ALL)
                            .productAnalyticsRetentionState(RUMProductAnalyticsRetentionState.MAX))
                    .id(RUM_APPLICATION_DATA_ID)
                    .type(RUMApplicationUpdateType.RUM_APPLICATION_UPDATE));

    try {
      RUMApplicationResponse result =
          apiInstance.updateRUMApplication(RUM_APPLICATION_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#updateRUMApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
"""
Update a RUM application returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_update import RUMApplicationUpdate
from datadog_api_client.v2.model.rum_application_update_attributes import RUMApplicationUpdateAttributes
from datadog_api_client.v2.model.rum_application_update_request import RUMApplicationUpdateRequest
from datadog_api_client.v2.model.rum_application_update_type import RUMApplicationUpdateType

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

body = RUMApplicationUpdateRequest(
    data=RUMApplicationUpdate(
        attributes=RUMApplicationUpdateAttributes(
            name="updated_name_for_my_existing_rum_application",
            type="browser",
        ),
        id=RUM_APPLICATION_DATA_ID,
        type=RUMApplicationUpdateType.RUM_APPLICATION_UPDATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.update_rum_application(id=RUM_APPLICATION_DATA_ID, body=body)

    print(response)
```text

#####

```python
"""
Update a RUM application with Product Scales returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_update import RUMApplicationUpdate
from datadog_api_client.v2.model.rum_application_update_attributes import RUMApplicationUpdateAttributes
from datadog_api_client.v2.model.rum_application_update_request import RUMApplicationUpdateRequest
from datadog_api_client.v2.model.rum_application_update_type import RUMApplicationUpdateType
from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState
from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

body = RUMApplicationUpdateRequest(
    data=RUMApplicationUpdate(
        attributes=RUMApplicationUpdateAttributes(
            name="updated_rum_with_product_scales",
            rum_event_processing_state=RUMEventProcessingState.ALL,
            product_analytics_retention_state=RUMProductAnalyticsRetentionState.MAX,
        ),
        id=RUM_APPLICATION_DATA_ID,
        type=RUMApplicationUpdateType.RUM_APPLICATION_UPDATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.update_rum_application(id=RUM_APPLICATION_DATA_ID, body=body)

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a RUM application returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = ENV["RUM_APPLICATION_DATA_ID"]

body = DatadogAPIClient::V2::RUMApplicationUpdateRequest.new({
  data: DatadogAPIClient::V2::RUMApplicationUpdate.new({
    attributes: DatadogAPIClient::V2::RUMApplicationUpdateAttributes.new({
      name: "updated_name_for_my_existing_rum_application",
      type: "browser",
    }),
    id: RUM_APPLICATION_DATA_ID,
    type: DatadogAPIClient::V2::RUMApplicationUpdateType::RUM_APPLICATION_UPDATE,
  }),
})
p api_instance.update_rum_application(RUM_APPLICATION_DATA_ID, body)
```text

#####

```ruby
# Update a RUM application with Product Scales returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = ENV["RUM_APPLICATION_DATA_ID"]

body = DatadogAPIClient::V2::RUMApplicationUpdateRequest.new({
  data: DatadogAPIClient::V2::RUMApplicationUpdate.new({
    attributes: DatadogAPIClient::V2::RUMApplicationUpdateAttributes.new({
      name: "updated_rum_with_product_scales",
      rum_event_processing_state: DatadogAPIClient::V2::RUMEventProcessingState::ALL,
      product_analytics_retention_state: DatadogAPIClient::V2::RUMProductAnalyticsRetentionState::MAX,
    }),
    id: RUM_APPLICATION_DATA_ID,
    type: DatadogAPIClient::V2::RUMApplicationUpdateType::RUM_APPLICATION_UPDATE,
  }),
})
p api_instance.update_rum_application(RUM_APPLICATION_DATA_ID, body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update a RUM application returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;
use datadog_api_client::datadogV2::model::RUMApplicationUpdate;
use datadog_api_client::datadogV2::model::RUMApplicationUpdateAttributes;
use datadog_api_client::datadogV2::model::RUMApplicationUpdateRequest;
use datadog_api_client::datadogV2::model::RUMApplicationUpdateType;

#[tokio::main]
async fn main() {
    // there is a valid "rum_application" in the system
    let rum_application_data_id = std::env::var("RUM_APPLICATION_DATA_ID").unwrap();
    let body = RUMApplicationUpdateRequest::new(
        RUMApplicationUpdate::new(
            rum_application_data_id.clone(),
            RUMApplicationUpdateType::RUM_APPLICATION_UPDATE,
        )
        .attributes(
            RUMApplicationUpdateAttributes::new()
                .name("updated_name_for_my_existing_rum_application".to_string())
                .type_("browser".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api
        .update_rum_application(rum_application_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#####

```rust
// Update a RUM application with Product Scales returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;
use datadog_api_client::datadogV2::model::RUMApplicationUpdate;
use datadog_api_client::datadogV2::model::RUMApplicationUpdateAttributes;
use datadog_api_client::datadogV2::model::RUMApplicationUpdateRequest;
use datadog_api_client::datadogV2::model::RUMApplicationUpdateType;
use datadog_api_client::datadogV2::model::RUMEventProcessingState;
use datadog_api_client::datadogV2::model::RUMProductAnalyticsRetentionState;

#[tokio::main]
async fn main() {
    // there is a valid "rum_application" in the system
    let rum_application_data_id = std::env::var("RUM_APPLICATION_DATA_ID").unwrap();
    let body = RUMApplicationUpdateRequest::new(
        RUMApplicationUpdate::new(
            rum_application_data_id.clone(),
            RUMApplicationUpdateType::RUM_APPLICATION_UPDATE,
        )
        .attributes(
            RUMApplicationUpdateAttributes::new()
                .name("updated_rum_with_product_scales".to_string())
                .product_analytics_retention_state(RUMProductAnalyticsRetentionState::MAX)
                .rum_event_processing_state(RUMEventProcessingState::ALL),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api
        .update_rum_application(rum_application_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Update a RUM application returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

// there is a valid "rum_application" in the system
const RUM_APPLICATION_DATA_ID = process.env.RUM_APPLICATION_DATA_ID as string;

const params: v2.RUMApiUpdateRUMApplicationRequest = {
  body: {
    data: {
      attributes: {
        name: "updated_name_for_my_existing_rum_application",
        type: "browser",
      },
      id: RUM_APPLICATION_DATA_ID,
      type: "rum_application_update",
    },
  },
  id: RUM_APPLICATION_DATA_ID,
};

apiInstance
  .updateRUMApplication(params)
  .then((data: v2.RUMApplicationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#####

```typescript
/**
 * Update a RUM application with Product Scales returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

// there is a valid "rum_application" in the system
const RUM_APPLICATION_DATA_ID = process.env.RUM_APPLICATION_DATA_ID as string;

const params: v2.RUMApiUpdateRUMApplicationRequest = {
  body: {
    data: {
      attributes: {
        name: "updated_rum_with_product_scales",
        rumEventProcessingState: "ALL",
        productAnalyticsRetentionState: "MAX",
      },
      id: RUM_APPLICATION_DATA_ID,
      type: "rum_application_update",
    },
  },
  id: RUM_APPLICATION_DATA_ID,
};

apiInstance
  .updateRUMApplication(params)
  .then((data: v2.RUMApplicationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get a RUM application{% #get-a-rum-application %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/applications/{id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/applications/{id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/applications/{id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/applications/{id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/applications/{id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/applications/{id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/applications/{id} |

### Overview

Get the RUM application with given ID in your organization. This endpoint requires the `rum_apps_read` permission.

### Arguments

#### Path Parameters

| Name                 | Type   | Description         |
| -------------------- | ------ | ------------------- |
| id [*required*] | string | RUM application ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
RUM application response.

| Parent field                      | Field                               | Type    | Description                                                                                                                                                    |
| --------------------------------- | ----------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                   | data                                | object  | RUM application.                                                                                                                                               |
| data                              | attributes [*required*]        | object  | RUM application attributes.                                                                                                                                    |
| attributes                        | api_key_id                          | int32   | ID of the API key associated with the application.                                                                                                             |
| attributes                        | application_id [*required*]    | string  | ID of the RUM application.                                                                                                                                     |
| attributes                        | client_token [*required*]      | string  | Client token of the RUM application.                                                                                                                           |
| attributes                        | created_at [*required*]        | int64   | Timestamp in ms of the creation date.                                                                                                                          |
| attributes                        | created_by_handle [*required*] | string  | Handle of the creator user.                                                                                                                                    |
| attributes                        | hash                                | string  | Hash of the RUM application. Optional.                                                                                                                         |
| attributes                        | is_active                           | boolean | Indicates if the RUM application is active.                                                                                                                    |
| attributes                        | name [*required*]              | string  | Name of the RUM application.                                                                                                                                   |
| attributes                        | org_id [*required*]            | int32   | Org ID of the RUM application.                                                                                                                                 |
| attributes                        | product_scales                      | object  | Product Scales configuration for the RUM application.                                                                                                          |
| product_scales                    | product_analytics_retention_scale   | object  | Product Analytics retention scale configuration.                                                                                                               |
| product_analytics_retention_scale | last_modified_at                    | int64   | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| product_analytics_retention_scale | state                               | enum    | Controls the retention policy for Product Analytics data derived from RUM events. Allowed enum values: `MAX,NONE`                                              |
| product_scales                    | rum_event_processing_scale          | object  | RUM event processing scale configuration.                                                                                                                      |
| rum_event_processing_scale        | last_modified_at                    | int64   | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| rum_event_processing_scale        | state                               | enum    | Configures which RUM events are processed and stored for the application. Allowed enum values: `ALL,ERROR_FOCUSED_MODE,NONE`                                   |
| attributes                        | type [*required*]              | string  | Type of the RUM application. Supported values are `browser`, `ios`, `android`, `react-native`, `flutter`, `roku`, `electron`, `unity`, `kotlin-multiplatform`. |
| attributes                        | updated_at [*required*]        | int64   | Timestamp in ms of the last update date.                                                                                                                       |
| attributes                        | updated_by_handle [*required*] | string  | Handle of the updater user.                                                                                                                                    |
| data                              | id [*required*]                | string  | RUM application ID.                                                                                                                                            |
| data                              | type [*required*]              | enum    | RUM application response type. Allowed enum values: `rum_application`                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key_id": 123456789,
      "application_id": "abcd1234-0000-0000-abcd-1234abcd5678",
      "client_token": "abcd1234efgh5678ijkl90abcd1234efgh0",
      "created_at": 1659479836169,
      "created_by_handle": "john.doe",
      "hash": "string",
      "is_active": true,
      "name": "my_rum_application",
      "org_id": 999,
      "product_scales": {
        "product_analytics_retention_scale": {
          "last_modified_at": 1747922145974,
          "state": "MAX"
        },
        "rum_event_processing_scale": {
          "last_modified_at": 1721897494108,
          "state": "ALL"
        }
      },
      "type": "browser",
      "updated_at": 1659479836169,
      "updated_by_handle": "jane.doe"
    },
    "id": "abcd1234-0000-0000-abcd-1234abcd5678",
    "type": "rum_application"
  }
}
```text

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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a RUM application returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.get_rum_application(
        id=RUM_APPLICATION_DATA_ID,
    )

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a RUM application returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = ENV["RUM_APPLICATION_DATA_ID"]
p api_instance.get_rum_application(RUM_APPLICATION_DATA_ID)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a RUM application returns "OK" response

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
    // there is a valid "rum_application" in the system
    RumApplicationDataID := os.Getenv("RUM_APPLICATION_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.GetRUMApplication(ctx, RumApplicationDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.GetRUMApplication`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.GetRUMApplication`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a RUM application returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMApplicationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    // there is a valid "rum_application" in the system
    String RUM_APPLICATION_DATA_ID = System.getenv("RUM_APPLICATION_DATA_ID");

    try {
      RUMApplicationResponse result = apiInstance.getRUMApplication(RUM_APPLICATION_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#getRUMApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get a RUM application returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;

#[tokio::main]
async fn main() {
    // there is a valid "rum_application" in the system
    let rum_application_data_id = std::env::var("RUM_APPLICATION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api
        .get_rum_application(rum_application_data_id.clone())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get a RUM application returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

// there is a valid "rum_application" in the system
const RUM_APPLICATION_DATA_ID = process.env.RUM_APPLICATION_DATA_ID as string;

const params: v2.RUMApiGetRUMApplicationRequest = {
  id: RUM_APPLICATION_DATA_ID,
};

apiInstance
  .getRUMApplication(params)
  .then((data: v2.RUMApplicationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete a RUM application{% #delete-a-rum-application %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/rum/applications/{id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/rum/applications/{id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/rum/applications/{id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/rum/applications/{id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/rum/applications/{id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/rum/applications/{id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/rum/applications/{id} |

### Overview

Delete an existing RUM application in your organization. This endpoint requires the `rum_apps_write` permission.

### Arguments

#### Path Parameters

| Name                 | Type   | Description         |
| -------------------- | ------ | ------------------- |
| id [*required*] | string | RUM application ID. |

### Response

{% tab title="204" %}
No Content
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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a RUM application returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    api_instance.delete_rum_application(
        id=RUM_APPLICATION_DATA_ID,
    )
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a RUM application returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = ENV["RUM_APPLICATION_DATA_ID"]
api_instance.delete_rum_application(RUM_APPLICATION_DATA_ID)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a RUM application returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "rum_application" in the system
    RumApplicationDataID := os.Getenv("RUM_APPLICATION_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    r, err := api.DeleteRUMApplication(ctx, RumApplicationDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.DeleteRUMApplication`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a RUM application returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    // there is a valid "rum_application" in the system
    String RUM_APPLICATION_DATA_ID = System.getenv("RUM_APPLICATION_DATA_ID");

    try {
      apiInstance.deleteRUMApplication(RUM_APPLICATION_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#deleteRUMApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Delete a RUM application returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;

#[tokio::main]
async fn main() {
    // there is a valid "rum_application" in the system
    let rum_application_data_id = std::env::var("RUM_APPLICATION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api
        .delete_rum_application(rum_application_data_id.clone())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Delete a RUM application returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

// there is a valid "rum_application" in the system
const RUM_APPLICATION_DATA_ID = process.env.RUM_APPLICATION_DATA_ID as string;

const params: v2.RUMApiDeleteRUMApplicationRequest = {
  id: RUM_APPLICATION_DATA_ID,
};

apiInstance
  .deleteRUMApplication(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create a new RUM application{% #create-a-new-rum-application %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/rum/applications |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/rum/applications |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/rum/applications      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/rum/applications      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/rum/applications     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/rum/applications |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/rum/applications |

### Overview

Create a new RUM application in your organization. This endpoint requires the `rum_apps_write` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                             | Type   | Description                                                                                                                                                    |
| ------------ | --------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]            | object | RUM application creation.                                                                                                                                      |
| data         | attributes [*required*]      | object | RUM application creation attributes.                                                                                                                           |
| attributes   | name [*required*]            | string | Name of the RUM application.                                                                                                                                   |
| attributes   | product_analytics_retention_state | enum   | Controls the retention policy for Product Analytics data derived from RUM events. Allowed enum values: `MAX,NONE`                                              |
| attributes   | rum_event_processing_state        | enum   | Configures which RUM events are processed and stored for the application. Allowed enum values: `ALL,ERROR_FOCUSED_MODE,NONE`                                   |
| attributes   | type                              | string | Type of the RUM application. Supported values are `browser`, `ios`, `android`, `react-native`, `flutter`, `roku`, `electron`, `unity`, `kotlin-multiplatform`. |
| data         | type [*required*]            | enum   | RUM application creation type. Allowed enum values: `rum_application_create`                                                                                   |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "name": "test-rum-5c67ebb32077e1d9",
      "type": "ios"
    },
    "type": "rum_application_create"
  }
}
```text

#####

```json
{
  "data": {
    "attributes": {
      "name": "test-rum-with-product-scales-5c67ebb32077e1d9",
      "type": "browser",
      "rum_event_processing_state": "ERROR_FOCUSED_MODE",
      "product_analytics_retention_state": "NONE"
    },
    "type": "rum_application_create"
  }
}
```text

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
RUM application response.

| Parent field                      | Field                               | Type    | Description                                                                                                                                                    |
| --------------------------------- | ----------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                   | data                                | object  | RUM application.                                                                                                                                               |
| data                              | attributes [*required*]        | object  | RUM application attributes.                                                                                                                                    |
| attributes                        | api_key_id                          | int32   | ID of the API key associated with the application.                                                                                                             |
| attributes                        | application_id [*required*]    | string  | ID of the RUM application.                                                                                                                                     |
| attributes                        | client_token [*required*]      | string  | Client token of the RUM application.                                                                                                                           |
| attributes                        | created_at [*required*]        | int64   | Timestamp in ms of the creation date.                                                                                                                          |
| attributes                        | created_by_handle [*required*] | string  | Handle of the creator user.                                                                                                                                    |
| attributes                        | hash                                | string  | Hash of the RUM application. Optional.                                                                                                                         |
| attributes                        | is_active                           | boolean | Indicates if the RUM application is active.                                                                                                                    |
| attributes                        | name [*required*]              | string  | Name of the RUM application.                                                                                                                                   |
| attributes                        | org_id [*required*]            | int32   | Org ID of the RUM application.                                                                                                                                 |
| attributes                        | product_scales                      | object  | Product Scales configuration for the RUM application.                                                                                                          |
| product_scales                    | product_analytics_retention_scale   | object  | Product Analytics retention scale configuration.                                                                                                               |
| product_analytics_retention_scale | last_modified_at                    | int64   | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| product_analytics_retention_scale | state                               | enum    | Controls the retention policy for Product Analytics data derived from RUM events. Allowed enum values: `MAX,NONE`                                              |
| product_scales                    | rum_event_processing_scale          | object  | RUM event processing scale configuration.                                                                                                                      |
| rum_event_processing_scale        | last_modified_at                    | int64   | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| rum_event_processing_scale        | state                               | enum    | Configures which RUM events are processed and stored for the application. Allowed enum values: `ALL,ERROR_FOCUSED_MODE,NONE`                                   |
| attributes                        | type [*required*]              | string  | Type of the RUM application. Supported values are `browser`, `ios`, `android`, `react-native`, `flutter`, `roku`, `electron`, `unity`, `kotlin-multiplatform`. |
| attributes                        | updated_at [*required*]        | int64   | Timestamp in ms of the last update date.                                                                                                                       |
| attributes                        | updated_by_handle [*required*] | string  | Handle of the updater user.                                                                                                                                    |
| data                              | id [*required*]                | string  | RUM application ID.                                                                                                                                            |
| data                              | type [*required*]              | enum    | RUM application response type. Allowed enum values: `rum_application`                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key_id": 123456789,
      "application_id": "abcd1234-0000-0000-abcd-1234abcd5678",
      "client_token": "abcd1234efgh5678ijkl90abcd1234efgh0",
      "created_at": 1659479836169,
      "created_by_handle": "john.doe",
      "hash": "string",
      "is_active": true,
      "name": "my_rum_application",
      "org_id": 999,
      "product_scales": {
        "product_analytics_retention_scale": {
          "last_modified_at": 1747922145974,
          "state": "MAX"
        },
        "rum_event_processing_scale": {
          "last_modified_at": 1721897494108,
          "state": "ALL"
        }
      },
      "type": "browser",
      "updated_at": 1659479836169,
      "updated_by_handle": "jane.doe"
    },
    "id": "abcd1234-0000-0000-abcd-1234abcd5678",
    "type": "rum_application"
  }
}
```text

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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "test-rum-5c67ebb32077e1d9",
      "type": "ios"
    },
    "type": "rum_application_create"
  }
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "test-rum-with-product-scales-5c67ebb32077e1d9",
      "type": "browser",
      "rum_event_processing_state": "ERROR_FOCUSED_MODE",
      "product_analytics_retention_state": "NONE"
    },
    "type": "rum_application_create"
  }
}
EOF

#####

```go
// Create a new RUM application returns "OK" response

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
    body := datadogV2.RUMApplicationCreateRequest{
        Data: datadogV2.RUMApplicationCreate{
            Attributes: datadogV2.RUMApplicationCreateAttributes{
                Name: "test-rum-5c67ebb32077e1d9",
                Type: datadog.PtrString("ios"),
            },
            Type: datadogV2.RUMAPPLICATIONCREATETYPE_RUM_APPLICATION_CREATE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.CreateRUMApplication(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.CreateRUMApplication`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.CreateRUMApplication`:\n%s\n", responseContent)
}
```text

#####

```go
// Create a new RUM application with Product Scales returns "OK" response

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
    body := datadogV2.RUMApplicationCreateRequest{
        Data: datadogV2.RUMApplicationCreate{
            Attributes: datadogV2.RUMApplicationCreateAttributes{
                Name:                           "test-rum-with-product-scales-5c67ebb32077e1d9",
                Type:                           datadog.PtrString("browser"),
                RumEventProcessingState:        datadogV2.RUMEVENTPROCESSINGSTATE_ERROR_FOCUSED_MODE.Ptr(),
                ProductAnalyticsRetentionState: datadogV2.RUMPRODUCTANALYTICSRETENTIONSTATE_NONE.Ptr(),
            },
            Type: datadogV2.RUMAPPLICATIONCREATETYPE_RUM_APPLICATION_CREATE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.CreateRUMApplication(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.CreateRUMApplication`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.CreateRUMApplication`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a new RUM application returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMApplicationCreate;
import com.datadog.api.client.v2.model.RUMApplicationCreateAttributes;
import com.datadog.api.client.v2.model.RUMApplicationCreateRequest;
import com.datadog.api.client.v2.model.RUMApplicationCreateType;
import com.datadog.api.client.v2.model.RUMApplicationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    RUMApplicationCreateRequest body =
        new RUMApplicationCreateRequest()
            .data(
                new RUMApplicationCreate()
                    .attributes(
                        new RUMApplicationCreateAttributes()
                            .name("test-rum-5c67ebb32077e1d9")
                            .type("ios"))
                    .type(RUMApplicationCreateType.RUM_APPLICATION_CREATE));

    try {
      RUMApplicationResponse result = apiInstance.createRUMApplication(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#createRUMApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#####

```java
// Create a new RUM application with Product Scales returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMApplicationCreate;
import com.datadog.api.client.v2.model.RUMApplicationCreateAttributes;
import com.datadog.api.client.v2.model.RUMApplicationCreateRequest;
import com.datadog.api.client.v2.model.RUMApplicationCreateType;
import com.datadog.api.client.v2.model.RUMApplicationResponse;
import com.datadog.api.client.v2.model.RUMEventProcessingState;
import com.datadog.api.client.v2.model.RUMProductAnalyticsRetentionState;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    RUMApplicationCreateRequest body =
        new RUMApplicationCreateRequest()
            .data(
                new RUMApplicationCreate()
                    .attributes(
                        new RUMApplicationCreateAttributes()
                            .name("test-rum-with-product-scales-5c67ebb32077e1d9")
                            .type("browser")
                            .rumEventProcessingState(RUMEventProcessingState.ERROR_FOCUSED_MODE)
                            .productAnalyticsRetentionState(RUMProductAnalyticsRetentionState.NONE))
                    .type(RUMApplicationCreateType.RUM_APPLICATION_CREATE));

    try {
      RUMApplicationResponse result = apiInstance.createRUMApplication(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#createRUMApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
"""
Create a new RUM application returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_create import RUMApplicationCreate
from datadog_api_client.v2.model.rum_application_create_attributes import RUMApplicationCreateAttributes
from datadog_api_client.v2.model.rum_application_create_request import RUMApplicationCreateRequest
from datadog_api_client.v2.model.rum_application_create_type import RUMApplicationCreateType

body = RUMApplicationCreateRequest(
    data=RUMApplicationCreate(
        attributes=RUMApplicationCreateAttributes(
            name="test-rum-5c67ebb32077e1d9",
            type="ios",
        ),
        type=RUMApplicationCreateType.RUM_APPLICATION_CREATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.create_rum_application(body=body)

    print(response)
```text

#####

```python
"""
Create a new RUM application with Product Scales returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_create import RUMApplicationCreate
from datadog_api_client.v2.model.rum_application_create_attributes import RUMApplicationCreateAttributes
from datadog_api_client.v2.model.rum_application_create_request import RUMApplicationCreateRequest
from datadog_api_client.v2.model.rum_application_create_type import RUMApplicationCreateType
from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState
from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState

body = RUMApplicationCreateRequest(
    data=RUMApplicationCreate(
        attributes=RUMApplicationCreateAttributes(
            name="test-rum-with-product-scales-5c67ebb32077e1d9",
            type="browser",
            rum_event_processing_state=RUMEventProcessingState.ERROR_FOCUSED_MODE,
            product_analytics_retention_state=RUMProductAnalyticsRetentionState.NONE,
        ),
        type=RUMApplicationCreateType.RUM_APPLICATION_CREATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.create_rum_application(body=body)

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a new RUM application returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

body = DatadogAPIClient::V2::RUMApplicationCreateRequest.new({
  data: DatadogAPIClient::V2::RUMApplicationCreate.new({
    attributes: DatadogAPIClient::V2::RUMApplicationCreateAttributes.new({
      name: "test-rum-5c67ebb32077e1d9",
      type: "ios",
    }),
    type: DatadogAPIClient::V2::RUMApplicationCreateType::RUM_APPLICATION_CREATE,
  }),
})
p api_instance.create_rum_application(body)
```text

#####

```ruby
# Create a new RUM application with Product Scales returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new

body = DatadogAPIClient::V2::RUMApplicationCreateRequest.new({
  data: DatadogAPIClient::V2::RUMApplicationCreate.new({
    attributes: DatadogAPIClient::V2::RUMApplicationCreateAttributes.new({
      name: "test-rum-with-product-scales-5c67ebb32077e1d9",
      type: "browser",
      rum_event_processing_state: DatadogAPIClient::V2::RUMEventProcessingState::ERROR_FOCUSED_MODE,
      product_analytics_retention_state: DatadogAPIClient::V2::RUMProductAnalyticsRetentionState::NONE,
    }),
    type: DatadogAPIClient::V2::RUMApplicationCreateType::RUM_APPLICATION_CREATE,
  }),
})
p api_instance.create_rum_application(body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a new RUM application returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;
use datadog_api_client::datadogV2::model::RUMApplicationCreate;
use datadog_api_client::datadogV2::model::RUMApplicationCreateAttributes;
use datadog_api_client::datadogV2::model::RUMApplicationCreateRequest;
use datadog_api_client::datadogV2::model::RUMApplicationCreateType;

#[tokio::main]
async fn main() {
    let body = RUMApplicationCreateRequest::new(RUMApplicationCreate::new(
        RUMApplicationCreateAttributes::new("test-rum-5c67ebb32077e1d9".to_string())
            .type_("ios".to_string()),
        RUMApplicationCreateType::RUM_APPLICATION_CREATE,
    ));
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api.create_rum_application(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#####

```rust
// Create a new RUM application with Product Scales returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;
use datadog_api_client::datadogV2::model::RUMApplicationCreate;
use datadog_api_client::datadogV2::model::RUMApplicationCreateAttributes;
use datadog_api_client::datadogV2::model::RUMApplicationCreateRequest;
use datadog_api_client::datadogV2::model::RUMApplicationCreateType;
use datadog_api_client::datadogV2::model::RUMEventProcessingState;
use datadog_api_client::datadogV2::model::RUMProductAnalyticsRetentionState;

#[tokio::main]
async fn main() {
    let body = RUMApplicationCreateRequest::new(RUMApplicationCreate::new(
        RUMApplicationCreateAttributes::new(
            "test-rum-with-product-scales-5c67ebb32077e1d9".to_string(),
        )
        .product_analytics_retention_state(RUMProductAnalyticsRetentionState::NONE)
        .rum_event_processing_state(RUMEventProcessingState::ERROR_FOCUSED_MODE)
        .type_("browser".to_string()),
        RUMApplicationCreateType::RUM_APPLICATION_CREATE,
    ));
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api.create_rum_application(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Create a new RUM application returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

const params: v2.RUMApiCreateRUMApplicationRequest = {
  body: {
    data: {
      attributes: {
        name: "test-rum-5c67ebb32077e1d9",
        type: "ios",
      },
      type: "rum_application_create",
    },
  },
};

apiInstance
  .createRUMApplication(params)
  .then((data: v2.RUMApplicationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#####

```typescript
/**
 * Create a new RUM application with Product Scales returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

const params: v2.RUMApiCreateRUMApplicationRequest = {
  body: {
    data: {
      attributes: {
        name: "test-rum-with-product-scales-5c67ebb32077e1d9",
        type: "browser",
        rumEventProcessingState: "ERROR_FOCUSED_MODE",
        productAnalyticsRetentionState: "NONE",
      },
      type: "rum_application_create",
    },
  },
};

apiInstance
  .createRUMApplication(params)
  .then((data: v2.RUMApplicationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## List all the RUM applications{% #list-all-the-rum-applications %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/applications |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/applications |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/applications      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/applications      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/applications     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/applications |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/applications |

### Overview

List all the RUM applications in your organization. This endpoint requires the `rum_apps_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
RUM applications response.

| Parent field                      | Field                               | Type     | Description                                                                                                                                                    |
| --------------------------------- | ----------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                   | data                                | [object] | RUM applications array response.                                                                                                                               |
| data                              | attributes [*required*]        | object   | RUM application list attributes.                                                                                                                               |
| attributes                        | application_id [*required*]    | string   | ID of the RUM application.                                                                                                                                     |
| attributes                        | created_at [*required*]        | int64    | Timestamp in ms of the creation date.                                                                                                                          |
| attributes                        | created_by_handle [*required*] | string   | Handle of the creator user.                                                                                                                                    |
| attributes                        | hash                                | string   | Hash of the RUM application. Optional.                                                                                                                         |
| attributes                        | is_active                           | boolean  | Indicates if the RUM application is active.                                                                                                                    |
| attributes                        | name [*required*]              | string   | Name of the RUM application.                                                                                                                                   |
| attributes                        | org_id [*required*]            | int32    | Org ID of the RUM application.                                                                                                                                 |
| attributes                        | product_scales                      | object   | Product Scales configuration for the RUM application.                                                                                                          |
| product_scales                    | product_analytics_retention_scale   | object   | Product Analytics retention scale configuration.                                                                                                               |
| product_analytics_retention_scale | last_modified_at                    | int64    | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| product_analytics_retention_scale | state                               | enum     | Controls the retention policy for Product Analytics data derived from RUM events. Allowed enum values: `MAX,NONE`                                              |
| product_scales                    | rum_event_processing_scale          | object   | RUM event processing scale configuration.                                                                                                                      |
| rum_event_processing_scale        | last_modified_at                    | int64    | Timestamp in milliseconds when this scale was last modified.                                                                                                   |
| rum_event_processing_scale        | state                               | enum     | Configures which RUM events are processed and stored for the application. Allowed enum values: `ALL,ERROR_FOCUSED_MODE,NONE`                                   |
| attributes                        | type [*required*]              | string   | Type of the RUM application. Supported values are `browser`, `ios`, `android`, `react-native`, `flutter`, `roku`, `electron`, `unity`, `kotlin-multiplatform`. |
| attributes                        | updated_at [*required*]        | int64    | Timestamp in ms of the last update date.                                                                                                                       |
| attributes                        | updated_by_handle [*required*] | string   | Handle of the updater user.                                                                                                                                    |
| data                              | id                                  | string   | RUM application ID.                                                                                                                                            |
| data                              | type [*required*]              | enum     | RUM application list type. Allowed enum values: `rum_application`                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "application_id": "abcd1234-0000-0000-abcd-1234abcd5678",
        "created_at": 1659479836169,
        "created_by_handle": "john.doe",
        "hash": "string",
        "is_active": true,
        "name": "my_rum_application",
        "org_id": 999,
        "product_scales": {
          "product_analytics_retention_scale": {
            "last_modified_at": 1747922145974,
            "state": "MAX"
          },
          "rum_event_processing_scale": {
            "last_modified_at": 1721897494108,
            "state": "ALL"
          }
        },
        "type": "browser",
        "updated_at": 1659479836169,
        "updated_by_handle": "jane.doe"
      },
      "id": "abcd1234-0000-0000-abcd-1234abcd5678",
      "type": "rum_application"
    }
  ]
}
```text

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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/applications" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List all the RUM applications returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.get_rum_applications()

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List all the RUM applications returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RUMAPI.new
p api_instance.get_rum_applications()
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List all the RUM applications returns "OK" response

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
    api := datadogV2.NewRUMApi(apiClient)
    resp, r, err := api.GetRUMApplications(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RUMApi.GetRUMApplications`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RUMApi.GetRUMApplications`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List all the RUM applications returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumApi;
import com.datadog.api.client.v2.model.RUMApplicationsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumApi apiInstance = new RumApi(defaultClient);

    try {
      RUMApplicationsResponse result = apiInstance.getRUMApplications();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumApi#getRUMApplications");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// List all the RUM applications returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum::RUMAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RUMAPI::with_config(configuration);
    let resp = api.get_rum_applications().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * List all the RUM applications returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RUMApi(configuration);

apiInstance
  .getRUMApplications()
  .then((data: v2.RUMApplicationsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
