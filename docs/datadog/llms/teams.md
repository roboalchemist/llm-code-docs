# Source: https://docs.datadoghq.com/api/latest/teams.md

---
title: Teams
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Teams
---

View and manage teams within Datadog. See the [Teams page](https://docs.datadoghq.com/account_management/teams/) for more information.

## Get all teams{% #get-all-teams %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                  |
| ----------------- | --------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team |

### Overview

Get all teams. Can be used to search for teams using the `filter[keyword]` and `filter[me]` query parameters. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Query Strings

| Name            | Type    | Description                                                                                               |
| --------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| page[number]    | integer | Specific page number to return.                                                                           |
| page[size]      | integer | Size for a given page. The maximum allowed value is 100.                                                  |
| sort            | enum    | Specifies the order of the returned teamsAllowed enum values: `name, -name, user_count, -user_count`      |
| include         | array   | Included related resources optionally requested. Allowed enum values: `team_links, user_team_permissions` |
| filter[keyword] | string  | Search query. Can be team name, team handle, or email of team member                                      |
| filter[me]      | boolean | When true, only returns teams the current user belongs to                                                 |
| fields[team]    | array   | List of fields that need to be fetched.                                                                   |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with multiple teams

| Parent field          | Field                        | Type            | Description                                                                                          |
| --------------------- | ---------------------------- | --------------- | ---------------------------------------------------------------------------------------------------- |
|                       | data                         | [object]        | Teams response data                                                                                  |
| data                  | attributes [*required*] | object          | Team attributes                                                                                      |
| attributes            | avatar                       | string          | Unicode representation of the avatar for the team, limited to a single grapheme                      |
| attributes            | banner                       | int64           | Banner selection for the team                                                                        |
| attributes            | created_at                   | date-time       | Creation date of the team                                                                            |
| attributes            | description                  | string          | Free-form markdown description/content for the team's homepage                                       |
| attributes            | handle [*required*]     | string          | The team's identifier                                                                                |
| attributes            | hidden_modules               | [string]        | Collection of hidden modules for the team                                                            |
| attributes            | is_managed                   | boolean         | Whether the team is managed from an external source                                                  |
| attributes            | link_count                   | int32           | The number of links belonging to the team                                                            |
| attributes            | modified_at                  | date-time       | Modification date of the team                                                                        |
| attributes            | name [*required*]       | string          | The name of the team                                                                                 |
| attributes            | summary                      | string          | A brief summary of the team, derived from the `description`                                          |
| attributes            | user_count                   | int32           | The number of users belonging to the team                                                            |
| attributes            | visible_modules              | [string]        | Collection of visible modules for the team                                                           |
| data                  | id [*required*]         | string          | The team's identifier                                                                                |
| data                  | relationships                | object          | Resources related to a team                                                                          |
| relationships         | team_links                   | object          | Relationship between a team and a team link                                                          |
| team_links            | data                         | [object]        | Related team links                                                                                   |
| data                  | id [*required*]         | string          | The team link's identifier                                                                           |
| data                  | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                     |
| team_links            | links                        | object          | Links attributes.                                                                                    |
| links                 | related                      | string          | Related link.                                                                                        |
| relationships         | user_team_permissions        | object          | Relationship between a user team permission and a team                                               |
| user_team_permissions | data                         | object          | Related user team permission data                                                                    |
| data                  | id [*required*]         | string          | The ID of the user team permission                                                                   |
| data                  | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                               |
| user_team_permissions | links                        | object          | Links attributes.                                                                                    |
| links                 | related                      | string          | Related link.                                                                                        |
| data                  | type [*required*]       | enum            | Team type Allowed enum values: `team`                                                                |
|                       | included                     | [ <oneOf>] | Resources related to the team                                                                        |
| included              | Option 1                     | object          | User object returned by the API.                                                                     |
| Option 1              | attributes                   | object          | Attributes of user object returned by the API.                                                       |
| attributes            | created_at                   | date-time       | Creation time of the user.                                                                           |
| attributes            | disabled                     | boolean         | Whether the user is disabled.                                                                        |
| attributes            | email                        | string          | Email of the user.                                                                                   |
| attributes            | handle                       | string          | Handle of the user.                                                                                  |
| attributes            | icon                         | string          | URL of the user's icon.                                                                              |
| attributes            | last_login_time              | date-time       | The last time the user logged in.                                                                    |
| attributes            | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                             |
| attributes            | modified_at                  | date-time       | Time that the user was last modified.                                                                |
| attributes            | name                         | string          | Name of the user.                                                                                    |
| attributes            | service_account              | boolean         | Whether the user is a service account.                                                               |
| attributes            | status                       | string          | Status of the user.                                                                                  |
| attributes            | title                        | string          | Title of the user.                                                                                   |
| attributes            | verified                     | boolean         | Whether the user is verified.                                                                        |
| Option 1              | id                           | string          | ID of the user.                                                                                      |
| Option 1              | relationships                | object          | Relationships of the user object returned by the API.                                                |
| relationships         | org                          | object          | Relationship to an organization.                                                                     |
| org                   | data [*required*]       | object          | Relationship to organization object.                                                                 |
| data                  | id [*required*]         | string          | ID of the organization.                                                                              |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                             |
| relationships         | other_orgs                   | object          | Relationship to organizations.                                                                       |
| other_orgs            | data [*required*]       | [object]        | Relationships to organization objects.                                                               |
| data                  | id [*required*]         | string          | ID of the organization.                                                                              |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                             |
| relationships         | other_users                  | object          | Relationship to users.                                                                               |
| other_users           | data [*required*]       | [object]        | Relationships to user objects.                                                                       |
| data                  | id [*required*]         | string          | A unique identifier that represents the user.                                                        |
| data                  | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                    |
| relationships         | roles                        | object          | Relationship to roles.                                                                               |
| roles                 | data                         | [object]        | An array containing type and the unique identifier of a role.                                        |
| data                  | id                           | string          | The unique identifier of the role.                                                                   |
| data                  | type                         | enum            | Roles type. Allowed enum values: `roles`                                                             |
| Option 1              | type                         | enum            | Users resource type. Allowed enum values: `users`                                                    |
| included              | Option 2                     | object          | Team link                                                                                            |
| Option 2              | attributes [*required*] | object          | Team link attributes                                                                                 |
| attributes            | label [*required*]      | string          | The link's label                                                                                     |
| attributes            | position                     | int32           | The link's position, used to sort links for the team                                                 |
| attributes            | team_id                      | string          | ID of the team the link is associated with                                                           |
| attributes            | url [*required*]        | string          | The URL for the link                                                                                 |
| Option 2              | id [*required*]         | string          | The team link's identifier                                                                           |
| Option 2              | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                     |
| included              | Option 3                     | object          | A user's permissions for a given team                                                                |
| Option 3              | attributes                   | object          | User team permission attributes                                                                      |
| attributes            | permissions                  | object          | Object of team permission actions and boolean values that a logged in user can perform on this team. |
| Option 3              | id [*required*]         | string          | The user team permission's identifier                                                                |
| Option 3              | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                               |
|                       | links                        | object          | Teams response links.                                                                                |
| links                 | first                        | string          | First link.                                                                                          |
| links                 | last                         | string          | Last link.                                                                                           |
| links                 | next                         | string          | Next link.                                                                                           |
| links                 | prev                         | string          | Previous link.                                                                                       |
| links                 | self                         | string          | Current link.                                                                                        |
|                       | meta                         | object          | Teams response metadata.                                                                             |
| meta                  | pagination                   | object          | Teams response metadata.                                                                             |
| pagination            | first_offset                 | int64           | The first offset.                                                                                    |
| pagination            | last_offset                  | int64           | The last offset.                                                                                     |
| pagination            | limit                        | int64           | Pagination limit.                                                                                    |
| pagination            | next_offset                  | int64           | The next offset.                                                                                     |
| pagination            | offset                       | int64           | The offset.                                                                                          |
| pagination            | prev_offset                  | int64           | The previous offset.                                                                                 |
| pagination            | total                        | int64           | Total results.                                                                                       |
| pagination            | type                         | string          | Offset type.                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "avatar": "ð¥",
        "banner": "integer",
        "created_at": "2019-09-19T10:00:00.000Z",
        "description": "string",
        "handle": "example-team",
        "hidden_modules": [],
        "is_managed": false,
        "link_count": "integer",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "Example Team",
        "summary": "string",
        "user_count": "integer",
        "visible_modules": []
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "relationships": {
        "team_links": {
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
        "user_team_permissions": {
          "data": {
            "id": "UserTeamPermissions-aeadc05e-98a8-11ec-ac2c-da7ad0900001-416595",
            "type": "user_team_permissions"
          },
          "links": {
            "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
          }
        }
      },
      "type": "team"
    }
  ],
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "pagination": {
      "first_offset": "integer",
      "last_offset": "integer",
      "limit": "integer",
      "next_offset": "integer",
      "offset": "integer",
      "prev_offset": "integer",
      "total": "integer",
      "type": "string"
    }
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all teams returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_teams()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.list_teams()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get all teams returns "OK" response

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
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.ListTeams(ctx, *datadogV2.NewListTeamsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.ListTeams`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.ListTeams`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get all teams returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    try {
      TeamsResponse result = apiInstance.listTeams();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#listTeams");
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
// Get all teams returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::ListTeamsOptionalParams;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.list_teams(ListTeamsOptionalParams::default()).await;
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
 * Get all teams returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

apiInstance
  .listTeams()
  .then((data: v2.TeamsResponse) => {
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

## Create a team{% #create-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team |

### Overview

Create a new team. User IDs passed through the `users` relationship field are added to the team. This endpoint requires all of the following permissions:
`teams_read``teams_manage`

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field  | Field                        | Type     | Description                                                                     |
| ------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------- |
|               | data [*required*]       | object   | Team create                                                                     |
| data          | attributes [*required*] | object   | Team creation attributes                                                        |
| attributes    | avatar                       | string   | Unicode representation of the avatar for the team, limited to a single grapheme |
| attributes    | banner                       | int64    | Banner selection for the team                                                   |
| attributes    | description                  | string   | Free-form markdown description/content for the team's homepage                  |
| attributes    | handle [*required*]     | string   | The team's identifier                                                           |
| attributes    | hidden_modules               | [string] | Collection of hidden modules for the team                                       |
| attributes    | name [*required*]       | string   | The name of the team                                                            |
| attributes    | visible_modules              | [string] | Collection of visible modules for the team                                      |
| data          | relationships                | object   | Relationships formed with the team on creation                                  |
| relationships | users                        | object   | Relationship to users.                                                          |
| users         | data [*required*]       | [object] | Relationships to user objects.                                                  |
| data          | id [*required*]         | string   | A unique identifier that represents the user.                                   |
| data          | type [*required*]       | enum     | Users resource type. Allowed enum values: `users`                               |
| data          | type [*required*]       | enum     | Team type Allowed enum values: `team`                                           |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "handle": "test-handle-a0fc0297eb519635",
      "name": "test-name-a0fc0297eb519635"
    },
    "relationships": {
      "users": {
        "data": []
      }
    },
    "type": "team"
  }
}
```

#####

```json
{
  "data": {
    "attributes": {
      "handle": "test-handle-a0fc0297eb519635",
      "name": "test-name-a0fc0297eb519635",
      "avatar": "\ud83e\udd51",
      "banner": 7,
      "visible_modules": [
        "m1",
        "m2"
      ],
      "hidden_modules": [
        "m3"
      ]
    },
    "type": "team"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response with a team

| Parent field          | Field                        | Type      | Description                                                                     |
| --------------------- | ---------------------------- | --------- | ------------------------------------------------------------------------------- |
|                       | data                         | object    | A team                                                                          |
| data                  | attributes [*required*] | object    | Team attributes                                                                 |
| attributes            | avatar                       | string    | Unicode representation of the avatar for the team, limited to a single grapheme |
| attributes            | banner                       | int64     | Banner selection for the team                                                   |
| attributes            | created_at                   | date-time | Creation date of the team                                                       |
| attributes            | description                  | string    | Free-form markdown description/content for the team's homepage                  |
| attributes            | handle [*required*]     | string    | The team's identifier                                                           |
| attributes            | hidden_modules               | [string]  | Collection of hidden modules for the team                                       |
| attributes            | is_managed                   | boolean   | Whether the team is managed from an external source                             |
| attributes            | link_count                   | int32     | The number of links belonging to the team                                       |
| attributes            | modified_at                  | date-time | Modification date of the team                                                   |
| attributes            | name [*required*]       | string    | The name of the team                                                            |
| attributes            | summary                      | string    | A brief summary of the team, derived from the `description`                     |
| attributes            | user_count                   | int32     | The number of users belonging to the team                                       |
| attributes            | visible_modules              | [string]  | Collection of visible modules for the team                                      |
| data                  | id [*required*]         | string    | The team's identifier                                                           |
| data                  | relationships                | object    | Resources related to a team                                                     |
| relationships         | team_links                   | object    | Relationship between a team and a team link                                     |
| team_links            | data                         | [object]  | Related team links                                                              |
| data                  | id [*required*]         | string    | The team link's identifier                                                      |
| data                  | type [*required*]       | enum      | Team link type Allowed enum values: `team_links`                                |
| team_links            | links                        | object    | Links attributes.                                                               |
| links                 | related                      | string    | Related link.                                                                   |
| relationships         | user_team_permissions        | object    | Relationship between a user team permission and a team                          |
| user_team_permissions | data                         | object    | Related user team permission data                                               |
| data                  | id [*required*]         | string    | The ID of the user team permission                                              |
| data                  | type [*required*]       | enum      | User team permission type Allowed enum values: `user_team_permissions`          |
| user_team_permissions | links                        | object    | Links attributes.                                                               |
| links                 | related                      | string    | Related link.                                                                   |
| data                  | type [*required*]       | enum      | Team type Allowed enum values: `team`                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "avatar": "ð¥",
      "banner": "integer",
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "handle": "example-team",
      "hidden_modules": [],
      "is_managed": false,
      "link_count": "integer",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "Example Team",
      "summary": "string",
      "user_count": "integer",
      "visible_modules": []
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "relationships": {
      "team_links": {
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
      "user_team_permissions": {
        "data": {
          "id": "UserTeamPermissions-aeadc05e-98a8-11ec-ac2c-da7ad0900001-416595",
          "type": "user_team_permissions"
        },
        "links": {
          "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
        }
      }
    },
    "type": "team"
  }
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

{% tab title="409" %}
API error response.
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "handle": "test-handle-a0fc0297eb519635",
      "name": "test-name-a0fc0297eb519635"
    },
    "relationships": {
      "users": {
        "data": []
      }
    },
    "type": "team"
  }
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "handle": "test-handle-a0fc0297eb519635",
      "name": "test-name-a0fc0297eb519635",
      "avatar": "\ud83e\udd51",
      "banner": 7,
      "visible_modules": [
        "m1",
        "m2"
      ],
      "hidden_modules": [
        "m3"
      ]
    },
    "type": "team"
  }
}
EOF

#####

```go
// Create a team returns "CREATED" response

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
    body := datadogV2.TeamCreateRequest{
        Data: datadogV2.TeamCreate{
            Attributes: datadogV2.TeamCreateAttributes{
                Handle: "test-handle-a0fc0297eb519635",
                Name:   "test-name-a0fc0297eb519635",
            },
            Relationships: &datadogV2.TeamCreateRelationships{
                Users: &datadogV2.RelationshipToUsers{
                    Data: []datadogV2.RelationshipToUserData{},
                },
            },
            Type: datadogV2.TEAMTYPE_TEAM,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.CreateTeam(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.CreateTeam`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.CreateTeam`:\n%s\n", responseContent)
}
```

#####

```go
// Create a team with V2 fields returns "CREATED" response

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
    body := datadogV2.TeamCreateRequest{
        Data: datadogV2.TeamCreate{
            Attributes: datadogV2.TeamCreateAttributes{
                Handle: "test-handle-a0fc0297eb519635",
                Name:   "test-name-a0fc0297eb519635",
                Avatar: *datadog.NewNullableString(datadog.PtrString("ð¥")),
                Banner: *datadog.NewNullableInt64(datadog.PtrInt64(7)),
                VisibleModules: []string{
                    "m1",
                    "m2",
                },
                HiddenModules: []string{
                    "m3",
                },
            },
            Type: datadogV2.TEAMTYPE_TEAM,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.CreateTeam(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.CreateTeam`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.CreateTeam`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a team returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.RelationshipToUsers;
import com.datadog.api.client.v2.model.TeamCreate;
import com.datadog.api.client.v2.model.TeamCreateAttributes;
import com.datadog.api.client.v2.model.TeamCreateRelationships;
import com.datadog.api.client.v2.model.TeamCreateRequest;
import com.datadog.api.client.v2.model.TeamResponse;
import com.datadog.api.client.v2.model.TeamType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    TeamCreateRequest body =
        new TeamCreateRequest()
            .data(
                new TeamCreate()
                    .attributes(
                        new TeamCreateAttributes()
                            .handle("test-handle-a0fc0297eb519635")
                            .name("test-name-a0fc0297eb519635"))
                    .relationships(new TeamCreateRelationships().users(new RelationshipToUsers()))
                    .type(TeamType.TEAM));

    try {
      TeamResponse result = apiInstance.createTeam(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#createTeam");
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
// Create a team with V2 fields returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamCreate;
import com.datadog.api.client.v2.model.TeamCreateAttributes;
import com.datadog.api.client.v2.model.TeamCreateRequest;
import com.datadog.api.client.v2.model.TeamResponse;
import com.datadog.api.client.v2.model.TeamType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    TeamCreateRequest body =
        new TeamCreateRequest()
            .data(
                new TeamCreate()
                    .attributes(
                        new TeamCreateAttributes()
                            .handle("test-handle-a0fc0297eb519635")
                            .name("test-name-a0fc0297eb519635")
                            .avatar("ð¥")
                            .banner(7L)
                            .visibleModules(Arrays.asList("m1", "m2"))
                            .hiddenModules(Collections.singletonList("m3")))
                    .type(TeamType.TEAM));

    try {
      TeamResponse result = apiInstance.createTeam(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#createTeam");
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
Create a team returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.relationship_to_users import RelationshipToUsers
from datadog_api_client.v2.model.team_create import TeamCreate
from datadog_api_client.v2.model.team_create_attributes import TeamCreateAttributes
from datadog_api_client.v2.model.team_create_relationships import TeamCreateRelationships
from datadog_api_client.v2.model.team_create_request import TeamCreateRequest
from datadog_api_client.v2.model.team_type import TeamType

body = TeamCreateRequest(
    data=TeamCreate(
        attributes=TeamCreateAttributes(
            handle="test-handle-a0fc0297eb519635",
            name="test-name-a0fc0297eb519635",
        ),
        relationships=TeamCreateRelationships(
            users=RelationshipToUsers(
                data=[],
            ),
        ),
        type=TeamType.TEAM,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team(body=body)

    print(response)
```

#####

```python
"""
Create a team with V2 fields returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_create import TeamCreate
from datadog_api_client.v2.model.team_create_attributes import TeamCreateAttributes
from datadog_api_client.v2.model.team_create_request import TeamCreateRequest
from datadog_api_client.v2.model.team_type import TeamType

body = TeamCreateRequest(
    data=TeamCreate(
        attributes=TeamCreateAttributes(
            handle="test-handle-a0fc0297eb519635",
            name="test-name-a0fc0297eb519635",
            avatar="ð¥",
            banner=7,
            visible_modules=[
                "m1",
                "m2",
            ],
            hidden_modules=[
                "m3",
            ],
        ),
        type=TeamType.TEAM,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a team returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::TeamCreateRequest.new({
  data: DatadogAPIClient::V2::TeamCreate.new({
    attributes: DatadogAPIClient::V2::TeamCreateAttributes.new({
      handle: "test-handle-a0fc0297eb519635",
      name: "test-name-a0fc0297eb519635",
    }),
    relationships: DatadogAPIClient::V2::TeamCreateRelationships.new({
      users: DatadogAPIClient::V2::RelationshipToUsers.new({
        data: [],
      }),
    }),
    type: DatadogAPIClient::V2::TeamType::TEAM,
  }),
})
p api_instance.create_team(body)
```

#####

```ruby
# Create a team with V2 fields returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::TeamCreateRequest.new({
  data: DatadogAPIClient::V2::TeamCreate.new({
    attributes: DatadogAPIClient::V2::TeamCreateAttributes.new({
      handle: "test-handle-a0fc0297eb519635",
      name: "test-name-a0fc0297eb519635",
      avatar: "ð¥",
      banner: 7,
      visible_modules: [
        "m1",
        "m2",
      ],
      hidden_modules: [
        "m3",
      ],
    }),
    type: DatadogAPIClient::V2::TeamType::TEAM,
  }),
})
p api_instance.create_team(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create a team returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::RelationshipToUsers;
use datadog_api_client::datadogV2::model::TeamCreate;
use datadog_api_client::datadogV2::model::TeamCreateAttributes;
use datadog_api_client::datadogV2::model::TeamCreateRelationships;
use datadog_api_client::datadogV2::model::TeamCreateRequest;
use datadog_api_client::datadogV2::model::TeamType;

#[tokio::main]
async fn main() {
    let body = TeamCreateRequest::new(
        TeamCreate::new(
            TeamCreateAttributes::new(
                "test-handle-a0fc0297eb519635".to_string(),
                "test-name-a0fc0297eb519635".to_string(),
            ),
            TeamType::TEAM,
        )
        .relationships(TeamCreateRelationships::new().users(RelationshipToUsers::new(vec![]))),
    );
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.create_team(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create a team with V2 fields returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamCreate;
use datadog_api_client::datadogV2::model::TeamCreateAttributes;
use datadog_api_client::datadogV2::model::TeamCreateRequest;
use datadog_api_client::datadogV2::model::TeamType;

#[tokio::main]
async fn main() {
    let body = TeamCreateRequest::new(TeamCreate::new(
        TeamCreateAttributes::new(
            "test-handle-a0fc0297eb519635".to_string(),
            "test-name-a0fc0297eb519635".to_string(),
        )
        .avatar(Some("ð¥".to_string()))
        .banner(Some(7))
        .hidden_modules(vec!["m3".to_string()])
        .visible_modules(vec!["m1".to_string(), "m2".to_string()]),
        TeamType::TEAM,
    ));
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.create_team(body).await;
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
 * Create a team returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiCreateTeamRequest = {
  body: {
    data: {
      attributes: {
        handle: "test-handle-a0fc0297eb519635",
        name: "test-name-a0fc0297eb519635",
      },
      relationships: {
        users: {
          data: [],
        },
      },
      type: "team",
    },
  },
};

apiInstance
  .createTeam(params)
  .then((data: v2.TeamResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create a team with V2 fields returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiCreateTeamRequest = {
  body: {
    data: {
      attributes: {
        handle: "test-handle-a0fc0297eb519635",
        name: "test-name-a0fc0297eb519635",
        avatar: "ð¥",
        banner: 7,
        visibleModules: ["m1", "m2"],
        hiddenModules: ["m3"],
      },
      type: "team",
    },
  },
};

apiInstance
  .createTeam(params)
  .then((data: v2.TeamResponse) => {
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

## Get a team{% #get-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{team_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{team_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{team_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{team_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{team_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{team_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{team_id} |

### Overview

Get a single team using the team's `id`. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with a team

| Parent field          | Field                        | Type      | Description                                                                     |
| --------------------- | ---------------------------- | --------- | ------------------------------------------------------------------------------- |
|                       | data                         | object    | A team                                                                          |
| data                  | attributes [*required*] | object    | Team attributes                                                                 |
| attributes            | avatar                       | string    | Unicode representation of the avatar for the team, limited to a single grapheme |
| attributes            | banner                       | int64     | Banner selection for the team                                                   |
| attributes            | created_at                   | date-time | Creation date of the team                                                       |
| attributes            | description                  | string    | Free-form markdown description/content for the team's homepage                  |
| attributes            | handle [*required*]     | string    | The team's identifier                                                           |
| attributes            | hidden_modules               | [string]  | Collection of hidden modules for the team                                       |
| attributes            | is_managed                   | boolean   | Whether the team is managed from an external source                             |
| attributes            | link_count                   | int32     | The number of links belonging to the team                                       |
| attributes            | modified_at                  | date-time | Modification date of the team                                                   |
| attributes            | name [*required*]       | string    | The name of the team                                                            |
| attributes            | summary                      | string    | A brief summary of the team, derived from the `description`                     |
| attributes            | user_count                   | int32     | The number of users belonging to the team                                       |
| attributes            | visible_modules              | [string]  | Collection of visible modules for the team                                      |
| data                  | id [*required*]         | string    | The team's identifier                                                           |
| data                  | relationships                | object    | Resources related to a team                                                     |
| relationships         | team_links                   | object    | Relationship between a team and a team link                                     |
| team_links            | data                         | [object]  | Related team links                                                              |
| data                  | id [*required*]         | string    | The team link's identifier                                                      |
| data                  | type [*required*]       | enum      | Team link type Allowed enum values: `team_links`                                |
| team_links            | links                        | object    | Links attributes.                                                               |
| links                 | related                      | string    | Related link.                                                                   |
| relationships         | user_team_permissions        | object    | Relationship between a user team permission and a team                          |
| user_team_permissions | data                         | object    | Related user team permission data                                               |
| data                  | id [*required*]         | string    | The ID of the user team permission                                              |
| data                  | type [*required*]       | enum      | User team permission type Allowed enum values: `user_team_permissions`          |
| user_team_permissions | links                        | object    | Links attributes.                                                               |
| links                 | related                      | string    | Related link.                                                                   |
| data                  | type [*required*]       | enum      | Team type Allowed enum values: `team`                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "avatar": "ð¥",
      "banner": "integer",
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "handle": "example-team",
      "hidden_modules": [],
      "is_managed": false,
      "link_count": "integer",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "Example Team",
      "summary": "string",
      "user_count": "integer",
      "visible_modules": []
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "relationships": {
      "team_links": {
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
      "user_team_permissions": {
        "data": {
          "id": "UserTeamPermissions-aeadc05e-98a8-11ec-ac2c-da7ad0900001-416595",
          "type": "user_team_permissions"
        },
        "links": {
          "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
        }
      }
    },
    "type": "team"
  }
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team(
        team_id=DD_TEAM_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team(DD_TEAM_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a team returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeam(ctx, DdTeamDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeam`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeam`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    try {
      TeamResponse result = apiInstance.getTeam(DD_TEAM_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeam");
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
// Get a team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.get_team(dd_team_data_id.clone()).await;
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
 * Get a team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiGetTeamRequest = {
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .getTeam(params)
  .then((data: v2.TeamResponse) => {
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

## Update a team{% #update-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/team/{team_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/team/{team_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/team/{team_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/team/{team_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/team/{team_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/team/{team_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/team/{team_id} |

### Overview

Update a team using the team's `id`. If the `team_links` relationship is present, the associated links are updated to be in the order they appear in the array, and any existing team links not present are removed. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field  | Field                        | Type     | Description                                                                     |
| ------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------- |
|               | data [*required*]       | object   | Team update request                                                             |
| data          | attributes [*required*] | object   | Team update attributes                                                          |
| attributes    | avatar                       | string   | Unicode representation of the avatar for the team, limited to a single grapheme |
| attributes    | banner                       | int64    | Banner selection for the team                                                   |
| attributes    | description                  | string   | Free-form markdown description/content for the team's homepage                  |
| attributes    | handle [*required*]     | string   | The team's identifier                                                           |
| attributes    | hidden_modules               | [string] | Collection of hidden modules for the team                                       |
| attributes    | name [*required*]       | string   | The name of the team                                                            |
| attributes    | visible_modules              | [string] | Collection of visible modules for the team                                      |
| data          | relationships                | object   | Team update relationships                                                       |
| relationships | team_links                   | object   | Relationship between a team and a team link                                     |
| team_links    | data                         | [object] | Related team links                                                              |
| data          | id [*required*]         | string   | The team link's identifier                                                      |
| data          | type [*required*]       | enum     | Team link type Allowed enum values: `team_links`                                |
| team_links    | links                        | object   | Links attributes.                                                               |
| links         | related                      | string   | Related link.                                                                   |
| data          | type [*required*]       | enum     | Team type Allowed enum values: `team`                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "handle": "example-team",
      "name": "Example Team updated",
      "avatar": "\ud83e\udd51",
      "banner": 7,
      "hidden_modules": [
        "m3"
      ],
      "visible_modules": [
        "m1",
        "m2"
      ]
    },
    "type": "team"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with a team

| Parent field          | Field                        | Type      | Description                                                                     |
| --------------------- | ---------------------------- | --------- | ------------------------------------------------------------------------------- |
|                       | data                         | object    | A team                                                                          |
| data                  | attributes [*required*] | object    | Team attributes                                                                 |
| attributes            | avatar                       | string    | Unicode representation of the avatar for the team, limited to a single grapheme |
| attributes            | banner                       | int64     | Banner selection for the team                                                   |
| attributes            | created_at                   | date-time | Creation date of the team                                                       |
| attributes            | description                  | string    | Free-form markdown description/content for the team's homepage                  |
| attributes            | handle [*required*]     | string    | The team's identifier                                                           |
| attributes            | hidden_modules               | [string]  | Collection of hidden modules for the team                                       |
| attributes            | is_managed                   | boolean   | Whether the team is managed from an external source                             |
| attributes            | link_count                   | int32     | The number of links belonging to the team                                       |
| attributes            | modified_at                  | date-time | Modification date of the team                                                   |
| attributes            | name [*required*]       | string    | The name of the team                                                            |
| attributes            | summary                      | string    | A brief summary of the team, derived from the `description`                     |
| attributes            | user_count                   | int32     | The number of users belonging to the team                                       |
| attributes            | visible_modules              | [string]  | Collection of visible modules for the team                                      |
| data                  | id [*required*]         | string    | The team's identifier                                                           |
| data                  | relationships                | object    | Resources related to a team                                                     |
| relationships         | team_links                   | object    | Relationship between a team and a team link                                     |
| team_links            | data                         | [object]  | Related team links                                                              |
| data                  | id [*required*]         | string    | The team link's identifier                                                      |
| data                  | type [*required*]       | enum      | Team link type Allowed enum values: `team_links`                                |
| team_links            | links                        | object    | Links attributes.                                                               |
| links                 | related                      | string    | Related link.                                                                   |
| relationships         | user_team_permissions        | object    | Relationship between a user team permission and a team                          |
| user_team_permissions | data                         | object    | Related user team permission data                                               |
| data                  | id [*required*]         | string    | The ID of the user team permission                                              |
| data                  | type [*required*]       | enum      | User team permission type Allowed enum values: `user_team_permissions`          |
| user_team_permissions | links                        | object    | Links attributes.                                                               |
| links                 | related                      | string    | Related link.                                                                   |
| data                  | type [*required*]       | enum      | Team type Allowed enum values: `team`                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "avatar": "ð¥",
      "banner": "integer",
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "handle": "example-team",
      "hidden_modules": [],
      "is_managed": false,
      "link_count": "integer",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "Example Team",
      "summary": "string",
      "user_count": "integer",
      "visible_modules": []
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "relationships": {
      "team_links": {
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
      "user_team_permissions": {
        "data": {
          "id": "UserTeamPermissions-aeadc05e-98a8-11ec-ac2c-da7ad0900001-416595",
          "type": "user_team_permissions"
        },
        "links": {
          "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
        }
      }
    },
    "type": "team"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
API error response.
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
API error response.
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
API error response.
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
                          \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "handle": "example-team",
      "name": "Example Team updated",
      "avatar": "\ud83e\udd51",
      "banner": 7,
      "hidden_modules": [
        "m3"
      ],
      "visible_modules": [
        "m1",
        "m2"
      ]
    },
    "type": "team"
  }
}
EOF

#####

```go
// Update a team returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataAttributesHandle := os.Getenv("DD_TEAM_DATA_ATTRIBUTES_HANDLE")
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    body := datadogV2.TeamUpdateRequest{
        Data: datadogV2.TeamUpdate{
            Attributes: datadogV2.TeamUpdateAttributes{
                Handle: DdTeamDataAttributesHandle,
                Name:   "Example Team updated",
                Avatar: *datadog.NewNullableString(datadog.PtrString("ð¥")),
                Banner: *datadog.NewNullableInt64(datadog.PtrInt64(7)),
                HiddenModules: []string{
                    "m3",
                },
                VisibleModules: []string{
                    "m1",
                    "m2",
                },
            },
            Type: datadogV2.TEAMTYPE_TEAM,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.UpdateTeam(ctx, DdTeamDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.UpdateTeam`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.UpdateTeam`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update a team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamResponse;
import com.datadog.api.client.v2.model.TeamType;
import com.datadog.api.client.v2.model.TeamUpdate;
import com.datadog.api.client.v2.model.TeamUpdateAttributes;
import com.datadog.api.client.v2.model.TeamUpdateRequest;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ATTRIBUTES_HANDLE = System.getenv("DD_TEAM_DATA_ATTRIBUTES_HANDLE");
    String DD_TEAM_DATA_ATTRIBUTES_NAME = System.getenv("DD_TEAM_DATA_ATTRIBUTES_NAME");
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    TeamUpdateRequest body =
        new TeamUpdateRequest()
            .data(
                new TeamUpdate()
                    .attributes(
                        new TeamUpdateAttributes()
                            .handle(DD_TEAM_DATA_ATTRIBUTES_HANDLE)
                            .name("Example Team updated")
                            .avatar("ð¥")
                            .banner(7L)
                            .hiddenModules(Collections.singletonList("m3"))
                            .visibleModules(Arrays.asList("m1", "m2")))
                    .type(TeamType.TEAM));

    try {
      TeamResponse result = apiInstance.updateTeam(DD_TEAM_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#updateTeam");
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
Update a team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_type import TeamType
from datadog_api_client.v2.model.team_update import TeamUpdate
from datadog_api_client.v2.model.team_update_attributes import TeamUpdateAttributes
from datadog_api_client.v2.model.team_update_request import TeamUpdateRequest

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ATTRIBUTES_HANDLE = environ["DD_TEAM_DATA_ATTRIBUTES_HANDLE"]
DD_TEAM_DATA_ATTRIBUTES_NAME = environ["DD_TEAM_DATA_ATTRIBUTES_NAME"]
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamUpdateRequest(
    data=TeamUpdate(
        attributes=TeamUpdateAttributes(
            handle=DD_TEAM_DATA_ATTRIBUTES_HANDLE,
            name="Example Team updated",
            avatar="ð¥",
            banner=7,
            hidden_modules=[
                "m3",
            ],
            visible_modules=[
                "m1",
                "m2",
            ],
        ),
        type=TeamType.TEAM,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ATTRIBUTES_HANDLE = ENV["DD_TEAM_DATA_ATTRIBUTES_HANDLE"]
DD_TEAM_DATA_ATTRIBUTES_NAME = ENV["DD_TEAM_DATA_ATTRIBUTES_NAME"]
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::TeamUpdateRequest.new({
  data: DatadogAPIClient::V2::TeamUpdate.new({
    attributes: DatadogAPIClient::V2::TeamUpdateAttributes.new({
      handle: DD_TEAM_DATA_ATTRIBUTES_HANDLE,
      name: "Example Team updated",
      avatar: "ð¥",
      banner: 7,
      hidden_modules: [
        "m3",
      ],
      visible_modules: [
        "m1",
        "m2",
      ],
    }),
    type: DatadogAPIClient::V2::TeamType::TEAM,
  }),
})
p api_instance.update_team(DD_TEAM_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update a team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamType;
use datadog_api_client::datadogV2::model::TeamUpdate;
use datadog_api_client::datadogV2::model::TeamUpdateAttributes;
use datadog_api_client::datadogV2::model::TeamUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_attributes_handle = std::env::var("DD_TEAM_DATA_ATTRIBUTES_HANDLE").unwrap();
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = TeamUpdateRequest::new(TeamUpdate::new(
        TeamUpdateAttributes::new(
            dd_team_data_attributes_handle.clone(),
            "Example Team updated".to_string(),
        )
        .avatar(Some("ð¥".to_string()))
        .banner(Some(7))
        .hidden_modules(vec!["m3".to_string()])
        .visible_modules(vec!["m1".to_string(), "m2".to_string()]),
        TeamType::TEAM,
    ));
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.update_team(dd_team_data_id.clone(), body).await;
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
 * Update a team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ATTRIBUTES_HANDLE = process.env
  .DD_TEAM_DATA_ATTRIBUTES_HANDLE as string;
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiUpdateTeamRequest = {
  body: {
    data: {
      attributes: {
        handle: DD_TEAM_DATA_ATTRIBUTES_HANDLE,
        name: "Example Team updated",
        avatar: "ð¥",
        banner: 7,
        hiddenModules: ["m3"],
        visibleModules: ["m1", "m2"],
      },
      type: "team",
    },
  },
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .updateTeam(params)
  .then((data: v2.TeamResponse) => {
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

## Remove a team{% #remove-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/team/{team_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/team/{team_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/team/{team_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/team/{team_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/team/{team_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/team/{team_id} |

### Overview

Remove a team using the team's `id`. This endpoint requires all of the following permissions:
`teams_read``teams_manage`

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove a team returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team(
        team_id=DD_TEAM_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Remove a team returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
api_instance.delete_team(DD_TEAM_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Remove a team returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.DeleteTeam(ctx, DdTeamDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.DeleteTeam`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Remove a team returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    try {
      apiInstance.deleteTeam(DD_TEAM_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#deleteTeam");
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
// Remove a team returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.delete_team(dd_team_data_id.clone()).await;
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
 * Remove a team returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiDeleteTeamRequest = {
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .deleteTeam(params)
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

## Get team memberships{% #get-team-memberships %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/memberships |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{team_id}/memberships |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{team_id}/memberships      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{team_id}/memberships      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{team_id}/memberships     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{team_id}/memberships |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships |

### Overview

Get a paginated list of members for a team This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

#### Query Strings

| Name            | Type    | Description                                                                                                                                     |
| --------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]      | integer | Size for a given page. The maximum allowed value is 100.                                                                                        |
| page[number]    | integer | Specific page number to return.                                                                                                                 |
| sort            | enum    | Specifies the order of returned team membershipsAllowed enum values: `manager_name, -manager_name, name, -name, handle, -handle, email, -email` |
| filter[keyword] | string  | Search query, can be user email or name                                                                                                         |

### Response

{% tab title="200" %}
Represents a user's association to a team
{% tab title="Model" %}
Team memberships response

| Parent field          | Field                        | Type            | Description                                                                                                                                                                                                       |
| --------------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                         | [object]        | Team memberships response data                                                                                                                                                                                    |
| data                  | attributes                   | object          | Team membership attributes                                                                                                                                                                                        |
| attributes            | provisioned_by               | string          | The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping. |
| attributes            | provisioned_by_id            | string          | UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.                                                                                                |
| attributes            | role                         | enum            | The user's role within the team Allowed enum values: `admin`                                                                                                                                                      |
| data                  | id [*required*]         | string          | The ID of a user's relationship with a team                                                                                                                                                                       |
| data                  | relationships                | object          | Relationship between membership and a user                                                                                                                                                                        |
| relationships         | team                         | object          | Relationship between team membership and team                                                                                                                                                                     |
| team                  | data [*required*]       | object          | The team associated with the membership                                                                                                                                                                           |
| data                  | id [*required*]         | string          | The ID of the team associated with the membership                                                                                                                                                                 |
| data                  | type [*required*]       | enum            | User team team type Allowed enum values: `team`                                                                                                                                                                   |
| relationships         | user                         | object          | Relationship between team membership and user                                                                                                                                                                     |
| user                  | data [*required*]       | object          | A user's relationship with a team                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user associated with the team                                                                                                                                                                       |
| data                  | type [*required*]       | enum            | User team user type Allowed enum values: `users`                                                                                                                                                                  |
| data                  | type [*required*]       | enum            | Team membership type Allowed enum values: `team_memberships`                                                                                                                                                      |
|                       | included                     | [ <oneOf>] | Resources related to the team memberships                                                                                                                                                                         |
| included              | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                  |
| Option 1              | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                    |
| attributes            | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                        |
| attributes            | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                     |
| attributes            | email                        | string          | Email of the user.                                                                                                                                                                                                |
| attributes            | handle                       | string          | Handle of the user.                                                                                                                                                                                               |
| attributes            | icon                         | string          | URL of the user's icon.                                                                                                                                                                                           |
| attributes            | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                 |
| attributes            | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                          |
| attributes            | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                             |
| attributes            | name                         | string          | Name of the user.                                                                                                                                                                                                 |
| attributes            | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                            |
| attributes            | status                       | string          | Status of the user.                                                                                                                                                                                               |
| attributes            | title                        | string          | Title of the user.                                                                                                                                                                                                |
| attributes            | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                     |
| Option 1              | id                           | string          | ID of the user.                                                                                                                                                                                                   |
| Option 1              | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                             |
| relationships         | org                          | object          | Relationship to an organization.                                                                                                                                                                                  |
| org                   | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                              |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                    |
| other_orgs            | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                            |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_users                  | object          | Relationship to users.                                                                                                                                                                                            |
| other_users           | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                    |
| data                  | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                     |
| data                  | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| relationships         | roles                        | object          | Relationship to roles.                                                                                                                                                                                            |
| roles                 | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                     |
| data                  | id                           | string          | The unique identifier of the role.                                                                                                                                                                                |
| data                  | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                          |
| Option 1              | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| included              | Option 2                     | object          | A team                                                                                                                                                                                                            |
| Option 2              | attributes [*required*] | object          | Team attributes                                                                                                                                                                                                   |
| attributes            | avatar                       | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                   |
| attributes            | banner                       | int64           | Banner selection for the team                                                                                                                                                                                     |
| attributes            | created_at                   | date-time       | Creation date of the team                                                                                                                                                                                         |
| attributes            | description                  | string          | Free-form markdown description/content for the team's homepage                                                                                                                                                    |
| attributes            | handle [*required*]     | string          | The team's identifier                                                                                                                                                                                             |
| attributes            | hidden_modules               | [string]        | Collection of hidden modules for the team                                                                                                                                                                         |
| attributes            | is_managed                   | boolean         | Whether the team is managed from an external source                                                                                                                                                               |
| attributes            | link_count                   | int32           | The number of links belonging to the team                                                                                                                                                                         |
| attributes            | modified_at                  | date-time       | Modification date of the team                                                                                                                                                                                     |
| attributes            | name [*required*]       | string          | The name of the team                                                                                                                                                                                              |
| attributes            | summary                      | string          | A brief summary of the team, derived from the `description`                                                                                                                                                       |
| attributes            | user_count                   | int32           | The number of users belonging to the team                                                                                                                                                                         |
| attributes            | visible_modules              | [string]        | Collection of visible modules for the team                                                                                                                                                                        |
| Option 2              | id [*required*]         | string          | The team's identifier                                                                                                                                                                                             |
| Option 2              | relationships                | object          | Resources related to a team                                                                                                                                                                                       |
| relationships         | team_links                   | object          | Relationship between a team and a team link                                                                                                                                                                       |
| team_links            | data                         | [object]        | Related team links                                                                                                                                                                                                |
| data                  | id [*required*]         | string          | The team link's identifier                                                                                                                                                                                        |
| data                  | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                                                                                                                                  |
| team_links            | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| relationships         | user_team_permissions        | object          | Relationship between a user team permission and a team                                                                                                                                                            |
| user_team_permissions | data                         | object          | Related user team permission data                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user team permission                                                                                                                                                                                |
| data                  | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                                                                                                                                            |
| user_team_permissions | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| Option 2              | type [*required*]       | enum            | Team type Allowed enum values: `team`                                                                                                                                                                             |
|                       | links                        | object          | Teams response links.                                                                                                                                                                                             |
| links                 | first                        | string          | First link.                                                                                                                                                                                                       |
| links                 | last                         | string          | Last link.                                                                                                                                                                                                        |
| links                 | next                         | string          | Next link.                                                                                                                                                                                                        |
| links                 | prev                         | string          | Previous link.                                                                                                                                                                                                    |
| links                 | self                         | string          | Current link.                                                                                                                                                                                                     |
|                       | meta                         | object          | Teams response metadata.                                                                                                                                                                                          |
| meta                  | pagination                   | object          | Teams response metadata.                                                                                                                                                                                          |
| pagination            | first_offset                 | int64           | The first offset.                                                                                                                                                                                                 |
| pagination            | last_offset                  | int64           | The last offset.                                                                                                                                                                                                  |
| pagination            | limit                        | int64           | Pagination limit.                                                                                                                                                                                                 |
| pagination            | next_offset                  | int64           | The next offset.                                                                                                                                                                                                  |
| pagination            | offset                       | int64           | The offset.                                                                                                                                                                                                       |
| pagination            | prev_offset                  | int64           | The previous offset.                                                                                                                                                                                              |
| pagination            | total                        | int64           | Total results.                                                                                                                                                                                                    |
| pagination            | type                         | string          | Offset type.                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "provisioned_by": "string",
        "provisioned_by_id": "string",
        "role": "string"
      },
      "id": "TeamMembership-aeadc05e-98a8-11ec-ac2c-da7ad0900001-38835",
      "relationships": {
        "team": {
          "data": {
            "id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
            "type": "team"
          }
        },
        "user": {
          "data": {
            "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
            "type": "users"
          }
        }
      },
      "type": "team_memberships"
    }
  ],
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "pagination": {
      "first_offset": "integer",
      "last_offset": "integer",
      "limit": "integer",
      "next_offset": "integer",
      "offset": "integer",
      "prev_offset": "integer",
      "total": "integer",
      "type": "string"
    }
  }
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get team memberships returns "Represents a user's association to a team" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_memberships(
        team_id=DD_TEAM_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get team memberships returns "Represents a user's association to a team" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team_memberships(DD_TEAM_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get team memberships returns "Represents a user's association to a team" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamMemberships(ctx, DdTeamDataID, *datadogV2.NewGetTeamMembershipsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamMemberships`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamMemberships`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get team memberships returns "Represents a user's association to a team" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.UserTeamsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    try {
      UserTeamsResponse result = apiInstance.getTeamMemberships(DD_TEAM_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamMemberships");
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
// Get team memberships returns "Represents a user's association to a team"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::GetTeamMembershipsOptionalParams;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .get_team_memberships(
            dd_team_data_id.clone(),
            GetTeamMembershipsOptionalParams::default(),
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
 * Get team memberships returns "Represents a user's association to a team" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiGetTeamMembershipsRequest = {
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .getTeamMemberships(params)
  .then((data: v2.UserTeamsResponse) => {
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

## Add a user to a team{% #add-a-user-to-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team/{team_id}/memberships |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team/{team_id}/memberships |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team/{team_id}/memberships      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team/{team_id}/memberships      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team/{team_id}/memberships     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team/{team_id}/memberships |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships |

### Overview

Add a user to a team.

**Note**: Each team has a setting that determines who is allowed to modify membership of the team. The `user_access_manage` permission generally grants access to modify membership of any team. To get the full picture, see [Team Membership documentation](https://docs.datadoghq.com/account_management/teams/manage/#team-membership).
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field  | Field                  | Type   | Description                                                                                                                                                                                                       |
| ------------- | ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data [*required*] | object | A user's relationship with a team                                                                                                                                                                                 |
| data          | attributes             | object | Team membership attributes                                                                                                                                                                                        |
| attributes    | provisioned_by         | string | The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping. |
| attributes    | provisioned_by_id      | string | UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.                                                                                                |
| attributes    | role                   | enum   | The user's role within the team Allowed enum values: `admin`                                                                                                                                                      |
| data          | relationships          | object | Relationship between membership and a user                                                                                                                                                                        |
| relationships | team                   | object | Relationship between team membership and team                                                                                                                                                                     |
| team          | data [*required*] | object | The team associated with the membership                                                                                                                                                                           |
| data          | id [*required*]   | string | The ID of the team associated with the membership                                                                                                                                                                 |
| data          | type [*required*] | enum   | User team team type Allowed enum values: `team`                                                                                                                                                                   |
| relationships | user                   | object | Relationship between team membership and user                                                                                                                                                                     |
| user          | data [*required*] | object | A user's relationship with a team                                                                                                                                                                                 |
| data          | id [*required*]   | string | The ID of the user associated with the team                                                                                                                                                                       |
| data          | type [*required*] | enum   | User team user type Allowed enum values: `users`                                                                                                                                                                  |
| data          | type [*required*] | enum   | Team membership type Allowed enum values: `team_memberships`                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "role": "string"
    },
    "relationships": {
      "team": {
        "data": {
          "id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
          "type": "team"
        }
      },
      "user": {
        "data": {
          "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
          "type": "users"
        }
      }
    },
    "type": "team_memberships"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Represents a user's association to a team
{% tab title="Model" %}
Team membership response

| Parent field          | Field                        | Type            | Description                                                                                                                                                                                                       |
| --------------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                         | object          | A user's relationship with a team                                                                                                                                                                                 |
| data                  | attributes                   | object          | Team membership attributes                                                                                                                                                                                        |
| attributes            | provisioned_by               | string          | The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping. |
| attributes            | provisioned_by_id            | string          | UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.                                                                                                |
| attributes            | role                         | enum            | The user's role within the team Allowed enum values: `admin`                                                                                                                                                      |
| data                  | id [*required*]         | string          | The ID of a user's relationship with a team                                                                                                                                                                       |
| data                  | relationships                | object          | Relationship between membership and a user                                                                                                                                                                        |
| relationships         | team                         | object          | Relationship between team membership and team                                                                                                                                                                     |
| team                  | data [*required*]       | object          | The team associated with the membership                                                                                                                                                                           |
| data                  | id [*required*]         | string          | The ID of the team associated with the membership                                                                                                                                                                 |
| data                  | type [*required*]       | enum            | User team team type Allowed enum values: `team`                                                                                                                                                                   |
| relationships         | user                         | object          | Relationship between team membership and user                                                                                                                                                                     |
| user                  | data [*required*]       | object          | A user's relationship with a team                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user associated with the team                                                                                                                                                                       |
| data                  | type [*required*]       | enum            | User team user type Allowed enum values: `users`                                                                                                                                                                  |
| data                  | type [*required*]       | enum            | Team membership type Allowed enum values: `team_memberships`                                                                                                                                                      |
|                       | included                     | [ <oneOf>] | Resources related to the team memberships                                                                                                                                                                         |
| included              | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                  |
| Option 1              | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                    |
| attributes            | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                        |
| attributes            | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                     |
| attributes            | email                        | string          | Email of the user.                                                                                                                                                                                                |
| attributes            | handle                       | string          | Handle of the user.                                                                                                                                                                                               |
| attributes            | icon                         | string          | URL of the user's icon.                                                                                                                                                                                           |
| attributes            | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                 |
| attributes            | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                          |
| attributes            | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                             |
| attributes            | name                         | string          | Name of the user.                                                                                                                                                                                                 |
| attributes            | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                            |
| attributes            | status                       | string          | Status of the user.                                                                                                                                                                                               |
| attributes            | title                        | string          | Title of the user.                                                                                                                                                                                                |
| attributes            | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                     |
| Option 1              | id                           | string          | ID of the user.                                                                                                                                                                                                   |
| Option 1              | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                             |
| relationships         | org                          | object          | Relationship to an organization.                                                                                                                                                                                  |
| org                   | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                              |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                    |
| other_orgs            | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                            |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_users                  | object          | Relationship to users.                                                                                                                                                                                            |
| other_users           | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                    |
| data                  | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                     |
| data                  | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| relationships         | roles                        | object          | Relationship to roles.                                                                                                                                                                                            |
| roles                 | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                     |
| data                  | id                           | string          | The unique identifier of the role.                                                                                                                                                                                |
| data                  | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                          |
| Option 1              | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| included              | Option 2                     | object          | A team                                                                                                                                                                                                            |
| Option 2              | attributes [*required*] | object          | Team attributes                                                                                                                                                                                                   |
| attributes            | avatar                       | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                   |
| attributes            | banner                       | int64           | Banner selection for the team                                                                                                                                                                                     |
| attributes            | created_at                   | date-time       | Creation date of the team                                                                                                                                                                                         |
| attributes            | description                  | string          | Free-form markdown description/content for the team's homepage                                                                                                                                                    |
| attributes            | handle [*required*]     | string          | The team's identifier                                                                                                                                                                                             |
| attributes            | hidden_modules               | [string]        | Collection of hidden modules for the team                                                                                                                                                                         |
| attributes            | is_managed                   | boolean         | Whether the team is managed from an external source                                                                                                                                                               |
| attributes            | link_count                   | int32           | The number of links belonging to the team                                                                                                                                                                         |
| attributes            | modified_at                  | date-time       | Modification date of the team                                                                                                                                                                                     |
| attributes            | name [*required*]       | string          | The name of the team                                                                                                                                                                                              |
| attributes            | summary                      | string          | A brief summary of the team, derived from the `description`                                                                                                                                                       |
| attributes            | user_count                   | int32           | The number of users belonging to the team                                                                                                                                                                         |
| attributes            | visible_modules              | [string]        | Collection of visible modules for the team                                                                                                                                                                        |
| Option 2              | id [*required*]         | string          | The team's identifier                                                                                                                                                                                             |
| Option 2              | relationships                | object          | Resources related to a team                                                                                                                                                                                       |
| relationships         | team_links                   | object          | Relationship between a team and a team link                                                                                                                                                                       |
| team_links            | data                         | [object]        | Related team links                                                                                                                                                                                                |
| data                  | id [*required*]         | string          | The team link's identifier                                                                                                                                                                                        |
| data                  | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                                                                                                                                  |
| team_links            | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| relationships         | user_team_permissions        | object          | Relationship between a user team permission and a team                                                                                                                                                            |
| user_team_permissions | data                         | object          | Related user team permission data                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user team permission                                                                                                                                                                                |
| data                  | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                                                                                                                                            |
| user_team_permissions | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| Option 2              | type [*required*]       | enum            | Team type Allowed enum values: `team`                                                                                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "provisioned_by": "string",
      "provisioned_by_id": "string",
      "role": "string"
    },
    "id": "TeamMembership-aeadc05e-98a8-11ec-ac2c-da7ad0900001-38835",
    "relationships": {
      "team": {
        "data": {
          "id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
          "type": "team"
        }
      },
      "user": {
        "data": {
          "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
          "type": "users"
        }
      }
    },
    "type": "team_memberships"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
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
API error response.
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "relationships": {
      "team": {
        "data": {
          "id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
          "type": "team"
        }
      },
      "user": {
        "data": {
          "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
          "type": "users"
        }
      }
    },
    "type": "team_memberships"
  }
}
EOF

#####

```python
"""
Add a user to a team returns "Represents a user's association to a team" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.relationship_to_user_team_team import RelationshipToUserTeamTeam
from datadog_api_client.v2.model.relationship_to_user_team_team_data import RelationshipToUserTeamTeamData
from datadog_api_client.v2.model.relationship_to_user_team_user import RelationshipToUserTeamUser
from datadog_api_client.v2.model.relationship_to_user_team_user_data import RelationshipToUserTeamUserData
from datadog_api_client.v2.model.user_team_attributes import UserTeamAttributes
from datadog_api_client.v2.model.user_team_create import UserTeamCreate
from datadog_api_client.v2.model.user_team_relationships import UserTeamRelationships
from datadog_api_client.v2.model.user_team_request import UserTeamRequest
from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_team_type import UserTeamTeamType
from datadog_api_client.v2.model.user_team_type import UserTeamType
from datadog_api_client.v2.model.user_team_user_type import UserTeamUserType

body = UserTeamRequest(
    data=UserTeamCreate(
        attributes=UserTeamAttributes(
            role=UserTeamRole.ADMIN,
        ),
        relationships=UserTeamRelationships(
            team=RelationshipToUserTeamTeam(
                data=RelationshipToUserTeamTeamData(
                    id="d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
                    type=UserTeamTeamType.TEAM,
                ),
            ),
            user=RelationshipToUserTeamUser(
                data=RelationshipToUserTeamUserData(
                    id="b8626d7e-cedd-11eb-abf5-da7ad0900001",
                    type=UserTeamUserType.USERS,
                ),
            ),
        ),
        type=UserTeamType.TEAM_MEMBERSHIPS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_membership(team_id="team_id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Add a user to a team returns "Represents a user's association to a team" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::UserTeamRequest.new({
  data: DatadogAPIClient::V2::UserTeamCreate.new({
    attributes: DatadogAPIClient::V2::UserTeamAttributes.new({
      role: DatadogAPIClient::V2::UserTeamRole::ADMIN,
    }),
    relationships: DatadogAPIClient::V2::UserTeamRelationships.new({
      team: DatadogAPIClient::V2::RelationshipToUserTeamTeam.new({
        data: DatadogAPIClient::V2::RelationshipToUserTeamTeamData.new({
          id: "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
          type: DatadogAPIClient::V2::UserTeamTeamType::TEAM,
        }),
      }),
      user: DatadogAPIClient::V2::RelationshipToUserTeamUser.new({
        data: DatadogAPIClient::V2::RelationshipToUserTeamUserData.new({
          id: "b8626d7e-cedd-11eb-abf5-da7ad0900001",
          type: DatadogAPIClient::V2::UserTeamUserType::USERS,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::UserTeamType::TEAM_MEMBERSHIPS,
  }),
})
p api_instance.create_team_membership("team_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Add a user to a team returns "Represents a user's association to a team" response

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
    body := datadogV2.UserTeamRequest{
        Data: datadogV2.UserTeamCreate{
            Attributes: &datadogV2.UserTeamAttributes{
                Role: *datadogV2.NewNullableUserTeamRole(datadogV2.USERTEAMROLE_ADMIN.Ptr()),
            },
            Relationships: &datadogV2.UserTeamRelationships{
                Team: &datadogV2.RelationshipToUserTeamTeam{
                    Data: datadogV2.RelationshipToUserTeamTeamData{
                        Id:   "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
                        Type: datadogV2.USERTEAMTEAMTYPE_TEAM,
                    },
                },
                User: &datadogV2.RelationshipToUserTeamUser{
                    Data: datadogV2.RelationshipToUserTeamUserData{
                        Id:   "b8626d7e-cedd-11eb-abf5-da7ad0900001",
                        Type: datadogV2.USERTEAMUSERTYPE_USERS,
                    },
                },
            },
            Type: datadogV2.USERTEAMTYPE_TEAM_MEMBERSHIPS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.CreateTeamMembership(ctx, "team_id", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.CreateTeamMembership`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.CreateTeamMembership`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Add a user to a team returns "Represents a user's association to a team" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.RelationshipToUserTeamTeam;
import com.datadog.api.client.v2.model.RelationshipToUserTeamTeamData;
import com.datadog.api.client.v2.model.RelationshipToUserTeamUser;
import com.datadog.api.client.v2.model.RelationshipToUserTeamUserData;
import com.datadog.api.client.v2.model.UserTeamAttributes;
import com.datadog.api.client.v2.model.UserTeamCreate;
import com.datadog.api.client.v2.model.UserTeamRelationships;
import com.datadog.api.client.v2.model.UserTeamRequest;
import com.datadog.api.client.v2.model.UserTeamResponse;
import com.datadog.api.client.v2.model.UserTeamRole;
import com.datadog.api.client.v2.model.UserTeamTeamType;
import com.datadog.api.client.v2.model.UserTeamType;
import com.datadog.api.client.v2.model.UserTeamUserType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    UserTeamRequest body =
        new UserTeamRequest()
            .data(
                new UserTeamCreate()
                    .attributes(new UserTeamAttributes().role(UserTeamRole.ADMIN))
                    .relationships(
                        new UserTeamRelationships()
                            .team(
                                new RelationshipToUserTeamTeam()
                                    .data(
                                        new RelationshipToUserTeamTeamData()
                                            .id("d7e15d9d-d346-43da-81d8-3d9e71d9a5e9")
                                            .type(UserTeamTeamType.TEAM)))
                            .user(
                                new RelationshipToUserTeamUser()
                                    .data(
                                        new RelationshipToUserTeamUserData()
                                            .id("b8626d7e-cedd-11eb-abf5-da7ad0900001")
                                            .type(UserTeamUserType.USERS))))
                    .type(UserTeamType.TEAM_MEMBERSHIPS));

    try {
      UserTeamResponse result = apiInstance.createTeamMembership("team_id", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#createTeamMembership");
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
// Add a user to a team returns "Represents a user's association to a team"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::RelationshipToUserTeamTeam;
use datadog_api_client::datadogV2::model::RelationshipToUserTeamTeamData;
use datadog_api_client::datadogV2::model::RelationshipToUserTeamUser;
use datadog_api_client::datadogV2::model::RelationshipToUserTeamUserData;
use datadog_api_client::datadogV2::model::UserTeamAttributes;
use datadog_api_client::datadogV2::model::UserTeamCreate;
use datadog_api_client::datadogV2::model::UserTeamRelationships;
use datadog_api_client::datadogV2::model::UserTeamRequest;
use datadog_api_client::datadogV2::model::UserTeamRole;
use datadog_api_client::datadogV2::model::UserTeamTeamType;
use datadog_api_client::datadogV2::model::UserTeamType;
use datadog_api_client::datadogV2::model::UserTeamUserType;

#[tokio::main]
async fn main() {
    let body = UserTeamRequest::new(
        UserTeamCreate::new(UserTeamType::TEAM_MEMBERSHIPS)
            .attributes(UserTeamAttributes::new().role(Some(UserTeamRole::ADMIN)))
            .relationships(
                UserTeamRelationships::new()
                    .team(RelationshipToUserTeamTeam::new(
                        RelationshipToUserTeamTeamData::new(
                            "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9".to_string(),
                            UserTeamTeamType::TEAM,
                        ),
                    ))
                    .user(RelationshipToUserTeamUser::new(
                        RelationshipToUserTeamUserData::new(
                            "b8626d7e-cedd-11eb-abf5-da7ad0900001".to_string(),
                            UserTeamUserType::USERS,
                        ),
                    )),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .create_team_membership("team_id".to_string(), body)
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
 * Add a user to a team returns "Represents a user's association to a team" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiCreateTeamMembershipRequest = {
  body: {
    data: {
      attributes: {
        role: "admin",
      },
      relationships: {
        team: {
          data: {
            id: "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
            type: "team",
          },
        },
        user: {
          data: {
            id: "b8626d7e-cedd-11eb-abf5-da7ad0900001",
            type: "users",
          },
        },
      },
      type: "team_memberships",
    },
  },
  teamId: "team_id",
};

apiInstance
  .createTeamMembership(params)
  .then((data: v2.UserTeamResponse) => {
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

## Remove a user from a team{% #remove-a-user-from-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/team/{team_id}/memberships/{user_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/team/{team_id}/memberships/{user_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |

### Overview

Remove a user from a team.

**Note**: Each team has a setting that determines who is allowed to modify membership of the team. The `user_access_manage` permission generally grants access to modify membership of any team. To get the full picture, see [Team Membership documentation](https://docs.datadoghq.com/account_management/teams/manage/#team-membership).
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| user_id [*required*] | string | None        |

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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"export user_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships/${user_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove a user from a team returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team_membership(
        team_id=DD_TEAM_DATA_ID,
        user_id="user_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Remove a user from a team returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
api_instance.delete_team_membership(DD_TEAM_DATA_ID, "user_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Remove a user from a team returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.DeleteTeamMembership(ctx, DdTeamDataID, "user_id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.DeleteTeamMembership`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Remove a user from a team returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    try {
      apiInstance.deleteTeamMembership(DD_TEAM_DATA_ID, "user_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#deleteTeamMembership");
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
// Remove a user from a team returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .delete_team_membership(dd_team_data_id.clone(), "user_id".to_string())
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
 * Remove a user from a team returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiDeleteTeamMembershipRequest = {
  teamId: DD_TEAM_DATA_ID,
  userId: "user_id",
};

apiInstance
  .deleteTeamMembership(params)
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

## Update a user's membership attributes on a team{% #update-a-users-membership-attributes-on-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/team/{team_id}/memberships/{user_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/team/{team_id}/memberships/{user_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id} |

### Overview

Update a user's membership attributes on a team.

**Note**: Each team has a setting that determines who is allowed to modify membership of the team. The `user_access_manage` permission generally grants access to modify membership of any team. To get the full picture, see [Team Membership documentation](https://docs.datadoghq.com/account_management/teams/manage/#team-membership).
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| user_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                                                                                                                                                                       |
| ------------ | ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | A user's relationship with a team                                                                                                                                                                                 |
| data         | attributes             | object | Team membership attributes                                                                                                                                                                                        |
| attributes   | provisioned_by         | string | The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping. |
| attributes   | provisioned_by_id      | string | UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.                                                                                                |
| attributes   | role                   | enum   | The user's role within the team Allowed enum values: `admin`                                                                                                                                                      |
| data         | type [*required*] | enum   | Team membership type Allowed enum values: `team_memberships`                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "role": "admin"
    },
    "type": "team_memberships"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team membership response

| Parent field          | Field                        | Type            | Description                                                                                                                                                                                                       |
| --------------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                         | object          | A user's relationship with a team                                                                                                                                                                                 |
| data                  | attributes                   | object          | Team membership attributes                                                                                                                                                                                        |
| attributes            | provisioned_by               | string          | The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping. |
| attributes            | provisioned_by_id            | string          | UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.                                                                                                |
| attributes            | role                         | enum            | The user's role within the team Allowed enum values: `admin`                                                                                                                                                      |
| data                  | id [*required*]         | string          | The ID of a user's relationship with a team                                                                                                                                                                       |
| data                  | relationships                | object          | Relationship between membership and a user                                                                                                                                                                        |
| relationships         | team                         | object          | Relationship between team membership and team                                                                                                                                                                     |
| team                  | data [*required*]       | object          | The team associated with the membership                                                                                                                                                                           |
| data                  | id [*required*]         | string          | The ID of the team associated with the membership                                                                                                                                                                 |
| data                  | type [*required*]       | enum            | User team team type Allowed enum values: `team`                                                                                                                                                                   |
| relationships         | user                         | object          | Relationship between team membership and user                                                                                                                                                                     |
| user                  | data [*required*]       | object          | A user's relationship with a team                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user associated with the team                                                                                                                                                                       |
| data                  | type [*required*]       | enum            | User team user type Allowed enum values: `users`                                                                                                                                                                  |
| data                  | type [*required*]       | enum            | Team membership type Allowed enum values: `team_memberships`                                                                                                                                                      |
|                       | included                     | [ <oneOf>] | Resources related to the team memberships                                                                                                                                                                         |
| included              | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                  |
| Option 1              | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                    |
| attributes            | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                        |
| attributes            | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                     |
| attributes            | email                        | string          | Email of the user.                                                                                                                                                                                                |
| attributes            | handle                       | string          | Handle of the user.                                                                                                                                                                                               |
| attributes            | icon                         | string          | URL of the user's icon.                                                                                                                                                                                           |
| attributes            | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                 |
| attributes            | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                          |
| attributes            | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                             |
| attributes            | name                         | string          | Name of the user.                                                                                                                                                                                                 |
| attributes            | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                            |
| attributes            | status                       | string          | Status of the user.                                                                                                                                                                                               |
| attributes            | title                        | string          | Title of the user.                                                                                                                                                                                                |
| attributes            | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                     |
| Option 1              | id                           | string          | ID of the user.                                                                                                                                                                                                   |
| Option 1              | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                             |
| relationships         | org                          | object          | Relationship to an organization.                                                                                                                                                                                  |
| org                   | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                              |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                    |
| other_orgs            | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                            |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_users                  | object          | Relationship to users.                                                                                                                                                                                            |
| other_users           | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                    |
| data                  | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                     |
| data                  | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| relationships         | roles                        | object          | Relationship to roles.                                                                                                                                                                                            |
| roles                 | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                     |
| data                  | id                           | string          | The unique identifier of the role.                                                                                                                                                                                |
| data                  | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                          |
| Option 1              | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| included              | Option 2                     | object          | A team                                                                                                                                                                                                            |
| Option 2              | attributes [*required*] | object          | Team attributes                                                                                                                                                                                                   |
| attributes            | avatar                       | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                   |
| attributes            | banner                       | int64           | Banner selection for the team                                                                                                                                                                                     |
| attributes            | created_at                   | date-time       | Creation date of the team                                                                                                                                                                                         |
| attributes            | description                  | string          | Free-form markdown description/content for the team's homepage                                                                                                                                                    |
| attributes            | handle [*required*]     | string          | The team's identifier                                                                                                                                                                                             |
| attributes            | hidden_modules               | [string]        | Collection of hidden modules for the team                                                                                                                                                                         |
| attributes            | is_managed                   | boolean         | Whether the team is managed from an external source                                                                                                                                                               |
| attributes            | link_count                   | int32           | The number of links belonging to the team                                                                                                                                                                         |
| attributes            | modified_at                  | date-time       | Modification date of the team                                                                                                                                                                                     |
| attributes            | name [*required*]       | string          | The name of the team                                                                                                                                                                                              |
| attributes            | summary                      | string          | A brief summary of the team, derived from the `description`                                                                                                                                                       |
| attributes            | user_count                   | int32           | The number of users belonging to the team                                                                                                                                                                         |
| attributes            | visible_modules              | [string]        | Collection of visible modules for the team                                                                                                                                                                        |
| Option 2              | id [*required*]         | string          | The team's identifier                                                                                                                                                                                             |
| Option 2              | relationships                | object          | Resources related to a team                                                                                                                                                                                       |
| relationships         | team_links                   | object          | Relationship between a team and a team link                                                                                                                                                                       |
| team_links            | data                         | [object]        | Related team links                                                                                                                                                                                                |
| data                  | id [*required*]         | string          | The team link's identifier                                                                                                                                                                                        |
| data                  | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                                                                                                                                  |
| team_links            | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| relationships         | user_team_permissions        | object          | Relationship between a user team permission and a team                                                                                                                                                            |
| user_team_permissions | data                         | object          | Related user team permission data                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user team permission                                                                                                                                                                                |
| data                  | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                                                                                                                                            |
| user_team_permissions | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| Option 2              | type [*required*]       | enum            | Team type Allowed enum values: `team`                                                                                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "provisioned_by": "string",
      "provisioned_by_id": "string",
      "role": "string"
    },
    "id": "TeamMembership-aeadc05e-98a8-11ec-ac2c-da7ad0900001-38835",
    "relationships": {
      "team": {
        "data": {
          "id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
          "type": "team"
        }
      },
      "user": {
        "data": {
          "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
          "type": "users"
        }
      }
    },
    "type": "team_memberships"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
API error response.
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
API error response.
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
                          \# Path parametersexport team_id="CHANGE_ME"export user_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships/${user_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "role": "admin"
    },
    "type": "team_memberships"
  }
}
EOF

#####

```go
// Update a user's membership attributes on a team returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "user" in the system
    UserDataID := os.Getenv("USER_DATA_ID")

    body := datadogV2.UserTeamUpdateRequest{
        Data: datadogV2.UserTeamUpdate{
            Attributes: &datadogV2.UserTeamAttributes{
                Role: *datadogV2.NewNullableUserTeamRole(datadogV2.USERTEAMROLE_ADMIN.Ptr()),
            },
            Type: datadogV2.USERTEAMTYPE_TEAM_MEMBERSHIPS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.UpdateTeamMembership(ctx, DdTeamDataID, UserDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.UpdateTeamMembership`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.UpdateTeamMembership`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update a user's membership attributes on a team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.UserTeamAttributes;
import com.datadog.api.client.v2.model.UserTeamResponse;
import com.datadog.api.client.v2.model.UserTeamRole;
import com.datadog.api.client.v2.model.UserTeamType;
import com.datadog.api.client.v2.model.UserTeamUpdate;
import com.datadog.api.client.v2.model.UserTeamUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    UserTeamUpdateRequest body =
        new UserTeamUpdateRequest()
            .data(
                new UserTeamUpdate()
                    .attributes(new UserTeamAttributes().role(UserTeamRole.ADMIN))
                    .type(UserTeamType.TEAM_MEMBERSHIPS));

    try {
      UserTeamResponse result =
          apiInstance.updateTeamMembership(DD_TEAM_DATA_ID, USER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#updateTeamMembership");
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
Update a user's membership attributes on a team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.user_team_attributes import UserTeamAttributes
from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_type import UserTeamType
from datadog_api_client.v2.model.user_team_update import UserTeamUpdate
from datadog_api_client.v2.model.user_team_update_request import UserTeamUpdateRequest

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserTeamUpdateRequest(
    data=UserTeamUpdate(
        attributes=UserTeamAttributes(
            role=UserTeamRole.ADMIN,
        ),
        type=UserTeamType.TEAM_MEMBERSHIPS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_membership(team_id=DD_TEAM_DATA_ID, user_id=USER_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update a user's membership attributes on a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::UserTeamUpdateRequest.new({
  data: DatadogAPIClient::V2::UserTeamUpdate.new({
    attributes: DatadogAPIClient::V2::UserTeamAttributes.new({
      role: DatadogAPIClient::V2::UserTeamRole::ADMIN,
    }),
    type: DatadogAPIClient::V2::UserTeamType::TEAM_MEMBERSHIPS,
  }),
})
p api_instance.update_team_membership(DD_TEAM_DATA_ID, USER_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update a user's membership attributes on a team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::UserTeamAttributes;
use datadog_api_client::datadogV2::model::UserTeamRole;
use datadog_api_client::datadogV2::model::UserTeamType;
use datadog_api_client::datadogV2::model::UserTeamUpdate;
use datadog_api_client::datadogV2::model::UserTeamUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = UserTeamUpdateRequest::new(
        UserTeamUpdate::new(UserTeamType::TEAM_MEMBERSHIPS)
            .attributes(UserTeamAttributes::new().role(Some(UserTeamRole::ADMIN))),
    );
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .update_team_membership(dd_team_data_id.clone(), user_data_id.clone(), body)
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
 * Update a user's membership attributes on a team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.TeamsApiUpdateTeamMembershipRequest = {
  body: {
    data: {
      attributes: {
        role: "admin",
      },
      type: "team_memberships",
    },
  },
  teamId: DD_TEAM_DATA_ID,
  userId: USER_DATA_ID,
};

apiInstance
  .updateTeamMembership(params)
  .then((data: v2.UserTeamResponse) => {
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

## Get links for a team{% #get-links-for-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{team_id}/links      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{team_id}/links      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{team_id}/links     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{team_id}/links |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{team_id}/links |

### Overview

Get all links for a given team. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team links response

| Parent field | Field                        | Type     | Description                                          |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------- |
|              | data                         | [object] | Team links response data                             |
| data         | attributes [*required*] | object   | Team link attributes                                 |
| attributes   | label [*required*]      | string   | The link's label                                     |
| attributes   | position                     | int32    | The link's position, used to sort links for the team |
| attributes   | team_id                      | string   | ID of the team the link is associated with           |
| attributes   | url [*required*]        | string   | The URL for the link                                 |
| data         | id [*required*]         | string   | The team link's identifier                           |
| data         | type [*required*]       | enum     | Team link type Allowed enum values: `team_links`     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "label": "Link label",
        "position": "integer",
        "team_id": "string",
        "url": "https://example.com"
      },
      "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
      "type": "team_links"
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get links for a team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_links(
        team_id=DD_TEAM_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get links for a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team_links(DD_TEAM_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get links for a team returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamLinks(ctx, DdTeamDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamLinks`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamLinks`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get links for a team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamLinksResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    try {
      TeamLinksResponse result = apiInstance.getTeamLinks(DD_TEAM_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamLinks");
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
// Get links for a team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.get_team_links(dd_team_data_id.clone()).await;
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
 * Get links for a team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiGetTeamLinksRequest = {
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .getTeamLinks(params)
  .then((data: v2.TeamLinksResponse) => {
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

## Create a team link{% #create-a-team-link %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team/{team_id}/links      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team/{team_id}/links      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team/{team_id}/links     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team/{team_id}/links |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team/{team_id}/links |

### Overview

Add a new link to a team. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                          |
| ------------ | ---------------------------- | ------ | ---------------------------------------------------- |
|              | data [*required*]       | object | Team link create                                     |
| data         | attributes [*required*] | object | Team link attributes                                 |
| attributes   | label [*required*]      | string | The link's label                                     |
| attributes   | position                     | int32  | The link's position, used to sort links for the team |
| attributes   | team_id                      | string | ID of the team the link is associated with           |
| attributes   | url [*required*]        | string | The URL for the link                                 |
| data         | type [*required*]       | enum   | Team link type Allowed enum values: `team_links`     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "label": "Link label",
      "url": "https://example.com",
      "position": 0
    },
    "type": "team_links"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team link response

| Parent field | Field                        | Type   | Description                                          |
| ------------ | ---------------------------- | ------ | ---------------------------------------------------- |
|              | data                         | object | Team link                                            |
| data         | attributes [*required*] | object | Team link attributes                                 |
| attributes   | label [*required*]      | string | The link's label                                     |
| attributes   | position                     | int32  | The link's position, used to sort links for the team |
| attributes   | team_id                      | string | ID of the team the link is associated with           |
| attributes   | url [*required*]        | string | The URL for the link                                 |
| data         | id [*required*]         | string | The team link's identifier                           |
| data         | type [*required*]       | enum   | Team link type Allowed enum values: `team_links`     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "label": "Link label",
      "position": "integer",
      "team_id": "string",
      "url": "https://example.com"
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "type": "team_links"
  }
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
API error response.
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

{% tab title="422" %}
API error response.
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
                          \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "label": "Link label",
      "url": "https://example.com",
      "position": 0
    },
    "type": "team_links"
  }
}
EOF

#####

```go
// Create a team link returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    body := datadogV2.TeamLinkCreateRequest{
        Data: datadogV2.TeamLinkCreate{
            Attributes: datadogV2.TeamLinkAttributes{
                Label:    "Link label",
                Url:      "https://example.com",
                Position: datadog.PtrInt32(0),
            },
            Type: datadogV2.TEAMLINKTYPE_TEAM_LINKS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.CreateTeamLink(ctx, DdTeamDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.CreateTeamLink`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.CreateTeamLink`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a team link returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamLinkAttributes;
import com.datadog.api.client.v2.model.TeamLinkCreate;
import com.datadog.api.client.v2.model.TeamLinkCreateRequest;
import com.datadog.api.client.v2.model.TeamLinkResponse;
import com.datadog.api.client.v2.model.TeamLinkType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    TeamLinkCreateRequest body =
        new TeamLinkCreateRequest()
            .data(
                new TeamLinkCreate()
                    .attributes(
                        new TeamLinkAttributes()
                            .label("Link label")
                            .url("https://example.com")
                            .position(0))
                    .type(TeamLinkType.TEAM_LINKS));

    try {
      TeamLinkResponse result = apiInstance.createTeamLink(DD_TEAM_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#createTeamLink");
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
Create a team link returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_link_attributes import TeamLinkAttributes
from datadog_api_client.v2.model.team_link_create import TeamLinkCreate
from datadog_api_client.v2.model.team_link_create_request import TeamLinkCreateRequest
from datadog_api_client.v2.model.team_link_type import TeamLinkType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamLinkCreateRequest(
    data=TeamLinkCreate(
        attributes=TeamLinkAttributes(
            label="Link label",
            url="https://example.com",
            position=0,
        ),
        type=TeamLinkType.TEAM_LINKS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_link(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a team link returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::TeamLinkCreateRequest.new({
  data: DatadogAPIClient::V2::TeamLinkCreate.new({
    attributes: DatadogAPIClient::V2::TeamLinkAttributes.new({
      label: "Link label",
      url: "https://example.com",
      position: 0,
    }),
    type: DatadogAPIClient::V2::TeamLinkType::TEAM_LINKS,
  }),
})
p api_instance.create_team_link(DD_TEAM_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create a team link returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamLinkAttributes;
use datadog_api_client::datadogV2::model::TeamLinkCreate;
use datadog_api_client::datadogV2::model::TeamLinkCreateRequest;
use datadog_api_client::datadogV2::model::TeamLinkType;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = TeamLinkCreateRequest::new(TeamLinkCreate::new(
        TeamLinkAttributes::new("Link label".to_string(), "https://example.com".to_string())
            .position(0),
        TeamLinkType::TEAM_LINKS,
    ));
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.create_team_link(dd_team_data_id.clone(), body).await;
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
 * Create a team link returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiCreateTeamLinkRequest = {
  body: {
    data: {
      attributes: {
        label: "Link label",
        url: "https://example.com",
        position: 0,
      },
      type: "team_links",
    },
  },
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .createTeamLink(params)
  .then((data: v2.TeamLinkResponse) => {
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

## Get a team link{% #get-a-team-link %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{team_id}/links/{link_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{team_id}/links/{link_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{team_id}/links/{link_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |

### Overview

Get a single link for a team. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| link_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team link response

| Parent field | Field                        | Type   | Description                                          |
| ------------ | ---------------------------- | ------ | ---------------------------------------------------- |
|              | data                         | object | Team link                                            |
| data         | attributes [*required*] | object | Team link attributes                                 |
| attributes   | label [*required*]      | string | The link's label                                     |
| attributes   | position                     | int32  | The link's position, used to sort links for the team |
| attributes   | team_id                      | string | ID of the team the link is associated with           |
| attributes   | url [*required*]        | string | The URL for the link                                 |
| data         | id [*required*]         | string | The team link's identifier                           |
| data         | type [*required*]       | enum   | Team link type Allowed enum values: `team_links`     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "label": "Link label",
      "position": "integer",
      "team_id": "string",
      "url": "https://example.com"
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "type": "team_links"
  }
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"export link_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links/${link_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a team link returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = environ["TEAM_LINK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_link(
        team_id=DD_TEAM_DATA_ID,
        link_id=TEAM_LINK_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a team link returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = ENV["TEAM_LINK_DATA_ID"]
p api_instance.get_team_link(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a team link returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "team_link" in the system
    TeamLinkDataID := os.Getenv("TEAM_LINK_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamLink(ctx, DdTeamDataID, TeamLinkDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamLink`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamLink`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a team link returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamLinkResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "team_link" in the system
    String TEAM_LINK_DATA_ID = System.getenv("TEAM_LINK_DATA_ID");

    try {
      TeamLinkResponse result = apiInstance.getTeamLink(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamLink");
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
// Get a team link returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "team_link" in the system
    let team_link_data_id = std::env::var("TEAM_LINK_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .get_team_link(dd_team_data_id.clone(), team_link_data_id.clone())
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
 * Get a team link returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "team_link" in the system
const TEAM_LINK_DATA_ID = process.env.TEAM_LINK_DATA_ID as string;

const params: v2.TeamsApiGetTeamLinkRequest = {
  teamId: DD_TEAM_DATA_ID,
  linkId: TEAM_LINK_DATA_ID,
};

apiInstance
  .getTeamLink(params)
  .then((data: v2.TeamLinkResponse) => {
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

## Update a team link{% #update-a-team-link %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/team/{team_id}/links/{link_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/team/{team_id}/links/{link_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/team/{team_id}/links/{link_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |

### Overview

Update a team link. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| link_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                          |
| ------------ | ---------------------------- | ------ | ---------------------------------------------------- |
|              | data [*required*]       | object | Team link create                                     |
| data         | attributes [*required*] | object | Team link attributes                                 |
| attributes   | label [*required*]      | string | The link's label                                     |
| attributes   | position                     | int32  | The link's position, used to sort links for the team |
| attributes   | team_id                      | string | ID of the team the link is associated with           |
| attributes   | url [*required*]        | string | The URL for the link                                 |
| data         | type [*required*]       | enum   | Team link type Allowed enum values: `team_links`     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "label": "New Label",
      "url": "https://example.com"
    },
    "type": "team_links"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team link response

| Parent field | Field                        | Type   | Description                                          |
| ------------ | ---------------------------- | ------ | ---------------------------------------------------- |
|              | data                         | object | Team link                                            |
| data         | attributes [*required*] | object | Team link attributes                                 |
| attributes   | label [*required*]      | string | The link's label                                     |
| attributes   | position                     | int32  | The link's position, used to sort links for the team |
| attributes   | team_id                      | string | ID of the team the link is associated with           |
| attributes   | url [*required*]        | string | The URL for the link                                 |
| data         | id [*required*]         | string | The team link's identifier                           |
| data         | type [*required*]       | enum   | Team link type Allowed enum values: `team_links`     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "label": "Link label",
      "position": "integer",
      "team_id": "string",
      "url": "https://example.com"
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "type": "team_links"
  }
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
API error response.
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
                          \# Path parametersexport team_id="CHANGE_ME"export link_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links/${link_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "label": "New Label",
      "url": "https://example.com"
    },
    "type": "team_links"
  }
}
EOF

#####

```go
// Update a team link returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "team_link" in the system
    TeamLinkDataID := os.Getenv("TEAM_LINK_DATA_ID")

    body := datadogV2.TeamLinkCreateRequest{
        Data: datadogV2.TeamLinkCreate{
            Attributes: datadogV2.TeamLinkAttributes{
                Label: "New Label",
                Url:   "https://example.com",
            },
            Type: datadogV2.TEAMLINKTYPE_TEAM_LINKS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.UpdateTeamLink(ctx, DdTeamDataID, TeamLinkDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.UpdateTeamLink`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.UpdateTeamLink`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update a team link returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamLinkAttributes;
import com.datadog.api.client.v2.model.TeamLinkCreate;
import com.datadog.api.client.v2.model.TeamLinkCreateRequest;
import com.datadog.api.client.v2.model.TeamLinkResponse;
import com.datadog.api.client.v2.model.TeamLinkType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "team_link" in the system
    String TEAM_LINK_DATA_ID = System.getenv("TEAM_LINK_DATA_ID");

    TeamLinkCreateRequest body =
        new TeamLinkCreateRequest()
            .data(
                new TeamLinkCreate()
                    .attributes(
                        new TeamLinkAttributes().label("New Label").url("https://example.com"))
                    .type(TeamLinkType.TEAM_LINKS));

    try {
      TeamLinkResponse result =
          apiInstance.updateTeamLink(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#updateTeamLink");
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
Update a team link returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_link_attributes import TeamLinkAttributes
from datadog_api_client.v2.model.team_link_create import TeamLinkCreate
from datadog_api_client.v2.model.team_link_create_request import TeamLinkCreateRequest
from datadog_api_client.v2.model.team_link_type import TeamLinkType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = environ["TEAM_LINK_DATA_ID"]

body = TeamLinkCreateRequest(
    data=TeamLinkCreate(
        attributes=TeamLinkAttributes(
            label="New Label",
            url="https://example.com",
        ),
        type=TeamLinkType.TEAM_LINKS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_link(team_id=DD_TEAM_DATA_ID, link_id=TEAM_LINK_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update a team link returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = ENV["TEAM_LINK_DATA_ID"]

body = DatadogAPIClient::V2::TeamLinkCreateRequest.new({
  data: DatadogAPIClient::V2::TeamLinkCreate.new({
    attributes: DatadogAPIClient::V2::TeamLinkAttributes.new({
      label: "New Label",
      url: "https://example.com",
    }),
    type: DatadogAPIClient::V2::TeamLinkType::TEAM_LINKS,
  }),
})
p api_instance.update_team_link(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update a team link returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamLinkAttributes;
use datadog_api_client::datadogV2::model::TeamLinkCreate;
use datadog_api_client::datadogV2::model::TeamLinkCreateRequest;
use datadog_api_client::datadogV2::model::TeamLinkType;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "team_link" in the system
    let team_link_data_id = std::env::var("TEAM_LINK_DATA_ID").unwrap();
    let body = TeamLinkCreateRequest::new(TeamLinkCreate::new(
        TeamLinkAttributes::new("New Label".to_string(), "https://example.com".to_string()),
        TeamLinkType::TEAM_LINKS,
    ));
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .update_team_link(dd_team_data_id.clone(), team_link_data_id.clone(), body)
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
 * Update a team link returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "team_link" in the system
const TEAM_LINK_DATA_ID = process.env.TEAM_LINK_DATA_ID as string;

const params: v2.TeamsApiUpdateTeamLinkRequest = {
  body: {
    data: {
      attributes: {
        label: "New Label",
        url: "https://example.com",
      },
      type: "team_links",
    },
  },
  teamId: DD_TEAM_DATA_ID,
  linkId: TEAM_LINK_DATA_ID,
};

apiInstance
  .updateTeamLink(params)
  .then((data: v2.TeamLinkResponse) => {
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

## Remove a team link{% #remove-a-team-link %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/team/{team_id}/links/{link_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/team/{team_id}/links/{link_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/team/{team_id}/links/{link_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/team/{team_id}/links/{link_id} |

### Overview

Remove a link from a team. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| link_id [*required*] | string | None        |

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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"export link_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links/${link_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove a team link returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = environ["TEAM_LINK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team_link(
        team_id=DD_TEAM_DATA_ID,
        link_id=TEAM_LINK_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Remove a team link returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = ENV["TEAM_LINK_DATA_ID"]
api_instance.delete_team_link(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Remove a team link returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "team_link" in the system
    TeamLinkDataID := os.Getenv("TEAM_LINK_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.DeleteTeamLink(ctx, DdTeamDataID, TeamLinkDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.DeleteTeamLink`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Remove a team link returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "team_link" in the system
    String TEAM_LINK_DATA_ID = System.getenv("TEAM_LINK_DATA_ID");

    try {
      apiInstance.deleteTeamLink(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#deleteTeamLink");
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
// Remove a team link returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "team_link" in the system
    let team_link_data_id = std::env::var("TEAM_LINK_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .delete_team_link(dd_team_data_id.clone(), team_link_data_id.clone())
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
 * Remove a team link returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "team_link" in the system
const TEAM_LINK_DATA_ID = process.env.TEAM_LINK_DATA_ID as string;

const params: v2.TeamsApiDeleteTeamLinkRequest = {
  teamId: DD_TEAM_DATA_ID,
  linkId: TEAM_LINK_DATA_ID,
};

apiInstance
  .deleteTeamLink(params)
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

## Get permission settings for a team{% #get-permission-settings-for-a-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/permission-settings |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{team_id}/permission-settings |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{team_id}/permission-settings      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{team_id}/permission-settings      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{team_id}/permission-settings     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{team_id}/permission-settings |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{team_id}/permission-settings |

### Overview

Get all permission settings for a given team. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team permission settings response

| Parent field | Field                  | Type     | Description                                                                                                                                     |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                   | [object] | Team permission settings response data                                                                                                          |
| data         | attributes             | object   | Team permission setting attributes                                                                                                              |
| attributes   | action                 | enum     | The identifier for the action Allowed enum values: `manage_membership,edit`                                                                     |
| attributes   | editable               | boolean  | Whether or not the permission setting is editable by the current user                                                                           |
| attributes   | options                | [string] | Possible values for action                                                                                                                      |
| attributes   | title                  | string   | The team permission name                                                                                                                        |
| attributes   | value                  | enum     | What type of user is allowed to perform the specified action Allowed enum values: `admins,members,organization,user_access_manage,teams_manage` |
| data         | id [*required*]   | string   | The team permission setting's identifier                                                                                                        |
| data         | type [*required*] | enum     | Team permission setting type Allowed enum values: `team_permission_settings`                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "action": "string",
        "editable": false,
        "options": [],
        "title": "string",
        "value": "string"
      },
      "id": "TeamPermission-aeadc05e-98a8-11ec-ac2c-da7ad0900001-edit",
      "type": "team_permission_settings"
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/permission-settings" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get permission settings for a team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_permission_settings(
        team_id=DD_TEAM_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get permission settings for a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team_permission_settings(DD_TEAM_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get permission settings for a team returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamPermissionSettings(ctx, DdTeamDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamPermissionSettings`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamPermissionSettings`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get permission settings for a team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamPermissionSettingsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    try {
      TeamPermissionSettingsResponse result =
          apiInstance.getTeamPermissionSettings(DD_TEAM_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamPermissionSettings");
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
// Get permission settings for a team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .get_team_permission_settings(dd_team_data_id.clone())
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
 * Get permission settings for a team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiGetTeamPermissionSettingsRequest = {
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .getTeamPermissionSettings(params)
  .then((data: v2.TeamPermissionSettingsResponse) => {
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

## Get team sync configurations{% #get-team-sync-configurations %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                       |
| ----------------- | -------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/sync |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/sync |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/sync      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/sync      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/sync     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/sync |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/sync |

### Overview

Get all team synchronization configurations. Returns a list of configurations used for linking or provisioning teams with external sources like GitHub. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Query Strings

| Name                             | Type | Description                                                                                  |
| -------------------------------- | ---- | -------------------------------------------------------------------------------------------- |
| filter[source] [*required*] | enum | Filter by the external source platform for team synchronizationAllowed enum values: `github` |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team sync configurations response.

| Parent field | Field                        | Type     | Description                                                                                                                                                                 |
| ------------ | ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | [object] | List of team sync configurations                                                                                                                                            |
| data         | attributes [*required*] | object   | Team sync attributes.                                                                                                                                                       |
| attributes   | frequency                    | enum     | How often the sync process should be run. Defaults to `once` when not provided. Allowed enum values: `once,continuously,paused`                                             |
| attributes   | source [*required*]     | enum     | The external source platform for team synchronization. Only "github" is supported. Allowed enum values: `github`                                                            |
| attributes   | sync_membership              | boolean  | Whether to sync members from the external team to the Datadog team. Defaults to `false` when not provided.                                                                  |
| attributes   | type [*required*]       | enum     | The type of synchronization operation. "link" connects teams by matching names. "provision" creates new teams when no match is found. Allowed enum values: `link,provision` |
| data         | id                           | string   | The sync's identifier                                                                                                                                                       |
| data         | type [*required*]       | enum     | Team sync bulk type. Allowed enum values: `team_sync_bulk`                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "frequency": "once",
        "source": "github",
        "sync_membership": true,
        "type": "link"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "team_sync_bulk"
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
Team sync configurations not found
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
                  \# Required query argumentsexport filter[source]="github"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/sync?filter[source]=${filter[source]}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get team sync configurations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_sync(
        filter_source=TeamSyncAttributesSource.GITHUB,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get team sync configurations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.get_team_sync(TeamSyncAttributesSource::GITHUB)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get team sync configurations returns "OK" response

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
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamSync(ctx, datadogV2.TEAMSYNCATTRIBUTESSOURCE_GITHUB)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamSync`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamSync`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get team sync configurations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamSyncAttributesSource;
import com.datadog.api.client.v2.model.TeamSyncResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    try {
      TeamSyncResponse result = apiInstance.getTeamSync(TeamSyncAttributesSource.GITHUB);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamSync");
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
// Get team sync configurations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamSyncAttributesSource;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.get_team_sync(TeamSyncAttributesSource::GITHUB).await;
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
 * Get team sync configurations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiGetTeamSyncRequest = {
  filterSource: "github",
};

apiInstance
  .getTeamSync(params)
  .then((data: v2.TeamSyncResponse) => {
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

## Update permission setting for team{% #update-permission-setting-for-team %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/team/{team_id}/permission-settings/{action}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/team/{team_id}/permission-settings/{action}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action} |

### Overview

Update a team permission setting for a given team. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| action [*required*]  | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                                                                                                     |
| ------------ | ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Team permission setting update                                                                                                                  |
| data         | attributes             | object | Team permission setting update attributes                                                                                                       |
| attributes   | value                  | enum   | What type of user is allowed to perform the specified action Allowed enum values: `admins,members,organization,user_access_manage,teams_manage` |
| data         | type [*required*] | enum   | Team permission setting type Allowed enum values: `team_permission_settings`                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "value": "admins"
    },
    "type": "team_permission_settings"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team permission setting response

| Parent field | Field                  | Type     | Description                                                                                                                                     |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                   | object   | Team permission setting                                                                                                                         |
| data         | attributes             | object   | Team permission setting attributes                                                                                                              |
| attributes   | action                 | enum     | The identifier for the action Allowed enum values: `manage_membership,edit`                                                                     |
| attributes   | editable               | boolean  | Whether or not the permission setting is editable by the current user                                                                           |
| attributes   | options                | [string] | Possible values for action                                                                                                                      |
| attributes   | title                  | string   | The team permission name                                                                                                                        |
| attributes   | value                  | enum     | What type of user is allowed to perform the specified action Allowed enum values: `admins,members,organization,user_access_manage,teams_manage` |
| data         | id [*required*]   | string   | The team permission setting's identifier                                                                                                        |
| data         | type [*required*] | enum     | Team permission setting type Allowed enum values: `team_permission_settings`                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "action": "string",
      "editable": false,
      "options": [],
      "title": "string",
      "value": "string"
    },
    "id": "TeamPermission-aeadc05e-98a8-11ec-ac2c-da7ad0900001-edit",
    "type": "team_permission_settings"
  }
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
API error response.
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
                          \# Path parametersexport team_id="CHANGE_ME"export action="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/permission-settings/${action}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "value": "admins"
    },
    "type": "team_permission_settings"
  }
}
EOF

#####

```go
// Update permission setting for team returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    body := datadogV2.TeamPermissionSettingUpdateRequest{
        Data: datadogV2.TeamPermissionSettingUpdate{
            Attributes: &datadogV2.TeamPermissionSettingUpdateAttributes{
                Value: datadogV2.TEAMPERMISSIONSETTINGVALUE_ADMINS.Ptr(),
            },
            Type: datadogV2.TEAMPERMISSIONSETTINGTYPE_TEAM_PERMISSION_SETTINGS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.UpdateTeamPermissionSetting(ctx, DdTeamDataID, "manage_membership", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.UpdateTeamPermissionSetting`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.UpdateTeamPermissionSetting`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update permission setting for team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamPermissionSettingResponse;
import com.datadog.api.client.v2.model.TeamPermissionSettingType;
import com.datadog.api.client.v2.model.TeamPermissionSettingUpdate;
import com.datadog.api.client.v2.model.TeamPermissionSettingUpdateAttributes;
import com.datadog.api.client.v2.model.TeamPermissionSettingUpdateRequest;
import com.datadog.api.client.v2.model.TeamPermissionSettingValue;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    TeamPermissionSettingUpdateRequest body =
        new TeamPermissionSettingUpdateRequest()
            .data(
                new TeamPermissionSettingUpdate()
                    .attributes(
                        new TeamPermissionSettingUpdateAttributes()
                            .value(TeamPermissionSettingValue.ADMINS))
                    .type(TeamPermissionSettingType.TEAM_PERMISSION_SETTINGS));

    try {
      TeamPermissionSettingResponse result =
          apiInstance.updateTeamPermissionSetting(DD_TEAM_DATA_ID, "manage_membership", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#updateTeamPermissionSetting");
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
Update permission setting for team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_permission_setting_type import TeamPermissionSettingType
from datadog_api_client.v2.model.team_permission_setting_update import TeamPermissionSettingUpdate
from datadog_api_client.v2.model.team_permission_setting_update_attributes import TeamPermissionSettingUpdateAttributes
from datadog_api_client.v2.model.team_permission_setting_update_request import TeamPermissionSettingUpdateRequest
from datadog_api_client.v2.model.team_permission_setting_value import TeamPermissionSettingValue

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamPermissionSettingUpdateRequest(
    data=TeamPermissionSettingUpdate(
        attributes=TeamPermissionSettingUpdateAttributes(
            value=TeamPermissionSettingValue.ADMINS,
        ),
        type=TeamPermissionSettingType.TEAM_PERMISSION_SETTINGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_permission_setting(
        team_id=DD_TEAM_DATA_ID, action="manage_membership", body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update permission setting for team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::TeamPermissionSettingUpdateRequest.new({
  data: DatadogAPIClient::V2::TeamPermissionSettingUpdate.new({
    attributes: DatadogAPIClient::V2::TeamPermissionSettingUpdateAttributes.new({
      value: DatadogAPIClient::V2::TeamPermissionSettingValue::ADMINS,
    }),
    type: DatadogAPIClient::V2::TeamPermissionSettingType::TEAM_PERMISSION_SETTINGS,
  }),
})
p api_instance.update_team_permission_setting(DD_TEAM_DATA_ID, "manage_membership", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update permission setting for team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamPermissionSettingType;
use datadog_api_client::datadogV2::model::TeamPermissionSettingUpdate;
use datadog_api_client::datadogV2::model::TeamPermissionSettingUpdateAttributes;
use datadog_api_client::datadogV2::model::TeamPermissionSettingUpdateRequest;
use datadog_api_client::datadogV2::model::TeamPermissionSettingValue;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = TeamPermissionSettingUpdateRequest::new(
        TeamPermissionSettingUpdate::new(TeamPermissionSettingType::TEAM_PERMISSION_SETTINGS)
            .attributes(
                TeamPermissionSettingUpdateAttributes::new()
                    .value(TeamPermissionSettingValue::ADMINS),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .update_team_permission_setting(
            dd_team_data_id.clone(),
            "manage_membership".to_string(),
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
 * Update permission setting for team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiUpdateTeamPermissionSettingRequest = {
  body: {
    data: {
      attributes: {
        value: "admins",
      },
      type: "team_permission_settings",
    },
  },
  teamId: DD_TEAM_DATA_ID,
  action: "manage_membership",
};

apiInstance
  .updateTeamPermissionSetting(params)
  .then((data: v2.TeamPermissionSettingResponse) => {
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

## Get user memberships{% #get-user-memberships %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/users/{user_uuid}/memberships |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/users/{user_uuid}/memberships |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/users/{user_uuid}/memberships      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/users/{user_uuid}/memberships      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/users/{user_uuid}/memberships     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/users/{user_uuid}/memberships |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/users/{user_uuid}/memberships |

### Overview

Get a list of memberships for a user This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                        | Type   | Description |
| --------------------------- | ------ | ----------- |
| user_uuid [*required*] | string | None        |

### Response

{% tab title="200" %}
Represents a user's association to a team
{% tab title="Model" %}
Team memberships response

| Parent field          | Field                        | Type            | Description                                                                                                                                                                                                       |
| --------------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                         | [object]        | Team memberships response data                                                                                                                                                                                    |
| data                  | attributes                   | object          | Team membership attributes                                                                                                                                                                                        |
| attributes            | provisioned_by               | string          | The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping. |
| attributes            | provisioned_by_id            | string          | UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.                                                                                                |
| attributes            | role                         | enum            | The user's role within the team Allowed enum values: `admin`                                                                                                                                                      |
| data                  | id [*required*]         | string          | The ID of a user's relationship with a team                                                                                                                                                                       |
| data                  | relationships                | object          | Relationship between membership and a user                                                                                                                                                                        |
| relationships         | team                         | object          | Relationship between team membership and team                                                                                                                                                                     |
| team                  | data [*required*]       | object          | The team associated with the membership                                                                                                                                                                           |
| data                  | id [*required*]         | string          | The ID of the team associated with the membership                                                                                                                                                                 |
| data                  | type [*required*]       | enum            | User team team type Allowed enum values: `team`                                                                                                                                                                   |
| relationships         | user                         | object          | Relationship between team membership and user                                                                                                                                                                     |
| user                  | data [*required*]       | object          | A user's relationship with a team                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user associated with the team                                                                                                                                                                       |
| data                  | type [*required*]       | enum            | User team user type Allowed enum values: `users`                                                                                                                                                                  |
| data                  | type [*required*]       | enum            | Team membership type Allowed enum values: `team_memberships`                                                                                                                                                      |
|                       | included                     | [ <oneOf>] | Resources related to the team memberships                                                                                                                                                                         |
| included              | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                  |
| Option 1              | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                    |
| attributes            | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                        |
| attributes            | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                     |
| attributes            | email                        | string          | Email of the user.                                                                                                                                                                                                |
| attributes            | handle                       | string          | Handle of the user.                                                                                                                                                                                               |
| attributes            | icon                         | string          | URL of the user's icon.                                                                                                                                                                                           |
| attributes            | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                 |
| attributes            | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                          |
| attributes            | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                             |
| attributes            | name                         | string          | Name of the user.                                                                                                                                                                                                 |
| attributes            | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                            |
| attributes            | status                       | string          | Status of the user.                                                                                                                                                                                               |
| attributes            | title                        | string          | Title of the user.                                                                                                                                                                                                |
| attributes            | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                     |
| Option 1              | id                           | string          | ID of the user.                                                                                                                                                                                                   |
| Option 1              | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                             |
| relationships         | org                          | object          | Relationship to an organization.                                                                                                                                                                                  |
| org                   | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                              |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                    |
| other_orgs            | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                            |
| data                  | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                           |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                          |
| relationships         | other_users                  | object          | Relationship to users.                                                                                                                                                                                            |
| other_users           | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                    |
| data                  | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                     |
| data                  | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| relationships         | roles                        | object          | Relationship to roles.                                                                                                                                                                                            |
| roles                 | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                     |
| data                  | id                           | string          | The unique identifier of the role.                                                                                                                                                                                |
| data                  | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                          |
| Option 1              | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                 |
| included              | Option 2                     | object          | A team                                                                                                                                                                                                            |
| Option 2              | attributes [*required*] | object          | Team attributes                                                                                                                                                                                                   |
| attributes            | avatar                       | string          | Unicode representation of the avatar for the team, limited to a single grapheme                                                                                                                                   |
| attributes            | banner                       | int64           | Banner selection for the team                                                                                                                                                                                     |
| attributes            | created_at                   | date-time       | Creation date of the team                                                                                                                                                                                         |
| attributes            | description                  | string          | Free-form markdown description/content for the team's homepage                                                                                                                                                    |
| attributes            | handle [*required*]     | string          | The team's identifier                                                                                                                                                                                             |
| attributes            | hidden_modules               | [string]        | Collection of hidden modules for the team                                                                                                                                                                         |
| attributes            | is_managed                   | boolean         | Whether the team is managed from an external source                                                                                                                                                               |
| attributes            | link_count                   | int32           | The number of links belonging to the team                                                                                                                                                                         |
| attributes            | modified_at                  | date-time       | Modification date of the team                                                                                                                                                                                     |
| attributes            | name [*required*]       | string          | The name of the team                                                                                                                                                                                              |
| attributes            | summary                      | string          | A brief summary of the team, derived from the `description`                                                                                                                                                       |
| attributes            | user_count                   | int32           | The number of users belonging to the team                                                                                                                                                                         |
| attributes            | visible_modules              | [string]        | Collection of visible modules for the team                                                                                                                                                                        |
| Option 2              | id [*required*]         | string          | The team's identifier                                                                                                                                                                                             |
| Option 2              | relationships                | object          | Resources related to a team                                                                                                                                                                                       |
| relationships         | team_links                   | object          | Relationship between a team and a team link                                                                                                                                                                       |
| team_links            | data                         | [object]        | Related team links                                                                                                                                                                                                |
| data                  | id [*required*]         | string          | The team link's identifier                                                                                                                                                                                        |
| data                  | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                                                                                                                                  |
| team_links            | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| relationships         | user_team_permissions        | object          | Relationship between a user team permission and a team                                                                                                                                                            |
| user_team_permissions | data                         | object          | Related user team permission data                                                                                                                                                                                 |
| data                  | id [*required*]         | string          | The ID of the user team permission                                                                                                                                                                                |
| data                  | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                                                                                                                                            |
| user_team_permissions | links                        | object          | Links attributes.                                                                                                                                                                                                 |
| links                 | related                      | string          | Related link.                                                                                                                                                                                                     |
| Option 2              | type [*required*]       | enum            | Team type Allowed enum values: `team`                                                                                                                                                                             |
|                       | links                        | object          | Teams response links.                                                                                                                                                                                             |
| links                 | first                        | string          | First link.                                                                                                                                                                                                       |
| links                 | last                         | string          | Last link.                                                                                                                                                                                                        |
| links                 | next                         | string          | Next link.                                                                                                                                                                                                        |
| links                 | prev                         | string          | Previous link.                                                                                                                                                                                                    |
| links                 | self                         | string          | Current link.                                                                                                                                                                                                     |
|                       | meta                         | object          | Teams response metadata.                                                                                                                                                                                          |
| meta                  | pagination                   | object          | Teams response metadata.                                                                                                                                                                                          |
| pagination            | first_offset                 | int64           | The first offset.                                                                                                                                                                                                 |
| pagination            | last_offset                  | int64           | The last offset.                                                                                                                                                                                                  |
| pagination            | limit                        | int64           | Pagination limit.                                                                                                                                                                                                 |
| pagination            | next_offset                  | int64           | The next offset.                                                                                                                                                                                                  |
| pagination            | offset                       | int64           | The offset.                                                                                                                                                                                                       |
| pagination            | prev_offset                  | int64           | The previous offset.                                                                                                                                                                                              |
| pagination            | total                        | int64           | Total results.                                                                                                                                                                                                    |
| pagination            | type                         | string          | Offset type.                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "provisioned_by": "string",
        "provisioned_by_id": "string",
        "role": "string"
      },
      "id": "TeamMembership-aeadc05e-98a8-11ec-ac2c-da7ad0900001-38835",
      "relationships": {
        "team": {
          "data": {
            "id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
            "type": "team"
          }
        },
        "user": {
          "data": {
            "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
            "type": "users"
          }
        }
      },
      "type": "team_memberships"
    }
  ],
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "pagination": {
      "first_offset": "integer",
      "last_offset": "integer",
      "limit": "integer",
      "next_offset": "integer",
      "offset": "integer",
      "prev_offset": "integer",
      "total": "integer",
      "type": "string"
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
API error response.
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
                  \# Path parametersexport user_uuid="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_uuid}/memberships" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get user memberships returns "Represents a user's association to a team" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_user_memberships(
        user_uuid=USER_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get user memberships returns "Represents a user's association to a team" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.get_user_memberships(USER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get user memberships returns "Represents a user's association to a team" response

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

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetUserMemberships(ctx, UserDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetUserMemberships`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetUserMemberships`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get user memberships returns "Represents a user's association to a team" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.UserTeamsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    try {
      UserTeamsResponse result = apiInstance.getUserMemberships(USER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getUserMemberships");
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
// Get user memberships returns "Represents a user's association to a team"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.get_user_memberships(user_data_id.clone()).await;
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
 * Get user memberships returns "Represents a user's association to a team" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.TeamsApiGetUserMembershipsRequest = {
  userUuid: USER_DATA_ID,
};

apiInstance
  .getUserMemberships(params)
  .then((data: v2.UserTeamsResponse) => {
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

## Link Teams with GitHub Teams{% #link-teams-with-github-teams %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team/sync |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team/sync |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team/sync      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team/sync      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team/sync     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team/sync |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team/sync |

### Overview

This endpoint attempts to link your existing Datadog teams with GitHub teams by matching their names. It evaluates all current Datadog teams and compares them against teams in the GitHub organization connected to your Datadog account, based on Datadog Team handle and GitHub Team slug (lowercased and kebab-cased).

This operation is read-only on the GitHub side, no teams will be modified or created.

[A GitHub organization must be connected to your Datadog account](https://docs.datadoghq.com/integrations/github/), and the GitHub App integrated with Datadog must have the `Members Read` permission. Matching is performed by comparing the Datadog team handle to the GitHub team slug using a normalized exact match; case is ignored and spaces are removed. No modifications are made to teams in GitHub. This only creates new teams in Datadog when type is set to `provision`.
This endpoint requires the `teams_manage` permission.
OAuth apps require the `teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                                                                                                                 |
| ------------ | ---------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object  | A configuration governing syncing between Datadog teams and teams from an external system.                                                                                  |
| data         | attributes [*required*] | object  | Team sync attributes.                                                                                                                                                       |
| attributes   | frequency                    | enum    | How often the sync process should be run. Defaults to `once` when not provided. Allowed enum values: `once,continuously,paused`                                             |
| attributes   | source [*required*]     | enum    | The external source platform for team synchronization. Only "github" is supported. Allowed enum values: `github`                                                            |
| attributes   | sync_membership              | boolean | Whether to sync members from the external team to the Datadog team. Defaults to `false` when not provided.                                                                  |
| attributes   | type [*required*]       | enum    | The type of synchronization operation. "link" connects teams by matching names. "provision" creates new teams when no match is found. Allowed enum values: `link,provision` |
| data         | id                           | string  | The sync's identifier                                                                                                                                                       |
| data         | type [*required*]       | enum    | Team sync bulk type. Allowed enum values: `team_sync_bulk`                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "source": "github",
      "type": "link"
    },
    "type": "team_sync_bulk"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
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

{% tab title="500" %}
Internal Server Error - Unexpected error during linking.
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/sync" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "source": "github",
      "type": "link"
    },
    "type": "team_sync_bulk"
  }
}
EOF

#####

```go
// Sync teams returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.TeamSyncRequest{
        Data: datadogV2.TeamSyncData{
            Attributes: datadogV2.TeamSyncAttributes{
                Source: datadogV2.TEAMSYNCATTRIBUTESSOURCE_GITHUB,
                Type:   datadogV2.TEAMSYNCATTRIBUTESTYPE_LINK,
            },
            Type: datadogV2.TEAMSYNCBULKTYPE_TEAM_SYNC_BULK,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.SyncTeams(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.SyncTeams`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Sync teams returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamSyncAttributes;
import com.datadog.api.client.v2.model.TeamSyncAttributesSource;
import com.datadog.api.client.v2.model.TeamSyncAttributesType;
import com.datadog.api.client.v2.model.TeamSyncBulkType;
import com.datadog.api.client.v2.model.TeamSyncData;
import com.datadog.api.client.v2.model.TeamSyncRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    TeamSyncRequest body =
        new TeamSyncRequest()
            .data(
                new TeamSyncData()
                    .attributes(
                        new TeamSyncAttributes()
                            .source(TeamSyncAttributesSource.GITHUB)
                            .type(TeamSyncAttributesType.LINK))
                    .type(TeamSyncBulkType.TEAM_SYNC_BULK));

    try {
      apiInstance.syncTeams(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#syncTeams");
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
Sync teams returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_sync_attributes import TeamSyncAttributes
from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource
from datadog_api_client.v2.model.team_sync_attributes_type import TeamSyncAttributesType
from datadog_api_client.v2.model.team_sync_bulk_type import TeamSyncBulkType
from datadog_api_client.v2.model.team_sync_data import TeamSyncData
from datadog_api_client.v2.model.team_sync_request import TeamSyncRequest

body = TeamSyncRequest(
    data=TeamSyncData(
        attributes=TeamSyncAttributes(
            source=TeamSyncAttributesSource.GITHUB,
            type=TeamSyncAttributesType.LINK,
        ),
        type=TeamSyncBulkType.TEAM_SYNC_BULK,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.sync_teams(body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::TeamSyncRequest.new({
  data: DatadogAPIClient::V2::TeamSyncData.new({
    attributes: DatadogAPIClient::V2::TeamSyncAttributes.new({
      source: DatadogAPIClient::V2::TeamSyncAttributesSource::GITHUB,
      type: DatadogAPIClient::V2::TeamSyncAttributesType::LINK,
    }),
    type: DatadogAPIClient::V2::TeamSyncBulkType::TEAM_SYNC_BULK,
  }),
})
p api_instance.sync_teams(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Sync teams returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamSyncAttributes;
use datadog_api_client::datadogV2::model::TeamSyncAttributesSource;
use datadog_api_client::datadogV2::model::TeamSyncAttributesType;
use datadog_api_client::datadogV2::model::TeamSyncBulkType;
use datadog_api_client::datadogV2::model::TeamSyncData;
use datadog_api_client::datadogV2::model::TeamSyncRequest;

#[tokio::main]
async fn main() {
    let body = TeamSyncRequest::new(TeamSyncData::new(
        TeamSyncAttributes::new(
            TeamSyncAttributesSource::GITHUB,
            TeamSyncAttributesType::LINK,
        ),
        TeamSyncBulkType::TEAM_SYNC_BULK,
    ));
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.sync_teams(body).await;
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
 * Sync teams returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiSyncTeamsRequest = {
  body: {
    data: {
      attributes: {
        source: "github",
        type: "link",
      },
      type: "team_sync_bulk",
    },
  },
};

apiInstance
  .syncTeams(params)
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

## Add a member team{% #add-a-member-team %}
**Note**: This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team/{super_team_id}/member_teams |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team/{super_team_id}/member_teams |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team/{super_team_id}/member_teams      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team/{super_team_id}/member_teams      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team/{super_team_id}/member_teams     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team/{super_team_id}/member_teams |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team/{super_team_id}/member_teams |

### Overview

Add a member team. Adds the team given by the `id` in the body as a member team of the super team.

**Note**: This API is deprecated. For creating team hierarchy links, use the team hierarchy links API: `POST /api/v2/team-hierarchy-links`.
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                            | Type   | Description |
| ------------------------------- | ------ | ----------- |
| super_team_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                          |
| ------------ | ---------------------- | ------ | ---------------------------------------------------- |
|              | data [*required*] | object | A member team                                        |
| data         | id [*required*]   | string | The member team's identifier                         |
| data         | type [*required*] | enum   | Member team type Allowed enum values: `member_teams` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "member_teams"
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
Added
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

{% tab title="409" %}
API error response.
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
                  \# Path parametersexport super_team_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${super_team_id}/member_teams" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "member_teams"
  }
}
EOF

#####

```python
"""
Add a member team returns "Added" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.add_member_team_request import AddMemberTeamRequest
from datadog_api_client.v2.model.member_team import MemberTeam
from datadog_api_client.v2.model.member_team_type import MemberTeamType

body = AddMemberTeamRequest(
    data=MemberTeam(
        id="aeadc05e-98a8-11ec-ac2c-da7ad0900001",
        type=MemberTeamType.MEMBER_TEAMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["add_member_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.add_member_team(super_team_id="super_team_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Add a member team returns "Added" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.add_member_team".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::AddMemberTeamRequest.new({
  data: DatadogAPIClient::V2::MemberTeam.new({
    id: "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    type: DatadogAPIClient::V2::MemberTeamType::MEMBER_TEAMS,
  }),
})
api_instance.add_member_team("super_team_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Add a member team returns "Added" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.AddMemberTeamRequest{
        Data: datadogV2.MemberTeam{
            Id:   "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            Type: datadogV2.MEMBERTEAMTYPE_MEMBER_TEAMS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.AddMemberTeam", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.AddMemberTeam(ctx, "super_team_id", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.AddMemberTeam`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Add a member team returns "Added" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.AddMemberTeamRequest;
import com.datadog.api.client.v2.model.MemberTeam;
import com.datadog.api.client.v2.model.MemberTeamType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.addMemberTeam", true);
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    AddMemberTeamRequest body =
        new AddMemberTeamRequest()
            .data(
                new MemberTeam()
                    .id("aeadc05e-98a8-11ec-ac2c-da7ad0900001")
                    .type(MemberTeamType.MEMBER_TEAMS));

    try {
      apiInstance.addMemberTeam("super_team_id", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#addMemberTeam");
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
// Add a member team returns "Added" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::AddMemberTeamRequest;
use datadog_api_client::datadogV2::model::MemberTeam;
use datadog_api_client::datadogV2::model::MemberTeamType;

#[tokio::main]
async fn main() {
    let body = AddMemberTeamRequest::new(MemberTeam::new(
        "aeadc05e-98a8-11ec-ac2c-da7ad0900001".to_string(),
        MemberTeamType::MEMBER_TEAMS,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.AddMemberTeam", true);
    let api = TeamsAPI::with_config(configuration);
    let resp = api.add_member_team("super_team_id".to_string(), body).await;
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
 * Add a member team returns "Added" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.addMemberTeam"] = true;
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiAddMemberTeamRequest = {
  body: {
    data: {
      id: "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      type: "member_teams",
    },
  },
  superTeamId: "super_team_id",
};

apiInstance
  .addMemberTeam(params)
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
## Get team hierarchy links{% #get-team-hierarchy-links %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team-hierarchy-links |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team-hierarchy-links |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team-hierarchy-links      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team-hierarchy-links      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team-hierarchy-links     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team-hierarchy-links |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team-hierarchy-links |

### Overview

List all team hierarchy links that match the provided filters. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Query Strings

| Name                | Type    | Description                                              |
| ------------------- | ------- | -------------------------------------------------------- |
| page[number]        | integer | Specific page number to return.                          |
| page[size]          | integer | Size for a given page. The maximum allowed value is 100. |
| filter[parent_team] | string  | Filter by parent team ID                                 |
| filter[sub_team]    | string  | Filter by sub team ID                                    |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team hierarchy links response

| Parent field  | Field                            | Type      | Description                                                                                                                        |
| ------------- | -------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|               | data                             | [object]  | Team hierarchy links response data                                                                                                 |
| data          | attributes [*required*]     | object    | Team hierarchy link attributes                                                                                                     |
| attributes    | created_at [*required*]     | date-time | Timestamp when the team hierarchy link was created                                                                                 |
| attributes    | provisioned_by [*required*] | string    | The provisioner of the team hierarchy link                                                                                         |
| data          | id [*required*]             | string    | The team hierarchy link's identifier                                                                                               |
| data          | relationships                    | object    | Team hierarchy link relationships                                                                                                  |
| relationships | parent_team [*required*]    | object    | Team hierarchy link team relationship                                                                                              |
| parent_team   | data [*required*]           | object    | Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.          |
| data          | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| data          | id [*required*]             | string    | The team's identifier                                                                                                              |
| data          | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
| relationships | sub_team [*required*]       | object    | Team hierarchy link team relationship                                                                                              |
| sub_team      | data [*required*]           | object    | Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.          |
| data          | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| data          | id [*required*]             | string    | The team's identifier                                                                                                              |
| data          | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
| data          | type [*required*]           | enum      | Team hierarchy link type Allowed enum values: `team_hierarchy_links`                                                               |
|               | included                         | [object]  | Included teams                                                                                                                     |
| included      | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| included      | id [*required*]             | string    | The team's identifier                                                                                                              |
| included      | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
|               | links                            | object    | When querying team hierarchy links, a set of links for navigation between different pages is included                              |
| links         | first                            | string    | Link to the first page.                                                                                                            |
| links         | last                             | string    | Link to the last page.                                                                                                             |
| links         | next                             | string    | Link to the next page.                                                                                                             |
| links         | prev                             | string    | Link to the previous page.                                                                                                         |
| links         | self                             | string    | Link to the current object.                                                                                                        |
|               | meta                             | object    | Metadata that is included in the response when querying the team hierarchy links                                                   |
| meta          | page                             | object    | Metadata related to paging information that is included in the response when querying the team hierarchy links                     |
| page          | first_number                     | int64     | First page number.                                                                                                                 |
| page          | last_number                      | int64     | Last page number.                                                                                                                  |
| page          | next_number                      | int64     | Next page number.                                                                                                                  |
| page          | number                           | int64     | Page number.                                                                                                                       |
| page          | prev_number                      | int64     | Previous page number.                                                                                                              |
| page          | size                             | int64     | Page size.                                                                                                                         |
| page          | total                            | int64     | Total number of results.                                                                                                           |
| page          | type                             | string    | Pagination type.                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "",
        "provisioned_by": "system"
      },
      "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
      "relationships": {
        "parent_team": {
          "data": {
            "attributes": {
              "avatar": "string",
              "banner": "integer",
              "handle": "team-handle",
              "is_managed": false,
              "is_open_membership": false,
              "link_count": "integer",
              "name": "Team Name",
              "summary": "string",
              "user_count": "integer"
            },
            "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
            "type": "team"
          }
        },
        "sub_team": {
          "data": {
            "attributes": {
              "avatar": "string",
              "banner": "integer",
              "handle": "team-handle",
              "is_managed": false,
              "is_open_membership": false,
              "link_count": "integer",
              "name": "Team Name",
              "summary": "string",
              "user_count": "integer"
            },
            "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
            "type": "team"
          }
        }
      },
      "type": "team_hierarchy_links"
    }
  ],
  "included": [
    {
      "attributes": {
        "avatar": "string",
        "banner": "integer",
        "handle": "team-handle",
        "is_managed": false,
        "is_open_membership": false,
        "link_count": "integer",
        "name": "Team Name",
        "summary": "string",
        "user_count": "integer"
      },
      "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
      "type": "team"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "page": {
      "first_number": "integer",
      "last_number": "integer",
      "next_number": "integer",
      "number": "integer",
      "prev_number": "integer",
      "size": "integer",
      "total": "integer",
      "type": "number_size"
    }
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get team hierarchy links returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID = environ[
    "TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID"
]
TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID = environ[
    "TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID"
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_team_hierarchy_links(
        page_number=0,
        page_size=100,
        filter_parent_team=TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID,
        filter_sub_team=TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get team hierarchy links returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID = ENV["TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID"]
TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID = ENV["TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID"]
opts = {
  filter_parent_team: TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID,
  filter_sub_team: TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID,
  page_number: 0,
  page_size: 100,
}
p api_instance.list_team_hierarchy_links(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get team hierarchy links returns "OK" response

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
    // there is a valid "team_hierarchy_link" in the system
    TeamHierarchyLinkDataRelationshipsParentTeamDataID := os.Getenv("TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID")
    TeamHierarchyLinkDataRelationshipsSubTeamDataID := os.Getenv("TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.ListTeamHierarchyLinks(ctx, *datadogV2.NewListTeamHierarchyLinksOptionalParameters().WithFilterParentTeam(TeamHierarchyLinkDataRelationshipsParentTeamDataID).WithFilterSubTeam(TeamHierarchyLinkDataRelationshipsSubTeamDataID).WithPageNumber(0).WithPageSize(100))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.ListTeamHierarchyLinks`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.ListTeamHierarchyLinks`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get team hierarchy links returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.api.TeamsApi.ListTeamHierarchyLinksOptionalParameters;
import com.datadog.api.client.v2.model.TeamHierarchyLinksResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "team_hierarchy_link" in the system
    String TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID =
        System.getenv("TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID");
    String TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID =
        System.getenv("TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID");

    try {
      TeamHierarchyLinksResponse result =
          apiInstance.listTeamHierarchyLinks(
              new ListTeamHierarchyLinksOptionalParameters()
                  .filterParentTeam(TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID)
                  .filterSubTeam(TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID)
                  .pageNumber(0L)
                  .pageSize(100L));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#listTeamHierarchyLinks");
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
// Get team hierarchy links returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::ListTeamHierarchyLinksOptionalParams;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "team_hierarchy_link" in the system
    let team_hierarchy_link_data_relationships_parent_team_data_id =
        std::env::var("TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID").unwrap();
    let team_hierarchy_link_data_relationships_sub_team_data_id =
        std::env::var("TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .list_team_hierarchy_links(
            ListTeamHierarchyLinksOptionalParams::default()
                .filter_parent_team(
                    team_hierarchy_link_data_relationships_parent_team_data_id.clone(),
                )
                .filter_sub_team(team_hierarchy_link_data_relationships_sub_team_data_id.clone())
                .page_number(0)
                .page_size(100),
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
 * Get team hierarchy links returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "team_hierarchy_link" in the system
const TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID = process.env
  .TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID as string;
const TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID = process.env
  .TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID as string;

const params: v2.TeamsApiListTeamHierarchyLinksRequest = {
  pageNumber: 0,
  pageSize: 100,
  filterParentTeam: TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_PARENT_TEAM_DATA_ID,
  filterSubTeam: TEAM_HIERARCHY_LINK_DATA_RELATIONSHIPS_SUB_TEAM_DATA_ID,
};

apiInstance
  .listTeamHierarchyLinks(params)
  .then((data: v2.TeamHierarchyLinksResponse) => {
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

## Get a team hierarchy link{% #get-a-team-hierarchy-link %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team-hierarchy-links/{link_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team-hierarchy-links/{link_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team-hierarchy-links/{link_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |

### Overview

Get a single team hierarchy link for the given link_id. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                          |
| ------------------------- | ------ | ------------------------------------ |
| link_id [*required*] | string | The team hierarchy link's identifier |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team hierarchy link response

| Parent field  | Field                            | Type      | Description                                                                                                                        |
| ------------- | -------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|               | data                             | object    | Team hierarchy link                                                                                                                |
| data          | attributes [*required*]     | object    | Team hierarchy link attributes                                                                                                     |
| attributes    | created_at [*required*]     | date-time | Timestamp when the team hierarchy link was created                                                                                 |
| attributes    | provisioned_by [*required*] | string    | The provisioner of the team hierarchy link                                                                                         |
| data          | id [*required*]             | string    | The team hierarchy link's identifier                                                                                               |
| data          | relationships                    | object    | Team hierarchy link relationships                                                                                                  |
| relationships | parent_team [*required*]    | object    | Team hierarchy link team relationship                                                                                              |
| parent_team   | data [*required*]           | object    | Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.          |
| data          | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| data          | id [*required*]             | string    | The team's identifier                                                                                                              |
| data          | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
| relationships | sub_team [*required*]       | object    | Team hierarchy link team relationship                                                                                              |
| sub_team      | data [*required*]           | object    | Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.          |
| data          | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| data          | id [*required*]             | string    | The team's identifier                                                                                                              |
| data          | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
| data          | type [*required*]           | enum      | Team hierarchy link type Allowed enum values: `team_hierarchy_links`                                                               |
|               | included                         | [object]  | Included teams                                                                                                                     |
| included      | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| included      | id [*required*]             | string    | The team's identifier                                                                                                              |
| included      | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
|               | links                            | object    | When querying team hierarchy links, a set of links for navigation between different pages is included                              |
| links         | first                            | string    | Link to the first page.                                                                                                            |
| links         | last                             | string    | Link to the last page.                                                                                                             |
| links         | next                             | string    | Link to the next page.                                                                                                             |
| links         | prev                             | string    | Link to the previous page.                                                                                                         |
| links         | self                             | string    | Link to the current object.                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "",
      "provisioned_by": "system"
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "relationships": {
      "parent_team": {
        "data": {
          "attributes": {
            "avatar": "string",
            "banner": "integer",
            "handle": "team-handle",
            "is_managed": false,
            "is_open_membership": false,
            "link_count": "integer",
            "name": "Team Name",
            "summary": "string",
            "user_count": "integer"
          },
          "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
          "type": "team"
        }
      },
      "sub_team": {
        "data": {
          "attributes": {
            "avatar": "string",
            "banner": "integer",
            "handle": "team-handle",
            "is_managed": false,
            "is_open_membership": false,
            "link_count": "integer",
            "name": "Team Name",
            "summary": "string",
            "user_count": "integer"
          },
          "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
          "type": "team"
        }
      }
    },
    "type": "team_hierarchy_links"
  },
  "included": [
    {
      "attributes": {
        "avatar": "string",
        "banner": "integer",
        "handle": "team-handle",
        "is_managed": false,
        "is_open_membership": false,
        "link_count": "integer",
        "name": "Team Name",
        "summary": "string",
        "user_count": "integer"
      },
      "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
      "type": "team"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  }
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
API error response.
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
                  \# Path parametersexport link_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/${link_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a team hierarchy link returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_ID = environ["TEAM_HIERARCHY_LINK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_hierarchy_link(
        link_id=TEAM_HIERARCHY_LINK_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a team hierarchy link returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_ID = ENV["TEAM_HIERARCHY_LINK_DATA_ID"]
p api_instance.get_team_hierarchy_link(TEAM_HIERARCHY_LINK_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a team hierarchy link returns "OK" response

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
    // there is a valid "team_hierarchy_link" in the system
    TeamHierarchyLinkDataID := os.Getenv("TEAM_HIERARCHY_LINK_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamHierarchyLink(ctx, TeamHierarchyLinkDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamHierarchyLink`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamHierarchyLink`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a team hierarchy link returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamHierarchyLinkResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "team_hierarchy_link" in the system
    String TEAM_HIERARCHY_LINK_DATA_ID = System.getenv("TEAM_HIERARCHY_LINK_DATA_ID");

    try {
      TeamHierarchyLinkResponse result =
          apiInstance.getTeamHierarchyLink(TEAM_HIERARCHY_LINK_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamHierarchyLink");
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
// Get a team hierarchy link returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "team_hierarchy_link" in the system
    let team_hierarchy_link_data_id = std::env::var("TEAM_HIERARCHY_LINK_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .get_team_hierarchy_link(team_hierarchy_link_data_id.clone())
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
 * Get a team hierarchy link returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "team_hierarchy_link" in the system
const TEAM_HIERARCHY_LINK_DATA_ID = process.env
  .TEAM_HIERARCHY_LINK_DATA_ID as string;

const params: v2.TeamsApiGetTeamHierarchyLinkRequest = {
  linkId: TEAM_HIERARCHY_LINK_DATA_ID,
};

apiInstance
  .getTeamHierarchyLink(params)
  .then((data: v2.TeamHierarchyLinkResponse) => {
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

## Get all member teams{% #get-all-member-teams %}
**Note**: This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{super_team_id}/member_teams |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{super_team_id}/member_teams |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{super_team_id}/member_teams      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{super_team_id}/member_teams      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{super_team_id}/member_teams     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{super_team_id}/member_teams |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{super_team_id}/member_teams |

### Overview

Get all member teams.

**Note**: This API is deprecated. For team hierarchy relationships (parent-child teams), use the team hierarchy links API: `GET /api/v2/team-hierarchy-links`.
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                            | Type   | Description |
| ------------------------------- | ------ | ----------- |
| super_team_id [*required*] | string | None        |

#### Query Strings

| Name         | Type    | Description                                              |
| ------------ | ------- | -------------------------------------------------------- |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100. |
| page[number] | integer | Specific page number to return.                          |
| fields[team] | array   | List of fields that need to be fetched.                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with multiple teams

| Parent field          | Field                        | Type            | Description                                                                                          |
| --------------------- | ---------------------------- | --------------- | ---------------------------------------------------------------------------------------------------- |
|                       | data                         | [object]        | Teams response data                                                                                  |
| data                  | attributes [*required*] | object          | Team attributes                                                                                      |
| attributes            | avatar                       | string          | Unicode representation of the avatar for the team, limited to a single grapheme                      |
| attributes            | banner                       | int64           | Banner selection for the team                                                                        |
| attributes            | created_at                   | date-time       | Creation date of the team                                                                            |
| attributes            | description                  | string          | Free-form markdown description/content for the team's homepage                                       |
| attributes            | handle [*required*]     | string          | The team's identifier                                                                                |
| attributes            | hidden_modules               | [string]        | Collection of hidden modules for the team                                                            |
| attributes            | is_managed                   | boolean         | Whether the team is managed from an external source                                                  |
| attributes            | link_count                   | int32           | The number of links belonging to the team                                                            |
| attributes            | modified_at                  | date-time       | Modification date of the team                                                                        |
| attributes            | name [*required*]       | string          | The name of the team                                                                                 |
| attributes            | summary                      | string          | A brief summary of the team, derived from the `description`                                          |
| attributes            | user_count                   | int32           | The number of users belonging to the team                                                            |
| attributes            | visible_modules              | [string]        | Collection of visible modules for the team                                                           |
| data                  | id [*required*]         | string          | The team's identifier                                                                                |
| data                  | relationships                | object          | Resources related to a team                                                                          |
| relationships         | team_links                   | object          | Relationship between a team and a team link                                                          |
| team_links            | data                         | [object]        | Related team links                                                                                   |
| data                  | id [*required*]         | string          | The team link's identifier                                                                           |
| data                  | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                     |
| team_links            | links                        | object          | Links attributes.                                                                                    |
| links                 | related                      | string          | Related link.                                                                                        |
| relationships         | user_team_permissions        | object          | Relationship between a user team permission and a team                                               |
| user_team_permissions | data                         | object          | Related user team permission data                                                                    |
| data                  | id [*required*]         | string          | The ID of the user team permission                                                                   |
| data                  | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                               |
| user_team_permissions | links                        | object          | Links attributes.                                                                                    |
| links                 | related                      | string          | Related link.                                                                                        |
| data                  | type [*required*]       | enum            | Team type Allowed enum values: `team`                                                                |
|                       | included                     | [ <oneOf>] | Resources related to the team                                                                        |
| included              | Option 1                     | object          | User object returned by the API.                                                                     |
| Option 1              | attributes                   | object          | Attributes of user object returned by the API.                                                       |
| attributes            | created_at                   | date-time       | Creation time of the user.                                                                           |
| attributes            | disabled                     | boolean         | Whether the user is disabled.                                                                        |
| attributes            | email                        | string          | Email of the user.                                                                                   |
| attributes            | handle                       | string          | Handle of the user.                                                                                  |
| attributes            | icon                         | string          | URL of the user's icon.                                                                              |
| attributes            | last_login_time              | date-time       | The last time the user logged in.                                                                    |
| attributes            | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                             |
| attributes            | modified_at                  | date-time       | Time that the user was last modified.                                                                |
| attributes            | name                         | string          | Name of the user.                                                                                    |
| attributes            | service_account              | boolean         | Whether the user is a service account.                                                               |
| attributes            | status                       | string          | Status of the user.                                                                                  |
| attributes            | title                        | string          | Title of the user.                                                                                   |
| attributes            | verified                     | boolean         | Whether the user is verified.                                                                        |
| Option 1              | id                           | string          | ID of the user.                                                                                      |
| Option 1              | relationships                | object          | Relationships of the user object returned by the API.                                                |
| relationships         | org                          | object          | Relationship to an organization.                                                                     |
| org                   | data [*required*]       | object          | Relationship to organization object.                                                                 |
| data                  | id [*required*]         | string          | ID of the organization.                                                                              |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                             |
| relationships         | other_orgs                   | object          | Relationship to organizations.                                                                       |
| other_orgs            | data [*required*]       | [object]        | Relationships to organization objects.                                                               |
| data                  | id [*required*]         | string          | ID of the organization.                                                                              |
| data                  | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                             |
| relationships         | other_users                  | object          | Relationship to users.                                                                               |
| other_users           | data [*required*]       | [object]        | Relationships to user objects.                                                                       |
| data                  | id [*required*]         | string          | A unique identifier that represents the user.                                                        |
| data                  | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                    |
| relationships         | roles                        | object          | Relationship to roles.                                                                               |
| roles                 | data                         | [object]        | An array containing type and the unique identifier of a role.                                        |
| data                  | id                           | string          | The unique identifier of the role.                                                                   |
| data                  | type                         | enum            | Roles type. Allowed enum values: `roles`                                                             |
| Option 1              | type                         | enum            | Users resource type. Allowed enum values: `users`                                                    |
| included              | Option 2                     | object          | Team link                                                                                            |
| Option 2              | attributes [*required*] | object          | Team link attributes                                                                                 |
| attributes            | label [*required*]      | string          | The link's label                                                                                     |
| attributes            | position                     | int32           | The link's position, used to sort links for the team                                                 |
| attributes            | team_id                      | string          | ID of the team the link is associated with                                                           |
| attributes            | url [*required*]        | string          | The URL for the link                                                                                 |
| Option 2              | id [*required*]         | string          | The team link's identifier                                                                           |
| Option 2              | type [*required*]       | enum            | Team link type Allowed enum values: `team_links`                                                     |
| included              | Option 3                     | object          | A user's permissions for a given team                                                                |
| Option 3              | attributes                   | object          | User team permission attributes                                                                      |
| attributes            | permissions                  | object          | Object of team permission actions and boolean values that a logged in user can perform on this team. |
| Option 3              | id [*required*]         | string          | The user team permission's identifier                                                                |
| Option 3              | type [*required*]       | enum            | User team permission type Allowed enum values: `user_team_permissions`                               |
|                       | links                        | object          | Teams response links.                                                                                |
| links                 | first                        | string          | First link.                                                                                          |
| links                 | last                         | string          | Last link.                                                                                           |
| links                 | next                         | string          | Next link.                                                                                           |
| links                 | prev                         | string          | Previous link.                                                                                       |
| links                 | self                         | string          | Current link.                                                                                        |
|                       | meta                         | object          | Teams response metadata.                                                                             |
| meta                  | pagination                   | object          | Teams response metadata.                                                                             |
| pagination            | first_offset                 | int64           | The first offset.                                                                                    |
| pagination            | last_offset                  | int64           | The last offset.                                                                                     |
| pagination            | limit                        | int64           | Pagination limit.                                                                                    |
| pagination            | next_offset                  | int64           | The next offset.                                                                                     |
| pagination            | offset                       | int64           | The offset.                                                                                          |
| pagination            | prev_offset                  | int64           | The previous offset.                                                                                 |
| pagination            | total                        | int64           | Total results.                                                                                       |
| pagination            | type                         | string          | Offset type.                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "avatar": "ð¥",
        "banner": "integer",
        "created_at": "2019-09-19T10:00:00.000Z",
        "description": "string",
        "handle": "example-team",
        "hidden_modules": [],
        "is_managed": false,
        "link_count": "integer",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "Example Team",
        "summary": "string",
        "user_count": "integer",
        "visible_modules": []
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "relationships": {
        "team_links": {
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
        "user_team_permissions": {
          "data": {
            "id": "UserTeamPermissions-aeadc05e-98a8-11ec-ac2c-da7ad0900001-416595",
            "type": "user_team_permissions"
          },
          "links": {
            "related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"
          }
        }
      },
      "type": "team"
    }
  ],
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "pagination": {
      "first_offset": "integer",
      "last_offset": "integer",
      "limit": "integer",
      "next_offset": "integer",
      "offset": "integer",
      "prev_offset": "integer",
      "total": "integer",
      "type": "string"
    }
  }
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
API error response.
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
                  \# Path parametersexport super_team_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${super_team_id}/member_teams" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all member teams returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.unstable_operations["list_member_teams"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_member_teams(
        super_team_id="super_team_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_member_teams".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.list_member_teams("super_team_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get all member teams returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.ListMemberTeams", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.ListMemberTeams(ctx, "super_team_id", *datadogV2.NewListMemberTeamsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.ListMemberTeams`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.ListMemberTeams`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get all member teams returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listMemberTeams", true);
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    try {
      TeamsResponse result = apiInstance.listMemberTeams("super_team_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#listMemberTeams");
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
// Get all member teams returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::ListMemberTeamsOptionalParams;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListMemberTeams", true);
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .list_member_teams(
            "super_team_id".to_string(),
            ListMemberTeamsOptionalParams::default(),
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
 * Get all member teams returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listMemberTeams"] = true;
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiListMemberTeamsRequest = {
  superTeamId: "super_team_id",
};

apiInstance
  .listMemberTeams(params)
  .then((data: v2.TeamsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Create a team hierarchy link{% #create-a-team-hierarchy-link %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team-hierarchy-links |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team-hierarchy-links |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team-hierarchy-links      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team-hierarchy-links      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team-hierarchy-links     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team-hierarchy-links |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team-hierarchy-links |

### Overview

Create a new team hierarchy link between a parent team and a sub team. This endpoint requires all of the following permissions:
`teams_read``teams_manage`

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field  | Field                           | Type   | Description                                                                                                    |
| ------------- | ------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------- |
|               | data [*required*]          | object | Data provided when creating a team hierarchy link                                                              |
| data          | relationships [*required*] | object | The related teams that will be connected by the team hierarchy link                                            |
| relationships | parent_team [*required*]   | object | Data about each team that will be connected by the team hierarchy link                                         |
| parent_team   | data [*required*]          | object | This schema defines the attributes about each team that has to be provided when creating a team hierarchy link |
| data          | id [*required*]            | string | The team's identifier                                                                                          |
| data          | type [*required*]          | enum   | Team type Allowed enum values: `team`                                                                          |
| relationships | sub_team [*required*]      | object | Data about each team that will be connected by the team hierarchy link                                         |
| sub_team      | data [*required*]          | object | This schema defines the attributes about each team that has to be provided when creating a team hierarchy link |
| data          | id [*required*]            | string | The team's identifier                                                                                          |
| data          | type [*required*]          | enum   | Team type Allowed enum values: `team`                                                                          |
| data          | type [*required*]          | enum   | Team hierarchy link type Allowed enum values: `team_hierarchy_links`                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "relationships": {
      "parent_team": {
        "data": {
          "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      },
      "sub_team": {
        "data": {
          "id": "7c47c39d-7740-6408-d686-7870a744701c",
          "type": "team"
        }
      }
    },
    "type": "team_hierarchy_links"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team hierarchy link response

| Parent field  | Field                            | Type      | Description                                                                                                                        |
| ------------- | -------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|               | data                             | object    | Team hierarchy link                                                                                                                |
| data          | attributes [*required*]     | object    | Team hierarchy link attributes                                                                                                     |
| attributes    | created_at [*required*]     | date-time | Timestamp when the team hierarchy link was created                                                                                 |
| attributes    | provisioned_by [*required*] | string    | The provisioner of the team hierarchy link                                                                                         |
| data          | id [*required*]             | string    | The team hierarchy link's identifier                                                                                               |
| data          | relationships                    | object    | Team hierarchy link relationships                                                                                                  |
| relationships | parent_team [*required*]    | object    | Team hierarchy link team relationship                                                                                              |
| parent_team   | data [*required*]           | object    | Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.          |
| data          | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| data          | id [*required*]             | string    | The team's identifier                                                                                                              |
| data          | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
| relationships | sub_team [*required*]       | object    | Team hierarchy link team relationship                                                                                              |
| sub_team      | data [*required*]           | object    | Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.          |
| data          | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| data          | id [*required*]             | string    | The team's identifier                                                                                                              |
| data          | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
| data          | type [*required*]           | enum      | Team hierarchy link type Allowed enum values: `team_hierarchy_links`                                                               |
|               | included                         | [object]  | Included teams                                                                                                                     |
| included      | attributes                       | object    | Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link. |
| attributes    | avatar                           | string    | The team's avatar                                                                                                                  |
| attributes    | banner                           | int64     | The team's banner                                                                                                                  |
| attributes    | handle [*required*]         | string    | The team's handle                                                                                                                  |
| attributes    | is_managed                       | boolean   | Whether the team is managed                                                                                                        |
| attributes    | is_open_membership               | boolean   | Whether the team has open membership                                                                                               |
| attributes    | link_count                       | int64     | The number of links for the team                                                                                                   |
| attributes    | name [*required*]           | string    | The team's name                                                                                                                    |
| attributes    | summary                          | string    | The team's summary                                                                                                                 |
| attributes    | user_count                       | int64     | The number of users in the team                                                                                                    |
| included      | id [*required*]             | string    | The team's identifier                                                                                                              |
| included      | type [*required*]           | enum      | Team type Allowed enum values: `team`                                                                                              |
|               | links                            | object    | When querying team hierarchy links, a set of links for navigation between different pages is included                              |
| links         | first                            | string    | Link to the first page.                                                                                                            |
| links         | last                             | string    | Link to the last page.                                                                                                             |
| links         | next                             | string    | Link to the next page.                                                                                                             |
| links         | prev                             | string    | Link to the previous page.                                                                                                         |
| links         | self                             | string    | Link to the current object.                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "",
      "provisioned_by": "system"
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "relationships": {
      "parent_team": {
        "data": {
          "attributes": {
            "avatar": "string",
            "banner": "integer",
            "handle": "team-handle",
            "is_managed": false,
            "is_open_membership": false,
            "link_count": "integer",
            "name": "Team Name",
            "summary": "string",
            "user_count": "integer"
          },
          "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
          "type": "team"
        }
      },
      "sub_team": {
        "data": {
          "attributes": {
            "avatar": "string",
            "banner": "integer",
            "handle": "team-handle",
            "is_managed": false,
            "is_open_membership": false,
            "link_count": "integer",
            "name": "Team Name",
            "summary": "string",
            "user_count": "integer"
          },
          "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
          "type": "team"
        }
      }
    },
    "type": "team_hierarchy_links"
  },
  "included": [
    {
      "attributes": {
        "avatar": "string",
        "banner": "integer",
        "handle": "team-handle",
        "is_managed": false,
        "is_open_membership": false,
        "link_count": "integer",
        "name": "Team Name",
        "summary": "string",
        "user_count": "integer"
      },
      "id": "692e8073-12c4-4c71-8408-5090bd44c9c8",
      "type": "team"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  }
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "relationships": {
      "parent_team": {
        "data": {
          "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      },
      "sub_team": {
        "data": {
          "id": "7c47c39d-7740-6408-d686-7870a744701c",
          "type": "team"
        }
      }
    },
    "type": "team_hierarchy_links"
  }
}
EOF

#####

```go
// Create a team hierarchy link returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "dd_team_2" in the system
    DdTeam2DataID := os.Getenv("DD_TEAM_2_DATA_ID")

    body := datadogV2.TeamHierarchyLinkCreateRequest{
        Data: datadogV2.TeamHierarchyLinkCreate{
            Relationships: datadogV2.TeamHierarchyLinkCreateRelationships{
                ParentTeam: datadogV2.TeamHierarchyLinkCreateTeamRelationship{
                    Data: datadogV2.TeamHierarchyLinkCreateTeam{
                        Id:   DdTeamDataID,
                        Type: datadogV2.TEAMTYPE_TEAM,
                    },
                },
                SubTeam: datadogV2.TeamHierarchyLinkCreateTeamRelationship{
                    Data: datadogV2.TeamHierarchyLinkCreateTeam{
                        Id:   DdTeam2DataID,
                        Type: datadogV2.TEAMTYPE_TEAM,
                    },
                },
            },
            Type: datadogV2.TEAMHIERARCHYLINKTYPE_TEAM_HIERARCHY_LINKS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.AddTeamHierarchyLink(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.AddTeamHierarchyLink`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.AddTeamHierarchyLink`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a team hierarchy link returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamHierarchyLinkCreate;
import com.datadog.api.client.v2.model.TeamHierarchyLinkCreateRelationships;
import com.datadog.api.client.v2.model.TeamHierarchyLinkCreateRequest;
import com.datadog.api.client.v2.model.TeamHierarchyLinkCreateTeam;
import com.datadog.api.client.v2.model.TeamHierarchyLinkCreateTeamRelationship;
import com.datadog.api.client.v2.model.TeamHierarchyLinkResponse;
import com.datadog.api.client.v2.model.TeamHierarchyLinkType;
import com.datadog.api.client.v2.model.TeamType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "dd_team_2" in the system
    String DD_TEAM_2_DATA_ID = System.getenv("DD_TEAM_2_DATA_ID");

    TeamHierarchyLinkCreateRequest body =
        new TeamHierarchyLinkCreateRequest()
            .data(
                new TeamHierarchyLinkCreate()
                    .relationships(
                        new TeamHierarchyLinkCreateRelationships()
                            .parentTeam(
                                new TeamHierarchyLinkCreateTeamRelationship()
                                    .data(
                                        new TeamHierarchyLinkCreateTeam()
                                            .id(DD_TEAM_DATA_ID)
                                            .type(TeamType.TEAM)))
                            .subTeam(
                                new TeamHierarchyLinkCreateTeamRelationship()
                                    .data(
                                        new TeamHierarchyLinkCreateTeam()
                                            .id(DD_TEAM_2_DATA_ID)
                                            .type(TeamType.TEAM))))
                    .type(TeamHierarchyLinkType.TEAM_HIERARCHY_LINKS));

    try {
      TeamHierarchyLinkResponse result = apiInstance.addTeamHierarchyLink(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#addTeamHierarchyLink");
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
Create a team hierarchy link returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_hierarchy_link_create import TeamHierarchyLinkCreate
from datadog_api_client.v2.model.team_hierarchy_link_create_relationships import TeamHierarchyLinkCreateRelationships
from datadog_api_client.v2.model.team_hierarchy_link_create_request import TeamHierarchyLinkCreateRequest
from datadog_api_client.v2.model.team_hierarchy_link_create_team import TeamHierarchyLinkCreateTeam
from datadog_api_client.v2.model.team_hierarchy_link_create_team_relationship import (
    TeamHierarchyLinkCreateTeamRelationship,
)
from datadog_api_client.v2.model.team_hierarchy_link_type import TeamHierarchyLinkType
from datadog_api_client.v2.model.team_type import TeamType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "dd_team_2" in the system
DD_TEAM_2_DATA_ID = environ["DD_TEAM_2_DATA_ID"]

body = TeamHierarchyLinkCreateRequest(
    data=TeamHierarchyLinkCreate(
        relationships=TeamHierarchyLinkCreateRelationships(
            parent_team=TeamHierarchyLinkCreateTeamRelationship(
                data=TeamHierarchyLinkCreateTeam(
                    id=DD_TEAM_DATA_ID,
                    type=TeamType.TEAM,
                ),
            ),
            sub_team=TeamHierarchyLinkCreateTeamRelationship(
                data=TeamHierarchyLinkCreateTeam(
                    id=DD_TEAM_2_DATA_ID,
                    type=TeamType.TEAM,
                ),
            ),
        ),
        type=TeamHierarchyLinkType.TEAM_HIERARCHY_LINKS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.add_team_hierarchy_link(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a team hierarchy link returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "dd_team_2" in the system
DD_TEAM_2_DATA_ID = ENV["DD_TEAM_2_DATA_ID"]

body = DatadogAPIClient::V2::TeamHierarchyLinkCreateRequest.new({
  data: DatadogAPIClient::V2::TeamHierarchyLinkCreate.new({
    relationships: DatadogAPIClient::V2::TeamHierarchyLinkCreateRelationships.new({
      parent_team: DatadogAPIClient::V2::TeamHierarchyLinkCreateTeamRelationship.new({
        data: DatadogAPIClient::V2::TeamHierarchyLinkCreateTeam.new({
          id: DD_TEAM_DATA_ID,
          type: DatadogAPIClient::V2::TeamType::TEAM,
        }),
      }),
      sub_team: DatadogAPIClient::V2::TeamHierarchyLinkCreateTeamRelationship.new({
        data: DatadogAPIClient::V2::TeamHierarchyLinkCreateTeam.new({
          id: DD_TEAM_2_DATA_ID,
          type: DatadogAPIClient::V2::TeamType::TEAM,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::TeamHierarchyLinkType::TEAM_HIERARCHY_LINKS,
  }),
})
p api_instance.add_team_hierarchy_link(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create a team hierarchy link returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamHierarchyLinkCreate;
use datadog_api_client::datadogV2::model::TeamHierarchyLinkCreateRelationships;
use datadog_api_client::datadogV2::model::TeamHierarchyLinkCreateRequest;
use datadog_api_client::datadogV2::model::TeamHierarchyLinkCreateTeam;
use datadog_api_client::datadogV2::model::TeamHierarchyLinkCreateTeamRelationship;
use datadog_api_client::datadogV2::model::TeamHierarchyLinkType;
use datadog_api_client::datadogV2::model::TeamType;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "dd_team_2" in the system
    let dd_team_2_data_id = std::env::var("DD_TEAM_2_DATA_ID").unwrap();
    let body = TeamHierarchyLinkCreateRequest::new(TeamHierarchyLinkCreate::new(
        TeamHierarchyLinkCreateRelationships::new(
            TeamHierarchyLinkCreateTeamRelationship::new(TeamHierarchyLinkCreateTeam::new(
                dd_team_data_id.clone(),
                TeamType::TEAM,
            )),
            TeamHierarchyLinkCreateTeamRelationship::new(TeamHierarchyLinkCreateTeam::new(
                dd_team_2_data_id.clone(),
                TeamType::TEAM,
            )),
        ),
        TeamHierarchyLinkType::TEAM_HIERARCHY_LINKS,
    ));
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.add_team_hierarchy_link(body).await;
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
 * Create a team hierarchy link returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "dd_team_2" in the system
const DD_TEAM_2_DATA_ID = process.env.DD_TEAM_2_DATA_ID as string;

const params: v2.TeamsApiAddTeamHierarchyLinkRequest = {
  body: {
    data: {
      relationships: {
        parentTeam: {
          data: {
            id: DD_TEAM_DATA_ID,
            type: "team",
          },
        },
        subTeam: {
          data: {
            id: DD_TEAM_2_DATA_ID,
            type: "team",
          },
        },
      },
      type: "team_hierarchy_links",
    },
  },
};

apiInstance
  .addTeamHierarchyLink(params)
  .then((data: v2.TeamHierarchyLinkResponse) => {
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

## Remove a member team{% #remove-a-member-team %}
**Note**: This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/team/{super_team_id}/member_teams/{member_team_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id} |

### Overview

Remove a super team's member team identified by `member_team_id`.

**Note**: This API is deprecated. For deleting team hierarchy links, use the team hierarchy links API: `DELETE /api/v2/team-hierarchy-links/{link_id}`.
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                             | Type   | Description |
| -------------------------------- | ------ | ----------- |
| super_team_id [*required*]  | string | None        |
| member_team_id [*required*] | string | None        |

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
API error response.
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
                  \# Path parametersexport super_team_id="CHANGE_ME"export member_team_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${super_team_id}/member_teams/${member_team_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove a member team returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.unstable_operations["remove_member_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.remove_member_team(
        super_team_id="super_team_id",
        member_team_id="member_team_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Remove a member team returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.remove_member_team".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new
api_instance.remove_member_team("super_team_id", "member_team_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Remove a member team returns "No Content" response

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
    configuration.SetUnstableOperationEnabled("v2.RemoveMemberTeam", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.RemoveMemberTeam(ctx, "super_team_id", "member_team_id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.RemoveMemberTeam`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Remove a member team returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.removeMemberTeam", true);
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    try {
      apiInstance.removeMemberTeam("super_team_id", "member_team_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#removeMemberTeam");
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
// Remove a member team returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.RemoveMemberTeam", true);
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .remove_member_team("super_team_id".to_string(), "member_team_id".to_string())
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
 * Remove a member team returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.removeMemberTeam"] = true;
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiRemoveMemberTeamRequest = {
  superTeamId: "super_team_id",
  memberTeamId: "member_team_id",
};

apiInstance
  .removeMemberTeam(params)
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
## Remove a team hierarchy link{% #remove-a-team-hierarchy-link %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/team-hierarchy-links/{link_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/team-hierarchy-links/{link_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/team-hierarchy-links/{link_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/{link_id} |

### Overview

Remove a team hierarchy link by the given link_id. This endpoint requires all of the following permissions:
`teams_read``teams_manage`

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                          |
| ------------------------- | ------ | ------------------------------------ |
| link_id [*required*] | string | The team hierarchy link's identifier |

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
API error response.
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
                  \# Path parametersexport link_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/${link_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove a team hierarchy link returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_ID = environ["TEAM_HIERARCHY_LINK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.remove_team_hierarchy_link(
        link_id=TEAM_HIERARCHY_LINK_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Remove a team hierarchy link returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_ID = ENV["TEAM_HIERARCHY_LINK_DATA_ID"]
api_instance.remove_team_hierarchy_link(TEAM_HIERARCHY_LINK_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Remove a team hierarchy link returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "team_hierarchy_link" in the system
    TeamHierarchyLinkDataID := os.Getenv("TEAM_HIERARCHY_LINK_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.RemoveTeamHierarchyLink(ctx, TeamHierarchyLinkDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.RemoveTeamHierarchyLink`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Remove a team hierarchy link returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "team_hierarchy_link" in the system
    String TEAM_HIERARCHY_LINK_DATA_ID = System.getenv("TEAM_HIERARCHY_LINK_DATA_ID");

    try {
      apiInstance.removeTeamHierarchyLink(TEAM_HIERARCHY_LINK_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#removeTeamHierarchyLink");
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
// Remove a team hierarchy link returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "team_hierarchy_link" in the system
    let team_hierarchy_link_data_id = std::env::var("TEAM_HIERARCHY_LINK_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .remove_team_hierarchy_link(team_hierarchy_link_data_id.clone())
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
 * Remove a team hierarchy link returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "team_hierarchy_link" in the system
const TEAM_HIERARCHY_LINK_DATA_ID = process.env
  .TEAM_HIERARCHY_LINK_DATA_ID as string;

const params: v2.TeamsApiRemoveTeamHierarchyLinkRequest = {
  linkId: TEAM_HIERARCHY_LINK_DATA_ID,
};

apiInstance
  .removeTeamHierarchyLink(params)
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

## List team connections{% #list-team-connections %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/connections |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/connections |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/connections      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/connections      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/connections     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/connections |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/connections |

### Overview

Returns all team connections. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Query Strings

| Name                       | Type    | Description                                                          |
| -------------------------- | ------- | -------------------------------------------------------------------- |
| page[size]                 | integer | Size for a given page. The maximum allowed value is 100.             |
| page[number]               | integer | Specific page number to return.                                      |
| filter[sources]            | array   | Filter team connections by external source systems.                  |
| filter[team_ids]           | array   | Filter team connections by Datadog team IDs.                         |
| filter[connected_team_ids] | array   | Filter team connections by connected team IDs from external systems. |
| filter[connection_ids]     | array   | Filter team connections by connection IDs.                           |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about multiple team connections.

| Parent field   | Field                  | Type     | Description                                                                 |
| -------------- | ---------------------- | -------- | --------------------------------------------------------------------------- |
|                | data                   | [object] | Array of team connections.                                                  |
| data           | attributes             | object   | Attributes of the team connection.                                          |
| attributes     | managed_by             | string   | The entity that manages this team connection.                               |
| attributes     | source                 | string   | The name of the external source.                                            |
| data           | id [*required*]   | string   | The unique identifier of the team connection.                               |
| data           | relationships          | object   | Relationships of the team connection.                                       |
| relationships  | connected_team         | object   | Reference to a team from an external system.                                |
| connected_team | data                   | object   | Reference to connected external team.                                       |
| data           | id [*required*]   | string   | The connected team ID as it is referenced throughout the Datadog ecosystem. |
| data           | type [*required*] | enum     | External team resource type. Allowed enum values: `github_team`             |
| relationships  | team                   | object   | Reference to a Datadog team.                                                |
| team           | data                   | object   | Reference to a Datadog team.                                                |
| data           | id [*required*]   | string   | The Datadog team ID.                                                        |
| data           | type [*required*] | enum     | Datadog team resource type. Allowed enum values: `team`                     |
| data           | type [*required*] | enum     | Team connection resource type. Allowed enum values: `team_connection`       |
|                | meta                   | object   | Connections response metadata.                                              |
| meta           | page                   | object   | Page-based pagination metadata.                                             |
| page           | first_number           | int64    | The first page number.                                                      |
| page           | last_number            | int64    | The last page number.                                                       |
| page           | next_number            | int64    | The next page number.                                                       |
| page           | number                 | int64    | The current page number.                                                    |
| page           | prev_number            | int64    | The previous page number.                                                   |
| page           | size                   | int64    | The page size.                                                              |
| page           | total                  | int64    | Total connections matching request.                                         |
| page           | type                   | string   | Pagination type.                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "managed_by": "github_sync",
        "source": "github"
      },
      "id": "12345678-1234-5678-9abc-123456789012",
      "relationships": {
        "connected_team": {
          "data": {
            "id": "@GitHubOrg/team-handle",
            "type": "github_team"
          }
        },
        "team": {
          "data": {
            "id": "87654321-4321-8765-dcba-210987654321",
            "type": "team"
          }
        }
      },
      "type": "team_connection"
    }
  ],
  "meta": {
    "page": {
      "first_number": "integer",
      "last_number": "integer",
      "next_number": "integer",
      "number": "integer",
      "prev_number": "integer",
      "size": "integer",
      "total": "integer",
      "type": "number_size"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/connections" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```ruby
# List team connections returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.list_team_connections()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```python
"""
List team connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_team_connections()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```go
// List team connections returns "OK" response

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
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.ListTeamConnections(ctx, *datadogV2.NewListTeamConnectionsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.ListTeamConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.ListTeamConnections`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List team connections returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamConnectionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    try {
      TeamConnectionsResponse result = apiInstance.listTeamConnections();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#listTeamConnections");
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
// List team connections returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::ListTeamConnectionsOptionalParams;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .list_team_connections(ListTeamConnectionsOptionalParams::default())
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
 * List team connections returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

apiInstance
  .listTeamConnections()
  .then((data: v2.TeamConnectionsResponse) => {
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

## Create team connections{% #create-team-connections %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team/connections |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team/connections |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team/connections      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team/connections      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team/connections     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team/connections |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team/connections |

### Overview

Create multiple team connections. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field   | Field                  | Type     | Description                                                                 |
| -------------- | ---------------------- | -------- | --------------------------------------------------------------------------- |
|                | data [*required*] | [object] | Array of team connections to create.                                        |
| data           | attributes             | object   | Attributes of the team connection.                                          |
| attributes     | managed_by             | string   | The entity that manages this team connection.                               |
| attributes     | source                 | string   | The name of the external source.                                            |
| data           | relationships          | object   | Relationships of the team connection.                                       |
| relationships  | connected_team         | object   | Reference to a team from an external system.                                |
| connected_team | data                   | object   | Reference to connected external team.                                       |
| data           | id [*required*]   | string   | The connected team ID as it is referenced throughout the Datadog ecosystem. |
| data           | type [*required*] | enum     | External team resource type. Allowed enum values: `github_team`             |
| relationships  | team                   | object   | Reference to a Datadog team.                                                |
| team           | data                   | object   | Reference to a Datadog team.                                                |
| data           | id [*required*]   | string   | The Datadog team ID.                                                        |
| data           | type [*required*] | enum     | Datadog team resource type. Allowed enum values: `team`                     |
| data           | type [*required*] | enum     | Team connection resource type. Allowed enum values: `team_connection`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "managed_by": "github_sync",
        "source": "github"
      },
      "relationships": {
        "connected_team": {
          "data": {
            "id": "@GitHubOrg/team-handle",
            "type": "github_team"
          }
        },
        "team": {
          "data": {
            "id": "87654321-4321-8765-dcba-210987654321",
            "type": "team"
          }
        }
      },
      "type": "team_connection"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response containing information about multiple team connections.

| Parent field   | Field                  | Type     | Description                                                                 |
| -------------- | ---------------------- | -------- | --------------------------------------------------------------------------- |
|                | data                   | [object] | Array of team connections.                                                  |
| data           | attributes             | object   | Attributes of the team connection.                                          |
| attributes     | managed_by             | string   | The entity that manages this team connection.                               |
| attributes     | source                 | string   | The name of the external source.                                            |
| data           | id [*required*]   | string   | The unique identifier of the team connection.                               |
| data           | relationships          | object   | Relationships of the team connection.                                       |
| relationships  | connected_team         | object   | Reference to a team from an external system.                                |
| connected_team | data                   | object   | Reference to connected external team.                                       |
| data           | id [*required*]   | string   | The connected team ID as it is referenced throughout the Datadog ecosystem. |
| data           | type [*required*] | enum     | External team resource type. Allowed enum values: `github_team`             |
| relationships  | team                   | object   | Reference to a Datadog team.                                                |
| team           | data                   | object   | Reference to a Datadog team.                                                |
| data           | id [*required*]   | string   | The Datadog team ID.                                                        |
| data           | type [*required*] | enum     | Datadog team resource type. Allowed enum values: `team`                     |
| data           | type [*required*] | enum     | Team connection resource type. Allowed enum values: `team_connection`       |
|                | meta                   | object   | Connections response metadata.                                              |
| meta           | page                   | object   | Page-based pagination metadata.                                             |
| page           | first_number           | int64    | The first page number.                                                      |
| page           | last_number            | int64    | The last page number.                                                       |
| page           | next_number            | int64    | The next page number.                                                       |
| page           | number                 | int64    | The current page number.                                                    |
| page           | prev_number            | int64    | The previous page number.                                                   |
| page           | size                   | int64    | The page size.                                                              |
| page           | total                  | int64    | Total connections matching request.                                         |
| page           | type                   | string   | Pagination type.                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "managed_by": "github_sync",
        "source": "github"
      },
      "id": "12345678-1234-5678-9abc-123456789012",
      "relationships": {
        "connected_team": {
          "data": {
            "id": "@GitHubOrg/team-handle",
            "type": "github_team"
          }
        },
        "team": {
          "data": {
            "id": "87654321-4321-8765-dcba-210987654321",
            "type": "team"
          }
        }
      },
      "type": "team_connection"
    }
  ],
  "meta": {
    "page": {
      "first_number": "integer",
      "last_number": "integer",
      "next_number": "integer",
      "number": "integer",
      "prev_number": "integer",
      "size": "integer",
      "total": "integer",
      "type": "number_size"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/connections" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "relationships": {
        "connected_team": {
          "data": {
            "id": "@GitHubOrg/team-handle",
            "type": "github_team"
          }
        },
        "team": {
          "data": {
            "id": "87654321-4321-8765-dcba-210987654321",
            "type": "team"
          }
        }
      },
      "type": "team_connection"
    }
  ]
}
EOF

#####

```python
"""
Create team connections returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.connected_team_ref import ConnectedTeamRef
from datadog_api_client.v2.model.connected_team_ref_data import ConnectedTeamRefData
from datadog_api_client.v2.model.connected_team_ref_data_type import ConnectedTeamRefDataType
from datadog_api_client.v2.model.team_connection_attributes import TeamConnectionAttributes
from datadog_api_client.v2.model.team_connection_create_data import TeamConnectionCreateData
from datadog_api_client.v2.model.team_connection_create_request import TeamConnectionCreateRequest
from datadog_api_client.v2.model.team_connection_relationships import TeamConnectionRelationships
from datadog_api_client.v2.model.team_connection_type import TeamConnectionType
from datadog_api_client.v2.model.team_ref import TeamRef
from datadog_api_client.v2.model.team_ref_data import TeamRefData
from datadog_api_client.v2.model.team_ref_data_type import TeamRefDataType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamConnectionCreateRequest(
    data=[
        TeamConnectionCreateData(
            type=TeamConnectionType.TEAM_CONNECTION,
            attributes=TeamConnectionAttributes(
                source="github",
                managed_by="datadog",
            ),
            relationships=TeamConnectionRelationships(
                team=TeamRef(
                    data=TeamRefData(
                        id=DD_TEAM_DATA_ID,
                        type=TeamRefDataType.TEAM,
                    ),
                ),
                connected_team=ConnectedTeamRef(
                    data=ConnectedTeamRefData(
                        id="@MyGitHubAccount/my-team-name",
                        type=ConnectedTeamRefDataType.GITHUB_TEAM,
                    ),
                ),
            ),
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["create_team_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_connections(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create team connections returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_team_connections".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::TeamConnectionCreateRequest.new({
  data: [
    DatadogAPIClient::V2::TeamConnectionCreateData.new({
      type: DatadogAPIClient::V2::TeamConnectionType::TEAM_CONNECTION,
      attributes: DatadogAPIClient::V2::TeamConnectionAttributes.new({
        source: "github",
        managed_by: "datadog",
      }),
      relationships: DatadogAPIClient::V2::TeamConnectionRelationships.new({
        team: DatadogAPIClient::V2::TeamRef.new({
          data: DatadogAPIClient::V2::TeamRefData.new({
            id: DD_TEAM_DATA_ID,
            type: DatadogAPIClient::V2::TeamRefDataType::TEAM,
          }),
        }),
        connected_team: DatadogAPIClient::V2::ConnectedTeamRef.new({
          data: DatadogAPIClient::V2::ConnectedTeamRefData.new({
            id: "@MyGitHubAccount/my-team-name",
            type: DatadogAPIClient::V2::ConnectedTeamRefDataType::GITHUB_TEAM,
          }),
        }),
      }),
    }),
  ],
})
p api_instance.create_team_connections(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create team connections returns "Created" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    body := datadogV2.TeamConnectionCreateRequest{
        Data: []datadogV2.TeamConnectionCreateData{
            {
                Type: datadogV2.TEAMCONNECTIONTYPE_TEAM_CONNECTION,
                Attributes: &datadogV2.TeamConnectionAttributes{
                    Source:    datadog.PtrString("github"),
                    ManagedBy: datadog.PtrString("datadog"),
                },
                Relationships: &datadogV2.TeamConnectionRelationships{
                    Team: &datadogV2.TeamRef{
                        Data: &datadogV2.TeamRefData{
                            Id:   DdTeamDataID,
                            Type: datadogV2.TEAMREFDATATYPE_TEAM,
                        },
                    },
                    ConnectedTeam: &datadogV2.ConnectedTeamRef{
                        Data: &datadogV2.ConnectedTeamRefData{
                            Id:   "@MyGitHubAccount/my-team-name",
                            Type: datadogV2.CONNECTEDTEAMREFDATATYPE_GITHUB_TEAM,
                        },
                    },
                },
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateTeamConnections", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.CreateTeamConnections(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.CreateTeamConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.CreateTeamConnections`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create team connections returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.ConnectedTeamRef;
import com.datadog.api.client.v2.model.ConnectedTeamRefData;
import com.datadog.api.client.v2.model.ConnectedTeamRefDataType;
import com.datadog.api.client.v2.model.TeamConnectionAttributes;
import com.datadog.api.client.v2.model.TeamConnectionCreateData;
import com.datadog.api.client.v2.model.TeamConnectionCreateRequest;
import com.datadog.api.client.v2.model.TeamConnectionRelationships;
import com.datadog.api.client.v2.model.TeamConnectionType;
import com.datadog.api.client.v2.model.TeamConnectionsResponse;
import com.datadog.api.client.v2.model.TeamRef;
import com.datadog.api.client.v2.model.TeamRefData;
import com.datadog.api.client.v2.model.TeamRefDataType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createTeamConnections", true);
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    TeamConnectionCreateRequest body =
        new TeamConnectionCreateRequest()
            .data(
                Collections.singletonList(
                    new TeamConnectionCreateData()
                        .type(TeamConnectionType.TEAM_CONNECTION)
                        .attributes(
                            new TeamConnectionAttributes().source("github").managedBy("datadog"))
                        .relationships(
                            new TeamConnectionRelationships()
                                .team(
                                    new TeamRef()
                                        .data(
                                            new TeamRefData()
                                                .id(DD_TEAM_DATA_ID)
                                                .type(TeamRefDataType.TEAM)))
                                .connectedTeam(
                                    new ConnectedTeamRef()
                                        .data(
                                            new ConnectedTeamRefData()
                                                .id("@MyGitHubAccount/my-team-name")
                                                .type(ConnectedTeamRefDataType.GITHUB_TEAM))))));

    try {
      TeamConnectionsResponse result = apiInstance.createTeamConnections(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#createTeamConnections");
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
// Create team connections returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::ConnectedTeamRef;
use datadog_api_client::datadogV2::model::ConnectedTeamRefData;
use datadog_api_client::datadogV2::model::ConnectedTeamRefDataType;
use datadog_api_client::datadogV2::model::TeamConnectionAttributes;
use datadog_api_client::datadogV2::model::TeamConnectionCreateData;
use datadog_api_client::datadogV2::model::TeamConnectionCreateRequest;
use datadog_api_client::datadogV2::model::TeamConnectionRelationships;
use datadog_api_client::datadogV2::model::TeamConnectionType;
use datadog_api_client::datadogV2::model::TeamRef;
use datadog_api_client::datadogV2::model::TeamRefData;
use datadog_api_client::datadogV2::model::TeamRefDataType;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = TeamConnectionCreateRequest::new(vec![TeamConnectionCreateData::new(
        TeamConnectionType::TEAM_CONNECTION,
    )
    .attributes(
        TeamConnectionAttributes::new()
            .managed_by("datadog".to_string())
            .source("github".to_string()),
    )
    .relationships(
        TeamConnectionRelationships::new()
            .connected_team(ConnectedTeamRef::new().data(ConnectedTeamRefData::new(
                "@MyGitHubAccount/my-team-name".to_string(),
                ConnectedTeamRefDataType::GITHUB_TEAM,
            )))
            .team(TeamRef::new().data(TeamRefData::new(
                dd_team_data_id.clone(),
                TeamRefDataType::TEAM,
            ))),
    )]);
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateTeamConnections", true);
    let api = TeamsAPI::with_config(configuration);
    let resp = api.create_team_connections(body).await;
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
 * Create team connections returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createTeamConnections"] = true;
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiCreateTeamConnectionsRequest = {
  body: {
    data: [
      {
        type: "team_connection",
        attributes: {
          source: "github",
          managedBy: "datadog",
        },
        relationships: {
          team: {
            data: {
              id: DD_TEAM_DATA_ID,
              type: "team",
            },
          },
          connectedTeam: {
            data: {
              id: "@MyGitHubAccount/my-team-name",
              type: "github_team",
            },
          },
        },
      },
    ],
  },
};

apiInstance
  .createTeamConnections(params)
  .then((data: v2.TeamConnectionsResponse) => {
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

## Delete team connections{% #delete-team-connections %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/team/connections |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/team/connections |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/team/connections      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/team/connections      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/team/connections     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/team/connections |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/team/connections |

### Overview

Delete multiple team connections. This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                           |
| ------------ | ---------------------- | -------- | --------------------------------------------------------------------- |
|              | data [*required*] | [object] | Array of team connection IDs to delete.                               |
| data         | id [*required*]   | string   | The unique identifier of the team connection to delete.               |
| data         | type [*required*] | enum     | Team connection resource type. Allowed enum values: `team_connection` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "12345678-1234-5678-9abc-123456789012",
      "type": "team_connection"
    }
  ]
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
                  \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/connections" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "id": "12345678-1234-5678-9abc-123456789012",
      "type": "team_connection"
    }
  ]
}
EOF

#####

```python
"""
Delete team connections returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_connection_delete_request import TeamConnectionDeleteRequest
from datadog_api_client.v2.model.team_connection_delete_request_data_item import TeamConnectionDeleteRequestDataItem
from datadog_api_client.v2.model.team_connection_type import TeamConnectionType

body = TeamConnectionDeleteRequest(
    data=[
        TeamConnectionDeleteRequestDataItem(
            id="12345678-1234-5678-9abc-123456789012",
            type=TeamConnectionType.TEAM_CONNECTION,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team_connections(body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete team connections returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::TeamConnectionDeleteRequest.new({
  data: [
    DatadogAPIClient::V2::TeamConnectionDeleteRequestDataItem.new({
      id: "12345678-1234-5678-9abc-123456789012",
      type: DatadogAPIClient::V2::TeamConnectionType::TEAM_CONNECTION,
    }),
  ],
})
api_instance.delete_team_connections(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete team connections returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.TeamConnectionDeleteRequest{
        Data: []datadogV2.TeamConnectionDeleteRequestDataItem{
            {
                Id:   "12345678-1234-5678-9abc-123456789012",
                Type: datadogV2.TEAMCONNECTIONTYPE_TEAM_CONNECTION,
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.DeleteTeamConnections(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.DeleteTeamConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete team connections returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamConnectionDeleteRequest;
import com.datadog.api.client.v2.model.TeamConnectionDeleteRequestDataItem;
import com.datadog.api.client.v2.model.TeamConnectionType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    TeamConnectionDeleteRequest body =
        new TeamConnectionDeleteRequest()
            .data(
                Collections.singletonList(
                    new TeamConnectionDeleteRequestDataItem()
                        .id("12345678-1234-5678-9abc-123456789012")
                        .type(TeamConnectionType.TEAM_CONNECTION)));

    try {
      apiInstance.deleteTeamConnections(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#deleteTeamConnections");
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
// Delete team connections returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamConnectionDeleteRequest;
use datadog_api_client::datadogV2::model::TeamConnectionDeleteRequestDataItem;
use datadog_api_client::datadogV2::model::TeamConnectionType;

#[tokio::main]
async fn main() {
    let body = TeamConnectionDeleteRequest::new(vec![TeamConnectionDeleteRequestDataItem::new(
        "12345678-1234-5678-9abc-123456789012".to_string(),
        TeamConnectionType::TEAM_CONNECTION,
    )]);
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api.delete_team_connections(body).await;
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
 * Delete team connections returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiDeleteTeamConnectionsRequest = {
  body: {
    data: [
      {
        id: "12345678-1234-5678-9abc-123456789012",
        type: "team_connection",
      },
    ],
  },
};

apiInstance
  .deleteTeamConnections(params)
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

## Get team notification rules{% #get-team-notification-rules %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules |

### Overview

This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team notification rules response

| Parent field | Field                        | Type     | Description                                                                                                       |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
|              | data                         | [object] | Team notification rules response data                                                                             |
| data         | attributes [*required*] | object   | Team notification rule attributes                                                                                 |
| attributes   | email                        | object   | Email notification settings for the team                                                                          |
| email        | enabled                      | boolean  | Flag indicating email notification                                                                                |
| attributes   | ms_teams                     | object   | MS Teams notification settings for the team                                                                       |
| ms_teams     | connector_name               | string   | Handle for MS Teams                                                                                               |
| attributes   | pagerduty                    | object   | PagerDuty notification settings for the team                                                                      |
| pagerduty    | service_name                 | string   | Service name for PagerDuty                                                                                        |
| attributes   | slack                        | object   | Slack notification settings for the team                                                                          |
| slack        | channel                      | string   | Channel for Slack notification                                                                                    |
| slack        | workspace                    | string   | Workspace for Slack notification                                                                                  |
| data         | id                           | string   | The identifier of the team notification rule                                                                      |
| data         | type [*required*]       | enum     | Team notification rule type Allowed enum values: `team_notification_rules`                                        |
|              | meta                         | object   | Metadata that is included in the response when querying the team notification rules                               |
| meta         | page                         | object   | Metadata related to paging information that is included in the response when querying the team notification rules |
| page         | first_offset                 | int64    | The first offset.                                                                                                 |
| page         | last_offset                  | int64    | The last offset.                                                                                                  |
| page         | limit                        | int64    | Pagination limit.                                                                                                 |
| page         | next_offset                  | int64    | The next offset.                                                                                                  |
| page         | offset                       | int64    | The offset.                                                                                                       |
| page         | prev_offset                  | int64    | The previous offset.                                                                                              |
| page         | total                        | int64    | Total results.                                                                                                    |
| page         | type                         | string   | Offset type.                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "email": {
          "enabled": false
        },
        "ms_teams": {
          "connector_name": "string"
        },
        "pagerduty": {
          "service_name": "string"
        },
        "slack": {
          "channel": "string",
          "workspace": "string"
        }
      },
      "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
      "type": "team_notification_rules"
    }
  ],
  "meta": {
    "page": {
      "first_offset": "integer",
      "last_offset": "integer",
      "limit": "integer",
      "next_offset": "integer",
      "offset": "integer",
      "prev_offset": "integer",
      "total": "integer",
      "type": "string"
    }
  }
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get team notification rules returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_notification_rules(
        team_id=DD_TEAM_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get team notification rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team_notification_rules(DD_TEAM_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get team notification rules returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamNotificationRules(ctx, DdTeamDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamNotificationRules`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamNotificationRules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get team notification rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamNotificationRulesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    try {
      TeamNotificationRulesResponse result = apiInstance.getTeamNotificationRules(DD_TEAM_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamNotificationRules");
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
// Get team notification rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .get_team_notification_rules(dd_team_data_id.clone())
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
 * Get team notification rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiGetTeamNotificationRulesRequest = {
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .getTeamNotificationRules(params)
  .then((data: v2.TeamNotificationRulesResponse) => {
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

## Create team notification rule{% #create-team-notification-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules |

### Overview

This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                |
| ------------ | ---------------------------- | ------- | -------------------------------------------------------------------------- |
|              | data [*required*]       | object  | Team notification rule                                                     |
| data         | attributes [*required*] | object  | Team notification rule attributes                                          |
| attributes   | email                        | object  | Email notification settings for the team                                   |
| email        | enabled                      | boolean | Flag indicating email notification                                         |
| attributes   | ms_teams                     | object  | MS Teams notification settings for the team                                |
| ms_teams     | connector_name               | string  | Handle for MS Teams                                                        |
| attributes   | pagerduty                    | object  | PagerDuty notification settings for the team                               |
| pagerduty    | service_name                 | string  | Service name for PagerDuty                                                 |
| attributes   | slack                        | object  | Slack notification settings for the team                                   |
| slack        | channel                      | string  | Channel for Slack notification                                             |
| slack        | workspace                    | string  | Workspace for Slack notification                                           |
| data         | id                           | string  | The identifier of the team notification rule                               |
| data         | type [*required*]       | enum    | Team notification rule type Allowed enum values: `team_notification_rules` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "team_notification_rules",
    "attributes": {
      "email": {
        "enabled": true
      },
      "slack": {
        "workspace": "Datadog",
        "channel": "aaa-omg-ops"
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Team notification rule response

| Parent field | Field                        | Type    | Description                                                                |
| ------------ | ---------------------------- | ------- | -------------------------------------------------------------------------- |
|              | data                         | object  | Team notification rule                                                     |
| data         | attributes [*required*] | object  | Team notification rule attributes                                          |
| attributes   | email                        | object  | Email notification settings for the team                                   |
| email        | enabled                      | boolean | Flag indicating email notification                                         |
| attributes   | ms_teams                     | object  | MS Teams notification settings for the team                                |
| ms_teams     | connector_name               | string  | Handle for MS Teams                                                        |
| attributes   | pagerduty                    | object  | PagerDuty notification settings for the team                               |
| pagerduty    | service_name                 | string  | Service name for PagerDuty                                                 |
| attributes   | slack                        | object  | Slack notification settings for the team                                   |
| slack        | channel                      | string  | Channel for Slack notification                                             |
| slack        | workspace                    | string  | Workspace for Slack notification                                           |
| data         | id                           | string  | The identifier of the team notification rule                               |
| data         | type [*required*]       | enum    | Team notification rule type Allowed enum values: `team_notification_rules` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "email": {
        "enabled": false
      },
      "ms_teams": {
        "connector_name": "string"
      },
      "pagerduty": {
        "service_name": "string"
      },
      "slack": {
        "channel": "string",
        "workspace": "string"
      }
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "type": "team_notification_rules"
  }
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
API error response.
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
API error response.
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
                          \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "team_notification_rules",
    "attributes": {
      "email": {
        "enabled": true
      },
      "slack": {
        "workspace": "Datadog",
        "channel": "aaa-omg-ops"
      }
    }
  }
}
EOF

#####

```go
// Create team notification rule returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    body := datadogV2.TeamNotificationRuleRequest{
        Data: datadogV2.TeamNotificationRule{
            Type: datadogV2.TEAMNOTIFICATIONRULETYPE_TEAM_NOTIFICATION_RULES,
            Attributes: datadogV2.TeamNotificationRuleAttributes{
                Email: &datadogV2.TeamNotificationRuleAttributesEmail{
                    Enabled: datadog.PtrBool(true),
                },
                Slack: &datadogV2.TeamNotificationRuleAttributesSlack{
                    Workspace: datadog.PtrString("Datadog"),
                    Channel:   datadog.PtrString("aaa-omg-ops"),
                },
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.CreateTeamNotificationRule(ctx, DdTeamDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.CreateTeamNotificationRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.CreateTeamNotificationRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create team notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamNotificationRule;
import com.datadog.api.client.v2.model.TeamNotificationRuleAttributes;
import com.datadog.api.client.v2.model.TeamNotificationRuleAttributesEmail;
import com.datadog.api.client.v2.model.TeamNotificationRuleAttributesSlack;
import com.datadog.api.client.v2.model.TeamNotificationRuleRequest;
import com.datadog.api.client.v2.model.TeamNotificationRuleResponse;
import com.datadog.api.client.v2.model.TeamNotificationRuleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    TeamNotificationRuleRequest body =
        new TeamNotificationRuleRequest()
            .data(
                new TeamNotificationRule()
                    .type(TeamNotificationRuleType.TEAM_NOTIFICATION_RULES)
                    .attributes(
                        new TeamNotificationRuleAttributes()
                            .email(new TeamNotificationRuleAttributesEmail().enabled(true))
                            .slack(
                                new TeamNotificationRuleAttributesSlack()
                                    .workspace("Datadog")
                                    .channel("aaa-omg-ops"))));

    try {
      TeamNotificationRuleResponse result =
          apiInstance.createTeamNotificationRule(DD_TEAM_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#createTeamNotificationRule");
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
Create team notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_notification_rule import TeamNotificationRule
from datadog_api_client.v2.model.team_notification_rule_attributes import TeamNotificationRuleAttributes
from datadog_api_client.v2.model.team_notification_rule_attributes_email import TeamNotificationRuleAttributesEmail
from datadog_api_client.v2.model.team_notification_rule_attributes_slack import TeamNotificationRuleAttributesSlack
from datadog_api_client.v2.model.team_notification_rule_request import TeamNotificationRuleRequest
from datadog_api_client.v2.model.team_notification_rule_type import TeamNotificationRuleType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamNotificationRuleRequest(
    data=TeamNotificationRule(
        type=TeamNotificationRuleType.TEAM_NOTIFICATION_RULES,
        attributes=TeamNotificationRuleAttributes(
            email=TeamNotificationRuleAttributesEmail(
                enabled=True,
            ),
            slack=TeamNotificationRuleAttributesSlack(
                workspace="Datadog",
                channel="aaa-omg-ops",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_notification_rule(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create team notification rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::TeamNotificationRuleRequest.new({
  data: DatadogAPIClient::V2::TeamNotificationRule.new({
    type: DatadogAPIClient::V2::TeamNotificationRuleType::TEAM_NOTIFICATION_RULES,
    attributes: DatadogAPIClient::V2::TeamNotificationRuleAttributes.new({
      email: DatadogAPIClient::V2::TeamNotificationRuleAttributesEmail.new({
        enabled: true,
      }),
      slack: DatadogAPIClient::V2::TeamNotificationRuleAttributesSlack.new({
        workspace: "Datadog",
        channel: "aaa-omg-ops",
      }),
    }),
  }),
})
p api_instance.create_team_notification_rule(DD_TEAM_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create team notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamNotificationRule;
use datadog_api_client::datadogV2::model::TeamNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::TeamNotificationRuleAttributesEmail;
use datadog_api_client::datadogV2::model::TeamNotificationRuleAttributesSlack;
use datadog_api_client::datadogV2::model::TeamNotificationRuleRequest;
use datadog_api_client::datadogV2::model::TeamNotificationRuleType;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = TeamNotificationRuleRequest::new(TeamNotificationRule::new(
        TeamNotificationRuleAttributes::new()
            .email(TeamNotificationRuleAttributesEmail::new().enabled(true))
            .slack(
                TeamNotificationRuleAttributesSlack::new()
                    .channel("aaa-omg-ops".to_string())
                    .workspace("Datadog".to_string()),
            ),
        TeamNotificationRuleType::TEAM_NOTIFICATION_RULES,
    ));
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .create_team_notification_rule(dd_team_data_id.clone(), body)
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
 * Create team notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.TeamsApiCreateTeamNotificationRuleRequest = {
  body: {
    data: {
      type: "team_notification_rules",
      attributes: {
        email: {
          enabled: true,
        },
        slack: {
          workspace: "Datadog",
          channel: "aaa-omg-ops",
        },
      },
    },
  },
  teamId: DD_TEAM_DATA_ID,
};

apiInstance
  .createTeamNotificationRule(params)
  .then((data: v2.TeamNotificationRuleResponse) => {
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

## Get team notification rule{% #get-team-notification-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules/{rule_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules/{rule_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |

### Overview

This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| rule_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team notification rule response

| Parent field | Field                        | Type    | Description                                                                |
| ------------ | ---------------------------- | ------- | -------------------------------------------------------------------------- |
|              | data                         | object  | Team notification rule                                                     |
| data         | attributes [*required*] | object  | Team notification rule attributes                                          |
| attributes   | email                        | object  | Email notification settings for the team                                   |
| email        | enabled                      | boolean | Flag indicating email notification                                         |
| attributes   | ms_teams                     | object  | MS Teams notification settings for the team                                |
| ms_teams     | connector_name               | string  | Handle for MS Teams                                                        |
| attributes   | pagerduty                    | object  | PagerDuty notification settings for the team                               |
| pagerduty    | service_name                 | string  | Service name for PagerDuty                                                 |
| attributes   | slack                        | object  | Slack notification settings for the team                                   |
| slack        | channel                      | string  | Channel for Slack notification                                             |
| slack        | workspace                    | string  | Workspace for Slack notification                                           |
| data         | id                           | string  | The identifier of the team notification rule                               |
| data         | type [*required*]       | enum    | Team notification rule type Allowed enum values: `team_notification_rules` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "email": {
        "enabled": false
      },
      "ms_teams": {
        "connector_name": "string"
      },
      "pagerduty": {
        "service_name": "string"
      },
      "slack": {
        "channel": "string",
        "workspace": "string"
      }
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "type": "team_notification_rules"
  }
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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"export rule_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules/${rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get team notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_notification_rule" in the system
TEAM_NOTIFICATION_RULE_DATA_ID = environ["TEAM_NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_notification_rule(
        team_id=DD_TEAM_DATA_ID,
        rule_id=TEAM_NOTIFICATION_RULE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get team notification rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_notification_rule" in the system
TEAM_NOTIFICATION_RULE_DATA_ID = ENV["TEAM_NOTIFICATION_RULE_DATA_ID"]
p api_instance.get_team_notification_rule(DD_TEAM_DATA_ID, TEAM_NOTIFICATION_RULE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get team notification rule returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "team_notification_rule" in the system
    TeamNotificationRuleDataID := os.Getenv("TEAM_NOTIFICATION_RULE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.GetTeamNotificationRule(ctx, DdTeamDataID, TeamNotificationRuleDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.GetTeamNotificationRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.GetTeamNotificationRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get team notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamNotificationRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "team_notification_rule" in the system
    String TEAM_NOTIFICATION_RULE_DATA_ID = System.getenv("TEAM_NOTIFICATION_RULE_DATA_ID");

    try {
      TeamNotificationRuleResponse result =
          apiInstance.getTeamNotificationRule(DD_TEAM_DATA_ID, TEAM_NOTIFICATION_RULE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamNotificationRule");
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
// Get team notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "team_notification_rule" in the system
    let team_notification_rule_data_id = std::env::var("TEAM_NOTIFICATION_RULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .get_team_notification_rule(
            dd_team_data_id.clone(),
            team_notification_rule_data_id.clone(),
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
 * Get team notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "team_notification_rule" in the system
const TEAM_NOTIFICATION_RULE_DATA_ID = process.env
  .TEAM_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.TeamsApiGetTeamNotificationRuleRequest = {
  teamId: DD_TEAM_DATA_ID,
  ruleId: TEAM_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .getTeamNotificationRule(params)
  .then((data: v2.TeamNotificationRuleResponse) => {
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

## Update team notification rule{% #update-team-notification-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules/{rule_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules/{rule_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |

### Overview

This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| rule_id [*required*] | string | None        |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                |
| ------------ | ---------------------------- | ------- | -------------------------------------------------------------------------- |
|              | data [*required*]       | object  | Team notification rule                                                     |
| data         | attributes [*required*] | object  | Team notification rule attributes                                          |
| attributes   | email                        | object  | Email notification settings for the team                                   |
| email        | enabled                      | boolean | Flag indicating email notification                                         |
| attributes   | ms_teams                     | object  | MS Teams notification settings for the team                                |
| ms_teams     | connector_name               | string  | Handle for MS Teams                                                        |
| attributes   | pagerduty                    | object  | PagerDuty notification settings for the team                               |
| pagerduty    | service_name                 | string  | Service name for PagerDuty                                                 |
| attributes   | slack                        | object  | Slack notification settings for the team                                   |
| slack        | channel                      | string  | Channel for Slack notification                                             |
| slack        | workspace                    | string  | Workspace for Slack notification                                           |
| data         | id                           | string  | The identifier of the team notification rule                               |
| data         | type [*required*]       | enum    | Team notification rule type Allowed enum values: `team_notification_rules` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "team_notification_rules",
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "attributes": {
      "pagerduty": {
        "service_name": "Datadog-prod"
      },
      "slack": {
        "workspace": "Datadog",
        "channel": "aaa-governance-ops"
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Team notification rule response

| Parent field | Field                        | Type    | Description                                                                |
| ------------ | ---------------------------- | ------- | -------------------------------------------------------------------------- |
|              | data                         | object  | Team notification rule                                                     |
| data         | attributes [*required*] | object  | Team notification rule attributes                                          |
| attributes   | email                        | object  | Email notification settings for the team                                   |
| email        | enabled                      | boolean | Flag indicating email notification                                         |
| attributes   | ms_teams                     | object  | MS Teams notification settings for the team                                |
| ms_teams     | connector_name               | string  | Handle for MS Teams                                                        |
| attributes   | pagerduty                    | object  | PagerDuty notification settings for the team                               |
| pagerduty    | service_name                 | string  | Service name for PagerDuty                                                 |
| attributes   | slack                        | object  | Slack notification settings for the team                                   |
| slack        | channel                      | string  | Channel for Slack notification                                             |
| slack        | workspace                    | string  | Workspace for Slack notification                                           |
| data         | id                           | string  | The identifier of the team notification rule                               |
| data         | type [*required*]       | enum    | Team notification rule type Allowed enum values: `team_notification_rules` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "email": {
        "enabled": false
      },
      "ms_teams": {
        "connector_name": "string"
      },
      "pagerduty": {
        "service_name": "string"
      },
      "slack": {
        "channel": "string",
        "workspace": "string"
      }
    },
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "type": "team_notification_rules"
  }
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
API error response.
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
                          \# Path parametersexport team_id="CHANGE_ME"export rule_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "team_notification_rules",
    "id": "b8626d7e-cedd-11eb-abf5-da7ad0900001",
    "attributes": {
      "pagerduty": {
        "service_name": "Datadog-prod"
      },
      "slack": {
        "workspace": "Datadog",
        "channel": "aaa-governance-ops"
      }
    }
  }
}
EOF

#####

```go
// Update team notification rule returns "OK" response

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
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "team_notification_rule" in the system
    TeamNotificationRuleDataID := os.Getenv("TEAM_NOTIFICATION_RULE_DATA_ID")

    body := datadogV2.TeamNotificationRuleRequest{
        Data: datadogV2.TeamNotificationRule{
            Type: datadogV2.TEAMNOTIFICATIONRULETYPE_TEAM_NOTIFICATION_RULES,
            Id:   datadog.PtrString(TeamNotificationRuleDataID),
            Attributes: datadogV2.TeamNotificationRuleAttributes{
                Pagerduty: &datadogV2.TeamNotificationRuleAttributesPagerduty{
                    ServiceName: datadog.PtrString("Datadog-prod"),
                },
                Slack: &datadogV2.TeamNotificationRuleAttributesSlack{
                    Workspace: datadog.PtrString("Datadog"),
                    Channel:   datadog.PtrString("aaa-governance-ops"),
                },
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    resp, r, err := api.UpdateTeamNotificationRule(ctx, DdTeamDataID, TeamNotificationRuleDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.UpdateTeamNotificationRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TeamsApi.UpdateTeamNotificationRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update team notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamNotificationRule;
import com.datadog.api.client.v2.model.TeamNotificationRuleAttributes;
import com.datadog.api.client.v2.model.TeamNotificationRuleAttributesPagerduty;
import com.datadog.api.client.v2.model.TeamNotificationRuleAttributesSlack;
import com.datadog.api.client.v2.model.TeamNotificationRuleRequest;
import com.datadog.api.client.v2.model.TeamNotificationRuleResponse;
import com.datadog.api.client.v2.model.TeamNotificationRuleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "team_notification_rule" in the system
    String TEAM_NOTIFICATION_RULE_DATA_ID = System.getenv("TEAM_NOTIFICATION_RULE_DATA_ID");

    TeamNotificationRuleRequest body =
        new TeamNotificationRuleRequest()
            .data(
                new TeamNotificationRule()
                    .type(TeamNotificationRuleType.TEAM_NOTIFICATION_RULES)
                    .id(TEAM_NOTIFICATION_RULE_DATA_ID)
                    .attributes(
                        new TeamNotificationRuleAttributes()
                            .pagerduty(
                                new TeamNotificationRuleAttributesPagerduty()
                                    .serviceName("Datadog-prod"))
                            .slack(
                                new TeamNotificationRuleAttributesSlack()
                                    .workspace("Datadog")
                                    .channel("aaa-governance-ops"))));

    try {
      TeamNotificationRuleResponse result =
          apiInstance.updateTeamNotificationRule(
              DD_TEAM_DATA_ID, TEAM_NOTIFICATION_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#updateTeamNotificationRule");
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
Update team notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_notification_rule import TeamNotificationRule
from datadog_api_client.v2.model.team_notification_rule_attributes import TeamNotificationRuleAttributes
from datadog_api_client.v2.model.team_notification_rule_attributes_pagerduty import (
    TeamNotificationRuleAttributesPagerduty,
)
from datadog_api_client.v2.model.team_notification_rule_attributes_slack import TeamNotificationRuleAttributesSlack
from datadog_api_client.v2.model.team_notification_rule_request import TeamNotificationRuleRequest
from datadog_api_client.v2.model.team_notification_rule_type import TeamNotificationRuleType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_notification_rule" in the system
TEAM_NOTIFICATION_RULE_DATA_ID = environ["TEAM_NOTIFICATION_RULE_DATA_ID"]

body = TeamNotificationRuleRequest(
    data=TeamNotificationRule(
        type=TeamNotificationRuleType.TEAM_NOTIFICATION_RULES,
        id=TEAM_NOTIFICATION_RULE_DATA_ID,
        attributes=TeamNotificationRuleAttributes(
            pagerduty=TeamNotificationRuleAttributesPagerduty(
                service_name="Datadog-prod",
            ),
            slack=TeamNotificationRuleAttributesSlack(
                workspace="Datadog",
                channel="aaa-governance-ops",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_notification_rule(
        team_id=DD_TEAM_DATA_ID, rule_id=TEAM_NOTIFICATION_RULE_DATA_ID, body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update team notification rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_notification_rule" in the system
TEAM_NOTIFICATION_RULE_DATA_ID = ENV["TEAM_NOTIFICATION_RULE_DATA_ID"]

body = DatadogAPIClient::V2::TeamNotificationRuleRequest.new({
  data: DatadogAPIClient::V2::TeamNotificationRule.new({
    type: DatadogAPIClient::V2::TeamNotificationRuleType::TEAM_NOTIFICATION_RULES,
    id: TEAM_NOTIFICATION_RULE_DATA_ID,
    attributes: DatadogAPIClient::V2::TeamNotificationRuleAttributes.new({
      pagerduty: DatadogAPIClient::V2::TeamNotificationRuleAttributesPagerduty.new({
        service_name: "Datadog-prod",
      }),
      slack: DatadogAPIClient::V2::TeamNotificationRuleAttributesSlack.new({
        workspace: "Datadog",
        channel: "aaa-governance-ops",
      }),
    }),
  }),
})
p api_instance.update_team_notification_rule(DD_TEAM_DATA_ID, TEAM_NOTIFICATION_RULE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update team notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamNotificationRule;
use datadog_api_client::datadogV2::model::TeamNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::TeamNotificationRuleAttributesPagerduty;
use datadog_api_client::datadogV2::model::TeamNotificationRuleAttributesSlack;
use datadog_api_client::datadogV2::model::TeamNotificationRuleRequest;
use datadog_api_client::datadogV2::model::TeamNotificationRuleType;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "team_notification_rule" in the system
    let team_notification_rule_data_id = std::env::var("TEAM_NOTIFICATION_RULE_DATA_ID").unwrap();
    let body = TeamNotificationRuleRequest::new(
        TeamNotificationRule::new(
            TeamNotificationRuleAttributes::new()
                .pagerduty(
                    TeamNotificationRuleAttributesPagerduty::new()
                        .service_name("Datadog-prod".to_string()),
                )
                .slack(
                    TeamNotificationRuleAttributesSlack::new()
                        .channel("aaa-governance-ops".to_string())
                        .workspace("Datadog".to_string()),
                ),
            TeamNotificationRuleType::TEAM_NOTIFICATION_RULES,
        )
        .id(team_notification_rule_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .update_team_notification_rule(
            dd_team_data_id.clone(),
            team_notification_rule_data_id.clone(),
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
 * Update team notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "team_notification_rule" in the system
const TEAM_NOTIFICATION_RULE_DATA_ID = process.env
  .TEAM_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.TeamsApiUpdateTeamNotificationRuleRequest = {
  body: {
    data: {
      type: "team_notification_rules",
      id: TEAM_NOTIFICATION_RULE_DATA_ID,
      attributes: {
        pagerduty: {
          serviceName: "Datadog-prod",
        },
        slack: {
          workspace: "Datadog",
          channel: "aaa-governance-ops",
        },
      },
    },
  },
  teamId: DD_TEAM_DATA_ID,
  ruleId: TEAM_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .updateTeamNotificationRule(params)
  .then((data: v2.TeamNotificationRuleResponse) => {
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

## Delete team notification rule{% #delete-team-notification-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules/{rule_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules/{rule_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id} |

### Overview

This endpoint requires the `teams_read` permission.

OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.

### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| team_id [*required*] | string | None        |
| rule_id [*required*] | string | None        |

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
API error response.
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
                  \# Path parametersexport team_id="CHANGE_ME"export rule_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules/${rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete team notification rule returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_notification_rule" in the system
TEAM_NOTIFICATION_RULE_DATA_ID = environ["TEAM_NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team_notification_rule(
        team_id=DD_TEAM_DATA_ID,
        rule_id=TEAM_NOTIFICATION_RULE_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete team notification rule returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_notification_rule" in the system
TEAM_NOTIFICATION_RULE_DATA_ID = ENV["TEAM_NOTIFICATION_RULE_DATA_ID"]
api_instance.delete_team_notification_rule(DD_TEAM_DATA_ID, TEAM_NOTIFICATION_RULE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete team notification rule returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "dd_team" in the system
    DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

    // there is a valid "team_notification_rule" in the system
    TeamNotificationRuleDataID := os.Getenv("TEAM_NOTIFICATION_RULE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewTeamsApi(apiClient)
    r, err := api.DeleteTeamNotificationRule(ctx, DdTeamDataID, TeamNotificationRuleDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.DeleteTeamNotificationRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete team notification rule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TeamsApi apiInstance = new TeamsApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "team_notification_rule" in the system
    String TEAM_NOTIFICATION_RULE_DATA_ID = System.getenv("TEAM_NOTIFICATION_RULE_DATA_ID");

    try {
      apiInstance.deleteTeamNotificationRule(DD_TEAM_DATA_ID, TEAM_NOTIFICATION_RULE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#deleteTeamNotificationRule");
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
// Delete team notification rule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "team_notification_rule" in the system
    let team_notification_rule_data_id = std::env::var("TEAM_NOTIFICATION_RULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .delete_team_notification_rule(
            dd_team_data_id.clone(),
            team_notification_rule_data_id.clone(),
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
 * Delete team notification rule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "team_notification_rule" in the system
const TEAM_NOTIFICATION_RULE_DATA_ID = process.env
  .TEAM_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.TeamsApiDeleteTeamNotificationRuleRequest = {
  teamId: DD_TEAM_DATA_ID,
  ruleId: TEAM_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .deleteTeamNotificationRule(params)
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
