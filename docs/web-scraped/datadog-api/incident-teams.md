# Source: https://docs.datadoghq.com/api/latest/incident-teams

# Incident Teams
The Incident Teams endpoints are deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/) to create, update, delete, and retrieve teams which can be associated with incidents.
## [Get details of an incident team](https://docs.datadoghq.com/api/latest/incident-teams/#get-details-of-an-incident-team)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/incident-teams/#get-details-of-an-incident-team-v2)


**Note** : This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
GET https://api.ap1.datadoghq.com/api/v2/teams/{team_id}https://api.ap2.datadoghq.com/api/v2/teams/{team_id}https://api.datadoghq.eu/api/v2/teams/{team_id}https://api.ddog-gov.com/api/v2/teams/{team_id}https://api.datadoghq.com/api/v2/teams/{team_id}https://api.us3.datadoghq.com/api/v2/teams/{team_id}https://api.us5.datadoghq.com/api/v2/teams/{team_id}
### Overview
Get details of an incident team. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
The ID of the incident team.
#### Query Strings
Name
Type
Description
include
enum
Specifies which types of related objects should be included in the response.  
Allowed enum values: `users, attachments`
### Response
  * [200](https://docs.datadoghq.com/api/latest/incident-teams/#GetIncidentTeam-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incident-teams/#GetIncidentTeam-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incident-teams/#GetIncidentTeam-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incident-teams/#GetIncidentTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incident-teams/#GetIncidentTeam-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incident-teams/#GetIncidentTeam-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


Response with an incident team payload.
Field
Type
Description
data [_required_]
object
Incident Team data from a response.
attributes
object
The incident team's attributes from a response.
created
date-time
Timestamp of when the incident team was created.
modified
date-time
Timestamp of when the incident team was modified.
name
string
Name of the incident team.
id
string
The incident team's ID.
relationships
object
The incident team's relationships.
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
Users resource type. Allowed enum values: `users`
default: `users`
last_modified_by
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
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Incident Team resource type. Allowed enum values: `teams`
default: `teams`
included
[ <oneOf>]
Included objects from relationships.
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
```
{
  "data": {
    "attributes": {
      "created": "2019-09-19T10:00:00.000Z",
      "modified": "2019-09-19T10:00:00.000Z",
      "name": "team name"
    },
    "id": "00000000-7ea3-0000-000a-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "teams"
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
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=typescript)


#####  Get details of an incident team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams/${team_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get details of an incident team
```
"""
Get details of an incident team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi

# there is a valid "team" in the system
TEAM_DATA_ID = environ["TEAM_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.get_incident_team(
        team_id=TEAM_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get details of an incident team
```
# Get details of an incident team returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident_team".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentTeamsAPI.new

# there is a valid "team" in the system
TEAM_DATA_ID = ENV["TEAM_DATA_ID"]
p api_instance.get_incident_team(TEAM_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get details of an incident team
```
// Get details of an incident team returns "OK" response

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
	// there is a valid "team" in the system
	TeamDataID := os.Getenv("TEAM_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetIncidentTeam", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentTeamsApi(apiClient)
	resp, r, err := api.GetIncidentTeam(ctx, TeamDataID, *datadogV2.NewGetIncidentTeamOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentTeamsApi.GetIncidentTeam`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentTeamsApi.GetIncidentTeam`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get details of an incident team
```
// Get details of an incident team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentTeamsApi;
import com.datadog.api.client.v2.model.IncidentTeamResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncidentTeam", true);
    IncidentTeamsApi apiInstance = new IncidentTeamsApi(defaultClient);

    // there is a valid "team" in the system
    String TEAM_DATA_ID = System.getenv("TEAM_DATA_ID");

    try {
      IncidentTeamResponse result = apiInstance.getIncidentTeam(TEAM_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentTeamsApi#getIncidentTeam");
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

#####  Get details of an incident team
```
// Get details of an incident team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_teams::GetIncidentTeamOptionalParams;
use datadog_api_client::datadogV2::api_incident_teams::IncidentTeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "team" in the system
    let team_data_id = std::env::var("TEAM_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncidentTeam", true);
    let api = IncidentTeamsAPI::with_config(configuration);
    let resp = api
        .get_incident_team(
            team_data_id.clone(),
            GetIncidentTeamOptionalParams::default(),
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

#####  Get details of an incident team
```
/**
 * Get details of an incident team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncidentTeam"] = true;
const apiInstance = new v2.IncidentTeamsApi(configuration);

// there is a valid "team" in the system
const TEAM_DATA_ID = process.env.TEAM_DATA_ID as string;

const params: v2.IncidentTeamsApiGetIncidentTeamRequest = {
  teamId: TEAM_DATA_ID,
};

apiInstance
  .getIncidentTeam(params)
  .then((data: v2.IncidentTeamResponse) => {
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
## [Delete an existing incident team](https://docs.datadoghq.com/api/latest/incident-teams/#delete-an-existing-incident-team)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/incident-teams/#delete-an-existing-incident-team-v2)


**Note** : This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
DELETE https://api.ap1.datadoghq.com/api/v2/teams/{team_id}https://api.ap2.datadoghq.com/api/v2/teams/{team_id}https://api.datadoghq.eu/api/v2/teams/{team_id}https://api.ddog-gov.com/api/v2/teams/{team_id}https://api.datadoghq.com/api/v2/teams/{team_id}https://api.us3.datadoghq.com/api/v2/teams/{team_id}https://api.us5.datadoghq.com/api/v2/teams/{team_id}
### Overview
Deletes an existing incident team. This endpoint requires the `incident_settings_write` permission.
OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
The ID of the incident team.
### Response
  * [204](https://docs.datadoghq.com/api/latest/incident-teams/#DeleteIncidentTeam-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incident-teams/#DeleteIncidentTeam-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incident-teams/#DeleteIncidentTeam-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incident-teams/#DeleteIncidentTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incident-teams/#DeleteIncidentTeam-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incident-teams/#DeleteIncidentTeam-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=typescript)


#####  Delete an existing incident team
Copy
```
                  # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams/${team_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an existing incident team
```
"""
Delete an existing incident team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi

# there is a valid "team" in the system
TEAM_DATA_ID = environ["TEAM_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    api_instance.delete_incident_team(
        team_id=TEAM_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an existing incident team
```
# Delete an existing incident team returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_team".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentTeamsAPI.new

# there is a valid "team" in the system
TEAM_DATA_ID = ENV["TEAM_DATA_ID"]
api_instance.delete_incident_team(TEAM_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an existing incident team
```
// Delete an existing incident team returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "team" in the system
	TeamDataID := os.Getenv("TEAM_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncidentTeam", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentTeamsApi(apiClient)
	r, err := api.DeleteIncidentTeam(ctx, TeamDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentTeamsApi.DeleteIncidentTeam`: %v\n", err)
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

#####  Delete an existing incident team
```
// Delete an existing incident team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentTeam", true);
    IncidentTeamsApi apiInstance = new IncidentTeamsApi(defaultClient);

    // there is a valid "team" in the system
    String TEAM_DATA_ID = System.getenv("TEAM_DATA_ID");

    try {
      apiInstance.deleteIncidentTeam(TEAM_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentTeamsApi#deleteIncidentTeam");
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

#####  Delete an existing incident team
```
// Delete an existing incident team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_teams::IncidentTeamsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "team" in the system
    let team_data_id = std::env::var("TEAM_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentTeam", true);
    let api = IncidentTeamsAPI::with_config(configuration);
    let resp = api.delete_incident_team(team_data_id.clone()).await;
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

#####  Delete an existing incident team
```
/**
 * Delete an existing incident team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentTeam"] = true;
const apiInstance = new v2.IncidentTeamsApi(configuration);

// there is a valid "team" in the system
const TEAM_DATA_ID = process.env.TEAM_DATA_ID as string;

const params: v2.IncidentTeamsApiDeleteIncidentTeamRequest = {
  teamId: TEAM_DATA_ID,
};

apiInstance
  .deleteIncidentTeam(params)
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
## [Update an existing incident team](https://docs.datadoghq.com/api/latest/incident-teams/#update-an-existing-incident-team)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/incident-teams/#update-an-existing-incident-team-v2)


**Note** : This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
PATCH https://api.ap1.datadoghq.com/api/v2/teams/{team_id}https://api.ap2.datadoghq.com/api/v2/teams/{team_id}https://api.datadoghq.eu/api/v2/teams/{team_id}https://api.ddog-gov.com/api/v2/teams/{team_id}https://api.datadoghq.com/api/v2/teams/{team_id}https://api.us3.datadoghq.com/api/v2/teams/{team_id}https://api.us5.datadoghq.com/api/v2/teams/{team_id}
### Overview
Updates an existing incident team. Only provide the attributes which should be updated as this request is a partial update. This endpoint requires the `incident_settings_write` permission.
OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
The ID of the incident team.
### Request
#### Body Data (required)
Incident Team Payload.
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


Field
Type
Description
data [_required_]
object
Incident Team data for an update request.
attributes
object
The incident team's attributes for an update request.
name [_required_]
string
Name of the incident team.
id
string
The incident team's ID.
relationships
object
The incident team's relationships.
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
Users resource type. Allowed enum values: `users`
default: `users`
last_modified_by
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
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Incident Team resource type. Allowed enum values: `teams`
default: `teams`
```
{
  "data": {
    "type": "teams",
    "attributes": {
      "name": "team name-updated"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incident-teams/#UpdateIncidentTeam-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incident-teams/#UpdateIncidentTeam-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incident-teams/#UpdateIncidentTeam-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incident-teams/#UpdateIncidentTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incident-teams/#UpdateIncidentTeam-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incident-teams/#UpdateIncidentTeam-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


Response with an incident team payload.
Field
Type
Description
data [_required_]
object
Incident Team data from a response.
attributes
object
The incident team's attributes from a response.
created
date-time
Timestamp of when the incident team was created.
modified
date-time
Timestamp of when the incident team was modified.
name
string
Name of the incident team.
id
string
The incident team's ID.
relationships
object
The incident team's relationships.
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
Users resource type. Allowed enum values: `users`
default: `users`
last_modified_by
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
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Incident Team resource type. Allowed enum values: `teams`
default: `teams`
included
[ <oneOf>]
Included objects from relationships.
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
```
{
  "data": {
    "attributes": {
      "created": "2019-09-19T10:00:00.000Z",
      "modified": "2019-09-19T10:00:00.000Z",
      "name": "team name"
    },
    "id": "00000000-7ea3-0000-000a-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "teams"
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
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=typescript)


#####  Update an existing incident team returns "OK" response
Copy
```
                          # Path parameters  
export team_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams/${team_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "teams",
    "attributes": {
      "name": "team name-updated"
    }
  }
}
EOF  

                        
```

#####  Update an existing incident team returns "OK" response
```
// Update an existing incident team returns "OK" response

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
	// there is a valid "team" in the system
	TeamDataID := os.Getenv("TEAM_DATA_ID")

	body := datadogV2.IncidentTeamUpdateRequest{
		Data: datadogV2.IncidentTeamUpdateData{
			Type: datadogV2.INCIDENTTEAMTYPE_TEAMS,
			Attributes: &datadogV2.IncidentTeamUpdateAttributes{
				Name: "team name-updated",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncidentTeam", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentTeamsApi(apiClient)
	resp, r, err := api.UpdateIncidentTeam(ctx, TeamDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentTeamsApi.UpdateIncidentTeam`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentTeamsApi.UpdateIncidentTeam`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update an existing incident team returns "OK" response
```
// Update an existing incident team returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentTeamsApi;
import com.datadog.api.client.v2.model.IncidentTeamResponse;
import com.datadog.api.client.v2.model.IncidentTeamType;
import com.datadog.api.client.v2.model.IncidentTeamUpdateAttributes;
import com.datadog.api.client.v2.model.IncidentTeamUpdateData;
import com.datadog.api.client.v2.model.IncidentTeamUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncidentTeam", true);
    IncidentTeamsApi apiInstance = new IncidentTeamsApi(defaultClient);

    // there is a valid "team" in the system
    String TEAM_DATA_ATTRIBUTES_NAME = System.getenv("TEAM_DATA_ATTRIBUTES_NAME");
    String TEAM_DATA_ID = System.getenv("TEAM_DATA_ID");

    IncidentTeamUpdateRequest body =
        new IncidentTeamUpdateRequest()
            .data(
                new IncidentTeamUpdateData()
                    .type(IncidentTeamType.TEAMS)
                    .attributes(new IncidentTeamUpdateAttributes().name("team name-updated")));

    try {
      IncidentTeamResponse result = apiInstance.updateIncidentTeam(TEAM_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentTeamsApi#updateIncidentTeam");
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

#####  Update an existing incident team returns "OK" response
```
"""
Update an existing incident team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi
from datadog_api_client.v2.model.incident_team_type import IncidentTeamType
from datadog_api_client.v2.model.incident_team_update_attributes import IncidentTeamUpdateAttributes
from datadog_api_client.v2.model.incident_team_update_data import IncidentTeamUpdateData
from datadog_api_client.v2.model.incident_team_update_request import IncidentTeamUpdateRequest

# there is a valid "team" in the system
TEAM_DATA_ATTRIBUTES_NAME = environ["TEAM_DATA_ATTRIBUTES_NAME"]
TEAM_DATA_ID = environ["TEAM_DATA_ID"]

body = IncidentTeamUpdateRequest(
    data=IncidentTeamUpdateData(
        type=IncidentTeamType.TEAMS,
        attributes=IncidentTeamUpdateAttributes(
            name="team name-updated",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.update_incident_team(team_id=TEAM_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update an existing incident team returns "OK" response
```
# Update an existing incident team returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident_team".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentTeamsAPI.new

# there is a valid "team" in the system
TEAM_DATA_ATTRIBUTES_NAME = ENV["TEAM_DATA_ATTRIBUTES_NAME"]
TEAM_DATA_ID = ENV["TEAM_DATA_ID"]

body = DatadogAPIClient::V2::IncidentTeamUpdateRequest.new({
  data: DatadogAPIClient::V2::IncidentTeamUpdateData.new({
    type: DatadogAPIClient::V2::IncidentTeamType::TEAMS,
    attributes: DatadogAPIClient::V2::IncidentTeamUpdateAttributes.new({
      name: "team name-updated",
    }),
  }),
})
p api_instance.update_incident_team(TEAM_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update an existing incident team returns "OK" response
```
// Update an existing incident team returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_teams::IncidentTeamsAPI;
use datadog_api_client::datadogV2::model::IncidentTeamType;
use datadog_api_client::datadogV2::model::IncidentTeamUpdateAttributes;
use datadog_api_client::datadogV2::model::IncidentTeamUpdateData;
use datadog_api_client::datadogV2::model::IncidentTeamUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "team" in the system
    let team_data_id = std::env::var("TEAM_DATA_ID").unwrap();
    let body = IncidentTeamUpdateRequest::new(
        IncidentTeamUpdateData::new(IncidentTeamType::TEAMS).attributes(
            IncidentTeamUpdateAttributes::new("team name-updated".to_string()),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncidentTeam", true);
    let api = IncidentTeamsAPI::with_config(configuration);
    let resp = api.update_incident_team(team_data_id.clone(), body).await;
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

#####  Update an existing incident team returns "OK" response
```
/**
 * Update an existing incident team returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncidentTeam"] = true;
const apiInstance = new v2.IncidentTeamsApi(configuration);

// there is a valid "team" in the system
const TEAM_DATA_ID = process.env.TEAM_DATA_ID as string;

const params: v2.IncidentTeamsApiUpdateIncidentTeamRequest = {
  body: {
    data: {
      type: "teams",
      attributes: {
        name: "team name-updated",
      },
    },
  },
  teamId: TEAM_DATA_ID,
};

apiInstance
  .updateIncidentTeam(params)
  .then((data: v2.IncidentTeamResponse) => {
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
## [Get a list of all incident teams](https://docs.datadoghq.com/api/latest/incident-teams/#get-a-list-of-all-incident-teams)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/incident-teams/#get-a-list-of-all-incident-teams-v2)


**Note** : This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
GET https://api.ap1.datadoghq.com/api/v2/teamshttps://api.ap2.datadoghq.com/api/v2/teamshttps://api.datadoghq.eu/api/v2/teamshttps://api.ddog-gov.com/api/v2/teamshttps://api.datadoghq.com/api/v2/teamshttps://api.us3.datadoghq.com/api/v2/teamshttps://api.us5.datadoghq.com/api/v2/teams
### Overview
Get all incident teams for the requesting user’s organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
include
enum
Specifies which types of related objects should be included in the response.  
Allowed enum values: `users, attachments`
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[offset]
integer
Specific offset to use as the beginning of the returned page.
filter
string
A search query that filters teams by name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incident-teams/#ListIncidentTeams-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incident-teams/#ListIncidentTeams-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incident-teams/#ListIncidentTeams-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incident-teams/#ListIncidentTeams-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incident-teams/#ListIncidentTeams-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incident-teams/#ListIncidentTeams-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


Response with a list of incident team payloads.
Field
Type
Description
data [_required_]
[object]
An array of incident teams.
attributes
object
The incident team's attributes from a response.
created
date-time
Timestamp of when the incident team was created.
modified
date-time
Timestamp of when the incident team was modified.
name
string
Name of the incident team.
id
string
The incident team's ID.
relationships
object
The incident team's relationships.
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
Users resource type. Allowed enum values: `users`
default: `users`
last_modified_by
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
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Incident Team resource type. Allowed enum values: `teams`
default: `teams`
included
[ <oneOf>]
Included related resources which the user requested.
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
meta
object
The metadata object containing pagination metadata.
pagination
object
Pagination properties.
next_offset
int64
The index of the first element in the next page of results. Equal to page size added to the current offset.
offset
int64
The index of the first element in the results.
size
int64
Maximum size of pages to return.
```
{
  "data": [
    {
      "attributes": {
        "created": "2019-09-19T10:00:00.000Z",
        "modified": "2019-09-19T10:00:00.000Z",
        "name": "team name"
      },
      "id": "00000000-7ea3-0000-000a-000000000000",
      "relationships": {
        "created_by": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "last_modified_by": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "teams"
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
  "meta": {
    "pagination": {
      "next_offset": 1000,
      "offset": 10,
      "size": 1000
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=typescript)


#####  Get a list of all incident teams
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of all incident teams
```
"""
Get a list of all incident teams returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi

# there is a valid "team" in the system
TEAM_DATA_ATTRIBUTES_NAME = environ["TEAM_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
configuration.unstable_operations["list_incident_teams"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.list_incident_teams(
        filter=TEAM_DATA_ATTRIBUTES_NAME,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of all incident teams
```
# Get a list of all incident teams returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_teams".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentTeamsAPI.new

# there is a valid "team" in the system
TEAM_DATA_ATTRIBUTES_NAME = ENV["TEAM_DATA_ATTRIBUTES_NAME"]
opts = {
  filter: TEAM_DATA_ATTRIBUTES_NAME,
}
p api_instance.list_incident_teams(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of all incident teams
```
// Get a list of all incident teams returns "OK" response

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
	// there is a valid "team" in the system
	TeamDataAttributesName := os.Getenv("TEAM_DATA_ATTRIBUTES_NAME")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ListIncidentTeams", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentTeamsApi(apiClient)
	resp, r, err := api.ListIncidentTeams(ctx, *datadogV2.NewListIncidentTeamsOptionalParameters().WithFilter(TeamDataAttributesName))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentTeamsApi.ListIncidentTeams`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentTeamsApi.ListIncidentTeams`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of all incident teams
```
// Get a list of all incident teams returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentTeamsApi;
import com.datadog.api.client.v2.api.IncidentTeamsApi.ListIncidentTeamsOptionalParameters;
import com.datadog.api.client.v2.model.IncidentTeamsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentTeams", true);
    IncidentTeamsApi apiInstance = new IncidentTeamsApi(defaultClient);

    // there is a valid "team" in the system
    String TEAM_DATA_ATTRIBUTES_NAME = System.getenv("TEAM_DATA_ATTRIBUTES_NAME");

    try {
      IncidentTeamsResponse result =
          apiInstance.listIncidentTeams(
              new ListIncidentTeamsOptionalParameters().filter(TEAM_DATA_ATTRIBUTES_NAME));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentTeamsApi#listIncidentTeams");
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

#####  Get a list of all incident teams
```
// Get a list of all incident teams returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_teams::IncidentTeamsAPI;
use datadog_api_client::datadogV2::api_incident_teams::ListIncidentTeamsOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "team" in the system
    let team_data_attributes_name = std::env::var("TEAM_DATA_ATTRIBUTES_NAME").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentTeams", true);
    let api = IncidentTeamsAPI::with_config(configuration);
    let resp = api
        .list_incident_teams(
            ListIncidentTeamsOptionalParams::default().filter(team_data_attributes_name.clone()),
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

#####  Get a list of all incident teams
```
/**
 * Get a list of all incident teams returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentTeams"] = true;
const apiInstance = new v2.IncidentTeamsApi(configuration);

// there is a valid "team" in the system
const TEAM_DATA_ATTRIBUTES_NAME = process.env
  .TEAM_DATA_ATTRIBUTES_NAME as string;

const params: v2.IncidentTeamsApiListIncidentTeamsRequest = {
  filter: TEAM_DATA_ATTRIBUTES_NAME,
};

apiInstance
  .listIncidentTeams(params)
  .then((data: v2.IncidentTeamsResponse) => {
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
## [Create a new incident team](https://docs.datadoghq.com/api/latest/incident-teams/#create-a-new-incident-team)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/incident-teams/#create-a-new-incident-team-v2)


**Note** : This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
POST https://api.ap1.datadoghq.com/api/v2/teamshttps://api.ap2.datadoghq.com/api/v2/teamshttps://api.datadoghq.eu/api/v2/teamshttps://api.ddog-gov.com/api/v2/teamshttps://api.datadoghq.com/api/v2/teamshttps://api.us3.datadoghq.com/api/v2/teamshttps://api.us5.datadoghq.com/api/v2/teams
### Overview
Creates a new incident team. This endpoint requires the `incident_settings_write` permission.
OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.
### Request
#### Body Data (required)
Incident Team Payload.
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


Field
Type
Description
data [_required_]
object
Incident Team data for a create request.
attributes
object
The incident team's attributes for a create request.
name [_required_]
string
Name of the incident team.
relationships
object
The incident team's relationships.
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
Users resource type. Allowed enum values: `users`
default: `users`
last_modified_by
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
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Incident Team resource type. Allowed enum values: `teams`
default: `teams`
```
{
  "data": {
    "type": "teams",
    "attributes": {
      "name": "Example-Incident-Team"
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incident-teams/#CreateIncidentTeam-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incident-teams/#CreateIncidentTeam-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incident-teams/#CreateIncidentTeam-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incident-teams/#CreateIncidentTeam-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incident-teams/#CreateIncidentTeam-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incident-teams/#CreateIncidentTeam-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


Response with an incident team payload.
Field
Type
Description
data [_required_]
object
Incident Team data from a response.
attributes
object
The incident team's attributes from a response.
created
date-time
Timestamp of when the incident team was created.
modified
date-time
Timestamp of when the incident team was modified.
name
string
Name of the incident team.
id
string
The incident team's ID.
relationships
object
The incident team's relationships.
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
Users resource type. Allowed enum values: `users`
default: `users`
last_modified_by
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
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Incident Team resource type. Allowed enum values: `teams`
default: `teams`
included
[ <oneOf>]
Included objects from relationships.
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
```
{
  "data": {
    "attributes": {
      "created": "2019-09-19T10:00:00.000Z",
      "modified": "2019-09-19T10:00:00.000Z",
      "name": "team name"
    },
    "id": "00000000-7ea3-0000-000a-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "teams"
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
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Model](https://docs.datadoghq.com/api/latest/incident-teams/)
  * [Example](https://docs.datadoghq.com/api/latest/incident-teams/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incident-teams/?code-lang=typescript)


#####  Create a new incident team returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "teams",
    "attributes": {
      "name": "Example-Incident-Team"
    }
  }
}
EOF  

                        
```

#####  Create a new incident team returns "CREATED" response
```
// Create a new incident team returns "CREATED" response

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
	body := datadogV2.IncidentTeamCreateRequest{
		Data: datadogV2.IncidentTeamCreateData{
			Type: datadogV2.INCIDENTTEAMTYPE_TEAMS,
			Attributes: &datadogV2.IncidentTeamCreateAttributes{
				Name: "Example-Incident-Team",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncidentTeam", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentTeamsApi(apiClient)
	resp, r, err := api.CreateIncidentTeam(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentTeamsApi.CreateIncidentTeam`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentTeamsApi.CreateIncidentTeam`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a new incident team returns "CREATED" response
```
// Create a new incident team returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentTeamsApi;
import com.datadog.api.client.v2.model.IncidentTeamCreateAttributes;
import com.datadog.api.client.v2.model.IncidentTeamCreateData;
import com.datadog.api.client.v2.model.IncidentTeamCreateRequest;
import com.datadog.api.client.v2.model.IncidentTeamResponse;
import com.datadog.api.client.v2.model.IncidentTeamType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentTeam", true);
    IncidentTeamsApi apiInstance = new IncidentTeamsApi(defaultClient);

    IncidentTeamCreateRequest body =
        new IncidentTeamCreateRequest()
            .data(
                new IncidentTeamCreateData()
                    .type(IncidentTeamType.TEAMS)
                    .attributes(new IncidentTeamCreateAttributes().name("Example-Incident-Team")));

    try {
      IncidentTeamResponse result = apiInstance.createIncidentTeam(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentTeamsApi#createIncidentTeam");
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

#####  Create a new incident team returns "CREATED" response
```
"""
Create a new incident team returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi
from datadog_api_client.v2.model.incident_team_create_attributes import IncidentTeamCreateAttributes
from datadog_api_client.v2.model.incident_team_create_data import IncidentTeamCreateData
from datadog_api_client.v2.model.incident_team_create_request import IncidentTeamCreateRequest
from datadog_api_client.v2.model.incident_team_type import IncidentTeamType

body = IncidentTeamCreateRequest(
    data=IncidentTeamCreateData(
        type=IncidentTeamType.TEAMS,
        attributes=IncidentTeamCreateAttributes(
            name="Example-Incident-Team",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.create_incident_team(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a new incident team returns "CREATED" response
```
# Create a new incident team returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_team".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentTeamsAPI.new

body = DatadogAPIClient::V2::IncidentTeamCreateRequest.new({
  data: DatadogAPIClient::V2::IncidentTeamCreateData.new({
    type: DatadogAPIClient::V2::IncidentTeamType::TEAMS,
    attributes: DatadogAPIClient::V2::IncidentTeamCreateAttributes.new({
      name: "Example-Incident-Team",
    }),
  }),
})
p api_instance.create_incident_team(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a new incident team returns "CREATED" response
```
// Create a new incident team returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_teams::IncidentTeamsAPI;
use datadog_api_client::datadogV2::model::IncidentTeamCreateAttributes;
use datadog_api_client::datadogV2::model::IncidentTeamCreateData;
use datadog_api_client::datadogV2::model::IncidentTeamCreateRequest;
use datadog_api_client::datadogV2::model::IncidentTeamType;

#[tokio::main]
async fn main() {
    let body = IncidentTeamCreateRequest::new(
        IncidentTeamCreateData::new(IncidentTeamType::TEAMS).attributes(
            IncidentTeamCreateAttributes::new("Example-Incident-Team".to_string()),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentTeam", true);
    let api = IncidentTeamsAPI::with_config(configuration);
    let resp = api.create_incident_team(body).await;
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

#####  Create a new incident team returns "CREATED" response
```
/**
 * Create a new incident team returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentTeam"] = true;
const apiInstance = new v2.IncidentTeamsApi(configuration);

const params: v2.IncidentTeamsApiCreateIncidentTeamRequest = {
  body: {
    data: {
      type: "teams",
      attributes: {
        name: "Example-Incident-Team",
      },
    },
  },
};

apiInstance
  .createIncidentTeam(params)
  .then((data: v2.IncidentTeamResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a702be77-f482-4118-a200-836272306c34&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b2ff3b54-3cdd-4cfa-82b2-28799788c8f5&pt=Incident%20Teams&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fincident-teams%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a702be77-f482-4118-a200-836272306c34&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b2ff3b54-3cdd-4cfa-82b2-28799788c8f5&pt=Incident%20Teams&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fincident-teams%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=b1f62ed5-ff34-45b5-9d24-1b89189125ea&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Incident%20Teams&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fincident-teams%2F&r=&lt=13530&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=42961)
