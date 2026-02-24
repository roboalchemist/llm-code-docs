# Source: https://docs.datadoghq.com/api/latest/case-management.md

---
title: Case Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Case Management
---

# Case Management

View and manage cases and projects within Case Management. See the [Case Management page](https://docs.datadoghq.com/service_management/case_management/) for more information.

## Create a project{% #create-a-project %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/projects |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/projects |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/projects      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/projects      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/projects     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/projects |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/projects |

### Overview

Create a project.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Request

#### Body Data (required)

Project payload

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                          |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------- |
|              | data [*required*]       | object   | Project create                                       |
| data         | attributes [*required*] | object   | Project creation attributes                          |
| attributes   | enabled_custom_case_types    | [string] | List of enabled custom case type IDs                 |
| attributes   | key [*required*]        | string   | Project's key. Cannot be "CASE"                      |
| attributes   | name [*required*]       | string   | Project name                                         |
| attributes   | team_uuid                    | string   | Team UUID to associate with the project              |
| data         | type [*required*]       | enum     | Project resource type Allowed enum values: `project` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled_custom_case_types": [],
      "key": "SEC",
      "name": "Security Investigation",
      "team_uuid": "string"
    },
    "type": "project"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Project response

| Parent field                   | Field                                           | Type                | Description                                            |
| ------------------------------ | ----------------------------------------------- | ------------------- | ------------------------------------------------------ |
|                                | data                                            | object              | A Project                                              |
| data                           | attributes [*required*]                    | object              | Project attributes                                     |
| attributes                     | columns_config                                  | object              | Project columns configuration                          |
| columns_config                 | columns                                         | [object]            |
| columns                        | sort                                            | object              |
| sort                           | ascending                                       | boolean             |
| sort                           | priority                                        | int64               |
| columns                        | sort_field                                      | string              |
| columns                        | type                                            | string              |
| attributes                     | enabled_custom_case_types                       | [string]            | List of enabled custom case type IDs                   |
| attributes                     | key                                             | string              | The project's key                                      |
| attributes                     | name                                            | string              | Project's name                                         |
| attributes                     | restricted                                      | boolean             | Whether the project is restricted                      |
| attributes                     | settings                                        | object              | Project settings                                       |
| settings                       | auto_close_inactive_cases                       | object              | Auto-close inactive cases settings                     |
| auto_close_inactive_cases      | enabled                                         | boolean             | Whether auto-close is enabled                          |
| auto_close_inactive_cases      | max_inactive_time_in_secs                       | int64               | Maximum inactive time in seconds before auto-closing   |
| settings                       | auto_transition_assigned_cases                  | object              | Auto-transition assigned cases settings                |
| auto_transition_assigned_cases | auto_transition_assigned_cases_on_self_assigned | boolean             | Whether to auto-transition cases when self-assigned    |
| settings                       | integration_incident                            | object              | Incident integration settings                          |
| integration_incident           | auto_escalation_query                           | string              | Query for auto-escalation                              |
| integration_incident           | default_incident_commander                      | string              | Default incident commander                             |
| integration_incident           | enabled                                         | boolean             | Whether incident integration is enabled                |
| integration_incident           | field_mappings                                  | [object]            |
| field_mappings                 | case_field                                      | string              |
| field_mappings                 | incident_user_defined_field_id                  | string              |
| integration_incident           | incident_type                                   | string              | Incident type                                          |
| integration_incident           | severity_config                                 | object              |
| severity_config                | priority_mapping                                | object              |
| additionalProperties           | <any-key>                                       | string              |
| settings                       | integration_jira                                | object              | Jira integration settings                              |
| integration_jira               | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_jira               | enabled                                         | boolean             | Whether Jira integration is enabled                    |
| integration_jira               | metadata                                        | object              |
| metadata                       | account_id                                      | string              |
| metadata                       | issue_type_id                                   | string              |
| metadata                       | project_id                                      | string              |
| integration_jira               | sync                                            | object              |
| sync                           | enabled                                         | boolean             |
| sync                           | properties                                      | object              |
| properties                     | assignee                                        | object              | Sync property configuration                            |
| assignee                       | sync_type                                       | string              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | custom_fields                                   | object              |
| additionalProperties           | <any-key>                                       | object              |
| <any-key>                      | sync_type                                       | string              |
| <any-key>                      | value                                           | object <oneOf> | Represents any valid JSON value.                       |
| value                          | Option 1                                        | string              |
| value                          | Option 2                                        | double              |
| value                          | Option 3                                        | object              |
| value                          | Option 4                                        | [ <oneOf>]     |
| Option 4                       | Option 1                                        | string              |
| Option 4                       | Option 2                                        | double              |
| Option 4                       | Option 3                                        | object              |
| Option 4                       | Option 4                                        | boolean             |
| value                          | Option 5                                        | boolean             |
| properties                     | description                                     | object              | Sync property configuration                            |
| description                    | sync_type                                       | string              |
| properties                     | due_date                                        | object              |
| due_date                       | jira_field_id                                   | string              |
| due_date                       | sync_type                                       | string              |
| properties                     | priority                                        | object              | Sync property with mapping configuration               |
| priority                       | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| properties                     | title                                           | object              | Sync property configuration                            |
| title                          | sync_type                                       | string              |
| settings                       | integration_monitor                             | object              | Monitor integration settings                           |
| integration_monitor            | auto_resolve_enabled                            | boolean             | Whether auto-resolve is enabled                        |
| integration_monitor            | case_type_id                                    | string              | Case type ID for monitor integration                   |
| integration_monitor            | enabled                                         | boolean             | Whether monitor integration is enabled                 |
| integration_monitor            | handle                                          | string              | Monitor handle                                         |
| settings                       | integration_on_call                             | object              | On-Call integration settings                           |
| integration_on_call            | auto_assign_on_call                             | boolean             | Whether to auto-assign on-call                         |
| integration_on_call            | enabled                                         | boolean             | Whether On-Call integration is enabled                 |
| integration_on_call            | escalation_queries                              | [object]            |
| escalation_queries             | enabled                                         | boolean             |
| escalation_queries             | id                                              | string              |
| escalation_queries             | query                                           | string              |
| escalation_queries             | target                                          | object              |
| target                         | dynamic_team_paging                             | boolean             |
| target                         | team_id                                         | string              |
| target                         | user_id                                         | string              |
| settings                       | integration_service_now                         | object              | ServiceNow integration settings                        |
| integration_service_now        | assignment_group                                | string              | Assignment group                                       |
| integration_service_now        | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_service_now        | enabled                                         | boolean             | Whether ServiceNow integration is enabled              |
| integration_service_now        | instance_name                                   | string              | ServiceNow instance name                               |
| integration_service_now        | sync_config                                     | object              |
| sync_config                    | enabled                                         | boolean             |
| sync_config                    | properties                                      | object              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | priority                                        | object              |
| priority                       | impact_mapping                                  | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| priority                       | urgency_mapping                                 | object              |
| additionalProperties           | <any-key>                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| settings                       | notification                                    | object              | Project notification settings                          |
| notification                   | destinations                                    | [integer]           | Notification destinations (1=email, 2=slack, 3=in-app) |
| notification                   | enabled                                         | boolean             | Whether notifications are enabled                      |
| notification                   | notify_on_case_assignment                       | boolean             |
| notification                   | notify_on_case_closed                           | boolean             |
| notification                   | notify_on_case_comment                          | boolean             |
| notification                   | notify_on_case_comment_mention                  | boolean             |
| notification                   | notify_on_case_priority_change                  | boolean             |
| notification                   | notify_on_case_status_change                    | boolean             |
| notification                   | notify_on_case_unassignment                     | boolean             |
| data                           | id [*required*]                            | string              | The Project's identifier                               |
| data                           | relationships                                   | object              | Project relationships                                  |
| relationships                  | member_team                                     | object              | Relationship between a team and a team link            |
| member_team                    | data                                            | [object]            | Related team links                                     |
| data                           | id [*required*]                            | string              | The team link's identifier                             |
| data                           | type [*required*]                          | enum                | Team link type Allowed enum values: `team_links`       |
| member_team                    | links                                           | object              | Links attributes.                                      |
| links                          | related                                         | string              | Related link.                                          |
| relationships                  | member_user                                     | object              | Relationship to users.                                 |
| member_user                    | data [*required*]                          | [object]            | Relationships to user objects.                         |
| data                           | id [*required*]                            | string              | A unique identifier that represents the user.          |
| data                           | type [*required*]                          | enum                | User resource type. Allowed enum values: `user`        |
| data                           | type [*required*]                          | enum                | Project resource type Allowed enum values: `project`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "columns_config": {
        "columns": [
          {
            "sort": {
              "ascending": false,
              "priority": "integer"
            },
            "sort_field": "string",
            "type": "string"
          }
        ]
      },
      "enabled_custom_case_types": [],
      "key": "CASEM",
      "name": "Security Investigation",
      "restricted": false,
      "settings": {
        "auto_close_inactive_cases": {
          "enabled": false,
          "max_inactive_time_in_secs": "integer"
        },
        "auto_transition_assigned_cases": {
          "auto_transition_assigned_cases_on_self_assigned": false
        },
        "integration_incident": {
          "auto_escalation_query": "string",
          "default_incident_commander": "string",
          "enabled": false,
          "field_mappings": [
            {
              "case_field": "string",
              "incident_user_defined_field_id": "string"
            }
          ],
          "incident_type": "string",
          "severity_config": {
            "priority_mapping": {
              "<any-key>": "string"
            }
          }
        },
        "integration_jira": {
          "auto_creation": {
            "enabled": false
          },
          "enabled": false,
          "metadata": {
            "account_id": "string",
            "issue_type_id": "string",
            "project_id": "string"
          },
          "sync": {
            "enabled": false,
            "properties": {
              "assignee": {
                "sync_type": "string"
              },
              "comments": {
                "sync_type": "string"
              },
              "custom_fields": {
                "<any-key>": {
                  "sync_type": "string",
                  "value": {
                    "type": "undefined"
                  }
                }
              },
              "description": {
                "sync_type": "string"
              },
              "due_date": {
                "jira_field_id": "string",
                "sync_type": "string"
              },
              "priority": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              },
              "status": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              },
              "title": {
                "sync_type": "string"
              }
            }
          }
        },
        "integration_monitor": {
          "auto_resolve_enabled": false,
          "case_type_id": "string",
          "enabled": false,
          "handle": "string"
        },
        "integration_on_call": {
          "auto_assign_on_call": false,
          "enabled": false,
          "escalation_queries": [
            {
              "enabled": false,
              "id": "string",
              "query": "string",
              "target": {
                "dynamic_team_paging": false,
                "team_id": "string",
                "user_id": "string"
              }
            }
          ]
        },
        "integration_service_now": {
          "assignment_group": "string",
          "auto_creation": {
            "enabled": false
          },
          "enabled": false,
          "instance_name": "string",
          "sync_config": {
            "enabled": false,
            "properties": {
              "comments": {
                "sync_type": "string"
              },
              "priority": {
                "impact_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string",
                "urgency_mapping": {
                  "<any-key>": "string"
                }
              },
              "status": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              }
            }
          }
        },
        "notification": {
          "destinations": [],
          "enabled": false,
          "notify_on_case_assignment": false,
          "notify_on_case_closed": false,
          "notify_on_case_comment": false,
          "notify_on_case_comment_mention": false,
          "notify_on_case_priority_change": false,
          "notify_on_case_status_change": false,
          "notify_on_case_unassignment": false
        }
      }
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects" \
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
                
##### 

```python
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
            enabled_custom_case_types=[],
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create a project returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::ProjectCreateRequest.new({
  data: DatadogAPIClient::V2::ProjectCreate.new({
    attributes: DatadogAPIClient::V2::ProjectCreateAttributes.new({
      enabled_custom_case_types: [],
      key: "SEC",
      name: "Security Investigation",
    }),
    type: DatadogAPIClient::V2::ProjectResourceType::PROJECT,
  }),
})
p api_instance.create_project(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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
				EnabledCustomCaseTypes: []string{},
				Key:                    "SEC",
				Name:                   "Security Investigation",
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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
        ProjectCreateAttributes::new("SEC".to_string(), "Security Investigation".to_string())
            .enabled_custom_case_types(vec![]),
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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
        enabledCustomCaseTypes: [],
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get notification rules{% #get-notification-rules %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases/projects/{project_id}/notification_rules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases/projects/{project_id}/notification_rules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |

### Overview

Get all notification rules for a project.

OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description  |
| ---------------------------- | ------ | ------------ |
| project_id [*required*] | string | Project UUID |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with notification rules

| Parent field | Field                        | Type     | Description                                                                                                       |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
|              | data                         | [object] | Notification rules data                                                                                           |
| data         | attributes [*required*] | object   | Notification rule attributes                                                                                      |
| attributes   | is_enabled                   | boolean  | Whether the notification rule is enabled                                                                          |
| attributes   | query                        | string   | Query to filter cases for this notification rule                                                                  |
| attributes   | recipients                   | [object] | List of notification recipients                                                                                   |
| recipients   | data                         | object   | Recipient data                                                                                                    |
| data         | channel                      | string   | Slack channel name                                                                                                |
| data         | channel_id                   | string   | Slack channel ID                                                                                                  |
| data         | channel_name                 | string   | Microsoft Teams channel name                                                                                      |
| data         | connector_name               | string   | Microsoft Teams connector name                                                                                    |
| data         | email                        | string   | Email address                                                                                                     |
| data         | name                         | string   | HTTP webhook name                                                                                                 |
| data         | service_name                 | string   | PagerDuty service name                                                                                            |
| data         | team_id                      | string   | Microsoft Teams team ID                                                                                           |
| data         | team_name                    | string   | Microsoft Teams team name                                                                                         |
| data         | tenant_id                    | string   | Microsoft Teams tenant ID                                                                                         |
| data         | tenant_name                  | string   | Microsoft Teams tenant name                                                                                       |
| data         | workspace                    | string   | Slack workspace name                                                                                              |
| data         | workspace_id                 | string   | Slack workspace ID                                                                                                |
| recipients   | type                         | string   | Type of recipient (SLACK_CHANNEL, EMAIL, HTTP, PAGERDUTY_SERVICE, MS_TEAMS_CHANNEL)                               |
| attributes   | triggers                     | [object] | List of triggers for this notification rule                                                                       |
| triggers     | data                         | object   | Trigger data                                                                                                      |
| data         | change_type                  | string   | Change type (added, removed, changed)                                                                             |
| data         | field                        | string   | Field name for attribute value changed trigger                                                                    |
| data         | from_status                  | string   | Status ID to transition from                                                                                      |
| data         | from_status_name             | string   | Status name to transition from                                                                                    |
| data         | to_status                    | string   | Status ID to transition to                                                                                        |
| data         | to_status_name               | string   | Status name to transition to                                                                                      |
| triggers     | type                         | string   | Type of trigger (CASE_CREATED, STATUS_TRANSITIONED, ATTRIBUTE_VALUE_CHANGED, EVENT_CORRELATION_SIGNAL_CORRELATED) |
| data         | id [*required*]         | string   | The notification rule's identifier                                                                                |
| data         | type [*required*]       | enum     | Notification rule resource type Allowed enum values: `notification_rule`                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "is_enabled": false,
        "query": "string",
        "recipients": [
          {
            "data": {
              "channel": "string",
              "channel_id": "string",
              "channel_name": "string",
              "connector_name": "string",
              "email": "string",
              "name": "string",
              "service_name": "string",
              "team_id": "string",
              "team_name": "string",
              "tenant_id": "string",
              "tenant_name": "string",
              "workspace": "string",
              "workspace_id": "string"
            },
            "type": "EMAIL"
          }
        ],
        "triggers": [
          {
            "data": {
              "change_type": "string",
              "field": "string",
              "from_status": "string",
              "from_status_name": "string",
              "to_status": "string",
              "to_status_name": "string"
            },
            "type": "CASE_CREATED"
          }
        ]
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "notification_rule"
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
                  \# Path parametersexport project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}/notification_rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get notification rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.get_project_notification_rules(
        project_id="project_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get notification rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
p api_instance.get_project_notification_rules("project_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get notification rules returns "OK" response

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
	resp, r, err := api.GetProjectNotificationRules(ctx, "project_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.GetProjectNotificationRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.GetProjectNotificationRules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get notification rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseNotificationRulesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    try {
      CaseNotificationRulesResponse result =
          apiInstance.getProjectNotificationRules("e555e290-ed65-49bd-ae18-8acbfcf18db7");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#getProjectNotificationRules");
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
// Get notification rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .get_project_notification_rules("project_id".to_string())
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
 * Get notification rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiGetProjectNotificationRulesRequest = {
  projectId: "project_id",
};

apiInstance
  .getProjectNotificationRules(params)
  .then((data: v2.CaseNotificationRulesResponse) => {
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

## Search cases{% #search-cases %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases |

### Overview

Search cases.

OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                                    |
| ------------ | ------- | ------------------------------------------------------------------------------ |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100.                       |
| page[number] | integer | Specific page number to return.                                                |
| sort[field]  | enum    | Specify which field to sortAllowed enum values: `created_at, priority, status` |
| filter       | string  | Search query                                                                   |
| sort[asc]    | boolean | Specify if order is ascending or not                                           |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with cases

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | [object]      | Cases response data                                                                                                                                                                                   |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |
|                      | meta                         | object        | Cases response metadata                                                                                                                                                                               |
| meta                 | page                         | object        | Pagination metadata                                                                                                                                                                                   |
| page                 | current                      | int64         | Current page number                                                                                                                                                                                   |
| page                 | size                         | int64         | Number of cases in current page                                                                                                                                                                       |
| page                 | total                        | int64         | Total number of pages                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
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
        "status_group": "SG_OPEN",
        "status_name": "Open",
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Search cases returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
p api_instance.search_cases()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create a case{% #create-a-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                    |
| ----------------- | ----------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases |

### Overview

Create a Case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Request

#### Body Data (required)

Case payload

{% tab title="Model" %}

| Parent field         | Field                        | Type          | Description                                                                   |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------- |
|                      | data [*required*]       | object        | Case creation data                                                            |
| data                 | attributes [*required*] | object        | Case creation attributes                                                      |
| attributes           | custom_attributes            | object        | Case custom attributes                                                        |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                       |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                               |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`          |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                               |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                              |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                        |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                              |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                       |
| attributes           | description                  | string        | Description                                                                   |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`               |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type. |
| attributes           | title [*required*]      | string        | Title                                                                         |
| attributes           | type_id [*required*]    | string        | Case type UUID                                                                |
| data                 | relationships                | object        | Relationships formed with the case on creation                                |
| relationships        | assignee                     | object        | Relationship to user.                                                         |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                  |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                 |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                               |
| relationships        | project [*required*]    | object        | Relationship to project                                                       |
| project              | data [*required*]       | object        | Relationship to project object                                                |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                               |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                          |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create a notification rule{% #create-a-notification-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/projects/{project_id}/notification_rules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/projects/{project_id}/notification_rules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules |

### Overview

Create a notification rule for a project.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description  |
| ---------------------------- | ------ | ------------ |
| project_id [*required*] | string | Project UUID |

### Request

#### Body Data (required)

Notification rule payload

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                       |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Notification rule create                                                                                          |
| data         | attributes [*required*] | object   | Notification rule creation attributes                                                                             |
| attributes   | is_enabled                   | boolean  | Whether the notification rule is enabled                                                                          |
| attributes   | query                        | string   | Query to filter cases for this notification rule                                                                  |
| attributes   | recipients [*required*] | [object] | List of notification recipients                                                                                   |
| recipients   | data                         | object   | Recipient data                                                                                                    |
| data         | channel                      | string   | Slack channel name                                                                                                |
| data         | channel_id                   | string   | Slack channel ID                                                                                                  |
| data         | channel_name                 | string   | Microsoft Teams channel name                                                                                      |
| data         | connector_name               | string   | Microsoft Teams connector name                                                                                    |
| data         | email                        | string   | Email address                                                                                                     |
| data         | name                         | string   | HTTP webhook name                                                                                                 |
| data         | service_name                 | string   | PagerDuty service name                                                                                            |
| data         | team_id                      | string   | Microsoft Teams team ID                                                                                           |
| data         | team_name                    | string   | Microsoft Teams team name                                                                                         |
| data         | tenant_id                    | string   | Microsoft Teams tenant ID                                                                                         |
| data         | tenant_name                  | string   | Microsoft Teams tenant name                                                                                       |
| data         | workspace                    | string   | Slack workspace name                                                                                              |
| data         | workspace_id                 | string   | Slack workspace ID                                                                                                |
| recipients   | type                         | string   | Type of recipient (SLACK_CHANNEL, EMAIL, HTTP, PAGERDUTY_SERVICE, MS_TEAMS_CHANNEL)                               |
| attributes   | triggers [*required*]   | [object] | List of triggers for this notification rule                                                                       |
| triggers     | data                         | object   | Trigger data                                                                                                      |
| data         | change_type                  | string   | Change type (added, removed, changed)                                                                             |
| data         | field                        | string   | Field name for attribute value changed trigger                                                                    |
| data         | from_status                  | string   | Status ID to transition from                                                                                      |
| data         | from_status_name             | string   | Status name to transition from                                                                                    |
| data         | to_status                    | string   | Status ID to transition to                                                                                        |
| data         | to_status_name               | string   | Status name to transition to                                                                                      |
| triggers     | type                         | string   | Type of trigger (CASE_CREATED, STATUS_TRANSITIONED, ATTRIBUTE_VALUE_CHANGED, EVENT_CORRELATION_SIGNAL_CORRELATED) |
| data         | type [*required*]       | enum     | Notification rule resource type Allowed enum values: `notification_rule`                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "is_enabled": false,
      "query": "string",
      "recipients": [
        {
          "data": {
            "channel": "string",
            "channel_id": "string",
            "channel_name": "string",
            "connector_name": "string",
            "email": "string",
            "name": "string",
            "service_name": "string",
            "team_id": "string",
            "team_name": "string",
            "tenant_id": "string",
            "tenant_name": "string",
            "workspace": "string",
            "workspace_id": "string"
          },
          "type": "EMAIL"
        }
      ],
      "triggers": [
        {
          "data": {
            "change_type": "string",
            "field": "string",
            "from_status": "string",
            "from_status_name": "string",
            "to_status": "string",
            "to_status_name": "string"
          },
          "type": "CASE_CREATED"
        }
      ]
    },
    "type": "notification_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Notification rule response

| Parent field | Field                        | Type     | Description                                                                                                       |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | A notification rule for case management                                                                           |
| data         | attributes [*required*] | object   | Notification rule attributes                                                                                      |
| attributes   | is_enabled                   | boolean  | Whether the notification rule is enabled                                                                          |
| attributes   | query                        | string   | Query to filter cases for this notification rule                                                                  |
| attributes   | recipients                   | [object] | List of notification recipients                                                                                   |
| recipients   | data                         | object   | Recipient data                                                                                                    |
| data         | channel                      | string   | Slack channel name                                                                                                |
| data         | channel_id                   | string   | Slack channel ID                                                                                                  |
| data         | channel_name                 | string   | Microsoft Teams channel name                                                                                      |
| data         | connector_name               | string   | Microsoft Teams connector name                                                                                    |
| data         | email                        | string   | Email address                                                                                                     |
| data         | name                         | string   | HTTP webhook name                                                                                                 |
| data         | service_name                 | string   | PagerDuty service name                                                                                            |
| data         | team_id                      | string   | Microsoft Teams team ID                                                                                           |
| data         | team_name                    | string   | Microsoft Teams team name                                                                                         |
| data         | tenant_id                    | string   | Microsoft Teams tenant ID                                                                                         |
| data         | tenant_name                  | string   | Microsoft Teams tenant name                                                                                       |
| data         | workspace                    | string   | Slack workspace name                                                                                              |
| data         | workspace_id                 | string   | Slack workspace ID                                                                                                |
| recipients   | type                         | string   | Type of recipient (SLACK_CHANNEL, EMAIL, HTTP, PAGERDUTY_SERVICE, MS_TEAMS_CHANNEL)                               |
| attributes   | triggers                     | [object] | List of triggers for this notification rule                                                                       |
| triggers     | data                         | object   | Trigger data                                                                                                      |
| data         | change_type                  | string   | Change type (added, removed, changed)                                                                             |
| data         | field                        | string   | Field name for attribute value changed trigger                                                                    |
| data         | from_status                  | string   | Status ID to transition from                                                                                      |
| data         | from_status_name             | string   | Status name to transition from                                                                                    |
| data         | to_status                    | string   | Status ID to transition to                                                                                        |
| data         | to_status_name               | string   | Status name to transition to                                                                                      |
| triggers     | type                         | string   | Type of trigger (CASE_CREATED, STATUS_TRANSITIONED, ATTRIBUTE_VALUE_CHANGED, EVENT_CORRELATION_SIGNAL_CORRELATED) |
| data         | id [*required*]         | string   | The notification rule's identifier                                                                                |
| data         | type [*required*]       | enum     | Notification rule resource type Allowed enum values: `notification_rule`                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "is_enabled": false,
      "query": "string",
      "recipients": [
        {
          "data": {
            "channel": "string",
            "channel_id": "string",
            "channel_name": "string",
            "connector_name": "string",
            "email": "string",
            "name": "string",
            "service_name": "string",
            "team_id": "string",
            "team_name": "string",
            "tenant_id": "string",
            "tenant_name": "string",
            "workspace": "string",
            "workspace_id": "string"
          },
          "type": "EMAIL"
        }
      ],
      "triggers": [
        {
          "data": {
            "change_type": "string",
            "field": "string",
            "from_status": "string",
            "from_status_name": "string",
            "to_status": "string",
            "to_status_name": "string"
          },
          "type": "CASE_CREATED"
        }
      ]
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "notification_rule"
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
                  \# Path parametersexport project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}/notification_rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "recipients": [
        {}
      ],
      "triggers": [
        {}
      ]
    },
    "type": "notification_rule"
  }
}
EOF
                
##### 

```python
"""
Create a notification rule returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_notification_rule_create import CaseNotificationRuleCreate
from datadog_api_client.v2.model.case_notification_rule_create_attributes import CaseNotificationRuleCreateAttributes
from datadog_api_client.v2.model.case_notification_rule_create_request import CaseNotificationRuleCreateRequest
from datadog_api_client.v2.model.case_notification_rule_recipient import CaseNotificationRuleRecipient
from datadog_api_client.v2.model.case_notification_rule_recipient_data import CaseNotificationRuleRecipientData
from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType
from datadog_api_client.v2.model.case_notification_rule_trigger import CaseNotificationRuleTrigger
from datadog_api_client.v2.model.case_notification_rule_trigger_data import CaseNotificationRuleTriggerData

body = CaseNotificationRuleCreateRequest(
    data=CaseNotificationRuleCreate(
        attributes=CaseNotificationRuleCreateAttributes(
            is_enabled=True,
            recipients=[
                CaseNotificationRuleRecipient(
                    data=CaseNotificationRuleRecipientData(),
                    type="EMAIL",
                ),
            ],
            triggers=[
                CaseNotificationRuleTrigger(
                    data=CaseNotificationRuleTriggerData(),
                    type="CASE_CREATED",
                ),
            ],
        ),
        type=CaseNotificationRuleResourceType.NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_project_notification_rule(project_id="project_id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create a notification rule returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::CaseNotificationRuleCreateRequest.new({
  data: DatadogAPIClient::V2::CaseNotificationRuleCreate.new({
    attributes: DatadogAPIClient::V2::CaseNotificationRuleCreateAttributes.new({
      is_enabled: true,
      recipients: [
        DatadogAPIClient::V2::CaseNotificationRuleRecipient.new({
          data: DatadogAPIClient::V2::CaseNotificationRuleRecipientData.new({}),
          type: "EMAIL",
        }),
      ],
      triggers: [
        DatadogAPIClient::V2::CaseNotificationRuleTrigger.new({
          data: DatadogAPIClient::V2::CaseNotificationRuleTriggerData.new({}),
          type: "CASE_CREATED",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::CaseNotificationRuleResourceType::NOTIFICATION_RULE,
  }),
})
p api_instance.create_project_notification_rule("project_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create a notification rule returns "CREATED" response

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
	body := datadogV2.CaseNotificationRuleCreateRequest{
		Data: datadogV2.CaseNotificationRuleCreate{
			Attributes: datadogV2.CaseNotificationRuleCreateAttributes{
				IsEnabled: datadog.PtrBool(true),
				Recipients: []datadogV2.CaseNotificationRuleRecipient{
					{
						Data: &datadogV2.CaseNotificationRuleRecipientData{},
						Type: datadog.PtrString("EMAIL"),
					},
				},
				Triggers: []datadogV2.CaseNotificationRuleTrigger{
					{
						Data: &datadogV2.CaseNotificationRuleTriggerData{},
						Type: datadog.PtrString("CASE_CREATED"),
					},
				},
			},
			Type: datadogV2.CASENOTIFICATIONRULERESOURCETYPE_NOTIFICATION_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.CreateProjectNotificationRule(ctx, "project_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.CreateProjectNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.CreateProjectNotificationRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create a notification rule returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseNotificationRuleCreate;
import com.datadog.api.client.v2.model.CaseNotificationRuleCreateAttributes;
import com.datadog.api.client.v2.model.CaseNotificationRuleCreateRequest;
import com.datadog.api.client.v2.model.CaseNotificationRuleRecipient;
import com.datadog.api.client.v2.model.CaseNotificationRuleRecipientData;
import com.datadog.api.client.v2.model.CaseNotificationRuleResourceType;
import com.datadog.api.client.v2.model.CaseNotificationRuleResponse;
import com.datadog.api.client.v2.model.CaseNotificationRuleTrigger;
import com.datadog.api.client.v2.model.CaseNotificationRuleTriggerData;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    CaseNotificationRuleCreateRequest body =
        new CaseNotificationRuleCreateRequest()
            .data(
                new CaseNotificationRuleCreate()
                    .attributes(
                        new CaseNotificationRuleCreateAttributes()
                            .isEnabled(true)
                            .recipients(
                                Collections.singletonList(
                                    new CaseNotificationRuleRecipient()
                                        .data(new CaseNotificationRuleRecipientData())
                                        .type("EMAIL")))
                            .triggers(
                                Collections.singletonList(
                                    new CaseNotificationRuleTrigger()
                                        .data(new CaseNotificationRuleTriggerData())
                                        .type("CASE_CREATED"))))
                    .type(CaseNotificationRuleResourceType.NOTIFICATION_RULE));

    try {
      CaseNotificationRuleResponse result =
          apiInstance.createProjectNotificationRule("e555e290-ed65-49bd-ae18-8acbfcf18db7", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#createProjectNotificationRule");
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
// Create a notification rule returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseNotificationRuleCreate;
use datadog_api_client::datadogV2::model::CaseNotificationRuleCreateAttributes;
use datadog_api_client::datadogV2::model::CaseNotificationRuleCreateRequest;
use datadog_api_client::datadogV2::model::CaseNotificationRuleRecipient;
use datadog_api_client::datadogV2::model::CaseNotificationRuleRecipientData;
use datadog_api_client::datadogV2::model::CaseNotificationRuleResourceType;
use datadog_api_client::datadogV2::model::CaseNotificationRuleTrigger;
use datadog_api_client::datadogV2::model::CaseNotificationRuleTriggerData;

#[tokio::main]
async fn main() {
    let body = CaseNotificationRuleCreateRequest::new(CaseNotificationRuleCreate::new(
        CaseNotificationRuleCreateAttributes::new(
            vec![CaseNotificationRuleRecipient::new()
                .data(CaseNotificationRuleRecipientData::new())
                .type_("EMAIL".to_string())],
            vec![CaseNotificationRuleTrigger::new()
                .data(CaseNotificationRuleTriggerData::new())
                .type_("CASE_CREATED".to_string())],
        )
        .is_enabled(true),
        CaseNotificationRuleResourceType::NOTIFICATION_RULE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .create_project_notification_rule("project_id".to_string(), body)
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
 * Create a notification rule returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiCreateProjectNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        isEnabled: true,
        recipients: [
          {
            data: {},
            type: "EMAIL",
          },
        ],
        triggers: [
          {
            data: {},
            type: "CASE_CREATED",
          },
        ],
      },
      type: "notification_rule",
    },
  },
  projectId: "project_id",
};

apiInstance
  .createProjectNotificationRule(params)
  .then((data: v2.CaseNotificationRuleResponse) => {
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

## Get all projects{% #get-all-projects %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases/projects |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases/projects |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases/projects      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases/projects      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases/projects     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases/projects |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases/projects |

### Overview

Get all projects.

OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with projects

| Parent field                   | Field                                           | Type                | Description                                            |
| ------------------------------ | ----------------------------------------------- | ------------------- | ------------------------------------------------------ |
|                                | data                                            | [object]            | Projects response data                                 |
| data                           | attributes [*required*]                    | object              | Project attributes                                     |
| attributes                     | columns_config                                  | object              | Project columns configuration                          |
| columns_config                 | columns                                         | [object]            |
| columns                        | sort                                            | object              |
| sort                           | ascending                                       | boolean             |
| sort                           | priority                                        | int64               |
| columns                        | sort_field                                      | string              |
| columns                        | type                                            | string              |
| attributes                     | enabled_custom_case_types                       | [string]            | List of enabled custom case type IDs                   |
| attributes                     | key                                             | string              | The project's key                                      |
| attributes                     | name                                            | string              | Project's name                                         |
| attributes                     | restricted                                      | boolean             | Whether the project is restricted                      |
| attributes                     | settings                                        | object              | Project settings                                       |
| settings                       | auto_close_inactive_cases                       | object              | Auto-close inactive cases settings                     |
| auto_close_inactive_cases      | enabled                                         | boolean             | Whether auto-close is enabled                          |
| auto_close_inactive_cases      | max_inactive_time_in_secs                       | int64               | Maximum inactive time in seconds before auto-closing   |
| settings                       | auto_transition_assigned_cases                  | object              | Auto-transition assigned cases settings                |
| auto_transition_assigned_cases | auto_transition_assigned_cases_on_self_assigned | boolean             | Whether to auto-transition cases when self-assigned    |
| settings                       | integration_incident                            | object              | Incident integration settings                          |
| integration_incident           | auto_escalation_query                           | string              | Query for auto-escalation                              |
| integration_incident           | default_incident_commander                      | string              | Default incident commander                             |
| integration_incident           | enabled                                         | boolean             | Whether incident integration is enabled                |
| integration_incident           | field_mappings                                  | [object]            |
| field_mappings                 | case_field                                      | string              |
| field_mappings                 | incident_user_defined_field_id                  | string              |
| integration_incident           | incident_type                                   | string              | Incident type                                          |
| integration_incident           | severity_config                                 | object              |
| severity_config                | priority_mapping                                | object              |
| additionalProperties           | <any-key>                                       | string              |
| settings                       | integration_jira                                | object              | Jira integration settings                              |
| integration_jira               | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_jira               | enabled                                         | boolean             | Whether Jira integration is enabled                    |
| integration_jira               | metadata                                        | object              |
| metadata                       | account_id                                      | string              |
| metadata                       | issue_type_id                                   | string              |
| metadata                       | project_id                                      | string              |
| integration_jira               | sync                                            | object              |
| sync                           | enabled                                         | boolean             |
| sync                           | properties                                      | object              |
| properties                     | assignee                                        | object              | Sync property configuration                            |
| assignee                       | sync_type                                       | string              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | custom_fields                                   | object              |
| additionalProperties           | <any-key>                                       | object              |
| <any-key>                      | sync_type                                       | string              |
| <any-key>                      | value                                           | object <oneOf> | Represents any valid JSON value.                       |
| value                          | Option 1                                        | string              |
| value                          | Option 2                                        | double              |
| value                          | Option 3                                        | object              |
| value                          | Option 4                                        | [ <oneOf>]     |
| Option 4                       | Option 1                                        | string              |
| Option 4                       | Option 2                                        | double              |
| Option 4                       | Option 3                                        | object              |
| Option 4                       | Option 4                                        | boolean             |
| value                          | Option 5                                        | boolean             |
| properties                     | description                                     | object              | Sync property configuration                            |
| description                    | sync_type                                       | string              |
| properties                     | due_date                                        | object              |
| due_date                       | jira_field_id                                   | string              |
| due_date                       | sync_type                                       | string              |
| properties                     | priority                                        | object              | Sync property with mapping configuration               |
| priority                       | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| properties                     | title                                           | object              | Sync property configuration                            |
| title                          | sync_type                                       | string              |
| settings                       | integration_monitor                             | object              | Monitor integration settings                           |
| integration_monitor            | auto_resolve_enabled                            | boolean             | Whether auto-resolve is enabled                        |
| integration_monitor            | case_type_id                                    | string              | Case type ID for monitor integration                   |
| integration_monitor            | enabled                                         | boolean             | Whether monitor integration is enabled                 |
| integration_monitor            | handle                                          | string              | Monitor handle                                         |
| settings                       | integration_on_call                             | object              | On-Call integration settings                           |
| integration_on_call            | auto_assign_on_call                             | boolean             | Whether to auto-assign on-call                         |
| integration_on_call            | enabled                                         | boolean             | Whether On-Call integration is enabled                 |
| integration_on_call            | escalation_queries                              | [object]            |
| escalation_queries             | enabled                                         | boolean             |
| escalation_queries             | id                                              | string              |
| escalation_queries             | query                                           | string              |
| escalation_queries             | target                                          | object              |
| target                         | dynamic_team_paging                             | boolean             |
| target                         | team_id                                         | string              |
| target                         | user_id                                         | string              |
| settings                       | integration_service_now                         | object              | ServiceNow integration settings                        |
| integration_service_now        | assignment_group                                | string              | Assignment group                                       |
| integration_service_now        | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_service_now        | enabled                                         | boolean             | Whether ServiceNow integration is enabled              |
| integration_service_now        | instance_name                                   | string              | ServiceNow instance name                               |
| integration_service_now        | sync_config                                     | object              |
| sync_config                    | enabled                                         | boolean             |
| sync_config                    | properties                                      | object              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | priority                                        | object              |
| priority                       | impact_mapping                                  | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| priority                       | urgency_mapping                                 | object              |
| additionalProperties           | <any-key>                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| settings                       | notification                                    | object              | Project notification settings                          |
| notification                   | destinations                                    | [integer]           | Notification destinations (1=email, 2=slack, 3=in-app) |
| notification                   | enabled                                         | boolean             | Whether notifications are enabled                      |
| notification                   | notify_on_case_assignment                       | boolean             |
| notification                   | notify_on_case_closed                           | boolean             |
| notification                   | notify_on_case_comment                          | boolean             |
| notification                   | notify_on_case_comment_mention                  | boolean             |
| notification                   | notify_on_case_priority_change                  | boolean             |
| notification                   | notify_on_case_status_change                    | boolean             |
| notification                   | notify_on_case_unassignment                     | boolean             |
| data                           | id [*required*]                            | string              | The Project's identifier                               |
| data                           | relationships                                   | object              | Project relationships                                  |
| relationships                  | member_team                                     | object              | Relationship between a team and a team link            |
| member_team                    | data                                            | [object]            | Related team links                                     |
| data                           | id [*required*]                            | string              | The team link's identifier                             |
| data                           | type [*required*]                          | enum                | Team link type Allowed enum values: `team_links`       |
| member_team                    | links                                           | object              | Links attributes.                                      |
| links                          | related                                         | string              | Related link.                                          |
| relationships                  | member_user                                     | object              | Relationship to users.                                 |
| member_user                    | data [*required*]                          | [object]            | Relationships to user objects.                         |
| data                           | id [*required*]                            | string              | A unique identifier that represents the user.          |
| data                           | type [*required*]                          | enum                | User resource type. Allowed enum values: `user`        |
| data                           | type [*required*]                          | enum                | Project resource type Allowed enum values: `project`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "columns_config": {
          "columns": [
            {
              "sort": {
                "ascending": false,
                "priority": "integer"
              },
              "sort_field": "string",
              "type": "string"
            }
          ]
        },
        "enabled_custom_case_types": [],
        "key": "CASEM",
        "name": "Security Investigation",
        "restricted": false,
        "settings": {
          "auto_close_inactive_cases": {
            "enabled": false,
            "max_inactive_time_in_secs": "integer"
          },
          "auto_transition_assigned_cases": {
            "auto_transition_assigned_cases_on_self_assigned": false
          },
          "integration_incident": {
            "auto_escalation_query": "string",
            "default_incident_commander": "string",
            "enabled": false,
            "field_mappings": [
              {
                "case_field": "string",
                "incident_user_defined_field_id": "string"
              }
            ],
            "incident_type": "string",
            "severity_config": {
              "priority_mapping": {
                "<any-key>": "string"
              }
            }
          },
          "integration_jira": {
            "auto_creation": {
              "enabled": false
            },
            "enabled": false,
            "metadata": {
              "account_id": "string",
              "issue_type_id": "string",
              "project_id": "string"
            },
            "sync": {
              "enabled": false,
              "properties": {
                "assignee": {
                  "sync_type": "string"
                },
                "comments": {
                  "sync_type": "string"
                },
                "custom_fields": {
                  "<any-key>": {
                    "sync_type": "string",
                    "value": {
                      "type": "undefined"
                    }
                  }
                },
                "description": {
                  "sync_type": "string"
                },
                "due_date": {
                  "jira_field_id": "string",
                  "sync_type": "string"
                },
                "priority": {
                  "mapping": {
                    "<any-key>": "string"
                  },
                  "name_mapping": {
                    "<any-key>": "string"
                  },
                  "sync_type": "string"
                },
                "status": {
                  "mapping": {
                    "<any-key>": "string"
                  },
                  "name_mapping": {
                    "<any-key>": "string"
                  },
                  "sync_type": "string"
                },
                "title": {
                  "sync_type": "string"
                }
              }
            }
          },
          "integration_monitor": {
            "auto_resolve_enabled": false,
            "case_type_id": "string",
            "enabled": false,
            "handle": "string"
          },
          "integration_on_call": {
            "auto_assign_on_call": false,
            "enabled": false,
            "escalation_queries": [
              {
                "enabled": false,
                "id": "string",
                "query": "string",
                "target": {
                  "dynamic_team_paging": false,
                  "team_id": "string",
                  "user_id": "string"
                }
              }
            ]
          },
          "integration_service_now": {
            "assignment_group": "string",
            "auto_creation": {
              "enabled": false
            },
            "enabled": false,
            "instance_name": "string",
            "sync_config": {
              "enabled": false,
              "properties": {
                "comments": {
                  "sync_type": "string"
                },
                "priority": {
                  "impact_mapping": {
                    "<any-key>": "string"
                  },
                  "sync_type": "string",
                  "urgency_mapping": {
                    "<any-key>": "string"
                  }
                },
                "status": {
                  "mapping": {
                    "<any-key>": "string"
                  },
                  "name_mapping": {
                    "<any-key>": "string"
                  },
                  "sync_type": "string"
                }
              }
            }
          },
          "notification": {
            "destinations": [],
            "enabled": false,
            "notify_on_case_assignment": false,
            "notify_on_case_closed": false,
            "notify_on_case_comment": false,
            "notify_on_case_comment_mention": false,
            "notify_on_case_priority_change": false,
            "notify_on_case_status_change": false,
            "notify_on_case_unassignment": false
          }
        }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get all projects returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
p api_instance.get_projects()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get the details of a case{% #get-the-details-of-a-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases/{case_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases/{case_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases/{case_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases/{case_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases/{case_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases/{case_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases/{case_id} |

### Overview

Get the details of case by `case_id`

OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get the details of a case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]
p api_instance.get_case(CASE_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get the details of a project{% #get-the-details-of-a-project %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases/projects/{project_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases/projects/{project_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases/projects/{project_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id} |

### Overview

Get the details of a project by `project_id`.

OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description  |
| ---------------------------- | ------ | ------------ |
| project_id [*required*] | string | Project UUID |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Project response

| Parent field                   | Field                                           | Type                | Description                                            |
| ------------------------------ | ----------------------------------------------- | ------------------- | ------------------------------------------------------ |
|                                | data                                            | object              | A Project                                              |
| data                           | attributes [*required*]                    | object              | Project attributes                                     |
| attributes                     | columns_config                                  | object              | Project columns configuration                          |
| columns_config                 | columns                                         | [object]            |
| columns                        | sort                                            | object              |
| sort                           | ascending                                       | boolean             |
| sort                           | priority                                        | int64               |
| columns                        | sort_field                                      | string              |
| columns                        | type                                            | string              |
| attributes                     | enabled_custom_case_types                       | [string]            | List of enabled custom case type IDs                   |
| attributes                     | key                                             | string              | The project's key                                      |
| attributes                     | name                                            | string              | Project's name                                         |
| attributes                     | restricted                                      | boolean             | Whether the project is restricted                      |
| attributes                     | settings                                        | object              | Project settings                                       |
| settings                       | auto_close_inactive_cases                       | object              | Auto-close inactive cases settings                     |
| auto_close_inactive_cases      | enabled                                         | boolean             | Whether auto-close is enabled                          |
| auto_close_inactive_cases      | max_inactive_time_in_secs                       | int64               | Maximum inactive time in seconds before auto-closing   |
| settings                       | auto_transition_assigned_cases                  | object              | Auto-transition assigned cases settings                |
| auto_transition_assigned_cases | auto_transition_assigned_cases_on_self_assigned | boolean             | Whether to auto-transition cases when self-assigned    |
| settings                       | integration_incident                            | object              | Incident integration settings                          |
| integration_incident           | auto_escalation_query                           | string              | Query for auto-escalation                              |
| integration_incident           | default_incident_commander                      | string              | Default incident commander                             |
| integration_incident           | enabled                                         | boolean             | Whether incident integration is enabled                |
| integration_incident           | field_mappings                                  | [object]            |
| field_mappings                 | case_field                                      | string              |
| field_mappings                 | incident_user_defined_field_id                  | string              |
| integration_incident           | incident_type                                   | string              | Incident type                                          |
| integration_incident           | severity_config                                 | object              |
| severity_config                | priority_mapping                                | object              |
| additionalProperties           | <any-key>                                       | string              |
| settings                       | integration_jira                                | object              | Jira integration settings                              |
| integration_jira               | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_jira               | enabled                                         | boolean             | Whether Jira integration is enabled                    |
| integration_jira               | metadata                                        | object              |
| metadata                       | account_id                                      | string              |
| metadata                       | issue_type_id                                   | string              |
| metadata                       | project_id                                      | string              |
| integration_jira               | sync                                            | object              |
| sync                           | enabled                                         | boolean             |
| sync                           | properties                                      | object              |
| properties                     | assignee                                        | object              | Sync property configuration                            |
| assignee                       | sync_type                                       | string              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | custom_fields                                   | object              |
| additionalProperties           | <any-key>                                       | object              |
| <any-key>                      | sync_type                                       | string              |
| <any-key>                      | value                                           | object <oneOf> | Represents any valid JSON value.                       |
| value                          | Option 1                                        | string              |
| value                          | Option 2                                        | double              |
| value                          | Option 3                                        | object              |
| value                          | Option 4                                        | [ <oneOf>]     |
| Option 4                       | Option 1                                        | string              |
| Option 4                       | Option 2                                        | double              |
| Option 4                       | Option 3                                        | object              |
| Option 4                       | Option 4                                        | boolean             |
| value                          | Option 5                                        | boolean             |
| properties                     | description                                     | object              | Sync property configuration                            |
| description                    | sync_type                                       | string              |
| properties                     | due_date                                        | object              |
| due_date                       | jira_field_id                                   | string              |
| due_date                       | sync_type                                       | string              |
| properties                     | priority                                        | object              | Sync property with mapping configuration               |
| priority                       | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| properties                     | title                                           | object              | Sync property configuration                            |
| title                          | sync_type                                       | string              |
| settings                       | integration_monitor                             | object              | Monitor integration settings                           |
| integration_monitor            | auto_resolve_enabled                            | boolean             | Whether auto-resolve is enabled                        |
| integration_monitor            | case_type_id                                    | string              | Case type ID for monitor integration                   |
| integration_monitor            | enabled                                         | boolean             | Whether monitor integration is enabled                 |
| integration_monitor            | handle                                          | string              | Monitor handle                                         |
| settings                       | integration_on_call                             | object              | On-Call integration settings                           |
| integration_on_call            | auto_assign_on_call                             | boolean             | Whether to auto-assign on-call                         |
| integration_on_call            | enabled                                         | boolean             | Whether On-Call integration is enabled                 |
| integration_on_call            | escalation_queries                              | [object]            |
| escalation_queries             | enabled                                         | boolean             |
| escalation_queries             | id                                              | string              |
| escalation_queries             | query                                           | string              |
| escalation_queries             | target                                          | object              |
| target                         | dynamic_team_paging                             | boolean             |
| target                         | team_id                                         | string              |
| target                         | user_id                                         | string              |
| settings                       | integration_service_now                         | object              | ServiceNow integration settings                        |
| integration_service_now        | assignment_group                                | string              | Assignment group                                       |
| integration_service_now        | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_service_now        | enabled                                         | boolean             | Whether ServiceNow integration is enabled              |
| integration_service_now        | instance_name                                   | string              | ServiceNow instance name                               |
| integration_service_now        | sync_config                                     | object              |
| sync_config                    | enabled                                         | boolean             |
| sync_config                    | properties                                      | object              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | priority                                        | object              |
| priority                       | impact_mapping                                  | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| priority                       | urgency_mapping                                 | object              |
| additionalProperties           | <any-key>                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| settings                       | notification                                    | object              | Project notification settings                          |
| notification                   | destinations                                    | [integer]           | Notification destinations (1=email, 2=slack, 3=in-app) |
| notification                   | enabled                                         | boolean             | Whether notifications are enabled                      |
| notification                   | notify_on_case_assignment                       | boolean             |
| notification                   | notify_on_case_closed                           | boolean             |
| notification                   | notify_on_case_comment                          | boolean             |
| notification                   | notify_on_case_comment_mention                  | boolean             |
| notification                   | notify_on_case_priority_change                  | boolean             |
| notification                   | notify_on_case_status_change                    | boolean             |
| notification                   | notify_on_case_unassignment                     | boolean             |
| data                           | id [*required*]                            | string              | The Project's identifier                               |
| data                           | relationships                                   | object              | Project relationships                                  |
| relationships                  | member_team                                     | object              | Relationship between a team and a team link            |
| member_team                    | data                                            | [object]            | Related team links                                     |
| data                           | id [*required*]                            | string              | The team link's identifier                             |
| data                           | type [*required*]                          | enum                | Team link type Allowed enum values: `team_links`       |
| member_team                    | links                                           | object              | Links attributes.                                      |
| links                          | related                                         | string              | Related link.                                          |
| relationships                  | member_user                                     | object              | Relationship to users.                                 |
| member_user                    | data [*required*]                          | [object]            | Relationships to user objects.                         |
| data                           | id [*required*]                            | string              | A unique identifier that represents the user.          |
| data                           | type [*required*]                          | enum                | User resource type. Allowed enum values: `user`        |
| data                           | type [*required*]                          | enum                | Project resource type Allowed enum values: `project`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "columns_config": {
        "columns": [
          {
            "sort": {
              "ascending": false,
              "priority": "integer"
            },
            "sort_field": "string",
            "type": "string"
          }
        ]
      },
      "enabled_custom_case_types": [],
      "key": "CASEM",
      "name": "Security Investigation",
      "restricted": false,
      "settings": {
        "auto_close_inactive_cases": {
          "enabled": false,
          "max_inactive_time_in_secs": "integer"
        },
        "auto_transition_assigned_cases": {
          "auto_transition_assigned_cases_on_self_assigned": false
        },
        "integration_incident": {
          "auto_escalation_query": "string",
          "default_incident_commander": "string",
          "enabled": false,
          "field_mappings": [
            {
              "case_field": "string",
              "incident_user_defined_field_id": "string"
            }
          ],
          "incident_type": "string",
          "severity_config": {
            "priority_mapping": {
              "<any-key>": "string"
            }
          }
        },
        "integration_jira": {
          "auto_creation": {
            "enabled": false
          },
          "enabled": false,
          "metadata": {
            "account_id": "string",
            "issue_type_id": "string",
            "project_id": "string"
          },
          "sync": {
            "enabled": false,
            "properties": {
              "assignee": {
                "sync_type": "string"
              },
              "comments": {
                "sync_type": "string"
              },
              "custom_fields": {
                "<any-key>": {
                  "sync_type": "string",
                  "value": {
                    "type": "undefined"
                  }
                }
              },
              "description": {
                "sync_type": "string"
              },
              "due_date": {
                "jira_field_id": "string",
                "sync_type": "string"
              },
              "priority": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              },
              "status": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              },
              "title": {
                "sync_type": "string"
              }
            }
          }
        },
        "integration_monitor": {
          "auto_resolve_enabled": false,
          "case_type_id": "string",
          "enabled": false,
          "handle": "string"
        },
        "integration_on_call": {
          "auto_assign_on_call": false,
          "enabled": false,
          "escalation_queries": [
            {
              "enabled": false,
              "id": "string",
              "query": "string",
              "target": {
                "dynamic_team_paging": false,
                "team_id": "string",
                "user_id": "string"
              }
            }
          ]
        },
        "integration_service_now": {
          "assignment_group": "string",
          "auto_creation": {
            "enabled": false
          },
          "enabled": false,
          "instance_name": "string",
          "sync_config": {
            "enabled": false,
            "properties": {
              "comments": {
                "sync_type": "string"
              },
              "priority": {
                "impact_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string",
                "urgency_mapping": {
                  "<any-key>": "string"
                }
              },
              "status": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              }
            }
          }
        },
        "notification": {
          "destinations": [],
          "enabled": false,
          "notify_on_case_assignment": false,
          "notify_on_case_closed": false,
          "notify_on_case_comment": false,
          "notify_on_case_comment_mention": false,
          "notify_on_case_priority_change": false,
          "notify_on_case_status_change": false,
          "notify_on_case_unassignment": false
        }
      }
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
                  \# Path parametersexport project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get the details of a project returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
p api_instance.get_project("project_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update a notification rule{% #update-a-notification-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                   |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |

### Overview

Update a notification rule.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                                   | Type   | Description            |
| -------------------------------------- | ------ | ---------------------- |
| project_id [*required*]           | string | Project UUID           |
| notification_rule_id [*required*] | string | Notification Rule UUID |

### Request

#### Body Data (required)

Notification rule payload

{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                       |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object   | Notification rule update                                                                                          |
| data         | attributes             | object   | Notification rule attributes                                                                                      |
| attributes   | is_enabled             | boolean  | Whether the notification rule is enabled                                                                          |
| attributes   | query                  | string   | Query to filter cases for this notification rule                                                                  |
| attributes   | recipients             | [object] | List of notification recipients                                                                                   |
| recipients   | data                   | object   | Recipient data                                                                                                    |
| data         | channel                | string   | Slack channel name                                                                                                |
| data         | channel_id             | string   | Slack channel ID                                                                                                  |
| data         | channel_name           | string   | Microsoft Teams channel name                                                                                      |
| data         | connector_name         | string   | Microsoft Teams connector name                                                                                    |
| data         | email                  | string   | Email address                                                                                                     |
| data         | name                   | string   | HTTP webhook name                                                                                                 |
| data         | service_name           | string   | PagerDuty service name                                                                                            |
| data         | team_id                | string   | Microsoft Teams team ID                                                                                           |
| data         | team_name              | string   | Microsoft Teams team name                                                                                         |
| data         | tenant_id              | string   | Microsoft Teams tenant ID                                                                                         |
| data         | tenant_name            | string   | Microsoft Teams tenant name                                                                                       |
| data         | workspace              | string   | Slack workspace name                                                                                              |
| data         | workspace_id           | string   | Slack workspace ID                                                                                                |
| recipients   | type                   | string   | Type of recipient (SLACK_CHANNEL, EMAIL, HTTP, PAGERDUTY_SERVICE, MS_TEAMS_CHANNEL)                               |
| attributes   | triggers               | [object] | List of triggers for this notification rule                                                                       |
| triggers     | data                   | object   | Trigger data                                                                                                      |
| data         | change_type            | string   | Change type (added, removed, changed)                                                                             |
| data         | field                  | string   | Field name for attribute value changed trigger                                                                    |
| data         | from_status            | string   | Status ID to transition from                                                                                      |
| data         | from_status_name       | string   | Status name to transition from                                                                                    |
| data         | to_status              | string   | Status ID to transition to                                                                                        |
| data         | to_status_name         | string   | Status name to transition to                                                                                      |
| triggers     | type                   | string   | Type of trigger (CASE_CREATED, STATUS_TRANSITIONED, ATTRIBUTE_VALUE_CHANGED, EVENT_CORRELATION_SIGNAL_CORRELATED) |
| data         | type [*required*] | enum     | Notification rule resource type Allowed enum values: `notification_rule`                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "is_enabled": false,
      "query": "string",
      "recipients": [
        {
          "data": {
            "channel": "string",
            "channel_id": "string",
            "channel_name": "string",
            "connector_name": "string",
            "email": "string",
            "name": "string",
            "service_name": "string",
            "team_id": "string",
            "team_name": "string",
            "tenant_id": "string",
            "tenant_name": "string",
            "workspace": "string",
            "workspace_id": "string"
          },
          "type": "EMAIL"
        }
      ],
      "triggers": [
        {
          "data": {
            "change_type": "string",
            "field": "string",
            "from_status": "string",
            "from_status_name": "string",
            "to_status": "string",
            "to_status_name": "string"
          },
          "type": "CASE_CREATED"
        }
      ]
    },
    "type": "notification_rule"
  }
}
```

{% /tab %}

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
                  \# Path parametersexport project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"export notification_rule_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}/notification_rules/${notification_rule_id}" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "notification_rule"
  }
}
EOF
                
##### 

```python
"""
Update a notification rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_notification_rule_attributes import CaseNotificationRuleAttributes
from datadog_api_client.v2.model.case_notification_rule_recipient import CaseNotificationRuleRecipient
from datadog_api_client.v2.model.case_notification_rule_recipient_data import CaseNotificationRuleRecipientData
from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType
from datadog_api_client.v2.model.case_notification_rule_trigger import CaseNotificationRuleTrigger
from datadog_api_client.v2.model.case_notification_rule_trigger_data import CaseNotificationRuleTriggerData
from datadog_api_client.v2.model.case_notification_rule_update import CaseNotificationRuleUpdate
from datadog_api_client.v2.model.case_notification_rule_update_request import CaseNotificationRuleUpdateRequest

body = CaseNotificationRuleUpdateRequest(
    data=CaseNotificationRuleUpdate(
        attributes=CaseNotificationRuleAttributes(
            recipients=[
                CaseNotificationRuleRecipient(
                    data=CaseNotificationRuleRecipientData(),
                    type="EMAIL",
                ),
            ],
            triggers=[
                CaseNotificationRuleTrigger(
                    data=CaseNotificationRuleTriggerData(),
                    type="CASE_CREATED",
                ),
            ],
        ),
        type=CaseNotificationRuleResourceType.NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.update_project_notification_rule(
        project_id="project_id", notification_rule_id="notification_rule_id", body=body
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update a notification rule returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::CaseNotificationRuleUpdateRequest.new({
  data: DatadogAPIClient::V2::CaseNotificationRuleUpdate.new({
    attributes: DatadogAPIClient::V2::CaseNotificationRuleAttributes.new({
      recipients: [
        DatadogAPIClient::V2::CaseNotificationRuleRecipient.new({
          data: DatadogAPIClient::V2::CaseNotificationRuleRecipientData.new({}),
          type: "EMAIL",
        }),
      ],
      triggers: [
        DatadogAPIClient::V2::CaseNotificationRuleTrigger.new({
          data: DatadogAPIClient::V2::CaseNotificationRuleTriggerData.new({}),
          type: "CASE_CREATED",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::CaseNotificationRuleResourceType::NOTIFICATION_RULE,
  }),
})
api_instance.update_project_notification_rule("project_id", "notification_rule_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Update a notification rule returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CaseNotificationRuleUpdateRequest{
		Data: datadogV2.CaseNotificationRuleUpdate{
			Attributes: &datadogV2.CaseNotificationRuleAttributes{
				Recipients: []datadogV2.CaseNotificationRuleRecipient{
					{
						Data: &datadogV2.CaseNotificationRuleRecipientData{},
						Type: datadog.PtrString("EMAIL"),
					},
				},
				Triggers: []datadogV2.CaseNotificationRuleTrigger{
					{
						Data: &datadogV2.CaseNotificationRuleTriggerData{},
						Type: datadog.PtrString("CASE_CREATED"),
					},
				},
			},
			Type: datadogV2.CASENOTIFICATIONRULERESOURCETYPE_NOTIFICATION_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.UpdateProjectNotificationRule(ctx, "project_id", "notification_rule_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdateProjectNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update a notification rule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseNotificationRuleAttributes;
import com.datadog.api.client.v2.model.CaseNotificationRuleRecipient;
import com.datadog.api.client.v2.model.CaseNotificationRuleRecipientData;
import com.datadog.api.client.v2.model.CaseNotificationRuleResourceType;
import com.datadog.api.client.v2.model.CaseNotificationRuleTrigger;
import com.datadog.api.client.v2.model.CaseNotificationRuleTriggerData;
import com.datadog.api.client.v2.model.CaseNotificationRuleUpdate;
import com.datadog.api.client.v2.model.CaseNotificationRuleUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    CaseNotificationRuleUpdateRequest body =
        new CaseNotificationRuleUpdateRequest()
            .data(
                new CaseNotificationRuleUpdate()
                    .attributes(
                        new CaseNotificationRuleAttributes()
                            .recipients(
                                Collections.singletonList(
                                    new CaseNotificationRuleRecipient()
                                        .data(new CaseNotificationRuleRecipientData())
                                        .type("EMAIL")))
                            .triggers(
                                Collections.singletonList(
                                    new CaseNotificationRuleTrigger()
                                        .data(new CaseNotificationRuleTriggerData())
                                        .type("CASE_CREATED"))))
                    .type(CaseNotificationRuleResourceType.NOTIFICATION_RULE));

    try {
      apiInstance.updateProjectNotificationRule(
          "e555e290-ed65-49bd-ae18-8acbfcf18db7", "e555e290-ed65-49bd-ae18-8acbfcf18db7", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updateProjectNotificationRule");
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
// Update a notification rule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::CaseNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::CaseNotificationRuleRecipient;
use datadog_api_client::datadogV2::model::CaseNotificationRuleRecipientData;
use datadog_api_client::datadogV2::model::CaseNotificationRuleResourceType;
use datadog_api_client::datadogV2::model::CaseNotificationRuleTrigger;
use datadog_api_client::datadogV2::model::CaseNotificationRuleTriggerData;
use datadog_api_client::datadogV2::model::CaseNotificationRuleUpdate;
use datadog_api_client::datadogV2::model::CaseNotificationRuleUpdateRequest;

#[tokio::main]
async fn main() {
    let body = CaseNotificationRuleUpdateRequest::new(
        CaseNotificationRuleUpdate::new(CaseNotificationRuleResourceType::NOTIFICATION_RULE)
            .attributes(
                CaseNotificationRuleAttributes::new()
                    .recipients(vec![CaseNotificationRuleRecipient::new()
                        .data(CaseNotificationRuleRecipientData::new())
                        .type_("EMAIL".to_string())])
                    .triggers(vec![CaseNotificationRuleTrigger::new()
                        .data(CaseNotificationRuleTriggerData::new())
                        .type_("CASE_CREATED".to_string())]),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .update_project_notification_rule(
            "project_id".to_string(),
            "notification_rule_id".to_string(),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Update a notification rule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiUpdateProjectNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        recipients: [
          {
            data: {},
            type: "EMAIL",
          },
        ],
        triggers: [
          {
            data: {},
            type: "CASE_CREATED",
          },
        ],
      },
      type: "notification_rule",
    },
  },
  projectId: "project_id",
  notificationRuleId: "notification_rule_id",
};

apiInstance
  .updateProjectNotificationRule(params)
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

## Delete a notification rule{% #delete-a-notification-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id} |

### Overview

Delete a notification rule using the notification rule's `id`.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                                   | Type   | Description            |
| -------------------------------------- | ------ | ---------------------- |
| project_id [*required*]           | string | Project UUID           |
| notification_rule_id [*required*] | string | Notification Rule UUID |

### Response

{% tab title="204" %}
No Content
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
API error response
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
                  \# Path parametersexport project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"export notification_rule_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}/notification_rules/${notification_rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a notification rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.delete_project_notification_rule(
        project_id="project_id",
        notification_rule_id="notification_rule_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete a notification rule returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
api_instance.delete_project_notification_rule("project_id", "notification_rule_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete a notification rule returns "No Content" response

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
	r, err := api.DeleteProjectNotificationRule(ctx, "project_id", "notification_rule_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.DeleteProjectNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete a notification rule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    try {
      apiInstance.deleteProjectNotificationRule(
          "e555e290-ed65-49bd-ae18-8acbfcf18db7", "e555e290-ed65-49bd-ae18-8acbfcf18db7");
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#deleteProjectNotificationRule");
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
// Delete a notification rule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .delete_project_notification_rule(
            "project_id".to_string(),
            "notification_rule_id".to_string(),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Delete a notification rule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiDeleteProjectNotificationRuleRequest = {
  projectId: "project_id",
  notificationRuleId: "notification_rule_id",
};

apiInstance
  .deleteProjectNotificationRule(params)
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

## Remove a project{% #remove-a-project %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cases/projects/{project_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cases/projects/{project_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cases/projects/{project_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id} |

### Overview

Remove a project using the project's `id`.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description  |
| ---------------------------- | ------ | ------------ |
| project_id [*required*] | string | Project UUID |

### Response

{% tab title="204" %}
No Content
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
API error response
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
                  \# Path parametersexport project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Remove a project returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
api_instance.delete_project("project_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update case description{% #update-case-description %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/description |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/description |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/description      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/description      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/description     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/description |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/description |

### Overview

Update case description

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Case description update payload

{% tab title="Model" %}

| Parent field | Field                         | Type   | Description                                    |
| ------------ | ----------------------------- | ------ | ---------------------------------------------- |
|              | data [*required*]        | object | Case update description                        |
| data         | attributes [*required*]  | object | Case update description attributes             |
| attributes   | description [*required*] | string | Case new description                           |
| data         | type [*required*]        | enum   | Case resource type Allowed enum values: `case` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Seeing some weird memory increase... Updating the description"
    },
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/description" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update case status{% #update-case-status %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/status |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/status |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/status      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/status      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/status     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/status |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/status |

### Overview

Update case status

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Case status update payload

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                                                                                           |
| ------------ | ---------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Case update status                                                                                                                                                                                    |
| data         | attributes [*required*] | object | Case update status attributes                                                                                                                                                                         |
| attributes   | status                       | enum   | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes   | status_name                  | string | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| data         | type [*required*]       | enum   | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "status": "IN_PROGRESS"
    },
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/status" \
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
                        
##### 

```go
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
				Status: datadogV2.CASESTATUS_IN_PROGRESS.Ptr(),
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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
        CaseUpdateStatusAttributes::new().status(CaseStatus::IN_PROGRESS),
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update case title{% #update-case-title %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/title |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/title |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/title      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/title      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/title     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/title |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/title |

### Overview

Update case title

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Case title update payload

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                    |
| ------------ | ---------------------------- | ------ | ---------------------------------------------- |
|              | data [*required*]       | object | Case update title                              |
| data         | attributes [*required*] | object | Case update title attributes                   |
| attributes   | title [*required*]      | string | Case new title                                 |
| data         | type [*required*]       | enum   | Case resource type Allowed enum values: `case` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "title": "[UPDATED] Memory leak investigation on API"
    },
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/title" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update a project{% #update-a-project %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/cases/projects/{project_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/cases/projects/{project_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/cases/projects/{project_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/cases/projects/{project_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/cases/projects/{project_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/cases/projects/{project_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/cases/projects/{project_id} |

### Overview

Update a project.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description  |
| ---------------------------- | ------ | ------------ |
| project_id [*required*] | string | Project UUID |

### Request

#### Body Data (required)

Project payload

{% tab title="Model" %}

| Parent field                   | Field                                           | Type                | Description                                            |
| ------------------------------ | ----------------------------------------------- | ------------------- | ------------------------------------------------------ |
|                                | data [*required*]                          | object              | Project update                                         |
| data                           | attributes                                      | object              | Project update attributes                              |
| attributes                     | columns_config                                  | object              | Project columns configuration                          |
| columns_config                 | columns                                         | [object]            |
| columns                        | sort                                            | object              |
| sort                           | ascending                                       | boolean             |
| sort                           | priority                                        | int64               |
| columns                        | sort_field                                      | string              |
| columns                        | type                                            | string              |
| attributes                     | enabled_custom_case_types                       | [string]            | List of enabled custom case type IDs                   |
| attributes                     | name                                            | string              | Project name                                           |
| attributes                     | settings                                        | object              | Project settings                                       |
| settings                       | auto_close_inactive_cases                       | object              | Auto-close inactive cases settings                     |
| auto_close_inactive_cases      | enabled                                         | boolean             | Whether auto-close is enabled                          |
| auto_close_inactive_cases      | max_inactive_time_in_secs                       | int64               | Maximum inactive time in seconds before auto-closing   |
| settings                       | auto_transition_assigned_cases                  | object              | Auto-transition assigned cases settings                |
| auto_transition_assigned_cases | auto_transition_assigned_cases_on_self_assigned | boolean             | Whether to auto-transition cases when self-assigned    |
| settings                       | integration_incident                            | object              | Incident integration settings                          |
| integration_incident           | auto_escalation_query                           | string              | Query for auto-escalation                              |
| integration_incident           | default_incident_commander                      | string              | Default incident commander                             |
| integration_incident           | enabled                                         | boolean             | Whether incident integration is enabled                |
| integration_incident           | field_mappings                                  | [object]            |
| field_mappings                 | case_field                                      | string              |
| field_mappings                 | incident_user_defined_field_id                  | string              |
| integration_incident           | incident_type                                   | string              | Incident type                                          |
| integration_incident           | severity_config                                 | object              |
| severity_config                | priority_mapping                                | object              |
| additionalProperties           | <any-key>                                       | string              |
| settings                       | integration_jira                                | object              | Jira integration settings                              |
| integration_jira               | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_jira               | enabled                                         | boolean             | Whether Jira integration is enabled                    |
| integration_jira               | metadata                                        | object              |
| metadata                       | account_id                                      | string              |
| metadata                       | issue_type_id                                   | string              |
| metadata                       | project_id                                      | string              |
| integration_jira               | sync                                            | object              |
| sync                           | enabled                                         | boolean             |
| sync                           | properties                                      | object              |
| properties                     | assignee                                        | object              | Sync property configuration                            |
| assignee                       | sync_type                                       | string              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | custom_fields                                   | object              |
| additionalProperties           | <any-key>                                       | object              |
| <any-key>                      | sync_type                                       | string              |
| <any-key>                      | value                                           | object <oneOf> | Represents any valid JSON value.                       |
| value                          | Option 1                                        | string              |
| value                          | Option 2                                        | double              |
| value                          | Option 3                                        | object              |
| value                          | Option 4                                        | [ <oneOf>]     |
| Option 4                       | Option 1                                        | string              |
| Option 4                       | Option 2                                        | double              |
| Option 4                       | Option 3                                        | object              |
| Option 4                       | Option 4                                        | boolean             |
| value                          | Option 5                                        | boolean             |
| properties                     | description                                     | object              | Sync property configuration                            |
| description                    | sync_type                                       | string              |
| properties                     | due_date                                        | object              |
| due_date                       | jira_field_id                                   | string              |
| due_date                       | sync_type                                       | string              |
| properties                     | priority                                        | object              | Sync property with mapping configuration               |
| priority                       | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| properties                     | title                                           | object              | Sync property configuration                            |
| title                          | sync_type                                       | string              |
| settings                       | integration_monitor                             | object              | Monitor integration settings                           |
| integration_monitor            | auto_resolve_enabled                            | boolean             | Whether auto-resolve is enabled                        |
| integration_monitor            | case_type_id                                    | string              | Case type ID for monitor integration                   |
| integration_monitor            | enabled                                         | boolean             | Whether monitor integration is enabled                 |
| integration_monitor            | handle                                          | string              | Monitor handle                                         |
| settings                       | integration_on_call                             | object              | On-Call integration settings                           |
| integration_on_call            | auto_assign_on_call                             | boolean             | Whether to auto-assign on-call                         |
| integration_on_call            | enabled                                         | boolean             | Whether On-Call integration is enabled                 |
| integration_on_call            | escalation_queries                              | [object]            |
| escalation_queries             | enabled                                         | boolean             |
| escalation_queries             | id                                              | string              |
| escalation_queries             | query                                           | string              |
| escalation_queries             | target                                          | object              |
| target                         | dynamic_team_paging                             | boolean             |
| target                         | team_id                                         | string              |
| target                         | user_id                                         | string              |
| settings                       | integration_service_now                         | object              | ServiceNow integration settings                        |
| integration_service_now        | assignment_group                                | string              | Assignment group                                       |
| integration_service_now        | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_service_now        | enabled                                         | boolean             | Whether ServiceNow integration is enabled              |
| integration_service_now        | instance_name                                   | string              | ServiceNow instance name                               |
| integration_service_now        | sync_config                                     | object              |
| sync_config                    | enabled                                         | boolean             |
| sync_config                    | properties                                      | object              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | priority                                        | object              |
| priority                       | impact_mapping                                  | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| priority                       | urgency_mapping                                 | object              |
| additionalProperties           | <any-key>                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| settings                       | notification                                    | object              | Project notification settings                          |
| notification                   | destinations                                    | [integer]           | Notification destinations (1=email, 2=slack, 3=in-app) |
| notification                   | enabled                                         | boolean             | Whether notifications are enabled                      |
| notification                   | notify_on_case_assignment                       | boolean             |
| notification                   | notify_on_case_closed                           | boolean             |
| notification                   | notify_on_case_comment                          | boolean             |
| notification                   | notify_on_case_comment_mention                  | boolean             |
| notification                   | notify_on_case_priority_change                  | boolean             |
| notification                   | notify_on_case_status_change                    | boolean             |
| notification                   | notify_on_case_unassignment                     | boolean             |
| attributes                     | team_uuid                                       | string              | Team UUID to associate with the project                |
| data                           | type [*required*]                          | enum                | Project resource type Allowed enum values: `project`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "project",
    "attributes": {
      "name": "Updated Project Name Example-Case-Management"
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Project response

| Parent field                   | Field                                           | Type                | Description                                            |
| ------------------------------ | ----------------------------------------------- | ------------------- | ------------------------------------------------------ |
|                                | data                                            | object              | A Project                                              |
| data                           | attributes [*required*]                    | object              | Project attributes                                     |
| attributes                     | columns_config                                  | object              | Project columns configuration                          |
| columns_config                 | columns                                         | [object]            |
| columns                        | sort                                            | object              |
| sort                           | ascending                                       | boolean             |
| sort                           | priority                                        | int64               |
| columns                        | sort_field                                      | string              |
| columns                        | type                                            | string              |
| attributes                     | enabled_custom_case_types                       | [string]            | List of enabled custom case type IDs                   |
| attributes                     | key                                             | string              | The project's key                                      |
| attributes                     | name                                            | string              | Project's name                                         |
| attributes                     | restricted                                      | boolean             | Whether the project is restricted                      |
| attributes                     | settings                                        | object              | Project settings                                       |
| settings                       | auto_close_inactive_cases                       | object              | Auto-close inactive cases settings                     |
| auto_close_inactive_cases      | enabled                                         | boolean             | Whether auto-close is enabled                          |
| auto_close_inactive_cases      | max_inactive_time_in_secs                       | int64               | Maximum inactive time in seconds before auto-closing   |
| settings                       | auto_transition_assigned_cases                  | object              | Auto-transition assigned cases settings                |
| auto_transition_assigned_cases | auto_transition_assigned_cases_on_self_assigned | boolean             | Whether to auto-transition cases when self-assigned    |
| settings                       | integration_incident                            | object              | Incident integration settings                          |
| integration_incident           | auto_escalation_query                           | string              | Query for auto-escalation                              |
| integration_incident           | default_incident_commander                      | string              | Default incident commander                             |
| integration_incident           | enabled                                         | boolean             | Whether incident integration is enabled                |
| integration_incident           | field_mappings                                  | [object]            |
| field_mappings                 | case_field                                      | string              |
| field_mappings                 | incident_user_defined_field_id                  | string              |
| integration_incident           | incident_type                                   | string              | Incident type                                          |
| integration_incident           | severity_config                                 | object              |
| severity_config                | priority_mapping                                | object              |
| additionalProperties           | <any-key>                                       | string              |
| settings                       | integration_jira                                | object              | Jira integration settings                              |
| integration_jira               | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_jira               | enabled                                         | boolean             | Whether Jira integration is enabled                    |
| integration_jira               | metadata                                        | object              |
| metadata                       | account_id                                      | string              |
| metadata                       | issue_type_id                                   | string              |
| metadata                       | project_id                                      | string              |
| integration_jira               | sync                                            | object              |
| sync                           | enabled                                         | boolean             |
| sync                           | properties                                      | object              |
| properties                     | assignee                                        | object              | Sync property configuration                            |
| assignee                       | sync_type                                       | string              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | custom_fields                                   | object              |
| additionalProperties           | <any-key>                                       | object              |
| <any-key>                      | sync_type                                       | string              |
| <any-key>                      | value                                           | object <oneOf> | Represents any valid JSON value.                       |
| value                          | Option 1                                        | string              |
| value                          | Option 2                                        | double              |
| value                          | Option 3                                        | object              |
| value                          | Option 4                                        | [ <oneOf>]     |
| Option 4                       | Option 1                                        | string              |
| Option 4                       | Option 2                                        | double              |
| Option 4                       | Option 3                                        | object              |
| Option 4                       | Option 4                                        | boolean             |
| value                          | Option 5                                        | boolean             |
| properties                     | description                                     | object              | Sync property configuration                            |
| description                    | sync_type                                       | string              |
| properties                     | due_date                                        | object              |
| due_date                       | jira_field_id                                   | string              |
| due_date                       | sync_type                                       | string              |
| properties                     | priority                                        | object              | Sync property with mapping configuration               |
| priority                       | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| properties                     | title                                           | object              | Sync property configuration                            |
| title                          | sync_type                                       | string              |
| settings                       | integration_monitor                             | object              | Monitor integration settings                           |
| integration_monitor            | auto_resolve_enabled                            | boolean             | Whether auto-resolve is enabled                        |
| integration_monitor            | case_type_id                                    | string              | Case type ID for monitor integration                   |
| integration_monitor            | enabled                                         | boolean             | Whether monitor integration is enabled                 |
| integration_monitor            | handle                                          | string              | Monitor handle                                         |
| settings                       | integration_on_call                             | object              | On-Call integration settings                           |
| integration_on_call            | auto_assign_on_call                             | boolean             | Whether to auto-assign on-call                         |
| integration_on_call            | enabled                                         | boolean             | Whether On-Call integration is enabled                 |
| integration_on_call            | escalation_queries                              | [object]            |
| escalation_queries             | enabled                                         | boolean             |
| escalation_queries             | id                                              | string              |
| escalation_queries             | query                                           | string              |
| escalation_queries             | target                                          | object              |
| target                         | dynamic_team_paging                             | boolean             |
| target                         | team_id                                         | string              |
| target                         | user_id                                         | string              |
| settings                       | integration_service_now                         | object              | ServiceNow integration settings                        |
| integration_service_now        | assignment_group                                | string              | Assignment group                                       |
| integration_service_now        | auto_creation                                   | object              |
| auto_creation                  | enabled                                         | boolean             |
| integration_service_now        | enabled                                         | boolean             | Whether ServiceNow integration is enabled              |
| integration_service_now        | instance_name                                   | string              | ServiceNow instance name                               |
| integration_service_now        | sync_config                                     | object              |
| sync_config                    | enabled                                         | boolean             |
| sync_config                    | properties                                      | object              |
| properties                     | comments                                        | object              | Sync property configuration                            |
| comments                       | sync_type                                       | string              |
| properties                     | priority                                        | object              |
| priority                       | impact_mapping                                  | object              |
| additionalProperties           | <any-key>                                       | string              |
| priority                       | sync_type                                       | string              |
| priority                       | urgency_mapping                                 | object              |
| additionalProperties           | <any-key>                                       | string              |
| properties                     | status                                          | object              | Sync property with mapping configuration               |
| status                         | mapping                                         | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | name_mapping                                    | object              |
| additionalProperties           | <any-key>                                       | string              |
| status                         | sync_type                                       | string              |
| settings                       | notification                                    | object              | Project notification settings                          |
| notification                   | destinations                                    | [integer]           | Notification destinations (1=email, 2=slack, 3=in-app) |
| notification                   | enabled                                         | boolean             | Whether notifications are enabled                      |
| notification                   | notify_on_case_assignment                       | boolean             |
| notification                   | notify_on_case_closed                           | boolean             |
| notification                   | notify_on_case_comment                          | boolean             |
| notification                   | notify_on_case_comment_mention                  | boolean             |
| notification                   | notify_on_case_priority_change                  | boolean             |
| notification                   | notify_on_case_status_change                    | boolean             |
| notification                   | notify_on_case_unassignment                     | boolean             |
| data                           | id [*required*]                            | string              | The Project's identifier                               |
| data                           | relationships                                   | object              | Project relationships                                  |
| relationships                  | member_team                                     | object              | Relationship between a team and a team link            |
| member_team                    | data                                            | [object]            | Related team links                                     |
| data                           | id [*required*]                            | string              | The team link's identifier                             |
| data                           | type [*required*]                          | enum                | Team link type Allowed enum values: `team_links`       |
| member_team                    | links                                           | object              | Links attributes.                                      |
| links                          | related                                         | string              | Related link.                                          |
| relationships                  | member_user                                     | object              | Relationship to users.                                 |
| member_user                    | data [*required*]                          | [object]            | Relationships to user objects.                         |
| data                           | id [*required*]                            | string              | A unique identifier that represents the user.          |
| data                           | type [*required*]                          | enum                | User resource type. Allowed enum values: `user`        |
| data                           | type [*required*]                          | enum                | Project resource type Allowed enum values: `project`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "columns_config": {
        "columns": [
          {
            "sort": {
              "ascending": false,
              "priority": "integer"
            },
            "sort_field": "string",
            "type": "string"
          }
        ]
      },
      "enabled_custom_case_types": [],
      "key": "CASEM",
      "name": "Security Investigation",
      "restricted": false,
      "settings": {
        "auto_close_inactive_cases": {
          "enabled": false,
          "max_inactive_time_in_secs": "integer"
        },
        "auto_transition_assigned_cases": {
          "auto_transition_assigned_cases_on_self_assigned": false
        },
        "integration_incident": {
          "auto_escalation_query": "string",
          "default_incident_commander": "string",
          "enabled": false,
          "field_mappings": [
            {
              "case_field": "string",
              "incident_user_defined_field_id": "string"
            }
          ],
          "incident_type": "string",
          "severity_config": {
            "priority_mapping": {
              "<any-key>": "string"
            }
          }
        },
        "integration_jira": {
          "auto_creation": {
            "enabled": false
          },
          "enabled": false,
          "metadata": {
            "account_id": "string",
            "issue_type_id": "string",
            "project_id": "string"
          },
          "sync": {
            "enabled": false,
            "properties": {
              "assignee": {
                "sync_type": "string"
              },
              "comments": {
                "sync_type": "string"
              },
              "custom_fields": {
                "<any-key>": {
                  "sync_type": "string",
                  "value": {
                    "type": "undefined"
                  }
                }
              },
              "description": {
                "sync_type": "string"
              },
              "due_date": {
                "jira_field_id": "string",
                "sync_type": "string"
              },
              "priority": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              },
              "status": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              },
              "title": {
                "sync_type": "string"
              }
            }
          }
        },
        "integration_monitor": {
          "auto_resolve_enabled": false,
          "case_type_id": "string",
          "enabled": false,
          "handle": "string"
        },
        "integration_on_call": {
          "auto_assign_on_call": false,
          "enabled": false,
          "escalation_queries": [
            {
              "enabled": false,
              "id": "string",
              "query": "string",
              "target": {
                "dynamic_team_paging": false,
                "team_id": "string",
                "user_id": "string"
              }
            }
          ]
        },
        "integration_service_now": {
          "assignment_group": "string",
          "auto_creation": {
            "enabled": false
          },
          "enabled": false,
          "instance_name": "string",
          "sync_config": {
            "enabled": false,
            "properties": {
              "comments": {
                "sync_type": "string"
              },
              "priority": {
                "impact_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string",
                "urgency_mapping": {
                  "<any-key>": "string"
                }
              },
              "status": {
                "mapping": {
                  "<any-key>": "string"
                },
                "name_mapping": {
                  "<any-key>": "string"
                },
                "sync_type": "string"
              }
            }
          }
        },
        "notification": {
          "destinations": [],
          "enabled": false,
          "notify_on_case_assignment": false,
          "notify_on_case_closed": false,
          "notify_on_case_comment": false,
          "notify_on_case_comment_mention": false,
          "notify_on_case_priority_change": false,
          "notify_on_case_status_change": false,
          "notify_on_case_unassignment": false
        }
      }
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
                          \# Path parametersexport project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/projects/${project_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "project",
    "attributes": {
      "name": "Updated Project Name Example-Case-Management"
    }
  }
}
EOF
                        
##### 

```go
// Update a project returns "OK" response

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
	body := datadogV2.ProjectUpdateRequest{
		Data: datadogV2.ProjectUpdate{
			Type: datadogV2.PROJECTRESOURCETYPE_PROJECT,
			Attributes: &datadogV2.ProjectUpdateAttributes{
				Name: datadog.PtrString("Updated Project Name Example-Case-Management"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.UpdateProject(ctx, "d4bbe1af-f36e-42f1-87c1-493ca35c320e", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UpdateProject`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.UpdateProject`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update a project returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.ProjectResourceType;
import com.datadog.api.client.v2.model.ProjectResponse;
import com.datadog.api.client.v2.model.ProjectUpdate;
import com.datadog.api.client.v2.model.ProjectUpdateAttributes;
import com.datadog.api.client.v2.model.ProjectUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    ProjectUpdateRequest body =
        new ProjectUpdateRequest()
            .data(
                new ProjectUpdate()
                    .type(ProjectResourceType.PROJECT)
                    .attributes(
                        new ProjectUpdateAttributes()
                            .name("Updated Project Name Example-Case-Management")));

    try {
      ProjectResponse result =
          apiInstance.updateProject("d4bbe1af-f36e-42f1-87c1-493ca35c320e", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#updateProject");
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
Update a project returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType
from datadog_api_client.v2.model.project_update import ProjectUpdate
from datadog_api_client.v2.model.project_update_attributes import ProjectUpdateAttributes
from datadog_api_client.v2.model.project_update_request import ProjectUpdateRequest

body = ProjectUpdateRequest(
    data=ProjectUpdate(
        type=ProjectResourceType.PROJECT,
        attributes=ProjectUpdateAttributes(
            name="Updated Project Name Example-Case-Management",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_project(project_id="d4bbe1af-f36e-42f1-87c1-493ca35c320e", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update a project returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::ProjectUpdateRequest.new({
  data: DatadogAPIClient::V2::ProjectUpdate.new({
    type: DatadogAPIClient::V2::ProjectResourceType::PROJECT,
    attributes: DatadogAPIClient::V2::ProjectUpdateAttributes.new({
      name: "Updated Project Name Example-Case-Management",
    }),
  }),
})
p api_instance.update_project("d4bbe1af-f36e-42f1-87c1-493ca35c320e", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update a project returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::ProjectResourceType;
use datadog_api_client::datadogV2::model::ProjectUpdate;
use datadog_api_client::datadogV2::model::ProjectUpdateAttributes;
use datadog_api_client::datadogV2::model::ProjectUpdateRequest;

#[tokio::main]
async fn main() {
    let body = ProjectUpdateRequest::new(
        ProjectUpdate::new(ProjectResourceType::PROJECT).attributes(
            ProjectUpdateAttributes::new()
                .name("Updated Project Name Example-Case-Management".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .update_project("d4bbe1af-f36e-42f1-87c1-493ca35c320e".to_string(), body)
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
 * Update a project returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiUpdateProjectRequest = {
  body: {
    data: {
      type: "project",
      attributes: {
        name: "Updated Project Name Example-Case-Management",
      },
    },
  },
  projectId: "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
};

apiInstance
  .updateProject(params)
  .then((data: v2.ProjectResponse) => {
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

## Update case priority{% #update-case-priority %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/priority |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/priority |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/priority      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/priority      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/priority     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/priority |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/priority |

### Overview

Update case priority

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Case priority update payload

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                     |
| ------------ | ---------------------------- | ------ | --------------------------------------------------------------- |
|              | data [*required*]       | object | Case priority status                                            |
| data         | attributes [*required*] | object | Case update priority attributes                                 |
| attributes   | priority [*required*]   | enum   | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5` |
| data         | type [*required*]       | enum   | Case resource type Allowed enum values: `case`                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "priority": "P3"
    },
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/priority" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Assign case{% #assign-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/assign |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/assign |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/assign      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/assign      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/assign     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/assign |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/assign |

### Overview

Assign case to a user

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Assign case payload

{% tab title="Model" %}

| Parent field | Field                         | Type   | Description                                    |
| ------------ | ----------------------------- | ------ | ---------------------------------------------- |
|              | data [*required*]        | object | Case assign                                    |
| data         | attributes [*required*]  | object | Case assign attributes                         |
| attributes   | assignee_id [*required*] | string | Assignee's UUID                                |
| data         | type [*required*]        | enum   | Case resource type Allowed enum values: `case` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignee_id": "string"
    },
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/assign" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Unassign case{% #unassign-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/unassign |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/unassign |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/unassign      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/unassign      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/unassign     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/unassign |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/unassign |

### Overview

Unassign case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Unassign case payload

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                    |
| ------------ | ---------------------- | ------ | ---------------------------------------------- |
|              | data [*required*] | object | Case empty request data                        |
| data         | type [*required*] | enum   | Case resource type Allowed enum values: `case` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/unassign" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Archive case{% #archive-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/archive |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/archive |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/archive      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/archive      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/archive     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/archive |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/archive |

### Overview

Archive case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Archive case payload

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                    |
| ------------ | ---------------------- | ------ | ---------------------------------------------- |
|              | data [*required*] | object | Case empty request data                        |
| data         | type [*required*] | enum   | Case resource type Allowed enum values: `case` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/archive" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Unarchive case{% #unarchive-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/unarchive |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/unarchive |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/unarchive      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/unarchive      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/unarchive     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/unarchive |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/unarchive |

### Overview

Unarchive case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Unarchive case payload

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                    |
| ------------ | ---------------------- | ------ | ---------------------------------------------- |
|              | data [*required*] | object | Case empty request data                        |
| data         | type [*required*] | enum   | Case resource type Allowed enum values: `case` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/unarchive" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update case attributes{% #update-case-attributes %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/attributes |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/attributes |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/attributes      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/attributes      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/attributes     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/attributes |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/attributes |

### Overview

Update case attributes

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Case attributes update payload

{% tab title="Model" %}

| Parent field         | Field                        | Type     | Description                                      |
| -------------------- | ---------------------------- | -------- | ------------------------------------------------ |
|                      | data [*required*]       | object   | Case update attributes                           |
| data                 | attributes [*required*] | object   | Case update attributes attributes                |
| attributes           | attributes [*required*] | object   | The definition of `CaseObjectAttributes` object. |
| additionalProperties | <any-key>                    | [string] |
| data                 | type [*required*]       | enum     | Case resource type Allowed enum values: `case`   |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/attributes" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Comment case{% #comment-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/comment |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/comment |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/comment      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/comment      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/comment     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/comment |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/comment |

### Overview

Comment case

### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Case comment payload

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                    |
| ------------ | ---------------------------- | ------ | ---------------------------------------------- |
|              | data [*required*]       | object | Case comment                                   |
| data         | attributes [*required*] | object | Case comment attributes                        |
| attributes   | comment [*required*]    | string | The `CaseCommentAttributes` `message`.         |
| data         | type [*required*]       | enum   | Case resource type Allowed enum values: `case` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "comment": "Hello World !"
    },
    "type": "case"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Timeline response

| Parent field | Field                        | Type          | Description                                                               |
| ------------ | ---------------------------- | ------------- | ------------------------------------------------------------------------- |
|              | data                         | [object]      | The `TimelineResponse` `data`.                                            |
| data         | attributes [*required*] | object        | timeline cell                                                             |
| attributes   | author                       |  <oneOf> | author of the timeline cell                                               |
| author       | Option 1                     | object        | timeline cell user author                                                 |
| Option 1     | content                      | object        | user author content.                                                      |
| content      | email                        | string        | user email                                                                |
| content      | handle                       | string        | user handle                                                               |
| content      | id                           | string        | user UUID                                                                 |
| content      | name                         | string        | user name                                                                 |
| Option 1     | type                         | enum          | user author type. Allowed enum values: `USER`                             |
| attributes   | cell_content                 |  <oneOf> | timeline cell content                                                     |
| cell_content | Option 1                     | object        | comment content                                                           |
| Option 1     | message                      | string        | comment message                                                           |
| attributes   | created_at                   | date-time     | Timestamp of when the cell was created                                    |
| attributes   | deleted_at                   | date-time     | Timestamp of when the cell was deleted                                    |
| attributes   | modified_at                  | date-time     | Timestamp of when the cell was last modified                              |
| attributes   | type                         | enum          | Timeline cell content type Allowed enum values: `COMMENT`                 |
| data         | id [*required*]         | string        | Timeline cell's identifier                                                |
| data         | type [*required*]       | enum          | Timeline cell JSON:API resource type Allowed enum values: `timeline_cell` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/comment" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete case comment{% #delete-case-comment %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cases/{case_id}/comment/{cell_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cases/{case_id}/comment/{cell_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cases/{case_id}/comment/{cell_id} |

### Overview

Delete case comment

### Arguments

#### Path Parameters

| Name                      | Type   | Description          |
| ------------------------- | ------ | -------------------- |
| case_id [*required*] | string | Case's UUID or key   |
| cell_id [*required*] | string | Timeline cell's UUID |

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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"export cell_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/comment/${cell_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete case comment returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" in the system
CASE_ID = ENV["CASE_ID"]

# there is a valid "comment" in the system
COMMENT_ID = ENV["COMMENT_ID"]
api_instance.delete_case_comment(CASE_ID, COMMENT_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update case custom attribute{% #update-case-custom-attribute %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |

### Overview

Update case custom attribute

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                                   | Type   | Description                 |
| -------------------------------------- | ------ | --------------------------- |
| case_id [*required*]              | string | Case's UUID or key          |
| custom_attribute_key [*required*] | string | Case Custom attribute's key |

### Request

#### Body Data (required)

Update case custom attribute payload

{% tab title="Model" %}

| Parent field | Field                        | Type          | Description                                                          |
| ------------ | ---------------------------- | ------------- | -------------------------------------------------------------------- |
|              | data [*required*]       | object        | Case update custom attribute                                         |
| data         | attributes [*required*] | object        | Custom attribute values                                              |
| attributes   | is_multi [*required*]   | boolean       | If true, value must be an array                                      |
| attributes   | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT` |
| attributes   | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                      |
| value        | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                     |
| value        | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute               |
| value        | Option 3                     | double        | Value of NUMBER custom attribute                                     |
| value        | Option 4                     | [number]      | Values of multi NUMBER custom attribute                              |
| data         | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                       |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"export custom_attribute_key="aws_region"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/custom_attributes/${custom_attribute_key}" \
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
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete custom attribute from case{% #delete-custom-attribute-from-case %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key} |

### Overview

Delete custom attribute from case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                                   | Type   | Description                 |
| -------------------------------------- | ------ | --------------------------- |
| case_id [*required*]              | string | Case's UUID or key          |
| custom_attribute_key [*required*] | string | Case Custom attribute's key |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"export custom_attribute_key="aws_region"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/custom_attributes/${custom_attribute_key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete custom attribute from case returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

# there is a valid "case" with a custom "case_type" in the system
CASE_WITH_TYPE_ID = ENV["CASE_WITH_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = ENV["CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY"]
p api_instance.delete_case_custom_attribute(CASE_WITH_TYPE_ID, CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update case project{% #update-case-project %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/relationships/project |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/relationships/project |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/cases/{case_id}/relationships/project      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/cases/{case_id}/relationships/project      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/cases/{case_id}/relationships/project     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/cases/{case_id}/relationships/project |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/cases/{case_id}/relationships/project |

### Overview

Update the project associated with a case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Project update request

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                          |
| ------------ | ---------------------- | ------ | ---------------------------------------------------- |
|              | data [*required*] | object | Relationship to project object                       |
| data         | id [*required*]   | string | A unique identifier that represents the project      |
| data         | type [*required*] | enum   | Project resource type Allowed enum values: `project` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "e555e290-ed65-49bd-ae18-8acbfcf18db7",
    "type": "project"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/relationships/project" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "e555e290-ed65-49bd-ae18-8acbfcf18db7",
    "type": "project"
  }
}
EOF
                
##### 

```python
"""
Update case project returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.project_relationship import ProjectRelationship
from datadog_api_client.v2.model.project_relationship_data import ProjectRelationshipData
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType

body = ProjectRelationship(
    data=ProjectRelationshipData(
        id="e555e290-ed65-49bd-ae18-8acbfcf18db7",
        type=ProjectResourceType.PROJECT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["move_case_to_project"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.move_case_to_project(case_id="case_id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update case project returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.move_case_to_project".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::ProjectRelationship.new({
  data: DatadogAPIClient::V2::ProjectRelationshipData.new({
    id: "e555e290-ed65-49bd-ae18-8acbfcf18db7",
    type: DatadogAPIClient::V2::ProjectResourceType::PROJECT,
  }),
})
p api_instance.move_case_to_project("case_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Update case project returns "OK" response

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
	body := datadogV2.ProjectRelationship{
		Data: datadogV2.ProjectRelationshipData{
			Id:   "e555e290-ed65-49bd-ae18-8acbfcf18db7",
			Type: datadogV2.PROJECTRESOURCETYPE_PROJECT,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.MoveCaseToProject", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.MoveCaseToProject(ctx, "case_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.MoveCaseToProject`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.MoveCaseToProject`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update case project returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.ProjectRelationship;
import com.datadog.api.client.v2.model.ProjectRelationshipData;
import com.datadog.api.client.v2.model.ProjectResourceType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.moveCaseToProject", true);
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    ProjectRelationship body =
        new ProjectRelationship()
            .data(
                new ProjectRelationshipData()
                    .id("e555e290-ed65-49bd-ae18-8acbfcf18db7")
                    .type(ProjectResourceType.PROJECT));

    try {
      CaseResponse result =
          apiInstance.moveCaseToProject("f98a5a5b-e0ff-45d4-b2f5-afe6e74de504", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#moveCaseToProject");
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
// Update case project returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::ProjectRelationship;
use datadog_api_client::datadogV2::model::ProjectRelationshipData;
use datadog_api_client::datadogV2::model::ProjectResourceType;

#[tokio::main]
async fn main() {
    let body = ProjectRelationship::new(ProjectRelationshipData::new(
        "e555e290-ed65-49bd-ae18-8acbfcf18db7".to_string(),
        ProjectResourceType::PROJECT,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.MoveCaseToProject", true);
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.move_case_to_project("case_id".to_string(), body).await;
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
 * Update case project returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.moveCaseToProject"] = true;
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiMoveCaseToProjectRequest = {
  body: {
    data: {
      id: "e555e290-ed65-49bd-ae18-8acbfcf18db7",
      type: "project",
    },
  },
  caseId: "case_id",
};

apiInstance
  .moveCaseToProject(params)
  .then((data: v2.CaseResponse) => {
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

## Link incident to case{% #link-incident-to-case %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/relationships/incidents |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/relationships/incidents |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/relationships/incidents      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/relationships/incidents      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/relationships/incidents     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/relationships/incidents |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/relationships/incidents |

### Overview

Link an incident to a case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Incident link request

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                             |
| ------------ | ---------------------- | ------ | ------------------------------------------------------- |
|              | data [*required*] | object | Incident relationship data                              |
| data         | id [*required*]   | string | Incident identifier                                     |
| data         | type [*required*] | enum   | Incident resource type Allowed enum values: `incidents` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "incidents"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Case response

| Parent field         | Field                        | Type          | Description                                                                                                                                                                                           |
| -------------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                         | object        | A case                                                                                                                                                                                                |
| data                 | attributes [*required*] | object        | Case resource attributes                                                                                                                                                                              |
| attributes           | archived_at                  | date-time     | Timestamp of when the case was archived                                                                                                                                                               |
| attributes           | attributes                   | object        | The definition of `CaseObjectAttributes` object.                                                                                                                                                      |
| additionalProperties | <any-key>                    | [string]      |
| attributes           | closed_at                    | date-time     | Timestamp of when the case was closed                                                                                                                                                                 |
| attributes           | created_at                   | date-time     | Timestamp of when the case was created                                                                                                                                                                |
| attributes           | custom_attributes            | object        | Case custom attributes                                                                                                                                                                                |
| additionalProperties | <any-key>                    | object        | Custom attribute values                                                                                                                                                                               |
| <any-key>            | is_multi [*required*]   | boolean       | If true, value must be an array                                                                                                                                                                       |
| <any-key>            | type [*required*]       | enum          | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                                                                                                                                  |
| <any-key>            | value [*required*]      |  <oneOf> | Union of supported value for a custom attribute                                                                                                                                                       |
| value                | Option 1                     | string        | Value of TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                      |
| value                | Option 2                     | [string]      | Value of multi TEXT/URL/NUMBER/SELECT custom attribute                                                                                                                                                |
| value                | Option 3                     | double        | Value of NUMBER custom attribute                                                                                                                                                                      |
| value                | Option 4                     | [number]      | Values of multi NUMBER custom attribute                                                                                                                                                               |
| attributes           | description                  | string        | Description                                                                                                                                                                                           |
| attributes           | jira_issue                   | object        | Jira issue attached to case                                                                                                                                                                           |
| jira_issue           | result                       | object        | Jira issue information                                                                                                                                                                                |
| result               | issue_id                     | string        | Jira issue ID                                                                                                                                                                                         |
| result               | issue_key                    | string        | Jira issue key                                                                                                                                                                                        |
| result               | issue_url                    | string        | Jira issue URL                                                                                                                                                                                        |
| result               | project_key                  | string        | Jira project key                                                                                                                                                                                      |
| jira_issue           | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | key                          | string        | Key                                                                                                                                                                                                   |
| attributes           | modified_at                  | date-time     | Timestamp of when the case was last modified                                                                                                                                                          |
| attributes           | priority                     | enum          | Case priority Allowed enum values: `NOT_DEFINED,P1,P2,P3,P4,P5`                                                                                                                                       |
| attributes           | service_now_ticket           | object        | ServiceNow ticket attached to case                                                                                                                                                                    |
| service_now_ticket   | result                       | object        | ServiceNow ticket information                                                                                                                                                                         |
| result               | sys_target_link              | string        | Link to the Incident created on ServiceNow                                                                                                                                                            |
| service_now_ticket   | status                       | enum          | Case status Allowed enum values: `IN_PROGRESS,COMPLETED,FAILED`                                                                                                                                       |
| attributes           | status                       | enum          | **DEPRECATED**: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use `status_name` instead. Allowed enum values: `OPEN,IN_PROGRESS,CLOSED` |
| attributes           | status_group                 | enum          | Status group of the case. Allowed enum values: `SG_OPEN,SG_IN_PROGRESS,SG_CLOSED`                                                                                                                     |
| attributes           | status_name                  | string        | Status of the case. Must be one of the existing statuses for the case's type.                                                                                                                         |
| attributes           | title                        | string        | Title                                                                                                                                                                                                 |
| attributes           | type                         | enum          | **DEPRECATED**: Case type Allowed enum values: `STANDARD`                                                                                                                                             |
| attributes           | type_id                      | string        | Case type UUID                                                                                                                                                                                        |
| data                 | id [*required*]         | string        | Case's identifier                                                                                                                                                                                     |
| data                 | relationships                | object        | Resources related to a case                                                                                                                                                                           |
| relationships        | assignee                     | object        | Relationship to user.                                                                                                                                                                                 |
| assignee             | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | created_by                   | object        | Relationship to user.                                                                                                                                                                                 |
| created_by           | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | modified_by                  | object        | Relationship to user.                                                                                                                                                                                 |
| modified_by          | data [*required*]       | object        | Relationship to user object.                                                                                                                                                                          |
| data                 | id [*required*]         | string        | A unique identifier that represents the user.                                                                                                                                                         |
| data                 | type [*required*]       | enum          | User resource type. Allowed enum values: `user`                                                                                                                                                       |
| relationships        | project                      | object        | Relationship to project                                                                                                                                                                               |
| project              | data [*required*]       | object        | Relationship to project object                                                                                                                                                                        |
| data                 | id [*required*]         | string        | A unique identifier that represents the project                                                                                                                                                       |
| data                 | type [*required*]       | enum          | Project resource type Allowed enum values: `project`                                                                                                                                                  |
| data                 | type [*required*]       | enum          | Case resource type Allowed enum values: `case`                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
      "status_group": "SG_OPEN",
      "status_name": "Open",
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/relationships/incidents" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "incidents"
  }
}
EOF
                
##### 

```python
"""
Link incident to case returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.incident_relationship_data import IncidentRelationshipData
from datadog_api_client.v2.model.incident_resource_type import IncidentResourceType
from datadog_api_client.v2.model.relationship_to_incident_request import RelationshipToIncidentRequest

body = RelationshipToIncidentRequest(
    data=IncidentRelationshipData(
        id="00000000-0000-0000-0000-000000000000",
        type=IncidentResourceType.INCIDENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["link_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.link_incident(case_id="case_id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Link incident to case returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.link_incident".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::RelationshipToIncidentRequest.new({
  data: DatadogAPIClient::V2::IncidentRelationshipData.new({
    id: "00000000-0000-0000-0000-000000000000",
    type: DatadogAPIClient::V2::IncidentResourceType::INCIDENTS,
  }),
})
p api_instance.link_incident("case_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Link incident to case returns "Created" response

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
	body := datadogV2.RelationshipToIncidentRequest{
		Data: datadogV2.IncidentRelationshipData{
			Id:   "00000000-0000-0000-0000-000000000000",
			Type: datadogV2.INCIDENTRESOURCETYPE_INCIDENTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.LinkIncident", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	resp, r, err := api.LinkIncident(ctx, "case_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.LinkIncident`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementApi.LinkIncident`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Link incident to case returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.CaseResponse;
import com.datadog.api.client.v2.model.IncidentRelationshipData;
import com.datadog.api.client.v2.model.IncidentResourceType;
import com.datadog.api.client.v2.model.RelationshipToIncidentRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.linkIncident", true);
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    RelationshipToIncidentRequest body =
        new RelationshipToIncidentRequest()
            .data(
                new IncidentRelationshipData()
                    .id("00000000-0000-0000-0000-000000000000")
                    .type(IncidentResourceType.INCIDENTS));

    try {
      CaseResponse result = apiInstance.linkIncident("f98a5a5b-e0ff-45d4-b2f5-afe6e74de504", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#linkIncident");
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
// Link incident to case returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::IncidentRelationshipData;
use datadog_api_client::datadogV2::model::IncidentResourceType;
use datadog_api_client::datadogV2::model::RelationshipToIncidentRequest;

#[tokio::main]
async fn main() {
    let body = RelationshipToIncidentRequest::new(IncidentRelationshipData::new(
        "00000000-0000-0000-0000-000000000000".to_string(),
        IncidentResourceType::INCIDENTS,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.LinkIncident", true);
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.link_incident("case_id".to_string(), body).await;
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
 * Link incident to case returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.linkIncident"] = true;
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiLinkIncidentRequest = {
  body: {
    data: {
      id: "00000000-0000-0000-0000-000000000000",
      type: "incidents",
    },
  },
  caseId: "case_id",
};

apiInstance
  .linkIncident(params)
  .then((data: v2.CaseResponse) => {
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

## Create Jira issue for case{% #create-jira-issue-for-case %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/relationships/jira_issues      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/relationships/jira_issues      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |

### Overview

Create a new Jira issue and link it to a case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Jira issue creation request

{% tab title="Model" %}

| Parent field | Field                             | Type   | Description                                            |
| ------------ | --------------------------------- | ------ | ------------------------------------------------------ |
|              | data [*required*]            | object | Jira issue creation data                               |
| data         | attributes [*required*]      | object | Jira issue creation attributes                         |
| attributes   | fields                            | object | Additional Jira fields                                 |
| attributes   | issue_type_id [*required*]   | string | Jira issue type ID                                     |
| attributes   | jira_account_id [*required*] | string | Jira account ID                                        |
| attributes   | project_id [*required*]      | string | Jira project ID                                        |
| data         | type [*required*]            | enum   | Jira issue resource type Allowed enum values: `issues` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {},
      "issue_type_id": "10001",
      "jira_account_id": "1234",
      "project_id": "5678"
    },
    "type": "issues"
  }
}
```

{% /tab %}

### Response

{% tab title="202" %}
Accepted
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/relationships/jira_issues" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "issue_type_id": "10001",
      "jira_account_id": "1234",
      "project_id": "5678"
    },
    "type": "issues"
  }
}
EOF
                
##### 

```python
"""
Create Jira issue for case returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.jira_issue_create_attributes import JiraIssueCreateAttributes
from datadog_api_client.v2.model.jira_issue_create_data import JiraIssueCreateData
from datadog_api_client.v2.model.jira_issue_create_request import JiraIssueCreateRequest
from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType

body = JiraIssueCreateRequest(
    data=JiraIssueCreateData(
        attributes=JiraIssueCreateAttributes(
            fields=dict(),
            issue_type_id="10001",
            jira_account_id="1234",
            project_id="5678",
        ),
        type=JiraIssueResourceType.ISSUES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_jira_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.create_case_jira_issue(case_id="case_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create Jira issue for case returns "Accepted" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_case_jira_issue".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::JiraIssueCreateRequest.new({
  data: DatadogAPIClient::V2::JiraIssueCreateData.new({
    attributes: DatadogAPIClient::V2::JiraIssueCreateAttributes.new({
      fields: {},
      issue_type_id: "10001",
      jira_account_id: "1234",
      project_id: "5678",
    }),
    type: DatadogAPIClient::V2::JiraIssueResourceType::ISSUES,
  }),
})
p api_instance.create_case_jira_issue("case_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create Jira issue for case returns "Accepted" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.JiraIssueCreateRequest{
		Data: datadogV2.JiraIssueCreateData{
			Attributes: datadogV2.JiraIssueCreateAttributes{
				Fields:        map[string]interface{}{},
				IssueTypeId:   "10001",
				JiraAccountId: "1234",
				ProjectId:     "5678",
			},
			Type: datadogV2.JIRAISSUERESOURCETYPE_ISSUES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateCaseJiraIssue", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.CreateCaseJiraIssue(ctx, "case_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.CreateCaseJiraIssue`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create Jira issue for case returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.JiraIssueCreateAttributes;
import com.datadog.api.client.v2.model.JiraIssueCreateData;
import com.datadog.api.client.v2.model.JiraIssueCreateRequest;
import com.datadog.api.client.v2.model.JiraIssueResourceType;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createCaseJiraIssue", true);
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    JiraIssueCreateRequest body =
        new JiraIssueCreateRequest()
            .data(
                new JiraIssueCreateData()
                    .attributes(
                        new JiraIssueCreateAttributes()
                            .fields(Map.ofEntries())
                            .issueTypeId("10001")
                            .jiraAccountId("1234")
                            .projectId("5678"))
                    .type(JiraIssueResourceType.ISSUES));

    try {
      apiInstance.createCaseJiraIssue("f98a5a5b-e0ff-45d4-b2f5-afe6e74de504", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#createCaseJiraIssue");
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
// Create Jira issue for case returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::JiraIssueCreateAttributes;
use datadog_api_client::datadogV2::model::JiraIssueCreateData;
use datadog_api_client::datadogV2::model::JiraIssueCreateRequest;
use datadog_api_client::datadogV2::model::JiraIssueResourceType;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = JiraIssueCreateRequest::new(JiraIssueCreateData::new(
        JiraIssueCreateAttributes::new("10001".to_string(), "1234".to_string(), "5678".to_string())
            .fields(BTreeMap::from([])),
        JiraIssueResourceType::ISSUES,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateCaseJiraIssue", true);
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .create_case_jira_issue("case_id".to_string(), body)
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
 * Create Jira issue for case returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createCaseJiraIssue"] = true;
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiCreateCaseJiraIssueRequest = {
  body: {
    data: {
      attributes: {
        fields: {},
        issueTypeId: "10001",
        jiraAccountId: "1234",
        projectId: "5678",
      },
      type: "issues",
    },
  },
  caseId: "case_id",
};

apiInstance
  .createCaseJiraIssue(params)
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

## Link existing Jira issue to case{% #link-existing-jira-issue-to-case %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/cases/{case_id}/relationships/jira_issues      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/cases/{case_id}/relationships/jira_issues      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |

### Overview

Link an existing Jira issue to a case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Jira issue link request

{% tab title="Model" %}

| Parent field | Field                            | Type   | Description                                            |
| ------------ | -------------------------------- | ------ | ------------------------------------------------------ |
|              | data [*required*]           | object | Jira issue link data                                   |
| data         | attributes [*required*]     | object | Jira issue link attributes                             |
| attributes   | jira_issue_url [*required*] | string | URL of the Jira issue                                  |
| data         | type [*required*]           | enum   | Jira issue resource type Allowed enum values: `issues` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "jira_issue_url": "https://jira.example.com/browse/PROJ-123"
    },
    "type": "issues"
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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

{% tab title="409" %}
Conflict
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/relationships/jira_issues" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "jira_issue_url": "https://jira.example.com/browse/PROJ-123"
    },
    "type": "issues"
  }
}
EOF
                
##### 

```python
"""
Link existing Jira issue to case returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.jira_issue_link_attributes import JiraIssueLinkAttributes
from datadog_api_client.v2.model.jira_issue_link_data import JiraIssueLinkData
from datadog_api_client.v2.model.jira_issue_link_request import JiraIssueLinkRequest
from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType

body = JiraIssueLinkRequest(
    data=JiraIssueLinkData(
        attributes=JiraIssueLinkAttributes(
            jira_issue_url="https://jira.example.com/browse/PROJ-123",
        ),
        type=JiraIssueResourceType.ISSUES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["link_jira_issue_to_case"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.link_jira_issue_to_case(case_id="case_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Link existing Jira issue to case returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.link_jira_issue_to_case".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::JiraIssueLinkRequest.new({
  data: DatadogAPIClient::V2::JiraIssueLinkData.new({
    attributes: DatadogAPIClient::V2::JiraIssueLinkAttributes.new({
      jira_issue_url: "https://jira.example.com/browse/PROJ-123",
    }),
    type: DatadogAPIClient::V2::JiraIssueResourceType::ISSUES,
  }),
})
api_instance.link_jira_issue_to_case("case_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Link existing Jira issue to case returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.JiraIssueLinkRequest{
		Data: datadogV2.JiraIssueLinkData{
			Attributes: datadogV2.JiraIssueLinkAttributes{
				JiraIssueUrl: "https://jira.example.com/browse/PROJ-123",
			},
			Type: datadogV2.JIRAISSUERESOURCETYPE_ISSUES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.LinkJiraIssueToCase", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.LinkJiraIssueToCase(ctx, "case_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.LinkJiraIssueToCase`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Link existing Jira issue to case returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.JiraIssueLinkAttributes;
import com.datadog.api.client.v2.model.JiraIssueLinkData;
import com.datadog.api.client.v2.model.JiraIssueLinkRequest;
import com.datadog.api.client.v2.model.JiraIssueResourceType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.linkJiraIssueToCase", true);
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    JiraIssueLinkRequest body =
        new JiraIssueLinkRequest()
            .data(
                new JiraIssueLinkData()
                    .attributes(
                        new JiraIssueLinkAttributes()
                            .jiraIssueUrl("https://jira.example.com/browse/PROJ-123"))
                    .type(JiraIssueResourceType.ISSUES));

    try {
      apiInstance.linkJiraIssueToCase("f98a5a5b-e0ff-45d4-b2f5-afe6e74de504", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#linkJiraIssueToCase");
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
// Link existing Jira issue to case returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::JiraIssueLinkAttributes;
use datadog_api_client::datadogV2::model::JiraIssueLinkData;
use datadog_api_client::datadogV2::model::JiraIssueLinkRequest;
use datadog_api_client::datadogV2::model::JiraIssueResourceType;

#[tokio::main]
async fn main() {
    let body = JiraIssueLinkRequest::new(JiraIssueLinkData::new(
        JiraIssueLinkAttributes::new("https://jira.example.com/browse/PROJ-123".to_string()),
        JiraIssueResourceType::ISSUES,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.LinkJiraIssueToCase", true);
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .link_jira_issue_to_case("case_id".to_string(), body)
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
 * Link existing Jira issue to case returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.linkJiraIssueToCase"] = true;
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiLinkJiraIssueToCaseRequest = {
  body: {
    data: {
      attributes: {
        jiraIssueUrl: "https://jira.example.com/browse/PROJ-123",
      },
      type: "issues",
    },
  },
  caseId: "case_id",
};

apiInstance
  .linkJiraIssueToCase(params)
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

## Remove Jira issue link from case{% #remove-jira-issue-link-from-case %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cases/{case_id}/relationships/jira_issues      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cases/{case_id}/relationships/jira_issues      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cases/{case_id}/relationships/jira_issues |

### Overview

Remove the link between a Jira issue and a case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/relationships/jira_issues" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Remove Jira issue link from case returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
configuration.unstable_operations["unlink_jira_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.unlink_jira_issue(
        case_id="case_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Remove Jira issue link from case returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.unlink_jira_issue".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new
api_instance.unlink_jira_issue("case_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Remove Jira issue link from case returns "No Content" response

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
	configuration.SetUnstableOperationEnabled("v2.UnlinkJiraIssue", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.UnlinkJiraIssue(ctx, "case_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.UnlinkJiraIssue`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Remove Jira issue link from case returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.unlinkJiraIssue", true);
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    try {
      apiInstance.unlinkJiraIssue("f98a5a5b-e0ff-45d4-b2f5-afe6e74de504");
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#unlinkJiraIssue");
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
// Remove Jira issue link from case returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UnlinkJiraIssue", true);
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.unlink_jira_issue("case_id".to_string()).await;
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
 * Remove Jira issue link from case returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.unlinkJiraIssue"] = true;
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiUnlinkJiraIssueRequest = {
  caseId: "case_id",
};

apiInstance
  .unlinkJiraIssue(params)
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

## Create ServiceNow ticket for case{% #create-servicenow-ticket-for-case %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/relationships/servicenow_tickets |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/relationships/servicenow_tickets |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/relationships/servicenow_tickets      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/relationships/servicenow_tickets      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/relationships/servicenow_tickets     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/relationships/servicenow_tickets |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/relationships/servicenow_tickets |

### Overview

Create a new ServiceNow incident ticket and link it to a case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

ServiceNow ticket creation request

{% tab title="Model" %}

| Parent field | Field                           | Type   | Description                                                    |
| ------------ | ------------------------------- | ------ | -------------------------------------------------------------- |
|              | data [*required*]          | object | ServiceNow ticket creation data                                |
| data         | attributes [*required*]    | object | ServiceNow ticket creation attributes                          |
| attributes   | assignment_group                | string | ServiceNow assignment group                                    |
| attributes   | instance_name [*required*] | string | ServiceNow instance name                                       |
| data         | type [*required*]          | enum   | ServiceNow ticket resource type Allowed enum values: `tickets` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group": "IT Support",
      "instance_name": "my-instance"
    },
    "type": "tickets"
  }
}
```

{% /tab %}

### Response

{% tab title="202" %}
Accepted
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/relationships/servicenow_tickets" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "instance_name": "my-instance"
    },
    "type": "tickets"
  }
}
EOF
                
##### 

```python
"""
Create ServiceNow ticket for case returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.service_now_ticket_create_attributes import ServiceNowTicketCreateAttributes
from datadog_api_client.v2.model.service_now_ticket_create_data import ServiceNowTicketCreateData
from datadog_api_client.v2.model.service_now_ticket_create_request import ServiceNowTicketCreateRequest
from datadog_api_client.v2.model.service_now_ticket_resource_type import ServiceNowTicketResourceType

body = ServiceNowTicketCreateRequest(
    data=ServiceNowTicketCreateData(
        attributes=ServiceNowTicketCreateAttributes(
            assignment_group="IT Support",
            instance_name="my-instance",
        ),
        type=ServiceNowTicketResourceType.TICKETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_service_now_ticket"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.create_case_service_now_ticket(case_id="case_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create ServiceNow ticket for case returns "Accepted" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_case_service_now_ticket".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::ServiceNowTicketCreateRequest.new({
  data: DatadogAPIClient::V2::ServiceNowTicketCreateData.new({
    attributes: DatadogAPIClient::V2::ServiceNowTicketCreateAttributes.new({
      assignment_group: "IT Support",
      instance_name: "my-instance",
    }),
    type: DatadogAPIClient::V2::ServiceNowTicketResourceType::TICKETS,
  }),
})
p api_instance.create_case_service_now_ticket("case_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create ServiceNow ticket for case returns "Accepted" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.ServiceNowTicketCreateRequest{
		Data: datadogV2.ServiceNowTicketCreateData{
			Attributes: datadogV2.ServiceNowTicketCreateAttributes{
				AssignmentGroup: datadog.PtrString("IT Support"),
				InstanceName:    "my-instance",
			},
			Type: datadogV2.SERVICENOWTICKETRESOURCETYPE_TICKETS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateCaseServiceNowTicket", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.CreateCaseServiceNowTicket(ctx, "case_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.CreateCaseServiceNowTicket`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create ServiceNow ticket for case returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.ServiceNowTicketCreateAttributes;
import com.datadog.api.client.v2.model.ServiceNowTicketCreateData;
import com.datadog.api.client.v2.model.ServiceNowTicketCreateRequest;
import com.datadog.api.client.v2.model.ServiceNowTicketResourceType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createCaseServiceNowTicket", true);
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    ServiceNowTicketCreateRequest body =
        new ServiceNowTicketCreateRequest()
            .data(
                new ServiceNowTicketCreateData()
                    .attributes(
                        new ServiceNowTicketCreateAttributes()
                            .assignmentGroup("IT Support")
                            .instanceName("my-instance"))
                    .type(ServiceNowTicketResourceType.TICKETS));

    try {
      apiInstance.createCaseServiceNowTicket("f98a5a5b-e0ff-45d4-b2f5-afe6e74de504", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#createCaseServiceNowTicket");
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
// Create ServiceNow ticket for case returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::ServiceNowTicketCreateAttributes;
use datadog_api_client::datadogV2::model::ServiceNowTicketCreateData;
use datadog_api_client::datadogV2::model::ServiceNowTicketCreateRequest;
use datadog_api_client::datadogV2::model::ServiceNowTicketResourceType;

#[tokio::main]
async fn main() {
    let body = ServiceNowTicketCreateRequest::new(ServiceNowTicketCreateData::new(
        ServiceNowTicketCreateAttributes::new("my-instance".to_string())
            .assignment_group("IT Support".to_string()),
        ServiceNowTicketResourceType::TICKETS,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateCaseServiceNowTicket", true);
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api
        .create_case_service_now_ticket("case_id".to_string(), body)
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
 * Create ServiceNow ticket for case returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createCaseServiceNowTicket"] = true;
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiCreateCaseServiceNowTicketRequest = {
  body: {
    data: {
      attributes: {
        assignmentGroup: "IT Support",
        instanceName: "my-instance",
      },
      type: "tickets",
    },
  },
  caseId: "case_id",
};

apiInstance
  .createCaseServiceNowTicket(params)
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

## Create investigation notebook for case{% #create-investigation-notebook-for-case %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/{case_id}/relationships/notebook |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/{case_id}/relationships/notebook |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/{case_id}/relationships/notebook      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/{case_id}/relationships/notebook      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/{case_id}/relationships/notebook     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/{case_id}/relationships/notebook |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/{case_id}/relationships/notebook |

### Overview

Create a new investigation notebook and link it to a case

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#case-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description        |
| ------------------------- | ------ | ------------------ |
| case_id [*required*] | string | Case's UUID or key |

### Request

#### Body Data (required)

Notebook creation request

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                            |
| ------------ | ---------------------- | ------ | ------------------------------------------------------ |
|              | data [*required*] | object | Notebook creation data                                 |
| data         | type [*required*] | enum   | Notebook resource type Allowed enum values: `notebook` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "notebook"
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport case_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de504"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/${case_id}/relationships/notebook" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "notebook"
  }
}
EOF
                
##### 

```python
"""
Create investigation notebook for case returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.notebook_create_data import NotebookCreateData
from datadog_api_client.v2.model.notebook_create_request import NotebookCreateRequest
from datadog_api_client.v2.model.notebook_resource_type import NotebookResourceType

body = NotebookCreateRequest(
    data=NotebookCreateData(
        type=NotebookResourceType.NOTEBOOK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_notebook"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.create_case_notebook(case_id="case_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create investigation notebook for case returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_case_notebook".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CaseManagementAPI.new

body = DatadogAPIClient::V2::NotebookCreateRequest.new({
  data: DatadogAPIClient::V2::NotebookCreateData.new({
    type: DatadogAPIClient::V2::NotebookResourceType::NOTEBOOK,
  }),
})
api_instance.create_case_notebook("case_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create investigation notebook for case returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.NotebookCreateRequest{
		Data: datadogV2.NotebookCreateData{
			Type: datadogV2.NOTEBOOKRESOURCETYPE_NOTEBOOK,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateCaseNotebook", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementApi(apiClient)
	r, err := api.CreateCaseNotebook(ctx, "case_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementApi.CreateCaseNotebook`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create investigation notebook for case returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementApi;
import com.datadog.api.client.v2.model.NotebookCreateData;
import com.datadog.api.client.v2.model.NotebookCreateRequest;
import com.datadog.api.client.v2.model.NotebookResourceType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createCaseNotebook", true);
    CaseManagementApi apiInstance = new CaseManagementApi(defaultClient);

    NotebookCreateRequest body =
        new NotebookCreateRequest()
            .data(new NotebookCreateData().type(NotebookResourceType.NOTEBOOK));

    try {
      apiInstance.createCaseNotebook("f98a5a5b-e0ff-45d4-b2f5-afe6e74de504", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementApi#createCaseNotebook");
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
// Create investigation notebook for case returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management::CaseManagementAPI;
use datadog_api_client::datadogV2::model::NotebookCreateData;
use datadog_api_client::datadogV2::model::NotebookCreateRequest;
use datadog_api_client::datadogV2::model::NotebookResourceType;

#[tokio::main]
async fn main() {
    let body = NotebookCreateRequest::new(NotebookCreateData::new(NotebookResourceType::NOTEBOOK));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateCaseNotebook", true);
    let api = CaseManagementAPI::with_config(configuration);
    let resp = api.create_case_notebook("case_id".to_string(), body).await;
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
 * Create investigation notebook for case returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createCaseNotebook"] = true;
const apiInstance = new v2.CaseManagementApi(configuration);

const params: v2.CaseManagementApiCreateCaseNotebookRequest = {
  body: {
    data: {
      type: "notebook",
    },
  },
  caseId: "case_id",
};

apiInstance
  .createCaseNotebook(params)
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
