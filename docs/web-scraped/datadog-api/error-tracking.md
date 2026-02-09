# Source: https://docs.datadoghq.com/api/latest/error-tracking

# Error Tracking
View and manage issues within Error Tracking. See the [Error Tracking page](https://docs.datadoghq.com/error_tracking/) for more information.
## [Search error tracking issues](https://docs.datadoghq.com/api/latest/error-tracking/#search-error-tracking-issues)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/error-tracking/#search-error-tracking-issues-v2)


POST https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/searchhttps://api.ap2.datadoghq.com/api/v2/error-tracking/issues/searchhttps://api.datadoghq.eu/api/v2/error-tracking/issues/searchhttps://api.ddog-gov.com/api/v2/error-tracking/issues/searchhttps://api.datadoghq.com/api/v2/error-tracking/issues/searchhttps://api.us3.datadoghq.com/api/v2/error-tracking/issues/searchhttps://api.us5.datadoghq.com/api/v2/error-tracking/issues/search
### Overview
Search issues endpoint allows you to programmatically search for issues within your organization. This endpoint returns a list of issues that match a given search query, following the event search syntax. The search results are limited to a maximum of 100 issues per request.
OAuth apps require the `error_tracking_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
include
array
Comma-separated list of relationship objects that should be included in the response. Possible values are `issue`, `issue.assignee`, `issue.case`, and `issue.team_owners`.
### Request
#### Body Data (required)
Search issues request payload.
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


Field
Type
Description
data [_required_]
object
Search issues request.
attributes [_required_]
object
Object describing a search issue request.
from [_required_]
int64
Start date (inclusive) of the query in milliseconds since the Unix epoch.
order_by
enum
The attribute to sort the search results by. Allowed enum values: `TOTAL_COUNT,FIRST_SEEN,IMPACTED_SESSIONS,PRIORITY`
persona
enum
Persona for the search. Either track(s) or persona(s) must be specified. Allowed enum values: `ALL,BROWSER,MOBILE,BACKEND`
query [_required_]
string
Search query following the event search syntax.
to [_required_]
int64
End date (exclusive) of the query in milliseconds since the Unix epoch.
track
enum
Track of the events to query. Either track(s) or persona(s) must be specified. Allowed enum values: `trace,logs,rum`
type [_required_]
enum
Type of the object. Allowed enum values: `search_request`
```
{
  "data": {
    "attributes": {
      "query": "service:orders-* AND @language:go",
      "from": 1671612804000,
      "to": 1671620004000,
      "track": "trace"
    },
    "type": "search_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/error-tracking/#SearchIssues-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/error-tracking/#SearchIssues-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/error-tracking/#SearchIssues-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/error-tracking/#SearchIssues-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/error-tracking/#SearchIssues-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


Search issues response payload.
Field
Type
Description
data
[object]
Array of results matching the search query.
attributes [_required_]
object
Object containing the information of a search result.
impacted_sessions
int64
Count of sessions impacted by the issue over the queried time window.
impacted_users
int64
Count of users impacted by the issue over the queried time window.
total_count
int64
Total count of errors that match the issue over the queried time window.
id [_required_]
string
Search result identifier (matches the nested issue's identifier).
relationships
object
Relationships between the search result and other resources.
issue
object
Relationship between the search result and the corresponding issue.
data [_required_]
object
The issue the search result corresponds to.
id [_required_]
string
Issue identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `issue`
type [_required_]
enum
Type of the object. Allowed enum values: `error_tracking_search_result`
included
[ <oneOf>]
Array of resources related to the search results.
Option 1
object
The issue matching the request.
attributes [_required_]
object
Object containing the information of an issue.
error_message
string
Error message associated with the issue.
error_type
string
Type of the error that matches the issue.
file_path
string
Path of the file where the issue occurred.
first_seen
int64
Timestamp of the first seen error in milliseconds since the Unix epoch.
first_seen_version
string
The application version (for example, git commit hash) where the issue was first observed.
function_name
string
Name of the function where the issue occurred.
is_crash
boolean
Error is a crash.
languages
[string]
Array of programming languages associated with the issue.
last_seen
int64
Timestamp of the last seen error in milliseconds since the Unix epoch.
last_seen_version
string
The application version (for example, git commit hash) where the issue was last observed.
platform
enum
Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`
service
string
Service name.
state
enum
State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`
id [_required_]
string
Issue identifier.
relationships
object
Relationship between the issue and an assignee, case and/or teams.
assignee
object
Relationship between the issue and assignee.
data [_required_]
object
The user the issue is assigned to.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
case
object
Relationship between the issue and case.
data [_required_]
object
The case the issue is attached to.
id [_required_]
string
Case identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `case`
team_owners
object
Relationship between the issue and teams.
data [_required_]
[object]
Array of teams that are owners of the issue.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
type [_required_]
enum
Type of the object. Allowed enum values: `issue`
Option 2
object
A case
attributes [_required_]
object
Case resource attributes
archived_at
date-time
Timestamp of when the case was archived
attributes
object
The definition of `CaseObjectAttributes` object.
<any-key>
[string]
closed_at
date-time
Timestamp of when the case was closed
created_at
date-time
Timestamp of when the case was created
custom_attributes
object
Case custom attributes
<any-key>
object
Custom attribute values
is_multi [_required_]
boolean
If true, value must be an array
type [_required_]
enum
Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`
value [_required_]
<oneOf>
Union of supported value for a custom attribute
Option 1
string
Value of TEXT/URL/NUMBER/SELECT custom attribute
Option 2
[string]
Value of multi TEXT/URL/NUMBER/SELECT custom attribute
Option 3
double
Value of NUMBER custom attribute
Option 4
[number]
Values of multi NUMBER custom attribute
description
string
Description
jira_issue
object
Jira issue attached to case
result
object
Jira issue information
issue_id
string
Jira issue ID
issue_key
string
Jira issue key
issue_url
string
Jira issue URL
project_key
string
Jira project key
status
enum
Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`
default: `IN_PROGRESS`
key
string
Key
modified_at
date-time
Timestamp of when the case was last modified
priority
enum
Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`
default: `NOT_DEFINED`
service_now_ticket
object
ServiceNow ticket attached to case
result
object
ServiceNow ticket information
sys_target_link
string
Link to the Incident created on ServiceNow
status
enum
Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`
default: `IN_PROGRESS`
status
enum
Case status Allowed enum values: `OPEN,IN_PROGRESS,CLOSED`
title
string
Title
type
enum
**DEPRECATED** : Case type Allowed enum values: `STANDARD`
type_id
string
Case type UUID
id [_required_]
string
Case's identifier
relationships
object
Resources related to a case
assignee
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
created_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
modified_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
project
object
Relationship to project
data [_required_]
object
Relationship to project object
id [_required_]
string
A unique identifier that represents the project
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
Option 3
object
The user to whom the issue is assigned.
attributes [_required_]
object
Object containing the information of a user.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
Option 4
object
A team that owns an issue.
attributes [_required_]
object
Object containing the information of a team.
handle
string
The team's identifier.
name
string
The name of the team.
summary
string
A brief summary of the team, derived from its description.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
```
{
  "data": [
    {
      "attributes": {
        "impacted_sessions": 12,
        "impacted_users": 4,
        "total_count": 82
      },
      "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
      "relationships": {
        "issue": {
          "data": {
            "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
            "type": "issue"
          }
        }
      },
      "type": "error_tracking_search_result"
    }
  ],
  "included": [
    {
      "attributes": {
        "error_message": "object of type 'NoneType' has no len()",
        "error_type": "builtins.TypeError",
        "file_path": "/django-email/conduit/apps/core/utils.py",
        "first_seen": 1671612804001,
        "first_seen_version": "aaf65cd0",
        "function_name": "filter_forbidden_tags",
        "is_crash": false,
        "languages": [
          "PYTHON",
          "GO"
        ],
        "last_seen": 1671620003100,
        "last_seen_version": "b6199f80",
        "platform": "BACKEND",
        "service": "email-api-py",
        "state": "RESOLVED"
      },
      "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
      "relationships": {
        "assignee": {
          "data": {
            "id": "87cb11a0-278c-440a-99fe-701223c80296",
            "type": "user"
          }
        },
        "case": {
          "data": {
            "id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
            "type": "case"
          }
        },
        "team_owners": {
          "data": [
            {
              "id": "221b0179-6447-4d03-91c3-3ca98bf60e8a",
              "type": "team"
            }
          ]
        }
      },
      "type": "issue"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=typescript)


#####  Search error tracking issues returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "query": "service:orders-* AND @language:go",
      "from": 1671612804000,
      "to": 1671620004000,
      "track": "trace"
    },
    "type": "search_request"
  }
}
EOF  

                        
```

#####  Search error tracking issues returns "OK" response
```
// Search error tracking issues returns "OK" response

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
	body := datadogV2.IssuesSearchRequest{
		Data: datadogV2.IssuesSearchRequestData{
			Attributes: datadogV2.IssuesSearchRequestDataAttributes{
				Query: "service:orders-* AND @language:go",
				From:  1671612804000,
				To:    1671620004000,
				Track: datadogV2.ISSUESSEARCHREQUESTDATAATTRIBUTESTRACK_TRACE.Ptr(),
			},
			Type: datadogV2.ISSUESSEARCHREQUESTDATATYPE_SEARCH_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewErrorTrackingApi(apiClient)
	resp, r, err := api.SearchIssues(ctx, body, *datadogV2.NewSearchIssuesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ErrorTrackingApi.SearchIssues`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ErrorTrackingApi.SearchIssues`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Search error tracking issues returns "OK" response
```
// Search error tracking issues returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ErrorTrackingApi;
import com.datadog.api.client.v2.model.IssuesSearchRequest;
import com.datadog.api.client.v2.model.IssuesSearchRequestData;
import com.datadog.api.client.v2.model.IssuesSearchRequestDataAttributes;
import com.datadog.api.client.v2.model.IssuesSearchRequestDataAttributesTrack;
import com.datadog.api.client.v2.model.IssuesSearchRequestDataType;
import com.datadog.api.client.v2.model.IssuesSearchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ErrorTrackingApi apiInstance = new ErrorTrackingApi(defaultClient);

    IssuesSearchRequest body =
        new IssuesSearchRequest()
            .data(
                new IssuesSearchRequestData()
                    .attributes(
                        new IssuesSearchRequestDataAttributes()
                            .query("service:orders-* AND @language:go")
                            .from(1671612804000L)
                            .to(1671620004000L)
                            .track(IssuesSearchRequestDataAttributesTrack.TRACE))
                    .type(IssuesSearchRequestDataType.SEARCH_REQUEST));

    try {
      IssuesSearchResponse result = apiInstance.searchIssues(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorTrackingApi#searchIssues");
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

#####  Search error tracking issues returns "OK" response
```
"""
Search error tracking issues returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.issues_search_request import IssuesSearchRequest
from datadog_api_client.v2.model.issues_search_request_data import IssuesSearchRequestData
from datadog_api_client.v2.model.issues_search_request_data_attributes import IssuesSearchRequestDataAttributes
from datadog_api_client.v2.model.issues_search_request_data_attributes_track import (
    IssuesSearchRequestDataAttributesTrack,
)
from datadog_api_client.v2.model.issues_search_request_data_type import IssuesSearchRequestDataType

body = IssuesSearchRequest(
    data=IssuesSearchRequestData(
        attributes=IssuesSearchRequestDataAttributes(
            query="service:orders-* AND @language:go",
            _from=1671612804000,
            to=1671620004000,
            track=IssuesSearchRequestDataAttributesTrack.TRACE,
        ),
        type=IssuesSearchRequestDataType.SEARCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.search_issues(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search error tracking issues returns "OK" response
```
# Search error tracking issues returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ErrorTrackingAPI.new

body = DatadogAPIClient::V2::IssuesSearchRequest.new({
  data: DatadogAPIClient::V2::IssuesSearchRequestData.new({
    attributes: DatadogAPIClient::V2::IssuesSearchRequestDataAttributes.new({
      query: "service:orders-* AND @language:go",
      from: 1671612804000,
      to: 1671620004000,
      track: DatadogAPIClient::V2::IssuesSearchRequestDataAttributesTrack::TRACE,
    }),
    type: DatadogAPIClient::V2::IssuesSearchRequestDataType::SEARCH_REQUEST,
  }),
})
p api_instance.search_issues(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search error tracking issues returns "OK" response
```
// Search error tracking issues returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_error_tracking::ErrorTrackingAPI;
use datadog_api_client::datadogV2::api_error_tracking::SearchIssuesOptionalParams;
use datadog_api_client::datadogV2::model::IssuesSearchRequest;
use datadog_api_client::datadogV2::model::IssuesSearchRequestData;
use datadog_api_client::datadogV2::model::IssuesSearchRequestDataAttributes;
use datadog_api_client::datadogV2::model::IssuesSearchRequestDataAttributesTrack;
use datadog_api_client::datadogV2::model::IssuesSearchRequestDataType;

#[tokio::main]
async fn main() {
    let body = IssuesSearchRequest::new(IssuesSearchRequestData::new(
        IssuesSearchRequestDataAttributes::new(
            1671612804000,
            "service:orders-* AND @language:go".to_string(),
            1671620004000,
        )
        .track(IssuesSearchRequestDataAttributesTrack::TRACE),
        IssuesSearchRequestDataType::SEARCH_REQUEST,
    ));
    let configuration = datadog::Configuration::new();
    let api = ErrorTrackingAPI::with_config(configuration);
    let resp = api
        .search_issues(body, SearchIssuesOptionalParams::default())
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

#####  Search error tracking issues returns "OK" response
```
/**
 * Search error tracking issues returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ErrorTrackingApi(configuration);

const params: v2.ErrorTrackingApiSearchIssuesRequest = {
  body: {
    data: {
      attributes: {
        query: "service:orders-* AND @language:go",
        from: 1671612804000,
        to: 1671620004000,
        track: "trace",
      },
      type: "search_request",
    },
  },
};

apiInstance
  .searchIssues(params)
  .then((data: v2.IssuesSearchResponse) => {
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
## [Get the details of an error tracking issue](https://docs.datadoghq.com/api/latest/error-tracking/#get-the-details-of-an-error-tracking-issue)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/error-tracking/#get-the-details-of-an-error-tracking-issue-v2)


GET https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id}https://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id}https://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}https://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}https://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}https://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id}https://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id}
### Overview
Retrieve the full details for a specific error tracking issue, including attributes and relationships.
OAuth apps require the `error_tracking_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
issue_id [_required_]
string
The identifier of the issue.
#### Query Strings
Name
Type
Description
include
array
Comma-separated list of relationship objects that should be included in the response. Possible values are `assignee`, `case`, and `team_owners`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/error-tracking/#GetIssue-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/error-tracking/#GetIssue-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/error-tracking/#GetIssue-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/error-tracking/#GetIssue-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/error-tracking/#GetIssue-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/error-tracking/#GetIssue-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


Response containing error tracking issue data.
Field
Type
Description
data
object
The issue matching the request.
attributes [_required_]
object
Object containing the information of an issue.
error_message
string
Error message associated with the issue.
error_type
string
Type of the error that matches the issue.
file_path
string
Path of the file where the issue occurred.
first_seen
int64
Timestamp of the first seen error in milliseconds since the Unix epoch.
first_seen_version
string
The application version (for example, git commit hash) where the issue was first observed.
function_name
string
Name of the function where the issue occurred.
is_crash
boolean
Error is a crash.
languages
[string]
Array of programming languages associated with the issue.
last_seen
int64
Timestamp of the last seen error in milliseconds since the Unix epoch.
last_seen_version
string
The application version (for example, git commit hash) where the issue was last observed.
platform
enum
Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`
service
string
Service name.
state
enum
State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`
id [_required_]
string
Issue identifier.
relationships
object
Relationship between the issue and an assignee, case and/or teams.
assignee
object
Relationship between the issue and assignee.
data [_required_]
object
The user the issue is assigned to.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
case
object
Relationship between the issue and case.
data [_required_]
object
The case the issue is attached to.
id [_required_]
string
Case identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `case`
team_owners
object
Relationship between the issue and teams.
data [_required_]
[object]
Array of teams that are owners of the issue.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
type [_required_]
enum
Type of the object. Allowed enum values: `issue`
included
[ <oneOf>]
Array of resources related to the issue.
Option 1
object
The case attached to the issue.
attributes [_required_]
object
Object containing the information of a case.
archived_at
date-time
Timestamp of when the case was archived.
closed_at
date-time
Timestamp of when the case was closed.
created_at
date-time
Timestamp of when the case was created.
creation_source
string
Source of the case creation.
description
string
Description of the case.
due_date
string
Due date of the case.
insights
[object]
Insights of the case.
ref
string
Reference of the insight.
resource_id
string
Insight identifier.
type
string
Type of the insight.
jira_issue
object
Jira issue of the case.
result
object
Contains the identifiers and URL for a successfully created Jira issue.
issue_id
string
Jira issue identifier.
issue_key
string
Jira issue key.
issue_url
string
Jira issue URL.
project_key
string
Jira project key.
status
string
Creation status of the Jira issue.
key
string
Key of the case.
modified_at
date-time
Timestamp of when the case was last modified.
priority
enum
Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`
default: `NOT_DEFINED`
status
enum
Case status Allowed enum values: `OPEN,IN_PROGRESS,CLOSED`
title
string
Title of the case.
type
string
Type of the case.
id [_required_]
string
Case identifier.
relationships
object
Resources related to a case.
assignee
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
created_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
modified_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
project
object
Relationship to project
data [_required_]
object
Relationship to project object
id [_required_]
string
A unique identifier that represents the project
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
type [_required_]
enum
Type of the object. Allowed enum values: `case`
Option 2
object
The user to whom the issue is assigned.
attributes [_required_]
object
Object containing the information of a user.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
Option 3
object
A team that owns an issue.
attributes [_required_]
object
Object containing the information of a team.
handle
string
The team's identifier.
name
string
The name of the team.
summary
string
A brief summary of the team, derived from its description.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
```
{
  "data": {
    "attributes": {
      "error_message": "object of type 'NoneType' has no len()",
      "error_type": "builtins.TypeError",
      "file_path": "/django-email/conduit/apps/core/utils.py",
      "first_seen": 1671612804001,
      "first_seen_version": "aaf65cd0",
      "function_name": "filter_forbidden_tags",
      "is_crash": false,
      "languages": [
        "PYTHON",
        "GO"
      ],
      "last_seen": 1671620003100,
      "last_seen_version": "b6199f80",
      "platform": "BACKEND",
      "service": "email-api-py",
      "state": "RESOLVED"
    },
    "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
    "relationships": {
      "assignee": {
        "data": {
          "id": "87cb11a0-278c-440a-99fe-701223c80296",
          "type": "user"
        }
      },
      "case": {
        "data": {
          "id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
          "type": "case"
        }
      },
      "team_owners": {
        "data": [
          {
            "id": "221b0179-6447-4d03-91c3-3ca98bf60e8a",
            "type": "team"
          }
        ]
      }
    },
    "type": "issue"
  },
  "included": [
    {
      "attributes": {
        "archived_at": "2025-01-01T00:00:00Z",
        "closed_at": "2025-01-01T00:00:00Z",
        "created_at": "2025-01-01T00:00:00Z",
        "creation_source": "ERROR_TRACKING",
        "description": "string",
        "due_date": "2025-01-01",
        "insights": [
          {
            "ref": "/error-tracking?issueId=2841440d-e780-4fe2-96cd-6a8c1d194da5",
            "resource_id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
            "type": "ERROR_TRACKING"
          }
        ],
        "jira_issue": {
          "result": {
            "issue_id": "1904866",
            "issue_key": "ET-123",
            "issue_url": "https://your-jira-instance.atlassian.net/browse/ET-123",
            "project_key": "ET"
          },
          "status": "COMPLETED"
        },
        "key": "ET-123",
        "modified_at": "2025-01-01T00:00:00Z",
        "priority": "NOT_DEFINED",
        "status": "OPEN",
        "title": "Error: HTTP error",
        "type": "ERROR_TRACKING_ISSUE"
      },
      "id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
      "relationships": {
        "assignee": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "created_by": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "modified_by": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "project": {
          "data": {
            "id": "e555e290-ed65-49bd-ae18-8acbfcf18db7",
            "type": "project"
          }
        }
      },
      "type": "case"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=typescript)


#####  Get the details of an error tracking issue
Copy
```
                  # Path parameters  
export issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the details of an error tracking issue
```
"""
Get the details of an error tracking issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.get_issue(
        issue_id=ISSUE_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get the details of an error tracking issue
```
# Get the details of an error tracking issue returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ErrorTrackingAPI.new

# there is a valid "issue" in the system
ISSUE_ID = ENV["ISSUE_ID"]
p api_instance.get_issue(ISSUE_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get the details of an error tracking issue
```
// Get the details of an error tracking issue returns "OK" response

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
	// there is a valid "issue" in the system
	IssueID := os.Getenv("ISSUE_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewErrorTrackingApi(apiClient)
	resp, r, err := api.GetIssue(ctx, IssueID, *datadogV2.NewGetIssueOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ErrorTrackingApi.GetIssue`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ErrorTrackingApi.GetIssue`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get the details of an error tracking issue
```
// Get the details of an error tracking issue returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ErrorTrackingApi;
import com.datadog.api.client.v2.model.IssueResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ErrorTrackingApi apiInstance = new ErrorTrackingApi(defaultClient);

    // there is a valid "issue" in the system
    String ISSUE_ID = System.getenv("ISSUE_ID");

    try {
      IssueResponse result = apiInstance.getIssue(ISSUE_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorTrackingApi#getIssue");
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

#####  Get the details of an error tracking issue
```
// Get the details of an error tracking issue returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_error_tracking::ErrorTrackingAPI;
use datadog_api_client::datadogV2::api_error_tracking::GetIssueOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "issue" in the system
    let issue_id = std::env::var("ISSUE_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ErrorTrackingAPI::with_config(configuration);
    let resp = api
        .get_issue(issue_id.clone(), GetIssueOptionalParams::default())
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

#####  Get the details of an error tracking issue
```
/**
 * Get the details of an error tracking issue returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ErrorTrackingApi(configuration);

// there is a valid "issue" in the system
const ISSUE_ID = process.env.ISSUE_ID as string;

const params: v2.ErrorTrackingApiGetIssueRequest = {
  issueId: ISSUE_ID,
};

apiInstance
  .getIssue(params)
  .then((data: v2.IssueResponse) => {
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
## [Update the state of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-state-of-an-issue)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-state-of-an-issue-v2)


PUT https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/statehttps://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/statehttps://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}/statehttps://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}/statehttps://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/statehttps://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/statehttps://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/state
### Overview
Update the state of an issue by `issue_id`. Use this endpoint to move an issue between states such as `OPEN`, `RESOLVED`, or `IGNORED`.
OAuth apps require the `error_tracking_read, error_tracking_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
issue_id [_required_]
string
The identifier of the issue.
### Request
#### Body Data (required)
Update issue state request payload.
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


Field
Type
Description
data [_required_]
object
Update issue state request.
attributes [_required_]
object
Object describing an issue state update request.
state [_required_]
enum
State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`
id [_required_]
string
Issue identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `error_tracking_issue`
```
{
  "data": {
    "attributes": {
      "state": "RESOLVED"
    },
    "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
    "type": "error_tracking_issue"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueState-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueState-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueState-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueState-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueState-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueState-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


Response containing error tracking issue data.
Field
Type
Description
data
object
The issue matching the request.
attributes [_required_]
object
Object containing the information of an issue.
error_message
string
Error message associated with the issue.
error_type
string
Type of the error that matches the issue.
file_path
string
Path of the file where the issue occurred.
first_seen
int64
Timestamp of the first seen error in milliseconds since the Unix epoch.
first_seen_version
string
The application version (for example, git commit hash) where the issue was first observed.
function_name
string
Name of the function where the issue occurred.
is_crash
boolean
Error is a crash.
languages
[string]
Array of programming languages associated with the issue.
last_seen
int64
Timestamp of the last seen error in milliseconds since the Unix epoch.
last_seen_version
string
The application version (for example, git commit hash) where the issue was last observed.
platform
enum
Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`
service
string
Service name.
state
enum
State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`
id [_required_]
string
Issue identifier.
relationships
object
Relationship between the issue and an assignee, case and/or teams.
assignee
object
Relationship between the issue and assignee.
data [_required_]
object
The user the issue is assigned to.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
case
object
Relationship between the issue and case.
data [_required_]
object
The case the issue is attached to.
id [_required_]
string
Case identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `case`
team_owners
object
Relationship between the issue and teams.
data [_required_]
[object]
Array of teams that are owners of the issue.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
type [_required_]
enum
Type of the object. Allowed enum values: `issue`
included
[ <oneOf>]
Array of resources related to the issue.
Option 1
object
The case attached to the issue.
attributes [_required_]
object
Object containing the information of a case.
archived_at
date-time
Timestamp of when the case was archived.
closed_at
date-time
Timestamp of when the case was closed.
created_at
date-time
Timestamp of when the case was created.
creation_source
string
Source of the case creation.
description
string
Description of the case.
due_date
string
Due date of the case.
insights
[object]
Insights of the case.
ref
string
Reference of the insight.
resource_id
string
Insight identifier.
type
string
Type of the insight.
jira_issue
object
Jira issue of the case.
result
object
Contains the identifiers and URL for a successfully created Jira issue.
issue_id
string
Jira issue identifier.
issue_key
string
Jira issue key.
issue_url
string
Jira issue URL.
project_key
string
Jira project key.
status
string
Creation status of the Jira issue.
key
string
Key of the case.
modified_at
date-time
Timestamp of when the case was last modified.
priority
enum
Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`
default: `NOT_DEFINED`
status
enum
Case status Allowed enum values: `OPEN,IN_PROGRESS,CLOSED`
title
string
Title of the case.
type
string
Type of the case.
id [_required_]
string
Case identifier.
relationships
object
Resources related to a case.
assignee
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
created_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
modified_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
project
object
Relationship to project
data [_required_]
object
Relationship to project object
id [_required_]
string
A unique identifier that represents the project
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
type [_required_]
enum
Type of the object. Allowed enum values: `case`
Option 2
object
The user to whom the issue is assigned.
attributes [_required_]
object
Object containing the information of a user.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
Option 3
object
A team that owns an issue.
attributes [_required_]
object
Object containing the information of a team.
handle
string
The team's identifier.
name
string
The name of the team.
summary
string
A brief summary of the team, derived from its description.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
```
{
  "data": {
    "attributes": {
      "error_message": "object of type 'NoneType' has no len()",
      "error_type": "builtins.TypeError",
      "file_path": "/django-email/conduit/apps/core/utils.py",
      "first_seen": 1671612804001,
      "first_seen_version": "aaf65cd0",
      "function_name": "filter_forbidden_tags",
      "is_crash": false,
      "languages": [
        "PYTHON",
        "GO"
      ],
      "last_seen": 1671620003100,
      "last_seen_version": "b6199f80",
      "platform": "BACKEND",
      "service": "email-api-py",
      "state": "RESOLVED"
    },
    "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
    "relationships": {
      "assignee": {
        "data": {
          "id": "87cb11a0-278c-440a-99fe-701223c80296",
          "type": "user"
        }
      },
      "case": {
        "data": {
          "id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
          "type": "case"
        }
      },
      "team_owners": {
        "data": [
          {
            "id": "221b0179-6447-4d03-91c3-3ca98bf60e8a",
            "type": "team"
          }
        ]
      }
    },
    "type": "issue"
  },
  "included": [
    {
      "attributes": {
        "archived_at": "2025-01-01T00:00:00Z",
        "closed_at": "2025-01-01T00:00:00Z",
        "created_at": "2025-01-01T00:00:00Z",
        "creation_source": "ERROR_TRACKING",
        "description": "string",
        "due_date": "2025-01-01",
        "insights": [
          {
            "ref": "/error-tracking?issueId=2841440d-e780-4fe2-96cd-6a8c1d194da5",
            "resource_id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
            "type": "ERROR_TRACKING"
          }
        ],
        "jira_issue": {
          "result": {
            "issue_id": "1904866",
            "issue_key": "ET-123",
            "issue_url": "https://your-jira-instance.atlassian.net/browse/ET-123",
            "project_key": "ET"
          },
          "status": "COMPLETED"
        },
        "key": "ET-123",
        "modified_at": "2025-01-01T00:00:00Z",
        "priority": "NOT_DEFINED",
        "status": "OPEN",
        "title": "Error: HTTP error",
        "type": "ERROR_TRACKING_ISSUE"
      },
      "id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
      "relationships": {
        "assignee": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "created_by": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "modified_by": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "project": {
          "data": {
            "id": "e555e290-ed65-49bd-ae18-8acbfcf18db7",
            "type": "project"
          }
        }
      },
      "type": "case"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=typescript)


#####  Update the state of an issue returns "OK" response
Copy
```
                          # Path parameters  
export issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}/state" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "state": "RESOLVED"
    },
    "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
    "type": "error_tracking_issue"
  }
}
EOF  

                        
```

#####  Update the state of an issue returns "OK" response
```
// Update the state of an issue returns "OK" response

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
	// there is a valid "issue" in the system
	IssueID := os.Getenv("ISSUE_ID")

	body := datadogV2.IssueUpdateStateRequest{
		Data: datadogV2.IssueUpdateStateRequestData{
			Attributes: datadogV2.IssueUpdateStateRequestDataAttributes{
				State: datadogV2.ISSUESTATE_RESOLVED,
			},
			Id:   IssueID,
			Type: datadogV2.ISSUEUPDATESTATEREQUESTDATATYPE_ERROR_TRACKING_ISSUE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewErrorTrackingApi(apiClient)
	resp, r, err := api.UpdateIssueState(ctx, IssueID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ErrorTrackingApi.UpdateIssueState`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ErrorTrackingApi.UpdateIssueState`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update the state of an issue returns "OK" response
```
// Update the state of an issue returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ErrorTrackingApi;
import com.datadog.api.client.v2.model.IssueResponse;
import com.datadog.api.client.v2.model.IssueState;
import com.datadog.api.client.v2.model.IssueUpdateStateRequest;
import com.datadog.api.client.v2.model.IssueUpdateStateRequestData;
import com.datadog.api.client.v2.model.IssueUpdateStateRequestDataAttributes;
import com.datadog.api.client.v2.model.IssueUpdateStateRequestDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ErrorTrackingApi apiInstance = new ErrorTrackingApi(defaultClient);

    // there is a valid "issue" in the system
    String ISSUE_ID = System.getenv("ISSUE_ID");

    IssueUpdateStateRequest body =
        new IssueUpdateStateRequest()
            .data(
                new IssueUpdateStateRequestData()
                    .attributes(
                        new IssueUpdateStateRequestDataAttributes().state(IssueState.RESOLVED))
                    .id(ISSUE_ID)
                    .type(IssueUpdateStateRequestDataType.ERROR_TRACKING_ISSUE));

    try {
      IssueResponse result = apiInstance.updateIssueState(ISSUE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorTrackingApi#updateIssueState");
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

#####  Update the state of an issue returns "OK" response
```
"""
Update the state of an issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.issue_state import IssueState
from datadog_api_client.v2.model.issue_update_state_request import IssueUpdateStateRequest
from datadog_api_client.v2.model.issue_update_state_request_data import IssueUpdateStateRequestData
from datadog_api_client.v2.model.issue_update_state_request_data_attributes import IssueUpdateStateRequestDataAttributes
from datadog_api_client.v2.model.issue_update_state_request_data_type import IssueUpdateStateRequestDataType

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

body = IssueUpdateStateRequest(
    data=IssueUpdateStateRequestData(
        attributes=IssueUpdateStateRequestDataAttributes(
            state=IssueState.RESOLVED,
        ),
        id=ISSUE_ID,
        type=IssueUpdateStateRequestDataType.ERROR_TRACKING_ISSUE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.update_issue_state(issue_id=ISSUE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update the state of an issue returns "OK" response
```
# Update the state of an issue returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ErrorTrackingAPI.new

# there is a valid "issue" in the system
ISSUE_ID = ENV["ISSUE_ID"]

body = DatadogAPIClient::V2::IssueUpdateStateRequest.new({
  data: DatadogAPIClient::V2::IssueUpdateStateRequestData.new({
    attributes: DatadogAPIClient::V2::IssueUpdateStateRequestDataAttributes.new({
      state: DatadogAPIClient::V2::IssueState::RESOLVED,
    }),
    id: ISSUE_ID,
    type: DatadogAPIClient::V2::IssueUpdateStateRequestDataType::ERROR_TRACKING_ISSUE,
  }),
})
p api_instance.update_issue_state(ISSUE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update the state of an issue returns "OK" response
```
// Update the state of an issue returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_error_tracking::ErrorTrackingAPI;
use datadog_api_client::datadogV2::model::IssueState;
use datadog_api_client::datadogV2::model::IssueUpdateStateRequest;
use datadog_api_client::datadogV2::model::IssueUpdateStateRequestData;
use datadog_api_client::datadogV2::model::IssueUpdateStateRequestDataAttributes;
use datadog_api_client::datadogV2::model::IssueUpdateStateRequestDataType;

#[tokio::main]
async fn main() {
    // there is a valid "issue" in the system
    let issue_id = std::env::var("ISSUE_ID").unwrap();
    let body = IssueUpdateStateRequest::new(IssueUpdateStateRequestData::new(
        IssueUpdateStateRequestDataAttributes::new(IssueState::RESOLVED),
        issue_id.clone(),
        IssueUpdateStateRequestDataType::ERROR_TRACKING_ISSUE,
    ));
    let configuration = datadog::Configuration::new();
    let api = ErrorTrackingAPI::with_config(configuration);
    let resp = api.update_issue_state(issue_id.clone(), body).await;
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

#####  Update the state of an issue returns "OK" response
```
/**
 * Update the state of an issue returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ErrorTrackingApi(configuration);

// there is a valid "issue" in the system
const ISSUE_ID = process.env.ISSUE_ID as string;

const params: v2.ErrorTrackingApiUpdateIssueStateRequest = {
  body: {
    data: {
      attributes: {
        state: "RESOLVED",
      },
      id: ISSUE_ID,
      type: "error_tracking_issue",
    },
  },
  issueId: ISSUE_ID,
};

apiInstance
  .updateIssueState(params)
  .then((data: v2.IssueResponse) => {
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
## [Update the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-assignee-of-an-issue)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-assignee-of-an-issue-v2)


PUT https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee
### Overview
Update the assignee of an issue by `issue_id`.
OAuth apps require the `error_tracking_read, error_tracking_write, cases_read, cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
issue_id [_required_]
string
The identifier of the issue.
### Request
#### Body Data (required)
Update issue assignee request payload.
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


Field
Type
Description
data [_required_]
object
Update issue assignee request.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `assignee`
```
{
  "data": {
    "id": "87cb11a0-278c-440a-99fe-701223c80296",
    "type": "assignee"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueAssignee-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueAssignee-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueAssignee-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueAssignee-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueAssignee-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/error-tracking/#UpdateIssueAssignee-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


Response containing error tracking issue data.
Field
Type
Description
data
object
The issue matching the request.
attributes [_required_]
object
Object containing the information of an issue.
error_message
string
Error message associated with the issue.
error_type
string
Type of the error that matches the issue.
file_path
string
Path of the file where the issue occurred.
first_seen
int64
Timestamp of the first seen error in milliseconds since the Unix epoch.
first_seen_version
string
The application version (for example, git commit hash) where the issue was first observed.
function_name
string
Name of the function where the issue occurred.
is_crash
boolean
Error is a crash.
languages
[string]
Array of programming languages associated with the issue.
last_seen
int64
Timestamp of the last seen error in milliseconds since the Unix epoch.
last_seen_version
string
The application version (for example, git commit hash) where the issue was last observed.
platform
enum
Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`
service
string
Service name.
state
enum
State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`
id [_required_]
string
Issue identifier.
relationships
object
Relationship between the issue and an assignee, case and/or teams.
assignee
object
Relationship between the issue and assignee.
data [_required_]
object
The user the issue is assigned to.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
case
object
Relationship between the issue and case.
data [_required_]
object
The case the issue is attached to.
id [_required_]
string
Case identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `case`
team_owners
object
Relationship between the issue and teams.
data [_required_]
[object]
Array of teams that are owners of the issue.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
type [_required_]
enum
Type of the object. Allowed enum values: `issue`
included
[ <oneOf>]
Array of resources related to the issue.
Option 1
object
The case attached to the issue.
attributes [_required_]
object
Object containing the information of a case.
archived_at
date-time
Timestamp of when the case was archived.
closed_at
date-time
Timestamp of when the case was closed.
created_at
date-time
Timestamp of when the case was created.
creation_source
string
Source of the case creation.
description
string
Description of the case.
due_date
string
Due date of the case.
insights
[object]
Insights of the case.
ref
string
Reference of the insight.
resource_id
string
Insight identifier.
type
string
Type of the insight.
jira_issue
object
Jira issue of the case.
result
object
Contains the identifiers and URL for a successfully created Jira issue.
issue_id
string
Jira issue identifier.
issue_key
string
Jira issue key.
issue_url
string
Jira issue URL.
project_key
string
Jira project key.
status
string
Creation status of the Jira issue.
key
string
Key of the case.
modified_at
date-time
Timestamp of when the case was last modified.
priority
enum
Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`
default: `NOT_DEFINED`
status
enum
Case status Allowed enum values: `OPEN,IN_PROGRESS,CLOSED`
title
string
Title of the case.
type
string
Type of the case.
id [_required_]
string
Case identifier.
relationships
object
Resources related to a case.
assignee
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
created_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
modified_by
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
project
object
Relationship to project
data [_required_]
object
Relationship to project object
id [_required_]
string
A unique identifier that represents the project
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
type [_required_]
enum
Type of the object. Allowed enum values: `case`
Option 2
object
The user to whom the issue is assigned.
attributes [_required_]
object
Object containing the information of a user.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
id [_required_]
string
User identifier.
type [_required_]
enum
Type of the object Allowed enum values: `user`
Option 3
object
A team that owns an issue.
attributes [_required_]
object
Object containing the information of a team.
handle
string
The team's identifier.
name
string
The name of the team.
summary
string
A brief summary of the team, derived from its description.
id [_required_]
string
Team identifier.
type [_required_]
enum
Type of the object. Allowed enum values: `team`
```
{
  "data": {
    "attributes": {
      "error_message": "object of type 'NoneType' has no len()",
      "error_type": "builtins.TypeError",
      "file_path": "/django-email/conduit/apps/core/utils.py",
      "first_seen": 1671612804001,
      "first_seen_version": "aaf65cd0",
      "function_name": "filter_forbidden_tags",
      "is_crash": false,
      "languages": [
        "PYTHON",
        "GO"
      ],
      "last_seen": 1671620003100,
      "last_seen_version": "b6199f80",
      "platform": "BACKEND",
      "service": "email-api-py",
      "state": "RESOLVED"
    },
    "id": "c1726a66-1f64-11ee-b338-da7ad0900002",
    "relationships": {
      "assignee": {
        "data": {
          "id": "87cb11a0-278c-440a-99fe-701223c80296",
          "type": "user"
        }
      },
      "case": {
        "data": {
          "id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
          "type": "case"
        }
      },
      "team_owners": {
        "data": [
          {
            "id": "221b0179-6447-4d03-91c3-3ca98bf60e8a",
            "type": "team"
          }
        ]
      }
    },
    "type": "issue"
  },
  "included": [
    {
      "attributes": {
        "archived_at": "2025-01-01T00:00:00Z",
        "closed_at": "2025-01-01T00:00:00Z",
        "created_at": "2025-01-01T00:00:00Z",
        "creation_source": "ERROR_TRACKING",
        "description": "string",
        "due_date": "2025-01-01",
        "insights": [
          {
            "ref": "/error-tracking?issueId=2841440d-e780-4fe2-96cd-6a8c1d194da5",
            "resource_id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
            "type": "ERROR_TRACKING"
          }
        ],
        "jira_issue": {
          "result": {
            "issue_id": "1904866",
            "issue_key": "ET-123",
            "issue_url": "https://your-jira-instance.atlassian.net/browse/ET-123",
            "project_key": "ET"
          },
          "status": "COMPLETED"
        },
        "key": "ET-123",
        "modified_at": "2025-01-01T00:00:00Z",
        "priority": "NOT_DEFINED",
        "status": "OPEN",
        "title": "Error: HTTP error",
        "type": "ERROR_TRACKING_ISSUE"
      },
      "id": "2841440d-e780-4fe2-96cd-6a8c1d194da5",
      "relationships": {
        "assignee": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "created_by": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "modified_by": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        },
        "project": {
          "data": {
            "id": "e555e290-ed65-49bd-ae18-8acbfcf18db7",
            "type": "project"
          }
        }
      },
      "type": "case"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=typescript)


#####  Update the assignee of an issue returns "OK" response
Copy
```
                          # Path parameters  
export issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}/assignee" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "87cb11a0-278c-440a-99fe-701223c80296",
    "type": "assignee"
  }
}
EOF  

                        
```

#####  Update the assignee of an issue returns "OK" response
```
// Update the assignee of an issue returns "OK" response

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
	// there is a valid "issue" in the system
	IssueID := os.Getenv("ISSUE_ID")

	body := datadogV2.IssueUpdateAssigneeRequest{
		Data: datadogV2.IssueUpdateAssigneeRequestData{
			Id:   "87cb11a0-278c-440a-99fe-701223c80296",
			Type: datadogV2.ISSUEUPDATEASSIGNEEREQUESTDATATYPE_ASSIGNEE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewErrorTrackingApi(apiClient)
	resp, r, err := api.UpdateIssueAssignee(ctx, IssueID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ErrorTrackingApi.UpdateIssueAssignee`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ErrorTrackingApi.UpdateIssueAssignee`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update the assignee of an issue returns "OK" response
```
// Update the assignee of an issue returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ErrorTrackingApi;
import com.datadog.api.client.v2.model.IssueResponse;
import com.datadog.api.client.v2.model.IssueUpdateAssigneeRequest;
import com.datadog.api.client.v2.model.IssueUpdateAssigneeRequestData;
import com.datadog.api.client.v2.model.IssueUpdateAssigneeRequestDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ErrorTrackingApi apiInstance = new ErrorTrackingApi(defaultClient);

    // there is a valid "issue" in the system
    String ISSUE_ID = System.getenv("ISSUE_ID");

    IssueUpdateAssigneeRequest body =
        new IssueUpdateAssigneeRequest()
            .data(
                new IssueUpdateAssigneeRequestData()
                    .id("87cb11a0-278c-440a-99fe-701223c80296")
                    .type(IssueUpdateAssigneeRequestDataType.ASSIGNEE));

    try {
      IssueResponse result = apiInstance.updateIssueAssignee(ISSUE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorTrackingApi#updateIssueAssignee");
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

#####  Update the assignee of an issue returns "OK" response
```
"""
Update the assignee of an issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.issue_update_assignee_request import IssueUpdateAssigneeRequest
from datadog_api_client.v2.model.issue_update_assignee_request_data import IssueUpdateAssigneeRequestData
from datadog_api_client.v2.model.issue_update_assignee_request_data_type import IssueUpdateAssigneeRequestDataType

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

body = IssueUpdateAssigneeRequest(
    data=IssueUpdateAssigneeRequestData(
        id="87cb11a0-278c-440a-99fe-701223c80296",
        type=IssueUpdateAssigneeRequestDataType.ASSIGNEE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.update_issue_assignee(issue_id=ISSUE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update the assignee of an issue returns "OK" response
```
# Update the assignee of an issue returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ErrorTrackingAPI.new

# there is a valid "issue" in the system
ISSUE_ID = ENV["ISSUE_ID"]

body = DatadogAPIClient::V2::IssueUpdateAssigneeRequest.new({
  data: DatadogAPIClient::V2::IssueUpdateAssigneeRequestData.new({
    id: "87cb11a0-278c-440a-99fe-701223c80296",
    type: DatadogAPIClient::V2::IssueUpdateAssigneeRequestDataType::ASSIGNEE,
  }),
})
p api_instance.update_issue_assignee(ISSUE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update the assignee of an issue returns "OK" response
```
// Update the assignee of an issue returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_error_tracking::ErrorTrackingAPI;
use datadog_api_client::datadogV2::model::IssueUpdateAssigneeRequest;
use datadog_api_client::datadogV2::model::IssueUpdateAssigneeRequestData;
use datadog_api_client::datadogV2::model::IssueUpdateAssigneeRequestDataType;

#[tokio::main]
async fn main() {
    // there is a valid "issue" in the system
    let issue_id = std::env::var("ISSUE_ID").unwrap();
    let body = IssueUpdateAssigneeRequest::new(IssueUpdateAssigneeRequestData::new(
        "87cb11a0-278c-440a-99fe-701223c80296".to_string(),
        IssueUpdateAssigneeRequestDataType::ASSIGNEE,
    ));
    let configuration = datadog::Configuration::new();
    let api = ErrorTrackingAPI::with_config(configuration);
    let resp = api.update_issue_assignee(issue_id.clone(), body).await;
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

#####  Update the assignee of an issue returns "OK" response
```
/**
 * Update the assignee of an issue returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ErrorTrackingApi(configuration);

// there is a valid "issue" in the system
const ISSUE_ID = process.env.ISSUE_ID as string;

const params: v2.ErrorTrackingApiUpdateIssueAssigneeRequest = {
  body: {
    data: {
      id: "87cb11a0-278c-440a-99fe-701223c80296",
      type: "assignee",
    },
  },
  issueId: ISSUE_ID,
};

apiInstance
  .updateIssueAssignee(params)
  .then((data: v2.IssueResponse) => {
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
## [Remove the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#remove-the-assignee-of-an-issue)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/error-tracking/#remove-the-assignee-of-an-issue-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assigneehttps://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee
### Overview
Remove the assignee of an issue by `issue_id`.
OAuth apps require the `error_tracking_read, error_tracking_write, cases_read, cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
issue_id [_required_]
string
The identifier of the issue.
### Response
  * [204](https://docs.datadoghq.com/api/latest/error-tracking/#DeleteIssueAssignee-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/error-tracking/#DeleteIssueAssignee-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/error-tracking/#DeleteIssueAssignee-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/error-tracking/#DeleteIssueAssignee-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/error-tracking/#DeleteIssueAssignee-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/error-tracking/#DeleteIssueAssignee-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Model](https://docs.datadoghq.com/api/latest/error-tracking/)
  * [Example](https://docs.datadoghq.com/api/latest/error-tracking/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/error-tracking/?code-lang=typescript)


#####  Remove the assignee of an issue
Copy
```
                  # Path parameters  
export issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}/assignee" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove the assignee of an issue
```
"""
Remove the assignee of an issue returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    api_instance.delete_issue_assignee(
        issue_id=ISSUE_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove the assignee of an issue
```
# Remove the assignee of an issue returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ErrorTrackingAPI.new

# there is a valid "issue" in the system
ISSUE_ID = ENV["ISSUE_ID"]
api_instance.delete_issue_assignee(ISSUE_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove the assignee of an issue
```
// Remove the assignee of an issue returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "issue" in the system
	IssueID := os.Getenv("ISSUE_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewErrorTrackingApi(apiClient)
	r, err := api.DeleteIssueAssignee(ctx, IssueID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ErrorTrackingApi.DeleteIssueAssignee`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Remove the assignee of an issue
```
// Remove the assignee of an issue returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ErrorTrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ErrorTrackingApi apiInstance = new ErrorTrackingApi(defaultClient);

    // there is a valid "issue" in the system
    String ISSUE_ID = System.getenv("ISSUE_ID");

    try {
      apiInstance.deleteIssueAssignee(ISSUE_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorTrackingApi#deleteIssueAssignee");
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

#####  Remove the assignee of an issue
```
// Remove the assignee of an issue returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_error_tracking::ErrorTrackingAPI;

#[tokio::main]
async fn main() {
    // there is a valid "issue" in the system
    let issue_id = std::env::var("ISSUE_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ErrorTrackingAPI::with_config(configuration);
    let resp = api.delete_issue_assignee(issue_id.clone()).await;
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

#####  Remove the assignee of an issue
```
/**
 * Remove the assignee of an issue returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ErrorTrackingApi(configuration);

// there is a valid "issue" in the system
const ISSUE_ID = process.env.ISSUE_ID as string;

const params: v2.ErrorTrackingApiDeleteIssueAssigneeRequest = {
  issueId: ISSUE_ID,
};

apiInstance
  .deleteIssueAssignee(params)
  .then((data: any) => {
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
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=24191c32-4081-4083-b64d-8d878ee8887d&bo=1&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Error%20Tracking&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ferror-tracking%2F&r=&evt=pageLoad&sv=2&cdb=AQAQ&rn=737228)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4679a05f-48fa-4138-9d01-2260df6a9e44&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=41574f96-6ed5-4cab-add6-f21ffd605ba8&pt=Error%20Tracking&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ferror-tracking%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4679a05f-48fa-4138-9d01-2260df6a9e44&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=41574f96-6ed5-4cab-add6-f21ffd605ba8&pt=Error%20Tracking&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ferror-tracking%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
