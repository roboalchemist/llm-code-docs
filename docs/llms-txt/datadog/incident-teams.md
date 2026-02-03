# Source: https://docs.datadoghq.com/api/latest/incident-teams.md

---
title: Incident Teams
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Incident Teams
---

# Incident Teams

The Incident Teams endpoints are deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/) to create, update, delete, and retrieve teams which can be associated with incidents.

## Get details of an incident team{% #get-details-of-an-incident-team %}
**Note**: This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/teams/{team_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/teams/{team_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/teams/{team_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/teams/{team_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/teams/{team_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/teams/{team_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/teams/{team_id} |

### Overview

Get details of an incident team. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. This endpoint requires the `incident_read` permission.

OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                  |
| ------------------------- | ------ | ---------------------------- |
| team_id [*required*] | string | The ID of the incident team. |

#### Query Strings

| Name    | Type | Description                                                                                                           |
| ------- | ---- | --------------------------------------------------------------------------------------------------------------------- |
| include | enum | Specifies which types of related objects should be included in the response.Allowed enum values: `users, attachments` |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with an incident team payload.

| Parent field     | Field                  | Type            | Description                                                   |
| ---------------- | ---------------------- | --------------- | ------------------------------------------------------------- |
|                  | data [*required*] | object          | Incident Team data from a response.                           |
| data             | attributes             | object          | The incident team's attributes from a response.               |
| attributes       | created                | date-time       | Timestamp of when the incident team was created.              |
| attributes       | modified               | date-time       | Timestamp of when the incident team was modified.             |
| attributes       | name                   | string          | Name of the incident team.                                    |
| data             | id                     | string          | The incident team's ID.                                       |
| data             | relationships          | object          | The incident team's relationships.                            |
| relationships    | created_by             | object          | Relationship to user.                                         |
| created_by       | data [*required*] | object          | Relationship to user object.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| relationships    | last_modified_by       | object          | Relationship to user.                                         |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| data             | type                   | enum            | Incident Team resource type. Allowed enum values: `teams`     |
|                  | included               | [ <oneOf>] | Included objects from relationships.                          |
| included         | Option 1               | object          | User object returned by the API.                              |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                |
| attributes       | created_at             | date-time       | Creation time of the user.                                    |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                 |
| attributes       | email                  | string          | Email of the user.                                            |
| attributes       | handle                 | string          | Handle of the user.                                           |
| attributes       | icon                   | string          | URL of the user's icon.                                       |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                             |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                      |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                         |
| attributes       | name                   | string          | Name of the user.                                             |
| attributes       | service_account        | boolean         | Whether the user is a service account.                        |
| attributes       | status                 | string          | Status of the user.                                           |
| attributes       | title                  | string          | Title of the user.                                            |
| attributes       | verified               | boolean         | Whether the user is verified.                                 |
| Option 1         | id                     | string          | ID of the user.                                               |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.         |
| relationships    | org                    | object          | Relationship to an organization.                              |
| org              | data [*required*] | object          | Relationship to organization object.                          |
| data             | id [*required*]   | string          | ID of the organization.                                       |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`      |
| relationships    | other_orgs             | object          | Relationship to organizations.                                |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                        |
| data             | id [*required*]   | string          | ID of the organization.                                       |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`      |
| relationships    | other_users            | object          | Relationship to users.                                        |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| relationships    | roles                  | object          | Relationship to roles.                                        |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role. |
| data             | id                     | string          | The unique identifier of the role.                            |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                      |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`             |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams/${team_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Delete an existing incident team{% #delete-an-existing-incident-team %}
**Note**: This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/teams/{team_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/teams/{team_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/teams/{team_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/teams/{team_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/teams/{team_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/teams/{team_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/teams/{team_id} |

### Overview

Deletes an existing incident team. This endpoint requires the `incident_settings_write` permission.

OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                  |
| ------------------------- | ------ | ---------------------------- |
| team_id [*required*] | string | The ID of the incident team. |

### Response

{% tab title="204" %}
OK
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
                  \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams/${team_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Update an existing incident team{% #update-an-existing-incident-team %}
**Note**: This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/teams/{team_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/teams/{team_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/teams/{team_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/teams/{team_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/teams/{team_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/teams/{team_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/teams/{team_id} |

### Overview

Updates an existing incident team. Only provide the attributes which should be updated as this request is a partial update. This endpoint requires the `incident_settings_write` permission.

OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                  |
| ------------------------- | ------ | ---------------------------- |
| team_id [*required*] | string | The ID of the incident team. |

### Request

#### Body Data (required)

Incident Team Payload.

{% tab title="Model" %}

| Parent field     | Field                  | Type   | Description                                               |
| ---------------- | ---------------------- | ------ | --------------------------------------------------------- |
|                  | data [*required*] | object | Incident Team data for an update request.                 |
| data             | attributes             | object | The incident team's attributes for an update request.     |
| attributes       | name [*required*] | string | Name of the incident team.                                |
| data             | id                     | string | The incident team's ID.                                   |
| data             | relationships          | object | The incident team's relationships.                        |
| relationships    | created_by             | object | Relationship to user.                                     |
| created_by       | data [*required*] | object | Relationship to user object.                              |
| data             | id [*required*]   | string | A unique identifier that represents the user.             |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`         |
| relationships    | last_modified_by       | object | Relationship to user.                                     |
| last_modified_by | data [*required*] | object | Relationship to user object.                              |
| data             | id [*required*]   | string | A unique identifier that represents the user.             |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`         |
| data             | type [*required*] | enum   | Incident Team resource type. Allowed enum values: `teams` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "teams",
    "attributes": {
      "name": "team name-updated"
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with an incident team payload.

| Parent field     | Field                  | Type            | Description                                                   |
| ---------------- | ---------------------- | --------------- | ------------------------------------------------------------- |
|                  | data [*required*] | object          | Incident Team data from a response.                           |
| data             | attributes             | object          | The incident team's attributes from a response.               |
| attributes       | created                | date-time       | Timestamp of when the incident team was created.              |
| attributes       | modified               | date-time       | Timestamp of when the incident team was modified.             |
| attributes       | name                   | string          | Name of the incident team.                                    |
| data             | id                     | string          | The incident team's ID.                                       |
| data             | relationships          | object          | The incident team's relationships.                            |
| relationships    | created_by             | object          | Relationship to user.                                         |
| created_by       | data [*required*] | object          | Relationship to user object.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| relationships    | last_modified_by       | object          | Relationship to user.                                         |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| data             | type                   | enum            | Incident Team resource type. Allowed enum values: `teams`     |
|                  | included               | [ <oneOf>] | Included objects from relationships.                          |
| included         | Option 1               | object          | User object returned by the API.                              |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                |
| attributes       | created_at             | date-time       | Creation time of the user.                                    |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                 |
| attributes       | email                  | string          | Email of the user.                                            |
| attributes       | handle                 | string          | Handle of the user.                                           |
| attributes       | icon                   | string          | URL of the user's icon.                                       |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                             |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                      |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                         |
| attributes       | name                   | string          | Name of the user.                                             |
| attributes       | service_account        | boolean         | Whether the user is a service account.                        |
| attributes       | status                 | string          | Status of the user.                                           |
| attributes       | title                  | string          | Title of the user.                                            |
| attributes       | verified               | boolean         | Whether the user is verified.                                 |
| Option 1         | id                     | string          | ID of the user.                                               |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.         |
| relationships    | org                    | object          | Relationship to an organization.                              |
| org              | data [*required*] | object          | Relationship to organization object.                          |
| data             | id [*required*]   | string          | ID of the organization.                                       |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`      |
| relationships    | other_orgs             | object          | Relationship to organizations.                                |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                        |
| data             | id [*required*]   | string          | ID of the organization.                                       |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`      |
| relationships    | other_users            | object          | Relationship to users.                                        |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| relationships    | roles                  | object          | Relationship to roles.                                        |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role. |
| data             | id                     | string          | The unique identifier of the role.                            |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                      |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`             |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport team_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams/${team_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Get a list of all incident teams{% #get-a-list-of-all-incident-teams %}
**Note**: This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/teams |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/teams |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/teams      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/teams      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/teams     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/teams |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/teams |

### Overview

Get all incident teams for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. This endpoint requires the `incident_read` permission.

OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                                           |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------- |
| include      | enum    | Specifies which types of related objects should be included in the response.Allowed enum values: `users, attachments` |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100.                                                              |
| page[offset] | integer | Specific offset to use as the beginning of the returned page.                                                         |
| filter       | string  | A search query that filters teams by name.                                                                            |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with a list of incident team payloads.

| Parent field     | Field                  | Type            | Description                                                                                                 |
| ---------------- | ---------------------- | --------------- | ----------------------------------------------------------------------------------------------------------- |
|                  | data [*required*] | [object]        | An array of incident teams.                                                                                 |
| data             | attributes             | object          | The incident team's attributes from a response.                                                             |
| attributes       | created                | date-time       | Timestamp of when the incident team was created.                                                            |
| attributes       | modified               | date-time       | Timestamp of when the incident team was modified.                                                           |
| attributes       | name                   | string          | Name of the incident team.                                                                                  |
| data             | id                     | string          | The incident team's ID.                                                                                     |
| data             | relationships          | object          | The incident team's relationships.                                                                          |
| relationships    | created_by             | object          | Relationship to user.                                                                                       |
| created_by       | data [*required*] | object          | Relationship to user object.                                                                                |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                                                               |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                           |
| relationships    | last_modified_by       | object          | Relationship to user.                                                                                       |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                                                                |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                                                               |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                           |
| data             | type                   | enum            | Incident Team resource type. Allowed enum values: `teams`                                                   |
|                  | included               | [ <oneOf>] | Included related resources which the user requested.                                                        |
| included         | Option 1               | object          | User object returned by the API.                                                                            |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                                                              |
| attributes       | created_at             | date-time       | Creation time of the user.                                                                                  |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                                                               |
| attributes       | email                  | string          | Email of the user.                                                                                          |
| attributes       | handle                 | string          | Handle of the user.                                                                                         |
| attributes       | icon                   | string          | URL of the user's icon.                                                                                     |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                                                                           |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                                                                    |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                                                                       |
| attributes       | name                   | string          | Name of the user.                                                                                           |
| attributes       | service_account        | boolean         | Whether the user is a service account.                                                                      |
| attributes       | status                 | string          | Status of the user.                                                                                         |
| attributes       | title                  | string          | Title of the user.                                                                                          |
| attributes       | verified               | boolean         | Whether the user is verified.                                                                               |
| Option 1         | id                     | string          | ID of the user.                                                                                             |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.                                                       |
| relationships    | org                    | object          | Relationship to an organization.                                                                            |
| org              | data [*required*] | object          | Relationship to organization object.                                                                        |
| data             | id [*required*]   | string          | ID of the organization.                                                                                     |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`                                                    |
| relationships    | other_orgs             | object          | Relationship to organizations.                                                                              |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                                                                      |
| data             | id [*required*]   | string          | ID of the organization.                                                                                     |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`                                                    |
| relationships    | other_users            | object          | Relationship to users.                                                                                      |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                                                              |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                                                               |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                           |
| relationships    | roles                  | object          | Relationship to roles.                                                                                      |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role.                                               |
| data             | id                     | string          | The unique identifier of the role.                                                                          |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                                                                    |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`                                                           |
|                  | meta                   | object          | The metadata object containing pagination metadata.                                                         |
| meta             | pagination             | object          | Pagination properties.                                                                                      |
| pagination       | next_offset            | int64           | The index of the first element in the next page of results. Equal to page size added to the current offset. |
| pagination       | offset                 | int64           | The index of the first element in the results.                                                              |
| pagination       | size                   | int64           | Maximum size of pages to return.                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Create a new incident team{% #create-a-new-incident-team %}
**Note**: This endpoint is deprecated. See the [Teams API endpoints](https://docs.datadoghq.com/api/latest/teams/).
| Datadog site      | API endpoint                                    |
| ----------------- | ----------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/teams |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/teams |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/teams      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/teams      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/teams     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/teams |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/teams |

### Overview

Creates a new incident team. This endpoint requires the `incident_settings_write` permission.

OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-teams) to access this endpoint.



### Request

#### Body Data (required)

Incident Team Payload.

{% tab title="Model" %}

| Parent field     | Field                  | Type   | Description                                               |
| ---------------- | ---------------------- | ------ | --------------------------------------------------------- |
|                  | data [*required*] | object | Incident Team data for a create request.                  |
| data             | attributes             | object | The incident team's attributes for a create request.      |
| attributes       | name [*required*] | string | Name of the incident team.                                |
| data             | relationships          | object | The incident team's relationships.                        |
| relationships    | created_by             | object | Relationship to user.                                     |
| created_by       | data [*required*] | object | Relationship to user object.                              |
| data             | id [*required*]   | string | A unique identifier that represents the user.             |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`         |
| relationships    | last_modified_by       | object | Relationship to user.                                     |
| last_modified_by | data [*required*] | object | Relationship to user object.                              |
| data             | id [*required*]   | string | A unique identifier that represents the user.             |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`         |
| data             | type [*required*] | enum   | Incident Team resource type. Allowed enum values: `teams` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "teams",
    "attributes": {
      "name": "Example-Incident-Team"
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response with an incident team payload.

| Parent field     | Field                  | Type            | Description                                                   |
| ---------------- | ---------------------- | --------------- | ------------------------------------------------------------- |
|                  | data [*required*] | object          | Incident Team data from a response.                           |
| data             | attributes             | object          | The incident team's attributes from a response.               |
| attributes       | created                | date-time       | Timestamp of when the incident team was created.              |
| attributes       | modified               | date-time       | Timestamp of when the incident team was modified.             |
| attributes       | name                   | string          | Name of the incident team.                                    |
| data             | id                     | string          | The incident team's ID.                                       |
| data             | relationships          | object          | The incident team's relationships.                            |
| relationships    | created_by             | object          | Relationship to user.                                         |
| created_by       | data [*required*] | object          | Relationship to user object.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| relationships    | last_modified_by       | object          | Relationship to user.                                         |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| data             | type                   | enum            | Incident Team resource type. Allowed enum values: `teams`     |
|                  | included               | [ <oneOf>] | Included objects from relationships.                          |
| included         | Option 1               | object          | User object returned by the API.                              |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                |
| attributes       | created_at             | date-time       | Creation time of the user.                                    |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                 |
| attributes       | email                  | string          | Email of the user.                                            |
| attributes       | handle                 | string          | Handle of the user.                                           |
| attributes       | icon                   | string          | URL of the user's icon.                                       |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                             |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                      |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                         |
| attributes       | name                   | string          | Name of the user.                                             |
| attributes       | service_account        | boolean         | Whether the user is a service account.                        |
| attributes       | status                 | string          | Status of the user.                                           |
| attributes       | title                  | string          | Title of the user.                                            |
| attributes       | verified               | boolean         | Whether the user is verified.                                 |
| Option 1         | id                     | string          | ID of the user.                                               |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.         |
| relationships    | org                    | object          | Relationship to an organization.                              |
| org              | data [*required*] | object          | Relationship to organization object.                          |
| data             | id [*required*]   | string          | ID of the organization.                                       |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`      |
| relationships    | other_orgs             | object          | Relationship to organizations.                                |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                        |
| data             | id [*required*]   | string          | ID of the organization.                                       |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`      |
| relationships    | other_users            | object          | Relationship to users.                                        |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                 |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`             |
| relationships    | roles                  | object          | Relationship to roles.                                        |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role. |
| data             | id                     | string          | The unique identifier of the role.                            |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                      |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`             |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/teams" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"