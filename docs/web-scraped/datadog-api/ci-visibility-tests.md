# Source: https://docs.datadoghq.com/api/latest/ci-visibility-tests

# CI Visibility Tests
Search or aggregate your CI Visibility test events over HTTP. See the [Test Visibility in Datadog page](https://docs.datadoghq.com/tests/) for more information.
## [Get a list of tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#get-a-list-of-tests-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#get-a-list-of-tests-events-v2)


GET https://api.ap1.datadoghq.com/api/v2/ci/tests/eventshttps://api.ap2.datadoghq.com/api/v2/ci/tests/eventshttps://api.datadoghq.eu/api/v2/ci/tests/eventshttps://api.ddog-gov.com/api/v2/ci/tests/eventshttps://api.datadoghq.com/api/v2/ci/tests/eventshttps://api.us3.datadoghq.com/api/v2/ci/tests/eventshttps://api.us5.datadoghq.com/api/v2/ci/tests/events
### Overview
List endpoint returns CI Visibility test events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/). [Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).
Use this endpoint to see your latest test events.
This endpoint requires any of the following permissions:
* `ci_visibility_read`
* `test_optimization_read`
  

OAuth apps require the `test_optimization_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ci-visibility-tests) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter[query]
string
Search query following log syntax.
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
  * [200](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#ListCIAppTestEvents-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#ListCIAppTestEvents-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#ListCIAppTestEvents-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#ListCIAppTestEvents-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


Response object with all test events matching the request and pagination information.
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
JSON object of attributes from CI Visibility test events.
tags
[string]
Array of tags associated with your event.
test_level
enum
Test run level. Allowed enum values: `session,module,suite,test`
id
string
Unique ID of the event.
type
enum
Type of the event. Allowed enum values: `citest`
links
object
Links attributes.
next
string
Link for the next set of results. The request can also be made using the POST endpoint.
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
        "tags": [
          "team:A"
        ],
        "test_level": "test"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "citest"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/ci/tests/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=typescript)


#####  Get a list of tests events
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/tests/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of tests events
```
"""
Get a list of tests events returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    response = api_instance.list_ci_app_test_events(
        filter_query="@test.service:web-ui-tests",
        filter_from=(datetime.now() + relativedelta(seconds=-30)),
        filter_to=datetime.now(),
        page_limit=5,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of tests events
```
# Get a list of tests events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityTestsAPI.new
opts = {
  filter_query: "@test.service:web-ui-tests",
  filter_from: (Time.now + -30),
  filter_to: Time.now,
  page_limit: 5,
}
p api_instance.list_ci_app_test_events(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of tests events
```
// Get a list of tests events returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityTestsApi(apiClient)
	resp, r, err := api.ListCIAppTestEvents(ctx, *datadogV2.NewListCIAppTestEventsOptionalParameters().WithFilterQuery("@test.service:web-ui-tests").WithFilterFrom(time.Now().Add(time.Second * -30)).WithFilterTo(time.Now()).WithPageLimit(5))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityTestsApi.ListCIAppTestEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityTestsApi.ListCIAppTestEvents`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of tests events
```
// Get a list of tests events returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityTestsApi;
import com.datadog.api.client.v2.api.CiVisibilityTestsApi.ListCIAppTestEventsOptionalParameters;
import com.datadog.api.client.v2.model.CIAppTestEventsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityTestsApi apiInstance = new CiVisibilityTestsApi(defaultClient);

    try {
      CIAppTestEventsResponse result =
          apiInstance.listCIAppTestEvents(
              new ListCIAppTestEventsOptionalParameters()
                  .filterQuery("@test.service:web-ui-tests")
                  .filterFrom(OffsetDateTime.now().plusSeconds(-30))
                  .filterTo(OffsetDateTime.now())
                  .pageLimit(5));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CiVisibilityTestsApi#listCIAppTestEvents");
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

#####  Get a list of tests events
```
// Get a list of tests events returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_tests::CIVisibilityTestsAPI;
use datadog_api_client::datadogV2::api_ci_visibility_tests::ListCIAppTestEventsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityTestsAPI::with_config(configuration);
    let resp = api
        .list_ci_app_test_events(
            ListCIAppTestEventsOptionalParams::default()
                .filter_query("@test.service:web-ui-tests".to_string())
                .filter_from(
                    DateTime::parse_from_rfc3339("2021-11-11T11:10:41+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .filter_to(
                    DateTime::parse_from_rfc3339("2021-11-11T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .page_limit(5),
        )
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

#####  Get a list of tests events
```
/**
 * Get a list of tests events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityTestsApi(configuration);

const params: v2.CIVisibilityTestsApiListCIAppTestEventsRequest = {
  filterQuery: "@test.service:web-ui-tests",
  filterFrom: new Date(new Date().getTime() + -30 * 1000),
  filterTo: new Date(),
  pageLimit: 5,
};

apiInstance
  .listCIAppTestEvents(params)
  .then((data: v2.CIAppTestEventsResponse) => {
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
## [Search tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#search-tests-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#search-tests-events-v2)


POST https://api.ap1.datadoghq.com/api/v2/ci/tests/events/searchhttps://api.ap2.datadoghq.com/api/v2/ci/tests/events/searchhttps://api.datadoghq.eu/api/v2/ci/tests/events/searchhttps://api.ddog-gov.com/api/v2/ci/tests/events/searchhttps://api.datadoghq.com/api/v2/ci/tests/events/searchhttps://api.us3.datadoghq.com/api/v2/ci/tests/events/searchhttps://api.us5.datadoghq.com/api/v2/ci/tests/events/search
### Overview
List endpoint returns CI Visibility test events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/). [Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).
Use this endpoint to build complex events filtering and search.
This endpoint requires any of the following permissions:
* `ci_visibility_read`
* `test_optimization_read`
  

OAuth apps require the `test_optimization_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ci-visibility-tests) to access this endpoint.
### Request
#### Body Data 
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


Field
Type
Description
filter
object
The search and filter query settings.
from
string
The minimum time for the requested events; supports date, math, and regular timestamps (in milliseconds).
default: `now-15m`
query
string
The search query following the CI Visibility Explorer search syntax.
default: `*`
to
string
The maximum time for the requested events, supports date, math, and regular timestamps (in milliseconds).
default: `now`
options
object
Global query options that are used during the query. Only supply timezone or time offset, not both. Otherwise, the query fails.
time_offset
int64
The time offset (in seconds) to apply to the query.
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
#####  Search tests events returns "OK" response
```
{
  "filter": {
    "from": "now-15m",
    "query": "@test.service:web-ui-tests AND @test.status:skip",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 25
  },
  "sort": "timestamp"
}
```

Copy
#####  Search tests events returns "OK" response with pagination
```
{
  "filter": {
    "from": "now-15m",
    "query": "@test.status:pass AND -@language:python",
    "to": "now"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#SearchCIAppTestEvents-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#SearchCIAppTestEvents-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#SearchCIAppTestEvents-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#SearchCIAppTestEvents-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


Response object with all test events matching the request and pagination information.
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
JSON object of attributes from CI Visibility test events.
tags
[string]
Array of tags associated with your event.
test_level
enum
Test run level. Allowed enum values: `session,module,suite,test`
id
string
Unique ID of the event.
type
enum
Type of the event. Allowed enum values: `citest`
links
object
Links attributes.
next
string
Link for the next set of results. The request can also be made using the POST endpoint.
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
        "tags": [
          "team:A"
        ],
        "test_level": "test"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "citest"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/ci/tests/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=typescript)


#####  Search tests events returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/tests/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "query": "@test.service:web-ui-tests AND @test.status:skip",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 25
  },
  "sort": "timestamp"
}
EOF  

                        
```

#####  Search tests events returns "OK" response with pagination
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/tests/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "query": "@test.status:pass AND -@language:python",
    "to": "now"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
EOF  

                        
```

#####  Search tests events returns "OK" response 
```
// Search tests events returns "OK" response

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
	body := datadogV2.CIAppTestEventsRequest{
		Filter: &datadogV2.CIAppTestsQueryFilter{
			From:  datadog.PtrString("now-15m"),
			Query: datadog.PtrString("@test.service:web-ui-tests AND @test.status:skip"),
			To:    datadog.PtrString("now"),
		},
		Options: &datadogV2.CIAppQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
		Page: &datadogV2.CIAppQueryPageOptions{
			Limit: datadog.PtrInt32(25),
		},
		Sort: datadogV2.CIAPPSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityTestsApi(apiClient)
	resp, r, err := api.SearchCIAppTestEvents(ctx, *datadogV2.NewSearchCIAppTestEventsOptionalParameters().WithBody(body))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityTestsApi.SearchCIAppTestEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityTestsApi.SearchCIAppTestEvents`:\n%s\n", responseContent)
}

```

Copy
#####  Search tests events returns "OK" response with pagination 
```
// Search tests events returns "OK" response with pagination

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
	body := datadogV2.CIAppTestEventsRequest{
		Filter: &datadogV2.CIAppTestsQueryFilter{
			From:  datadog.PtrString("now-15m"),
			Query: datadog.PtrString("@test.status:pass AND -@language:python"),
			To:    datadog.PtrString("now"),
		},
		Page: &datadogV2.CIAppQueryPageOptions{
			Limit: datadog.PtrInt32(2),
		},
		Sort: datadogV2.CIAPPSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityTestsApi(apiClient)
	resp, _ := api.SearchCIAppTestEventsWithPagination(ctx, *datadogV2.NewSearchCIAppTestEventsOptionalParameters().WithBody(body))

	for paginationResult := range resp {
		if paginationResult.Error != nil {
			fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityTestsApi.SearchCIAppTestEvents`: %v\n", paginationResult.Error)
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

#####  Search tests events returns "OK" response 
```
// Search tests events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityTestsApi;
import com.datadog.api.client.v2.api.CiVisibilityTestsApi.SearchCIAppTestEventsOptionalParameters;
import com.datadog.api.client.v2.model.CIAppQueryOptions;
import com.datadog.api.client.v2.model.CIAppQueryPageOptions;
import com.datadog.api.client.v2.model.CIAppSort;
import com.datadog.api.client.v2.model.CIAppTestEventsRequest;
import com.datadog.api.client.v2.model.CIAppTestEventsResponse;
import com.datadog.api.client.v2.model.CIAppTestsQueryFilter;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityTestsApi apiInstance = new CiVisibilityTestsApi(defaultClient);

    CIAppTestEventsRequest body =
        new CIAppTestEventsRequest()
            .filter(
                new CIAppTestsQueryFilter()
                    .from("now-15m")
                    .query("@test.service:web-ui-tests AND @test.status:skip")
                    .to("now"))
            .options(new CIAppQueryOptions().timezone("GMT"))
            .page(new CIAppQueryPageOptions().limit(25))
            .sort(CIAppSort.TIMESTAMP_ASCENDING);

    try {
      CIAppTestEventsResponse result =
          apiInstance.searchCIAppTestEvents(
              new SearchCIAppTestEventsOptionalParameters().body(body));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CiVisibilityTestsApi#searchCIAppTestEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Search tests events returns "OK" response with pagination 
```
// Search tests events returns "OK" response with pagination

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.PaginationIterable;
import com.datadog.api.client.v2.api.CiVisibilityTestsApi;
import com.datadog.api.client.v2.api.CiVisibilityTestsApi.SearchCIAppTestEventsOptionalParameters;
import com.datadog.api.client.v2.model.CIAppQueryPageOptions;
import com.datadog.api.client.v2.model.CIAppSort;
import com.datadog.api.client.v2.model.CIAppTestEvent;
import com.datadog.api.client.v2.model.CIAppTestEventsRequest;
import com.datadog.api.client.v2.model.CIAppTestsQueryFilter;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityTestsApi apiInstance = new CiVisibilityTestsApi(defaultClient);

    CIAppTestEventsRequest body =
        new CIAppTestEventsRequest()
            .filter(
                new CIAppTestsQueryFilter()
                    .from("now-15m")
                    .query("@test.status:pass AND -@language:python")
                    .to("now"))
            .page(new CIAppQueryPageOptions().limit(2))
            .sort(CIAppSort.TIMESTAMP_ASCENDING);

    try {
      PaginationIterable<CIAppTestEvent> iterable =
          apiInstance.searchCIAppTestEventsWithPagination(
              new SearchCIAppTestEventsOptionalParameters().body(body));

      for (CIAppTestEvent item : iterable) {
        System.out.println(item);
      }
    } catch (RuntimeException e) {
      System.err.println(
          "Exception when calling CiVisibilityTestsApi#searchCIAppTestEventsWithPagination");
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

#####  Search tests events returns "OK" response 
```
"""
Search tests events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort import CIAppSort
from datadog_api_client.v2.model.ci_app_test_events_request import CIAppTestEventsRequest
from datadog_api_client.v2.model.ci_app_tests_query_filter import CIAppTestsQueryFilter

body = CIAppTestEventsRequest(
    filter=CIAppTestsQueryFilter(
        _from="now-15m",
        query="@test.service:web-ui-tests AND @test.status:skip",
        to="now",
    ),
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
    page=CIAppQueryPageOptions(
        limit=25,
    ),
    sort=CIAppSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    response = api_instance.search_ci_app_test_events(body=body)

    print(response)

```

Copy
#####  Search tests events returns "OK" response with pagination 
```
"""
Search tests events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort import CIAppSort
from datadog_api_client.v2.model.ci_app_test_events_request import CIAppTestEventsRequest
from datadog_api_client.v2.model.ci_app_tests_query_filter import CIAppTestsQueryFilter

body = CIAppTestEventsRequest(
    filter=CIAppTestsQueryFilter(
        _from="now-15m",
        query="@test.status:pass AND -@language:python",
        to="now",
    ),
    page=CIAppQueryPageOptions(
        limit=2,
    ),
    sort=CIAppSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    items = api_instance.search_ci_app_test_events_with_pagination(body=body)
    for item in items:
        print(item)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search tests events returns "OK" response 
```
# Search tests events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityTestsAPI.new

body = DatadogAPIClient::V2::CIAppTestEventsRequest.new({
  filter: DatadogAPIClient::V2::CIAppTestsQueryFilter.new({
    from: "now-15m",
    query: "@test.service:web-ui-tests AND @test.status:skip",
    to: "now",
  }),
  options: DatadogAPIClient::V2::CIAppQueryOptions.new({
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::CIAppQueryPageOptions.new({
    limit: 25,
  }),
  sort: DatadogAPIClient::V2::CIAppSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
p api_instance.search_ci_app_test_events(opts)

```

Copy
#####  Search tests events returns "OK" response with pagination 
```
# Search tests events returns "OK" response with pagination

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityTestsAPI.new

body = DatadogAPIClient::V2::CIAppTestEventsRequest.new({
  filter: DatadogAPIClient::V2::CIAppTestsQueryFilter.new({
    from: "now-15m",
    query: "@test.status:pass AND -@language:python",
    to: "now",
  }),
  page: DatadogAPIClient::V2::CIAppQueryPageOptions.new({
    limit: 2,
  }),
  sort: DatadogAPIClient::V2::CIAppSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
api_instance.search_ci_app_test_events_with_pagination(opts) { |item| puts item }

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search tests events returns "OK" response 
```
// Search tests events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_tests::CIVisibilityTestsAPI;
use datadog_api_client::datadogV2::api_ci_visibility_tests::SearchCIAppTestEventsOptionalParams;
use datadog_api_client::datadogV2::model::CIAppQueryOptions;
use datadog_api_client::datadogV2::model::CIAppQueryPageOptions;
use datadog_api_client::datadogV2::model::CIAppSort;
use datadog_api_client::datadogV2::model::CIAppTestEventsRequest;
use datadog_api_client::datadogV2::model::CIAppTestsQueryFilter;

#[tokio::main]
async fn main() {
    let body = CIAppTestEventsRequest::new()
        .filter(
            CIAppTestsQueryFilter::new()
                .from("now-15m".to_string())
                .query("@test.service:web-ui-tests AND @test.status:skip".to_string())
                .to("now".to_string()),
        )
        .options(CIAppQueryOptions::new().timezone("GMT".to_string()))
        .page(CIAppQueryPageOptions::new().limit(25))
        .sort(CIAppSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityTestsAPI::with_config(configuration);
    let resp = api
        .search_ci_app_test_events(SearchCIAppTestEventsOptionalParams::default().body(body))
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Search tests events returns "OK" response with pagination 
```
// Search tests events returns "OK" response with pagination
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_tests::CIVisibilityTestsAPI;
use datadog_api_client::datadogV2::api_ci_visibility_tests::SearchCIAppTestEventsOptionalParams;
use datadog_api_client::datadogV2::model::CIAppQueryPageOptions;
use datadog_api_client::datadogV2::model::CIAppSort;
use datadog_api_client::datadogV2::model::CIAppTestEventsRequest;
use datadog_api_client::datadogV2::model::CIAppTestsQueryFilter;
use futures_util::pin_mut;
use futures_util::stream::StreamExt;

#[tokio::main]
async fn main() {
    let body = CIAppTestEventsRequest::new()
        .filter(
            CIAppTestsQueryFilter::new()
                .from("now-15m".to_string())
                .query("@test.status:pass AND -@language:python".to_string())
                .to("now".to_string()),
        )
        .page(CIAppQueryPageOptions::new().limit(2))
        .sort(CIAppSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityTestsAPI::with_config(configuration);
    let response = api.search_ci_app_test_events_with_pagination(
        SearchCIAppTestEventsOptionalParams::default().body(body),
    );
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

#####  Search tests events returns "OK" response 
```
/**
 * Search tests events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityTestsApi(configuration);

const params: v2.CIVisibilityTestsApiSearchCIAppTestEventsRequest = {
  body: {
    filter: {
      from: "now-15m",
      query: "@test.service:web-ui-tests AND @test.status:skip",
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
};

apiInstance
  .searchCIAppTestEvents(params)
  .then((data: v2.CIAppTestEventsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Search tests events returns "OK" response with pagination 
```
/**
 * Search tests events returns "OK" response with pagination
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityTestsApi(configuration);

const params: v2.CIVisibilityTestsApiSearchCIAppTestEventsRequest = {
  body: {
    filter: {
      from: "now-15m",
      query: "@test.status:pass AND -@language:python",
      to: "now",
    },
    page: {
      limit: 2,
    },
    sort: "timestamp",
  },
};

(async () => {
  try {
    for await (const item of apiInstance.searchCIAppTestEventsWithPagination(
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Aggregate tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#aggregate-tests-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#aggregate-tests-events-v2)


POST https://api.ap1.datadoghq.com/api/v2/ci/tests/analytics/aggregatehttps://api.ap2.datadoghq.com/api/v2/ci/tests/analytics/aggregatehttps://api.datadoghq.eu/api/v2/ci/tests/analytics/aggregatehttps://api.ddog-gov.com/api/v2/ci/tests/analytics/aggregatehttps://api.datadoghq.com/api/v2/ci/tests/analytics/aggregatehttps://api.us3.datadoghq.com/api/v2/ci/tests/analytics/aggregatehttps://api.us5.datadoghq.com/api/v2/ci/tests/analytics/aggregate
### Overview
The API endpoint to aggregate CI Visibility test events into buckets of computed metrics and timeseries. This endpoint requires any of the following permissions:
* `ci_visibility_read`
* `test_optimization_read`
  

OAuth apps require the `test_optimization_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ci-visibility-tests) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


Field
Type
Description
compute
[object]
The list of metrics or timeseries to compute for the retrieved buckets.
aggregation [_required_]
enum
An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median,latest,earliest,most_frequent,delta`
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
The minimum time for the requested events; supports date, math, and regular timestamps (in milliseconds).
default: `now-15m`
query
string
The search query following the CI Visibility Explorer search syntax.
default: `*`
to
string
The maximum time for the requested events, supports date, math, and regular timestamps (in milliseconds).
default: `now`
group_by
[object]
The rules for the group-by.
facet [_required_]
string
The name of the facet to use (required).
histogram
object
Used to perform a histogram computation (only for measure facets). At most, 100 buckets are allowed, the number of buckets is `(max - min)/interval`.
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
The maximum buckets to return for this group-by.
default: `10`
missing
<oneOf>
The value to use for logs that don't have the facet used to group-by.
Option 1
string
The missing value to use if there is a string valued facet.
Option 2
double
The missing value to use if there is a number valued facet.
sort
object
A sort rule. The `aggregation` field is required when `type` is `measure`.
aggregation
enum
An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median,latest,earliest,most_frequent,delta`
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
Global query options that are used during the query. Only supply timezone or time offset, not both. Otherwise, the query fails.
time_offset
int64
The time offset (in seconds) to apply to the query.
timezone
string
The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).
default: `UTC`
```
{
  "compute": [
    {
      "aggregation": "count",
      "metric": "@test.is_flaky",
      "type": "total"
    }
  ],
  "filter": {
    "from": "now-15m",
    "query": "@language:(python OR go)",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "@git.branch",
      "limit": 10,
      "sort": {
        "order": "asc"
      },
      "total": false
    }
  ],
  "options": {
    "timezone": "GMT"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#AggregateCIAppTestEvents-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#AggregateCIAppTestEvents-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#AggregateCIAppTestEvents-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#AggregateCIAppTestEvents-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


The response object for the test events aggregate API endpoint.
Field
Type
Description
data
object
The query results.
buckets
[object]
The list of matching buckets, one item per bucket.
by
object
The key-value pairs for each group-by.
<any-key>
The values for each group-by.
computes
object
A map of the metric name to value for regular compute, or a list of values for a timeseries.
<any-key>
<oneOf>
A bucket value, can either be a timeseries or a single value.
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
date-time
The time value for this point.
value
double
The value for this point.
links
object
Links attributes.
next
string
Link for the next set of results. The request can also be made using the POST endpoint.
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
A unique code for this type of warning.
detail
string
A detailed explanation of this specific warning.
title
string
A short human-readable summary of the warning.
```
{
  "data": {
    "buckets": [
      {
        "by": {
          "<any-key>": "undefined"
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
    "next": "https://app.datadoghq.com/api/v2/ci/tests/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Model](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)
  * [Example](https://docs.datadoghq.com/api/latest/ci-visibility-tests/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/ci-visibility-tests/?code-lang=typescript)


#####  Aggregate tests events returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/tests/analytics/aggregate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "compute": [
    {
      "aggregation": "count",
      "metric": "@test.is_flaky",
      "type": "total"
    }
  ],
  "filter": {
    "from": "now-15m",
    "query": "@language:(python OR go)",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "@git.branch",
      "limit": 10,
      "sort": {
        "order": "asc"
      },
      "total": false
    }
  ],
  "options": {
    "timezone": "GMT"
  }
}
EOF  

                        
```

#####  Aggregate tests events returns "OK" response
```
// Aggregate tests events returns "OK" response

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
	body := datadogV2.CIAppTestsAggregateRequest{
		Compute: []datadogV2.CIAppCompute{
			{
				Aggregation: datadogV2.CIAPPAGGREGATIONFUNCTION_COUNT,
				Metric:      datadog.PtrString("@test.is_flaky"),
				Type:        datadogV2.CIAPPCOMPUTETYPE_TOTAL.Ptr(),
			},
		},
		Filter: &datadogV2.CIAppTestsQueryFilter{
			From:  datadog.PtrString("now-15m"),
			Query: datadog.PtrString("@language:(python OR go)"),
			To:    datadog.PtrString("now"),
		},
		GroupBy: []datadogV2.CIAppTestsGroupBy{
			{
				Facet: "@git.branch",
				Limit: datadog.PtrInt64(10),
				Sort: &datadogV2.CIAppAggregateSort{
					Order: datadogV2.CIAPPSORTORDER_ASCENDING.Ptr(),
				},
				Total: &datadogV2.CIAppGroupByTotal{
					CIAppGroupByTotalBoolean: datadog.PtrBool(false)},
			},
		},
		Options: &datadogV2.CIAppQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityTestsApi(apiClient)
	resp, r, err := api.AggregateCIAppTestEvents(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityTestsApi.AggregateCIAppTestEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityTestsApi.AggregateCIAppTestEvents`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Aggregate tests events returns "OK" response
```
// Aggregate tests events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityTestsApi;
import com.datadog.api.client.v2.model.CIAppAggregateSort;
import com.datadog.api.client.v2.model.CIAppAggregationFunction;
import com.datadog.api.client.v2.model.CIAppCompute;
import com.datadog.api.client.v2.model.CIAppComputeType;
import com.datadog.api.client.v2.model.CIAppGroupByTotal;
import com.datadog.api.client.v2.model.CIAppQueryOptions;
import com.datadog.api.client.v2.model.CIAppSortOrder;
import com.datadog.api.client.v2.model.CIAppTestsAggregateRequest;
import com.datadog.api.client.v2.model.CIAppTestsAnalyticsAggregateResponse;
import com.datadog.api.client.v2.model.CIAppTestsGroupBy;
import com.datadog.api.client.v2.model.CIAppTestsQueryFilter;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityTestsApi apiInstance = new CiVisibilityTestsApi(defaultClient);

    CIAppTestsAggregateRequest body =
        new CIAppTestsAggregateRequest()
            .compute(
                Collections.singletonList(
                    new CIAppCompute()
                        .aggregation(CIAppAggregationFunction.COUNT)
                        .metric("@test.is_flaky")
                        .type(CIAppComputeType.TOTAL)))
            .filter(
                new CIAppTestsQueryFilter()
                    .from("now-15m")
                    .query("@language:(python OR go)")
                    .to("now"))
            .groupBy(
                Collections.singletonList(
                    new CIAppTestsGroupBy()
                        .facet("@git.branch")
                        .limit(10L)
                        .sort(new CIAppAggregateSort().order(CIAppSortOrder.ASCENDING))
                        .total(new CIAppGroupByTotal(false))))
            .options(new CIAppQueryOptions().timezone("GMT"));

    try {
      CIAppTestsAnalyticsAggregateResponse result = apiInstance.aggregateCIAppTestEvents(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CiVisibilityTestsApi#aggregateCIAppTestEvents");
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

#####  Aggregate tests events returns "OK" response
```
"""
Aggregate tests events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi
from datadog_api_client.v2.model.ci_app_aggregate_sort import CIAppAggregateSort
from datadog_api_client.v2.model.ci_app_aggregation_function import CIAppAggregationFunction
from datadog_api_client.v2.model.ci_app_compute import CIAppCompute
from datadog_api_client.v2.model.ci_app_compute_type import CIAppComputeType
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_sort_order import CIAppSortOrder
from datadog_api_client.v2.model.ci_app_tests_aggregate_request import CIAppTestsAggregateRequest
from datadog_api_client.v2.model.ci_app_tests_group_by import CIAppTestsGroupBy
from datadog_api_client.v2.model.ci_app_tests_query_filter import CIAppTestsQueryFilter

body = CIAppTestsAggregateRequest(
    compute=[
        CIAppCompute(
            aggregation=CIAppAggregationFunction.COUNT,
            metric="@test.is_flaky",
            type=CIAppComputeType.TOTAL,
        ),
    ],
    filter=CIAppTestsQueryFilter(
        _from="now-15m",
        query="@language:(python OR go)",
        to="now",
    ),
    group_by=[
        CIAppTestsGroupBy(
            facet="@git.branch",
            limit=10,
            sort=CIAppAggregateSort(
                order=CIAppSortOrder.ASCENDING,
            ),
            total=False,
        ),
    ],
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    response = api_instance.aggregate_ci_app_test_events(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Aggregate tests events returns "OK" response
```
# Aggregate tests events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityTestsAPI.new

body = DatadogAPIClient::V2::CIAppTestsAggregateRequest.new({
  compute: [
    DatadogAPIClient::V2::CIAppCompute.new({
      aggregation: DatadogAPIClient::V2::CIAppAggregationFunction::COUNT,
      metric: "@test.is_flaky",
      type: DatadogAPIClient::V2::CIAppComputeType::TOTAL,
    }),
  ],
  filter: DatadogAPIClient::V2::CIAppTestsQueryFilter.new({
    from: "now-15m",
    query: "@language:(python OR go)",
    to: "now",
  }),
  group_by: [
    DatadogAPIClient::V2::CIAppTestsGroupBy.new({
      facet: "@git.branch",
      limit: 10,
      sort: DatadogAPIClient::V2::CIAppAggregateSort.new({
        order: DatadogAPIClient::V2::CIAppSortOrder::ASCENDING,
      }),
      total: false,
    }),
  ],
  options: DatadogAPIClient::V2::CIAppQueryOptions.new({
    timezone: "GMT",
  }),
})
p api_instance.aggregate_ci_app_test_events(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Aggregate tests events returns "OK" response
```
// Aggregate tests events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_tests::CIVisibilityTestsAPI;
use datadog_api_client::datadogV2::model::CIAppAggregateSort;
use datadog_api_client::datadogV2::model::CIAppAggregationFunction;
use datadog_api_client::datadogV2::model::CIAppCompute;
use datadog_api_client::datadogV2::model::CIAppComputeType;
use datadog_api_client::datadogV2::model::CIAppGroupByTotal;
use datadog_api_client::datadogV2::model::CIAppQueryOptions;
use datadog_api_client::datadogV2::model::CIAppSortOrder;
use datadog_api_client::datadogV2::model::CIAppTestsAggregateRequest;
use datadog_api_client::datadogV2::model::CIAppTestsGroupBy;
use datadog_api_client::datadogV2::model::CIAppTestsQueryFilter;

#[tokio::main]
async fn main() {
    let body = CIAppTestsAggregateRequest::new()
        .compute(vec![CIAppCompute::new(CIAppAggregationFunction::COUNT)
            .metric("@test.is_flaky".to_string())
            .type_(CIAppComputeType::TOTAL)])
        .filter(
            CIAppTestsQueryFilter::new()
                .from("now-15m".to_string())
                .query("@language:(python OR go)".to_string())
                .to("now".to_string()),
        )
        .group_by(vec![CIAppTestsGroupBy::new("@git.branch".to_string())
            .limit(10)
            .sort(CIAppAggregateSort::new().order(CIAppSortOrder::ASCENDING))
            .total(CIAppGroupByTotal::CIAppGroupByTotalBoolean(false))])
        .options(CIAppQueryOptions::new().timezone("GMT".to_string()));
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityTestsAPI::with_config(configuration);
    let resp = api.aggregate_ci_app_test_events(body).await;
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

#####  Aggregate tests events returns "OK" response
```
/**
 * Aggregate tests events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityTestsApi(configuration);

const params: v2.CIVisibilityTestsApiAggregateCIAppTestEventsRequest = {
  body: {
    compute: [
      {
        aggregation: "count",
        metric: "@test.is_flaky",
        type: "total",
      },
    ],
    filter: {
      from: "now-15m",
      query: "@language:(python OR go)",
      to: "now",
    },
    groupBy: [
      {
        facet: "@git.branch",
        limit: 10,
        sort: {
          order: "asc",
        },
        total: false,
      },
    ],
    options: {
      timezone: "GMT",
    },
  },
};

apiInstance
  .aggregateCIAppTestEvents(params)
  .then((data: v2.CIAppTestsAnalyticsAggregateResponse) => {
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
![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=af92da46-b624-43bb-9173-f0b97f4d4963&bo=1&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=CI%20Visibility%20Tests&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fci-visibility-tests%2F&r=&evt=pageLoad&sv=2&cdb=AQAA&rn=859457)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4de5bb84-382c-457f-a941-8cfe7f54450a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=73770c56-1b51-43ea-8c11-e90fd77bc57b&pt=CI%20Visibility%20Tests&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fci-visibility-tests%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4de5bb84-382c-457f-a941-8cfe7f54450a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=73770c56-1b51-43ea-8c11-e90fd77bc57b&pt=CI%20Visibility%20Tests&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fci-visibility-tests%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
