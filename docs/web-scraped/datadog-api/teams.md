# Source: https://docs.datadoghq.com/api/latest/teams

# Teams
View and manage teams within Datadog. See the [Teams page](https://docs.datadoghq.com/account_management/teams/) for more information.
## [Get all teams](https://docs.datadoghq.com/api/latest/teams/#get-all-teams)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-all-teams-v2)


GET https://api.ap1.datadoghq.com/api/v2/teamhttps://api.ap2.datadoghq.com/api/v2/teamhttps://api.datadoghq.eu/api/v2/teamhttps://api.ddog-gov.com/api/v2/teamhttps://api.datadoghq.com/api/v2/teamhttps://api.us3.datadoghq.com/api/v2/teamhttps://api.us5.datadoghq.com/api/v2/team
### Overview
Get all teams. Can be used to search for teams using the `filter[keyword]` and `filter[me]` query parameters. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[number]
integer
Specific page number to return.
page[size]
integer
Size for a given page. The maximum allowed value is 100.
sort
enum
Specifies the order of the returned teams  
Allowed enum values: `name, -name, user_count, -user_count`
include
array
Included related resources optionally requested. Allowed enum values: `team_links, user_team_permissions`
filter[keyword]
string
Search query. Can be team name, team handle, or email of team member
filter[me]
boolean
When true, only returns teams the current user belongs to
fields[team]
array
List of fields that need to be fetched.
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#ListTeams-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#ListTeams-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#ListTeams-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Response with multiple teams
Field
Type
Description
data
[object]
Teams response data
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
included
[ <oneOf>]
Resources related to the team
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
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
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
Team link
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
Option 3
object
A user's permissions for a given team
attributes
object
User team permission attributes
permissions
object
Object of team permission actions and boolean values that a logged in user can perform on this team.
id [_required_]
string
The user team permission's identifier
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Teams response links.
first
string
First link.
last
string
Last link.
next
string
Next link.
prev
string
Previous link.
self
string
Current link.
meta
object
Teams response metadata.
pagination
object
Teams response metadata.
first_offset
int64
The first offset.
last_offset
int64
The last offset.
limit
int64
Pagination limit.
next_offset
int64
The next offset.
offset
int64
The offset.
prev_offset
int64
The previous offset.
total
int64
Total results.
type
string
Offset type.
```
{
  "data": [
    {
      "attributes": {
        "avatar": "🥑",
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get all teams
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all teams
```
# Get all teams returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.list_teams()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get all teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get all teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create a team](https://docs.datadoghq.com/api/latest/teams/#create-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#create-a-team-v2)


POST https://api.ap1.datadoghq.com/api/v2/teamhttps://api.ap2.datadoghq.com/api/v2/teamhttps://api.datadoghq.eu/api/v2/teamhttps://api.ddog-gov.com/api/v2/teamhttps://api.datadoghq.com/api/v2/teamhttps://api.us3.datadoghq.com/api/v2/teamhttps://api.us5.datadoghq.com/api/v2/team
### Overview
Create a new team. User IDs passed through the `users` relationship field are added to the team. This endpoint requires all of the following permissions:
* `teams_read`
* `teams_manage`
  

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Team create
attributes [_required_]
object
Team creation attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
name [_required_]
string
The name of the team
visible_modules
[string]
Collection of visible modules for the team
relationships
object
Relationships formed with the team on creation
users
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
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
#####  Create a team returns "CREATED" response
```
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

Copy
#####  Create a team with V2 fields returns "CREATED" response
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/teams/#CreateTeam-201-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#CreateTeam-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/teams/#CreateTeam-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#CreateTeam-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Response with a team
Field
Type
Description
data
object
A team
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
```
{
  "data": {
    "attributes": {
      "avatar": "🥑",
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Create a team returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team" \
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

                        
```

#####  Create a team with V2 fields returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team" \
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

                        
```

#####  Create a team returns "CREATED" response 
```
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

Copy
#####  Create a team with V2 fields returns "CREATED" response 
```
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
				Avatar: *datadog.NewNullableString(datadog.PtrString("🥑")),
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a team returns "CREATED" response 
```
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

Copy
#####  Create a team with V2 fields returns "CREATED" response 
```
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
                            .avatar("🥑")
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create a team returns "CREATED" response 
```
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

Copy
#####  Create a team with V2 fields returns "CREATED" response 
```
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
            avatar="🥑",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a team returns "CREATED" response 
```
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

Copy
#####  Create a team with V2 fields returns "CREATED" response 
```
# Create a team with V2 fields returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::TeamCreateRequest.new({
  data: DatadogAPIClient::V2::TeamCreate.new({
    attributes: DatadogAPIClient::V2::TeamCreateAttributes.new({
      handle: "test-handle-a0fc0297eb519635",
      name: "test-name-a0fc0297eb519635",
      avatar: "🥑",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a team returns "CREATED" response 
```
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

Copy
#####  Create a team with V2 fields returns "CREATED" response 
```
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
        .avatar(Some("🥑".to_string()))
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create a team returns "CREATED" response 
```
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

Copy
#####  Create a team with V2 fields returns "CREATED" response 
```
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
        avatar: "🥑",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a team](https://docs.datadoghq.com/api/latest/teams/#get-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-a-team-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}https://api.datadoghq.eu/api/v2/team/{team_id}https://api.ddog-gov.com/api/v2/team/{team_id}https://api.datadoghq.com/api/v2/team/{team_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}
### Overview
Get a single team using the team’s `id`. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeam-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeam-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeam-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Response with a team
Field
Type
Description
data
object
A team
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
```
{
  "data": {
    "attributes": {
      "avatar": "🥑",
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get a team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a team
```
# Get a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team(DD_TEAM_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update a team](https://docs.datadoghq.com/api/latest/teams/#update-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#update-a-team-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/team/{team_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}https://api.datadoghq.eu/api/v2/team/{team_id}https://api.ddog-gov.com/api/v2/team/{team_id}https://api.datadoghq.com/api/v2/team/{team_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}
### Overview
Update a team using the team’s `id`. If the `team_links` relationship is present, the associated links are updated to be in the order they appear in the array, and any existing team links not present are removed. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Team update request
attributes [_required_]
object
Team update attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
name [_required_]
string
The name of the team
visible_modules
[string]
Collection of visible modules for the team
relationships
object
Team update relationships
team_links
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
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#UpdateTeam-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/teams/#UpdateTeam-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#UpdateTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#UpdateTeam-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/teams/#UpdateTeam-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#UpdateTeam-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Response with a team
Field
Type
Description
data
object
A team
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
```
{
  "data": {
    "attributes": {
      "avatar": "🥑",
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

Copy
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Update a team returns "OK" response
Copy
```
                          # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}" \
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

                        
```

#####  Update a team returns "OK" response
```
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
				Avatar: *datadog.NewNullableString(datadog.PtrString("🥑")),
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a team returns "OK" response
```
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
                            .avatar("🥑")
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update a team returns "OK" response
```
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
            avatar="🥑",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a team returns "OK" response
```
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
      avatar: "🥑",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a team returns "OK" response
```
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
        .avatar(Some("🥑".to_string()))
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update a team returns "OK" response
```
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
        avatar: "🥑",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Remove a team](https://docs.datadoghq.com/api/latest/teams/#remove-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}https://api.datadoghq.eu/api/v2/team/{team_id}https://api.ddog-gov.com/api/v2/team/{team_id}https://api.datadoghq.com/api/v2/team/{team_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}
### Overview
Remove a team using the team’s `id`. This endpoint requires all of the following permissions:
* `teams_read`
* `teams_manage`
  

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#DeleteTeam-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#DeleteTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#DeleteTeam-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#DeleteTeam-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Remove a team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove a team
```
# Remove a team returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
api_instance.delete_team(DD_TEAM_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Remove a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Remove a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Remove a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get team memberships](https://docs.datadoghq.com/api/latest/teams/#get-team-memberships)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-team-memberships-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.ap2.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.datadoghq.eu/api/v2/team/{team_id}/membershipshttps://api.ddog-gov.com/api/v2/team/{team_id}/membershipshttps://api.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.us3.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships
### Overview
Get a paginated list of members for a team This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
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
sort
enum
Specifies the order of returned team memberships  
Allowed enum values: `manager_name, -manager_name, name, -name, handle, -handle, email, -email`
filter[keyword]
string
Search query, can be user email or name
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamMemberships-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamMemberships-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamMemberships-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamMemberships-429-v2)


Represents a user's association to a team
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team memberships response
Field
Type
Description
data
[object]
Team memberships response data
attributes
object
Team membership attributes
provisioned_by
string
The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping.
provisioned_by_id
string
UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.
role
enum
The user's role within the team Allowed enum values: `admin`
id [_required_]
string
The ID of a user's relationship with a team
relationships
object
Relationship between membership and a user
team
object
Relationship between team membership and team
data [_required_]
object
The team associated with the membership
id [_required_]
string
The ID of the team associated with the membership
type [_required_]
enum
User team team type Allowed enum values: `team`
default: `team`
user
object
Relationship between team membership and user
data [_required_]
object
A user's relationship with a team
id [_required_]
string
The ID of the user associated with the team
type [_required_]
enum
User team user type Allowed enum values: `users`
default: `users`
type [_required_]
enum
Team membership type Allowed enum values: `team_memberships`
default: `team_memberships`
included
[ <oneOf>]
Resources related to the team memberships
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
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
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
A team
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
links
object
Teams response links.
first
string
First link.
last
string
Last link.
next
string
Next link.
prev
string
Previous link.
self
string
Current link.
meta
object
Teams response metadata.
pagination
object
Teams response metadata.
first_offset
int64
The first offset.
last_offset
int64
The last offset.
limit
int64
Pagination limit.
next_offset
int64
The next offset.
offset
int64
The offset.
prev_offset
int64
The previous offset.
total
int64
Total results.
type
string
Offset type.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get team memberships
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get team memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get team memberships
```
# Get team memberships returns "Represents a user's association to a team" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team_memberships(DD_TEAM_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get team memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get team memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get team memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get team memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Add a user to a team](https://docs.datadoghq.com/api/latest/teams/#add-a-user-to-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#add-a-user-to-a-team-v2)


POST https://api.ap1.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.ap2.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.datadoghq.eu/api/v2/team/{team_id}/membershipshttps://api.ddog-gov.com/api/v2/team/{team_id}/membershipshttps://api.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.us3.datadoghq.com/api/v2/team/{team_id}/membershipshttps://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships
### Overview
Add a user to a team.
**Note** : Each team has a setting that determines who is allowed to modify membership of the team. The `user_access_manage` permission generally grants access to modify membership of any team. To get the full picture, see [Team Membership documentation](https://docs.datadoghq.com/account_management/teams/manage/#team-membership).
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
A user's relationship with a team
attributes
object
Team membership attributes
provisioned_by
string
The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping.
provisioned_by_id
string
UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.
role
enum
The user's role within the team Allowed enum values: `admin`
relationships
object
Relationship between membership and a user
team
object
Relationship between team membership and team
data [_required_]
object
The team associated with the membership
id [_required_]
string
The ID of the team associated with the membership
type [_required_]
enum
User team team type Allowed enum values: `team`
default: `team`
user
object
Relationship between team membership and user
data [_required_]
object
A user's relationship with a team
id [_required_]
string
The ID of the user associated with the team
type [_required_]
enum
User team user type Allowed enum values: `users`
default: `users`
type [_required_]
enum
Team membership type Allowed enum values: `team_memberships`
default: `team_memberships`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#CreateTeamMembership-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#CreateTeamMembership-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#CreateTeamMembership-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/teams/#CreateTeamMembership-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#CreateTeamMembership-429-v2)


Represents a user's association to a team
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team membership response
Field
Type
Description
data
object
A user's relationship with a team
attributes
object
Team membership attributes
provisioned_by
string
The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping.
provisioned_by_id
string
UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.
role
enum
The user's role within the team Allowed enum values: `admin`
id [_required_]
string
The ID of a user's relationship with a team
relationships
object
Relationship between membership and a user
team
object
Relationship between team membership and team
data [_required_]
object
The team associated with the membership
id [_required_]
string
The ID of the team associated with the membership
type [_required_]
enum
User team team type Allowed enum values: `team`
default: `team`
user
object
Relationship between team membership and user
data [_required_]
object
A user's relationship with a team
id [_required_]
string
The ID of the user associated with the team
type [_required_]
enum
User team user type Allowed enum values: `users`
default: `users`
type [_required_]
enum
Team membership type Allowed enum values: `team_memberships`
default: `team_memberships`
included
[ <oneOf>]
Resources related to the team memberships
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
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
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
A team
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Add a user to a team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships" \
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

                
```

#####  Add a user to a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Add a user to a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Add a user to a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Add a user to a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Add a user to a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Add a user to a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Remove a user from a team](https://docs.datadoghq.com/api/latest/teams/#remove-a-user-from-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#remove-a-user-from-a-team-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.datadoghq.eu/api/v2/team/{team_id}/memberships/{user_id}https://api.ddog-gov.com/api/v2/team/{team_id}/memberships/{user_id}https://api.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}
### Overview
Remove a user from a team.
**Note** : Each team has a setting that determines who is allowed to modify membership of the team. The `user_access_manage` permission generally grants access to modify membership of any team. To get the full picture, see [Team Membership documentation](https://docs.datadoghq.com/account_management/teams/manage/#team-membership).
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
user_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamMembership-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamMembership-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamMembership-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamMembership-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Remove a user from a team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
export user_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships/${user_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove a user from a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove a user from a team
```
# Remove a user from a team returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
api_instance.delete_team_membership(DD_TEAM_DATA_ID, "user_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove a user from a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Remove a user from a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Remove a user from a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Remove a user from a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update a user's membership attributes on a team](https://docs.datadoghq.com/api/latest/teams/#update-a-users-membership-attributes-on-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#update-a-users-membership-attributes-on-a-team-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.datadoghq.eu/api/v2/team/{team_id}/memberships/{user_id}https://api.ddog-gov.com/api/v2/team/{team_id}/memberships/{user_id}https://api.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/memberships/{user_id}
### Overview
Update a user’s membership attributes on a team.
**Note** : Each team has a setting that determines who is allowed to modify membership of the team. The `user_access_manage` permission generally grants access to modify membership of any team. To get the full picture, see [Team Membership documentation](https://docs.datadoghq.com/account_management/teams/manage/#team-membership).
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
user_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
A user's relationship with a team
attributes
object
Team membership attributes
provisioned_by
string
The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping.
provisioned_by_id
string
UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.
role
enum
The user's role within the team Allowed enum values: `admin`
type [_required_]
enum
Team membership type Allowed enum values: `team_memberships`
default: `team_memberships`
```
{
  "data": {
    "attributes": {
      "role": "string"
    },
    "type": "team_memberships"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamMembership-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamMembership-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamMembership-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamMembership-429-v2)


Represents a user's association to a team
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team membership response
Field
Type
Description
data
object
A user's relationship with a team
attributes
object
Team membership attributes
provisioned_by
string
The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping.
provisioned_by_id
string
UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.
role
enum
The user's role within the team Allowed enum values: `admin`
id [_required_]
string
The ID of a user's relationship with a team
relationships
object
Relationship between membership and a user
team
object
Relationship between team membership and team
data [_required_]
object
The team associated with the membership
id [_required_]
string
The ID of the team associated with the membership
type [_required_]
enum
User team team type Allowed enum values: `team`
default: `team`
user
object
Relationship between team membership and user
data [_required_]
object
A user's relationship with a team
id [_required_]
string
The ID of the user associated with the team
type [_required_]
enum
User team user type Allowed enum values: `users`
default: `users`
type [_required_]
enum
Team membership type Allowed enum values: `team_memberships`
default: `team_memberships`
included
[ <oneOf>]
Resources related to the team memberships
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
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
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
A team
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Update a user's membership attributes on a team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
export user_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/memberships/${user_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "team_memberships"
  }
}
EOF  

                
```

#####  Update a user's membership attributes on a team
```
"""
Update a user's membership attributes on a team returns "Represents a user's association to a team" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.user_team_attributes import UserTeamAttributes
from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_type import UserTeamType
from datadog_api_client.v2.model.user_team_update import UserTeamUpdate
from datadog_api_client.v2.model.user_team_update_request import UserTeamUpdateRequest

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
    response = api_instance.update_team_membership(team_id="team_id", user_id="user_id", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a user's membership attributes on a team
```
# Update a user's membership attributes on a team returns "Represents a user's association to a team" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

body = DatadogAPIClient::V2::UserTeamUpdateRequest.new({
  data: DatadogAPIClient::V2::UserTeamUpdate.new({
    attributes: DatadogAPIClient::V2::UserTeamAttributes.new({
      role: DatadogAPIClient::V2::UserTeamRole::ADMIN,
    }),
    type: DatadogAPIClient::V2::UserTeamType::TEAM_MEMBERSHIPS,
  }),
})
p api_instance.update_team_membership("team_id", "user_id", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a user's membership attributes on a team
```
// Update a user's membership attributes on a team returns "Represents a user's association to a team" response

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
	resp, r, err := api.UpdateTeamMembership(ctx, "team_id", "user_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.UpdateTeamMembership`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `TeamsApi.UpdateTeamMembership`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a user's membership attributes on a team
```
// Update a user's membership attributes on a team returns "Represents a user's association to a
// team" response

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

    UserTeamUpdateRequest body =
        new UserTeamUpdateRequest()
            .data(
                new UserTeamUpdate()
                    .attributes(new UserTeamAttributes().role(UserTeamRole.ADMIN))
                    .type(UserTeamType.TEAM_MEMBERSHIPS));

    try {
      UserTeamResponse result = apiInstance.updateTeamMembership("team_id", "user_id", body);
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update a user's membership attributes on a team
```
// Update a user's membership attributes on a team returns "Represents a user's
// association to a team" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::UserTeamAttributes;
use datadog_api_client::datadogV2::model::UserTeamRole;
use datadog_api_client::datadogV2::model::UserTeamType;
use datadog_api_client::datadogV2::model::UserTeamUpdate;
use datadog_api_client::datadogV2::model::UserTeamUpdateRequest;

#[tokio::main]
async fn main() {
    let body = UserTeamUpdateRequest::new(
        UserTeamUpdate::new(UserTeamType::TEAM_MEMBERSHIPS)
            .attributes(UserTeamAttributes::new().role(Some(UserTeamRole::ADMIN))),
    );
    let configuration = datadog::Configuration::new();
    let api = TeamsAPI::with_config(configuration);
    let resp = api
        .update_team_membership("team_id".to_string(), "user_id".to_string(), body)
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

#####  Update a user's membership attributes on a team
```
/**
 * Update a user's membership attributes on a team returns "Represents a user's association to a team" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.TeamsApi(configuration);

const params: v2.TeamsApiUpdateTeamMembershipRequest = {
  body: {
    data: {
      attributes: {
        role: "admin",
      },
      type: "team_memberships",
    },
  },
  teamId: "team_id",
  userId: "user_id",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get links for a team](https://docs.datadoghq.com/api/latest/teams/#get-links-for-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-links-for-a-team-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.ap2.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.datadoghq.eu/api/v2/team/{team_id}/linkshttps://api.ddog-gov.com/api/v2/team/{team_id}/linkshttps://api.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.us3.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.us5.datadoghq.com/api/v2/team/{team_id}/links
### Overview
Get all links for a given team. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamLinks-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamLinks-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamLinks-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamLinks-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team links response
Field
Type
Description
data
[object]
Team links response data
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get links for a team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get links for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get links for a team
```
# Get links for a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team_links(DD_TEAM_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get links for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get links for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get links for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get links for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create a team link](https://docs.datadoghq.com/api/latest/teams/#create-a-team-link)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#create-a-team-link-v2)


POST https://api.ap1.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.ap2.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.datadoghq.eu/api/v2/team/{team_id}/linkshttps://api.ddog-gov.com/api/v2/team/{team_id}/linkshttps://api.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.us3.datadoghq.com/api/v2/team/{team_id}/linkshttps://api.us5.datadoghq.com/api/v2/team/{team_id}/links
### Overview
Add a new link to a team. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Team link create
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#CreateTeamLink-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#CreateTeamLink-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#CreateTeamLink-404-v2)
  * [422](https://docs.datadoghq.com/api/latest/teams/#CreateTeamLink-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#CreateTeamLink-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team link response
Field
Type
Description
data
object
Team link
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Create a team link returns "OK" response
Copy
```
                          # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links" \
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

                        
```

#####  Create a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a team link](https://docs.datadoghq.com/api/latest/teams/#get-a-team-link)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-a-team-link-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.datadoghq.eu/api/v2/team/{team_id}/links/{link_id}https://api.ddog-gov.com/api/v2/team/{team_id}/links/{link_id}https://api.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/links/{link_id}
### Overview
Get a single link for a team. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
link_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamLink-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamLink-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamLink-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamLink-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team link response
Field
Type
Description
data
object
Team link
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get a team link
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
export link_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links/${link_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a team link
```
# Get a team link returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = ENV["TEAM_LINK_DATA_ID"]
p api_instance.get_team_link(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update a team link](https://docs.datadoghq.com/api/latest/teams/#update-a-team-link)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#update-a-team-link-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.datadoghq.eu/api/v2/team/{team_id}/links/{link_id}https://api.ddog-gov.com/api/v2/team/{team_id}/links/{link_id}https://api.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/links/{link_id}
### Overview
Update a team link. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
link_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Team link create
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamLink-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamLink-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamLink-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamLink-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team link response
Field
Type
Description
data
object
Team link
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Update a team link returns "OK" response
Copy
```
                          # Path parameters  
export team_id="CHANGE_ME"  
export link_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links/${link_id}" \
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

                        
```

#####  Update a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update a team link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Remove a team link](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-link)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-link-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.datadoghq.eu/api/v2/team/{team_id}/links/{link_id}https://api.ddog-gov.com/api/v2/team/{team_id}/links/{link_id}https://api.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/links/{link_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/links/{link_id}
### Overview
Remove a link from a team. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
link_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamLink-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamLink-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamLink-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamLink-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Remove a team link
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
export link_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/links/${link_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove a team link
```
# Remove a team link returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = ENV["TEAM_LINK_DATA_ID"]
api_instance.delete_team_link(DD_TEAM_DATA_ID, TEAM_LINK_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Remove a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Remove a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Remove a team link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get permission settings for a team](https://docs.datadoghq.com/api/latest/teams/#get-permission-settings-for-a-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-permission-settings-for-a-team-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/permission-settingshttps://api.ap2.datadoghq.com/api/v2/team/{team_id}/permission-settingshttps://api.datadoghq.eu/api/v2/team/{team_id}/permission-settingshttps://api.ddog-gov.com/api/v2/team/{team_id}/permission-settingshttps://api.datadoghq.com/api/v2/team/{team_id}/permission-settingshttps://api.us3.datadoghq.com/api/v2/team/{team_id}/permission-settingshttps://api.us5.datadoghq.com/api/v2/team/{team_id}/permission-settings
### Overview
Get all permission settings for a given team. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamPermissionSettings-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamPermissionSettings-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamPermissionSettings-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamPermissionSettings-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team permission settings response
Field
Type
Description
data
[object]
Team permission settings response data
attributes
object
Team permission setting attributes
action
enum
The identifier for the action Allowed enum values: `manage_membership,edit`
editable
boolean
Whether or not the permission setting is editable by the current user
options
[string]
Possible values for action
title
string
The team permission name
value
enum
What type of user is allowed to perform the specified action Allowed enum values: `admins,members,organization,user_access_manage,teams_manage`
id [_required_]
string
The team permission setting's identifier
type [_required_]
enum
Team permission setting type Allowed enum values: `team_permission_settings`
default: `team_permission_settings`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get permission settings for a team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/permission-settings" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get permission settings for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get permission settings for a team
```
# Get permission settings for a team returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]
p api_instance.get_team_permission_settings(DD_TEAM_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get permission settings for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get permission settings for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get permission settings for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get permission settings for a team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get team sync configurations](https://docs.datadoghq.com/api/latest/teams/#get-team-sync-configurations)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-team-sync-configurations-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/synchttps://api.ap2.datadoghq.com/api/v2/team/synchttps://api.datadoghq.eu/api/v2/team/synchttps://api.ddog-gov.com/api/v2/team/synchttps://api.datadoghq.com/api/v2/team/synchttps://api.us3.datadoghq.com/api/v2/team/synchttps://api.us5.datadoghq.com/api/v2/team/sync
### Overview
Get all team synchronization configurations. Returns a list of configurations used for linking or provisioning teams with external sources like GitHub. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter[source] [_required_]
enum
Filter by the external source platform for team synchronization  
Allowed enum values: `github`
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamSync-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamSync-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamSync-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamSync-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team sync configurations response.
Field
Type
Description
data
[object]
List of team sync configurations
attributes [_required_]
object
Team sync attributes.
frequency
enum
How often the sync process should be run. Defaults to `once` when not provided. Allowed enum values: `once,continuously,paused`
source [_required_]
enum
The external source platform for team synchronization. Only "github" is supported. Allowed enum values: `github`
sync_membership
boolean
Whether to sync members from the external team to the Datadog team. Defaults to `false` when not provided.
type [_required_]
enum
The type of synchronization operation. "link" connects teams by matching names. "provision" creates new teams when no match is found. Allowed enum values: `link,provision`
id
string
The sync's identifier
type [_required_]
enum
Team sync bulk type. Allowed enum values: `team_sync_bulk`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
Team sync configurations not found
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get team sync configurations
Copy
```
                  # Required query arguments  
export filter[source]="github"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/sync?filter[source]=${filter[source]}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get team sync configurations
```
"""
Get team sync configurations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource

configuration = Configuration()
configuration.unstable_operations["get_team_sync"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_sync(
        filter_source=TeamSyncAttributesSource.GITHUB,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get team sync configurations
```
# Get team sync configurations returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_team_sync".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.get_team_sync(TeamSyncAttributesSource::GITHUB)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get team sync configurations
```
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
	configuration.SetUnstableOperationEnabled("v2.GetTeamSync", true)
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get team sync configurations
```
// Get team sync configurations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamSyncAttributesSource;
import com.datadog.api.client.v2.model.TeamSyncResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getTeamSync", true);
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get team sync configurations
```
// Get team sync configurations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;
use datadog_api_client::datadogV2::model::TeamSyncAttributesSource;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetTeamSync", true);
    let api = TeamsAPI::with_config(configuration);
    let resp = api.get_team_sync(TeamSyncAttributesSource::GITHUB).await;
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

#####  Get team sync configurations
```
/**
 * Get team sync configurations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getTeamSync"] = true;
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update permission setting for team](https://docs.datadoghq.com/api/latest/teams/#update-permission-setting-for-team)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#update-permission-setting-for-team-v2)


PUT https://api.ap1.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action}https://api.datadoghq.eu/api/v2/team/{team_id}/permission-settings/{action}https://api.ddog-gov.com/api/v2/team/{team_id}/permission-settings/{action}https://api.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action}https://api.us3.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action}https://api.us5.datadoghq.com/api/v2/team/{team_id}/permission-settings/{action}
### Overview
Update a team permission setting for a given team. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
action [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Team permission setting update
attributes
object
Team permission setting update attributes
value
enum
What type of user is allowed to perform the specified action Allowed enum values: `admins,members,organization,user_access_manage,teams_manage`
type [_required_]
enum
Team permission setting type Allowed enum values: `team_permission_settings`
default: `team_permission_settings`
```
{
  "data": {
    "attributes": {
      "value": "admins"
    },
    "type": "team_permission_settings"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamPermissionSetting-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamPermissionSetting-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamPermissionSetting-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamPermissionSetting-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team permission setting response
Field
Type
Description
data
object
Team permission setting
attributes
object
Team permission setting attributes
action
enum
The identifier for the action Allowed enum values: `manage_membership,edit`
editable
boolean
Whether or not the permission setting is editable by the current user
options
[string]
Possible values for action
title
string
The team permission name
value
enum
What type of user is allowed to perform the specified action Allowed enum values: `admins,members,organization,user_access_manage,teams_manage`
id [_required_]
string
The team permission setting's identifier
type [_required_]
enum
Team permission setting type Allowed enum values: `team_permission_settings`
default: `team_permission_settings`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Update permission setting for team returns "OK" response
Copy
```
                          # Path parameters  
export team_id="CHANGE_ME"  
export action="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/permission-settings/${action}" \
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

                        
```

#####  Update permission setting for team returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update permission setting for team returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update permission setting for team returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update permission setting for team returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update permission setting for team returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update permission setting for team returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get user memberships](https://docs.datadoghq.com/api/latest/teams/#get-user-memberships)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-user-memberships-v2)


GET https://api.ap1.datadoghq.com/api/v2/users/{user_uuid}/membershipshttps://api.ap2.datadoghq.com/api/v2/users/{user_uuid}/membershipshttps://api.datadoghq.eu/api/v2/users/{user_uuid}/membershipshttps://api.ddog-gov.com/api/v2/users/{user_uuid}/membershipshttps://api.datadoghq.com/api/v2/users/{user_uuid}/membershipshttps://api.us3.datadoghq.com/api/v2/users/{user_uuid}/membershipshttps://api.us5.datadoghq.com/api/v2/users/{user_uuid}/memberships
### Overview
Get a list of memberships for a user This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
user_uuid [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetUserMemberships-200-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetUserMemberships-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetUserMemberships-429-v2)


Represents a user's association to a team
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team memberships response
Field
Type
Description
data
[object]
Team memberships response data
attributes
object
Team membership attributes
provisioned_by
string
The mechanism responsible for provisioning the team relationship. Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping.
provisioned_by_id
string
UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.
role
enum
The user's role within the team Allowed enum values: `admin`
id [_required_]
string
The ID of a user's relationship with a team
relationships
object
Relationship between membership and a user
team
object
Relationship between team membership and team
data [_required_]
object
The team associated with the membership
id [_required_]
string
The ID of the team associated with the membership
type [_required_]
enum
User team team type Allowed enum values: `team`
default: `team`
user
object
Relationship between team membership and user
data [_required_]
object
A user's relationship with a team
id [_required_]
string
The ID of the user associated with the team
type [_required_]
enum
User team user type Allowed enum values: `users`
default: `users`
type [_required_]
enum
Team membership type Allowed enum values: `team_memberships`
default: `team_memberships`
included
[ <oneOf>]
Resources related to the team memberships
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
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
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
A team
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
links
object
Teams response links.
first
string
First link.
last
string
Last link.
next
string
Next link.
prev
string
Previous link.
self
string
Current link.
meta
object
Teams response metadata.
pagination
object
Teams response metadata.
first_offset
int64
The first offset.
last_offset
int64
The last offset.
limit
int64
Pagination limit.
next_offset
int64
The next offset.
offset
int64
The offset.
prev_offset
int64
The previous offset.
total
int64
Total results.
type
string
Offset type.
```
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

Copy
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get user memberships
Copy
```
                  # Path parameters  
export user_uuid="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_uuid}/memberships" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get user memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get user memberships
```
# Get user memberships returns "Represents a user's association to a team" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.get_user_memberships(USER_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get user memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get user memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get user memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get user memberships
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Link Teams with GitHub Teams](https://docs.datadoghq.com/api/latest/teams/#link-teams-with-github-teams)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#link-teams-with-github-teams-v2)


POST https://api.ap1.datadoghq.com/api/v2/team/synchttps://api.ap2.datadoghq.com/api/v2/team/synchttps://api.datadoghq.eu/api/v2/team/synchttps://api.ddog-gov.com/api/v2/team/synchttps://api.datadoghq.com/api/v2/team/synchttps://api.us3.datadoghq.com/api/v2/team/synchttps://api.us5.datadoghq.com/api/v2/team/sync
### Overview
This endpoint attempts to link your existing Datadog teams with GitHub teams by matching their names. It evaluates all current Datadog teams and compares them against teams in the GitHub organization connected to your Datadog account, based on Datadog Team handle and GitHub Team slug (lowercased and kebab-cased).
This operation is read-only on the GitHub side, no teams will be modified or created.
[A GitHub organization must be connected to your Datadog account](https://docs.datadoghq.com/integrations/github/), and the GitHub App integrated with Datadog must have the `Members Read` permission. Matching is performed by comparing the Datadog team handle to the GitHub team slug using a normalized exact match; case is ignored and spaces are removed. No modifications are made to teams in GitHub. This only creates new teams in Datadog when type is set to `provision`.
This endpoint requires the `teams_manage` permission.
OAuth apps require the `teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
A configuration governing syncing between Datadog teams and teams from an external system.
attributes [_required_]
object
Team sync attributes.
frequency
enum
How often the sync process should be run. Defaults to `once` when not provided. Allowed enum values: `once,continuously,paused`
source [_required_]
enum
The external source platform for team synchronization. Only "github" is supported. Allowed enum values: `github`
sync_membership
boolean
Whether to sync members from the external team to the Datadog team. Defaults to `false` when not provided.
type [_required_]
enum
The type of synchronization operation. "link" connects teams by matching names. "provision" creates new teams when no match is found. Allowed enum values: `link,provision`
id
string
The sync's identifier
type [_required_]
enum
Team sync bulk type. Allowed enum values: `team_sync_bulk`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#SyncTeams-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#SyncTeams-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#SyncTeams-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/teams/#SyncTeams-500-v2)


OK
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
Internal Server Error - Unexpected error during linking.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Sync teams returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/sync" \
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

                        
```

#####  Sync teams returns "OK" response
```
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
	configuration.SetUnstableOperationEnabled("v2.SyncTeams", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewTeamsApi(apiClient)
	r, err := api.SyncTeams(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.SyncTeams`: %v\n", err)
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

#####  Sync teams returns "OK" response
```
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
    defaultClient.setUnstableOperationEnabled("v2.syncTeams", true);
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Sync teams returns "OK" response
```
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
configuration.unstable_operations["sync_teams"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.sync_teams(body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Sync teams returns "OK" response
```
# Sync teams returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.sync_teams".to_sym] = true
end
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Sync teams returns "OK" response
```
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
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.SyncTeams", true);
    let api = TeamsAPI::with_config(configuration);
    let resp = api.sync_teams(body).await;
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

#####  Sync teams returns "OK" response
```
/**
 * Sync teams returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.syncTeams"] = true;
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Add a member team](https://docs.datadoghq.com/api/latest/teams/#add-a-member-team)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/teams/#add-a-member-team-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.ap2.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.datadoghq.eu/api/v2/team/{super_team_id}/member_teamshttps://api.ddog-gov.com/api/v2/team/{super_team_id}/member_teamshttps://api.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.us3.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.us5.datadoghq.com/api/v2/team/{super_team_id}/member_teams
### Overview
Add a member team. Adds the team given by the `id` in the body as a member team of the super team.
**Note** : This API is deprecated. For creating team hierarchy links, use the team hierarchy links API: `POST /api/v2/team-hierarchy-links`.
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
super_team_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
A member team
id [_required_]
string
The member team's identifier
type [_required_]
enum
Member team type Allowed enum values: `member_teams`
default: `member_teams`
```
{
  "data": {
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "member_teams"
  }
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#AddMemberTeam-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#AddMemberTeam-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/teams/#AddMemberTeam-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#AddMemberTeam-429-v2)


Added
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Add a member team
Copy
```
                  # Path parameters  
export super_team_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${super_team_id}/member_teams" \
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

                
```

#####  Add a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Add a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Add a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Add a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Add a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Add a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get team hierarchy links](https://docs.datadoghq.com/api/latest/teams/#get-team-hierarchy-links)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-team-hierarchy-links-v2)


GET https://api.ap1.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.ap2.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.datadoghq.eu/api/v2/team-hierarchy-linkshttps://api.ddog-gov.com/api/v2/team-hierarchy-linkshttps://api.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.us3.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.us5.datadoghq.com/api/v2/team-hierarchy-links
### Overview
List all team hierarchy links that match the provided filters. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[number]
integer
Specific page number to return.
page[size]
integer
Size for a given page. The maximum allowed value is 100.
filter[parent_team]
string
Filter by parent team ID
filter[sub_team]
string
Filter by sub team ID
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#ListTeamHierarchyLinks-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#ListTeamHierarchyLinks-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#ListTeamHierarchyLinks-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team hierarchy links response
Field
Type
Description
data
[object]
Team hierarchy links response data
attributes [_required_]
object
Team hierarchy link attributes
created_at [_required_]
date-time
Timestamp when the team hierarchy link was created
provisioned_by [_required_]
string
The provisioner of the team hierarchy link
id [_required_]
string
The team hierarchy link's identifier
relationships
object
Team hierarchy link relationships
parent_team [_required_]
object
Team hierarchy link team relationship
data [_required_]
object
Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
sub_team [_required_]
object
Team hierarchy link team relationship
data [_required_]
object
Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
Team hierarchy link type Allowed enum values: `team_hierarchy_links`
default: `team_hierarchy_links`
included
[object]
Included teams
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
links
object
When querying team hierarchy links, a set of links for navigation between different pages is included
first
string
Link to the first page.
last
string
Link to the last page.
next
string
Link to the next page.
prev
string
Link to the previous page.
self
string
Link to the current object.
meta
object
Metadata that is included in the response when querying the team hierarchy links
page
object
Metadata related to paging information that is included in the response when querying the team hierarchy links
first_number
int64
First page number.
last_number
int64
Last page number.
next_number
int64
Next page number.
number
int64
Page number.
prev_number
int64
Previous page number.
size
int64
Page size.
total
int64
Total number of results.
type
string
Pagination type.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get team hierarchy links
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get team hierarchy links
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get team hierarchy links
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get team hierarchy links
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get team hierarchy links
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get team hierarchy links
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get team hierarchy links
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#get-a-team-hierarchy-link)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-a-team-hierarchy-link-v2)


GET https://api.ap1.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.ap2.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.datadoghq.eu/api/v2/team-hierarchy-links/{link_id}https://api.ddog-gov.com/api/v2/team-hierarchy-links/{link_id}https://api.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.us3.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/{link_id}
### Overview
Get a single team hierarchy link for the given link_id. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
link_id [_required_]
string
The team hierarchy link’s identifier
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamHierarchyLink-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamHierarchyLink-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamHierarchyLink-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamHierarchyLink-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team hierarchy link response
Field
Type
Description
data
object
Team hierarchy link
attributes [_required_]
object
Team hierarchy link attributes
created_at [_required_]
date-time
Timestamp when the team hierarchy link was created
provisioned_by [_required_]
string
The provisioner of the team hierarchy link
id [_required_]
string
The team hierarchy link's identifier
relationships
object
Team hierarchy link relationships
parent_team [_required_]
object
Team hierarchy link team relationship
data [_required_]
object
Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
sub_team [_required_]
object
Team hierarchy link team relationship
data [_required_]
object
Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
Team hierarchy link type Allowed enum values: `team_hierarchy_links`
default: `team_hierarchy_links`
included
[object]
Included teams
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
links
object
When querying team hierarchy links, a set of links for navigation between different pages is included
first
string
Link to the first page.
last
string
Link to the last page.
next
string
Link to the next page.
prev
string
Link to the previous page.
self
string
Link to the current object.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get a team hierarchy link
Copy
```
                  # Path parameters  
export link_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/${link_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a team hierarchy link
```
# Get a team hierarchy link returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_ID = ENV["TEAM_HIERARCHY_LINK_DATA_ID"]
p api_instance.get_team_hierarchy_link(TEAM_HIERARCHY_LINK_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get all member teams](https://docs.datadoghq.com/api/latest/teams/#get-all-member-teams)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/teams/#get-all-member-teams-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.ap2.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.datadoghq.eu/api/v2/team/{super_team_id}/member_teamshttps://api.ddog-gov.com/api/v2/team/{super_team_id}/member_teamshttps://api.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.us3.datadoghq.com/api/v2/team/{super_team_id}/member_teamshttps://api.us5.datadoghq.com/api/v2/team/{super_team_id}/member_teams
### Overview
Get all member teams.
**Note** : This API is deprecated. For team hierarchy relationships (parent-child teams), use the team hierarchy links API: `GET /api/v2/team-hierarchy-links`.
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
super_team_id [_required_]
string
None
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
fields[team]
array
List of fields that need to be fetched.
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#ListMemberTeams-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#ListMemberTeams-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#ListMemberTeams-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#ListMemberTeams-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Response with multiple teams
Field
Type
Description
data
[object]
Teams response data
attributes [_required_]
object
Team attributes
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
created_at
date-time
Creation date of the team
description
string
Free-form markdown description/content for the team's homepage
handle [_required_]
string
The team's identifier
hidden_modules
[string]
Collection of hidden modules for the team
is_managed
boolean
Whether the team is managed from an external source
link_count
int32
The number of links belonging to the team
modified_at
date-time
Modification date of the team
name [_required_]
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
visible_modules
[string]
Collection of visible modules for the team
id [_required_]
string
The team's identifier
relationships
object
Resources related to a team
team_links
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
user_team_permissions
object
Relationship between a user team permission and a team
data
object
Related user team permission data
id [_required_]
string
The ID of the user team permission
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Links attributes.
related
string
Related link.
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
included
[ <oneOf>]
Resources related to the team
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
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
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
Team link
attributes [_required_]
object
Team link attributes
label [_required_]
string
The link's label
position
int32
The link's position, used to sort links for the team
team_id
string
ID of the team the link is associated with
url [_required_]
string
The URL for the link
id [_required_]
string
The team link's identifier
type [_required_]
enum
Team link type Allowed enum values: `team_links`
default: `team_links`
Option 3
object
A user's permissions for a given team
attributes
object
User team permission attributes
permissions
object
Object of team permission actions and boolean values that a logged in user can perform on this team.
id [_required_]
string
The user team permission's identifier
type [_required_]
enum
User team permission type Allowed enum values: `user_team_permissions`
default: `user_team_permissions`
links
object
Teams response links.
first
string
First link.
last
string
Last link.
next
string
Next link.
prev
string
Previous link.
self
string
Current link.
meta
object
Teams response metadata.
pagination
object
Teams response metadata.
first_offset
int64
The first offset.
last_offset
int64
The last offset.
limit
int64
Pagination limit.
next_offset
int64
The next offset.
offset
int64
The offset.
prev_offset
int64
The previous offset.
total
int64
Total results.
type
string
Offset type.
```
{
  "data": [
    {
      "attributes": {
        "avatar": "🥑",
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Get all member teams
Copy
```
                  # Path parameters  
export super_team_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${super_team_id}/member_teams" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all member teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all member teams
```
# Get all member teams returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_member_teams".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.list_member_teams("super_team_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all member teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all member teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get all member teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get all member teams
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#create-a-team-hierarchy-link)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#create-a-team-hierarchy-link-v2)


POST https://api.ap1.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.ap2.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.datadoghq.eu/api/v2/team-hierarchy-linkshttps://api.ddog-gov.com/api/v2/team-hierarchy-linkshttps://api.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.us3.datadoghq.com/api/v2/team-hierarchy-linkshttps://api.us5.datadoghq.com/api/v2/team-hierarchy-links
### Overview
Create a new team hierarchy link between a parent team and a sub team. This endpoint requires all of the following permissions:
* `teams_read`
* `teams_manage`
  

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Data provided when creating a team hierarchy link
relationships [_required_]
object
The related teams that will be connected by the team hierarchy link
parent_team [_required_]
object
Data about each team that will be connected by the team hierarchy link
data [_required_]
object
This schema defines the attributes about each team that has to be provided when creating a team hierarchy link
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
sub_team [_required_]
object
Data about each team that will be connected by the team hierarchy link
data [_required_]
object
This schema defines the attributes about each team that has to be provided when creating a team hierarchy link
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
Team hierarchy link type Allowed enum values: `team_hierarchy_links`
default: `team_hierarchy_links`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#AddTeamHierarchyLink-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#AddTeamHierarchyLink-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/teams/#AddTeamHierarchyLink-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#AddTeamHierarchyLink-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team hierarchy link response
Field
Type
Description
data
object
Team hierarchy link
attributes [_required_]
object
Team hierarchy link attributes
created_at [_required_]
date-time
Timestamp when the team hierarchy link was created
provisioned_by [_required_]
string
The provisioner of the team hierarchy link
id [_required_]
string
The team hierarchy link's identifier
relationships
object
Team hierarchy link relationships
parent_team [_required_]
object
Team hierarchy link team relationship
data [_required_]
object
Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
sub_team [_required_]
object
Team hierarchy link team relationship
data [_required_]
object
Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
Team hierarchy link type Allowed enum values: `team_hierarchy_links`
default: `team_hierarchy_links`
included
[object]
Included teams
attributes
object
Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
avatar
string
The team's avatar
banner
int64
The team's banner
handle [_required_]
string
The team's handle
is_managed
boolean
Whether the team is managed
is_open_membership
boolean
Whether the team has open membership
link_count
int64
The number of links for the team
name [_required_]
string
The team's name
summary
string
The team's summary
user_count
int64
The number of users in the team
id [_required_]
string
The team's identifier
type [_required_]
enum
Team type Allowed enum values: `team`
default: `team`
links
object
When querying team hierarchy links, a set of links for navigation between different pages is included
first
string
Link to the first page.
last
string
Link to the last page.
next
string
Link to the next page.
prev
string
Link to the previous page.
self
string
Link to the current object.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Create a team hierarchy link returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links" \
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

                        
```

#####  Create a team hierarchy link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a team hierarchy link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create a team hierarchy link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a team hierarchy link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a team hierarchy link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create a team hierarchy link returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Remove a member team](https://docs.datadoghq.com/api/latest/teams/#remove-a-member-team)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/teams/#remove-a-member-team-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}https://api.ap2.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}https://api.datadoghq.eu/api/v2/team/{super_team_id}/member_teams/{member_team_id}https://api.ddog-gov.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}https://api.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}https://api.us3.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}https://api.us5.datadoghq.com/api/v2/team/{super_team_id}/member_teams/{member_team_id}
### Overview
Remove a super team’s member team identified by `member_team_id`.
**Note** : This API is deprecated. For deleting team hierarchy links, use the team hierarchy links API: `DELETE /api/v2/team-hierarchy-links/{link_id}`.
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
super_team_id [_required_]
string
None
member_team_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#RemoveMemberTeam-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#RemoveMemberTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#RemoveMemberTeam-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#RemoveMemberTeam-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Remove a member team
Copy
```
                  # Path parameters  
export super_team_id="CHANGE_ME"  
export member_team_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${super_team_id}/member_teams/${member_team_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove a member team
```
# Remove a member team returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.remove_member_team".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new
api_instance.remove_member_team("super_team_id", "member_team_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Remove a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Remove a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Remove a member team
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Remove a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-hierarchy-link)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-hierarchy-link-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.ap2.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.datadoghq.eu/api/v2/team-hierarchy-links/{link_id}https://api.ddog-gov.com/api/v2/team-hierarchy-links/{link_id}https://api.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.us3.datadoghq.com/api/v2/team-hierarchy-links/{link_id}https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/{link_id}
### Overview
Remove a team hierarchy link by the given link_id. This endpoint requires all of the following permissions:
* `teams_read`
* `teams_manage`
  

OAuth apps require the `teams_read, teams_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
link_id [_required_]
string
The team hierarchy link’s identifier
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#RemoveTeamHierarchyLink-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#RemoveTeamHierarchyLink-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#RemoveTeamHierarchyLink-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#RemoveTeamHierarchyLink-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Remove a team hierarchy link
Copy
```
                  # Path parameters  
export link_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team-hierarchy-links/${link_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove a team hierarchy link
```
# Remove a team hierarchy link returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::TeamsAPI.new

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_ID = ENV["TEAM_HIERARCHY_LINK_DATA_ID"]
api_instance.remove_team_hierarchy_link(TEAM_HIERARCHY_LINK_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Remove a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Remove a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Remove a team hierarchy link
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List team connections](https://docs.datadoghq.com/api/latest/teams/#list-team-connections)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#list-team-connections-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/connectionshttps://api.ap2.datadoghq.com/api/v2/team/connectionshttps://api.datadoghq.eu/api/v2/team/connectionshttps://api.ddog-gov.com/api/v2/team/connectionshttps://api.datadoghq.com/api/v2/team/connectionshttps://api.us3.datadoghq.com/api/v2/team/connectionshttps://api.us5.datadoghq.com/api/v2/team/connections
### Overview
Returns all team connections. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
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
filter[sources]
array
Filter team connections by external source systems.
filter[team_ids]
array
Filter team connections by Datadog team IDs.
filter[connected_team_ids]
array
Filter team connections by connected team IDs from external systems.
filter[connection_ids]
array
Filter team connections by connection IDs.
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#ListTeamConnections-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/teams/#ListTeamConnections-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#ListTeamConnections-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#ListTeamConnections-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Response containing information about multiple team connections.
Field
Type
Description
data
[object]
Array of team connections.
attributes
object
Attributes of the team connection.
managed_by
string
The entity that manages this team connection.
source
string
The name of the external source.
id [_required_]
string
The unique identifier of the team connection.
relationships
object
Relationships of the team connection.
connected_team
object
Reference to a team from an external system.
data
object
Reference to connected external team.
id [_required_]
string
The connected team ID as it is referenced throughout the Datadog ecosystem.
type [_required_]
enum
External team resource type. Allowed enum values: `github_team`
default: `github_team`
team
object
Reference to a Datadog team.
data
object
Reference to a Datadog team.
id [_required_]
string
The Datadog team ID.
type [_required_]
enum
Datadog team resource type. Allowed enum values: `team`
default: `team`
type [_required_]
enum
Team connection resource type. Allowed enum values: `team_connection`
default: `team_connection`
meta
object
Connections response metadata.
page
object
Page-based pagination metadata.
first_number
int64
The first page number.
last_number
int64
The last page number.
next_number
int64
The next page number.
number
int64
The current page number.
prev_number
int64
The previous page number.
size
int64
The page size.
total
int64
Total connections matching request.
type
string
Pagination type.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  List team connections
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/connections" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List team connections
```
"""
List team connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.unstable_operations["list_team_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_team_connections()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List team connections
```
# List team connections returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_team_connections".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TeamsAPI.new
p api_instance.list_team_connections()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List team connections
```
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
	configuration.SetUnstableOperationEnabled("v2.ListTeamConnections", true)
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List team connections
```
// List team connections returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TeamsApi;
import com.datadog.api.client.v2.model.TeamConnectionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listTeamConnections", true);
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List team connections
```
// List team connections returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_teams::ListTeamConnectionsOptionalParams;
use datadog_api_client::datadogV2::api_teams::TeamsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListTeamConnections", true);
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List team connections
```
/**
 * List team connections returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listTeamConnections"] = true;
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create team connections](https://docs.datadoghq.com/api/latest/teams/#create-team-connections)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#create-team-connections-v2)


POST https://api.ap1.datadoghq.com/api/v2/team/connectionshttps://api.ap2.datadoghq.com/api/v2/team/connectionshttps://api.datadoghq.eu/api/v2/team/connectionshttps://api.ddog-gov.com/api/v2/team/connectionshttps://api.datadoghq.com/api/v2/team/connectionshttps://api.us3.datadoghq.com/api/v2/team/connectionshttps://api.us5.datadoghq.com/api/v2/team/connections
### Overview
Create multiple team connections. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
[object]
Array of team connections to create.
attributes
object
Attributes of the team connection.
managed_by
string
The entity that manages this team connection.
source
string
The name of the external source.
relationships
object
Relationships of the team connection.
connected_team
object
Reference to a team from an external system.
data
object
Reference to connected external team.
id [_required_]
string
The connected team ID as it is referenced throughout the Datadog ecosystem.
type [_required_]
enum
External team resource type. Allowed enum values: `github_team`
default: `github_team`
team
object
Reference to a Datadog team.
data
object
Reference to a Datadog team.
id [_required_]
string
The Datadog team ID.
type [_required_]
enum
Datadog team resource type. Allowed enum values: `team`
default: `team`
type [_required_]
enum
Team connection resource type. Allowed enum values: `team_connection`
default: `team_connection`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/teams/#CreateTeamConnections-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/teams/#CreateTeamConnections-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#CreateTeamConnections-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/teams/#CreateTeamConnections-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#CreateTeamConnections-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Response containing information about multiple team connections.
Field
Type
Description
data
[object]
Array of team connections.
attributes
object
Attributes of the team connection.
managed_by
string
The entity that manages this team connection.
source
string
The name of the external source.
id [_required_]
string
The unique identifier of the team connection.
relationships
object
Relationships of the team connection.
connected_team
object
Reference to a team from an external system.
data
object
Reference to connected external team.
id [_required_]
string
The connected team ID as it is referenced throughout the Datadog ecosystem.
type [_required_]
enum
External team resource type. Allowed enum values: `github_team`
default: `github_team`
team
object
Reference to a Datadog team.
data
object
Reference to a Datadog team.
id [_required_]
string
The Datadog team ID.
type [_required_]
enum
Datadog team resource type. Allowed enum values: `team`
default: `team`
type [_required_]
enum
Team connection resource type. Allowed enum values: `team_connection`
default: `team_connection`
meta
object
Connections response metadata.
page
object
Page-based pagination metadata.
first_number
int64
The first page number.
last_number
int64
The last page number.
next_number
int64
The next page number.
number
int64
The current page number.
prev_number
int64
The previous page number.
size
int64
The page size.
total
int64
Total connections matching request.
type
string
Pagination type.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Create team connections
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/connections" \
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

                
```

#####  Create team connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create team connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create team connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create team connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create team connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create team connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete team connections](https://docs.datadoghq.com/api/latest/teams/#delete-team-connections)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#delete-team-connections-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/team/connectionshttps://api.ap2.datadoghq.com/api/v2/team/connectionshttps://api.datadoghq.eu/api/v2/team/connectionshttps://api.ddog-gov.com/api/v2/team/connectionshttps://api.datadoghq.com/api/v2/team/connectionshttps://api.us3.datadoghq.com/api/v2/team/connectionshttps://api.us5.datadoghq.com/api/v2/team/connections
### Overview
Delete multiple team connections. This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
[object]
Array of team connection IDs to delete.
id [_required_]
string
The unique identifier of the team connection to delete.
type [_required_]
enum
Team connection resource type. Allowed enum values: `team_connection`
default: `team_connection`
```
{
  "data": [
    {
      "id": "12345678-1234-5678-9abc-123456789012",
      "type": "team_connection"
    }
  ]
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamConnections-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamConnections-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamConnections-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamConnections-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamConnections-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/teams/?code-lang=typescript)


#####  Delete team connections
Copy
```
                  # Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/connections" \
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

                
```

#####  Delete team connections
```
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
configuration.unstable_operations["delete_team_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team_connections(body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete team connections
```
# Delete team connections returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_team_connections".to_sym] = true
end
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete team connections
```
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
	configuration.SetUnstableOperationEnabled("v2.DeleteTeamConnections", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewTeamsApi(apiClient)
	r, err := api.DeleteTeamConnections(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsApi.DeleteTeamConnections`: %v\n", err)
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

#####  Delete team connections
```
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
    defaultClient.setUnstableOperationEnabled("v2.deleteTeamConnections", true);
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete team connections
```
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
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteTeamConnections", true);
    let api = TeamsAPI::with_config(configuration);
    let resp = api.delete_team_connections(body).await;
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

#####  Delete team connections
```
/**
 * Delete team connections returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteTeamConnections"] = true;
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get team notification rules](https://docs.datadoghq.com/api/latest/teams/#get-team-notification-rules)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-team-notification-rules-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.datadoghq.eu/api/v2/team/{team_id}/notification-ruleshttps://api.ddog-gov.com/api/v2/team/{team_id}/notification-ruleshttps://api.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules
### Overview
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRules-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRules-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRules-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRules-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team notification rules response
Field
Type
Description
data
[object]
Team notification rules response data
attributes [_required_]
object
Team notification rule attributes
email
object
Email notification settings for the team
enabled
boolean
Flag indicating email notification
ms_teams
object
MS Teams notification settings for the team
connector_name
string
Handle for MS Teams
pagerduty
object
PagerDuty notification settings for the team
service_name
string
Service name for PagerDuty
slack
object
Slack notification settings for the team
channel
string
Channel for Slack notification
workspace
string
Workspace for Slack notification
id
string
The identifier of the team notification rule
type [_required_]
enum
Team notification rule type Allowed enum values: `team_notification_rules`
default: `team_notification_rules`
meta
object
Metadata that is included in the response when querying the team notification rules
page
object
Metadata related to paging information that is included in the response when querying the team notification rules
first_offset
int64
The first offset.
last_offset
int64
The last offset.
limit
int64
Pagination limit.
next_offset
int64
The next offset.
offset
int64
The offset.
prev_offset
int64
The previous offset.
total
int64
Total results.
type
string
Offset type.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)


#####  Get team notification rules
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Create team notification rule](https://docs.datadoghq.com/api/latest/teams/#create-team-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#create-team-notification-rule-v2)


POST https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.datadoghq.eu/api/v2/team/{team_id}/notification-ruleshttps://api.ddog-gov.com/api/v2/team/{team_id}/notification-ruleshttps://api.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-ruleshttps://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules
### Overview
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Team notification rule
attributes [_required_]
object
Team notification rule attributes
email
object
Email notification settings for the team
enabled
boolean
Flag indicating email notification
ms_teams
object
MS Teams notification settings for the team
connector_name
string
Handle for MS Teams
pagerduty
object
PagerDuty notification settings for the team
service_name
string
Service name for PagerDuty
slack
object
Slack notification settings for the team
channel
string
Channel for Slack notification
workspace
string
Workspace for Slack notification
id
string
The identifier of the team notification rule
type [_required_]
enum
Team notification rule type Allowed enum values: `team_notification_rules`
default: `team_notification_rules`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/teams/#CreateTeamNotificationRule-201-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#CreateTeamNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#CreateTeamNotificationRule-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/teams/#CreateTeamNotificationRule-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#CreateTeamNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team notification rule response
Field
Type
Description
data
object
Team notification rule
attributes [_required_]
object
Team notification rule attributes
email
object
Email notification settings for the team
enabled
boolean
Flag indicating email notification
ms_teams
object
MS Teams notification settings for the team
connector_name
string
Handle for MS Teams
pagerduty
object
PagerDuty notification settings for the team
service_name
string
Service name for PagerDuty
slack
object
Slack notification settings for the team
channel
string
Channel for Slack notification
workspace
string
Workspace for Slack notification
id
string
The identifier of the team notification rule
type [_required_]
enum
Team notification rule type Allowed enum values: `team_notification_rules`
default: `team_notification_rules`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)


#####  Create team notification rule returns "OK" response
Copy
```
                          # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules" \
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

                        
```

* * *
## [Get team notification rule](https://docs.datadoghq.com/api/latest/teams/#get-team-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#get-team-notification-rule-v2)


GET https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}
### Overview
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
rule_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRule-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#GetTeamNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team notification rule response
Field
Type
Description
data
object
Team notification rule
attributes [_required_]
object
Team notification rule attributes
email
object
Email notification settings for the team
enabled
boolean
Flag indicating email notification
ms_teams
object
MS Teams notification settings for the team
connector_name
string
Handle for MS Teams
pagerduty
object
PagerDuty notification settings for the team
service_name
string
Service name for PagerDuty
slack
object
Slack notification settings for the team
channel
string
Channel for Slack notification
workspace
string
Workspace for Slack notification
id
string
The identifier of the team notification rule
type [_required_]
enum
Team notification rule type Allowed enum values: `team_notification_rules`
default: `team_notification_rules`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)


#####  Get team notification rule
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules/${rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Update team notification rule](https://docs.datadoghq.com/api/latest/teams/#update-team-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#update-team-notification-rule-v2)


PUT https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}
### Overview
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
rule_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Field
Type
Description
data [_required_]
object
Team notification rule
attributes [_required_]
object
Team notification rule attributes
email
object
Email notification settings for the team
enabled
boolean
Flag indicating email notification
ms_teams
object
MS Teams notification settings for the team
connector_name
string
Handle for MS Teams
pagerduty
object
PagerDuty notification settings for the team
service_name
string
Service name for PagerDuty
slack
object
Slack notification settings for the team
channel
string
Channel for Slack notification
workspace
string
Workspace for Slack notification
id
string
The identifier of the team notification rule
type [_required_]
enum
Team notification rule type Allowed enum values: `team_notification_rules`
default: `team_notification_rules`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamNotificationRule-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#UpdateTeamNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


Team notification rule response
Field
Type
Description
data
object
Team notification rule
attributes [_required_]
object
Team notification rule attributes
email
object
Email notification settings for the team
enabled
boolean
Flag indicating email notification
ms_teams
object
MS Teams notification settings for the team
connector_name
string
Handle for MS Teams
pagerduty
object
PagerDuty notification settings for the team
service_name
string
Service name for PagerDuty
slack
object
Slack notification settings for the team
channel
string
Channel for Slack notification
workspace
string
Workspace for Slack notification
id
string
The identifier of the team notification rule
type [_required_]
enum
Team notification rule type Allowed enum values: `team_notification_rules`
default: `team_notification_rules`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)


#####  Update team notification rule returns "OK" response
Copy
```
                          # Path parameters  
export team_id="CHANGE_ME"  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules/${rule_id}" \
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

                        
```

* * *
## [Delete team notification rule](https://docs.datadoghq.com/api/latest/teams/#delete-team-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/teams/#delete-team-notification-rule-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.datadoghq.eu/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.ddog-gov.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.us3.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}https://api.us5.datadoghq.com/api/v2/team/{team_id}/notification-rules/{rule_id}
### Overview
This endpoint requires the `teams_read` permission.
OAuth apps require the `teams_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
None
rule_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamNotificationRule-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/teams/#DeleteTeamNotificationRule-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/teams/)
  * [Example](https://docs.datadoghq.com/api/latest/teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/teams/?code-lang=curl)


#####  Delete team notification rule
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/team/${team_id}/notification-rules/${rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=73beefbf-dd3a-4f0f-b7d5-68db78d29a29&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=0633be22-c613-4aab-8de3-706107e7aafe&pt=Teams&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fteams%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=73beefbf-dd3a-4f0f-b7d5-68db78d29a29&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=0633be22-c613-4aab-8de3-706107e7aafe&pt=Teams&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fteams%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=030e871f-5062-4d3b-ace8-47fd7556ba05&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Teams&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fteams%2F&r=&lt=14801&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=55476)
