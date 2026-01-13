# Source: https://docs.datadoghq.com/api/latest/case-management

# Case Management
View and manage cases and projects within Case Management. See the [Case Management page](https://docs.datadoghq.com/service_management/case_management/) for more information.
## [Create a project](https://docs.datadoghq.com/api/latest/case-management/#create-a-project)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#create-a-project-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/projectshttps://api.ap2.datadoghq.com/api/v2/cases/projectshttps://api.datadoghq.eu/api/v2/cases/projectshttps://api.ddog-gov.com/api/v2/cases/projectshttps://api.datadoghq.com/api/v2/cases/projectshttps://api.us3.datadoghq.com/api/v2/cases/projectshttps://api.us5.datadoghq.com/api/v2/cases/projects
### Overview
Create a project.
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Request
#### Body Data (required)
Project payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Project create
attributes [_required_]
object
Project creation attributes
key [_required_]
string
Project's key. Cannot be "CASE"
name [_required_]
string
name
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
```
{
  "data": {
    "attributes": {
      "key": "SEC",
      "name": "Security Investigation"
    },
    "type": "project"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/case-management/#CreateProject-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#CreateProject-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#CreateProject-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#CreateProject-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#CreateProject-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#CreateProject-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Project response
Field
Type
Description
data
object
A Project
attributes [_required_]
object
Project attributes
key
string
The project's key
name
string
Project's name
id [_required_]
string
The Project's identifier
relationships
object
Project relationships
member_team
object
Relationship between a team and a team link
data
[object]
Related team links
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
links
object
Links attributes.
related
string
Related link.
member_user
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
```
{
  "data": {
    "attributes": {
      "key": "CASEM",
      "name": "string"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "relationships": {
      "member_team": {
        "data": [
          {
            "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
            "type": "team_links"
          }
        ],
        "links": {
          "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
        }
      },
      "member_user": {
        "data": [
          {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        ]
      }
    },
    "type": "project"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Create a project
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "key": "SEC",
      "name": "Security Investigation"
    },
    "type": "project"
  }
}
EOF  

                
```

#####  Create a project
```
"""
Create a project returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.project_create import ProjectCreate
from datadog_api_client.v2.model.project_create_attributes import ProjectCreateAttributes
from datadog_api_client.v2.model.project_create_request import ProjectCreateRequest
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType

body = ProjectCreateRequest(
    data=ProjectCreate(
        attributes=ProjectCreateAttributes(
            key="SEC",
            name="Security Investigation",
        ),
        type=ProjectResourceType.PROJECT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_project(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a project
```
# Create a project returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::ProjectCreateRequest.new({
  data: DatadogAPIClient::V2::ProjectCreate.new({
    attributes: DatadogAPIClient::V2::ProjectCreateAttributes.new({
      key: "SEC",
      name: "Security Investigation",
    }),
    type: DatadogAPIClient::V2::ProjectResourceType::PROJECT,
  }),
})
p api_instance.create_project(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a project
```
// Create a project returns "CREATED" response

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
	body := datadogV2.ProjectCreateRequest{
		Data: datadogV2.ProjectCreate{
			Attributes: datadogV2.ProjectCreateAttributes{
				Key:  "SEC",
				Name: "Security Investigation",
			},
			Type: datadogV2.PROJECTRESOURCETYPE_PROJECT,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.CreateProject(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.CreateProject`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.CreateProject`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a project
```
// Create a project returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.ProjectCreate;
import com.datadog.api.client.v2.model.ProjectCreateAttributes;
import com.datadog.api.client.v2.model.ProjectCreateRequest;
import com.datadog.api.client.v2.model.ProjectResourceType;
import com.datadog.api.client.v2.model.ProjectResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    ProjectCreateRequest body =
        new ProjectCreateRequest()
            .data(
                new ProjectCreate()
                    .attributes(
                        new ProjectCreateAttributes().key("SEC").name("Security Investigation"))
                    .type(ProjectResourceType.PROJECT));

    try {
      ProjectResponse result = apiInstance.createProject(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#createProject");
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

#####  Create a project
```
// Create a project returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::ProjectCreate;
use datadog_api_client::datadogV2::model::ProjectCreateAttributes;
use datadog_api_client::datadogV2::model::ProjectCreateRequest;
use datadog_api_client::datadogV2::model::ProjectResourceType;

#[tokio::main]
async fn main() {
    let body = ProjectCreateRequest::new(ProjectCreate::new(
        ProjectCreateAttributes::new("SEC".to_string(), "Security Investigation".to_string()),
        ProjectResourceType::PROJECT,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.create_project(body).await;
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

#####  Create a project
```
/**
 * Create a project returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiCreateProjectRequest = {
  body: {
    data: {
      attributes: {
        key: "SEC",
        name: "Security Investigation",
      },
      type: "project",
    },
  },
};

apiInstance
  .createProject(params)
  .then((data: v2.ProjectResponse) => {
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
## [Search cases](https://docs.datadoghq.com/api/latest/case-management/#search-cases)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#search-cases-v2)


GET https://api.ap1.datadoghq.com/api/v2/caseshttps://api.ap2.datadoghq.com/api/v2/caseshttps://api.datadoghq.eu/api/v2/caseshttps://api.ddog-gov.com/api/v2/caseshttps://api.datadoghq.com/api/v2/caseshttps://api.us3.datadoghq.com/api/v2/caseshttps://api.us5.datadoghq.com/api/v2/cases
### Overview
Search cases.
OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[number]
integer
Specific page number to return.
sort[field]
enum
Specify which field to sort  
Allowed enum values: `created_at, priority, status`
filter
string
Search query
sort[asc]
boolean
Specify if order is ascending or not
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#SearchCases-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#SearchCases-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#SearchCases-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#SearchCases-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#SearchCases-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#SearchCases-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Response with cases
Field
Type
Description
data
[object]
Cases response data
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
meta
object
Cases response metadata
page
object
Pagination metadata
current
int64
Current page number
size
int64
Number of cases in current page
total
int64
Total number of pages
```
{
  "data": [
    {
      "attributes": {
        "archived_at": "2019-09-19T10:00:00.000Z",
        "attributes": {
          "<any-key>": []
        },
        "closed_at": "2019-09-19T10:00:00.000Z",
        "created_at": "2019-09-19T10:00:00.000Z",
        "custom_attributes": {
          "<any-key>": {
            "is_multi": false,
            "type": "NUMBER",
            "value": {
              "description": "",
              "type": ""
            }
          }
        },
        "description": "string",
        "jira_issue": {
          "result": {
            "issue_id": "string",
            "issue_key": "string",
            "issue_url": "string",
            "project_key": "string"
          },
          "status": "COMPLETED"
        },
        "key": "CASEM-4523",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "priority": "NOT_DEFINED",
        "service_now_ticket": {
          "result": {
            "sys_target_link": "string"
          },
          "status": "COMPLETED"
        },
        "status": "OPEN",
        "title": "Memory leak investigation on API",
        "type": "STANDARD",
        "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
  ],
  "meta": {
    "page": {
      "current": "integer",
      "size": "integer",
      "total": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Search cases
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Search cases
```
"""
Search cases returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.search_cases()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search cases
```
# Search cases returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
p api_instance.search_cases()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search cases
```
// Search cases returns "OK" response

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
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.SearchCases(ctx, *datadogV2.NewSearchCasesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.SearchCases`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.SearchCases`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Search cases
```
// Search cases returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CasesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    try {
      CasesResponse result = apiInstance.searchCases();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#searchCases");
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

#####  Search cases
```
// Search cases returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::api_case_management::SearchCasesOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.search_cases(SearchCasesOptionalParams::default()).await;
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

#####  Search cases
```
/**
 * Search cases returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

apiInstance
  .searchCases()
  .then((data: v2.CasesResponse) => {
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
## [Create a case](https://docs.datadoghq.com/api/latest/case-management/#create-a-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#create-a-case-v2)


POST https://api.ap1.datadoghq.com/api/v2/caseshttps://api.ap2.datadoghq.com/api/v2/caseshttps://api.datadoghq.eu/api/v2/caseshttps://api.ddog-gov.com/api/v2/caseshttps://api.datadoghq.com/api/v2/caseshttps://api.us3.datadoghq.com/api/v2/caseshttps://api.us5.datadoghq.com/api/v2/cases
### Overview
Create a Case
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Request
#### Body Data (required)
Case payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case creation data
attributes [_required_]
object
Case creation attributes
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
priority
enum
Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`
default: `NOT_DEFINED`
title [_required_]
string
Title
type_id [_required_]
string
Case type UUID
relationships
object
Relationships formed with the case on creation
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
project [_required_]
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
```
{
  "data": {
    "attributes": {
      "priority": "NOT_DEFINED",
      "title": "Security breach investigation in 0cfbc5cbc676ee71",
      "type_id": "00000000-0000-0000-0000-000000000001"
    },
    "relationships": {
      "assignee": {
        "data": {
          "id": "string",
          "type": "user"
        }
      },
      "project": {
        "data": {
          "id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
          "type": "project"
        }
      }
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/case-management/#CreateCase-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#CreateCase-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#CreateCase-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#CreateCase-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#CreateCase-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#CreateCase-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Create a case returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "priority": "NOT_DEFINED",
      "title": "Security breach investigation in 0cfbc5cbc676ee71",
      "type_id": "00000000-0000-0000-0000-000000000001"
    },
    "relationships": {
      "assignee": {
        "data": {
          "id": "string",
          "type": "user"
        }
      },
      "project": {
        "data": {
          "id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
          "type": "project"
        }
      }
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Create a case returns "CREATED" response
```
// Create a case returns "CREATED" response

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
	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	body := datadogV2.CaseCreateRequest{
		Data: datadogV2.CaseCreate{
			Attributes: datadogV2.CaseCreateAttributes{
				Priority: datadogV2.CASEPRIORITY_NOT_DEFINED.Ptr(),
				Title:    "Security breach investigation in 0cfbc5cbc676ee71",
				TypeId:   "00000000-0000-0000-0000-000000000001",
			},
			Relationships: &datadogV2.CaseCreateRelationships{
				Assignee: *datadogV2.NewNullableNullableUserRelationship(&datadogV2.NullableUserRelationship{
					Data: *datadogV2.NewNullableNullableUserRelationshipData(&datadogV2.NullableUserRelationshipData{
						Id:   UserDataID,
						Type: datadogV2.USERRESOURCETYPE_USER,
					}),
				}),
				Project: datadogV2.ProjectRelationship{
					Data: datadogV2.ProjectRelationshipData{
						Id:   "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
						Type: datadogV2.PROJECTRESOURCETYPE_PROJECT,
					},
				},
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.CreateCase(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.CreateCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.CreateCase`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a case returns "CREATED" response
```
// Create a case returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseCreate;
import com.datadog.api.client.v2.model.CaseCreateAttributes;
import com.datadog.api.client.v2.model.CaseCreateRelationships;
import com.datadog.api.client.v2.model.CaseCreateRequest;
import com.datadog.api.client.v2.model.CasePriority;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.NullableUserRelationship;
import com.datadog.api.client.v2.model.NullableUserRelationshipData;
import com.datadog.api.client.v2.model.ProjectRelationship;
import com.datadog.api.client.v2.model.ProjectRelationshipData;
import com.datadog.api.client.v2.model.ProjectResourceType;
import com.datadog.api.client.v2.model.UserResourceType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    CaseCreateRequest body =
        new CaseCreateRequest()
            .data(
                new CaseCreate()
                    .attributes(
                        new CaseCreateAttributes()
                            .priority(CasePriority.NOT_DEFINED)
                            .title("Security breach investigation in 0cfbc5cbc676ee71")
                            .typeId("00000000-0000-0000-0000-000000000001"))
                    .relationships(
                        new CaseCreateRelationships()
                            .assignee(
                                new NullableUserRelationship()
                                    .data(
                                        new NullableUserRelationshipData()
                                            .id(USER_DATA_ID)
                                            .type(UserResourceType.USER)))
                            .project(
                                new ProjectRelationship()
                                    .data(
                                        new ProjectRelationshipData()
                                            .id("d4bbe1af-f36e-42f1-87c1-493ca35c320e")
                                            .type(ProjectResourceType.PROJECT))))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.createCase(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#createCase");
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

#####  Create a case returns "CREATED" response
```
"""
Create a case returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_create import CaseCreate
from datadog_api_client.v2.model.case_create_attributes import CaseCreateAttributes
from datadog_api_client.v2.model.case_create_relationships import CaseCreateRelationships
from datadog_api_client.v2.model.case_create_request import CaseCreateRequest
from datadog_api_client.v2.model.case_priority import CasePriority
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.nullable_user_relationship import NullableUserRelationship
from datadog_api_client.v2.model.nullable_user_relationship_data import NullableUserRelationshipData
from datadog_api_client.v2.model.project_relationship import ProjectRelationship
from datadog_api_client.v2.model.project_relationship_data import ProjectRelationshipData
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType
from datadog_api_client.v2.model.user_resource_type import UserResourceType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = CaseCreateRequest(
    data=CaseCreate(
        attributes=CaseCreateAttributes(
            priority=CasePriority.NOT_DEFINED,
            title="Security breach investigation in 0cfbc5cbc676ee71",
            type_id="00000000-0000-0000-0000-000000000001",
        ),
        relationships=CaseCreateRelationships(
            assignee=NullableUserRelationship(
                data=NullableUserRelationshipData(
                    id=USER_DATA_ID,
                    type=UserResourceType.USER,
                ),
            ),
            project=ProjectRelationship(
                data=ProjectRelationshipData(
                    id="d4bbe1af-f36e-42f1-87c1-493ca35c320e",
                    type=ProjectResourceType.PROJECT,
                ),
            ),
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_case(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a case returns "CREATED" response
```
# Create a case returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::CaseCreateRequest.new({
  data: DatadogAPIClient::V2::CaseCreate.new({
    attributes: DatadogAPIClient::V2::CaseCreateAttributes.new({
      priority: DatadogAPIClient::V2::CasePriority::NOT_DEFINED,
      title: "Security breach investigation in 0cfbc5cbc676ee71",
      type_id: "00000000-0000-0000-0000-000000000001",
    }),
    relationships: DatadogAPIClient::V2::CaseCreateRelationships.new({
      assignee: DatadogAPIClient::V2::NullableUserRelationship.new({
        data: DatadogAPIClient::V2::NullableUserRelationshipData.new({
          id: USER_DATA_ID,
          type: DatadogAPIClient::V2::UserResourceType::USER,
        }),
      }),
      project: DatadogAPIClient::V2::ProjectRelationship.new({
        data: DatadogAPIClient::V2::ProjectRelationshipData.new({
          id: "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
          type: DatadogAPIClient::V2::ProjectResourceType::PROJECT,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.create_case(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a case returns "CREATED" response
```
// Create a case returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseCreate;
use datadog_api_client::datadogV2::model::CaseCreateAttributes;
use datadog_api_client::datadogV2::model::CaseCreateRelationships;
use datadog_api_client::datadogV2::model::CaseCreateRequest;
use datadog_api_client::datadogV2::model::CasePriority;
use datadog_api_client::datadogV2::model::CaseResourceType;
use datadog_api_client::datadogV2::model::NullableUserRelationship;
use datadog_api_client::datadogV2::model::NullableUserRelationshipData;
use datadog_api_client::datadogV2::model::ProjectRelationship;
use datadog_api_client::datadogV2::model::ProjectRelationshipData;
use datadog_api_client::datadogV2::model::ProjectResourceType;
use datadog_api_client::datadogV2::model::UserResourceType;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = CaseCreateRequest::new(
        CaseCreate::new(
            CaseCreateAttributes::new(
                "Security breach investigation in 0cfbc5cbc676ee71".to_string(),
                "00000000-0000-0000-0000-000000000001".to_string(),
            )
            .priority(CasePriority::NOT_DEFINED),
            CaseResourceType::CASE,
        )
        .relationships(
            CaseCreateRelationships::new(ProjectRelationship::new(ProjectRelationshipData::new(
                "d4bbe1af-f36e-42f1-87c1-493ca35c320e".to_string(),
                ProjectResourceType::PROJECT,
            )))
            .assignee(Some(NullableUserRelationship::new(Some(
                NullableUserRelationshipData::new(user_data_id.clone(), UserResourceType::USER),
            )))),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.create_case(body).await;
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

#####  Create a case returns "CREATED" response
```
/**
 * Create a case returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.CaseManagementApiCreateCaseRequest = {
  body: {
    data: {
      attributes: {
        priority: "NOT_DEFINED",
        title: "Security breach investigation in 0cfbc5cbc676ee71",
        typeId: "00000000-0000-0000-0000-000000000001",
      },
      relationships: {
        assignee: {
          data: {
            id: USER_DATA_ID,
            type: "user",
          },
        },
        project: {
          data: {
            id: "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
            type: "project",
          },
        },
      },
      type: "case",
    },
  },
};

apiInstance
  .createCase(params)
  .then((data: v2.CaseResponse) => {
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
## [Get all projects](https://docs.datadoghq.com/api/latest/case-management/#get-all-projects)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#get-all-projects-v2)


GET https://api.ap1.datadoghq.com/api/v2/cases/projectshttps://api.ap2.datadoghq.com/api/v2/cases/projectshttps://api.datadoghq.eu/api/v2/cases/projectshttps://api.ddog-gov.com/api/v2/cases/projectshttps://api.datadoghq.com/api/v2/cases/projectshttps://api.us3.datadoghq.com/api/v2/cases/projectshttps://api.us5.datadoghq.com/api/v2/cases/projects
### Overview
Get all projects.
OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#GetProjects-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#GetProjects-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#GetProjects-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#GetProjects-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#GetProjects-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#GetProjects-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Response with projects
Field
Type
Description
data
[object]
Projects response data
attributes [_required_]
object
Project attributes
key
string
The project's key
name
string
Project's name
id [_required_]
string
The Project's identifier
relationships
object
Project relationships
member_team
object
Relationship between a team and a team link
data
[object]
Related team links
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
links
object
Links attributes.
related
string
Related link.
member_user
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
```
{
  "data": [
    {
      "attributes": {
        "key": "CASEM",
        "name": "string"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "relationships": {
        "member_team": {
          "data": [
            {
              "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
              "type": "team_links"
            }
          ],
          "links": {
            "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
          }
        },
        "member_user": {
          "data": [
            {
              "id": "00000000-0000-0000-0000-000000000000",
              "type": "user"
            }
          ]
        }
      },
      "type": "project"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Get all projects
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all projects
```
"""
Get all projects returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.get_projects()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all projects
```
# Get all projects returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
p api_instance.get_projects()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all projects
```
// Get all projects returns "OK" response

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
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.GetProjects(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.GetProjects`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.GetProjects`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all projects
```
// Get all projects returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.ProjectsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    try {
      ProjectsResponse result = apiInstance.getProjects();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#getProjects");
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

#####  Get all projects
```
// Get all projects returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.get_projects().await;
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

#####  Get all projects
```
/**
 * Get all projects returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

apiInstance
  .getProjects()
  .then((data: v2.ProjectsResponse) => {
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
## [Get the details of a case](https://docs.datadoghq.com/api/latest/case-management/#get-the-details-of-a-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#get-the-details-of-a-case-v2)


GET https://api.ap1.datadoghq.com/api/v2/cases/{case_id}https://api.ap2.datadoghq.com/api/v2/cases/{case_id}https://api.datadoghq.eu/api/v2/cases/{case_id}https://api.ddog-gov.com/api/v2/cases/{case_id}https://api.datadoghq.com/api/v2/cases/{case_id}https://api.us3.datadoghq.com/api/v2/cases/{case_id}https://api.us5.datadoghq.com/api/v2/cases/{case_id}
### Overview
Get the details of case by `case_id`
OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#GetCase-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#GetCase-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#GetCase-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#GetCase-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#GetCase-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#GetCase-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Get the details of a case
Copy
```
                  # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the details of a case
```
"""
Get the details of a case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.get_case(
        case_id=CASE_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get the details of a case
```
# Get the details of a case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]
p api_instance.get_case(CASE_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get the details of a case
```
// Get the details of a case returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.GetCase(ctx, CaseID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.GetCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.GetCase`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get the details of a case
```
// Get the details of a case returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    try {
      CaseResponse result = apiInstance.getCase(CASE_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#getCase");
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

#####  Get the details of a case
```
// Get the details of a case returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.get_case(case_id.clone()).await;
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

#####  Get the details of a case
```
/**
 * Get the details of a case returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiGetCaseRequest = {
  caseId: CASE_ID,
};

apiInstance
  .getCase(params)
  .then((data: v2.CaseResponse) => {
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
## [Get the details of a project](https://docs.datadoghq.com/api/latest/case-management/#get-the-details-of-a-project)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#get-the-details-of-a-project-v2)


GET https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id}https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id}https://api.datadoghq.eu/api/v2/cases/projects/{project_id}https://api.ddog-gov.com/api/v2/cases/projects/{project_id}https://api.datadoghq.com/api/v2/cases/projects/{project_id}https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id}https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id}
### Overview
Get the details of a project by `project_id`.
OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
project_id [_required_]
string
Project UUID
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#GetProject-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#GetProject-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#GetProject-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#GetProject-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#GetProject-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#GetProject-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Project response
Field
Type
Description
data
object
A Project
attributes [_required_]
object
Project attributes
key
string
The project's key
name
string
Project's name
id [_required_]
string
The Project's identifier
relationships
object
Project relationships
member_team
object
Relationship between a team and a team link
data
[object]
Related team links
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
links
object
Links attributes.
related
string
Related link.
member_user
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
User resource type. Allowed enum values: `user`
default: `user`
type [_required_]
enum
Project resource type Allowed enum values: `project`
default: `project`
```
{
  "data": {
    "attributes": {
      "key": "CASEM",
      "name": "string"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "relationships": {
      "member_team": {
        "data": [
          {
            "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
            "type": "team_links"
          }
        ],
        "links": {
          "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
        }
      },
      "member_user": {
        "data": [
          {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        ]
      }
    },
    "type": "project"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)


#####  Get the details of a project
Copy
```
                  # Path parameters  
export project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the details of a project
```
"""
Get the details of a project returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.get_project(
        project_id="project_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get the details of a project
```
# Get the details of a project returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
p api_instance.get_project("project_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get the details of a project
```
/**
 * Get the details of a project returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiGetProjectRequest = {
  projectId: "project_id",
};

apiInstance
  .getProject(params)
  .then((data: v2.ProjectResponse) => {
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

#####  Get the details of a project
```
// Get the details of a project returns "OK" response

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
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.GetProject(ctx, "project_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.GetProject`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.GetProject`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get the details of a project
```
// Get the details of a project returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.ProjectResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    try {
      ProjectResponse result = apiInstance.getProject("e555e290-ed65-49bd-ae18-8acbfcf18db7");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#getProject");
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

#####  Get the details of a project
```
// Get the details of a project returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.get_project("project_id".to_string()).await;
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

* * *
## [Remove a project](https://docs.datadoghq.com/api/latest/case-management/#remove-a-project)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#remove-a-project-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id}https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id}https://api.datadoghq.eu/api/v2/cases/projects/{project_id}https://api.ddog-gov.com/api/v2/cases/projects/{project_id}https://api.datadoghq.com/api/v2/cases/projects/{project_id}https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id}https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id}
### Overview
Remove a project using the project’s `id`.
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
project_id [_required_]
string
Project UUID
### Response
  * [204](https://docs.datadoghq.com/api/latest/case-management/#DeleteProject-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#DeleteProject-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#DeleteProject-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#DeleteProject-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
API error response
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Remove a project
Copy
```
                  # Path parameters  
export project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove a project
```
"""
Remove a project returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.delete_project(
        project_id="project_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove a project
```
# Remove a project returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
api_instance.delete_project("project_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove a project
```
// Remove a project returns "No Content" response

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
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.DeleteProject(ctx, "project_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.DeleteProject`: %v\n", err)
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

#####  Remove a project
```
// Remove a project returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    try {
      apiInstance.deleteProject("e555e290-ed65-49bd-ae18-8acbfcf18db7");
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#deleteProject");
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

#####  Remove a project
```
// Remove a project returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.delete_project("project_id".to_string()).await;
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

#####  Remove a project
```
/**
 * Remove a project returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiDeleteProjectRequest = {
  projectId: "project_id",
};

apiInstance
  .deleteProject(params)
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
## [Update case description](https://docs.datadoghq.com/api/latest/case-management/#update-case-description)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#update-case-description-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/descriptionhttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/descriptionhttps://api.datadoghq.eu/api/v2/cases/{case_id}/descriptionhttps://api.ddog-gov.com/api/v2/cases/{case_id}/descriptionhttps://api.datadoghq.com/api/v2/cases/{case_id}/descriptionhttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/descriptionhttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/description
### Overview
Update case description
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Case description update payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case update description
attributes [_required_]
object
Case update description attributes
description [_required_]
string
Case new description
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "description": "Seeing some weird memory increase... Updating the description"
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseDescription-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseDescription-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseDescription-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseDescription-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseDescription-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseDescription-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Update case description returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/description" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Seeing some weird memory increase... Updating the description"
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Update case description returns "OK" response
```
// Update case description returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseUpdateDescriptionRequest{
		Data: datadogV2.CaseUpdateDescription{
			Attributes: datadogV2.CaseUpdateDescriptionAttributes{
				Description: "Seeing some weird memory increase... Updating the description",
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UpdateCaseDescription(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdateCaseDescription`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UpdateCaseDescription`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update case description returns "OK" response
```
// Update case description returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.CaseUpdateDescription;
import com.datadog.api.client.v2.model.CaseUpdateDescriptionAttributes;
import com.datadog.api.client.v2.model.CaseUpdateDescriptionRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseUpdateDescriptionRequest body =
        new CaseUpdateDescriptionRequest()
            .data(
                new CaseUpdateDescription()
                    .attributes(
                        new CaseUpdateDescriptionAttributes()
                            .description(
                                "Seeing some weird memory increase... Updating the description"))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.updateCaseDescription(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updateCaseDescription");
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

#####  Update case description returns "OK" response
```
"""
Update case description returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_description import CaseUpdateDescription
from datadog_api_client.v2.model.case_update_description_attributes import CaseUpdateDescriptionAttributes
from datadog_api_client.v2.model.case_update_description_request import CaseUpdateDescriptionRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateDescriptionRequest(
    data=CaseUpdateDescription(
        attributes=CaseUpdateDescriptionAttributes(
            description="Seeing some weird memory increase... Updating the description",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_description(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update case description returns "OK" response
```
# Update case description returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseUpdateDescriptionRequest.new({
  data: DatadogAPIClient::V2::CaseUpdateDescription.new({
    attributes: DatadogAPIClient::V2::CaseUpdateDescriptionAttributes.new({
      description: "Seeing some weird memory increase... Updating the description",
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.update_case_description(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update case description returns "OK" response
```
// Update case description returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseResourceType;
use datadog_api_client::datadogV2::model::CaseUpdateDescription;
use datadog_api_client::datadogV2::model::CaseUpdateDescriptionAttributes;
use datadog_api_client::datadogV2::model::CaseUpdateDescriptionRequest;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseUpdateDescriptionRequest::new(CaseUpdateDescription::new(
        CaseUpdateDescriptionAttributes::new(
            "Seeing some weird memory increase... Updating the description".to_string(),
        ),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.update_case_description(case_id.clone(), body).await;
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

#####  Update case description returns "OK" response
```
/**
 * Update case description returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiUpdateCaseDescriptionRequest = {
  body: {
    data: {
      attributes: {
        description:
          "Seeing some weird memory increase... Updating the description",
      },
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .updateCaseDescription(params)
  .then((data: v2.CaseResponse) => {
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
## [Update case status](https://docs.datadoghq.com/api/latest/case-management/#update-case-status)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#update-case-status-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/statushttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/statushttps://api.datadoghq.eu/api/v2/cases/{case_id}/statushttps://api.ddog-gov.com/api/v2/cases/{case_id}/statushttps://api.datadoghq.com/api/v2/cases/{case_id}/statushttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/statushttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/status
### Overview
Update case status
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Case status update payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case update status
attributes [_required_]
object
Case update status attributes
status [_required_]
enum
Case status Allowed enum values: `OPEN,IN_PROGRESS,CLOSED`
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "status": "IN_PROGRESS"
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UpdateStatus-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UpdateStatus-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UpdateStatus-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UpdateStatus-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UpdateStatus-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UpdateStatus-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Update case status returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/status" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "status": "IN_PROGRESS"
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Update case status returns "OK" response
```
// Update case status returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseUpdateStatusRequest{
		Data: datadogV2.CaseUpdateStatus{
			Attributes: datadogV2.CaseUpdateStatusAttributes{
				Status: datadogV2.CASESTATUS_IN_PROGRESS,
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UpdateStatus(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdateStatus`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UpdateStatus`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update case status returns "OK" response
```
// Update case status returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.CaseStatus;
import com.datadog.api.client.v2.model.CaseUpdateStatus;
import com.datadog.api.client.v2.model.CaseUpdateStatusAttributes;
import com.datadog.api.client.v2.model.CaseUpdateStatusRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseUpdateStatusRequest body =
        new CaseUpdateStatusRequest()
            .data(
                new CaseUpdateStatus()
                    .attributes(new CaseUpdateStatusAttributes().status(CaseStatus.IN_PROGRESS))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.updateStatus(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updateStatus");
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

#####  Update case status returns "OK" response
```
"""
Update case status returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_status import CaseStatus
from datadog_api_client.v2.model.case_update_status import CaseUpdateStatus
from datadog_api_client.v2.model.case_update_status_attributes import CaseUpdateStatusAttributes
from datadog_api_client.v2.model.case_update_status_request import CaseUpdateStatusRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateStatusRequest(
    data=CaseUpdateStatus(
        attributes=CaseUpdateStatusAttributes(
            status=CaseStatus.IN_PROGRESS,
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_status(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update case status returns "OK" response
```
# Update case status returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseUpdateStatusRequest.new({
  data: DatadogAPIClient::V2::CaseUpdateStatus.new({
    attributes: DatadogAPIClient::V2::CaseUpdateStatusAttributes.new({
      status: DatadogAPIClient::V2::CaseStatus::IN_PROGRESS,
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.update_status(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update case status returns "OK" response
```
// Update case status returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseResourceType;
use datadog_api_client::datadogV2::model::CaseStatus;
use datadog_api_client::datadogV2::model::CaseUpdateStatus;
use datadog_api_client::datadogV2::model::CaseUpdateStatusAttributes;
use datadog_api_client::datadogV2::model::CaseUpdateStatusRequest;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseUpdateStatusRequest::new(CaseUpdateStatus::new(
        CaseUpdateStatusAttributes::new(CaseStatus::IN_PROGRESS),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.update_status(case_id.clone(), body).await;
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

#####  Update case status returns "OK" response
```
/**
 * Update case status returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiUpdateStatusRequest = {
  body: {
    data: {
      attributes: {
        status: "IN_PROGRESS",
      },
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .updateStatus(params)
  .then((data: v2.CaseResponse) => {
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
## [Update case title](https://docs.datadoghq.com/api/latest/case-management/#update-case-title)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#update-case-title-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/titlehttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/titlehttps://api.datadoghq.eu/api/v2/cases/{case_id}/titlehttps://api.ddog-gov.com/api/v2/cases/{case_id}/titlehttps://api.datadoghq.com/api/v2/cases/{case_id}/titlehttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/titlehttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/title
### Overview
Update case title
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Case title update payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case update title
attributes [_required_]
object
Case update title attributes
title [_required_]
string
Case new title
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "title": "[UPDATED] Memory leak investigation on API"
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseTitle-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseTitle-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseTitle-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseTitle-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseTitle-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseTitle-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Update case title returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/title" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "title": "[UPDATED] Memory leak investigation on API"
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Update case title returns "OK" response
```
// Update case title returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseUpdateTitleRequest{
		Data: datadogV2.CaseUpdateTitle{
			Attributes: datadogV2.CaseUpdateTitleAttributes{
				Title: "[UPDATED] Memory leak investigation on API",
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UpdateCaseTitle(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdateCaseTitle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UpdateCaseTitle`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update case title returns "OK" response
```
// Update case title returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.CaseUpdateTitle;
import com.datadog.api.client.v2.model.CaseUpdateTitleAttributes;
import com.datadog.api.client.v2.model.CaseUpdateTitleRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseUpdateTitleRequest body =
        new CaseUpdateTitleRequest()
            .data(
                new CaseUpdateTitle()
                    .attributes(
                        new CaseUpdateTitleAttributes()
                            .title("[UPDATED] Memory leak investigation on API"))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.updateCaseTitle(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updateCaseTitle");
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

#####  Update case title returns "OK" response
```
"""
Update case title returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_title import CaseUpdateTitle
from datadog_api_client.v2.model.case_update_title_attributes import CaseUpdateTitleAttributes
from datadog_api_client.v2.model.case_update_title_request import CaseUpdateTitleRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateTitleRequest(
    data=CaseUpdateTitle(
        attributes=CaseUpdateTitleAttributes(
            title="[UPDATED] Memory leak investigation on API",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_title(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update case title returns "OK" response
```
# Update case title returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseUpdateTitleRequest.new({
  data: DatadogAPIClient::V2::CaseUpdateTitle.new({
    attributes: DatadogAPIClient::V2::CaseUpdateTitleAttributes.new({
      title: "[UPDATED] Memory leak investigation on API",
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.update_case_title(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update case title returns "OK" response
```
// Update case title returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseResourceType;
use datadog_api_client::datadogV2::model::CaseUpdateTitle;
use datadog_api_client::datadogV2::model::CaseUpdateTitleAttributes;
use datadog_api_client::datadogV2::model::CaseUpdateTitleRequest;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseUpdateTitleRequest::new(CaseUpdateTitle::new(
        CaseUpdateTitleAttributes::new("[UPDATED] Memory leak investigation on API".to_string()),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.update_case_title(case_id.clone(), body).await;
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

#####  Update case title returns "OK" response
```
/**
 * Update case title returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiUpdateCaseTitleRequest = {
  body: {
    data: {
      attributes: {
        title: "[UPDATED] Memory leak investigation on API",
      },
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .updateCaseTitle(params)
  .then((data: v2.CaseResponse) => {
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
## [Update case priority](https://docs.datadoghq.com/api/latest/case-management/#update-case-priority)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#update-case-priority-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/priorityhttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/priorityhttps://api.datadoghq.eu/api/v2/cases/{case_id}/priorityhttps://api.ddog-gov.com/api/v2/cases/{case_id}/priorityhttps://api.datadoghq.com/api/v2/cases/{case_id}/priorityhttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/priorityhttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/priority
### Overview
Update case priority
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Case priority update payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case priority status
attributes [_required_]
object
Case update priority attributes
priority [_required_]
enum
Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`
default: `NOT_DEFINED`
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "priority": "P3"
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UpdatePriority-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UpdatePriority-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UpdatePriority-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UpdatePriority-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UpdatePriority-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UpdatePriority-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Update case priority returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/priority" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "priority": "P3"
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Update case priority returns "OK" response
```
// Update case priority returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseUpdatePriorityRequest{
		Data: datadogV2.CaseUpdatePriority{
			Attributes: datadogV2.CaseUpdatePriorityAttributes{
				Priority: datadogV2.CASEPRIORITY_P3,
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UpdatePriority(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdatePriority`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UpdatePriority`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update case priority returns "OK" response
```
// Update case priority returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CasePriority;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.CaseUpdatePriority;
import com.datadog.api.client.v2.model.CaseUpdatePriorityAttributes;
import com.datadog.api.client.v2.model.CaseUpdatePriorityRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseUpdatePriorityRequest body =
        new CaseUpdatePriorityRequest()
            .data(
                new CaseUpdatePriority()
                    .attributes(new CaseUpdatePriorityAttributes().priority(CasePriority.P3))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.updatePriority(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updatePriority");
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

#####  Update case priority returns "OK" response
```
"""
Update case priority returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_priority import CasePriority
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_priority import CaseUpdatePriority
from datadog_api_client.v2.model.case_update_priority_attributes import CaseUpdatePriorityAttributes
from datadog_api_client.v2.model.case_update_priority_request import CaseUpdatePriorityRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdatePriorityRequest(
    data=CaseUpdatePriority(
        attributes=CaseUpdatePriorityAttributes(
            priority=CasePriority.P3,
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_priority(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update case priority returns "OK" response
```
# Update case priority returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseUpdatePriorityRequest.new({
  data: DatadogAPIClient::V2::CaseUpdatePriority.new({
    attributes: DatadogAPIClient::V2::CaseUpdatePriorityAttributes.new({
      priority: DatadogAPIClient::V2::CasePriority::P3,
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.update_priority(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update case priority returns "OK" response
```
// Update case priority returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CasePriority;
use datadog_api_client::datadogV2::model::CaseResourceType;
use datadog_api_client::datadogV2::model::CaseUpdatePriority;
use datadog_api_client::datadogV2::model::CaseUpdatePriorityAttributes;
use datadog_api_client::datadogV2::model::CaseUpdatePriorityRequest;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseUpdatePriorityRequest::new(CaseUpdatePriority::new(
        CaseUpdatePriorityAttributes::new(CasePriority::P3),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.update_priority(case_id.clone(), body).await;
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

#####  Update case priority returns "OK" response
```
/**
 * Update case priority returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiUpdatePriorityRequest = {
  body: {
    data: {
      attributes: {
        priority: "P3",
      },
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .updatePriority(params)
  .then((data: v2.CaseResponse) => {
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
## [Assign case](https://docs.datadoghq.com/api/latest/case-management/#assign-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#assign-case-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/assignhttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/assignhttps://api.datadoghq.eu/api/v2/cases/{case_id}/assignhttps://api.ddog-gov.com/api/v2/cases/{case_id}/assignhttps://api.datadoghq.com/api/v2/cases/{case_id}/assignhttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/assignhttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/assign
### Overview
Assign case to a user
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Assign case payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case assign
attributes [_required_]
object
Case assign attributes
assignee_id [_required_]
string
Assignee's UUID
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "assignee_id": "string"
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#AssignCase-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#AssignCase-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#AssignCase-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#AssignCase-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#AssignCase-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#AssignCase-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Assign case returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/assign" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "assignee_id": "string"
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Assign case returns "OK" response
```
// Assign case returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	body := datadogV2.CaseAssignRequest{
		Data: datadogV2.CaseAssign{
			Attributes: datadogV2.CaseAssignAttributes{
				AssigneeId: UserDataID,
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.AssignCase(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.AssignCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.AssignCase`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Assign case returns "OK" response
```
// Assign case returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseAssign;
import com.datadog.api.client.v2.model.CaseAssignAttributes;
import com.datadog.api.client.v2.model.CaseAssignRequest;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    CaseAssignRequest body =
        new CaseAssignRequest()
            .data(
                new CaseAssign()
                    .attributes(new CaseAssignAttributes().assigneeId(USER_DATA_ID))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.assignCase(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#assignCase");
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

#####  Assign case returns "OK" response
```
"""
Assign case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_assign import CaseAssign
from datadog_api_client.v2.model.case_assign_attributes import CaseAssignAttributes
from datadog_api_client.v2.model.case_assign_request import CaseAssignRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = CaseAssignRequest(
    data=CaseAssign(
        attributes=CaseAssignAttributes(
            assignee_id=USER_DATA_ID,
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.assign_case(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Assign case returns "OK" response
```
# Assign case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::CaseAssignRequest.new({
  data: DatadogAPIClient::V2::CaseAssign.new({
    attributes: DatadogAPIClient::V2::CaseAssignAttributes.new({
      assignee_id: USER_DATA_ID,
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.assign_case(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Assign case returns "OK" response
```
// Assign case returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseAssign;
use datadog_api_client::datadogV2::model::CaseAssignAttributes;
use datadog_api_client::datadogV2::model::CaseAssignRequest;
use datadog_api_client::datadogV2::model::CaseResourceType;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();

    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = CaseAssignRequest::new(CaseAssign::new(
        CaseAssignAttributes::new(user_data_id.clone()),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.assign_case(case_id.clone(), body).await;
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

#####  Assign case returns "OK" response
```
/**
 * Assign case returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.CaseManagementApiAssignCaseRequest = {
  body: {
    data: {
      attributes: {
        assigneeId: USER_DATA_ID,
      },
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .assignCase(params)
  .then((data: v2.CaseResponse) => {
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
## [Unassign case](https://docs.datadoghq.com/api/latest/case-management/#unassign-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#unassign-case-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/unassignhttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/unassignhttps://api.datadoghq.eu/api/v2/cases/{case_id}/unassignhttps://api.ddog-gov.com/api/v2/cases/{case_id}/unassignhttps://api.datadoghq.com/api/v2/cases/{case_id}/unassignhttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/unassignhttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/unassign
### Overview
Unassign case
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Unassign case payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case empty request data
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UnassignCase-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UnassignCase-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UnassignCase-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UnassignCase-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UnassignCase-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UnassignCase-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Unassign case returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/unassign" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "case"
  }
}
EOF  

                        
```

#####  Unassign case returns "OK" response
```
// Unassign case returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseEmptyRequest{
		Data: datadogV2.CaseEmpty{
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UnassignCase(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UnassignCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UnassignCase`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Unassign case returns "OK" response
```
// Unassign case returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseEmpty;
import com.datadog.api.client.v2.model.CaseEmptyRequest;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseEmptyRequest body =
        new CaseEmptyRequest().data(new CaseEmpty().type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.unassignCase(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#unassignCase");
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

#####  Unassign case returns "OK" response
```
"""
Unassign case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_empty import CaseEmpty
from datadog_api_client.v2.model.case_empty_request import CaseEmptyRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseEmptyRequest(
    data=CaseEmpty(
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.unassign_case(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Unassign case returns "OK" response
```
# Unassign case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseEmptyRequest.new({
  data: DatadogAPIClient::V2::CaseEmpty.new({
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.unassign_case(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Unassign case returns "OK" response
```
// Unassign case returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseEmpty;
use datadog_api_client::datadogV2::model::CaseEmptyRequest;
use datadog_api_client::datadogV2::model::CaseResourceType;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseEmptyRequest::new(CaseEmpty::new(CaseResourceType::CASE));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.unassign_case(case_id.clone(), body).await;
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

#####  Unassign case returns "OK" response
```
/**
 * Unassign case returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiUnassignCaseRequest = {
  body: {
    data: {
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .unassignCase(params)
  .then((data: v2.CaseResponse) => {
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
## [Archive case](https://docs.datadoghq.com/api/latest/case-management/#archive-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#archive-case-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/archivehttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/archivehttps://api.datadoghq.eu/api/v2/cases/{case_id}/archivehttps://api.ddog-gov.com/api/v2/cases/{case_id}/archivehttps://api.datadoghq.com/api/v2/cases/{case_id}/archivehttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/archivehttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/archive
### Overview
Archive case
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Archive case payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case empty request data
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#ArchiveCase-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#ArchiveCase-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#ArchiveCase-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#ArchiveCase-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#ArchiveCase-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#ArchiveCase-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Archive case returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/archive" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "case"
  }
}
EOF  

                        
```

#####  Archive case returns "OK" response
```
// Archive case returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseEmptyRequest{
		Data: datadogV2.CaseEmpty{
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.ArchiveCase(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.ArchiveCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.ArchiveCase`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Archive case returns "OK" response
```
// Archive case returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseEmpty;
import com.datadog.api.client.v2.model.CaseEmptyRequest;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseEmptyRequest body =
        new CaseEmptyRequest().data(new CaseEmpty().type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.archiveCase(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#archiveCase");
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

#####  Archive case returns "OK" response
```
"""
Archive case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_empty import CaseEmpty
from datadog_api_client.v2.model.case_empty_request import CaseEmptyRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseEmptyRequest(
    data=CaseEmpty(
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.archive_case(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Archive case returns "OK" response
```
# Archive case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseEmptyRequest.new({
  data: DatadogAPIClient::V2::CaseEmpty.new({
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.archive_case(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Archive case returns "OK" response
```
// Archive case returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseEmpty;
use datadog_api_client::datadogV2::model::CaseEmptyRequest;
use datadog_api_client::datadogV2::model::CaseResourceType;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseEmptyRequest::new(CaseEmpty::new(CaseResourceType::CASE));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.archive_case(case_id.clone(), body).await;
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

#####  Archive case returns "OK" response
```
/**
 * Archive case returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiArchiveCaseRequest = {
  body: {
    data: {
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .archiveCase(params)
  .then((data: v2.CaseResponse) => {
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
## [Unarchive case](https://docs.datadoghq.com/api/latest/case-management/#unarchive-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#unarchive-case-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/unarchivehttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/unarchivehttps://api.datadoghq.eu/api/v2/cases/{case_id}/unarchivehttps://api.ddog-gov.com/api/v2/cases/{case_id}/unarchivehttps://api.datadoghq.com/api/v2/cases/{case_id}/unarchivehttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/unarchivehttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/unarchive
### Overview
Unarchive case
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Unarchive case payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case empty request data
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UnarchiveCase-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UnarchiveCase-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UnarchiveCase-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UnarchiveCase-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UnarchiveCase-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UnarchiveCase-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Unarchive case returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/unarchive" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "case"
  }
}
EOF  

                        
```

#####  Unarchive case returns "OK" response
```
// Unarchive case returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseEmptyRequest{
		Data: datadogV2.CaseEmpty{
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UnarchiveCase(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UnarchiveCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UnarchiveCase`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Unarchive case returns "OK" response
```
// Unarchive case returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseEmpty;
import com.datadog.api.client.v2.model.CaseEmptyRequest;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseEmptyRequest body =
        new CaseEmptyRequest().data(new CaseEmpty().type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.unarchiveCase(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#unarchiveCase");
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

#####  Unarchive case returns "OK" response
```
"""
Unarchive case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_empty import CaseEmpty
from datadog_api_client.v2.model.case_empty_request import CaseEmptyRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseEmptyRequest(
    data=CaseEmpty(
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.unarchive_case(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Unarchive case returns "OK" response
```
# Unarchive case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseEmptyRequest.new({
  data: DatadogAPIClient::V2::CaseEmpty.new({
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.unarchive_case(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Unarchive case returns "OK" response
```
// Unarchive case returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseEmpty;
use datadog_api_client::datadogV2::model::CaseEmptyRequest;
use datadog_api_client::datadogV2::model::CaseResourceType;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseEmptyRequest::new(CaseEmpty::new(CaseResourceType::CASE));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.unarchive_case(case_id.clone(), body).await;
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

#####  Unarchive case returns "OK" response
```
/**
 * Unarchive case returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiUnarchiveCaseRequest = {
  body: {
    data: {
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .unarchiveCase(params)
  .then((data: v2.CaseResponse) => {
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
## [Update case attributes](https://docs.datadoghq.com/api/latest/case-management/#update-case-attributes)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#update-case-attributes-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/attributeshttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/attributeshttps://api.datadoghq.eu/api/v2/cases/{case_id}/attributeshttps://api.ddog-gov.com/api/v2/cases/{case_id}/attributeshttps://api.datadoghq.com/api/v2/cases/{case_id}/attributeshttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/attributeshttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/attributes
### Overview
Update case attributes
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Case attributes update payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case update attributes
attributes [_required_]
object
Case update attributes attributes
attributes [_required_]
object
The definition of `CaseObjectAttributes` object.
<any-key>
[string]
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "attributes": {
        "env": [
          "test"
        ],
        "service": [
          "web-store",
          "web-api"
        ],
        "team": [
          "engineer"
        ]
      }
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UpdateAttributes-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UpdateAttributes-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UpdateAttributes-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UpdateAttributes-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UpdateAttributes-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UpdateAttributes-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Update case attributes returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/attributes" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "attributes": {
        "env": [
          "test"
        ],
        "service": [
          "web-store",
          "web-api"
        ],
        "team": [
          "engineer"
        ]
      }
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Update case attributes returns "OK" response
```
// Update case attributes returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseUpdateAttributesRequest{
		Data: datadogV2.CaseUpdateAttributes{
			Attributes: datadogV2.CaseUpdateAttributesAttributes{
				Attributes: map[string][]string{
					"env": []string{
						"test",
					},
					"service": []string{
						"web-store",
						"web-api",
					},
					"team": []string{
						"engineer",
					},
				},
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UpdateAttributes(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdateAttributes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UpdateAttributes`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update case attributes returns "OK" response
```
// Update case attributes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.CaseUpdateAttributes;
import com.datadog.api.client.v2.model.CaseUpdateAttributesAttributes;
import com.datadog.api.client.v2.model.CaseUpdateAttributesRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseUpdateAttributesRequest body =
        new CaseUpdateAttributesRequest()
            .data(
                new CaseUpdateAttributes()
                    .attributes(
                        new CaseUpdateAttributesAttributes()
                            .attributes(
                                Map.ofEntries(
                                    Map.entry("env", Collections.singletonList("test")),
                                    Map.entry("service", Arrays.asList("web-store", "web-api")),
                                    Map.entry("team", Collections.singletonList("engineer")))))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result = apiInstance.updateAttributes(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updateAttributes");
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

#####  Update case attributes returns "OK" response
```
"""
Update case attributes returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_object_attributes import CaseObjectAttributes
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_attributes import CaseUpdateAttributes
from datadog_api_client.v2.model.case_update_attributes_attributes import CaseUpdateAttributesAttributes
from datadog_api_client.v2.model.case_update_attributes_request import CaseUpdateAttributesRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateAttributesRequest(
    data=CaseUpdateAttributes(
        attributes=CaseUpdateAttributesAttributes(
            attributes=CaseObjectAttributes(
                env=[
                    "test",
                ],
                service=[
                    "web-store",
                    "web-api",
                ],
                team=[
                    "engineer",
                ],
            ),
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_attributes(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update case attributes returns "OK" response
```
# Update case attributes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseUpdateAttributesRequest.new({
  data: DatadogAPIClient::V2::CaseUpdateAttributes.new({
    attributes: DatadogAPIClient::V2::CaseUpdateAttributesAttributes.new({
      attributes: {
        env: [
          "test",
        ], service: [
          "web-store",
          "web-api",
        ], team: [
          "engineer",
        ],
      },
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.update_attributes(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update case attributes returns "OK" response
```
// Update case attributes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseResourceType;
use datadog_api_client::datadogV2::model::CaseUpdateAttributes;
use datadog_api_client::datadogV2::model::CaseUpdateAttributesAttributes;
use datadog_api_client::datadogV2::model::CaseUpdateAttributesRequest;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseUpdateAttributesRequest::new(CaseUpdateAttributes::new(
        CaseUpdateAttributesAttributes::new(BTreeMap::from([
            ("env".to_string(), vec!["test".to_string()]),
            (
                "service".to_string(),
                vec!["web-store".to_string(), "web-api".to_string()],
            ),
            ("team".to_string(), vec!["engineer".to_string()]),
        ])),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.update_attributes(case_id.clone(), body).await;
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

#####  Update case attributes returns "OK" response
```
/**
 * Update case attributes returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiUpdateAttributesRequest = {
  body: {
    data: {
      attributes: {
        attributes: {
          env: ["test"],
          service: ["web-store", "web-api"],
          team: ["engineer"],
        },
      },
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .updateAttributes(params)
  .then((data: v2.CaseResponse) => {
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
## [Comment case](https://docs.datadoghq.com/api/latest/case-management/#comment-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#comment-case-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/commenthttps://api.ap2.datadoghq.com/api/v2/cases/{case_id}/commenthttps://api.datadoghq.eu/api/v2/cases/{case_id}/commenthttps://api.ddog-gov.com/api/v2/cases/{case_id}/commenthttps://api.datadoghq.com/api/v2/cases/{case_id}/commenthttps://api.us3.datadoghq.com/api/v2/cases/{case_id}/commenthttps://api.us5.datadoghq.com/api/v2/cases/{case_id}/comment
### Overview
Comment case
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
### Request
#### Body Data (required)
Case comment payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case comment
attributes [_required_]
object
Case comment attributes
comment [_required_]
string
The `CaseCommentAttributes` `message`.
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "comment": "Hello World !"
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#CommentCase-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#CommentCase-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#CommentCase-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#CommentCase-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#CommentCase-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#CommentCase-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Timeline response
Field
Type
Description
data
[object]
The `TimelineResponse` `data`.
attributes [_required_]
object
timeline cell
author
<oneOf>
author of the timeline cell
Option 1
object
timeline cell user author
content
object
user author content.
email
string
user email
handle
string
user handle
id
string
user UUID
name
string
user name
type
enum
user author type. Allowed enum values: `USER`
cell_content
<oneOf>
timeline cell content
Option 1
object
comment content
message
string
comment message
created_at
date-time
Timestamp of when the cell was created
deleted_at
date-time
Timestamp of when the cell was deleted
modified_at
date-time
Timestamp of when the cell was last modified
type
enum
Timeline cell content type Allowed enum values: `COMMENT`
id [_required_]
string
Timeline cell's identifier
type [_required_]
enum
Timeline cell JSON:API resource type Allowed enum values: `timeline_cell`
default: `timeline_cell`
```
{
  "data": [
    {
      "attributes": {
        "author": {
          "content": {
            "email": "string",
            "handle": "string",
            "id": "string",
            "name": "string"
          },
          "type": "USER"
        },
        "cell_content": {
          "message": "string"
        },
        "created_at": "2019-09-19T10:00:00.000Z",
        "deleted_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "type": "COMMENT"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "timeline_cell"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Comment case returns "OK" response
Copy
```
                          # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/comment" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "comment": "Hello World !"
    },
    "type": "case"
  }
}
EOF  

                        
```

#####  Comment case returns "OK" response
```
// Comment case returns "OK" response

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
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	body := datadogV2.CaseCommentRequest{
		Data: datadogV2.CaseComment{
			Attributes: datadogV2.CaseCommentAttributes{
				Comment: "Hello World !",
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.CommentCase(ctx, CaseID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.CommentCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.CommentCase`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Comment case returns "OK" response
```
// Comment case returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseComment;
import com.datadog.api.client.v2.model.CaseCommentAttributes;
import com.datadog.api.client.v2.model.CaseCommentRequest;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.TimelineResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    CaseCommentRequest body =
        new CaseCommentRequest()
            .data(
                new CaseComment()
                    .attributes(new CaseCommentAttributes().comment("Hello World !"))
                    .type(CaseResourceType.CASE));

    try {
      TimelineResponse result = apiInstance.commentCase(CASE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#commentCase");
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

#####  Comment case returns "OK" response
```
"""
Comment case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_comment import CaseComment
from datadog_api_client.v2.model.case_comment_attributes import CaseCommentAttributes
from datadog_api_client.v2.model.case_comment_request import CaseCommentRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseCommentRequest(
    data=CaseComment(
        attributes=CaseCommentAttributes(
            comment="Hello World !",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.comment_case(case_id=CASE_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Comment case returns "OK" response
```
# Comment case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

body = DatadogAPIClient::V2::CaseCommentRequest.new({
  data: DatadogAPIClient::V2::CaseComment.new({
    attributes: DatadogAPIClient::V2::CaseCommentAttributes.new({
      comment: "Hello World !",
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.comment_case(CASE_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Comment case returns "OK" response
```
// Comment case returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseComment;
use datadog_api_client::datadogV2::model::CaseCommentAttributes;
use datadog_api_client::datadogV2::model::CaseCommentRequest;
use datadog_api_client::datadogV2::model::CaseResourceType;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();
    let body = CaseCommentRequest::new(CaseComment::new(
        CaseCommentAttributes::new("Hello World !".to_string()),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.comment_case(case_id.clone(), body).await;
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

#####  Comment case returns "OK" response
```
/**
 * Comment case returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

const params: v2.CaseManagementApiCommentCaseRequest = {
  body: {
    data: {
      attributes: {
        comment: "Hello World !",
      },
      type: "case",
    },
  },
  caseId: CASE_ID,
};

apiInstance
  .commentCase(params)
  .then((data: v2.TimelineResponse) => {
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
## [Delete case comment](https://docs.datadoghq.com/api/latest/case-management/#delete-case-comment)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#delete-case-comment-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id}https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id}https://api.datadoghq.eu/api/v2/cases/{case_id}/comment/{cell_id}https://api.ddog-gov.com/api/v2/cases/{case_id}/comment/{cell_id}https://api.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id}https://api.us3.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id}https://api.us5.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id}
### Overview
Delete case comment
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
cell_id [_required_]
string
Timeline cell’s UUID
### Response
  * [204](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseComment-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseComment-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseComment-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseComment-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseComment-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseComment-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Delete case comment
Copy
```
                  # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
export cell_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/comment/${cell_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete case comment
```
"""
Delete case comment returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

# there is a valid "comment" in the system
COMMENT_ID = environ["COMMENT_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.delete_case_comment(
        case_id=CASE_ID,
        cell_id=COMMENT_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete case comment
```
# Delete case comment returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

# there is a valid "comment" in the system
COMMENT_ID = ENV["COMMENT_ID"]
api_instance.delete_case_comment(CASE_ID, COMMENT_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete case comment
```
// Delete case comment returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "case" in the system
	CaseID := os.Getenv("CASE_ID")

	// there is a valid "comment" in the system
	CommentID := os.Getenv("COMMENT_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.DeleteCaseComment(ctx, CaseID, CommentID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.DeleteCaseComment`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete case comment
```
// Delete case comment returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" in the system
    String CASE_ID = System.getenv("CASE_ID");

    // there is a valid "comment" in the system
    String COMMENT_ID = System.getenv("COMMENT_ID");

    try {
      apiInstance.deleteCaseComment(CASE_ID, COMMENT_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#deleteCaseComment");
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

#####  Delete case comment
```
// Delete case comment returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "case" in the system
    let case_id = std::env::var("CASE_ID").unwrap();

    // there is a valid "comment" in the system
    let comment_id = std::env::var("COMMENT_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .delete_case_comment(case_id.clone(), comment_id.clone())
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

#####  Delete case comment
```
/**
 * Delete case comment returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" in the system
const CASE_ID = process.env.CASE_ID as string;

// there is a valid "comment" in the system
const COMMENT_ID = process.env.COMMENT_ID as string;

const params: v2.CaseManagementApiDeleteCaseCommentRequest = {
  caseId: CASE_ID,
  cellId: COMMENT_ID,
};

apiInstance
  .deleteCaseComment(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update case custom attribute](https://docs.datadoghq.com/api/latest/case-management/#update-case-custom-attribute)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#update-case-custom-attribute-v2)


POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.datadoghq.eu/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.ddog-gov.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.us3.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.us5.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}
### Overview
Update case custom attribute
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
custom_attribute_key [_required_]
string
Case Custom attribute’s key
### Request
#### Body Data (required)
Update case custom attribute payload
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Field
Type
Description
data [_required_]
object
Case update custom attribute
attributes [_required_]
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
type [_required_]
enum
Case resource type Allowed enum values: `case`
default: `case`
```
{
  "data": {
    "attributes": {
      "is_multi": false,
      "type": "NUMBER",
      "value": {
        "description": "",
        "type": ""
      }
    },
    "type": "case"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseCustomAttribute-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseCustomAttribute-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseCustomAttribute-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseCustomAttribute-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseCustomAttribute-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#UpdateCaseCustomAttribute-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Update case custom attribute
Copy
```
                  # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
export custom_attribute_key="aws_region"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/custom_attributes/${custom_attribute_key}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "is_multi": false,
      "type": "NUMBER",
      "value": {}
    },
    "type": "case"
  }
}
EOF  

                
```

#####  Update case custom attribute
```
"""
Update case custom attribute returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_custom_attribute import CaseUpdateCustomAttribute
from datadog_api_client.v2.model.case_update_custom_attribute_request import CaseUpdateCustomAttributeRequest
from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType
from datadog_api_client.v2.model.custom_attribute_value import CustomAttributeValue

# there is a valid "case" with a custom "case_type" in the system
CASE_WITH_TYPE_ID = environ["CASE_WITH_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = environ["CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY"]

body = CaseUpdateCustomAttributeRequest(
    data=CaseUpdateCustomAttribute(
        attributes=CustomAttributeValue(
            type=CustomAttributeType.TEXT,
            is_multi=True,
            value=["Abba", "The Cure"],
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_custom_attribute(
        case_id=CASE_WITH_TYPE_ID, custom_attribute_key=CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY, body=body
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update case custom attribute
```
# Update case custom attribute returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" with a custom "case_type" in the system
CASE_WITH_TYPE_ID = ENV["CASE_WITH_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = ENV["CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY"]

body = DatadogAPIClient::V2::CaseUpdateCustomAttributeRequest.new({
  data: DatadogAPIClient::V2::CaseUpdateCustomAttribute.new({
    attributes: DatadogAPIClient::V2::CustomAttributeValue.new({
      type: DatadogAPIClient::V2::CustomAttributeType::TEXT,
      is_multi: true,
      value: [
        "Abba",
        "The Cure",
      ],
    }),
    type: DatadogAPIClient::V2::CaseResourceType::CASE,
  }),
})
p api_instance.update_case_custom_attribute(CASE_WITH_TYPE_ID, CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update case custom attribute
```
// Update case custom attribute returns "OK" response

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
	// there is a valid "case" with a custom "case_type" in the system
	CaseWithTypeID := os.Getenv("CASE_WITH_TYPE_ID")

	// there is a valid "custom_attribute" in the system
	CustomAttributeAttributesKey := os.Getenv("CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY")

	body := datadogV2.CaseUpdateCustomAttributeRequest{
		Data: datadogV2.CaseUpdateCustomAttribute{
			Attributes: datadogV2.CustomAttributeValue{
				Type:    datadogV2.CUSTOMATTRIBUTETYPE_TEXT,
				IsMulti: true,
				Value: datadogV2.CustomAttributeValuesUnion{
					CustomAttributeMultiStringValue: &[]string{
						"Abba",
						"The Cure",
					}},
			},
			Type: datadogV2.CASERESOURCETYPE_CASE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UpdateCaseCustomAttribute(ctx, CaseWithTypeID, CustomAttributeAttributesKey, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdateCaseCustomAttribute`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UpdateCaseCustomAttribute`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update case custom attribute
```
// Update case custom attribute returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResourceType;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.CaseUpdateCustomAttribute;
import com.datadog.api.client.v2.model.CaseUpdateCustomAttributeRequest;
import com.datadog.api.client.v2.model.CustomAttributeType;
import com.datadog.api.client.v2.model.CustomAttributeValue;
import com.datadog.api.client.v2.model.CustomAttributeValuesUnion;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" with a custom "case_type" in the system
    String CASE_WITH_TYPE_ID = System.getenv("CASE_WITH_TYPE_ID");

    // there is a valid "custom_attribute" in the system
    String CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = System.getenv("CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY");

    CaseUpdateCustomAttributeRequest body =
        new CaseUpdateCustomAttributeRequest()
            .data(
                new CaseUpdateCustomAttribute()
                    .attributes(
                        new CustomAttributeValue()
                            .type(CustomAttributeType.TEXT)
                            .isMulti(true)
                            .value(
                                CustomAttributeValuesUnion.fromStringList(
                                    Arrays.asList("Abba", "The Cure"))))
                    .type(CaseResourceType.CASE));

    try {
      CaseResponse result =
          apiInstance.updateCaseCustomAttribute(
              CASE_WITH_TYPE_ID, CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updateCaseCustomAttribute");
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

#####  Update case custom attribute
```
// Update case custom attribute returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseResourceType;
use datadog_api_client::datadogV2::model::CaseUpdateCustomAttribute;
use datadog_api_client::datadogV2::model::CaseUpdateCustomAttributeRequest;
use datadog_api_client::datadogV2::model::CustomAttributeType;
use datadog_api_client::datadogV2::model::CustomAttributeValue;
use datadog_api_client::datadogV2::model::CustomAttributeValuesUnion;

#[tokio::main]
async fn main() {
    // there is a valid "case" with a custom "case_type" in the system
    let case_with_type_id = std::env::var("CASE_WITH_TYPE_ID").unwrap();

    // there is a valid "custom_attribute" in the system
    let custom_attribute_attributes_key = std::env::var("CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY").unwrap();
    let body = CaseUpdateCustomAttributeRequest::new(CaseUpdateCustomAttribute::new(
        CustomAttributeValue::new(
            true,
            CustomAttributeType::TEXT,
            CustomAttributeValuesUnion::CustomAttributeMultiStringValue(vec![
                "Abba".to_string(),
                "The Cure".to_string(),
            ]),
        ),
        CaseResourceType::CASE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .update_case_custom_attribute(
            case_with_type_id.clone(),
            custom_attribute_attributes_key.clone(),
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update case custom attribute
```
/**
 * Update case custom attribute returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" with a custom "case_type" in the system
const CASE_WITH_TYPE_ID = process.env.CASE_WITH_TYPE_ID as string;

// there is a valid "custom_attribute" in the system
const CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = process.env
  .CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY as string;

const params: v2.CaseManagementApiUpdateCaseCustomAttributeRequest = {
  body: {
    data: {
      attributes: {
        type: "TEXT",
        isMulti: true,
        value: ["Abba", "The Cure"],
      },
      type: "case",
    },
  },
  caseId: CASE_WITH_TYPE_ID,
  customAttributeKey: CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY,
};

apiInstance
  .updateCaseCustomAttribute(params)
  .then((data: v2.CaseResponse) => {
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
## [Delete custom attribute from case](https://docs.datadoghq.com/api/latest/case-management/#delete-custom-attribute-from-case)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/case-management/#delete-custom-attribute-from-case-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.datadoghq.eu/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.ddog-gov.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.us3.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}https://api.us5.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}
### Overview
Delete custom attribute from case
OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
case_id [_required_]
string
Case’s UUID or key
custom_attribute_key [_required_]
string
Case Custom attribute’s key
### Response
  * [200](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseCustomAttribute-200-v2)
  * [401](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseCustomAttribute-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseCustomAttribute-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseCustomAttribute-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/case-management/#DeleteCaseCustomAttribute-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


Case response
Field
Type
Description
data
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
```
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_attributes": {
        "<any-key>": {
          "is_multi": false,
          "type": "NUMBER",
          "value": {
            "description": "",
            "type": ""
          }
        }
      },
      "description": "string",
      "jira_issue": {
        "result": {
          "issue_id": "string",
          "issue_key": "string",
          "issue_url": "string",
          "project_key": "string"
        },
        "status": "COMPLETED"
      },
      "key": "CASEM-4523",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "priority": "NOT_DEFINED",
      "service_now_ticket": {
        "result": {
          "sys_target_link": "string"
        },
        "status": "COMPLETED"
      },
      "status": "OPEN",
      "title": "Memory leak investigation on API",
      "type": "STANDARD",
      "type_id": "3b010bde-09ce-4449-b745-71dd5f861963"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
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
}
```

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/case-management/)
  * [Example](https://docs.datadoghq.com/api/latest/case-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/case-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/case-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/case-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/case-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/case-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/case-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/case-management/?code-lang=typescript)


#####  Delete custom attribute from case
Copy
```
                  # Path parameters  
export case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"  
export custom_attribute_key="aws_region"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/custom_attributes/${custom_attribute_key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete custom attribute from case
```
"""
Delete custom attribute from case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

# there is a valid "case" with a custom "case_type" in the system
CASE_WITH_TYPE_ID = environ["CASE_WITH_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = environ["CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.delete_case_custom_attribute(
        case_id=CASE_WITH_TYPE_ID,
        custom_attribute_key=CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete custom attribute from case
```
# Delete custom attribute from case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" with a custom "case_type" in the system
CASE_WITH_TYPE_ID = ENV["CASE_WITH_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = ENV["CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY"]
p api_instance.delete_case_custom_attribute(CASE_WITH_TYPE_ID, CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete custom attribute from case
```
// Delete custom attribute from case returns "OK" response

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
	// there is a valid "case" with a custom "case_type" in the system
	CaseWithTypeID := os.Getenv("CASE_WITH_TYPE_ID")

	// there is a valid "custom_attribute" in the system
	CustomAttributeAttributesKey := os.Getenv("CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.DeleteCaseCustomAttribute(ctx, CaseWithTypeID, CustomAttributeAttributesKey)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.DeleteCaseCustomAttribute`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.DeleteCaseCustomAttribute`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete custom attribute from case
```
// Delete custom attribute from case returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    // there is a valid "case" with a custom "case_type" in the system
    String CASE_WITH_TYPE_ID = System.getenv("CASE_WITH_TYPE_ID");

    // there is a valid "custom_attribute" in the system
    String CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = System.getenv("CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY");

    try {
      CaseResponse result =
          apiInstance.deleteCaseCustomAttribute(CASE_WITH_TYPE_ID, CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#deleteCaseCustomAttribute");
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

#####  Delete custom attribute from case
```
// Delete custom attribute from case returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "case" with a custom "case_type" in the system
    let case_with_type_id = std::env::var("CASE_WITH_TYPE_ID").unwrap();

    // there is a valid "custom_attribute" in the system
    let custom_attribute_attributes_key = std::env::var("CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .delete_case_custom_attribute(
            case_with_type_id.clone(),
            custom_attribute_attributes_key.clone(),
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

#####  Delete custom attribute from case
```
/**
 * Delete custom attribute from case returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

// there is a valid "case" with a custom "case_type" in the system
const CASE_WITH_TYPE_ID = process.env.CASE_WITH_TYPE_ID as string;

// there is a valid "custom_attribute" in the system
const CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = process.env
  .CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY as string;

const params: v2.CaseManagementApiDeleteCaseCustomAttributeRequest = {
  caseId: CASE_WITH_TYPE_ID,
  customAttributeKey: CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY,
};

apiInstance
  .deleteCaseCustomAttribute(params)
  .then((data: v2.CaseResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6896163f-0a28-4f35-b5fc-c5c3a84c6bd8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=5779c400-02c9-45c2-b548-9822fa5414d0&pt=Case%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6896163f-0a28-4f35-b5fc-c5c3a84c6bd8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=5779c400-02c9-45c2-b548-9822fa5414d0&pt=Case%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=a40d5063-42b8-4c32-ad47-939eb0916e87&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Case%20Management&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcase-management%2F&r=&lt=33700&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=742776)
