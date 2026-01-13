# Source: https://docs.datadoghq.com/api/latest/audit/

# Audit
Search your Audit Logs events over HTTP.
## [Search Audit Logs events](https://docs.datadoghq.com/api/latest/audit/#search-audit-logs-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/audit/#search-audit-logs-events-v2)


POST https://api.ap1.datadoghq.com/api/v2/audit/events/searchhttps://api.ap2.datadoghq.com/api/v2/audit/events/searchhttps://api.datadoghq.eu/api/v2/audit/events/searchhttps://api.ddog-gov.com/api/v2/audit/events/searchhttps://api.datadoghq.com/api/v2/audit/events/searchhttps://api.us3.datadoghq.com/api/v2/audit/events/searchhttps://api.us5.datadoghq.com/api/v2/audit/events/search
### Overview
List endpoint returns Audit Logs events that match an Audit search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).
Use this endpoint to build complex Audit Logs events filtering and search.
This endpoint requires the `audit_logs_read` permission.
### Request
#### Body Data 
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


Field
Type
Description
filter
object
Search and filter query settings.
from
string
Minimum time for the requested events. Supports date, math, and regular timestamps (in milliseconds).
default: `now-15m`
query
string
Search query following the Audit Logs search syntax.
default: `*`
to
string
Maximum time for the requested events. Supports date, math, and regular timestamps (in milliseconds).
default: `now`
options
object
Global query options that are used during the query. Note: Specify either timezone or time offset, not both. Otherwise, the query fails.
time_offset
int64
Time offset (in seconds) to apply to the query.
timezone
string
The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).
default: `UTC`
page
object
Paging attributes for listing events.
cursor
string
List following results with a cursor provided in the previous query.
limit
int32
Maximum number of events in the response.
default: `10`
sort
enum
Sort parameters when querying events. Allowed enum values: `timestamp,-timestamp`
#####  Search Audit Logs events returns "OK" response
```
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
```

Copy
#####  Search Audit Logs events returns "OK" response with pagination
```
{
  "filter": {
    "from": "now-15m",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/audit/#SearchAuditLogs-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/audit/#SearchAuditLogs-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/audit/#SearchAuditLogs-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/audit/#SearchAuditLogs-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


Response object with all events matching the request and pagination information.
Field
Type
Description
data
[object]
Array of events matching the request.
attributes
object
JSON object containing all event attributes and their associated values.
attributes
object
JSON object of attributes from Audit Logs events.
message
string
Message of the event.
service
string
Name of the application or service generating Audit Logs events. This name is used to correlate Audit Logs to APM, so make sure you specify the same value when you use both products.
tags
[string]
Array of tags associated with your event.
timestamp
date-time
Timestamp of your event.
id
string
Unique ID of the event.
type
enum
Type of the event. Allowed enum values: `audit`
default: `audit`
links
object
Links attributes.
next
string
Link for the next set of results. Note that the request can also be made using the POST endpoint.
meta
object
The metadata associated with a request.
elapsed
int64
Time elapsed in milliseconds.
page
object
Paging attributes.
after
string
The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`.
request_id
string
The identifier of the request.
status
enum
The status of the response. Allowed enum values: `done,timeout`
warnings
[object]
A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response.
code
string
Unique code for this type of warning.
detail
string
Detailed explanation of this specific warning.
title
string
Short human-readable summary of the warning.
```
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "message": "string",
        "service": "web-app",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "audit"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/audit/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/audit/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/audit/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/audit/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/audit/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/audit/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/audit/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/audit/?code-lang=typescript)


#####  Search Audit Logs events returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/audit/events/search" \
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

                        
```

#####  Search Audit Logs events returns "OK" response with pagination
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/audit/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
EOF  

                        
```

#####  Search Audit Logs events returns "OK" response 
```
// Search Audit Logs events returns "OK" response

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
	body := datadogV2.AuditLogsSearchEventsRequest{
		Filter: &datadogV2.AuditLogsQueryFilter{
			From:  datadog.PtrString("now-15m"),
			Query: datadog.PtrString("@type:session AND @session.type:user"),
			To:    datadog.PtrString("now"),
		},
		Options: &datadogV2.AuditLogsQueryOptions{
			TimeOffset: datadog.PtrInt64(0),
			Timezone:   datadog.PtrString("GMT"),
		},
		Page: &datadogV2.AuditLogsQueryPageOptions{
			Limit: datadog.PtrInt32(25),
		},
		Sort: datadogV2.AUDITLOGSSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuditApi(apiClient)
	resp, r, err := api.SearchAuditLogs(ctx, *datadogV2.NewSearchAuditLogsOptionalParameters().WithBody(body))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditApi.SearchAuditLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuditApi.SearchAuditLogs`:\n%s\n", responseContent)
}

```

Copy
#####  Search Audit Logs events returns "OK" response with pagination 
```
// Search Audit Logs events returns "OK" response with pagination

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
	body := datadogV2.AuditLogsSearchEventsRequest{
		Filter: &datadogV2.AuditLogsQueryFilter{
			From: datadog.PtrString("now-15m"),
			To:   datadog.PtrString("now"),
		},
		Options: &datadogV2.AuditLogsQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
		Page: &datadogV2.AuditLogsQueryPageOptions{
			Limit: datadog.PtrInt32(2),
		},
		Sort: datadogV2.AUDITLOGSSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuditApi(apiClient)
	resp, _ := api.SearchAuditLogsWithPagination(ctx, *datadogV2.NewSearchAuditLogsOptionalParameters().WithBody(body))

	for paginationResult := range resp {
		if paginationResult.Error != nil {
			fmt.Fprintf(os.Stderr, "Error when calling `AuditApi.SearchAuditLogs`: %v\n", paginationResult.Error)
		}
		responseContent, _ := json.MarshalIndent(paginationResult.Item, "", "  ")
		fmt.Fprintf(os.Stdout, "%s\n", responseContent)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Search Audit Logs events returns "OK" response 
```
// Search Audit Logs events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuditApi;
import com.datadog.api.client.v2.api.AuditApi.SearchAuditLogsOptionalParameters;
import com.datadog.api.client.v2.model.AuditLogsEventsResponse;
import com.datadog.api.client.v2.model.AuditLogsQueryFilter;
import com.datadog.api.client.v2.model.AuditLogsQueryOptions;
import com.datadog.api.client.v2.model.AuditLogsQueryPageOptions;
import com.datadog.api.client.v2.model.AuditLogsSearchEventsRequest;
import com.datadog.api.client.v2.model.AuditLogsSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuditApi apiInstance = new AuditApi(defaultClient);

    AuditLogsSearchEventsRequest body =
        new AuditLogsSearchEventsRequest()
            .filter(
                new AuditLogsQueryFilter()
                    .from("now-15m")
                    .query("@type:session AND @session.type:user")
                    .to("now"))
            .options(new AuditLogsQueryOptions().timeOffset(0L).timezone("GMT"))
            .page(new AuditLogsQueryPageOptions().limit(25))
            .sort(AuditLogsSort.TIMESTAMP_ASCENDING);

    try {
      AuditLogsEventsResponse result =
          apiInstance.searchAuditLogs(new SearchAuditLogsOptionalParameters().body(body));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditApi#searchAuditLogs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Search Audit Logs events returns "OK" response with pagination 
```
// Search Audit Logs events returns "OK" response with pagination

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.PaginationIterable;
import com.datadog.api.client.v2.api.AuditApi;
import com.datadog.api.client.v2.api.AuditApi.SearchAuditLogsOptionalParameters;
import com.datadog.api.client.v2.model.AuditLogsEvent;
import com.datadog.api.client.v2.model.AuditLogsQueryFilter;
import com.datadog.api.client.v2.model.AuditLogsQueryOptions;
import com.datadog.api.client.v2.model.AuditLogsQueryPageOptions;
import com.datadog.api.client.v2.model.AuditLogsSearchEventsRequest;
import com.datadog.api.client.v2.model.AuditLogsSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuditApi apiInstance = new AuditApi(defaultClient);

    AuditLogsSearchEventsRequest body =
        new AuditLogsSearchEventsRequest()
            .filter(new AuditLogsQueryFilter().from("now-15m").to("now"))
            .options(new AuditLogsQueryOptions().timezone("GMT"))
            .page(new AuditLogsQueryPageOptions().limit(2))
            .sort(AuditLogsSort.TIMESTAMP_ASCENDING);

    try {
      PaginationIterable<AuditLogsEvent> iterable =
          apiInstance.searchAuditLogsWithPagination(
              new SearchAuditLogsOptionalParameters().body(body));

      for (AuditLogsEvent item : iterable) {
        System.out.println(item);
      }
    } catch (RuntimeException e) {
      System.err.println("Exception when calling AuditApi#searchAuditLogsWithPagination");
      System.err.println("Reason: " + e.getMessage());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Search Audit Logs events returns "OK" response 
```
"""
Search Audit Logs events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.audit_api import AuditApi
from datadog_api_client.v2.model.audit_logs_query_filter import AuditLogsQueryFilter
from datadog_api_client.v2.model.audit_logs_query_options import AuditLogsQueryOptions
from datadog_api_client.v2.model.audit_logs_query_page_options import AuditLogsQueryPageOptions
from datadog_api_client.v2.model.audit_logs_search_events_request import AuditLogsSearchEventsRequest
from datadog_api_client.v2.model.audit_logs_sort import AuditLogsSort

body = AuditLogsSearchEventsRequest(
    filter=AuditLogsQueryFilter(
        _from="now-15m",
        query="@type:session AND @session.type:user",
        to="now",
    ),
    options=AuditLogsQueryOptions(
        time_offset=0,
        timezone="GMT",
    ),
    page=AuditLogsQueryPageOptions(
        limit=25,
    ),
    sort=AuditLogsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuditApi(api_client)
    response = api_instance.search_audit_logs(body=body)

    print(response)

```

Copy
#####  Search Audit Logs events returns "OK" response with pagination 
```
"""
Search Audit Logs events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.audit_api import AuditApi
from datadog_api_client.v2.model.audit_logs_query_filter import AuditLogsQueryFilter
from datadog_api_client.v2.model.audit_logs_query_options import AuditLogsQueryOptions
from datadog_api_client.v2.model.audit_logs_query_page_options import AuditLogsQueryPageOptions
from datadog_api_client.v2.model.audit_logs_search_events_request import AuditLogsSearchEventsRequest
from datadog_api_client.v2.model.audit_logs_sort import AuditLogsSort

body = AuditLogsSearchEventsRequest(
    filter=AuditLogsQueryFilter(
        _from="now-15m",
        to="now",
    ),
    options=AuditLogsQueryOptions(
        timezone="GMT",
    ),
    page=AuditLogsQueryPageOptions(
        limit=2,
    ),
    sort=AuditLogsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuditApi(api_client)
    items = api_instance.search_audit_logs_with_pagination(body=body)
    for item in items:
        print(item)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Search Audit Logs events returns "OK" response 
```
# Search Audit Logs events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuditAPI.new

body = DatadogAPIClient::V2::AuditLogsSearchEventsRequest.new({
  filter: DatadogAPIClient::V2::AuditLogsQueryFilter.new({
    from: "now-15m",
    query: "@type:session AND @session.type:user",
    to: "now",
  }),
  options: DatadogAPIClient::V2::AuditLogsQueryOptions.new({
    time_offset: 0,
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::AuditLogsQueryPageOptions.new({
    limit: 25,
  }),
  sort: DatadogAPIClient::V2::AuditLogsSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
p api_instance.search_audit_logs(opts)

```

Copy
#####  Search Audit Logs events returns "OK" response with pagination 
```
# Search Audit Logs events returns "OK" response with pagination

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuditAPI.new

body = DatadogAPIClient::V2::AuditLogsSearchEventsRequest.new({
  filter: DatadogAPIClient::V2::AuditLogsQueryFilter.new({
    from: "now-15m",
    to: "now",
  }),
  options: DatadogAPIClient::V2::AuditLogsQueryOptions.new({
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::AuditLogsQueryPageOptions.new({
    limit: 2,
  }),
  sort: DatadogAPIClient::V2::AuditLogsSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
api_instance.search_audit_logs_with_pagination(opts) { |item| puts item }

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Search Audit Logs events returns "OK" response 
```
// Search Audit Logs events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_audit::AuditAPI;
use datadog_api_client::datadogV2::api_audit::SearchAuditLogsOptionalParams;
use datadog_api_client::datadogV2::model::AuditLogsQueryFilter;
use datadog_api_client::datadogV2::model::AuditLogsQueryOptions;
use datadog_api_client::datadogV2::model::AuditLogsQueryPageOptions;
use datadog_api_client::datadogV2::model::AuditLogsSearchEventsRequest;
use datadog_api_client::datadogV2::model::AuditLogsSort;

#[tokio::main]
async fn main() {
    let body = AuditLogsSearchEventsRequest::new()
        .filter(
            AuditLogsQueryFilter::new()
                .from("now-15m".to_string())
                .query("@type:session AND @session.type:user".to_string())
                .to("now".to_string()),
        )
        .options(
            AuditLogsQueryOptions::new()
                .time_offset(0)
                .timezone("GMT".to_string()),
        )
        .page(AuditLogsQueryPageOptions::new().limit(25))
        .sort(AuditLogsSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = AuditAPI::with_config(configuration);
    let resp = api
        .search_audit_logs(SearchAuditLogsOptionalParams::default().body(body))
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Search Audit Logs events returns "OK" response with pagination 
```
// Search Audit Logs events returns "OK" response with pagination
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_audit::AuditAPI;
use datadog_api_client::datadogV2::api_audit::SearchAuditLogsOptionalParams;
use datadog_api_client::datadogV2::model::AuditLogsQueryFilter;
use datadog_api_client::datadogV2::model::AuditLogsQueryOptions;
use datadog_api_client::datadogV2::model::AuditLogsQueryPageOptions;
use datadog_api_client::datadogV2::model::AuditLogsSearchEventsRequest;
use datadog_api_client::datadogV2::model::AuditLogsSort;
use futures_util::pin_mut;
use futures_util::stream::StreamExt;

#[tokio::main]
async fn main() {
    let body = AuditLogsSearchEventsRequest::new()
        .filter(
            AuditLogsQueryFilter::new()
                .from("now-15m".to_string())
                .to("now".to_string()),
        )
        .options(AuditLogsQueryOptions::new().timezone("GMT".to_string()))
        .page(AuditLogsQueryPageOptions::new().limit(2))
        .sort(AuditLogsSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = AuditAPI::with_config(configuration);
    let response =
        api.search_audit_logs_with_pagination(SearchAuditLogsOptionalParams::default().body(body));
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Search Audit Logs events returns "OK" response 
```
/**
 * Search Audit Logs events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuditApi(configuration);

const params: v2.AuditApiSearchAuditLogsRequest = {
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
  .searchAuditLogs(params)
  .then((data: v2.AuditLogsEventsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Search Audit Logs events returns "OK" response with pagination 
```
/**
 * Search Audit Logs events returns "OK" response with pagination
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuditApi(configuration);

const params: v2.AuditApiSearchAuditLogsRequest = {
  body: {
    filter: {
      from: "now-15m",
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
};

(async () => {
  try {
    for await (const item of apiInstance.searchAuditLogsWithPagination(
      params
    )) {
      console.log(item);
    }
  } catch (error) {
    console.error(error);
  }
})();

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a list of Audit Logs events](https://docs.datadoghq.com/api/latest/audit/#get-a-list-of-audit-logs-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/audit/#get-a-list-of-audit-logs-events-v2)


GET https://api.ap1.datadoghq.com/api/v2/audit/eventshttps://api.ap2.datadoghq.com/api/v2/audit/eventshttps://api.datadoghq.eu/api/v2/audit/eventshttps://api.ddog-gov.com/api/v2/audit/eventshttps://api.datadoghq.com/api/v2/audit/eventshttps://api.us3.datadoghq.com/api/v2/audit/eventshttps://api.us5.datadoghq.com/api/v2/audit/events
### Overview
List endpoint returns events that match a Audit Logs search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).
Use this endpoint to see your latest Audit Logs events.
This endpoint requires the `audit_logs_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
filter[query]
string
Search query following Audit Logs syntax.
filter[from]
string
Minimum timestamp for requested events.
filter[to]
string
Maximum timestamp for requested events.
sort
enum
Order of events in results.  
Allowed enum values: `timestamp, -timestamp`
page[cursor]
string
List following results with a cursor provided in the previous query.
page[limit]
integer
Maximum number of events in the response.
### Response
  * [200](https://docs.datadoghq.com/api/latest/audit/#ListAuditLogs-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/audit/#ListAuditLogs-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/audit/#ListAuditLogs-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/audit/#ListAuditLogs-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


Response object with all events matching the request and pagination information.
Field
Type
Description
data
[object]
Array of events matching the request.
attributes
object
JSON object containing all event attributes and their associated values.
attributes
object
JSON object of attributes from Audit Logs events.
message
string
Message of the event.
service
string
Name of the application or service generating Audit Logs events. This name is used to correlate Audit Logs to APM, so make sure you specify the same value when you use both products.
tags
[string]
Array of tags associated with your event.
timestamp
date-time
Timestamp of your event.
id
string
Unique ID of the event.
type
enum
Type of the event. Allowed enum values: `audit`
default: `audit`
links
object
Links attributes.
next
string
Link for the next set of results. Note that the request can also be made using the POST endpoint.
meta
object
The metadata associated with a request.
elapsed
int64
Time elapsed in milliseconds.
page
object
Paging attributes.
after
string
The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`.
request_id
string
The identifier of the request.
status
enum
The status of the response. Allowed enum values: `done,timeout`
warnings
[object]
A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response.
code
string
Unique code for this type of warning.
detail
string
Detailed explanation of this specific warning.
title
string
Short human-readable summary of the warning.
```
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "message": "string",
        "service": "web-app",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "audit"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/audit/event?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/audit/)
  * [Example](https://docs.datadoghq.com/api/latest/audit/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/audit/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/audit/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/audit/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/audit/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/audit/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/audit/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/audit/?code-lang=typescript)


#####  Get a list of Audit Logs events
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/audit/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of Audit Logs events
```
"""
Get a list of Audit Logs events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.audit_api import AuditApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuditApi(api_client)
    response = api_instance.list_audit_logs()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a list of Audit Logs events
```
# Get a list of Audit Logs events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuditAPI.new
p api_instance.list_audit_logs()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a list of Audit Logs events
```
// Get a list of Audit Logs events returns "OK" response

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
	api := datadogV2.NewAuditApi(apiClient)
	resp, r, err := api.ListAuditLogs(ctx, *datadogV2.NewListAuditLogsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditApi.ListAuditLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuditApi.ListAuditLogs`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a list of Audit Logs events
```
// Get a list of Audit Logs events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuditApi;
import com.datadog.api.client.v2.model.AuditLogsEventsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuditApi apiInstance = new AuditApi(defaultClient);

    try {
      AuditLogsEventsResponse result = apiInstance.listAuditLogs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditApi#listAuditLogs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a list of Audit Logs events
```
// Get a list of Audit Logs events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_audit::AuditAPI;
use datadog_api_client::datadogV2::api_audit::ListAuditLogsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AuditAPI::with_config(configuration);
    let resp = api
        .list_audit_logs(ListAuditLogsOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a list of Audit Logs events
```
/**
 * Get a list of Audit Logs events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuditApi(configuration);

apiInstance
  .listAuditLogs()
  .then((data: v2.AuditLogsEventsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=dc19c66a-60f3-4198-8ffe-e06e69e560a9&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=830fa690-e35b-4750-8694-b7601907dc02&pt=Audit&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faudit%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=dc19c66a-60f3-4198-8ffe-e06e69e560a9&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=830fa690-e35b-4750-8694-b7601907dc02&pt=Audit&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faudit%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=1797db4b-5d35-42d0-9f38-b8480cc60a7c&bo=2&sid=d4936d40f0be11f0ac22fbecbc28d170&vid=d4939990f0be11f08645c313e3c6d719&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Audit&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faudit%2F&r=&lt=1156&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=661964)
