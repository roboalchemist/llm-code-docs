# Source: https://docs.datadoghq.com/api/latest/spans

# Spans
Search and aggregate your spans from your Datadog platform over HTTP.
## [Get a list of spans](https://docs.datadoghq.com/api/latest/spans/#get-a-list-of-spans)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/spans/#get-a-list-of-spans-v2)


GET https://api.ap1.datadoghq.com/api/v2/spans/eventshttps://api.ap2.datadoghq.com/api/v2/spans/eventshttps://api.datadoghq.eu/api/v2/spans/eventshttps://api.ddog-gov.com/api/v2/spans/eventshttps://api.datadoghq.com/api/v2/spans/eventshttps://api.us3.datadoghq.com/api/v2/spans/eventshttps://api.us5.datadoghq.com/api/v2/spans/events
### Overview
List endpoint returns spans that match a span search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination?tab=v2api).
Use this endpoint to see your latest spans. This endpoint is rate limited to `300` requests per hour.
OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#spans) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter[query]
string
Search query following spans syntax.
filter[from]
string
Minimum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds).
filter[to]
string
Maximum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds).
sort
enum
Order of spans in results.  
Allowed enum values: `timestamp, -timestamp`
page[cursor]
string
List following results with a cursor provided in the previous query.
page[limit]
integer
Maximum number of spans in the response.
### Response
  * [200](https://docs.datadoghq.com/api/latest/spans/#ListSpansGet-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/spans/#ListSpansGet-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/spans/#ListSpansGet-403-v2)
  * [422](https://docs.datadoghq.com/api/latest/spans/#ListSpansGet-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/spans/#ListSpansGet-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


Response object with all spans matching the request and pagination information.
Field
Type
Description
data
[object]
Array of spans matching the request.
attributes
object
JSON object containing all span attributes and their associated values.
attributes
object
JSON object of attributes from your span.
custom
object
JSON object of custom spans data.
end_timestamp
date-time
End timestamp of your span.
env
string
Name of the environment from where the spans are being sent.
host
string
Name of the machine from where the spans are being sent.
ingestion_reason
string
The reason why the span was ingested.
parent_id
string
Id of the span that's parent of this span.
resource_hash
string
Unique identifier of the resource.
resource_name
string
The name of the resource.
retained_by
string
The reason why the span was indexed.
service
string
The name of the application or service generating the span events. It is used to switch from APM to Logs, so make sure you define the same value when you use both products.
single_span
boolean
Whether or not the span was collected as a stand-alone span. Always associated to "single_span" ingestion_reason if true.
span_id
string
Id of the span.
start_timestamp
date-time
Start timestamp of your span.
tags
[string]
Array of tags associated with your span.
trace_id
string
Id of the trace to which the span belongs.
type
string
The type of the span.
id
string
Unique ID of the Span.
type
enum
Type of the span. Allowed enum values: `spans`
default: `spans`
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
The time elapsed in milliseconds.
page
object
Paging attributes.
after
string
The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.
request_id
string
The identifier of the request.
status
enum
The status of the response. Allowed enum values: `done,timeout`
warnings
[object]
A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.
code
string
A unique code for this type of warning.
detail
string
A detailed explanation of this specific warning.
title
string
A short human-readable summary of the warning.
```
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

Copy
Bad Request.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden: Access denied.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Unprocessable Entity.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too many requests: The rate limit set by the API has been exceeded.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/spans/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/spans/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/spans/?code-lang=ruby)
  * [Java](https://docs.datadoghq.com/api/latest/spans/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/spans/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/spans/?code-lang=typescript)
  * [Go](https://docs.datadoghq.com/api/latest/spans/?code-lang=go)


#####  Get a list of spans
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of spans
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of spans
```
# Get a list of spans returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansAPI.new
p api_instance.list_spans_get()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of spans
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a list of spans
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a list of spans
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

#####  Get a list of spans
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

* * *
## [Search spans](https://docs.datadoghq.com/api/latest/spans/#search-spans)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/spans/#search-spans-v2)


POST https://api.ap1.datadoghq.com/api/v2/spans/events/searchhttps://api.ap2.datadoghq.com/api/v2/spans/events/searchhttps://api.datadoghq.eu/api/v2/spans/events/searchhttps://api.ddog-gov.com/api/v2/spans/events/searchhttps://api.datadoghq.com/api/v2/spans/events/searchhttps://api.us3.datadoghq.com/api/v2/spans/events/searchhttps://api.us5.datadoghq.com/api/v2/spans/events/search
### Overview
List endpoint returns spans that match a span search query. [Results are paginated](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination?tab=v2api).
Use this endpoint to build complex spans filtering and search. This endpoint is rate limited to `300` requests per hour.
OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#spans) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


Field
Type
Description
data
object
The object containing the query content.
attributes
object
The object containing all the query parameters.
filter
object
The search and filter query settings.
from
string
The minimum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).
default: `now-15m`
query
string
The search query - following the span search syntax.
default: `*`
to
string
The maximum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).
default: `now`
options
object
Global query options that are used during the query. Note: You should only supply timezone or time offset but not both otherwise the query will fail.
timeOffset
int64
The time offset (in seconds) to apply to the query.
timezone
string
The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).
default: `UTC`
page
object
Paging attributes for listing spans.
cursor
string
List following results with a cursor provided in the previous query.
limit
int32
Maximum number of spans in the response.
default: `10`
sort
enum
Sort parameters when querying spans. Allowed enum values: `timestamp,-timestamp`
type
enum
The type of resource. The value should always be search_request. Allowed enum values: `search_request`
default: `search_request`
#####  Search spans returns "OK" response
```
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

Copy
#####  Search spans returns "OK" response with pagination
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/spans/#ListSpans-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/spans/#ListSpans-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/spans/#ListSpans-403-v2)
  * [422](https://docs.datadoghq.com/api/latest/spans/#ListSpans-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/spans/#ListSpans-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


Response object with all spans matching the request and pagination information.
Field
Type
Description
data
[object]
Array of spans matching the request.
attributes
object
JSON object containing all span attributes and their associated values.
attributes
object
JSON object of attributes from your span.
custom
object
JSON object of custom spans data.
end_timestamp
date-time
End timestamp of your span.
env
string
Name of the environment from where the spans are being sent.
host
string
Name of the machine from where the spans are being sent.
ingestion_reason
string
The reason why the span was ingested.
parent_id
string
Id of the span that's parent of this span.
resource_hash
string
Unique identifier of the resource.
resource_name
string
The name of the resource.
retained_by
string
The reason why the span was indexed.
service
string
The name of the application or service generating the span events. It is used to switch from APM to Logs, so make sure you define the same value when you use both products.
single_span
boolean
Whether or not the span was collected as a stand-alone span. Always associated to "single_span" ingestion_reason if true.
span_id
string
Id of the span.
start_timestamp
date-time
Start timestamp of your span.
tags
[string]
Array of tags associated with your span.
trace_id
string
Id of the trace to which the span belongs.
type
string
The type of the span.
id
string
Unique ID of the Span.
type
enum
Type of the span. Allowed enum values: `spans`
default: `spans`
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
The time elapsed in milliseconds.
page
object
Paging attributes.
after
string
The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.
request_id
string
The identifier of the request.
status
enum
The status of the response. Allowed enum values: `done,timeout`
warnings
[object]
A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.
code
string
A unique code for this type of warning.
detail
string
A detailed explanation of this specific warning.
title
string
A short human-readable summary of the warning.
```
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

Copy
Bad Request.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden: Access denied.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Unprocessable Entity.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too many requests: The rate limit set by the API has been exceeded.
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/spans/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/spans/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/spans/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/spans/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/spans/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/spans/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/spans/?code-lang=typescript)


#####  Search spans returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/events/search" \
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

                        
```

#####  Search spans returns "OK" response with pagination
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/events/search" \
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

                        
```

#####  Search spans returns "OK" response 
```
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

Copy
#####  Search spans returns "OK" response with pagination 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Search spans returns "OK" response 
```
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

Copy
#####  Search spans returns "OK" response with pagination 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Search spans returns "OK" response 
```
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

Copy
#####  Search spans returns "OK" response with pagination 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search spans returns "OK" response 
```
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

Copy
#####  Search spans returns "OK" response with pagination 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search spans returns "OK" response 
```
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

Copy
#####  Search spans returns "OK" response with pagination 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Search spans returns "OK" response 
```
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

Copy
#####  Search spans returns "OK" response with pagination 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Aggregate spans](https://docs.datadoghq.com/api/latest/spans/#aggregate-spans)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/spans/#aggregate-spans-v2)


POST https://api.ap1.datadoghq.com/api/v2/spans/analytics/aggregatehttps://api.ap2.datadoghq.com/api/v2/spans/analytics/aggregatehttps://api.datadoghq.eu/api/v2/spans/analytics/aggregatehttps://api.ddog-gov.com/api/v2/spans/analytics/aggregatehttps://api.datadoghq.com/api/v2/spans/analytics/aggregatehttps://api.us3.datadoghq.com/api/v2/spans/analytics/aggregatehttps://api.us5.datadoghq.com/api/v2/spans/analytics/aggregate
### Overview
The API endpoint to aggregate spans into buckets and compute metrics and timeseries. This endpoint is rate limited to `300` requests per hour. This endpoint requires the `apm_read` permission.
OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#spans) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


Field
Type
Description
data
object
The object containing the query content.
attributes
object
The object containing all the query parameters.
compute
[object]
The list of metrics or timeseries to compute for the retrieved buckets.
aggregation [_required_]
enum
An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`
interval
string
The time buckets' size (only used for type=timeseries) Defaults to a resolution of 150 points.
metric
string
The metric to use.
type
enum
The type of compute. Allowed enum values: `timeseries,total`
default: `total`
filter
object
The search and filter query settings.
from
string
The minimum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).
default: `now-15m`
query
string
The search query - following the span search syntax.
default: `*`
to
string
The maximum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).
default: `now`
group_by
[object]
The rules for the group by.
facet [_required_]
string
The name of the facet to use (required).
histogram
object
Used to perform a histogram computation (only for measure facets). Note: At most 100 buckets are allowed, the number of buckets is (max - min)/interval.
interval [_required_]
double
The bin size of the histogram buckets.
max [_required_]
double
The maximum value for the measure used in the histogram (values greater than this one are filtered out).
min [_required_]
double
The minimum value for the measure used in the histogram (values smaller than this one are filtered out).
limit
int64
The maximum buckets to return for this group by.
default: `10`
missing
<oneOf>
The value to use for spans that don't have the facet used to group by.
Option 1
string
The missing value to use if there is string valued facet.
Option 2
double
The missing value to use if there is a number valued facet.
sort
object
A sort rule.
aggregation
enum
An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median`
metric
string
The metric to sort by (only used for `type=measure`).
order
enum
The order to use, ascending or descending. Allowed enum values: `asc,desc`
type
enum
The type of sorting algorithm. Allowed enum values: `alphabetical,measure`
default: `alphabetical`
total
<oneOf>
A resulting object to put the given computes in over all the matching records.
Option 1
boolean
If set to true, creates an additional bucket labeled "$facet_total".
Option 2
string
A string to use as the key value for the total bucket.
Option 3
double
A number to use as the key value for the total bucket.
options
object
Global query options that are used during the query. Note: You should only supply timezone or time offset but not both otherwise the query will fail.
timeOffset
int64
The time offset (in seconds) to apply to the query.
timezone
string
The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).
default: `UTC`
type
enum
The type of resource. The value should always be aggregate_request. Allowed enum values: `aggregate_request`
default: `aggregate_request`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/spans/#AggregateSpans-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/spans/#AggregateSpans-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/spans/#AggregateSpans-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/spans/#AggregateSpans-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


The response object for the spans aggregate API endpoint.
Field
Type
Description
data
[object]
The list of matching buckets, one item per bucket.
attributes
object
A bucket values.
by
object
The key, value pairs for each group by.
<any-key>
The values for each group by.
compute
object
The compute data.
computes
object
A map of the metric name -> value for regular compute or list of values for a timeseries.
<any-key>
<oneOf>
A bucket value, can be either a timeseries or a single value.
Option 1
string
A single string value.
Option 2
double
A single number value.
Option 3
[object]
A timeseries array.
time
string
The time value for this point.
value
double
The value for this point.
id
string
ID of the spans aggregate.
type
enum
The spans aggregate bucket type. Allowed enum values: `bucket`
meta
object
The metadata associated with a request.
elapsed
int64
The time elapsed in milliseconds.
request_id
string
The identifier of the request.
status
enum
The status of the response. Allowed enum values: `done,timeout`
warnings
[object]
A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response.
code
string
A unique code for this type of warning.
detail
string
A detailed explanation of this specific warning.
title
string
A short human-readable summary of the warning.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


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
  * [Model](https://docs.datadoghq.com/api/latest/spans/)
  * [Example](https://docs.datadoghq.com/api/latest/spans/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/spans/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/spans/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/spans/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/spans/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/spans/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/spans/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/spans/?code-lang=typescript)


#####  Aggregate spans returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spans/analytics/aggregate" \
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

                        
```

#####  Aggregate spans returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Aggregate spans returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Aggregate spans returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Aggregate spans returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Aggregate spans returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Aggregate spans returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d5f5b39f-7b93-46dc-9f7a-1d49f13be603&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d7a19fc3-cce8-4282-8140-55ff586f3989&pt=Spans&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fspans%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d5f5b39f-7b93-46dc-9f7a-1d49f13be603&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d7a19fc3-cce8-4282-8140-55ff586f3989&pt=Spans&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fspans%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=b4e94658-6cb7-4e39-ad2f-fa846362759c&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Spans&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fspans%2F&r=&lt=10866&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=958333)
