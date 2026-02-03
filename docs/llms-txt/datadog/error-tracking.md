# Source: https://docs.datadoghq.com/api/latest/error-tracking.md

---
title: Error Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Error Tracking
---

# Error Tracking

View and manage issues within Error Tracking. See the [Error Tracking page](https://docs.datadoghq.com/error_tracking/) for more information.

## Search error tracking issues{% #search-error-tracking-issues %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/search |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/error-tracking/issues/search |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/error-tracking/issues/search      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/error-tracking/issues/search      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/error-tracking/issues/search     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/error-tracking/issues/search |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/error-tracking/issues/search |

### Overview

Search issues endpoint allows you to programmatically search for issues within your organization. This endpoint returns a list of issues that match a given search query, following the event search syntax. The search results are limited to a maximum of 100 issues per request.

OAuth apps require the `error_tracking_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.



### Arguments

#### Query Strings

| Name    | Type  | Description                                                                                                                                                                 |
| ------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include | array | Comma-separated list of relationship objects that should be included in the response. Possible values are `issue`, `issue.assignee`, `issue.case`, and `issue.team_owners`. |

### Request

#### Body Data (required)

Search issues request payload.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                |
| ------------ | ---------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Search issues request.                                                                                                     |
| data         | attributes [*required*] | object | Object describing a search issue request.                                                                                  |
| attributes   | from [*required*]       | int64  | Start date (inclusive) of the query in milliseconds since the Unix epoch.                                                  |
| attributes   | order_by                     | enum   | The attribute to sort the search results by. Allowed enum values: `TOTAL_COUNT,FIRST_SEEN,IMPACTED_SESSIONS,PRIORITY`      |
| attributes   | persona                      | enum   | Persona for the search. Either track(s) or persona(s) must be specified. Allowed enum values: `ALL,BROWSER,MOBILE,BACKEND` |
| attributes   | query [*required*]      | string | Search query following the event search syntax.                                                                            |
| attributes   | to [*required*]         | int64  | End date (exclusive) of the query in milliseconds since the Unix epoch.                                                    |
| attributes   | track                        | enum   | Track of the events to query. Either track(s) or persona(s) must be specified. Allowed enum values: `trace,logs,rum`       |
| data         | type [*required*]       | enum   | Type of the object. Allowed enum values: `search_request`                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Search issues response payload.

| Parent field         | Field                        | Type            | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | [object]        | Array of results matching the search query.                                                                                                                                                           |
| data                 | attributes [*required*] | object          | Object containing the information of a search result.                                                                                                                                                 |
| attributes           | impacted_sessions            | int64           | Count of sessions impacted by the issue over the queried time window.                                                                                                                                 |
| attributes           | impacted_users               | int64           | Count of users impacted by the issue over the queried time window.                                                                                                                                    |
| attributes           | total_count                  | int64           | Total count of errors that match the issue over the queried time window.                                                                                                                              |
| data                 | id [*required*]         | string          | Search result identifier (matches the nested issue's identifier).                                                                                                                                     |
| data                 | relationships                | object          | Relationships between the search result and other resources.                                                                                                                                          |
| relationships        | issue                        | object          | Relationship between the search result and the corresponding issue.                                                                                                                                   |
| issue                | data [*required*]       | object          | The issue the search result corresponds to.                                                                                                                                                           |
| data                 | id [*required*]         | string          | Issue identifier.                                                                                                                                                                                     |
| data                 | type [*required*]       | enum            | Type of the object. Allowed enum values: `issue`                                                                                                                                                      |
| data                 | type [*required*]       | enum            | Type of the object. Allowed enum values: `error_tracking_search_result`                                                                                                                               |
|                      | included                     | [ <oneOf>] | Array of resources related to the search results.                                                                                                                                                     |
| included             | Option 1                     | object          | The issue matching the request.                                                                                                                                                                       |
| Option 1             | attributes [*required*] | object          | Object containing the information of an issue.                                                                                                                                                        |
| attributes           | error_message                | string          | Error message associated with the issue.                                                                                                                                                              |
| attributes           | error_type                   | string          | Type of the error that matches the issue.                                                                                                                                                             |
| attributes           | file_path                    | string          | Path of the file where the issue occurred.                                                                                                                                                            |
| attributes           | first_seen                   | int64           | Timestamp of the first seen error in milliseconds since the Unix epoch.                                                                                                                               |
| attributes           | first_seen_version           | string          | The application version (for example, git commit hash) where the issue was first observed.                                                                                                            |
| attributes           | function_name                | string          | Name of the function where the issue occurred.                                                                                                                                                        |
| attributes           | is_crash                     | boolean         | Error is a crash.                                                                                                                                                                                     |
| attributes           | languages                    | [string]        | Array of programming languages associated with the issue.                                                                                                                                             |
| attributes           | last_seen                    | int64           | Timestamp of the last seen error in milliseconds since the Unix epoch.                                                                                                                                |
| attributes           | last_seen_version            | string          | The application version (for example, git commit hash) where the issue was last observed.                                                                                                             |
| attributes           | platform                     | enum            | Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`                                                                              |
| attributes           | service                      | string          | Service name.                                                                                                                                                                                         |
| attributes           | state                        | enum            | State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`                                                                                                                 |
| Option 1             | id [*required*]         | string          | Issue identifier.                                                                                                                                                                                     |
| Option 1             | relationships                | object          | Relationship between the issue and an assignee, case and/or teams.                                                                                                                                    |
| relationships        | assignee                     | object          | Relationship between the issue and assignee.                                                                                                                                                          |
| assignee             | data [*required*]       | object          | The user the issue is assigned to.                                                                                                                                                                    |
| data                 | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| data                 | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| relationships        | case                         | object          | Relationship between the issue and case.                                                                                                                                                              |
| case                 | data [*required*]       | object          | The case the issue is attached to.                                                                                                                                                                    |
| data                 | id [*required*]         | string          | Case identifier.                                                                                                                                                                                      |
| data                 | type [*required*]       | enum            | Type of the object. Allowed enum values: `case`                                                                                                                                                       |
| relationships        | team_owners                  | object          | Relationship between the issue and teams.                                                                                                                                                             |
| team_owners          | data [*required*]       | [object]        | Array of teams that are owners of the issue.                                                                                                                                                          |
| data                 | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| data                 | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |
| Option 1             | type [*required*]       | enum            | Type of the object. Allowed enum values: `issue`                                                                                                                                                      |
| included             | Option 2                     | object          | A case                                                                                                                                                                                                |
| Option 2             | attributes [*required*] | object          | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time       | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object          | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]        |
| attributes           | closed_at                    | date-time       | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time       | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object          | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object          | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean         | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum            | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf>   | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string          | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]        | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double          | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]        | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string          | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object          | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object          | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string          | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string          | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string          | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string          | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum            | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string          | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time       | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum            | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object          | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object          | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string          | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum            | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum            | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum            | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string          | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string          | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum            | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string          | Case type UUID                                                                                                                                                                                        |
| Option 2             | id [*required*]         | string          | Case's identifier                                                                                                                                                                                     |
| Option 2             | relationships                | object          | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object          | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object          | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object          | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object          | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object          | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string          | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum            | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| Option 2             | type [*required*]       | enum            | Case resource type Allowed enum values: `case`                                                                                                                                                        |
| included             | Option 3                     | object          | The user to whom the issue is assigned.                                                                                                                                                               |
| Option 3             | attributes [*required*] | object          | Object containing the information of a user.                                                                                                                                                          |
| attributes           | email                        | string          | Email of the user.                                                                                                                                                                                    |
| attributes           | handle                       | string          | Handle of the user.                                                                                                                                                                                   |
| attributes           | name                         | string          | Name of the user.                                                                                                                                                                                     |
| Option 3             | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| Option 3             | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| included             | Option 4                     | object          | A team that owns an issue.                                                                                                                                                                            |
| Option 4             | attributes [*required*] | object          | Object containing the information of a team.                                                                                                                                                          |
| attributes           | handle                       | string          | The team's identifier.                                                                                                                                                                                |
| attributes           | name                         | string          | The name of the team.                                                                                                                                                                                 |
| attributes           | summary                      | string          | A brief summary of the team, derived from its description.                                                                                                                                            |
| Option 4             | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| Option 4             | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
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

{% tab title="401" %}
Unauthorized
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/search" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get the details of an error tracking issue{% #get-the-details-of-an-error-tracking-issue %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id} |

### Overview

Retrieve the full details for a specific error tracking issue, including attributes and relationships.

OAuth apps require the `error_tracking_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.



### Arguments

#### Path Parameters

| Name                       | Type   | Description                  |
| -------------------------- | ------ | ---------------------------- |
| issue_id [*required*] | string | The identifier of the issue. |

#### Query Strings

| Name    | Type  | Description                                                                                                                                      |
| ------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| include | array | Comma-separated list of relationship objects that should be included in the response. Possible values are `assignee`, `case`, and `team_owners`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing error tracking issue data.

| Parent field  | Field                        | Type            | Description                                                                                                                                                                                           |
| ------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                         | object          | The issue matching the request.                                                                                                                                                                       |
| data          | attributes [*required*] | object          | Object containing the information of an issue.                                                                                                                                                        |
| attributes    | error_message                | string          | Error message associated with the issue.                                                                                                                                                              |
| attributes    | error_type                   | string          | Type of the error that matches the issue.                                                                                                                                                             |
| attributes    | file_path                    | string          | Path of the file where the issue occurred.                                                                                                                                                            |
| attributes    | first_seen                   | int64           | Timestamp of the first seen error in milliseconds since the Unix epoch.                                                                                                                               |
| attributes    | first_seen_version           | string          | The application version (for example, git commit hash) where the issue was first observed.                                                                                                            |
| attributes    | function_name                | string          | Name of the function where the issue occurred.                                                                                                                                                        |
| attributes    | is_crash                     | boolean         | Error is a crash.                                                                                                                                                                                     |
| attributes    | languages                    | [string]        | Array of programming languages associated with the issue.                                                                                                                                             |
| attributes    | last_seen                    | int64           | Timestamp of the last seen error in milliseconds since the Unix epoch.                                                                                                                                |
| attributes    | last_seen_version            | string          | The application version (for example, git commit hash) where the issue was last observed.                                                                                                             |
| attributes    | platform                     | enum            | Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`                                                                              |
| attributes    | service                      | string          | Service name.                                                                                                                                                                                         |
| attributes    | state                        | enum            | State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`                                                                                                                 |
| data          | id [*required*]         | string          | Issue identifier.                                                                                                                                                                                     |
| data          | relationships                | object          | Relationship between the issue and an assignee, case and/or teams.                                                                                                                                    |
| relationships | assignee                     | object          | Relationship between the issue and assignee.                                                                                                                                                          |
| assignee      | data [*required*]       | object          | The user the issue is assigned to.                                                                                                                                                                    |
| data          | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| relationships | case                         | object          | Relationship between the issue and case.                                                                                                                                                              |
| case          | data [*required*]       | object          | The case the issue is attached to.                                                                                                                                                                    |
| data          | id [*required*]         | string          | Case identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `case`                                                                                                                                                       |
| relationships | team_owners                  | object          | Relationship between the issue and teams.                                                                                                                                                             |
| team_owners   | data [*required*]       | [object]        | Array of teams that are owners of the issue.                                                                                                                                                          |
| data          | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `issue`                                                                                                                                                      |
|               | included                     | [ <oneOf>] | Array of resources related to the issue.                                                                                                                                                              |
| included      | Option 1                     | object          | The case attached to the issue.                                                                                                                                                                       |
| Option 1      | attributes [*required*] | object          | Object containing the information of a case.                                                                                                                                                          |
| attributes    | archived_at                  | date-time       | Timestamp of when the case was archived.                                                                                                                                                              |
| attributes    | closed_at                    | date-time       | Timestamp of when the case was closed.                                                                                                                                                                |
| attributes    | created_at                   | date-time       | Timestamp of when the case was created.                                                                                                                                                               |
| attributes    | creation_source              | string          | Source of the case creation.                                                                                                                                                                          |
| attributes    | description                  | string          | Description of the case.                                                                                                                                                                              |
| attributes    | due_date                     | string          | Due date of the case.                                                                                                                                                                                 |
| attributes    | insights                     | [object]        | Insights of the case.                                                                                                                                                                                 |
| insights      | ref                          | string          | Reference of the insight.                                                                                                                                                                             |
| insights      | resource_id                  | string          | Insight identifier.                                                                                                                                                                                   |
| insights      | type                         | string          | Type of the insight.                                                                                                                                                                                  |
| attributes    | jira_issue                   | object          | Jira issue of the case.                                                                                                                                                                               |
| jira_issue    | result                       | object          | Contains the identifiers and URL for a successfully created Jira issue.                                                                                                                               |
| result        | issue_id                     | string          | Jira issue identifier.                                                                                                                                                                                |
| result        | issue_key                    | string          | Jira issue key.                                                                                                                                                                                       |
| result        | issue_url                    | string          | Jira issue URL.                                                                                                                                                                                       |
| result        | project_key                  | string          | Jira project key.                                                                                                                                                                                     |
| jira_issue    | status                       | string          | Creation status of the Jira issue.                                                                                                                                                                    |
| attributes    | key                          | string          | Key of the case.                                                                                                                                                                                      |
| attributes    | modified_at                  | date-time       | Timestamp of when the case was last modified.                                                                                                                                                         |
| attributes    | priority                     | enum            | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes    | status                       | enum            | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes    | title                        | string          | Title of the case.                                                                                                                                                                                    |
| attributes    | type                         | string          | Type of the case.                                                                                                                                                                                     |
| Option 1      | id [*required*]         | string          | Case identifier.                                                                                                                                                                                      |
| Option 1      | relationships                | object          | Resources related to a case.                                                                                                                                                                          |
| relationships | assignee                     | object          | Relationship to user.                                                                                                                                                                                 |
| assignee      | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | created_by                   | object          | Relationship to user.                                                                                                                                                                                 |
| created_by    | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | modified_by                  | object          | Relationship to user.                                                                                                                                                                                 |
| modified_by   | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | project                      | object          | Relationship to project                                                                                                                                                                               |
| project       | data [*required*]       | object          | Relationship to project object                                                                                                                                                                        |
| data          | id [*required*]         | string          | A unique identifier that represents the project                                                                                                                                                       |
| data          | type [*required*]       | enum            | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| Option 1      | type [*required*]       | enum            | Type of the object. Allowed enum values: `case`                                                                                                                                                       |
| included      | Option 2                     | object          | The user to whom the issue is assigned.                                                                                                                                                               |
| Option 2      | attributes [*required*] | object          | Object containing the information of a user.                                                                                                                                                          |
| attributes    | email                        | string          | Email of the user.                                                                                                                                                                                    |
| attributes    | handle                       | string          | Handle of the user.                                                                                                                                                                                   |
| attributes    | name                         | string          | Name of the user.                                                                                                                                                                                     |
| Option 2      | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| Option 2      | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| included      | Option 3                     | object          | A team that owns an issue.                                                                                                                                                                            |
| Option 3      | attributes [*required*] | object          | Object containing the information of a team.                                                                                                                                                          |
| attributes    | handle                       | string          | The team's identifier.                                                                                                                                                                                |
| attributes    | name                         | string          | The name of the team.                                                                                                                                                                                 |
| attributes    | summary                      | string          | A brief summary of the team, derived from its description.                                                                                                                                            |
| Option 3      | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| Option 3      | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
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

{% tab title="401" %}
Unauthorized
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
                  \# Path parametersexport issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get the details of an error tracking issue returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ErrorTrackingAPI.new

# there is a valid "issue" in the system
ISSUE_ID = ENV["ISSUE_ID"]
p api_instance.get_issue(ISSUE_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update the state of an issue{% #update-the-state-of-an-issue %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/state |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/state |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}/state      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}/state      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/state     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/state |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/state |

### Overview

Update the state of an issue by `issue_id`. Use this endpoint to move an issue between states such as `OPEN`, `RESOLVED`, or `IGNORED`.

OAuth apps require the `error_tracking_read, error_tracking_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.



### Arguments

#### Path Parameters

| Name                       | Type   | Description                  |
| -------------------------- | ------ | ---------------------------- |
| issue_id [*required*] | string | The identifier of the issue. |

### Request

#### Body Data (required)

Update issue state request payload.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                           |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Update issue state request.                                                           |
| data         | attributes [*required*] | object | Object describing an issue state update request.                                      |
| attributes   | state [*required*]      | enum   | State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED` |
| data         | id [*required*]         | string | Issue identifier.                                                                     |
| data         | type [*required*]       | enum   | Type of the object. Allowed enum values: `error_tracking_issue`                       |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing error tracking issue data.

| Parent field  | Field                        | Type            | Description                                                                                                                                                                                           |
| ------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                         | object          | The issue matching the request.                                                                                                                                                                       |
| data          | attributes [*required*] | object          | Object containing the information of an issue.                                                                                                                                                        |
| attributes    | error_message                | string          | Error message associated with the issue.                                                                                                                                                              |
| attributes    | error_type                   | string          | Type of the error that matches the issue.                                                                                                                                                             |
| attributes    | file_path                    | string          | Path of the file where the issue occurred.                                                                                                                                                            |
| attributes    | first_seen                   | int64           | Timestamp of the first seen error in milliseconds since the Unix epoch.                                                                                                                               |
| attributes    | first_seen_version           | string          | The application version (for example, git commit hash) where the issue was first observed.                                                                                                            |
| attributes    | function_name                | string          | Name of the function where the issue occurred.                                                                                                                                                        |
| attributes    | is_crash                     | boolean         | Error is a crash.                                                                                                                                                                                     |
| attributes    | languages                    | [string]        | Array of programming languages associated with the issue.                                                                                                                                             |
| attributes    | last_seen                    | int64           | Timestamp of the last seen error in milliseconds since the Unix epoch.                                                                                                                                |
| attributes    | last_seen_version            | string          | The application version (for example, git commit hash) where the issue was last observed.                                                                                                             |
| attributes    | platform                     | enum            | Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`                                                                              |
| attributes    | service                      | string          | Service name.                                                                                                                                                                                         |
| attributes    | state                        | enum            | State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`                                                                                                                 |
| data          | id [*required*]         | string          | Issue identifier.                                                                                                                                                                                     |
| data          | relationships                | object          | Relationship between the issue and an assignee, case and/or teams.                                                                                                                                    |
| relationships | assignee                     | object          | Relationship between the issue and assignee.                                                                                                                                                          |
| assignee      | data [*required*]       | object          | The user the issue is assigned to.                                                                                                                                                                    |
| data          | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| relationships | case                         | object          | Relationship between the issue and case.                                                                                                                                                              |
| case          | data [*required*]       | object          | The case the issue is attached to.                                                                                                                                                                    |
| data          | id [*required*]         | string          | Case identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `case`                                                                                                                                                       |
| relationships | team_owners                  | object          | Relationship between the issue and teams.                                                                                                                                                             |
| team_owners   | data [*required*]       | [object]        | Array of teams that are owners of the issue.                                                                                                                                                          |
| data          | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `issue`                                                                                                                                                      |
|               | included                     | [ <oneOf>] | Array of resources related to the issue.                                                                                                                                                              |
| included      | Option 1                     | object          | The case attached to the issue.                                                                                                                                                                       |
| Option 1      | attributes [*required*] | object          | Object containing the information of a case.                                                                                                                                                          |
| attributes    | archived_at                  | date-time       | Timestamp of when the case was archived.                                                                                                                                                              |
| attributes    | closed_at                    | date-time       | Timestamp of when the case was closed.                                                                                                                                                                |
| attributes    | created_at                   | date-time       | Timestamp of when the case was created.                                                                                                                                                               |
| attributes    | creation_source              | string          | Source of the case creation.                                                                                                                                                                          |
| attributes    | description                  | string          | Description of the case.                                                                                                                                                                              |
| attributes    | due_date                     | string          | Due date of the case.                                                                                                                                                                                 |
| attributes    | insights                     | [object]        | Insights of the case.                                                                                                                                                                                 |
| insights      | ref                          | string          | Reference of the insight.                                                                                                                                                                             |
| insights      | resource_id                  | string          | Insight identifier.                                                                                                                                                                                   |
| insights      | type                         | string          | Type of the insight.                                                                                                                                                                                  |
| attributes    | jira_issue                   | object          | Jira issue of the case.                                                                                                                                                                               |
| jira_issue    | result                       | object          | Contains the identifiers and URL for a successfully created Jira issue.                                                                                                                               |
| result        | issue_id                     | string          | Jira issue identifier.                                                                                                                                                                                |
| result        | issue_key                    | string          | Jira issue key.                                                                                                                                                                                       |
| result        | issue_url                    | string          | Jira issue URL.                                                                                                                                                                                       |
| result        | project_key                  | string          | Jira project key.                                                                                                                                                                                     |
| jira_issue    | status                       | string          | Creation status of the Jira issue.                                                                                                                                                                    |
| attributes    | key                          | string          | Key of the case.                                                                                                                                                                                      |
| attributes    | modified_at                  | date-time       | Timestamp of when the case was last modified.                                                                                                                                                         |
| attributes    | priority                     | enum            | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes    | status                       | enum            | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes    | title                        | string          | Title of the case.                                                                                                                                                                                    |
| attributes    | type                         | string          | Type of the case.                                                                                                                                                                                     |
| Option 1      | id [*required*]         | string          | Case identifier.                                                                                                                                                                                      |
| Option 1      | relationships                | object          | Resources related to a case.                                                                                                                                                                          |
| relationships | assignee                     | object          | Relationship to user.                                                                                                                                                                                 |
| assignee      | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | created_by                   | object          | Relationship to user.                                                                                                                                                                                 |
| created_by    | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | modified_by                  | object          | Relationship to user.                                                                                                                                                                                 |
| modified_by   | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | project                      | object          | Relationship to project                                                                                                                                                                               |
| project       | data [*required*]       | object          | Relationship to project object                                                                                                                                                                        |
| data          | id [*required*]         | string          | A unique identifier that represents the project                                                                                                                                                       |
| data          | type [*required*]       | enum            | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| Option 1      | type [*required*]       | enum            | Type of the object. Allowed enum values: `case`                                                                                                                                                       |
| included      | Option 2                     | object          | The user to whom the issue is assigned.                                                                                                                                                               |
| Option 2      | attributes [*required*] | object          | Object containing the information of a user.                                                                                                                                                          |
| attributes    | email                        | string          | Email of the user.                                                                                                                                                                                    |
| attributes    | handle                       | string          | Handle of the user.                                                                                                                                                                                   |
| attributes    | name                         | string          | Name of the user.                                                                                                                                                                                     |
| Option 2      | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| Option 2      | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| included      | Option 3                     | object          | A team that owns an issue.                                                                                                                                                                            |
| Option 3      | attributes [*required*] | object          | Object containing the information of a team.                                                                                                                                                          |
| attributes    | handle                       | string          | The team's identifier.                                                                                                                                                                                |
| attributes    | name                         | string          | The name of the team.                                                                                                                                                                                 |
| attributes    | summary                      | string          | A brief summary of the team, derived from its description.                                                                                                                                            |
| Option 3      | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| Option 3      | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
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

{% tab title="401" %}
Unauthorized
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
                          \# Path parametersexport issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}/state" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update the assignee of an issue{% #update-the-assignee-of-an-issue %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}/assignee      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}/assignee      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |

### Overview

Update the assignee of an issue by `issue_id`.

OAuth apps require the `error_tracking_read, error_tracking_write, cases_read, cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.



### Arguments

#### Path Parameters

| Name                       | Type   | Description                  |
| -------------------------- | ------ | ---------------------------- |
| issue_id [*required*] | string | The identifier of the issue. |

### Request

#### Body Data (required)

Update issue assignee request payload.

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                         |
| ------------ | ---------------------- | ------ | --------------------------------------------------- |
|              | data [*required*] | object | Update issue assignee request.                      |
| data         | id [*required*]   | string | User identifier.                                    |
| data         | type [*required*] | enum   | Type of the object. Allowed enum values: `assignee` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "87cb11a0-278c-440a-99fe-701223c80296",
    "type": "assignee"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing error tracking issue data.

| Parent field  | Field                        | Type            | Description                                                                                                                                                                                           |
| ------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                         | object          | The issue matching the request.                                                                                                                                                                       |
| data          | attributes [*required*] | object          | Object containing the information of an issue.                                                                                                                                                        |
| attributes    | error_message                | string          | Error message associated with the issue.                                                                                                                                                              |
| attributes    | error_type                   | string          | Type of the error that matches the issue.                                                                                                                                                             |
| attributes    | file_path                    | string          | Path of the file where the issue occurred.                                                                                                                                                            |
| attributes    | first_seen                   | int64           | Timestamp of the first seen error in milliseconds since the Unix epoch.                                                                                                                               |
| attributes    | first_seen_version           | string          | The application version (for example, git commit hash) where the issue was first observed.                                                                                                            |
| attributes    | function_name                | string          | Name of the function where the issue occurred.                                                                                                                                                        |
| attributes    | is_crash                     | boolean         | Error is a crash.                                                                                                                                                                                     |
| attributes    | languages                    | [string]        | Array of programming languages associated with the issue.                                                                                                                                             |
| attributes    | last_seen                    | int64           | Timestamp of the last seen error in milliseconds since the Unix epoch.                                                                                                                                |
| attributes    | last_seen_version            | string          | The application version (for example, git commit hash) where the issue was last observed.                                                                                                             |
| attributes    | platform                     | enum            | Platform associated with the issue. Allowed enum values: `ANDROID,BACKEND,BROWSER,FLUTTER,IOS,REACT_NATIVE,ROKU,UNKNOWN`                                                                              |
| attributes    | service                      | string          | Service name.                                                                                                                                                                                         |
| attributes    | state                        | enum            | State of the issue Allowed enum values: `OPEN,ACKNOWLEDGED,RESOLVED,IGNORED,EXCLUDED`                                                                                                                 |
| data          | id [*required*]         | string          | Issue identifier.                                                                                                                                                                                     |
| data          | relationships                | object          | Relationship between the issue and an assignee, case and/or teams.                                                                                                                                    |
| relationships | assignee                     | object          | Relationship between the issue and assignee.                                                                                                                                                          |
| assignee      | data [*required*]       | object          | The user the issue is assigned to.                                                                                                                                                                    |
| data          | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| relationships | case                         | object          | Relationship between the issue and case.                                                                                                                                                              |
| case          | data [*required*]       | object          | The case the issue is attached to.                                                                                                                                                                    |
| data          | id [*required*]         | string          | Case identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `case`                                                                                                                                                       |
| relationships | team_owners                  | object          | Relationship between the issue and teams.                                                                                                                                                             |
| team_owners   | data [*required*]       | [object]        | Array of teams that are owners of the issue.                                                                                                                                                          |
| data          | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |
| data          | type [*required*]       | enum            | Type of the object. Allowed enum values: `issue`                                                                                                                                                      |
|               | included                     | [ <oneOf>] | Array of resources related to the issue.                                                                                                                                                              |
| included      | Option 1                     | object          | The case attached to the issue.                                                                                                                                                                       |
| Option 1      | attributes [*required*] | object          | Object containing the information of a case.                                                                                                                                                          |
| attributes    | archived_at                  | date-time       | Timestamp of when the case was archived.                                                                                                                                                              |
| attributes    | closed_at                    | date-time       | Timestamp of when the case was closed.                                                                                                                                                                |
| attributes    | created_at                   | date-time       | Timestamp of when the case was created.                                                                                                                                                               |
| attributes    | creation_source              | string          | Source of the case creation.                                                                                                                                                                          |
| attributes    | description                  | string          | Description of the case.                                                                                                                                                                              |
| attributes    | due_date                     | string          | Due date of the case.                                                                                                                                                                                 |
| attributes    | insights                     | [object]        | Insights of the case.                                                                                                                                                                                 |
| insights      | ref                          | string          | Reference of the insight.                                                                                                                                                                             |
| insights      | resource_id                  | string          | Insight identifier.                                                                                                                                                                                   |
| insights      | type                         | string          | Type of the insight.                                                                                                                                                                                  |
| attributes    | jira_issue                   | object          | Jira issue of the case.                                                                                                                                                                               |
| jira_issue    | result                       | object          | Contains the identifiers and URL for a successfully created Jira issue.                                                                                                                               |
| result        | issue_id                     | string          | Jira issue identifier.                                                                                                                                                                                |
| result        | issue_key                    | string          | Jira issue key.                                                                                                                                                                                       |
| result        | issue_url                    | string          | Jira issue URL.                                                                                                                                                                                       |
| result        | project_key                  | string          | Jira project key.                                                                                                                                                                                     |
| jira_issue    | status                       | string          | Creation status of the Jira issue.                                                                                                                                                                    |
| attributes    | key                          | string          | Key of the case.                                                                                                                                                                                      |
| attributes    | modified_at                  | date-time       | Timestamp of when the case was last modified.                                                                                                                                                         |
| attributes    | priority                     | enum            | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes    | status                       | enum            | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes    | title                        | string          | Title of the case.                                                                                                                                                                                    |
| attributes    | type                         | string          | Type of the case.                                                                                                                                                                                     |
| Option 1      | id [*required*]         | string          | Case identifier.                                                                                                                                                                                      |
| Option 1      | relationships                | object          | Resources related to a case.                                                                                                                                                                          |
| relationships | assignee                     | object          | Relationship to user.                                                                                                                                                                                 |
| assignee      | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | created_by                   | object          | Relationship to user.                                                                                                                                                                                 |
| created_by    | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | modified_by                  | object          | Relationship to user.                                                                                                                                                                                 |
| modified_by   | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                          |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                         |
| data          | type [*required*]       | enum            | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships | project                      | object          | Relationship to project                                                                                                                                                                               |
| project       | data [*required*]       | object          | Relationship to project object                                                                                                                                                                        |
| data          | id [*required*]         | string          | A unique identifier that represents the project                                                                                                                                                       |
| data          | type [*required*]       | enum            | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| Option 1      | type [*required*]       | enum            | Type of the object. Allowed enum values: `case`                                                                                                                                                       |
| included      | Option 2                     | object          | The user to whom the issue is assigned.                                                                                                                                                               |
| Option 2      | attributes [*required*] | object          | Object containing the information of a user.                                                                                                                                                          |
| attributes    | email                        | string          | Email of the user.                                                                                                                                                                                    |
| attributes    | handle                       | string          | Handle of the user.                                                                                                                                                                                   |
| attributes    | name                         | string          | Name of the user.                                                                                                                                                                                     |
| Option 2      | id [*required*]         | string          | User identifier.                                                                                                                                                                                      |
| Option 2      | type [*required*]       | enum            | Type of the object Allowed enum values: `user`                                                                                                                                                        |
| included      | Option 3                     | object          | A team that owns an issue.                                                                                                                                                                            |
| Option 3      | attributes [*required*] | object          | Object containing the information of a team.                                                                                                                                                          |
| attributes    | handle                       | string          | The team's identifier.                                                                                                                                                                                |
| attributes    | name                         | string          | The name of the team.                                                                                                                                                                                 |
| attributes    | summary                      | string          | A brief summary of the team, derived from its description.                                                                                                                                            |
| Option 3      | id [*required*]         | string          | Team identifier.                                                                                                                                                                                      |
| Option 3      | type [*required*]       | enum            | Type of the object. Allowed enum values: `team`                                                                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
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

{% tab title="401" %}
Unauthorized
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
                          \# Path parametersexport issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}/assignee" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Remove the assignee of an issue{% #remove-the-assignee-of-an-issue %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/error-tracking/issues/{issue_id}/assignee      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/error-tracking/issues/{issue_id}/assignee      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/error-tracking/issues/{issue_id}/assignee |

### Overview

Remove the assignee of an issue by `issue_id`.

OAuth apps require the `error_tracking_read, error_tracking_write, cases_read, cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#error-tracking) to access this endpoint.



### Arguments

#### Path Parameters

| Name                       | Type   | Description                  |
| -------------------------- | ------ | ---------------------------- |
| issue_id [*required*] | string | The identifier of the issue. |

### Response

{% tab title="204" %}
No Content
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

{% tab title="401" %}
Unauthorized
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
                  \# Path parametersexport issue_id="c1726a66-1f64-11ee-b338-da7ad0900002"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/error-tracking/issues/${issue_id}/assignee" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Remove the assignee of an issue returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ErrorTrackingAPI.new

# there is a valid "issue" in the system
ISSUE_ID = ENV["ISSUE_ID"]
api_instance.delete_issue_assignee(ISSUE_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
