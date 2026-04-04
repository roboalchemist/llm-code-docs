# Source: https://docs.datadoghq.com/api/latest/on-call/

This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). (US1).
# On-Call
Configure your [Datadog On-Call](https://docs.datadoghq.com/service_management/on-call/) directly through the Datadog API.
## [Create On-Call schedule](https://docs.datadoghq.com/api/latest/on-call/#create-on-call-schedule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#create-on-call-schedule-v2)


POST https://api.ap1.datadoghq.com/api/v2/on-call/scheduleshttps://api.ap2.datadoghq.com/api/v2/on-call/scheduleshttps://api.datadoghq.eu/api/v2/on-call/scheduleshttps://api.ddog-gov.com/api/v2/on-call/scheduleshttps://api.datadoghq.com/api/v2/on-call/scheduleshttps://api.us3.datadoghq.com/api/v2/on-call/scheduleshttps://api.us5.datadoghq.com/api/v2/on-call/schedules
### Overview
Create a new On-Call schedule This endpoint requires the `on_call_write` permission.
### Arguments
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `teams`, `layers`, `layers.members`, `layers.members.user`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data [_required_]
object
The core data wrapper for creating a schedule, encompassing attributes, relationships, and the resource type.
attributes [_required_]
object
Describes the main attributes for creating a new schedule, including name, layers, and time zone.
layers [_required_]
[object]
The layers of On-Call coverage that define rotation intervals and restrictions.
effective_date [_required_]
date-time
The date/time when this layer becomes active (in ISO 8601).
end_date
date-time
The date/time after which this layer no longer applies (in ISO 8601).
interval [_required_]
object
Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
days
int32
The number of days in each rotation cycle.
seconds
int64
Any additional seconds for the rotation cycle (up to 30 days).
members [_required_]
[object]
A list of members who participate in this layer's rotation.
user
object
Identifies the user participating in this layer as a single object with an `id`.
id
string
The user's ID.
name [_required_]
string
The name of this layer.
restrictions
[object]
Zero or more time-based restrictions (for example, only weekdays, during business hours).
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
rotation_start [_required_]
date-time
The date/time when the rotation for this layer starts (in ISO 8601).
time_zone
string
The time zone for this layer.
name [_required_]
string
A human-readable name for the new schedule.
time_zone [_required_]
string
The time zone in which the schedule is defined.
relationships
object
Gathers relationship objects for the schedule creation request, including the teams to associate.
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
```
{
  "data": {
    "attributes": {
      "layers": [
        {
          "effective_date": "2021-11-01T11:11:11+00:00",
          "end_date": "2021-11-21T11:11:11+00:00",
          "interval": {
            "days": 1
          },
          "members": [
            {
              "user": {
                "id": "string"
              }
            }
          ],
          "name": "Layer 1",
          "restrictions": [
            {
              "end_day": "friday",
              "end_time": "17:00:00",
              "start_day": "monday",
              "start_time": "09:00:00"
            }
          ],
          "rotation_start": "2021-11-06T11:11:11+00:00"
        }
      ],
      "name": "Example-On-Call",
      "time_zone": "America/New_York"
    },
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "schedules"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallSchedule-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallSchedule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallSchedule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallSchedule-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallSchedule-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Top-level container for a schedule object, including both the `data` payload and any related `included` resources (such as teams, layers, or members).
Field
Type
Description
data
object
Represents the primary data object for a schedule, linking attributes and relationships.
attributes
object
Provides core properties of a schedule object such as its name and time zone.
name
string
A short name for the schedule.
time_zone
string
The time zone in which this schedule operates.
id
string
The schedule's unique identifier.
relationships
object
Groups the relationships for a schedule object, referencing layers and teams.
layers
object
Associates layers with this schedule in a data structure.
data
[object]
An array of layer references for this schedule.
id [_required_]
string
The unique identifier of the layer in this relationship.
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
included
[ <oneOf>]
Any additional resources related to this schedule, such as teams and layers.
Option 1
object
Provides a reference to a team, including ID, type, and basic attributes/relationships.
attributes
object
Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
avatar
string
URL or reference for the team's avatar (if available).
description
string
A short text describing the team.
handle
string
A unique handle/slug for the team.
name
string
The full, human-readable name of the team.
id
string
The team's unique identifier.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
Option 2
object
Encapsulates a layer resource, holding attributes like rotation details, plus relationships to the members covering that layer.
attributes
object
Describes key properties of a Layer, including rotation details, name, start/end times, and any restrictions.
effective_date
date-time
When the layer becomes active (ISO 8601).
end_date
date-time
When the layer ceases to be active (ISO 8601).
interval
object
Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
days
int32
The number of days in each rotation cycle.
seconds
int64
Any additional seconds for the rotation cycle (up to 30 days).
name
string
The name of this layer.
restrictions
[object]
An optional list of time restrictions for when this layer is in effect.
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
rotation_start
date-time
The date/time when the rotation starts (ISO 8601).
time_zone
string
The time zone for this layer.
id
string
A unique identifier for this layer.
relationships
object
Holds references to objects related to the Layer entity, such as its members.
members
object
Holds an array of references to the members of a Layer, each containing member IDs.
data
[object]
The list of members who belong to this layer.
id [_required_]
string
The unique user ID of the layer member.
type [_required_]
enum
Members resource type. Allowed enum values: `members`
default: `members`
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
Option 3
object
Represents a single member entry in a schedule, referencing a specific user.
id
string
The unique identifier for this schedule member.
relationships
object
Defines relationships for a schedule member, primarily referencing a single user.
user
object
Wraps the user data reference for a schedule member.
data [_required_]
object
Points to the user data associated with this schedule member, including an ID and type.
id [_required_]
string
The user's unique identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Schedule Members resource type. Allowed enum values: `members`
default: `members`
Option 4
object
Represents a user object in the context of a schedule, including their `id`, type, and basic attributes.
attributes
object
Provides basic user information for a schedule, including a name and email address.
email
string
The user's email address.
name
string
The user's name.
status
enum
The user's status. Allowed enum values: `active,deactivated,pending`
id
string
The unique user identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "name": "On-Call Schedule",
      "time_zone": "America/New_York"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "layers": {
        "data": [
          {
            "id": "00000000-0000-0000-0000-000000000001",
            "type": "layers"
          }
        ]
      },
      "teams": {
        "data": [
          {
            "id": "00000000-da3a-0000-0000-000000000000",
            "type": "teams"
          }
        ]
      }
    },
    "type": "schedules"
  },
  "included": [
    {
      "attributes": {
        "avatar": "",
        "description": "Team 1 description",
        "handle": "team1",
        "name": "Team 1"
      },
      "id": "00000000-da3a-0000-0000-000000000000",
      "type": "teams"
    },
    {
      "attributes": {
        "effective_date": "2025-02-03T05:00:00Z",
        "end_date": "2025-12-31T00:00:00Z",
        "interval": {
          "days": 1
        },
        "name": "Layer 1",
        "restrictions": [
          {
            "end_day": "friday",
            "end_time": "17:00:00",
            "start_day": "monday",
            "start_time": "09:00:00"
          }
        ],
        "rotation_start": "2025-02-01T00:00:00Z"
      },
      "id": "00000000-0000-0000-0000-000000000001",
      "relationships": {
        "members": {
          "data": [
            {
              "id": "00000000-0000-0000-0000-000000000002",
              "type": "members"
            }
          ]
        }
      },
      "type": "layers"
    },
    {
      "id": "00000000-0000-0000-0000-000000000002",
      "relationships": {
        "user": {
          "data": {
            "id": "00000000-aba1-0000-0000-000000000000",
            "type": "users"
          }
        }
      },
      "type": "members"
    },
    {
      "attributes": {
        "email": "foo@bar.com",
        "name": "User 1"
      },
      "id": "00000000-aba1-0000-0000-000000000000",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Create On-Call schedule returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/schedules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "layers": [
        {
          "effective_date": "2021-11-01T11:11:11+00:00",
          "end_date": "2021-11-21T11:11:11+00:00",
          "interval": {
            "days": 1
          },
          "members": [
            {
              "user": {
                "id": "string"
              }
            }
          ],
          "name": "Layer 1",
          "restrictions": [
            {
              "end_day": "friday",
              "end_time": "17:00:00",
              "start_day": "monday",
              "start_time": "09:00:00"
            }
          ],
          "rotation_start": "2021-11-06T11:11:11+00:00"
        }
      ],
      "name": "Example-On-Call",
      "time_zone": "America/New_York"
    },
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "schedules"
  }
}
EOF  

                        
```

#####  Create On-Call schedule returns "Created" response
```
// Create On-Call schedule returns "Created" response

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
	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	// there is a valid "dd_team" in the system
	DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

	body := datadogV2.ScheduleCreateRequest{
		Data: datadogV2.ScheduleCreateRequestData{
			Attributes: datadogV2.ScheduleCreateRequestDataAttributes{
				Layers: []datadogV2.ScheduleCreateRequestDataAttributesLayersItems{
					{
						EffectiveDate: time.Now().AddDate(0, 0, -10),
						EndDate:       datadog.PtrTime(time.Now().AddDate(0, 0, 10)),
						Interval: datadogV2.LayerAttributesInterval{
							Days: datadog.PtrInt32(1),
						},
						Members: []datadogV2.ScheduleRequestDataAttributesLayersItemsMembersItems{
							{
								User: &datadogV2.ScheduleRequestDataAttributesLayersItemsMembersItemsUser{
									Id: datadog.PtrString(UserDataID),
								},
							},
						},
						Name: "Layer 1",
						Restrictions: []datadogV2.TimeRestriction{
							{
								EndDay:    datadogV2.WEEKDAY_FRIDAY.Ptr(),
								EndTime:   datadog.PtrString("17:00:00"),
								StartDay:  datadogV2.WEEKDAY_MONDAY.Ptr(),
								StartTime: datadog.PtrString("09:00:00"),
							},
						},
						RotationStart: time.Now().AddDate(0, 0, -5),
					},
				},
				Name:     "Example-On-Call",
				TimeZone: "America/New_York",
			},
			Relationships: &datadogV2.ScheduleCreateRequestDataRelationships{
				Teams: &datadogV2.DataRelationshipsTeams{
					Data: []datadogV2.DataRelationshipsTeamsDataItems{
						{
							Id:   DdTeamDataID,
							Type: datadogV2.DATARELATIONSHIPSTEAMSDATAITEMSTYPE_TEAMS,
						},
					},
				},
			},
			Type: datadogV2.SCHEDULECREATEREQUESTDATATYPE_SCHEDULES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.CreateOnCallSchedule(ctx, body, *datadogV2.NewCreateOnCallScheduleOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.CreateOnCallSchedule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.CreateOnCallSchedule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create On-Call schedule returns "Created" response
```
// Create On-Call schedule returns "Created" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.DataRelationshipsTeams;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItems;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItemsType;
import com.datadog.api.client.v2.model.LayerAttributesInterval;
import com.datadog.api.client.v2.model.Schedule;
import com.datadog.api.client.v2.model.ScheduleCreateRequest;
import com.datadog.api.client.v2.model.ScheduleCreateRequestData;
import com.datadog.api.client.v2.model.ScheduleCreateRequestDataAttributes;
import com.datadog.api.client.v2.model.ScheduleCreateRequestDataAttributesLayersItems;
import com.datadog.api.client.v2.model.ScheduleCreateRequestDataRelationships;
import com.datadog.api.client.v2.model.ScheduleCreateRequestDataType;
import com.datadog.api.client.v2.model.ScheduleRequestDataAttributesLayersItemsMembersItems;
import com.datadog.api.client.v2.model.ScheduleRequestDataAttributesLayersItemsMembersItemsUser;
import com.datadog.api.client.v2.model.TimeRestriction;
import com.datadog.api.client.v2.model.Weekday;
import java.time.OffsetDateTime;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    ScheduleCreateRequest body =
        new ScheduleCreateRequest()
            .data(
                new ScheduleCreateRequestData()
                    .attributes(
                        new ScheduleCreateRequestDataAttributes()
                            .layers(
                                Collections.singletonList(
                                    new ScheduleCreateRequestDataAttributesLayersItems()
                                        .effectiveDate(OffsetDateTime.now().plusDays(-10))
                                        .endDate(OffsetDateTime.now().plusDays(10))
                                        .interval(new LayerAttributesInterval().days(1))
                                        .members(
                                            Collections.singletonList(
                                                new ScheduleRequestDataAttributesLayersItemsMembersItems()
                                                    .user(
                                                        new ScheduleRequestDataAttributesLayersItemsMembersItemsUser()
                                                            .id(USER_DATA_ID))))
                                        .name("Layer 1")
                                        .restrictions(
                                            Collections.singletonList(
                                                new TimeRestriction()
                                                    .endDay(Weekday.FRIDAY)
                                                    .endTime("17:00:00")
                                                    .startDay(Weekday.MONDAY)
                                                    .startTime("09:00:00")))
                                        .rotationStart(OffsetDateTime.now().plusDays(-5))))
                            .name("Example-On-Call")
                            .timeZone("America/New_York"))
                    .relationships(
                        new ScheduleCreateRequestDataRelationships()
                            .teams(
                                new DataRelationshipsTeams()
                                    .data(
                                        Collections.singletonList(
                                            new DataRelationshipsTeamsDataItems()
                                                .id(DD_TEAM_DATA_ID)
                                                .type(DataRelationshipsTeamsDataItemsType.TEAMS)))))
                    .type(ScheduleCreateRequestDataType.SCHEDULES));

    try {
      Schedule result = apiInstance.createOnCallSchedule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#createOnCallSchedule");
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

#####  Create On-Call schedule returns "Created" response
```
"""
Create On-Call schedule returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams
from datadog_api_client.v2.model.data_relationships_teams_data_items import DataRelationshipsTeamsDataItems
from datadog_api_client.v2.model.data_relationships_teams_data_items_type import DataRelationshipsTeamsDataItemsType
from datadog_api_client.v2.model.layer_attributes_interval import LayerAttributesInterval
from datadog_api_client.v2.model.schedule_create_request import ScheduleCreateRequest
from datadog_api_client.v2.model.schedule_create_request_data import ScheduleCreateRequestData
from datadog_api_client.v2.model.schedule_create_request_data_attributes import ScheduleCreateRequestDataAttributes
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items import (
    ScheduleCreateRequestDataAttributesLayersItems,
)
from datadog_api_client.v2.model.schedule_create_request_data_relationships import (
    ScheduleCreateRequestDataRelationships,
)
from datadog_api_client.v2.model.schedule_create_request_data_type import ScheduleCreateRequestDataType
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items import (
    ScheduleRequestDataAttributesLayersItemsMembersItems,
)
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items_user import (
    ScheduleRequestDataAttributesLayersItemsMembersItemsUser,
)
from datadog_api_client.v2.model.time_restriction import TimeRestriction
from datadog_api_client.v2.model.weekday import Weekday

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = ScheduleCreateRequest(
    data=ScheduleCreateRequestData(
        attributes=ScheduleCreateRequestDataAttributes(
            layers=[
                ScheduleCreateRequestDataAttributesLayersItems(
                    effective_date=(datetime.now() + relativedelta(days=-10)),
                    end_date=(datetime.now() + relativedelta(days=10)),
                    interval=LayerAttributesInterval(
                        days=1,
                    ),
                    members=[
                        ScheduleRequestDataAttributesLayersItemsMembersItems(
                            user=ScheduleRequestDataAttributesLayersItemsMembersItemsUser(
                                id=USER_DATA_ID,
                            ),
                        ),
                    ],
                    name="Layer 1",
                    restrictions=[
                        TimeRestriction(
                            end_day=Weekday.FRIDAY,
                            end_time="17:00:00",
                            start_day=Weekday.MONDAY,
                            start_time="09:00:00",
                        ),
                    ],
                    rotation_start=(datetime.now() + relativedelta(days=-5)),
                ),
            ],
            name="Example-On-Call",
            time_zone="America/New_York",
        ),
        relationships=ScheduleCreateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=ScheduleCreateRequestDataType.SCHEDULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_on_call_schedule(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create On-Call schedule returns "Created" response
```
# Create On-Call schedule returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::ScheduleCreateRequest.new({
  data: DatadogAPIClient::V2::ScheduleCreateRequestData.new({
    attributes: DatadogAPIClient::V2::ScheduleCreateRequestDataAttributes.new({
      layers: [
        DatadogAPIClient::V2::ScheduleCreateRequestDataAttributesLayersItems.new({
          effective_date: (Time.now + -10 * 86400),
          end_date: (Time.now + 10 * 86400),
          interval: DatadogAPIClient::V2::LayerAttributesInterval.new({
            days: 1,
          }),
          members: [
            DatadogAPIClient::V2::ScheduleRequestDataAttributesLayersItemsMembersItems.new({
              user: DatadogAPIClient::V2::ScheduleRequestDataAttributesLayersItemsMembersItemsUser.new({
                id: USER_DATA_ID,
              }),
            }),
          ],
          name: "Layer 1",
          restrictions: [
            DatadogAPIClient::V2::TimeRestriction.new({
              end_day: DatadogAPIClient::V2::Weekday::FRIDAY,
              end_time: "17:00:00",
              start_day: DatadogAPIClient::V2::Weekday::MONDAY,
              start_time: "09:00:00",
            }),
          ],
          rotation_start: (Time.now + -5 * 86400),
        }),
      ],
      name: "Example-On-Call",
      time_zone: "America/New_York",
    }),
    relationships: DatadogAPIClient::V2::ScheduleCreateRequestDataRelationships.new({
      teams: DatadogAPIClient::V2::DataRelationshipsTeams.new({
        data: [
          DatadogAPIClient::V2::DataRelationshipsTeamsDataItems.new({
            id: DD_TEAM_DATA_ID,
            type: DatadogAPIClient::V2::DataRelationshipsTeamsDataItemsType::TEAMS,
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::ScheduleCreateRequestDataType::SCHEDULES,
  }),
})
p api_instance.create_on_call_schedule(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create On-Call schedule returns "Created" response
```
// Create On-Call schedule returns "Created" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::CreateOnCallScheduleOptionalParams;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;
use datadog_api_client::datadogV2::model::DataRelationshipsTeams;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItems;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItemsType;
use datadog_api_client::datadogV2::model::LayerAttributesInterval;
use datadog_api_client::datadogV2::model::ScheduleCreateRequest;
use datadog_api_client::datadogV2::model::ScheduleCreateRequestData;
use datadog_api_client::datadogV2::model::ScheduleCreateRequestDataAttributes;
use datadog_api_client::datadogV2::model::ScheduleCreateRequestDataAttributesLayersItems;
use datadog_api_client::datadogV2::model::ScheduleCreateRequestDataRelationships;
use datadog_api_client::datadogV2::model::ScheduleCreateRequestDataType;
use datadog_api_client::datadogV2::model::ScheduleRequestDataAttributesLayersItemsMembersItems;
use datadog_api_client::datadogV2::model::ScheduleRequestDataAttributesLayersItemsMembersItemsUser;
use datadog_api_client::datadogV2::model::TimeRestriction;
use datadog_api_client::datadogV2::model::Weekday;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();

    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = ScheduleCreateRequest::new(
        ScheduleCreateRequestData::new(
            ScheduleCreateRequestDataAttributes::new(
                vec![ScheduleCreateRequestDataAttributesLayersItems::new(
                    DateTime::parse_from_rfc3339("2021-11-01T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                    LayerAttributesInterval::new().days(1),
                    vec![
                        ScheduleRequestDataAttributesLayersItemsMembersItems::new().user(
                            ScheduleRequestDataAttributesLayersItemsMembersItemsUser::new()
                                .id(user_data_id.clone()),
                        ),
                    ],
                    "Layer 1".to_string(),
                    DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .end_date(
                    DateTime::parse_from_rfc3339("2021-11-21T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .restrictions(vec![TimeRestriction::new()
                    .end_day(Weekday::FRIDAY)
                    .end_time("17:00:00".to_string())
                    .start_day(Weekday::MONDAY)
                    .start_time("09:00:00".to_string())])],
                "Example-On-Call".to_string(),
                "America/New_York".to_string(),
            ),
            ScheduleCreateRequestDataType::SCHEDULES,
        )
        .relationships(ScheduleCreateRequestDataRelationships::new().teams(
            DataRelationshipsTeams::new().data(vec![DataRelationshipsTeamsDataItems::new(
                dd_team_data_id.clone(),
                DataRelationshipsTeamsDataItemsType::TEAMS,
            )]),
        )),
    );
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .create_on_call_schedule(body, CreateOnCallScheduleOptionalParams::default())
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

#####  Create On-Call schedule returns "Created" response
```
/**
 * Create On-Call schedule returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.OnCallApiCreateOnCallScheduleRequest = {
  body: {
    data: {
      attributes: {
        layers: [
          {
            effectiveDate: new Date(new Date().getTime() + -10 * 86400 * 1000),
            endDate: new Date(new Date().getTime() + 10 * 86400 * 1000),
            interval: {
              days: 1,
            },
            members: [
              {
                user: {
                  id: USER_DATA_ID,
                },
              },
            ],
            name: "Layer 1",
            restrictions: [
              {
                endDay: "friday",
                endTime: "17:00:00",
                startDay: "monday",
                startTime: "09:00:00",
              },
            ],
            rotationStart: new Date(new Date().getTime() + -5 * 86400 * 1000),
          },
        ],
        name: "Example-On-Call",
        timeZone: "America/New_York",
      },
      relationships: {
        teams: {
          data: [
            {
              id: DD_TEAM_DATA_ID,
              type: "teams",
            },
          ],
        },
      },
      type: "schedules",
    },
  },
};

apiInstance
  .createOnCallSchedule(params)
  .then((data: v2.Schedule) => {
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
## [Get On-Call schedule](https://docs.datadoghq.com/api/latest/on-call/#get-on-call-schedule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#get-on-call-schedule-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.ap2.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.datadoghq.eu/api/v2/on-call/schedules/{schedule_id}https://api.ddog-gov.com/api/v2/on-call/schedules/{schedule_id}https://api.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.us3.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.us5.datadoghq.com/api/v2/on-call/schedules/{schedule_id}
### Overview
Get an On-Call schedule This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
schedule_id [_required_]
string
The ID of the schedule
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `teams`, `layers`, `layers.members`, `layers.members.user`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallSchedule-200-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallSchedule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallSchedule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallSchedule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallSchedule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Top-level container for a schedule object, including both the `data` payload and any related `included` resources (such as teams, layers, or members).
Field
Type
Description
data
object
Represents the primary data object for a schedule, linking attributes and relationships.
attributes
object
Provides core properties of a schedule object such as its name and time zone.
name
string
A short name for the schedule.
time_zone
string
The time zone in which this schedule operates.
id
string
The schedule's unique identifier.
relationships
object
Groups the relationships for a schedule object, referencing layers and teams.
layers
object
Associates layers with this schedule in a data structure.
data
[object]
An array of layer references for this schedule.
id [_required_]
string
The unique identifier of the layer in this relationship.
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
included
[ <oneOf>]
Any additional resources related to this schedule, such as teams and layers.
Option 1
object
Provides a reference to a team, including ID, type, and basic attributes/relationships.
attributes
object
Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
avatar
string
URL or reference for the team's avatar (if available).
description
string
A short text describing the team.
handle
string
A unique handle/slug for the team.
name
string
The full, human-readable name of the team.
id
string
The team's unique identifier.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
Option 2
object
Encapsulates a layer resource, holding attributes like rotation details, plus relationships to the members covering that layer.
attributes
object
Describes key properties of a Layer, including rotation details, name, start/end times, and any restrictions.
effective_date
date-time
When the layer becomes active (ISO 8601).
end_date
date-time
When the layer ceases to be active (ISO 8601).
interval
object
Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
days
int32
The number of days in each rotation cycle.
seconds
int64
Any additional seconds for the rotation cycle (up to 30 days).
name
string
The name of this layer.
restrictions
[object]
An optional list of time restrictions for when this layer is in effect.
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
rotation_start
date-time
The date/time when the rotation starts (ISO 8601).
time_zone
string
The time zone for this layer.
id
string
A unique identifier for this layer.
relationships
object
Holds references to objects related to the Layer entity, such as its members.
members
object
Holds an array of references to the members of a Layer, each containing member IDs.
data
[object]
The list of members who belong to this layer.
id [_required_]
string
The unique user ID of the layer member.
type [_required_]
enum
Members resource type. Allowed enum values: `members`
default: `members`
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
Option 3
object
Represents a single member entry in a schedule, referencing a specific user.
id
string
The unique identifier for this schedule member.
relationships
object
Defines relationships for a schedule member, primarily referencing a single user.
user
object
Wraps the user data reference for a schedule member.
data [_required_]
object
Points to the user data associated with this schedule member, including an ID and type.
id [_required_]
string
The user's unique identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Schedule Members resource type. Allowed enum values: `members`
default: `members`
Option 4
object
Represents a user object in the context of a schedule, including their `id`, type, and basic attributes.
attributes
object
Provides basic user information for a schedule, including a name and email address.
email
string
The user's email address.
name
string
The user's name.
status
enum
The user's status. Allowed enum values: `active,deactivated,pending`
id
string
The unique user identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "name": "On-Call Schedule",
      "time_zone": "America/New_York"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "layers": {
        "data": [
          {
            "id": "00000000-0000-0000-0000-000000000001",
            "type": "layers"
          }
        ]
      },
      "teams": {
        "data": [
          {
            "id": "00000000-da3a-0000-0000-000000000000",
            "type": "teams"
          }
        ]
      }
    },
    "type": "schedules"
  },
  "included": [
    {
      "attributes": {
        "avatar": "",
        "description": "Team 1 description",
        "handle": "team1",
        "name": "Team 1"
      },
      "id": "00000000-da3a-0000-0000-000000000000",
      "type": "teams"
    },
    {
      "attributes": {
        "effective_date": "2025-02-03T05:00:00Z",
        "end_date": "2025-12-31T00:00:00Z",
        "interval": {
          "days": 1
        },
        "name": "Layer 1",
        "restrictions": [
          {
            "end_day": "friday",
            "end_time": "17:00:00",
            "start_day": "monday",
            "start_time": "09:00:00"
          }
        ],
        "rotation_start": "2025-02-01T00:00:00Z"
      },
      "id": "00000000-0000-0000-0000-000000000001",
      "relationships": {
        "members": {
          "data": [
            {
              "id": "00000000-0000-0000-0000-000000000002",
              "type": "members"
            }
          ]
        }
      },
      "type": "layers"
    },
    {
      "id": "00000000-0000-0000-0000-000000000002",
      "relationships": {
        "user": {
          "data": {
            "id": "00000000-aba1-0000-0000-000000000000",
            "type": "users"
          }
        }
      },
      "type": "members"
    },
    {
      "attributes": {
        "email": "foo@bar.com",
        "name": "User 1"
      },
      "id": "00000000-aba1-0000-0000-000000000000",
      "type": "users"
    }
  ]
}
```

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Get On-Call schedule
Copy
```
                  # Path parameters  
export schedule_id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/schedules/${schedule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get On-Call schedule
```
"""
Get On-Call schedule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_on_call_schedule(
        schedule_id=SCHEDULE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get On-Call schedule
```
# Get On-Call schedule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = ENV["SCHEDULE_DATA_ID"]
p api_instance.get_on_call_schedule(SCHEDULE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get On-Call schedule
```
// Get On-Call schedule returns "OK" response

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
	// there is a valid "schedule" in the system
	ScheduleDataID := os.Getenv("SCHEDULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.GetOnCallSchedule(ctx, ScheduleDataID, *datadogV2.NewGetOnCallScheduleOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.GetOnCallSchedule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.GetOnCallSchedule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get On-Call schedule
```
// Get On-Call schedule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.Schedule;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "schedule" in the system
    String SCHEDULE_DATA_ID = System.getenv("SCHEDULE_DATA_ID");

    try {
      Schedule result = apiInstance.getOnCallSchedule(SCHEDULE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#getOnCallSchedule");
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

#####  Get On-Call schedule
```
// Get On-Call schedule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::GetOnCallScheduleOptionalParams;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "schedule" in the system
    let schedule_data_id = std::env::var("SCHEDULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .get_on_call_schedule(
            schedule_data_id.clone(),
            GetOnCallScheduleOptionalParams::default(),
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

#####  Get On-Call schedule
```
/**
 * Get On-Call schedule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "schedule" in the system
const SCHEDULE_DATA_ID = process.env.SCHEDULE_DATA_ID as string;

const params: v2.OnCallApiGetOnCallScheduleRequest = {
  scheduleId: SCHEDULE_DATA_ID,
};

apiInstance
  .getOnCallSchedule(params)
  .then((data: v2.Schedule) => {
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
## [Delete On-Call schedule](https://docs.datadoghq.com/api/latest/on-call/#delete-on-call-schedule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#delete-on-call-schedule-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.ap2.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.datadoghq.eu/api/v2/on-call/schedules/{schedule_id}https://api.ddog-gov.com/api/v2/on-call/schedules/{schedule_id}https://api.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.us3.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.us5.datadoghq.com/api/v2/on-call/schedules/{schedule_id}
### Overview
Delete an On-Call schedule This endpoint requires the `on_call_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
schedule_id [_required_]
string
The ID of the schedule
### Response
  * [204](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallSchedule-204-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallSchedule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallSchedule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallSchedule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallSchedule-429-v2)


No Content
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Delete On-Call schedule
Copy
```
                  # Path parameters  
export schedule_id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/schedules/${schedule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete On-Call schedule
```
"""
Delete On-Call schedule returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    api_instance.delete_on_call_schedule(
        schedule_id=SCHEDULE_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete On-Call schedule
```
# Delete On-Call schedule returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = ENV["SCHEDULE_DATA_ID"]
api_instance.delete_on_call_schedule(SCHEDULE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete On-Call schedule
```
// Delete On-Call schedule returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "schedule" in the system
	ScheduleDataID := os.Getenv("SCHEDULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	r, err := api.DeleteOnCallSchedule(ctx, ScheduleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.DeleteOnCallSchedule`: %v\n", err)
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

#####  Delete On-Call schedule
```
// Delete On-Call schedule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "schedule" in the system
    String SCHEDULE_DATA_ID = System.getenv("SCHEDULE_DATA_ID");

    try {
      apiInstance.deleteOnCallSchedule(SCHEDULE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#deleteOnCallSchedule");
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

#####  Delete On-Call schedule
```
// Delete On-Call schedule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "schedule" in the system
    let schedule_data_id = std::env::var("SCHEDULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api.delete_on_call_schedule(schedule_data_id.clone()).await;
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

#####  Delete On-Call schedule
```
/**
 * Delete On-Call schedule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "schedule" in the system
const SCHEDULE_DATA_ID = process.env.SCHEDULE_DATA_ID as string;

const params: v2.OnCallApiDeleteOnCallScheduleRequest = {
  scheduleId: SCHEDULE_DATA_ID,
};

apiInstance
  .deleteOnCallSchedule(params)
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
## [Update On-Call schedule](https://docs.datadoghq.com/api/latest/on-call/#update-on-call-schedule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#update-on-call-schedule-v2)


PUT https://api.ap1.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.ap2.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.datadoghq.eu/api/v2/on-call/schedules/{schedule_id}https://api.ddog-gov.com/api/v2/on-call/schedules/{schedule_id}https://api.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.us3.datadoghq.com/api/v2/on-call/schedules/{schedule_id}https://api.us5.datadoghq.com/api/v2/on-call/schedules/{schedule_id}
### Overview
Update a new On-Call schedule This endpoint requires the `on_call_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
schedule_id [_required_]
string
The ID of the schedule
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `teams`, `layers`, `layers.members`, `layers.members.user`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data [_required_]
object
Contains all data needed to update an existing schedule, including its attributes (such as name and time zone) and any relationships to teams.
attributes [_required_]
object
Defines the updatable attributes for a schedule, such as name, time zone, and layers.
layers [_required_]
[object]
The updated list of layers (rotations) for this schedule.
effective_date [_required_]
date-time
When this updated layer takes effect (ISO 8601 format).
end_date
date-time
When this updated layer should stop being active (ISO 8601 format).
id
string
A unique identifier for the layer being updated.
interval [_required_]
object
Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
days
int32
The number of days in each rotation cycle.
seconds
int64
Any additional seconds for the rotation cycle (up to 30 days).
members [_required_]
[object]
The members assigned to this layer.
user
object
Identifies the user participating in this layer as a single object with an `id`.
id
string
The user's ID.
name [_required_]
string
The name for this layer (for example, "Secondary Coverage").
restrictions
[object]
Any time restrictions that define when this layer is active.
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
rotation_start [_required_]
date-time
The date/time at which the rotation begins (ISO 8601 format).
time_zone
string
The time zone for this layer.
name [_required_]
string
A short name for the schedule.
time_zone [_required_]
string
The time zone used when interpreting rotation times.
id [_required_]
string
The ID of the schedule to be updated.
relationships
object
Houses relationships for the schedule update, typically referencing teams.
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
```
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "attributes": {
      "layers": [
        {
          "id": "00000000-0000-0000-0000-000000000001",
          "effective_date": "2021-11-01T11:11:11+00:00",
          "end_date": "2021-11-21T11:11:11+00:00",
          "interval": {
            "seconds": 3600
          },
          "members": [
            {
              "user": {
                "id": "string"
              }
            }
          ],
          "name": "Layer 1",
          "restrictions": [
            {
              "end_day": "friday",
              "end_time": "17:00:00",
              "start_day": "monday",
              "start_time": "09:00:00"
            }
          ],
          "rotation_start": "2021-11-06T11:11:11+00:00"
        }
      ],
      "name": "Example-On-Call",
      "time_zone": "America/New_York"
    },
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "schedules"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallSchedule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallSchedule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallSchedule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallSchedule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallSchedule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallSchedule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Top-level container for a schedule object, including both the `data` payload and any related `included` resources (such as teams, layers, or members).
Field
Type
Description
data
object
Represents the primary data object for a schedule, linking attributes and relationships.
attributes
object
Provides core properties of a schedule object such as its name and time zone.
name
string
A short name for the schedule.
time_zone
string
The time zone in which this schedule operates.
id
string
The schedule's unique identifier.
relationships
object
Groups the relationships for a schedule object, referencing layers and teams.
layers
object
Associates layers with this schedule in a data structure.
data
[object]
An array of layer references for this schedule.
id [_required_]
string
The unique identifier of the layer in this relationship.
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
included
[ <oneOf>]
Any additional resources related to this schedule, such as teams and layers.
Option 1
object
Provides a reference to a team, including ID, type, and basic attributes/relationships.
attributes
object
Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
avatar
string
URL or reference for the team's avatar (if available).
description
string
A short text describing the team.
handle
string
A unique handle/slug for the team.
name
string
The full, human-readable name of the team.
id
string
The team's unique identifier.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
Option 2
object
Encapsulates a layer resource, holding attributes like rotation details, plus relationships to the members covering that layer.
attributes
object
Describes key properties of a Layer, including rotation details, name, start/end times, and any restrictions.
effective_date
date-time
When the layer becomes active (ISO 8601).
end_date
date-time
When the layer ceases to be active (ISO 8601).
interval
object
Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
days
int32
The number of days in each rotation cycle.
seconds
int64
Any additional seconds for the rotation cycle (up to 30 days).
name
string
The name of this layer.
restrictions
[object]
An optional list of time restrictions for when this layer is in effect.
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
rotation_start
date-time
The date/time when the rotation starts (ISO 8601).
time_zone
string
The time zone for this layer.
id
string
A unique identifier for this layer.
relationships
object
Holds references to objects related to the Layer entity, such as its members.
members
object
Holds an array of references to the members of a Layer, each containing member IDs.
data
[object]
The list of members who belong to this layer.
id [_required_]
string
The unique user ID of the layer member.
type [_required_]
enum
Members resource type. Allowed enum values: `members`
default: `members`
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
Option 3
object
Represents a single member entry in a schedule, referencing a specific user.
id
string
The unique identifier for this schedule member.
relationships
object
Defines relationships for a schedule member, primarily referencing a single user.
user
object
Wraps the user data reference for a schedule member.
data [_required_]
object
Points to the user data associated with this schedule member, including an ID and type.
id [_required_]
string
The user's unique identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Schedule Members resource type. Allowed enum values: `members`
default: `members`
Option 4
object
Represents a user object in the context of a schedule, including their `id`, type, and basic attributes.
attributes
object
Provides basic user information for a schedule, including a name and email address.
email
string
The user's email address.
name
string
The user's name.
status
enum
The user's status. Allowed enum values: `active,deactivated,pending`
id
string
The unique user identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "name": "On-Call Schedule",
      "time_zone": "America/New_York"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "layers": {
        "data": [
          {
            "id": "00000000-0000-0000-0000-000000000001",
            "type": "layers"
          }
        ]
      },
      "teams": {
        "data": [
          {
            "id": "00000000-da3a-0000-0000-000000000000",
            "type": "teams"
          }
        ]
      }
    },
    "type": "schedules"
  },
  "included": [
    {
      "attributes": {
        "avatar": "",
        "description": "Team 1 description",
        "handle": "team1",
        "name": "Team 1"
      },
      "id": "00000000-da3a-0000-0000-000000000000",
      "type": "teams"
    },
    {
      "attributes": {
        "effective_date": "2025-02-03T05:00:00Z",
        "end_date": "2025-12-31T00:00:00Z",
        "interval": {
          "days": 1
        },
        "name": "Layer 1",
        "restrictions": [
          {
            "end_day": "friday",
            "end_time": "17:00:00",
            "start_day": "monday",
            "start_time": "09:00:00"
          }
        ],
        "rotation_start": "2025-02-01T00:00:00Z"
      },
      "id": "00000000-0000-0000-0000-000000000001",
      "relationships": {
        "members": {
          "data": [
            {
              "id": "00000000-0000-0000-0000-000000000002",
              "type": "members"
            }
          ]
        }
      },
      "type": "layers"
    },
    {
      "id": "00000000-0000-0000-0000-000000000002",
      "relationships": {
        "user": {
          "data": {
            "id": "00000000-aba1-0000-0000-000000000000",
            "type": "users"
          }
        }
      },
      "type": "members"
    },
    {
      "attributes": {
        "email": "foo@bar.com",
        "name": "User 1"
      },
      "id": "00000000-aba1-0000-0000-000000000000",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Update On-Call schedule returns "OK" response
Copy
```
                          # Path parameters  
export schedule_id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/schedules/${schedule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "attributes": {
      "layers": [
        {
          "id": "00000000-0000-0000-0000-000000000001",
          "effective_date": "2021-11-01T11:11:11+00:00",
          "end_date": "2021-11-21T11:11:11+00:00",
          "interval": {
            "seconds": 3600
          },
          "members": [
            {
              "user": {
                "id": "string"
              }
            }
          ],
          "name": "Layer 1",
          "restrictions": [
            {
              "end_day": "friday",
              "end_time": "17:00:00",
              "start_day": "monday",
              "start_time": "09:00:00"
            }
          ],
          "rotation_start": "2021-11-06T11:11:11+00:00"
        }
      ],
      "name": "Example-On-Call",
      "time_zone": "America/New_York"
    },
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "schedules"
  }
}
EOF  

                        
```

#####  Update On-Call schedule returns "OK" response
```
// Update On-Call schedule returns "OK" response

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
	// there is a valid "schedule" in the system
	ScheduleDataID := os.Getenv("SCHEDULE_DATA_ID")
	ScheduleDataRelationshipsLayersData0ID := os.Getenv("SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID")

	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	// there is a valid "dd_team" in the system
	DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

	body := datadogV2.ScheduleUpdateRequest{
		Data: datadogV2.ScheduleUpdateRequestData{
			Id: ScheduleDataID,
			Attributes: datadogV2.ScheduleUpdateRequestDataAttributes{
				Layers: []datadogV2.ScheduleUpdateRequestDataAttributesLayersItems{
					{
						Id:            datadog.PtrString(ScheduleDataRelationshipsLayersData0ID),
						EffectiveDate: time.Now().AddDate(0, 0, -10),
						EndDate:       datadog.PtrTime(time.Now().AddDate(0, 0, 10)),
						Interval: datadogV2.LayerAttributesInterval{
							Seconds: datadog.PtrInt64(3600),
						},
						Members: []datadogV2.ScheduleRequestDataAttributesLayersItemsMembersItems{
							{
								User: &datadogV2.ScheduleRequestDataAttributesLayersItemsMembersItemsUser{
									Id: datadog.PtrString(UserDataID),
								},
							},
						},
						Name: "Layer 1",
						Restrictions: []datadogV2.TimeRestriction{
							{
								EndDay:    datadogV2.WEEKDAY_FRIDAY.Ptr(),
								EndTime:   datadog.PtrString("17:00:00"),
								StartDay:  datadogV2.WEEKDAY_MONDAY.Ptr(),
								StartTime: datadog.PtrString("09:00:00"),
							},
						},
						RotationStart: time.Now().AddDate(0, 0, -5),
					},
				},
				Name:     "Example-On-Call",
				TimeZone: "America/New_York",
			},
			Relationships: &datadogV2.ScheduleUpdateRequestDataRelationships{
				Teams: &datadogV2.DataRelationshipsTeams{
					Data: []datadogV2.DataRelationshipsTeamsDataItems{
						{
							Id:   DdTeamDataID,
							Type: datadogV2.DATARELATIONSHIPSTEAMSDATAITEMSTYPE_TEAMS,
						},
					},
				},
			},
			Type: datadogV2.SCHEDULEUPDATEREQUESTDATATYPE_SCHEDULES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.UpdateOnCallSchedule(ctx, ScheduleDataID, body, *datadogV2.NewUpdateOnCallScheduleOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.UpdateOnCallSchedule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.UpdateOnCallSchedule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update On-Call schedule returns "OK" response
```
// Update On-Call schedule returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.DataRelationshipsTeams;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItems;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItemsType;
import com.datadog.api.client.v2.model.LayerAttributesInterval;
import com.datadog.api.client.v2.model.Schedule;
import com.datadog.api.client.v2.model.ScheduleRequestDataAttributesLayersItemsMembersItems;
import com.datadog.api.client.v2.model.ScheduleRequestDataAttributesLayersItemsMembersItemsUser;
import com.datadog.api.client.v2.model.ScheduleUpdateRequest;
import com.datadog.api.client.v2.model.ScheduleUpdateRequestData;
import com.datadog.api.client.v2.model.ScheduleUpdateRequestDataAttributes;
import com.datadog.api.client.v2.model.ScheduleUpdateRequestDataAttributesLayersItems;
import com.datadog.api.client.v2.model.ScheduleUpdateRequestDataRelationships;
import com.datadog.api.client.v2.model.ScheduleUpdateRequestDataType;
import com.datadog.api.client.v2.model.TimeRestriction;
import com.datadog.api.client.v2.model.Weekday;
import java.time.OffsetDateTime;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "schedule" in the system
    String SCHEDULE_DATA_ID = System.getenv("SCHEDULE_DATA_ID");
    String SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID =
        System.getenv("SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID");

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    ScheduleUpdateRequest body =
        new ScheduleUpdateRequest()
            .data(
                new ScheduleUpdateRequestData()
                    .id(SCHEDULE_DATA_ID)
                    .attributes(
                        new ScheduleUpdateRequestDataAttributes()
                            .layers(
                                Collections.singletonList(
                                    new ScheduleUpdateRequestDataAttributesLayersItems()
                                        .id(SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID)
                                        .effectiveDate(OffsetDateTime.now().plusDays(-10))
                                        .endDate(OffsetDateTime.now().plusDays(10))
                                        .interval(new LayerAttributesInterval().seconds(3600L))
                                        .members(
                                            Collections.singletonList(
                                                new ScheduleRequestDataAttributesLayersItemsMembersItems()
                                                    .user(
                                                        new ScheduleRequestDataAttributesLayersItemsMembersItemsUser()
                                                            .id(USER_DATA_ID))))
                                        .name("Layer 1")
                                        .restrictions(
                                            Collections.singletonList(
                                                new TimeRestriction()
                                                    .endDay(Weekday.FRIDAY)
                                                    .endTime("17:00:00")
                                                    .startDay(Weekday.MONDAY)
                                                    .startTime("09:00:00")))
                                        .rotationStart(OffsetDateTime.now().plusDays(-5))))
                            .name("Example-On-Call")
                            .timeZone("America/New_York"))
                    .relationships(
                        new ScheduleUpdateRequestDataRelationships()
                            .teams(
                                new DataRelationshipsTeams()
                                    .data(
                                        Collections.singletonList(
                                            new DataRelationshipsTeamsDataItems()
                                                .id(DD_TEAM_DATA_ID)
                                                .type(DataRelationshipsTeamsDataItemsType.TEAMS)))))
                    .type(ScheduleUpdateRequestDataType.SCHEDULES));

    try {
      Schedule result = apiInstance.updateOnCallSchedule(SCHEDULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#updateOnCallSchedule");
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

#####  Update On-Call schedule returns "OK" response
```
"""
Update On-Call schedule returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams
from datadog_api_client.v2.model.data_relationships_teams_data_items import DataRelationshipsTeamsDataItems
from datadog_api_client.v2.model.data_relationships_teams_data_items_type import DataRelationshipsTeamsDataItemsType
from datadog_api_client.v2.model.layer_attributes_interval import LayerAttributesInterval
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items import (
    ScheduleRequestDataAttributesLayersItemsMembersItems,
)
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items_user import (
    ScheduleRequestDataAttributesLayersItemsMembersItemsUser,
)
from datadog_api_client.v2.model.schedule_update_request import ScheduleUpdateRequest
from datadog_api_client.v2.model.schedule_update_request_data import ScheduleUpdateRequestData
from datadog_api_client.v2.model.schedule_update_request_data_attributes import ScheduleUpdateRequestDataAttributes
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items import (
    ScheduleUpdateRequestDataAttributesLayersItems,
)
from datadog_api_client.v2.model.schedule_update_request_data_relationships import (
    ScheduleUpdateRequestDataRelationships,
)
from datadog_api_client.v2.model.schedule_update_request_data_type import ScheduleUpdateRequestDataType
from datadog_api_client.v2.model.time_restriction import TimeRestriction
from datadog_api_client.v2.model.weekday import Weekday

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]
SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID = environ["SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = ScheduleUpdateRequest(
    data=ScheduleUpdateRequestData(
        id=SCHEDULE_DATA_ID,
        attributes=ScheduleUpdateRequestDataAttributes(
            layers=[
                ScheduleUpdateRequestDataAttributesLayersItems(
                    id=SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID,
                    effective_date=(datetime.now() + relativedelta(days=-10)),
                    end_date=(datetime.now() + relativedelta(days=10)),
                    interval=LayerAttributesInterval(
                        seconds=3600,
                    ),
                    members=[
                        ScheduleRequestDataAttributesLayersItemsMembersItems(
                            user=ScheduleRequestDataAttributesLayersItemsMembersItemsUser(
                                id=USER_DATA_ID,
                            ),
                        ),
                    ],
                    name="Layer 1",
                    restrictions=[
                        TimeRestriction(
                            end_day=Weekday.FRIDAY,
                            end_time="17:00:00",
                            start_day=Weekday.MONDAY,
                            start_time="09:00:00",
                        ),
                    ],
                    rotation_start=(datetime.now() + relativedelta(days=-5)),
                ),
            ],
            name="Example-On-Call",
            time_zone="America/New_York",
        ),
        relationships=ScheduleUpdateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=ScheduleUpdateRequestDataType.SCHEDULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.update_on_call_schedule(schedule_id=SCHEDULE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update On-Call schedule returns "OK" response
```
# Update On-Call schedule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = ENV["SCHEDULE_DATA_ID"]
SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID = ENV["SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID"]

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::ScheduleUpdateRequest.new({
  data: DatadogAPIClient::V2::ScheduleUpdateRequestData.new({
    id: SCHEDULE_DATA_ID,
    attributes: DatadogAPIClient::V2::ScheduleUpdateRequestDataAttributes.new({
      layers: [
        DatadogAPIClient::V2::ScheduleUpdateRequestDataAttributesLayersItems.new({
          id: SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID,
          effective_date: (Time.now + -10 * 86400),
          end_date: (Time.now + 10 * 86400),
          interval: DatadogAPIClient::V2::LayerAttributesInterval.new({
            seconds: 3600,
          }),
          members: [
            DatadogAPIClient::V2::ScheduleRequestDataAttributesLayersItemsMembersItems.new({
              user: DatadogAPIClient::V2::ScheduleRequestDataAttributesLayersItemsMembersItemsUser.new({
                id: USER_DATA_ID,
              }),
            }),
          ],
          name: "Layer 1",
          restrictions: [
            DatadogAPIClient::V2::TimeRestriction.new({
              end_day: DatadogAPIClient::V2::Weekday::FRIDAY,
              end_time: "17:00:00",
              start_day: DatadogAPIClient::V2::Weekday::MONDAY,
              start_time: "09:00:00",
            }),
          ],
          rotation_start: (Time.now + -5 * 86400),
        }),
      ],
      name: "Example-On-Call",
      time_zone: "America/New_York",
    }),
    relationships: DatadogAPIClient::V2::ScheduleUpdateRequestDataRelationships.new({
      teams: DatadogAPIClient::V2::DataRelationshipsTeams.new({
        data: [
          DatadogAPIClient::V2::DataRelationshipsTeamsDataItems.new({
            id: DD_TEAM_DATA_ID,
            type: DatadogAPIClient::V2::DataRelationshipsTeamsDataItemsType::TEAMS,
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::ScheduleUpdateRequestDataType::SCHEDULES,
  }),
})
p api_instance.update_on_call_schedule(SCHEDULE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update On-Call schedule returns "OK" response
```
// Update On-Call schedule returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;
use datadog_api_client::datadogV2::api_on_call::UpdateOnCallScheduleOptionalParams;
use datadog_api_client::datadogV2::model::DataRelationshipsTeams;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItems;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItemsType;
use datadog_api_client::datadogV2::model::LayerAttributesInterval;
use datadog_api_client::datadogV2::model::ScheduleRequestDataAttributesLayersItemsMembersItems;
use datadog_api_client::datadogV2::model::ScheduleRequestDataAttributesLayersItemsMembersItemsUser;
use datadog_api_client::datadogV2::model::ScheduleUpdateRequest;
use datadog_api_client::datadogV2::model::ScheduleUpdateRequestData;
use datadog_api_client::datadogV2::model::ScheduleUpdateRequestDataAttributes;
use datadog_api_client::datadogV2::model::ScheduleUpdateRequestDataAttributesLayersItems;
use datadog_api_client::datadogV2::model::ScheduleUpdateRequestDataRelationships;
use datadog_api_client::datadogV2::model::ScheduleUpdateRequestDataType;
use datadog_api_client::datadogV2::model::TimeRestriction;
use datadog_api_client::datadogV2::model::Weekday;

#[tokio::main]
async fn main() {
    // there is a valid "schedule" in the system
    let schedule_data_id = std::env::var("SCHEDULE_DATA_ID").unwrap();
    let schedule_data_relationships_layers_data_0_id =
        std::env::var("SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID").unwrap();

    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();

    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = ScheduleUpdateRequest::new(
        ScheduleUpdateRequestData::new(
            ScheduleUpdateRequestDataAttributes::new(
                vec![ScheduleUpdateRequestDataAttributesLayersItems::new(
                    DateTime::parse_from_rfc3339("2021-11-01T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                    LayerAttributesInterval::new().seconds(3600),
                    vec![
                        ScheduleRequestDataAttributesLayersItemsMembersItems::new().user(
                            ScheduleRequestDataAttributesLayersItemsMembersItemsUser::new()
                                .id(user_data_id.clone()),
                        ),
                    ],
                    "Layer 1".to_string(),
                    DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .end_date(
                    DateTime::parse_from_rfc3339("2021-11-21T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .id(schedule_data_relationships_layers_data_0_id.clone())
                .restrictions(vec![TimeRestriction::new()
                    .end_day(Weekday::FRIDAY)
                    .end_time("17:00:00".to_string())
                    .start_day(Weekday::MONDAY)
                    .start_time("09:00:00".to_string())])],
                "Example-On-Call".to_string(),
                "America/New_York".to_string(),
            ),
            schedule_data_id.clone(),
            ScheduleUpdateRequestDataType::SCHEDULES,
        )
        .relationships(ScheduleUpdateRequestDataRelationships::new().teams(
            DataRelationshipsTeams::new().data(vec![DataRelationshipsTeamsDataItems::new(
                dd_team_data_id.clone(),
                DataRelationshipsTeamsDataItemsType::TEAMS,
            )]),
        )),
    );
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .update_on_call_schedule(
            schedule_data_id.clone(),
            body,
            UpdateOnCallScheduleOptionalParams::default(),
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

#####  Update On-Call schedule returns "OK" response
```
/**
 * Update On-Call schedule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "schedule" in the system
const SCHEDULE_DATA_ID = process.env.SCHEDULE_DATA_ID as string;
const SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID = process.env
  .SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID as string;

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.OnCallApiUpdateOnCallScheduleRequest = {
  body: {
    data: {
      id: SCHEDULE_DATA_ID,
      attributes: {
        layers: [
          {
            id: SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID,
            effectiveDate: new Date(new Date().getTime() + -10 * 86400 * 1000),
            endDate: new Date(new Date().getTime() + 10 * 86400 * 1000),
            interval: {
              seconds: 3600,
            },
            members: [
              {
                user: {
                  id: USER_DATA_ID,
                },
              },
            ],
            name: "Layer 1",
            restrictions: [
              {
                endDay: "friday",
                endTime: "17:00:00",
                startDay: "monday",
                startTime: "09:00:00",
              },
            ],
            rotationStart: new Date(new Date().getTime() + -5 * 86400 * 1000),
          },
        ],
        name: "Example-On-Call",
        timeZone: "America/New_York",
      },
      relationships: {
        teams: {
          data: [
            {
              id: DD_TEAM_DATA_ID,
              type: "teams",
            },
          ],
        },
      },
      type: "schedules",
    },
  },
  scheduleId: SCHEDULE_DATA_ID,
};

apiInstance
  .updateOnCallSchedule(params)
  .then((data: v2.Schedule) => {
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
## [Create On-Call escalation policy](https://docs.datadoghq.com/api/latest/on-call/#create-on-call-escalation-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#create-on-call-escalation-policy-v2)


POST https://api.ap1.datadoghq.com/api/v2/on-call/escalation-policieshttps://api.ap2.datadoghq.com/api/v2/on-call/escalation-policieshttps://api.datadoghq.eu/api/v2/on-call/escalation-policieshttps://api.ddog-gov.com/api/v2/on-call/escalation-policieshttps://api.datadoghq.com/api/v2/on-call/escalation-policieshttps://api.us3.datadoghq.com/api/v2/on-call/escalation-policieshttps://api.us5.datadoghq.com/api/v2/on-call/escalation-policies
### Overview
Create a new On-Call escalation policy This endpoint requires the `on_call_write` permission.
### Arguments
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `teams`, `steps`, `steps.targets`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data [_required_]
object
Represents the data for creating an escalation policy, including its attributes, relationships, and resource type.
attributes [_required_]
object
Defines the attributes for creating an escalation policy, including its description, name, resolution behavior, retries, and steps.
name [_required_]
string
Specifies the name for the new escalation policy.
resolve_page_on_policy_end
boolean
Indicates whether the page is automatically resolved when the policy ends.
retries
int64
Specifies how many times the escalation sequence is retried if there is no response.
steps [_required_]
[object]
A list of escalation steps, each defining assignment, escalation timeout, and targets for the new policy.
assignment
enum
Specifies how this escalation step will assign targets (example `default` or `round-robin`). Allowed enum values: `default,round-robin`
escalate_after_seconds
int64
Defines how many seconds to wait before escalating to the next step.
targets [_required_]
[object]
Specifies the collection of escalation targets for this step.
config
object
Configuration for an escalation target, such as schedule position.
schedule
object
Schedule-specific configuration for an escalation target.
position
enum
Specifies the position of a schedule target (example `previous`, `current`, or `next`). Allowed enum values: `previous,current,next`
id
string
Specifies the unique identifier for this target.
type
enum
Specifies the type of escalation target (example `users`, `schedules`, or `teams`). Allowed enum values: `users,schedules,teams`
relationships
object
Represents relationships in an escalation policy creation request, including references to teams.
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Indicates that the resource is of type `policies`. Allowed enum values: `policies`
default: `policies`
```
{
  "data": {
    "attributes": {
      "name": "Example-On-Call",
      "resolve_page_on_policy_end": true,
      "retries": 2,
      "steps": [
        {
          "assignment": "default",
          "escalate_after_seconds": 3600,
          "targets": [
            {
              "id": "string",
              "type": "users"
            },
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "schedules"
            },
            {
              "config": {
                "schedule": {
                  "position": "previous"
                }
              },
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "schedules"
            },
            {
              "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
              "type": "teams"
            }
          ]
        },
        {
          "assignment": "round-robin",
          "escalate_after_seconds": 3600,
          "targets": [
            {
              "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
              "type": "teams"
            }
          ]
        }
      ]
    },
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "policies"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallEscalationPolicy-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallEscalationPolicy-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallEscalationPolicy-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallEscalationPolicy-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#CreateOnCallEscalationPolicy-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Represents a complete escalation policy response, including policy data and optionally included related resources.
Field
Type
Description
data
object
Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type.
attributes
object
Defines the main attributes of an escalation policy, such as its name and behavior on policy end.
name [_required_]
string
Specifies the name of the escalation policy.
resolve_page_on_policy_end
boolean
Indicates whether the page is automatically resolved when the policy ends.
retries
int64
Specifies how many times the escalation sequence is retried if there is no response.
id
string
Specifies the unique identifier of the escalation policy.
relationships
object
Represents the relationships for an escalation policy, including references to steps and teams.
steps [_required_]
object
Defines the relationship to a collection of steps within an escalation policy. Contains an array of step data references.
data
[object]
An array of references to the steps defined in this escalation policy.
id [_required_]
string
Specifies the unique identifier for the step resource.
type [_required_]
enum
Indicates that the resource is of type `steps`. Allowed enum values: `steps`
default: `steps`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Indicates that the resource is of type `policies`. Allowed enum values: `policies`
default: `policies`
included
[ <oneOf>]
Provides any included related resources, such as steps or targets, returned with the policy.
Option 1
object
Represents a single step in an escalation policy, including its attributes, relationships, and resource type.
attributes
object
Defines attributes for an escalation policy step, such as assignment strategy and escalation timeout.
assignment
enum
Specifies how this escalation step will assign targets (example `default` or `round-robin`). Allowed enum values: `default,round-robin`
escalate_after_seconds
int64
Specifies how many seconds to wait before escalating to the next step.
id
string
Specifies the unique identifier of this escalation policy step.
relationships
object
Represents the relationship of an escalation policy step to its targets.
targets
object
A list of escalation targets for a step
data
[ <oneOf>]
The `EscalationTargets` `data`.
Option 1
object
Represents a team target for an escalation policy step, including the team's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the team resource.
type [_required_]
enum
Indicates that the resource is of type `teams`. Allowed enum values: `teams`
default: `teams`
Option 2
object
Represents a user target for an escalation policy step, including the user's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the user resource.
type [_required_]
enum
Indicates that the resource is of type `users`. Allowed enum values: `users`
default: `users`
Option 3
object
Represents a schedule target for an escalation policy step, including its ID and resource type. This is a shortcut for a configured schedule target with position set to 'current'.
id [_required_]
string
Specifies the unique identifier of the schedule resource.
type [_required_]
enum
Indicates that the resource is of type `schedules`. Allowed enum values: `schedules`
default: `schedules`
Option 4
object
Relationship reference to a configured schedule target.
id [_required_]
string
Specifies the unique identifier of the configured schedule target.
type [_required_]
enum
Indicates that the resource is of type `schedule_target`. Allowed enum values: `schedule_target`
default: `schedule_target`
type [_required_]
enum
Indicates that the resource is of type `steps`. Allowed enum values: `steps`
default: `steps`
Option 2
object
Represents a user object in the context of an escalation policy, including their `id`, type, and basic attributes.
attributes
object
Provides basic user information for an escalation policy, including a name and email address.
email
string
The user's email address.
name
string
The user's name.
status
enum
The user's status. Allowed enum values: `active,deactivated,pending`
id
string
The unique user identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 3
object
Represents the primary data object for a schedule, linking attributes and relationships.
attributes
object
Provides core properties of a schedule object such as its name and time zone.
name
string
A short name for the schedule.
time_zone
string
The time zone in which this schedule operates.
id
string
The schedule's unique identifier.
relationships
object
Groups the relationships for a schedule object, referencing layers and teams.
layers
object
Associates layers with this schedule in a data structure.
data
[object]
An array of layer references for this schedule.
id [_required_]
string
The unique identifier of the layer in this relationship.
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
Option 4
object
Full resource representation of a configured schedule target with position (previous, current, or next).
attributes [_required_]
object
Attributes for a configured schedule target, including position.
position [_required_]
enum
Specifies the position of a schedule target (example `previous`, `current`, or `next`). Allowed enum values: `previous,current,next`
id [_required_]
string
Specifies the unique identifier of the configured schedule target.
relationships [_required_]
object
Represents the relationships of a configured schedule target.
schedule [_required_]
object
Holds the schedule reference for a configured schedule target.
data [_required_]
object
Represents a schedule target for an escalation policy step, including its ID and resource type. This is a shortcut for a configured schedule target with position set to 'current'.
id [_required_]
string
Specifies the unique identifier of the schedule resource.
type [_required_]
enum
Indicates that the resource is of type `schedules`. Allowed enum values: `schedules`
default: `schedules`
type [_required_]
enum
Indicates that the resource is of type `schedule_target`. Allowed enum values: `schedule_target`
default: `schedule_target`
Option 5
object
Provides a reference to a team, including ID, type, and basic attributes/relationships.
attributes
object
Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
avatar
string
URL or reference for the team's avatar (if available).
description
string
A short text describing the team.
handle
string
A unique handle/slug for the team.
name
string
The full, human-readable name of the team.
id
string
The team's unique identifier.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
```
{
  "data": {
    "attributes": {
      "name": "Escalation Policy 1",
      "resolve_page_on_policy_end": true,
      "retries": 2
    },
    "id": "00000000-aba1-0000-0000-000000000000",
    "relationships": {
      "steps": {
        "data": [
          {
            "id": "00000000-aba1-0000-0000-000000000000",
            "type": "steps"
          }
        ]
      },
      "teams": {
        "data": [
          {
            "id": "00000000-da3a-0000-0000-000000000000",
            "type": "teams"
          }
        ]
      }
    },
    "type": "policies"
  },
  "included": [
    {
      "attributes": {
        "avatar": "",
        "description": "Team 1 description",
        "handle": "team1",
        "name": "Team 1"
      },
      "id": "00000000-da3a-0000-0000-000000000000",
      "type": "teams"
    },
    {
      "attributes": {
        "assignment": "default",
        "escalate_after_seconds": 3600
      },
      "id": "00000000-aba1-0000-0000-000000000000",
      "relationships": {
        "targets": {
          "data": [
            {
              "id": "00000000-aba1-0000-0000-000000000000",
              "type": "users"
            },
            {
              "id": "00000000-aba2-0000-0000-000000000000",
              "type": "schedules"
            },
            {
              "id": "00000000-aba2-0000-0000-000000000000_previous",
              "type": "schedule_target"
            },
            {
              "id": "00000000-aba3-0000-0000-000000000000",
              "type": "teams"
            }
          ]
        }
      },
      "type": "steps"
    },
    {
      "id": "00000000-aba1-0000-0000-000000000000",
      "type": "users"
    },
    {
      "id": "00000000-aba2-0000-0000-000000000000",
      "type": "schedules"
    },
    {
      "attributes": {
        "position": "previous"
      },
      "id": "00000000-aba2-0000-0000-000000000000_previous",
      "relationships": {
        "schedule": {
          "data": {
            "id": "00000000-aba2-0000-0000-000000000000",
            "type": "schedules"
          }
        }
      },
      "type": "schedule_target"
    },
    {
      "id": "00000000-aba3-0000-0000-000000000000",
      "type": "teams"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Create On-Call escalation policy returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/escalation-policies" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-On-Call",
      "resolve_page_on_policy_end": true,
      "retries": 2,
      "steps": [
        {
          "assignment": "default",
          "escalate_after_seconds": 3600,
          "targets": [
            {
              "id": "string",
              "type": "users"
            },
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "schedules"
            },
            {
              "config": {
                "schedule": {
                  "position": "previous"
                }
              },
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "schedules"
            },
            {
              "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
              "type": "teams"
            }
          ]
        },
        {
          "assignment": "round-robin",
          "escalate_after_seconds": 3600,
          "targets": [
            {
              "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
              "type": "teams"
            }
          ]
        }
      ]
    },
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "policies"
  }
}
EOF  

                        
```

#####  Create On-Call escalation policy returns "Created" response
```
// Create On-Call escalation policy returns "Created" response

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

	// there is a valid "schedule" in the system
	ScheduleDataID := os.Getenv("SCHEDULE_DATA_ID")

	// there is a valid "dd_team" in the system
	DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

	body := datadogV2.EscalationPolicyCreateRequest{
		Data: datadogV2.EscalationPolicyCreateRequestData{
			Attributes: datadogV2.EscalationPolicyCreateRequestDataAttributes{
				Name:                   "Example-On-Call",
				ResolvePageOnPolicyEnd: datadog.PtrBool(true),
				Retries:                datadog.PtrInt64(2),
				Steps: []datadogV2.EscalationPolicyCreateRequestDataAttributesStepsItems{
					{
						Assignment:           datadogV2.ESCALATIONPOLICYSTEPATTRIBUTESASSIGNMENT_DEFAULT.Ptr(),
						EscalateAfterSeconds: datadog.PtrInt64(3600),
						Targets: []datadogV2.EscalationPolicyStepTarget{
							{
								Id:   datadog.PtrString(UserDataID),
								Type: datadogV2.ESCALATIONPOLICYSTEPTARGETTYPE_USERS.Ptr(),
							},
							{
								Id:   datadog.PtrString(ScheduleDataID),
								Type: datadogV2.ESCALATIONPOLICYSTEPTARGETTYPE_SCHEDULES.Ptr(),
							},
							{
								Config: &datadogV2.EscalationPolicyStepTargetConfig{
									Schedule: &datadogV2.EscalationPolicyStepTargetConfigSchedule{
										Position: datadogV2.SCHEDULETARGETPOSITION_PREVIOUS.Ptr(),
									},
								},
								Id:   datadog.PtrString(ScheduleDataID),
								Type: datadogV2.ESCALATIONPOLICYSTEPTARGETTYPE_SCHEDULES.Ptr(),
							},
							{
								Id:   datadog.PtrString(DdTeamDataID),
								Type: datadogV2.ESCALATIONPOLICYSTEPTARGETTYPE_TEAMS.Ptr(),
							},
						},
					},
					{
						Assignment:           datadogV2.ESCALATIONPOLICYSTEPATTRIBUTESASSIGNMENT_ROUND_ROBIN.Ptr(),
						EscalateAfterSeconds: datadog.PtrInt64(3600),
						Targets: []datadogV2.EscalationPolicyStepTarget{
							{
								Id:   datadog.PtrString(DdTeamDataID),
								Type: datadogV2.ESCALATIONPOLICYSTEPTARGETTYPE_TEAMS.Ptr(),
							},
						},
					},
				},
			},
			Relationships: &datadogV2.EscalationPolicyCreateRequestDataRelationships{
				Teams: &datadogV2.DataRelationshipsTeams{
					Data: []datadogV2.DataRelationshipsTeamsDataItems{
						{
							Id:   DdTeamDataID,
							Type: datadogV2.DATARELATIONSHIPSTEAMSDATAITEMSTYPE_TEAMS,
						},
					},
				},
			},
			Type: datadogV2.ESCALATIONPOLICYCREATEREQUESTDATATYPE_POLICIES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.CreateOnCallEscalationPolicy(ctx, body, *datadogV2.NewCreateOnCallEscalationPolicyOptionalParameters().WithInclude("steps.targets"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.CreateOnCallEscalationPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.CreateOnCallEscalationPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create On-Call escalation policy returns "Created" response
```
// Create On-Call escalation policy returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.api.OnCallApi.CreateOnCallEscalationPolicyOptionalParameters;
import com.datadog.api.client.v2.model.DataRelationshipsTeams;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItems;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItemsType;
import com.datadog.api.client.v2.model.EscalationPolicy;
import com.datadog.api.client.v2.model.EscalationPolicyCreateRequest;
import com.datadog.api.client.v2.model.EscalationPolicyCreateRequestData;
import com.datadog.api.client.v2.model.EscalationPolicyCreateRequestDataAttributes;
import com.datadog.api.client.v2.model.EscalationPolicyCreateRequestDataAttributesStepsItems;
import com.datadog.api.client.v2.model.EscalationPolicyCreateRequestDataRelationships;
import com.datadog.api.client.v2.model.EscalationPolicyCreateRequestDataType;
import com.datadog.api.client.v2.model.EscalationPolicyStepAttributesAssignment;
import com.datadog.api.client.v2.model.EscalationPolicyStepTarget;
import com.datadog.api.client.v2.model.EscalationPolicyStepTargetConfig;
import com.datadog.api.client.v2.model.EscalationPolicyStepTargetConfigSchedule;
import com.datadog.api.client.v2.model.EscalationPolicyStepTargetType;
import com.datadog.api.client.v2.model.ScheduleTargetPosition;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    // there is a valid "schedule" in the system
    String SCHEDULE_DATA_ID = System.getenv("SCHEDULE_DATA_ID");

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    EscalationPolicyCreateRequest body =
        new EscalationPolicyCreateRequest()
            .data(
                new EscalationPolicyCreateRequestData()
                    .attributes(
                        new EscalationPolicyCreateRequestDataAttributes()
                            .name("Example-On-Call")
                            .resolvePageOnPolicyEnd(true)
                            .retries(2L)
                            .steps(
                                Arrays.asList(
                                    new EscalationPolicyCreateRequestDataAttributesStepsItems()
                                        .assignment(
                                            EscalationPolicyStepAttributesAssignment.DEFAULT)
                                        .escalateAfterSeconds(3600L)
                                        .targets(
                                            Arrays.asList(
                                                new EscalationPolicyStepTarget()
                                                    .id(USER_DATA_ID)
                                                    .type(EscalationPolicyStepTargetType.USERS),
                                                new EscalationPolicyStepTarget()
                                                    .id(SCHEDULE_DATA_ID)
                                                    .type(EscalationPolicyStepTargetType.SCHEDULES),
                                                new EscalationPolicyStepTarget()
                                                    .config(
                                                        new EscalationPolicyStepTargetConfig()
                                                            .schedule(
                                                                new EscalationPolicyStepTargetConfigSchedule()
                                                                    .position(
                                                                        ScheduleTargetPosition
                                                                            .PREVIOUS)))
                                                    .id(SCHEDULE_DATA_ID)
                                                    .type(EscalationPolicyStepTargetType.SCHEDULES),
                                                new EscalationPolicyStepTarget()
                                                    .id(DD_TEAM_DATA_ID)
                                                    .type(EscalationPolicyStepTargetType.TEAMS))),
                                    new EscalationPolicyCreateRequestDataAttributesStepsItems()
                                        .assignment(
                                            EscalationPolicyStepAttributesAssignment.ROUND_ROBIN)
                                        .escalateAfterSeconds(3600L)
                                        .targets(
                                            Collections.singletonList(
                                                new EscalationPolicyStepTarget()
                                                    .id(DD_TEAM_DATA_ID)
                                                    .type(EscalationPolicyStepTargetType.TEAMS))))))
                    .relationships(
                        new EscalationPolicyCreateRequestDataRelationships()
                            .teams(
                                new DataRelationshipsTeams()
                                    .data(
                                        Collections.singletonList(
                                            new DataRelationshipsTeamsDataItems()
                                                .id(DD_TEAM_DATA_ID)
                                                .type(DataRelationshipsTeamsDataItemsType.TEAMS)))))
                    .type(EscalationPolicyCreateRequestDataType.POLICIES));

    try {
      EscalationPolicy result =
          apiInstance.createOnCallEscalationPolicy(
              body, new CreateOnCallEscalationPolicyOptionalParameters().include("steps.targets"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#createOnCallEscalationPolicy");
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

#####  Create On-Call escalation policy returns "Created" response
```
"""
Create On-Call escalation policy returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams
from datadog_api_client.v2.model.data_relationships_teams_data_items import DataRelationshipsTeamsDataItems
from datadog_api_client.v2.model.data_relationships_teams_data_items_type import DataRelationshipsTeamsDataItemsType
from datadog_api_client.v2.model.escalation_policy_create_request import EscalationPolicyCreateRequest
from datadog_api_client.v2.model.escalation_policy_create_request_data import EscalationPolicyCreateRequestData
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes import (
    EscalationPolicyCreateRequestDataAttributes,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items import (
    EscalationPolicyCreateRequestDataAttributesStepsItems,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships import (
    EscalationPolicyCreateRequestDataRelationships,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_type import EscalationPolicyCreateRequestDataType
from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
    EscalationPolicyStepAttributesAssignment,
)
from datadog_api_client.v2.model.escalation_policy_step_target import EscalationPolicyStepTarget
from datadog_api_client.v2.model.escalation_policy_step_target_config import EscalationPolicyStepTargetConfig
from datadog_api_client.v2.model.escalation_policy_step_target_config_schedule import (
    EscalationPolicyStepTargetConfigSchedule,
)
from datadog_api_client.v2.model.escalation_policy_step_target_type import EscalationPolicyStepTargetType
from datadog_api_client.v2.model.schedule_target_position import ScheduleTargetPosition

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = EscalationPolicyCreateRequest(
    data=EscalationPolicyCreateRequestData(
        attributes=EscalationPolicyCreateRequestDataAttributes(
            name="Example-On-Call",
            resolve_page_on_policy_end=True,
            retries=2,
            steps=[
                EscalationPolicyCreateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyStepAttributesAssignment.DEFAULT,
                    escalate_after_seconds=3600,
                    targets=[
                        EscalationPolicyStepTarget(
                            id=USER_DATA_ID,
                            type=EscalationPolicyStepTargetType.USERS,
                        ),
                        EscalationPolicyStepTarget(
                            id=SCHEDULE_DATA_ID,
                            type=EscalationPolicyStepTargetType.SCHEDULES,
                        ),
                        EscalationPolicyStepTarget(
                            config=EscalationPolicyStepTargetConfig(
                                schedule=EscalationPolicyStepTargetConfigSchedule(
                                    position=ScheduleTargetPosition.PREVIOUS,
                                ),
                            ),
                            id=SCHEDULE_DATA_ID,
                            type=EscalationPolicyStepTargetType.SCHEDULES,
                        ),
                        EscalationPolicyStepTarget(
                            id=DD_TEAM_DATA_ID,
                            type=EscalationPolicyStepTargetType.TEAMS,
                        ),
                    ],
                ),
                EscalationPolicyCreateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyStepAttributesAssignment.ROUND_ROBIN,
                    escalate_after_seconds=3600,
                    targets=[
                        EscalationPolicyStepTarget(
                            id=DD_TEAM_DATA_ID,
                            type=EscalationPolicyStepTargetType.TEAMS,
                        ),
                    ],
                ),
            ],
        ),
        relationships=EscalationPolicyCreateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=EscalationPolicyCreateRequestDataType.POLICIES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_on_call_escalation_policy(include="steps.targets", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create On-Call escalation policy returns "Created" response
```
# Create On-Call escalation policy returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = ENV["SCHEDULE_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::EscalationPolicyCreateRequest.new({
  data: DatadogAPIClient::V2::EscalationPolicyCreateRequestData.new({
    attributes: DatadogAPIClient::V2::EscalationPolicyCreateRequestDataAttributes.new({
      name: "Example-On-Call",
      resolve_page_on_policy_end: true,
      retries: 2,
      steps: [
        DatadogAPIClient::V2::EscalationPolicyCreateRequestDataAttributesStepsItems.new({
          assignment: DatadogAPIClient::V2::EscalationPolicyStepAttributesAssignment::DEFAULT,
          escalate_after_seconds: 3600,
          targets: [
            DatadogAPIClient::V2::EscalationPolicyStepTarget.new({
              id: USER_DATA_ID,
              type: DatadogAPIClient::V2::EscalationPolicyStepTargetType::USERS,
            }),
            DatadogAPIClient::V2::EscalationPolicyStepTarget.new({
              id: SCHEDULE_DATA_ID,
              type: DatadogAPIClient::V2::EscalationPolicyStepTargetType::SCHEDULES,
            }),
            DatadogAPIClient::V2::EscalationPolicyStepTarget.new({
              config: DatadogAPIClient::V2::EscalationPolicyStepTargetConfig.new({
                schedule: DatadogAPIClient::V2::EscalationPolicyStepTargetConfigSchedule.new({
                  position: DatadogAPIClient::V2::ScheduleTargetPosition::PREVIOUS,
                }),
              }),
              id: SCHEDULE_DATA_ID,
              type: DatadogAPIClient::V2::EscalationPolicyStepTargetType::SCHEDULES,
            }),
            DatadogAPIClient::V2::EscalationPolicyStepTarget.new({
              id: DD_TEAM_DATA_ID,
              type: DatadogAPIClient::V2::EscalationPolicyStepTargetType::TEAMS,
            }),
          ],
        }),
        DatadogAPIClient::V2::EscalationPolicyCreateRequestDataAttributesStepsItems.new({
          assignment: DatadogAPIClient::V2::EscalationPolicyStepAttributesAssignment::ROUND_ROBIN,
          escalate_after_seconds: 3600,
          targets: [
            DatadogAPIClient::V2::EscalationPolicyStepTarget.new({
              id: DD_TEAM_DATA_ID,
              type: DatadogAPIClient::V2::EscalationPolicyStepTargetType::TEAMS,
            }),
          ],
        }),
      ],
    }),
    relationships: DatadogAPIClient::V2::EscalationPolicyCreateRequestDataRelationships.new({
      teams: DatadogAPIClient::V2::DataRelationshipsTeams.new({
        data: [
          DatadogAPIClient::V2::DataRelationshipsTeamsDataItems.new({
            id: DD_TEAM_DATA_ID,
            type: DatadogAPIClient::V2::DataRelationshipsTeamsDataItemsType::TEAMS,
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::EscalationPolicyCreateRequestDataType::POLICIES,
  }),
})
opts = {
  include: "steps.targets",
}
p api_instance.create_on_call_escalation_policy(body, opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create On-Call escalation policy returns "Created" response
```
// Create On-Call escalation policy returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::CreateOnCallEscalationPolicyOptionalParams;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;
use datadog_api_client::datadogV2::model::DataRelationshipsTeams;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItems;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItemsType;
use datadog_api_client::datadogV2::model::EscalationPolicyCreateRequest;
use datadog_api_client::datadogV2::model::EscalationPolicyCreateRequestData;
use datadog_api_client::datadogV2::model::EscalationPolicyCreateRequestDataAttributes;
use datadog_api_client::datadogV2::model::EscalationPolicyCreateRequestDataAttributesStepsItems;
use datadog_api_client::datadogV2::model::EscalationPolicyCreateRequestDataRelationships;
use datadog_api_client::datadogV2::model::EscalationPolicyCreateRequestDataType;
use datadog_api_client::datadogV2::model::EscalationPolicyStepAttributesAssignment;
use datadog_api_client::datadogV2::model::EscalationPolicyStepTarget;
use datadog_api_client::datadogV2::model::EscalationPolicyStepTargetConfig;
use datadog_api_client::datadogV2::model::EscalationPolicyStepTargetConfigSchedule;
use datadog_api_client::datadogV2::model::EscalationPolicyStepTargetType;
use datadog_api_client::datadogV2::model::ScheduleTargetPosition;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();

    // there is a valid "schedule" in the system
    let schedule_data_id = std::env::var("SCHEDULE_DATA_ID").unwrap();

    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = EscalationPolicyCreateRequest::new(
        EscalationPolicyCreateRequestData::new(
            EscalationPolicyCreateRequestDataAttributes::new(
                "Example-On-Call".to_string(),
                vec![
                    EscalationPolicyCreateRequestDataAttributesStepsItems::new(vec![
                        EscalationPolicyStepTarget::new()
                            .id(user_data_id.clone())
                            .type_(EscalationPolicyStepTargetType::USERS),
                        EscalationPolicyStepTarget::new()
                            .id(schedule_data_id.clone())
                            .type_(EscalationPolicyStepTargetType::SCHEDULES),
                        EscalationPolicyStepTarget::new()
                            .config(
                                EscalationPolicyStepTargetConfig::new().schedule(
                                    EscalationPolicyStepTargetConfigSchedule::new()
                                        .position(ScheduleTargetPosition::PREVIOUS),
                                ),
                            )
                            .id(schedule_data_id.clone())
                            .type_(EscalationPolicyStepTargetType::SCHEDULES),
                        EscalationPolicyStepTarget::new()
                            .id(dd_team_data_id.clone())
                            .type_(EscalationPolicyStepTargetType::TEAMS),
                    ])
                    .assignment(EscalationPolicyStepAttributesAssignment::DEFAULT)
                    .escalate_after_seconds(3600),
                    EscalationPolicyCreateRequestDataAttributesStepsItems::new(vec![
                        EscalationPolicyStepTarget::new()
                            .id(dd_team_data_id.clone())
                            .type_(EscalationPolicyStepTargetType::TEAMS),
                    ])
                    .assignment(EscalationPolicyStepAttributesAssignment::ROUND_ROBIN)
                    .escalate_after_seconds(3600),
                ],
            )
            .resolve_page_on_policy_end(true)
            .retries(2),
            EscalationPolicyCreateRequestDataType::POLICIES,
        )
        .relationships(EscalationPolicyCreateRequestDataRelationships::new().teams(
            DataRelationshipsTeams::new().data(vec![DataRelationshipsTeamsDataItems::new(
                dd_team_data_id.clone(),
                DataRelationshipsTeamsDataItemsType::TEAMS,
            )]),
        )),
    );
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .create_on_call_escalation_policy(
            body,
            CreateOnCallEscalationPolicyOptionalParams::default()
                .include("steps.targets".to_string()),
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

#####  Create On-Call escalation policy returns "Created" response
```
/**
 * Create On-Call escalation policy returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

// there is a valid "schedule" in the system
const SCHEDULE_DATA_ID = process.env.SCHEDULE_DATA_ID as string;

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.OnCallApiCreateOnCallEscalationPolicyRequest = {
  body: {
    data: {
      attributes: {
        name: "Example-On-Call",
        resolvePageOnPolicyEnd: true,
        retries: 2,
        steps: [
          {
            assignment: "default",
            escalateAfterSeconds: 3600,
            targets: [
              {
                id: USER_DATA_ID,
                type: "users",
              },
              {
                id: SCHEDULE_DATA_ID,
                type: "schedules",
              },
              {
                config: {
                  schedule: {
                    position: "previous",
                  },
                },
                id: SCHEDULE_DATA_ID,
                type: "schedules",
              },
              {
                id: DD_TEAM_DATA_ID,
                type: "teams",
              },
            ],
          },
          {
            assignment: "round-robin",
            escalateAfterSeconds: 3600,
            targets: [
              {
                id: DD_TEAM_DATA_ID,
                type: "teams",
              },
            ],
          },
        ],
      },
      relationships: {
        teams: {
          data: [
            {
              id: DD_TEAM_DATA_ID,
              type: "teams",
            },
          ],
        },
      },
      type: "policies",
    },
  },
  include: "steps.targets",
};

apiInstance
  .createOnCallEscalationPolicy(params)
  .then((data: v2.EscalationPolicy) => {
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
## [Update On-Call escalation policy](https://docs.datadoghq.com/api/latest/on-call/#update-on-call-escalation-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#update-on-call-escalation-policy-v2)


PUT https://api.ap1.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.ap2.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.datadoghq.eu/api/v2/on-call/escalation-policies/{policy_id}https://api.ddog-gov.com/api/v2/on-call/escalation-policies/{policy_id}https://api.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.us3.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.us5.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}
### Overview
Update an On-Call escalation policy This endpoint requires the `on_call_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
policy_id [_required_]
string
The ID of the escalation policy
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `teams`, `steps`, `steps.targets`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data [_required_]
object
Represents the data for updating an existing escalation policy, including its ID, attributes, relationships, and resource type.
attributes [_required_]
object
Defines the attributes that can be updated for an escalation policy, such as description, name, resolution behavior, retries, and steps.
name [_required_]
string
Specifies the name of the escalation policy.
resolve_page_on_policy_end
boolean
Indicates whether the page is automatically resolved when the policy ends.
retries
int64
Specifies how many times the escalation sequence is retried if there is no response.
steps [_required_]
[object]
A list of escalation steps, each defining assignment, escalation timeout, and targets.
assignment
enum
Specifies how this escalation step will assign targets (example `default` or `round-robin`). Allowed enum values: `default,round-robin`
escalate_after_seconds
int64
Defines how many seconds to wait before escalating to the next step.
id
string
Specifies the unique identifier of this step.
targets [_required_]
[object]
Specifies the collection of escalation targets for this step.
config
object
Configuration for an escalation target, such as schedule position.
schedule
object
Schedule-specific configuration for an escalation target.
position
enum
Specifies the position of a schedule target (example `previous`, `current`, or `next`). Allowed enum values: `previous,current,next`
id
string
Specifies the unique identifier for this target.
type
enum
Specifies the type of escalation target (example `users`, `schedules`, or `teams`). Allowed enum values: `users,schedules,teams`
id [_required_]
string
Specifies the unique identifier of the escalation policy being updated.
relationships
object
Represents relationships in an escalation policy update request, including references to teams.
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Indicates that the resource is of type `policies`. Allowed enum values: `policies`
default: `policies`
```
{
  "data": {
    "attributes": {
      "name": "Example-On-Call-updated",
      "resolve_page_on_policy_end": false,
      "retries": 0,
      "steps": [
        {
          "assignment": "default",
          "escalate_after_seconds": 3600,
          "id": "00000000-aba1-0000-0000-000000000000",
          "targets": [
            {
              "id": "string",
              "type": "users"
            }
          ]
        }
      ]
    },
    "id": "ab000000-0000-0000-0000-000000000000",
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "policies"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallEscalationPolicy-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallEscalationPolicy-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallEscalationPolicy-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallEscalationPolicy-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallEscalationPolicy-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#UpdateOnCallEscalationPolicy-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Represents a complete escalation policy response, including policy data and optionally included related resources.
Field
Type
Description
data
object
Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type.
attributes
object
Defines the main attributes of an escalation policy, such as its name and behavior on policy end.
name [_required_]
string
Specifies the name of the escalation policy.
resolve_page_on_policy_end
boolean
Indicates whether the page is automatically resolved when the policy ends.
retries
int64
Specifies how many times the escalation sequence is retried if there is no response.
id
string
Specifies the unique identifier of the escalation policy.
relationships
object
Represents the relationships for an escalation policy, including references to steps and teams.
steps [_required_]
object
Defines the relationship to a collection of steps within an escalation policy. Contains an array of step data references.
data
[object]
An array of references to the steps defined in this escalation policy.
id [_required_]
string
Specifies the unique identifier for the step resource.
type [_required_]
enum
Indicates that the resource is of type `steps`. Allowed enum values: `steps`
default: `steps`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Indicates that the resource is of type `policies`. Allowed enum values: `policies`
default: `policies`
included
[ <oneOf>]
Provides any included related resources, such as steps or targets, returned with the policy.
Option 1
object
Represents a single step in an escalation policy, including its attributes, relationships, and resource type.
attributes
object
Defines attributes for an escalation policy step, such as assignment strategy and escalation timeout.
assignment
enum
Specifies how this escalation step will assign targets (example `default` or `round-robin`). Allowed enum values: `default,round-robin`
escalate_after_seconds
int64
Specifies how many seconds to wait before escalating to the next step.
id
string
Specifies the unique identifier of this escalation policy step.
relationships
object
Represents the relationship of an escalation policy step to its targets.
targets
object
A list of escalation targets for a step
data
[ <oneOf>]
The `EscalationTargets` `data`.
Option 1
object
Represents a team target for an escalation policy step, including the team's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the team resource.
type [_required_]
enum
Indicates that the resource is of type `teams`. Allowed enum values: `teams`
default: `teams`
Option 2
object
Represents a user target for an escalation policy step, including the user's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the user resource.
type [_required_]
enum
Indicates that the resource is of type `users`. Allowed enum values: `users`
default: `users`
Option 3
object
Represents a schedule target for an escalation policy step, including its ID and resource type. This is a shortcut for a configured schedule target with position set to 'current'.
id [_required_]
string
Specifies the unique identifier of the schedule resource.
type [_required_]
enum
Indicates that the resource is of type `schedules`. Allowed enum values: `schedules`
default: `schedules`
Option 4
object
Relationship reference to a configured schedule target.
id [_required_]
string
Specifies the unique identifier of the configured schedule target.
type [_required_]
enum
Indicates that the resource is of type `schedule_target`. Allowed enum values: `schedule_target`
default: `schedule_target`
type [_required_]
enum
Indicates that the resource is of type `steps`. Allowed enum values: `steps`
default: `steps`
Option 2
object
Represents a user object in the context of an escalation policy, including their `id`, type, and basic attributes.
attributes
object
Provides basic user information for an escalation policy, including a name and email address.
email
string
The user's email address.
name
string
The user's name.
status
enum
The user's status. Allowed enum values: `active,deactivated,pending`
id
string
The unique user identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 3
object
Represents the primary data object for a schedule, linking attributes and relationships.
attributes
object
Provides core properties of a schedule object such as its name and time zone.
name
string
A short name for the schedule.
time_zone
string
The time zone in which this schedule operates.
id
string
The schedule's unique identifier.
relationships
object
Groups the relationships for a schedule object, referencing layers and teams.
layers
object
Associates layers with this schedule in a data structure.
data
[object]
An array of layer references for this schedule.
id [_required_]
string
The unique identifier of the layer in this relationship.
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
Option 4
object
Full resource representation of a configured schedule target with position (previous, current, or next).
attributes [_required_]
object
Attributes for a configured schedule target, including position.
position [_required_]
enum
Specifies the position of a schedule target (example `previous`, `current`, or `next`). Allowed enum values: `previous,current,next`
id [_required_]
string
Specifies the unique identifier of the configured schedule target.
relationships [_required_]
object
Represents the relationships of a configured schedule target.
schedule [_required_]
object
Holds the schedule reference for a configured schedule target.
data [_required_]
object
Represents a schedule target for an escalation policy step, including its ID and resource type. This is a shortcut for a configured schedule target with position set to 'current'.
id [_required_]
string
Specifies the unique identifier of the schedule resource.
type [_required_]
enum
Indicates that the resource is of type `schedules`. Allowed enum values: `schedules`
default: `schedules`
type [_required_]
enum
Indicates that the resource is of type `schedule_target`. Allowed enum values: `schedule_target`
default: `schedule_target`
Option 5
object
Provides a reference to a team, including ID, type, and basic attributes/relationships.
attributes
object
Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
avatar
string
URL or reference for the team's avatar (if available).
description
string
A short text describing the team.
handle
string
A unique handle/slug for the team.
name
string
The full, human-readable name of the team.
id
string
The team's unique identifier.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
```
{
  "data": {
    "attributes": {
      "name": "Escalation Policy 1",
      "resolve_page_on_policy_end": true,
      "retries": 2
    },
    "id": "00000000-aba1-0000-0000-000000000000",
    "relationships": {
      "steps": {
        "data": [
          {
            "id": "00000000-aba1-0000-0000-000000000000",
            "type": "steps"
          }
        ]
      },
      "teams": {
        "data": [
          {
            "id": "00000000-da3a-0000-0000-000000000000",
            "type": "teams"
          }
        ]
      }
    },
    "type": "policies"
  },
  "included": [
    {
      "attributes": {
        "avatar": "",
        "description": "Team 1 description",
        "handle": "team1",
        "name": "Team 1"
      },
      "id": "00000000-da3a-0000-0000-000000000000",
      "type": "teams"
    },
    {
      "attributes": {
        "assignment": "default",
        "escalate_after_seconds": 3600
      },
      "id": "00000000-aba1-0000-0000-000000000000",
      "relationships": {
        "targets": {
          "data": [
            {
              "id": "00000000-aba1-0000-0000-000000000000",
              "type": "users"
            },
            {
              "id": "00000000-aba2-0000-0000-000000000000",
              "type": "schedules"
            },
            {
              "id": "00000000-aba2-0000-0000-000000000000_previous",
              "type": "schedule_target"
            },
            {
              "id": "00000000-aba3-0000-0000-000000000000",
              "type": "teams"
            }
          ]
        }
      },
      "type": "steps"
    },
    {
      "id": "00000000-aba1-0000-0000-000000000000",
      "type": "users"
    },
    {
      "id": "00000000-aba2-0000-0000-000000000000",
      "type": "schedules"
    },
    {
      "attributes": {
        "position": "previous"
      },
      "id": "00000000-aba2-0000-0000-000000000000_previous",
      "relationships": {
        "schedule": {
          "data": {
            "id": "00000000-aba2-0000-0000-000000000000",
            "type": "schedules"
          }
        }
      },
      "type": "schedule_target"
    },
    {
      "id": "00000000-aba3-0000-0000-000000000000",
      "type": "teams"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Update On-Call escalation policy returns "OK" response
Copy
```
                          # Path parameters  
export policy_id="a3000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/escalation-policies/${policy_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-On-Call-updated",
      "resolve_page_on_policy_end": false,
      "retries": 0,
      "steps": [
        {
          "assignment": "default",
          "escalate_after_seconds": 3600,
          "id": "00000000-aba1-0000-0000-000000000000",
          "targets": [
            {
              "id": "string",
              "type": "users"
            }
          ]
        }
      ]
    },
    "id": "ab000000-0000-0000-0000-000000000000",
    "relationships": {
      "teams": {
        "data": [
          {
            "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
            "type": "teams"
          }
        ]
      }
    },
    "type": "policies"
  }
}
EOF  

                        
```

#####  Update On-Call escalation policy returns "OK" response
```
// Update On-Call escalation policy returns "OK" response

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
	// there is a valid "escalation_policy" in the system
	EscalationPolicyDataID := os.Getenv("ESCALATION_POLICY_DATA_ID")
	EscalationPolicyDataRelationshipsStepsData0ID := os.Getenv("ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID")

	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	// there is a valid "dd_team" in the system
	DdTeamDataID := os.Getenv("DD_TEAM_DATA_ID")

	body := datadogV2.EscalationPolicyUpdateRequest{
		Data: datadogV2.EscalationPolicyUpdateRequestData{
			Attributes: datadogV2.EscalationPolicyUpdateRequestDataAttributes{
				Name:                   "Example-On-Call-updated",
				ResolvePageOnPolicyEnd: datadog.PtrBool(false),
				Retries:                datadog.PtrInt64(0),
				Steps: []datadogV2.EscalationPolicyUpdateRequestDataAttributesStepsItems{
					{
						Assignment:           datadogV2.ESCALATIONPOLICYSTEPATTRIBUTESASSIGNMENT_DEFAULT.Ptr(),
						EscalateAfterSeconds: datadog.PtrInt64(3600),
						Id:                   datadog.PtrString(EscalationPolicyDataRelationshipsStepsData0ID),
						Targets: []datadogV2.EscalationPolicyStepTarget{
							{
								Id:   datadog.PtrString(UserDataID),
								Type: datadogV2.ESCALATIONPOLICYSTEPTARGETTYPE_USERS.Ptr(),
							},
						},
					},
				},
			},
			Id: EscalationPolicyDataID,
			Relationships: &datadogV2.EscalationPolicyUpdateRequestDataRelationships{
				Teams: &datadogV2.DataRelationshipsTeams{
					Data: []datadogV2.DataRelationshipsTeamsDataItems{
						{
							Id:   DdTeamDataID,
							Type: datadogV2.DATARELATIONSHIPSTEAMSDATAITEMSTYPE_TEAMS,
						},
					},
				},
			},
			Type: datadogV2.ESCALATIONPOLICYUPDATEREQUESTDATATYPE_POLICIES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.UpdateOnCallEscalationPolicy(ctx, EscalationPolicyDataID, body, *datadogV2.NewUpdateOnCallEscalationPolicyOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.UpdateOnCallEscalationPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.UpdateOnCallEscalationPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update On-Call escalation policy returns "OK" response
```
// Update On-Call escalation policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.DataRelationshipsTeams;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItems;
import com.datadog.api.client.v2.model.DataRelationshipsTeamsDataItemsType;
import com.datadog.api.client.v2.model.EscalationPolicy;
import com.datadog.api.client.v2.model.EscalationPolicyStepAttributesAssignment;
import com.datadog.api.client.v2.model.EscalationPolicyStepTarget;
import com.datadog.api.client.v2.model.EscalationPolicyStepTargetType;
import com.datadog.api.client.v2.model.EscalationPolicyUpdateRequest;
import com.datadog.api.client.v2.model.EscalationPolicyUpdateRequestData;
import com.datadog.api.client.v2.model.EscalationPolicyUpdateRequestDataAttributes;
import com.datadog.api.client.v2.model.EscalationPolicyUpdateRequestDataAttributesStepsItems;
import com.datadog.api.client.v2.model.EscalationPolicyUpdateRequestDataRelationships;
import com.datadog.api.client.v2.model.EscalationPolicyUpdateRequestDataType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "escalation_policy" in the system
    String ESCALATION_POLICY_DATA_ID = System.getenv("ESCALATION_POLICY_DATA_ID");
    String ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID =
        System.getenv("ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID");

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    EscalationPolicyUpdateRequest body =
        new EscalationPolicyUpdateRequest()
            .data(
                new EscalationPolicyUpdateRequestData()
                    .attributes(
                        new EscalationPolicyUpdateRequestDataAttributes()
                            .name("Example-On-Call-updated")
                            .resolvePageOnPolicyEnd(false)
                            .retries(0L)
                            .steps(
                                Collections.singletonList(
                                    new EscalationPolicyUpdateRequestDataAttributesStepsItems()
                                        .assignment(
                                            EscalationPolicyStepAttributesAssignment.DEFAULT)
                                        .escalateAfterSeconds(3600L)
                                        .id(ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID)
                                        .targets(
                                            Collections.singletonList(
                                                new EscalationPolicyStepTarget()
                                                    .id(USER_DATA_ID)
                                                    .type(EscalationPolicyStepTargetType.USERS))))))
                    .id(ESCALATION_POLICY_DATA_ID)
                    .relationships(
                        new EscalationPolicyUpdateRequestDataRelationships()
                            .teams(
                                new DataRelationshipsTeams()
                                    .data(
                                        Collections.singletonList(
                                            new DataRelationshipsTeamsDataItems()
                                                .id(DD_TEAM_DATA_ID)
                                                .type(DataRelationshipsTeamsDataItemsType.TEAMS)))))
                    .type(EscalationPolicyUpdateRequestDataType.POLICIES));

    try {
      EscalationPolicy result =
          apiInstance.updateOnCallEscalationPolicy(ESCALATION_POLICY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#updateOnCallEscalationPolicy");
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

#####  Update On-Call escalation policy returns "OK" response
```
"""
Update On-Call escalation policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams
from datadog_api_client.v2.model.data_relationships_teams_data_items import DataRelationshipsTeamsDataItems
from datadog_api_client.v2.model.data_relationships_teams_data_items_type import DataRelationshipsTeamsDataItemsType
from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
    EscalationPolicyStepAttributesAssignment,
)
from datadog_api_client.v2.model.escalation_policy_step_target import EscalationPolicyStepTarget
from datadog_api_client.v2.model.escalation_policy_step_target_type import EscalationPolicyStepTargetType
from datadog_api_client.v2.model.escalation_policy_update_request import EscalationPolicyUpdateRequest
from datadog_api_client.v2.model.escalation_policy_update_request_data import EscalationPolicyUpdateRequestData
from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes import (
    EscalationPolicyUpdateRequestDataAttributes,
)
from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes_steps_items import (
    EscalationPolicyUpdateRequestDataAttributesStepsItems,
)
from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships import (
    EscalationPolicyUpdateRequestDataRelationships,
)
from datadog_api_client.v2.model.escalation_policy_update_request_data_type import EscalationPolicyUpdateRequestDataType

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = environ["ESCALATION_POLICY_DATA_ID"]
ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID = environ["ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = EscalationPolicyUpdateRequest(
    data=EscalationPolicyUpdateRequestData(
        attributes=EscalationPolicyUpdateRequestDataAttributes(
            name="Example-On-Call-updated",
            resolve_page_on_policy_end=False,
            retries=0,
            steps=[
                EscalationPolicyUpdateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyStepAttributesAssignment.DEFAULT,
                    escalate_after_seconds=3600,
                    id=ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID,
                    targets=[
                        EscalationPolicyStepTarget(
                            id=USER_DATA_ID,
                            type=EscalationPolicyStepTargetType.USERS,
                        ),
                    ],
                ),
            ],
        ),
        id=ESCALATION_POLICY_DATA_ID,
        relationships=EscalationPolicyUpdateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=EscalationPolicyUpdateRequestDataType.POLICIES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.update_on_call_escalation_policy(policy_id=ESCALATION_POLICY_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update On-Call escalation policy returns "OK" response
```
# Update On-Call escalation policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = ENV["ESCALATION_POLICY_DATA_ID"]
ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID = ENV["ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID"]

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

body = DatadogAPIClient::V2::EscalationPolicyUpdateRequest.new({
  data: DatadogAPIClient::V2::EscalationPolicyUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::EscalationPolicyUpdateRequestDataAttributes.new({
      name: "Example-On-Call-updated",
      resolve_page_on_policy_end: false,
      retries: 0,
      steps: [
        DatadogAPIClient::V2::EscalationPolicyUpdateRequestDataAttributesStepsItems.new({
          assignment: DatadogAPIClient::V2::EscalationPolicyStepAttributesAssignment::DEFAULT,
          escalate_after_seconds: 3600,
          id: ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID,
          targets: [
            DatadogAPIClient::V2::EscalationPolicyStepTarget.new({
              id: USER_DATA_ID,
              type: DatadogAPIClient::V2::EscalationPolicyStepTargetType::USERS,
            }),
          ],
        }),
      ],
    }),
    id: ESCALATION_POLICY_DATA_ID,
    relationships: DatadogAPIClient::V2::EscalationPolicyUpdateRequestDataRelationships.new({
      teams: DatadogAPIClient::V2::DataRelationshipsTeams.new({
        data: [
          DatadogAPIClient::V2::DataRelationshipsTeamsDataItems.new({
            id: DD_TEAM_DATA_ID,
            type: DatadogAPIClient::V2::DataRelationshipsTeamsDataItemsType::TEAMS,
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::EscalationPolicyUpdateRequestDataType::POLICIES,
  }),
})
p api_instance.update_on_call_escalation_policy(ESCALATION_POLICY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update On-Call escalation policy returns "OK" response
```
// Update On-Call escalation policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;
use datadog_api_client::datadogV2::api_on_call::UpdateOnCallEscalationPolicyOptionalParams;
use datadog_api_client::datadogV2::model::DataRelationshipsTeams;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItems;
use datadog_api_client::datadogV2::model::DataRelationshipsTeamsDataItemsType;
use datadog_api_client::datadogV2::model::EscalationPolicyStepAttributesAssignment;
use datadog_api_client::datadogV2::model::EscalationPolicyStepTarget;
use datadog_api_client::datadogV2::model::EscalationPolicyStepTargetType;
use datadog_api_client::datadogV2::model::EscalationPolicyUpdateRequest;
use datadog_api_client::datadogV2::model::EscalationPolicyUpdateRequestData;
use datadog_api_client::datadogV2::model::EscalationPolicyUpdateRequestDataAttributes;
use datadog_api_client::datadogV2::model::EscalationPolicyUpdateRequestDataAttributesStepsItems;
use datadog_api_client::datadogV2::model::EscalationPolicyUpdateRequestDataRelationships;
use datadog_api_client::datadogV2::model::EscalationPolicyUpdateRequestDataType;

#[tokio::main]
async fn main() {
    // there is a valid "escalation_policy" in the system
    let escalation_policy_data_id = std::env::var("ESCALATION_POLICY_DATA_ID").unwrap();
    let escalation_policy_data_relationships_steps_data_0_id =
        std::env::var("ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID").unwrap();

    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();

    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();
    let body = EscalationPolicyUpdateRequest::new(
        EscalationPolicyUpdateRequestData::new(
            EscalationPolicyUpdateRequestDataAttributes::new(
                "Example-On-Call-updated".to_string(),
                vec![
                    EscalationPolicyUpdateRequestDataAttributesStepsItems::new(vec![
                        EscalationPolicyStepTarget::new()
                            .id(user_data_id.clone())
                            .type_(EscalationPolicyStepTargetType::USERS),
                    ])
                    .assignment(EscalationPolicyStepAttributesAssignment::DEFAULT)
                    .escalate_after_seconds(3600)
                    .id(escalation_policy_data_relationships_steps_data_0_id.clone()),
                ],
            )
            .resolve_page_on_policy_end(false)
            .retries(0),
            escalation_policy_data_id.clone(),
            EscalationPolicyUpdateRequestDataType::POLICIES,
        )
        .relationships(EscalationPolicyUpdateRequestDataRelationships::new().teams(
            DataRelationshipsTeams::new().data(vec![DataRelationshipsTeamsDataItems::new(
                dd_team_data_id.clone(),
                DataRelationshipsTeamsDataItemsType::TEAMS,
            )]),
        )),
    );
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .update_on_call_escalation_policy(
            escalation_policy_data_id.clone(),
            body,
            UpdateOnCallEscalationPolicyOptionalParams::default(),
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

#####  Update On-Call escalation policy returns "OK" response
```
/**
 * Update On-Call escalation policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "escalation_policy" in the system
const ESCALATION_POLICY_DATA_ID = process.env
  .ESCALATION_POLICY_DATA_ID as string;
const ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID = process.env
  .ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID as string;

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

const params: v2.OnCallApiUpdateOnCallEscalationPolicyRequest = {
  body: {
    data: {
      attributes: {
        name: "Example-On-Call-updated",
        resolvePageOnPolicyEnd: false,
        retries: 0,
        steps: [
          {
            assignment: "default",
            escalateAfterSeconds: 3600,
            id: ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID,
            targets: [
              {
                id: USER_DATA_ID,
                type: "users",
              },
            ],
          },
        ],
      },
      id: ESCALATION_POLICY_DATA_ID,
      relationships: {
        teams: {
          data: [
            {
              id: DD_TEAM_DATA_ID,
              type: "teams",
            },
          ],
        },
      },
      type: "policies",
    },
  },
  policyId: ESCALATION_POLICY_DATA_ID,
};

apiInstance
  .updateOnCallEscalationPolicy(params)
  .then((data: v2.EscalationPolicy) => {
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
## [Get On-Call escalation policy](https://docs.datadoghq.com/api/latest/on-call/#get-on-call-escalation-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#get-on-call-escalation-policy-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.ap2.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.datadoghq.eu/api/v2/on-call/escalation-policies/{policy_id}https://api.ddog-gov.com/api/v2/on-call/escalation-policies/{policy_id}https://api.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.us3.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.us5.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}
### Overview
Get an On-Call escalation policy This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
policy_id [_required_]
string
The ID of the escalation policy
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `teams`, `steps`, `steps.targets`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallEscalationPolicy-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallEscalationPolicy-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallEscalationPolicy-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallEscalationPolicy-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallEscalationPolicy-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallEscalationPolicy-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Represents a complete escalation policy response, including policy data and optionally included related resources.
Field
Type
Description
data
object
Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type.
attributes
object
Defines the main attributes of an escalation policy, such as its name and behavior on policy end.
name [_required_]
string
Specifies the name of the escalation policy.
resolve_page_on_policy_end
boolean
Indicates whether the page is automatically resolved when the policy ends.
retries
int64
Specifies how many times the escalation sequence is retried if there is no response.
id
string
Specifies the unique identifier of the escalation policy.
relationships
object
Represents the relationships for an escalation policy, including references to steps and teams.
steps [_required_]
object
Defines the relationship to a collection of steps within an escalation policy. Contains an array of step data references.
data
[object]
An array of references to the steps defined in this escalation policy.
id [_required_]
string
Specifies the unique identifier for the step resource.
type [_required_]
enum
Indicates that the resource is of type `steps`. Allowed enum values: `steps`
default: `steps`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Indicates that the resource is of type `policies`. Allowed enum values: `policies`
default: `policies`
included
[ <oneOf>]
Provides any included related resources, such as steps or targets, returned with the policy.
Option 1
object
Represents a single step in an escalation policy, including its attributes, relationships, and resource type.
attributes
object
Defines attributes for an escalation policy step, such as assignment strategy and escalation timeout.
assignment
enum
Specifies how this escalation step will assign targets (example `default` or `round-robin`). Allowed enum values: `default,round-robin`
escalate_after_seconds
int64
Specifies how many seconds to wait before escalating to the next step.
id
string
Specifies the unique identifier of this escalation policy step.
relationships
object
Represents the relationship of an escalation policy step to its targets.
targets
object
A list of escalation targets for a step
data
[ <oneOf>]
The `EscalationTargets` `data`.
Option 1
object
Represents a team target for an escalation policy step, including the team's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the team resource.
type [_required_]
enum
Indicates that the resource is of type `teams`. Allowed enum values: `teams`
default: `teams`
Option 2
object
Represents a user target for an escalation policy step, including the user's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the user resource.
type [_required_]
enum
Indicates that the resource is of type `users`. Allowed enum values: `users`
default: `users`
Option 3
object
Represents a schedule target for an escalation policy step, including its ID and resource type. This is a shortcut for a configured schedule target with position set to 'current'.
id [_required_]
string
Specifies the unique identifier of the schedule resource.
type [_required_]
enum
Indicates that the resource is of type `schedules`. Allowed enum values: `schedules`
default: `schedules`
Option 4
object
Relationship reference to a configured schedule target.
id [_required_]
string
Specifies the unique identifier of the configured schedule target.
type [_required_]
enum
Indicates that the resource is of type `schedule_target`. Allowed enum values: `schedule_target`
default: `schedule_target`
type [_required_]
enum
Indicates that the resource is of type `steps`. Allowed enum values: `steps`
default: `steps`
Option 2
object
Represents a user object in the context of an escalation policy, including their `id`, type, and basic attributes.
attributes
object
Provides basic user information for an escalation policy, including a name and email address.
email
string
The user's email address.
name
string
The user's name.
status
enum
The user's status. Allowed enum values: `active,deactivated,pending`
id
string
The unique user identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 3
object
Represents the primary data object for a schedule, linking attributes and relationships.
attributes
object
Provides core properties of a schedule object such as its name and time zone.
name
string
A short name for the schedule.
time_zone
string
The time zone in which this schedule operates.
id
string
The schedule's unique identifier.
relationships
object
Groups the relationships for a schedule object, referencing layers and teams.
layers
object
Associates layers with this schedule in a data structure.
data
[object]
An array of layer references for this schedule.
id [_required_]
string
The unique identifier of the layer in this relationship.
type [_required_]
enum
Layers resource type. Allowed enum values: `layers`
default: `layers`
teams
object
Associates teams with this schedule in a data structure.
data
[object]
An array of team references for this schedule.
id [_required_]
string
The unique identifier of the team in this relationship.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
type [_required_]
enum
Schedules resource type. Allowed enum values: `schedules`
default: `schedules`
Option 4
object
Full resource representation of a configured schedule target with position (previous, current, or next).
attributes [_required_]
object
Attributes for a configured schedule target, including position.
position [_required_]
enum
Specifies the position of a schedule target (example `previous`, `current`, or `next`). Allowed enum values: `previous,current,next`
id [_required_]
string
Specifies the unique identifier of the configured schedule target.
relationships [_required_]
object
Represents the relationships of a configured schedule target.
schedule [_required_]
object
Holds the schedule reference for a configured schedule target.
data [_required_]
object
Represents a schedule target for an escalation policy step, including its ID and resource type. This is a shortcut for a configured schedule target with position set to 'current'.
id [_required_]
string
Specifies the unique identifier of the schedule resource.
type [_required_]
enum
Indicates that the resource is of type `schedules`. Allowed enum values: `schedules`
default: `schedules`
type [_required_]
enum
Indicates that the resource is of type `schedule_target`. Allowed enum values: `schedule_target`
default: `schedule_target`
Option 5
object
Provides a reference to a team, including ID, type, and basic attributes/relationships.
attributes
object
Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
avatar
string
URL or reference for the team's avatar (if available).
description
string
A short text describing the team.
handle
string
A unique handle/slug for the team.
name
string
The full, human-readable name of the team.
id
string
The team's unique identifier.
type [_required_]
enum
Teams resource type. Allowed enum values: `teams`
default: `teams`
```
{
  "data": {
    "attributes": {
      "name": "Escalation Policy 1",
      "resolve_page_on_policy_end": true,
      "retries": 2
    },
    "id": "00000000-aba1-0000-0000-000000000000",
    "relationships": {
      "steps": {
        "data": [
          {
            "id": "00000000-aba1-0000-0000-000000000000",
            "type": "steps"
          }
        ]
      },
      "teams": {
        "data": [
          {
            "id": "00000000-da3a-0000-0000-000000000000",
            "type": "teams"
          }
        ]
      }
    },
    "type": "policies"
  },
  "included": [
    {
      "attributes": {
        "avatar": "",
        "description": "Team 1 description",
        "handle": "team1",
        "name": "Team 1"
      },
      "id": "00000000-da3a-0000-0000-000000000000",
      "type": "teams"
    },
    {
      "attributes": {
        "assignment": "default",
        "escalate_after_seconds": 3600
      },
      "id": "00000000-aba1-0000-0000-000000000000",
      "relationships": {
        "targets": {
          "data": [
            {
              "id": "00000000-aba1-0000-0000-000000000000",
              "type": "users"
            },
            {
              "id": "00000000-aba2-0000-0000-000000000000",
              "type": "schedules"
            },
            {
              "id": "00000000-aba2-0000-0000-000000000000_previous",
              "type": "schedule_target"
            },
            {
              "id": "00000000-aba3-0000-0000-000000000000",
              "type": "teams"
            }
          ]
        }
      },
      "type": "steps"
    },
    {
      "id": "00000000-aba1-0000-0000-000000000000",
      "type": "users"
    },
    {
      "id": "00000000-aba2-0000-0000-000000000000",
      "type": "schedules"
    },
    {
      "attributes": {
        "position": "previous"
      },
      "id": "00000000-aba2-0000-0000-000000000000_previous",
      "relationships": {
        "schedule": {
          "data": {
            "id": "00000000-aba2-0000-0000-000000000000",
            "type": "schedules"
          }
        }
      },
      "type": "schedule_target"
    },
    {
      "id": "00000000-aba3-0000-0000-000000000000",
      "type": "teams"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Get On-Call escalation policy
Copy
```
                  # Path parameters  
export policy_id="a3000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/escalation-policies/${policy_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get On-Call escalation policy
```
"""
Get On-Call escalation policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = environ["ESCALATION_POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_on_call_escalation_policy(
        policy_id=ESCALATION_POLICY_DATA_ID,
        include="steps.targets",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get On-Call escalation policy
```
# Get On-Call escalation policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = ENV["ESCALATION_POLICY_DATA_ID"]
opts = {
  include: "steps.targets",
}
p api_instance.get_on_call_escalation_policy(ESCALATION_POLICY_DATA_ID, opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get On-Call escalation policy
```
// Get On-Call escalation policy returns "OK" response

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
	// there is a valid "escalation_policy" in the system
	EscalationPolicyDataID := os.Getenv("ESCALATION_POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.GetOnCallEscalationPolicy(ctx, EscalationPolicyDataID, *datadogV2.NewGetOnCallEscalationPolicyOptionalParameters().WithInclude("steps.targets"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.GetOnCallEscalationPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.GetOnCallEscalationPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get On-Call escalation policy
```
// Get On-Call escalation policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.api.OnCallApi.GetOnCallEscalationPolicyOptionalParameters;
import com.datadog.api.client.v2.model.EscalationPolicy;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "escalation_policy" in the system
    String ESCALATION_POLICY_DATA_ID = System.getenv("ESCALATION_POLICY_DATA_ID");

    try {
      EscalationPolicy result =
          apiInstance.getOnCallEscalationPolicy(
              ESCALATION_POLICY_DATA_ID,
              new GetOnCallEscalationPolicyOptionalParameters().include("steps.targets"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#getOnCallEscalationPolicy");
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

#####  Get On-Call escalation policy
```
// Get On-Call escalation policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::GetOnCallEscalationPolicyOptionalParams;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "escalation_policy" in the system
    let escalation_policy_data_id = std::env::var("ESCALATION_POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .get_on_call_escalation_policy(
            escalation_policy_data_id.clone(),
            GetOnCallEscalationPolicyOptionalParams::default().include("steps.targets".to_string()),
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

#####  Get On-Call escalation policy
```
/**
 * Get On-Call escalation policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "escalation_policy" in the system
const ESCALATION_POLICY_DATA_ID = process.env
  .ESCALATION_POLICY_DATA_ID as string;

const params: v2.OnCallApiGetOnCallEscalationPolicyRequest = {
  policyId: ESCALATION_POLICY_DATA_ID,
  include: "steps.targets",
};

apiInstance
  .getOnCallEscalationPolicy(params)
  .then((data: v2.EscalationPolicy) => {
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
## [Delete On-Call escalation policy](https://docs.datadoghq.com/api/latest/on-call/#delete-on-call-escalation-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#delete-on-call-escalation-policy-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.ap2.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.datadoghq.eu/api/v2/on-call/escalation-policies/{policy_id}https://api.ddog-gov.com/api/v2/on-call/escalation-policies/{policy_id}https://api.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.us3.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}https://api.us5.datadoghq.com/api/v2/on-call/escalation-policies/{policy_id}
### Overview
Delete an On-Call escalation policy This endpoint requires the `on_call_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
policy_id [_required_]
string
The ID of the escalation policy
### Response
  * [204](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallEscalationPolicy-204-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallEscalationPolicy-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallEscalationPolicy-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallEscalationPolicy-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#DeleteOnCallEscalationPolicy-429-v2)


No Content
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Delete On-Call escalation policy
Copy
```
                  # Path parameters  
export policy_id="a3000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/escalation-policies/${policy_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete On-Call escalation policy
```
"""
Delete On-Call escalation policy returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = environ["ESCALATION_POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    api_instance.delete_on_call_escalation_policy(
        policy_id=ESCALATION_POLICY_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete On-Call escalation policy
```
# Delete On-Call escalation policy returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = ENV["ESCALATION_POLICY_DATA_ID"]
api_instance.delete_on_call_escalation_policy(ESCALATION_POLICY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete On-Call escalation policy
```
// Delete On-Call escalation policy returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "escalation_policy" in the system
	EscalationPolicyDataID := os.Getenv("ESCALATION_POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	r, err := api.DeleteOnCallEscalationPolicy(ctx, EscalationPolicyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.DeleteOnCallEscalationPolicy`: %v\n", err)
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

#####  Delete On-Call escalation policy
```
// Delete On-Call escalation policy returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "escalation_policy" in the system
    String ESCALATION_POLICY_DATA_ID = System.getenv("ESCALATION_POLICY_DATA_ID");

    try {
      apiInstance.deleteOnCallEscalationPolicy(ESCALATION_POLICY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#deleteOnCallEscalationPolicy");
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

#####  Delete On-Call escalation policy
```
// Delete On-Call escalation policy returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "escalation_policy" in the system
    let escalation_policy_data_id = std::env::var("ESCALATION_POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .delete_on_call_escalation_policy(escalation_policy_data_id.clone())
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

#####  Delete On-Call escalation policy
```
/**
 * Delete On-Call escalation policy returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "escalation_policy" in the system
const ESCALATION_POLICY_DATA_ID = process.env
  .ESCALATION_POLICY_DATA_ID as string;

const params: v2.OnCallApiDeleteOnCallEscalationPolicyRequest = {
  policyId: ESCALATION_POLICY_DATA_ID,
};

apiInstance
  .deleteOnCallEscalationPolicy(params)
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
## [Get On-Call team routing rules](https://docs.datadoghq.com/api/latest/on-call/#get-on-call-team-routing-rules)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#get-on-call-team-routing-rules-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.ap2.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.datadoghq.eu/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.ddog-gov.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.us3.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.us5.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-rules
### Overview
Get a team’s On-Call routing rules This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
The team ID
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `rules`, `rules.policy`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallTeamRoutingRules-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#GetOnCallTeamRoutingRules-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Represents a complete set of team routing rules, including data and optionally included related resources.
Field
Type
Description
data
object
Represents the top-level data object for team routing rules, containing the ID, relationships, and resource type.
id
string
Specifies the unique identifier of this team routing rules record.
relationships
object
Specifies relationships for team routing rules, including rule references.
rules
object
Holds references to a set of routing rules in a relationship.
data
[object]
An array of references to the routing rules associated with this team.
id [_required_]
string
Specifies the unique identifier for the related routing rule.
type [_required_]
enum
Indicates that the resource is of type 'team_routing_rules'. Allowed enum values: `team_routing_rules`
default: `team_routing_rules`
type [_required_]
enum
Team routing rules resource type. Allowed enum values: `team_routing_rules`
default: `team_routing_rules`
included
[ <oneOf>]
Provides related routing rules or other included resources.
Option 1
object
Represents a routing rule, including its attributes, relationships, and unique identifier.
attributes
object
Defines the configurable attributes of a routing rule, such as actions, query, time restriction, and urgency.
actions
[ <oneOf>]
Specifies the list of actions to perform when the routing rule matches.
Option 1
object
Sends a message to a Slack channel.
channel [_required_]
string
The channel ID.
type [_required_]
enum
Indicates that the action is a send Slack message action. Allowed enum values: `send_slack_message`
default: `send_slack_message`
workspace [_required_]
string
The workspace ID.
Option 2
object
Sends a message to a Microsoft Teams channel.
channel [_required_]
string
The channel ID.
team [_required_]
string
The team ID.
tenant [_required_]
string
The tenant ID.
type [_required_]
enum
Indicates that the action is a send Microsoft Teams message action. Allowed enum values: `send_teams_message`
default: `send_teams_message`
query
string
Defines the query or condition that triggers this routing rule.
time_restriction
object
Holds time zone information and a list of time restrictions for a routing rule.
restrictions [_required_]
[object]
Defines the list of time-based restrictions.
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
time_zone [_required_]
string
Specifies the time zone applicable to the restrictions.
urgency
enum
Specifies the level of urgency for a routing rule (low, high, or dynamic). Allowed enum values: `low,high,dynamic`
id
string
Specifies the unique identifier of this routing rule.
relationships
object
Specifies relationships for a routing rule, linking to associated policy resources.
policy
object
Defines the relationship that links a routing rule to a policy.
data
object
Represents the policy data reference, containing the policy's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the policy.
type [_required_]
enum
Indicates that the resource is of type 'policies'. Allowed enum values: `policies`
default: `policies`
type [_required_]
enum
Team routing rules resource type. Allowed enum values: `team_routing_rules`
default: `team_routing_rules`
```
{
  "data": {
    "id": "27590dae-47be-4a7d-9abf-8f4e45124020",
    "relationships": {
      "rules": {
        "data": [
          {
            "id": "03aff2d6-6cbf-496c-997f-a857bbe9a94a",
            "type": "team_routing_rules"
          },
          {
            "id": "03aff2d6-6cbf-496c-997f-a857bbe9a94a",
            "type": "team_routing_rules"
          }
        ]
      }
    },
    "type": "team_routing_rules"
  },
  "included": [
    {
      "attributes": {
        "actions": null,
        "query": "tags.service:test",
        "time_restriction": {
          "restrictions": [
            {
              "end_day": "monday",
              "end_time": "17:00:00",
              "start_day": "monday",
              "start_time": "09:00:00"
            },
            {
              "end_day": "tuesday",
              "end_time": "17:00:00",
              "start_day": "tuesday",
              "start_time": "09:00:00"
            }
          ],
          "time_zone": ""
        },
        "urgency": "high"
      },
      "id": "03aff2d6-6cbf-496c-997f-a857bbe9a94a",
      "relationships": {
        "policy": {
          "data": null
        }
      },
      "type": "team_routing_rules"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Get On-Call team routing rules
Copy
```
                  # Path parameters  
export team_id="27590dae-47be-4a7d-9abf-8f4e45124020"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/teams/${team_id}/routing-rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get On-Call team routing rules
```
"""
Get On-Call team routing rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_on_call_team_routing_rules(
        team_id="27590dae-47be-4a7d-9abf-8f4e45124020",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get On-Call team routing rules
```
# Get On-Call team routing rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new
p api_instance.get_on_call_team_routing_rules("27590dae-47be-4a7d-9abf-8f4e45124020")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get On-Call team routing rules
```
// Get On-Call team routing rules returns "OK" response

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
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.GetOnCallTeamRoutingRules(ctx, "27590dae-47be-4a7d-9abf-8f4e45124020", *datadogV2.NewGetOnCallTeamRoutingRulesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.GetOnCallTeamRoutingRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.GetOnCallTeamRoutingRules`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get On-Call team routing rules
```
// Get On-Call team routing rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.TeamRoutingRules;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    try {
      TeamRoutingRules result =
          apiInstance.getOnCallTeamRoutingRules("27590dae-47be-4a7d-9abf-8f4e45124020");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#getOnCallTeamRoutingRules");
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

#####  Get On-Call team routing rules
```
// Get On-Call team routing rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::GetOnCallTeamRoutingRulesOptionalParams;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .get_on_call_team_routing_rules(
            "27590dae-47be-4a7d-9abf-8f4e45124020".to_string(),
            GetOnCallTeamRoutingRulesOptionalParams::default(),
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

#####  Get On-Call team routing rules
```
/**
 * Get On-Call team routing rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

const params: v2.OnCallApiGetOnCallTeamRoutingRulesRequest = {
  teamId: "27590dae-47be-4a7d-9abf-8f4e45124020",
};

apiInstance
  .getOnCallTeamRoutingRules(params)
  .then((data: v2.TeamRoutingRules) => {
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
## [Set On-Call team routing rules](https://docs.datadoghq.com/api/latest/on-call/#set-on-call-team-routing-rules)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#set-on-call-team-routing-rules-v2)


PUT https://api.ap1.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.ap2.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.datadoghq.eu/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.ddog-gov.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.us3.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-ruleshttps://api.us5.datadoghq.com/api/v2/on-call/teams/{team_id}/routing-rules
### Overview
Set a team’s On-Call routing rules This endpoint requires the `on_call_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
The team ID
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `rules`, `rules.policy`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data
object
Holds the data necessary to create or update team routing rules, including attributes, ID, and resource type.
attributes
object
Represents the attributes of a request to update or create team routing rules.
rules
[object]
A list of routing rule items that define how incoming pages should be handled.
actions
[ <oneOf>]
Specifies the list of actions to perform when the routing rule is matched.
Option 1
object
Sends a message to a Slack channel.
channel [_required_]
string
The channel ID.
type [_required_]
enum
Indicates that the action is a send Slack message action. Allowed enum values: `send_slack_message`
default: `send_slack_message`
workspace [_required_]
string
The workspace ID.
Option 2
object
Sends a message to a Microsoft Teams channel.
channel [_required_]
string
The channel ID.
team [_required_]
string
The team ID.
tenant [_required_]
string
The tenant ID.
type [_required_]
enum
Indicates that the action is a send Microsoft Teams message action. Allowed enum values: `send_teams_message`
default: `send_teams_message`
policy_id
string
Identifies the policy to be applied when this routing rule matches.
query
string
Defines the query or condition that triggers this routing rule.
time_restriction
object
Holds time zone information and a list of time restrictions for a routing rule.
restrictions [_required_]
[object]
Defines the list of time-based restrictions.
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
time_zone [_required_]
string
Specifies the time zone applicable to the restrictions.
urgency
enum
Specifies the level of urgency for a routing rule (low, high, or dynamic). Allowed enum values: `low,high,dynamic`
id
string
Specifies the unique identifier for this set of team routing rules.
type [_required_]
enum
Team routing rules resource type. Allowed enum values: `team_routing_rules`
default: `team_routing_rules`
```
{
  "data": {
    "attributes": {
      "rules": [
        {
          "actions": [
            {
              "channel": "channel",
              "type": "send_slack_message",
              "workspace": "workspace"
            }
          ],
          "query": "tags.service:test",
          "time_restriction": {
            "time_zone": "Europe/Paris",
            "restrictions": [
              {
                "end_day": "monday",
                "end_time": "17:00:00",
                "start_day": "monday",
                "start_time": "09:00:00"
              },
              {
                "end_day": "tuesday",
                "end_time": "17:00:00",
                "start_day": "tuesday",
                "start_time": "09:00:00"
              }
            ]
          }
        },
        {
          "policy_id": "ab000000-0000-0000-0000-000000000000",
          "query": "",
          "urgency": "low"
        }
      ]
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "team_routing_rules"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#SetOnCallTeamRoutingRules-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#SetOnCallTeamRoutingRules-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Represents a complete set of team routing rules, including data and optionally included related resources.
Field
Type
Description
data
object
Represents the top-level data object for team routing rules, containing the ID, relationships, and resource type.
id
string
Specifies the unique identifier of this team routing rules record.
relationships
object
Specifies relationships for team routing rules, including rule references.
rules
object
Holds references to a set of routing rules in a relationship.
data
[object]
An array of references to the routing rules associated with this team.
id [_required_]
string
Specifies the unique identifier for the related routing rule.
type [_required_]
enum
Indicates that the resource is of type 'team_routing_rules'. Allowed enum values: `team_routing_rules`
default: `team_routing_rules`
type [_required_]
enum
Team routing rules resource type. Allowed enum values: `team_routing_rules`
default: `team_routing_rules`
included
[ <oneOf>]
Provides related routing rules or other included resources.
Option 1
object
Represents a routing rule, including its attributes, relationships, and unique identifier.
attributes
object
Defines the configurable attributes of a routing rule, such as actions, query, time restriction, and urgency.
actions
[ <oneOf>]
Specifies the list of actions to perform when the routing rule matches.
Option 1
object
Sends a message to a Slack channel.
channel [_required_]
string
The channel ID.
type [_required_]
enum
Indicates that the action is a send Slack message action. Allowed enum values: `send_slack_message`
default: `send_slack_message`
workspace [_required_]
string
The workspace ID.
Option 2
object
Sends a message to a Microsoft Teams channel.
channel [_required_]
string
The channel ID.
team [_required_]
string
The team ID.
tenant [_required_]
string
The tenant ID.
type [_required_]
enum
Indicates that the action is a send Microsoft Teams message action. Allowed enum values: `send_teams_message`
default: `send_teams_message`
query
string
Defines the query or condition that triggers this routing rule.
time_restriction
object
Holds time zone information and a list of time restrictions for a routing rule.
restrictions [_required_]
[object]
Defines the list of time-based restrictions.
end_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
end_time
string
Specifies the ending time for this restriction.
start_day
enum
A day of the week. Allowed enum values: `monday,tuesday,wednesday,thursday,friday,saturday,sunday`
start_time
string
Specifies the starting time for this restriction.
time_zone [_required_]
string
Specifies the time zone applicable to the restrictions.
urgency
enum
Specifies the level of urgency for a routing rule (low, high, or dynamic). Allowed enum values: `low,high,dynamic`
id
string
Specifies the unique identifier of this routing rule.
relationships
object
Specifies relationships for a routing rule, linking to associated policy resources.
policy
object
Defines the relationship that links a routing rule to a policy.
data
object
Represents the policy data reference, containing the policy's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the policy.
type [_required_]
enum
Indicates that the resource is of type 'policies'. Allowed enum values: `policies`
default: `policies`
type [_required_]
enum
Team routing rules resource type. Allowed enum values: `team_routing_rules`
default: `team_routing_rules`
```
{
  "data": {
    "id": "27590dae-47be-4a7d-9abf-8f4e45124020",
    "relationships": {
      "rules": {
        "data": [
          {
            "id": "03aff2d6-6cbf-496c-997f-a857bbe9a94a",
            "type": "team_routing_rules"
          },
          {
            "id": "03aff2d6-6cbf-496c-997f-a857bbe9a94a",
            "type": "team_routing_rules"
          }
        ]
      }
    },
    "type": "team_routing_rules"
  },
  "included": [
    {
      "attributes": {
        "actions": null,
        "query": "tags.service:test",
        "time_restriction": {
          "restrictions": [
            {
              "end_day": "monday",
              "end_time": "17:00:00",
              "start_day": "monday",
              "start_time": "09:00:00"
            },
            {
              "end_day": "tuesday",
              "end_time": "17:00:00",
              "start_day": "tuesday",
              "start_time": "09:00:00"
            }
          ],
          "time_zone": ""
        },
        "urgency": "high"
      },
      "id": "03aff2d6-6cbf-496c-997f-a857bbe9a94a",
      "relationships": {
        "policy": {
          "data": null
        }
      },
      "type": "team_routing_rules"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Set On-Call team routing rules returns "OK" response
Copy
```
                          # Path parameters  
export team_id="27590dae-47be-4a7d-9abf-8f4e45124020"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/teams/${team_id}/routing-rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "rules": [
        {
          "actions": [
            {
              "channel": "channel",
              "type": "send_slack_message",
              "workspace": "workspace"
            }
          ],
          "query": "tags.service:test",
          "time_restriction": {
            "time_zone": "Europe/Paris",
            "restrictions": [
              {
                "end_day": "monday",
                "end_time": "17:00:00",
                "start_day": "monday",
                "start_time": "09:00:00"
              },
              {
                "end_day": "tuesday",
                "end_time": "17:00:00",
                "start_day": "tuesday",
                "start_time": "09:00:00"
              }
            ]
          }
        },
        {
          "policy_id": "ab000000-0000-0000-0000-000000000000",
          "query": "",
          "urgency": "low"
        }
      ]
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "team_routing_rules"
  }
}
EOF  

                        
```

#####  Set On-Call team routing rules returns "OK" response
```
// Set On-Call team routing rules returns "OK" response

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

	// there is a valid "escalation_policy" in the system
	EscalationPolicyDataID := os.Getenv("ESCALATION_POLICY_DATA_ID")

	body := datadogV2.TeamRoutingRulesRequest{
		Data: &datadogV2.TeamRoutingRulesRequestData{
			Attributes: &datadogV2.TeamRoutingRulesRequestDataAttributes{
				Rules: []datadogV2.TeamRoutingRulesRequestRule{
					{
						Actions: []datadogV2.RoutingRuleAction{
							datadogV2.RoutingRuleAction{
								SendSlackMessageAction: &datadogV2.SendSlackMessageAction{
									Channel:   "channel",
									Type:      datadogV2.SENDSLACKMESSAGEACTIONTYPE_SEND_SLACK_MESSAGE,
									Workspace: "workspace",
								}},
						},
						Query: datadog.PtrString("tags.service:test"),
						TimeRestriction: &datadogV2.TimeRestrictions{
							TimeZone: "Europe/Paris",
							Restrictions: []datadogV2.TimeRestriction{
								{
									EndDay:    datadogV2.WEEKDAY_MONDAY.Ptr(),
									EndTime:   datadog.PtrString("17:00:00"),
									StartDay:  datadogV2.WEEKDAY_MONDAY.Ptr(),
									StartTime: datadog.PtrString("09:00:00"),
								},
								{
									EndDay:    datadogV2.WEEKDAY_TUESDAY.Ptr(),
									EndTime:   datadog.PtrString("17:00:00"),
									StartDay:  datadogV2.WEEKDAY_TUESDAY.Ptr(),
									StartTime: datadog.PtrString("09:00:00"),
								},
							},
						},
					},
					{
						PolicyId: datadog.PtrString(EscalationPolicyDataID),
						Query:    datadog.PtrString(""),
						Urgency:  datadogV2.URGENCY_LOW.Ptr(),
					},
				},
			},
			Id:   datadog.PtrString(DdTeamDataID),
			Type: datadogV2.TEAMROUTINGRULESREQUESTDATATYPE_TEAM_ROUTING_RULES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.SetOnCallTeamRoutingRules(ctx, DdTeamDataID, body, *datadogV2.NewSetOnCallTeamRoutingRulesOptionalParameters().WithInclude("rules"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.SetOnCallTeamRoutingRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.SetOnCallTeamRoutingRules`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Set On-Call team routing rules returns "OK" response
```
// Set On-Call team routing rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.api.OnCallApi.SetOnCallTeamRoutingRulesOptionalParameters;
import com.datadog.api.client.v2.model.RoutingRuleAction;
import com.datadog.api.client.v2.model.SendSlackMessageAction;
import com.datadog.api.client.v2.model.SendSlackMessageActionType;
import com.datadog.api.client.v2.model.TeamRoutingRules;
import com.datadog.api.client.v2.model.TeamRoutingRulesRequest;
import com.datadog.api.client.v2.model.TeamRoutingRulesRequestData;
import com.datadog.api.client.v2.model.TeamRoutingRulesRequestDataAttributes;
import com.datadog.api.client.v2.model.TeamRoutingRulesRequestDataType;
import com.datadog.api.client.v2.model.TeamRoutingRulesRequestRule;
import com.datadog.api.client.v2.model.TimeRestriction;
import com.datadog.api.client.v2.model.TimeRestrictions;
import com.datadog.api.client.v2.model.Urgency;
import com.datadog.api.client.v2.model.Weekday;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "dd_team" in the system
    String DD_TEAM_DATA_ID = System.getenv("DD_TEAM_DATA_ID");

    // there is a valid "escalation_policy" in the system
    String ESCALATION_POLICY_DATA_ID = System.getenv("ESCALATION_POLICY_DATA_ID");

    TeamRoutingRulesRequest body =
        new TeamRoutingRulesRequest()
            .data(
                new TeamRoutingRulesRequestData()
                    .attributes(
                        new TeamRoutingRulesRequestDataAttributes()
                            .rules(
                                Arrays.asList(
                                    new TeamRoutingRulesRequestRule()
                                        .actions(
                                            Collections.singletonList(
                                                new RoutingRuleAction(
                                                    new SendSlackMessageAction()
                                                        .channel("channel")
                                                        .type(
                                                            SendSlackMessageActionType
                                                                .SEND_SLACK_MESSAGE)
                                                        .workspace("workspace"))))
                                        .query("tags.service:test")
                                        .timeRestriction(
                                            new TimeRestrictions()
                                                .timeZone("Europe/Paris")
                                                .restrictions(
                                                    Arrays.asList(
                                                        new TimeRestriction()
                                                            .endDay(Weekday.MONDAY)
                                                            .endTime("17:00:00")
                                                            .startDay(Weekday.MONDAY)
                                                            .startTime("09:00:00"),
                                                        new TimeRestriction()
                                                            .endDay(Weekday.TUESDAY)
                                                            .endTime("17:00:00")
                                                            .startDay(Weekday.TUESDAY)
                                                            .startTime("09:00:00")))),
                                    new TeamRoutingRulesRequestRule()
                                        .policyId(ESCALATION_POLICY_DATA_ID)
                                        .query("")
                                        .urgency(Urgency.LOW))))
                    .id(DD_TEAM_DATA_ID)
                    .type(TeamRoutingRulesRequestDataType.TEAM_ROUTING_RULES));

    try {
      TeamRoutingRules result =
          apiInstance.setOnCallTeamRoutingRules(
              DD_TEAM_DATA_ID,
              body,
              new SetOnCallTeamRoutingRulesOptionalParameters().include("rules"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#setOnCallTeamRoutingRules");
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

#####  Set On-Call team routing rules returns "OK" response
```
"""
Set On-Call team routing rules returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.send_slack_message_action import SendSlackMessageAction
from datadog_api_client.v2.model.send_slack_message_action_type import SendSlackMessageActionType
from datadog_api_client.v2.model.team_routing_rules_request import TeamRoutingRulesRequest
from datadog_api_client.v2.model.team_routing_rules_request_data import TeamRoutingRulesRequestData
from datadog_api_client.v2.model.team_routing_rules_request_data_attributes import TeamRoutingRulesRequestDataAttributes
from datadog_api_client.v2.model.team_routing_rules_request_data_type import TeamRoutingRulesRequestDataType
from datadog_api_client.v2.model.team_routing_rules_request_rule import TeamRoutingRulesRequestRule
from datadog_api_client.v2.model.time_restriction import TimeRestriction
from datadog_api_client.v2.model.time_restrictions import TimeRestrictions
from datadog_api_client.v2.model.urgency import Urgency
from datadog_api_client.v2.model.weekday import Weekday

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = environ["ESCALATION_POLICY_DATA_ID"]

body = TeamRoutingRulesRequest(
    data=TeamRoutingRulesRequestData(
        attributes=TeamRoutingRulesRequestDataAttributes(
            rules=[
                TeamRoutingRulesRequestRule(
                    actions=[
                        SendSlackMessageAction(
                            channel="channel",
                            type=SendSlackMessageActionType.SEND_SLACK_MESSAGE,
                            workspace="workspace",
                        ),
                    ],
                    query="tags.service:test",
                    time_restriction=TimeRestrictions(
                        time_zone="Europe/Paris",
                        restrictions=[
                            TimeRestriction(
                                end_day=Weekday.MONDAY,
                                end_time="17:00:00",
                                start_day=Weekday.MONDAY,
                                start_time="09:00:00",
                            ),
                            TimeRestriction(
                                end_day=Weekday.TUESDAY,
                                end_time="17:00:00",
                                start_day=Weekday.TUESDAY,
                                start_time="09:00:00",
                            ),
                        ],
                    ),
                ),
                TeamRoutingRulesRequestRule(
                    policy_id=ESCALATION_POLICY_DATA_ID,
                    query="",
                    urgency=Urgency.LOW,
                ),
            ],
        ),
        id=DD_TEAM_DATA_ID,
        type=TeamRoutingRulesRequestDataType.TEAM_ROUTING_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.set_on_call_team_routing_rules(team_id=DD_TEAM_DATA_ID, include="rules", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Set On-Call team routing rules returns "OK" response
```
# Set On-Call team routing rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = ENV["DD_TEAM_DATA_ID"]

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = ENV["ESCALATION_POLICY_DATA_ID"]

body = DatadogAPIClient::V2::TeamRoutingRulesRequest.new({
  data: DatadogAPIClient::V2::TeamRoutingRulesRequestData.new({
    attributes: DatadogAPIClient::V2::TeamRoutingRulesRequestDataAttributes.new({
      rules: [
        DatadogAPIClient::V2::TeamRoutingRulesRequestRule.new({
          actions: [
            DatadogAPIClient::V2::SendSlackMessageAction.new({
              channel: "channel",
              type: DatadogAPIClient::V2::SendSlackMessageActionType::SEND_SLACK_MESSAGE,
              workspace: "workspace",
            }),
          ],
          query: "tags.service:test",
          time_restriction: DatadogAPIClient::V2::TimeRestrictions.new({
            time_zone: "Europe/Paris",
            restrictions: [
              DatadogAPIClient::V2::TimeRestriction.new({
                end_day: DatadogAPIClient::V2::Weekday::MONDAY,
                end_time: "17:00:00",
                start_day: DatadogAPIClient::V2::Weekday::MONDAY,
                start_time: "09:00:00",
              }),
              DatadogAPIClient::V2::TimeRestriction.new({
                end_day: DatadogAPIClient::V2::Weekday::TUESDAY,
                end_time: "17:00:00",
                start_day: DatadogAPIClient::V2::Weekday::TUESDAY,
                start_time: "09:00:00",
              }),
            ],
          }),
        }),
        DatadogAPIClient::V2::TeamRoutingRulesRequestRule.new({
          policy_id: ESCALATION_POLICY_DATA_ID,
          query: "",
          urgency: DatadogAPIClient::V2::Urgency::LOW,
        }),
      ],
    }),
    id: DD_TEAM_DATA_ID,
    type: DatadogAPIClient::V2::TeamRoutingRulesRequestDataType::TEAM_ROUTING_RULES,
  }),
})
opts = {
  include: "rules",
}
p api_instance.set_on_call_team_routing_rules(DD_TEAM_DATA_ID, body, opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Set On-Call team routing rules returns "OK" response
```
// Set On-Call team routing rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;
use datadog_api_client::datadogV2::api_on_call::SetOnCallTeamRoutingRulesOptionalParams;
use datadog_api_client::datadogV2::model::RoutingRuleAction;
use datadog_api_client::datadogV2::model::SendSlackMessageAction;
use datadog_api_client::datadogV2::model::SendSlackMessageActionType;
use datadog_api_client::datadogV2::model::TeamRoutingRulesRequest;
use datadog_api_client::datadogV2::model::TeamRoutingRulesRequestData;
use datadog_api_client::datadogV2::model::TeamRoutingRulesRequestDataAttributes;
use datadog_api_client::datadogV2::model::TeamRoutingRulesRequestDataType;
use datadog_api_client::datadogV2::model::TeamRoutingRulesRequestRule;
use datadog_api_client::datadogV2::model::TimeRestriction;
use datadog_api_client::datadogV2::model::TimeRestrictions;
use datadog_api_client::datadogV2::model::Urgency;
use datadog_api_client::datadogV2::model::Weekday;

#[tokio::main]
async fn main() {
    // there is a valid "dd_team" in the system
    let dd_team_data_id = std::env::var("DD_TEAM_DATA_ID").unwrap();

    // there is a valid "escalation_policy" in the system
    let escalation_policy_data_id = std::env::var("ESCALATION_POLICY_DATA_ID").unwrap();
    let body = TeamRoutingRulesRequest::new().data(
        TeamRoutingRulesRequestData::new(TeamRoutingRulesRequestDataType::TEAM_ROUTING_RULES)
            .attributes(TeamRoutingRulesRequestDataAttributes::new().rules(vec![
                            TeamRoutingRulesRequestRule::new()
                                .actions(
                                    vec![
                                        RoutingRuleAction::SendSlackMessageAction(
                                            Box::new(
                                                SendSlackMessageAction::new(
                                                    "channel".to_string(),
                                                    SendSlackMessageActionType::SEND_SLACK_MESSAGE,
                                                    "workspace".to_string(),
                                                ),
                                            ),
                                        )
                                    ],
                                )
                                .query("tags.service:test".to_string())
                                .time_restriction(
                                    TimeRestrictions::new(
                                        vec![
                                            TimeRestriction::new()
                                                .end_day(Weekday::MONDAY)
                                                .end_time("17:00:00".to_string())
                                                .start_day(Weekday::MONDAY)
                                                .start_time("09:00:00".to_string()),
                                            TimeRestriction::new()
                                                .end_day(Weekday::TUESDAY)
                                                .end_time("17:00:00".to_string())
                                                .start_day(Weekday::TUESDAY)
                                                .start_time("09:00:00".to_string())
                                        ],
                                        "Europe/Paris".to_string(),
                                    ),
                                ),
                            TeamRoutingRulesRequestRule::new()
                                .policy_id(escalation_policy_data_id.clone())
                                .query("".to_string())
                                .urgency(Urgency::LOW)
                        ]))
            .id(dd_team_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .set_on_call_team_routing_rules(
            dd_team_data_id.clone(),
            body,
            SetOnCallTeamRoutingRulesOptionalParams::default().include("rules".to_string()),
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

#####  Set On-Call team routing rules returns "OK" response
```
/**
 * Set On-Call team routing rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "dd_team" in the system
const DD_TEAM_DATA_ID = process.env.DD_TEAM_DATA_ID as string;

// there is a valid "escalation_policy" in the system
const ESCALATION_POLICY_DATA_ID = process.env
  .ESCALATION_POLICY_DATA_ID as string;

const params: v2.OnCallApiSetOnCallTeamRoutingRulesRequest = {
  body: {
    data: {
      attributes: {
        rules: [
          {
            actions: [
              {
                channel: "channel",
                type: "send_slack_message",
                workspace: "workspace",
              },
            ],
            query: "tags.service:test",
            timeRestriction: {
              timeZone: "Europe/Paris",
              restrictions: [
                {
                  endDay: "monday",
                  endTime: "17:00:00",
                  startDay: "monday",
                  startTime: "09:00:00",
                },
                {
                  endDay: "tuesday",
                  endTime: "17:00:00",
                  startDay: "tuesday",
                  startTime: "09:00:00",
                },
              ],
            },
          },
          {
            policyId: ESCALATION_POLICY_DATA_ID,
            query: "",
            urgency: "low",
          },
        ],
      },
      id: DD_TEAM_DATA_ID,
      type: "team_routing_rules",
    },
  },
  teamId: DD_TEAM_DATA_ID,
  include: "rules",
};

apiInstance
  .setOnCallTeamRoutingRules(params)
  .then((data: v2.TeamRoutingRules) => {
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
## [Get scheduled on-call user](https://docs.datadoghq.com/api/latest/on-call/#get-scheduled-on-call-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#get-scheduled-on-call-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/schedules/{schedule_id}/on-callhttps://api.ap2.datadoghq.com/api/v2/on-call/schedules/{schedule_id}/on-callhttps://api.datadoghq.eu/api/v2/on-call/schedules/{schedule_id}/on-callhttps://api.ddog-gov.com/api/v2/on-call/schedules/{schedule_id}/on-callhttps://api.datadoghq.com/api/v2/on-call/schedules/{schedule_id}/on-callhttps://api.us3.datadoghq.com/api/v2/on-call/schedules/{schedule_id}/on-callhttps://api.us5.datadoghq.com/api/v2/on-call/schedules/{schedule_id}/on-call
### Overview
Retrieves the user who is on-call for the specified schedule at a given time. This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
schedule_id [_required_]
string
The ID of the schedule.
#### Query Strings
Name
Type
Description
include
string
Specifies related resources to include in the response as a comma-separated list. Allowed value: `user`.
filter[at_ts]
string
Retrieves the on-call user at the given timestamp (ISO-8601). Defaults to the current time if omitted."
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#GetScheduleOnCallUser-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#GetScheduleOnCallUser-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#GetScheduleOnCallUser-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#GetScheduleOnCallUser-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#GetScheduleOnCallUser-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#GetScheduleOnCallUser-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


An on-call shift with its associated data and relationships.
Field
Type
Description
data
object
Data for an on-call shift.
attributes
object
Attributes for an on-call shift.
end
date-time
The end time of the shift.
start
date-time
The start time of the shift.
id
string
The `ShiftData` `id`.
relationships
object
Relationships for an on-call shift.
user
object
Defines the relationship between a shift and the user who is working that shift.
data [_required_]
object
Represents a reference to the user assigned to this shift, containing the user's ID and resource type.
id [_required_]
string
Specifies the unique identifier of the user.
type [_required_]
enum
Indicates that the related resource is of type 'users'. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Indicates that the resource is of type 'shifts'. Allowed enum values: `shifts`
default: `shifts`
included
[ <oneOf>]
The `Shift` `included`.
Option 1
object
Represents a user object in the context of a schedule, including their `id`, type, and basic attributes.
attributes
object
Provides basic user information for a schedule, including a name and email address.
email
string
The user's email address.
name
string
The user's name.
status
enum
The user's status. Allowed enum values: `active,deactivated,pending`
id
string
The unique user identifier.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "end": "2025-05-07T03:53:01.206662873Z",
      "start": "2025-05-07T02:53:01.206662814Z"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "relationships": {
      "user": {
        "data": {
          "id": "00000000-aba1-0000-0000-000000000000",
          "type": "users"
        }
      }
    },
    "type": "shifts"
  },
  "included": [
    {
      "attributes": {
        "email": "foo@bar.com",
        "name": "User 1",
        "status": ""
      },
      "id": "00000000-aba1-0000-0000-000000000000",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Get scheduled on-call user
Copy
```
                  # Path parameters  
export schedule_id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/schedules/${schedule_id}/on-call" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get scheduled on-call user
```
"""
Get scheduled on-call user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_schedule_on_call_user(
        schedule_id=SCHEDULE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get scheduled on-call user
```
# Get scheduled on-call user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = ENV["SCHEDULE_DATA_ID"]
p api_instance.get_schedule_on_call_user(SCHEDULE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get scheduled on-call user
```
// Get scheduled on-call user returns "OK" response

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
	// there is a valid "schedule" in the system
	ScheduleDataID := os.Getenv("SCHEDULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.GetScheduleOnCallUser(ctx, ScheduleDataID, *datadogV2.NewGetScheduleOnCallUserOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.GetScheduleOnCallUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.GetScheduleOnCallUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get scheduled on-call user
```
// Get scheduled on-call user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.Shift;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "schedule" in the system
    String SCHEDULE_DATA_ID = System.getenv("SCHEDULE_DATA_ID");

    try {
      Shift result = apiInstance.getScheduleOnCallUser(SCHEDULE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#getScheduleOnCallUser");
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

#####  Get scheduled on-call user
```
// Get scheduled on-call user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::GetScheduleOnCallUserOptionalParams;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "schedule" in the system
    let schedule_data_id = std::env::var("SCHEDULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .get_schedule_on_call_user(
            schedule_data_id.clone(),
            GetScheduleOnCallUserOptionalParams::default(),
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

#####  Get scheduled on-call user
```
/**
 * Get scheduled on-call user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "schedule" in the system
const SCHEDULE_DATA_ID = process.env.SCHEDULE_DATA_ID as string;

const params: v2.OnCallApiGetScheduleOnCallUserRequest = {
  scheduleId: SCHEDULE_DATA_ID,
};

apiInstance
  .getScheduleOnCallUser(params)
  .then((data: v2.Shift) => {
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
## [Get team on-call users](https://docs.datadoghq.com/api/latest/on-call/#get-team-on-call-users)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#get-team-on-call-users-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/teams/{team_id}/on-callhttps://api.ap2.datadoghq.com/api/v2/on-call/teams/{team_id}/on-callhttps://api.datadoghq.eu/api/v2/on-call/teams/{team_id}/on-callhttps://api.ddog-gov.com/api/v2/on-call/teams/{team_id}/on-callhttps://api.datadoghq.com/api/v2/on-call/teams/{team_id}/on-callhttps://api.us3.datadoghq.com/api/v2/on-call/teams/{team_id}/on-callhttps://api.us5.datadoghq.com/api/v2/on-call/teams/{team_id}/on-call
### Overview
Get a team’s on-call users at a given time This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
team_id [_required_]
string
The team ID
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `responders`, `escalations`, `escalations.responders`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#GetTeamOnCallUsers-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#GetTeamOnCallUsers-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#GetTeamOnCallUsers-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#GetTeamOnCallUsers-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#GetTeamOnCallUsers-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#GetTeamOnCallUsers-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Root object representing a team’s on-call responder configuration.
Field
Type
Description
data
object
Defines the main on-call responder object for a team, including relationships and metadata.
id
string
Unique identifier of the on-call responder configuration.
relationships
object
Relationship objects linked to a team's on-call responder configuration, including escalations and responders.
escalations
object
Defines the escalation policy steps linked to the team's on-call configuration.
data
[object]
Array of escalation step references.
id [_required_]
string
Unique identifier of the escalation step.
type [_required_]
enum
Identifies the resource type for escalation policy steps linked to a team's on-call configuration. Allowed enum values: `escalation_policy_steps`
default: `escalation_policy_steps`
responders
object
Defines the list of users assigned as on-call responders for the team.
data
[object]
Array of user references associated as responders.
id [_required_]
string
Unique identifier of the responder.
type [_required_]
enum
Identifies the resource type for individual user entities associated with on-call response. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Represents the resource type for a group of users assigned to handle on-call duties within a team. Allowed enum values: `team_oncall_responders`
default: `team_oncall_responders`
included
[ <oneOf>]
The `TeamOnCallResponders` `included`.
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
Represents an escalation policy step.
id
string
Unique identifier of the escalation step.
relationships
object
Contains the relationships of an escalation object, including its responders.
responders
object
Lists the users involved in a specific step of the escalation policy.
data
[object]
Array of user references assigned as responders for this escalation step.
id [_required_]
string
Unique identifier of the user assigned to the escalation step.
type [_required_]
enum
Represents the resource type for users assigned as responders in an escalation step. Allowed enum values: `users`
default: `users`
type [_required_]
enum
Represents the resource type for individual steps in an escalation policy used during incident response. Allowed enum values: `escalation_policy_steps`
default: `escalation_policy_steps`
```
{
  "data": {
    "id": "111ee23r-aaaaa-aaaa-aaww-1234wertsd23",
    "relationships": {
      "escalations": {
        "data": [
          {
            "id": "111ee23r-aaaaa-aaaa-aaww-1234wertsd23",
            "type": "escalation_policy_steps"
          }
        ]
      },
      "responders": {
        "data": [
          {
            "id": "111ee23r-aaaaa-aaaa-aaww-1234wertsd23",
            "type": "users"
          }
        ]
      }
    },
    "type": "team_oncall_responders"
  },
  "included": [
    {
      "attributes": {
        "email": "test@test.com",
        "name": "Test User",
        "status": "active"
      },
      "id": "111ee23r-aaaaa-aaaa-aaww-1234wertsd23",
      "type": "users"
    },
    {
      "id": "111ee23r-aaaaa-aaaa-aaww-1234wertsd23",
      "relationships": {
        "responders": {
          "data": [
            {
              "id": "111ee23r-aaaaa-aaaa-aaww-1234wertsd23",
              "type": "users"
            }
          ]
        }
      },
      "type": "escalation_policy_steps"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Get team on-call users
Copy
```
                  # Path parameters  
export team_id="27590dae-47be-4a7d-9abf-8f4e45124020"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/teams/${team_id}/on-call" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get team on-call users
```
"""
Get team on-call users returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there are valid "routing_rules" in the system
ROUTING_RULES_DATA_ID = environ["ROUTING_RULES_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_team_on_call_users(
        include="responders,escalations.responders",
        team_id=ROUTING_RULES_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get team on-call users
```
# Get team on-call users returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there are valid "routing_rules" in the system
ROUTING_RULES_DATA_ID = ENV["ROUTING_RULES_DATA_ID"]
opts = {
  include: "responders,escalations.responders",
}
p api_instance.get_team_on_call_users(ROUTING_RULES_DATA_ID, opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get team on-call users
```
// Get team on-call users returns "OK" response

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
	// there are valid "routing_rules" in the system
	RoutingRulesDataID := os.Getenv("ROUTING_RULES_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.GetTeamOnCallUsers(ctx, RoutingRulesDataID, *datadogV2.NewGetTeamOnCallUsersOptionalParameters().WithInclude("responders,escalations.responders"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.GetTeamOnCallUsers`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.GetTeamOnCallUsers`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get team on-call users
```
// Get team on-call users returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.api.OnCallApi.GetTeamOnCallUsersOptionalParameters;
import com.datadog.api.client.v2.model.TeamOnCallResponders;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there are valid "routing_rules" in the system
    String ROUTING_RULES_DATA_ID = System.getenv("ROUTING_RULES_DATA_ID");

    try {
      TeamOnCallResponders result =
          apiInstance.getTeamOnCallUsers(
              ROUTING_RULES_DATA_ID,
              new GetTeamOnCallUsersOptionalParameters()
                  .include("responders,escalations.responders"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#getTeamOnCallUsers");
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

#####  Get team on-call users
```
// Get team on-call users returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::GetTeamOnCallUsersOptionalParams;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there are valid "routing_rules" in the system
    let routing_rules_data_id = std::env::var("ROUTING_RULES_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .get_team_on_call_users(
            routing_rules_data_id.clone(),
            GetTeamOnCallUsersOptionalParams::default()
                .include("responders,escalations.responders".to_string()),
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

#####  Get team on-call users
```
/**
 * Get team on-call users returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there are valid "routing_rules" in the system
const ROUTING_RULES_DATA_ID = process.env.ROUTING_RULES_DATA_ID as string;

const params: v2.OnCallApiGetTeamOnCallUsersRequest = {
  include: "responders,escalations.responders",
  teamId: ROUTING_RULES_DATA_ID,
};

apiInstance
  .getTeamOnCallUsers(params)
  .then((data: v2.TeamOnCallResponders) => {
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
## [Delete an On-Call notification channel for a user](https://docs.datadoghq.com/api/latest/on-call/#delete-an-on-call-notification-channel-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#delete-an-on-call-notification-channel-for-a-user-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}
### Overview
Delete a notification channel for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_respond` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
channel_id [_required_]
string
The channel ID
### Response
  * [204](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationChannel-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationChannel-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationChannel-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationChannel-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationChannel-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationChannel-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Delete an On-Call notification channel for a user
Copy
```
                  # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
export channel_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-channels/${channel_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an On-Call notification channel for a user
```
"""
Delete an On-Call notification channel for a user returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "oncall_email_notification_channel" in the system
ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = environ["ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    api_instance.delete_user_notification_channel(
        user_id=USER_DATA_ID,
        channel_id=ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an On-Call notification channel for a user
```
# Delete an On-Call notification channel for a user returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

# there is a valid "oncall_email_notification_channel" in the system
ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = ENV["ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID"]
api_instance.delete_user_notification_channel(USER_DATA_ID, ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an On-Call notification channel for a user
```
// Delete an On-Call notification channel for a user returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	// there is a valid "oncall_email_notification_channel" in the system
	OncallEmailNotificationChannelDataID := os.Getenv("ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	r, err := api.DeleteUserNotificationChannel(ctx, UserDataID, OncallEmailNotificationChannelDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.DeleteUserNotificationChannel`: %v\n", err)
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

#####  Delete an On-Call notification channel for a user
```
// Delete an On-Call notification channel for a user returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    // there is a valid "oncall_email_notification_channel" in the system
    String ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID =
        System.getenv("ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID");

    try {
      apiInstance.deleteUserNotificationChannel(
          USER_DATA_ID, ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#deleteUserNotificationChannel");
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

#####  Delete an On-Call notification channel for a user
```
// Delete an On-Call notification channel for a user returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();

    // there is a valid "oncall_email_notification_channel" in the system
    let oncall_email_notification_channel_data_id =
        std::env::var("ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .delete_user_notification_channel(
            user_data_id.clone(),
            oncall_email_notification_channel_data_id.clone(),
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

#####  Delete an On-Call notification channel for a user
```
/**
 * Delete an On-Call notification channel for a user returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

// there is a valid "oncall_email_notification_channel" in the system
const ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = process.env
  .ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID as string;

const params: v2.OnCallApiDeleteUserNotificationChannelRequest = {
  userId: USER_DATA_ID,
  channelId: ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID,
};

apiInstance
  .deleteUserNotificationChannel(params)
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
## [Get an On-Call notification channel for a user](https://docs.datadoghq.com/api/latest/on-call/#get-an-on-call-notification-channel-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#get-an-on-call-notification-channel-for-a-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}https://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels/{channel_id}
### Overview
Get a notification channel for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
channel_id [_required_]
string
The channel ID
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationChannel-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationChannel-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationChannel-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationChannel-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationChannel-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationChannel-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


A top-level wrapper for a user notification channel
Field
Type
Description
data
object
Data for an on-call notification channel
attributes
object
Attributes for an on-call notification channel.
active
boolean
Whether the notification channel is currently active.
config
<oneOf>
Notification channel configuration
Option 1
object
Phone notification channel configuration
formatted_number [_required_]
string
The formatted international version of Number (e.g. +33 7 1 23 45 67).
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
region [_required_]
string
The ISO 3166-1 alpha-2 two-letter country code.
sms_subscribed_at
date-time
If present, the date the user subscribed this number to SMS messages
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
verified [_required_]
boolean
Indicates whether this phone has been verified by the user in Datadog On-Call
Option 2
object
Email notification channel configuration
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
Option 3
object
Push notification channel configuration
application_name [_required_]
string
The name of the application used to receive push notifications
device_name [_required_]
string
The name of the mobile device being used
type [_required_]
enum
Indicates that the notification channel is a mobile device for push notifications Allowed enum values: `push`
default: `push`
id
string
Unique identifier for the channel
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": {
    "attributes": {
      "config": {
        "address": "foo@bar.com",
        "formats": [
          "html"
        ],
        "type": "email"
      }
    },
    "id": "27590dae-47be-4a7d-9abf-8f4e45124020",
    "type": "notification_channels"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Get an On-Call notification channel for a user
Copy
```
                  # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
export channel_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-channels/${channel_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an On-Call notification channel for a user
```
"""
Get an On-Call notification channel for a user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "oncall_email_notification_channel" in the system
ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = environ["ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_user_notification_channel(
        user_id=USER_DATA_ID,
        channel_id=ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get an On-Call notification channel for a user
```
# Get an On-Call notification channel for a user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

# there is a valid "oncall_email_notification_channel" in the system
ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = ENV["ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID"]
p api_instance.get_user_notification_channel(USER_DATA_ID, ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get an On-Call notification channel for a user
```
// Get an On-Call notification channel for a user returns "OK" response

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

	// there is a valid "oncall_email_notification_channel" in the system
	OncallEmailNotificationChannelDataID := os.Getenv("ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.GetUserNotificationChannel(ctx, UserDataID, OncallEmailNotificationChannelDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.GetUserNotificationChannel`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.GetUserNotificationChannel`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get an On-Call notification channel for a user
```
// Get an On-Call notification channel for a user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.NotificationChannel;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    // there is a valid "oncall_email_notification_channel" in the system
    String ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID =
        System.getenv("ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID");

    try {
      NotificationChannel result =
          apiInstance.getUserNotificationChannel(
              USER_DATA_ID, ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#getUserNotificationChannel");
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

#####  Get an On-Call notification channel for a user
```
// Get an On-Call notification channel for a user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();

    // there is a valid "oncall_email_notification_channel" in the system
    let oncall_email_notification_channel_data_id =
        std::env::var("ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .get_user_notification_channel(
            user_data_id.clone(),
            oncall_email_notification_channel_data_id.clone(),
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

#####  Get an On-Call notification channel for a user
```
/**
 * Get an On-Call notification channel for a user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

// there is a valid "oncall_email_notification_channel" in the system
const ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = process.env
  .ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID as string;

const params: v2.OnCallApiGetUserNotificationChannelRequest = {
  userId: USER_DATA_ID,
  channelId: ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID,
};

apiInstance
  .getUserNotificationChannel(params)
  .then((data: v2.NotificationChannel) => {
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
## [List On-Call notification channels for a user](https://docs.datadoghq.com/api/latest/on-call/#list-on-call-notification-channels-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#list-on-call-notification-channels-for-a-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-channelshttps://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels
### Overview
List the notification channels for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationChannels-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationChannels-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationChannels-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationChannels-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationChannels-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationChannels-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Response type for listing notification channels for a user
Field
Type
Description
data
[object]
attributes
object
Attributes for an on-call notification channel.
active
boolean
Whether the notification channel is currently active.
config
<oneOf>
Notification channel configuration
Option 1
object
Phone notification channel configuration
formatted_number [_required_]
string
The formatted international version of Number (e.g. +33 7 1 23 45 67).
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
region [_required_]
string
The ISO 3166-1 alpha-2 two-letter country code.
sms_subscribed_at
date-time
If present, the date the user subscribed this number to SMS messages
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
verified [_required_]
boolean
Indicates whether this phone has been verified by the user in Datadog On-Call
Option 2
object
Email notification channel configuration
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
Option 3
object
Push notification channel configuration
application_name [_required_]
string
The name of the application used to receive push notifications
device_name [_required_]
string
The name of the mobile device being used
type [_required_]
enum
Indicates that the notification channel is a mobile device for push notifications Allowed enum values: `push`
default: `push`
id
string
Unique identifier for the channel
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": [
    {
      "attributes": {
        "active": false,
        "config": {
          "formatted_number": "",
          "number": "",
          "region": "",
          "sms_subscribed_at": "2019-09-19T10:00:00.000Z",
          "type": "phone",
          "verified": false
        }
      },
      "id": "string",
      "type": "notification_channels"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  List On-Call notification channels for a user
Copy
```
                  # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-channels" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List On-Call notification channels for a user
```
"""
List On-Call notification channels for a user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.list_user_notification_channels(
        user_id=USER_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List On-Call notification channels for a user
```
# List On-Call notification channels for a user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.list_user_notification_channels(USER_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List On-Call notification channels for a user
```
// List On-Call notification channels for a user returns "OK" response

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
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.ListUserNotificationChannels(ctx, UserDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.ListUserNotificationChannels`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.ListUserNotificationChannels`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List On-Call notification channels for a user
```
// List On-Call notification channels for a user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.ListNotificationChannelsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    try {
      ListNotificationChannelsResponse result =
          apiInstance.listUserNotificationChannels(USER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#listUserNotificationChannels");
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

#####  List On-Call notification channels for a user
```
// List On-Call notification channels for a user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .list_user_notification_channels(user_data_id.clone())
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

#####  List On-Call notification channels for a user
```
/**
 * List On-Call notification channels for a user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.OnCallApiListUserNotificationChannelsRequest = {
  userId: USER_DATA_ID,
};

apiInstance
  .listUserNotificationChannels(params)
  .then((data: v2.ListNotificationChannelsResponse) => {
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
## [Create an On-Call notification channel for a user](https://docs.datadoghq.com/api/latest/on-call/#create-an-on-call-notification-channel-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#create-an-on-call-notification-channel-for-a-user-v2)


POST https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-channelshttps://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channelshttps://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-channels
### Overview
Create a new notification channel for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_respond` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data [_required_]
object
Data for creating an on-call notification channel
attributes
object
Attributes for creating an on-call notification channel.
config
<oneOf>
Notification channel configuration
Option 1
object
Configuration to create a phone notification channel
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
Option 2
object
Configuration to create an e-mail notification channel
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": {
    "attributes": {
      "config": {
        "address": "foo@bar.com",
        "formats": [
          "html"
        ],
        "type": "email"
      }
    },
    "type": "notification_channels"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationChannel-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationChannel-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationChannel-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationChannel-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationChannel-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationChannel-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


A top-level wrapper for a user notification channel
Field
Type
Description
data
object
Data for an on-call notification channel
attributes
object
Attributes for an on-call notification channel.
active
boolean
Whether the notification channel is currently active.
config
<oneOf>
Notification channel configuration
Option 1
object
Phone notification channel configuration
formatted_number [_required_]
string
The formatted international version of Number (e.g. +33 7 1 23 45 67).
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
region [_required_]
string
The ISO 3166-1 alpha-2 two-letter country code.
sms_subscribed_at
date-time
If present, the date the user subscribed this number to SMS messages
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
verified [_required_]
boolean
Indicates whether this phone has been verified by the user in Datadog On-Call
Option 2
object
Email notification channel configuration
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
Option 3
object
Push notification channel configuration
application_name [_required_]
string
The name of the application used to receive push notifications
device_name [_required_]
string
The name of the mobile device being used
type [_required_]
enum
Indicates that the notification channel is a mobile device for push notifications Allowed enum values: `push`
default: `push`
id
string
Unique identifier for the channel
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": {
    "attributes": {
      "config": {
        "address": "foo@bar.com",
        "formats": [
          "html"
        ],
        "type": "email"
      }
    },
    "id": "27590dae-47be-4a7d-9abf-8f4e45124020",
    "type": "notification_channels"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/on-call/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/on-call/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/on-call/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/on-call/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/on-call/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/on-call/?code-lang=typescript)


#####  Create an On-Call notification channel for a user returns "Created" response
Copy
```
                          # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-channels" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config": {
        "address": "foo@bar.com",
        "formats": [
          "html"
        ],
        "type": "email"
      }
    },
    "type": "notification_channels"
  }
}
EOF  

                        
```

#####  Create an On-Call notification channel for a user returns "Created" response
```
// Create an On-Call notification channel for a user returns "Created" response

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

	body := datadogV2.CreateUserNotificationChannelRequest{
		Data: datadogV2.CreateNotificationChannelData{
			Attributes: &datadogV2.CreateNotificationChannelAttributes{
				Config: &datadogV2.CreateNotificationChannelConfig{
					CreateEmailNotificationChannelConfig: &datadogV2.CreateEmailNotificationChannelConfig{
						Address: "foo@bar.com",
						Formats: []datadogV2.NotificationChannelEmailFormatType{
							datadogV2.NOTIFICATIONCHANNELEMAILFORMATTYPE_HTML,
						},
						Type: datadogV2.NOTIFICATIONCHANNELEMAILCONFIGTYPE_EMAIL,
					}},
			},
			Type: datadogV2.NOTIFICATIONCHANNELTYPE_NOTIFICATION_CHANNELS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallApi(apiClient)
	resp, r, err := api.CreateUserNotificationChannel(ctx, UserDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallApi.CreateUserNotificationChannel`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallApi.CreateUserNotificationChannel`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create an On-Call notification channel for a user returns "Created" response
```
// Create an On-Call notification channel for a user returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallApi;
import com.datadog.api.client.v2.model.CreateEmailNotificationChannelConfig;
import com.datadog.api.client.v2.model.CreateNotificationChannelAttributes;
import com.datadog.api.client.v2.model.CreateNotificationChannelConfig;
import com.datadog.api.client.v2.model.CreateNotificationChannelData;
import com.datadog.api.client.v2.model.CreateUserNotificationChannelRequest;
import com.datadog.api.client.v2.model.NotificationChannel;
import com.datadog.api.client.v2.model.NotificationChannelEmailConfigType;
import com.datadog.api.client.v2.model.NotificationChannelEmailFormatType;
import com.datadog.api.client.v2.model.NotificationChannelType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallApi apiInstance = new OnCallApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    CreateUserNotificationChannelRequest body =
        new CreateUserNotificationChannelRequest()
            .data(
                new CreateNotificationChannelData()
                    .attributes(
                        new CreateNotificationChannelAttributes()
                            .config(
                                new CreateNotificationChannelConfig(
                                    new CreateEmailNotificationChannelConfig()
                                        .address("foo@bar.com")
                                        .formats(
                                            Collections.singletonList(
                                                NotificationChannelEmailFormatType.HTML))
                                        .type(NotificationChannelEmailConfigType.EMAIL))))
                    .type(NotificationChannelType.NOTIFICATION_CHANNELS));

    try {
      NotificationChannel result = apiInstance.createUserNotificationChannel(USER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#createUserNotificationChannel");
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

#####  Create an On-Call notification channel for a user returns "Created" response
```
"""
Create an On-Call notification channel for a user returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.create_email_notification_channel_config import CreateEmailNotificationChannelConfig
from datadog_api_client.v2.model.create_notification_channel_attributes import CreateNotificationChannelAttributes
from datadog_api_client.v2.model.create_notification_channel_data import CreateNotificationChannelData
from datadog_api_client.v2.model.create_user_notification_channel_request import CreateUserNotificationChannelRequest
from datadog_api_client.v2.model.notification_channel_email_config_type import NotificationChannelEmailConfigType
from datadog_api_client.v2.model.notification_channel_email_format_type import NotificationChannelEmailFormatType
from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = CreateUserNotificationChannelRequest(
    data=CreateNotificationChannelData(
        attributes=CreateNotificationChannelAttributes(
            config=CreateEmailNotificationChannelConfig(
                address="foo@bar.com",
                formats=[
                    NotificationChannelEmailFormatType.HTML,
                ],
                type=NotificationChannelEmailConfigType.EMAIL,
            ),
        ),
        type=NotificationChannelType.NOTIFICATION_CHANNELS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_user_notification_channel(user_id=USER_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an On-Call notification channel for a user returns "Created" response
```
# Create an On-Call notification channel for a user returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::CreateUserNotificationChannelRequest.new({
  data: DatadogAPIClient::V2::CreateNotificationChannelData.new({
    attributes: DatadogAPIClient::V2::CreateNotificationChannelAttributes.new({
      config: DatadogAPIClient::V2::CreateEmailNotificationChannelConfig.new({
        address: "foo@bar.com",
        formats: [
          DatadogAPIClient::V2::NotificationChannelEmailFormatType::HTML,
        ],
        type: DatadogAPIClient::V2::NotificationChannelEmailConfigType::EMAIL,
      }),
    }),
    type: DatadogAPIClient::V2::NotificationChannelType::NOTIFICATION_CHANNELS,
  }),
})
p api_instance.create_user_notification_channel(USER_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create an On-Call notification channel for a user returns "Created" response
```
// Create an On-Call notification channel for a user returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call::OnCallAPI;
use datadog_api_client::datadogV2::model::CreateEmailNotificationChannelConfig;
use datadog_api_client::datadogV2::model::CreateNotificationChannelAttributes;
use datadog_api_client::datadogV2::model::CreateNotificationChannelConfig;
use datadog_api_client::datadogV2::model::CreateNotificationChannelData;
use datadog_api_client::datadogV2::model::CreateUserNotificationChannelRequest;
use datadog_api_client::datadogV2::model::NotificationChannelEmailConfigType;
use datadog_api_client::datadogV2::model::NotificationChannelEmailFormatType;
use datadog_api_client::datadogV2::model::NotificationChannelType;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = CreateUserNotificationChannelRequest::new(
        CreateNotificationChannelData::new(NotificationChannelType::NOTIFICATION_CHANNELS)
            .attributes(CreateNotificationChannelAttributes::new().config(
                CreateNotificationChannelConfig::CreateEmailNotificationChannelConfig(Box::new(
                    CreateEmailNotificationChannelConfig::new(
                        "foo@bar.com".to_string(),
                        vec![NotificationChannelEmailFormatType::HTML],
                        NotificationChannelEmailConfigType::EMAIL,
                    ),
                )),
            )),
    );
    let configuration = datadog::Configuration::new();
    let api = OnCallAPI::with_config(configuration);
    let resp = api
        .create_user_notification_channel(user_data_id.clone(), body)
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

#####  Create an On-Call notification channel for a user returns "Created" response
```
/**
 * Create an On-Call notification channel for a user returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.OnCallApiCreateUserNotificationChannelRequest = {
  body: {
    data: {
      attributes: {
        config: {
          address: "foo@bar.com",
          formats: ["html"],
          type: "email",
        },
      },
      type: "notification_channels",
    },
  },
  userId: USER_DATA_ID,
};

apiInstance
  .createUserNotificationChannel(params)
  .then((data: v2.NotificationChannel) => {
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
## [Create an On-Call notification rule for a user](https://docs.datadoghq.com/api/latest/on-call/#create-an-on-call-notification-rule-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#create-an-on-call-notification-rule-for-a-user-v2)


POST https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules
### Overview
Create a new notification rule for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_respond` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data [_required_]
object
Data for creating an on-call notification rule
attributes
object
Attributes for creating or modifying an on-call notification rule.
category
enum
Specifies the category a notification rule will apply to Allowed enum values: `high_urgency,low_urgency`
default: `high_urgency`
channel_settings
<oneOf>
Configuration for the associated channel, if necessary
Option 1
object
Configuration for using a phone notification channel in a notification rule
method [_required_]
enum
Specifies the method in which a phone is used in a notification rule Allowed enum values: `sms,voice`
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
delay_minutes
int64
The number of minutes that will elapse before this rule is evaluated. 0 indicates immediate evaluation
relationships
object
Relationship object for creating a notification rule
channel
object
Relationship object for creating a notification rule
data [_required_]
object
Channel relationship data for creating a notification rule
id
string
ID of the notification channel
type
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
type [_required_]
enum
Indicates that the resource is of type 'notification_rules'. Allowed enum values: `notification_rules`
default: `notification_rules`
```
{
  "data": {
    "attributes": {
      "category": "high_urgency",
      "delay_minutes": 0
    },
    "relationships": {
      "channel": {
        "data": {
          "id": "7c1ce93f-30a5-596a-0f7b-06bfe153704c",
          "type": "notification_channels"
        }
      }
    },
    "type": "notification_rules"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationRule-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#CreateUserNotificationRule-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


A top-level wrapper for a notification rule
Field
Type
Description
data [_required_]
object
Data for an on-call notification rule
attributes
object
Attributes for an on-call notification rule.
category
enum
Specifies the category a notification rule will apply to Allowed enum values: `high_urgency,low_urgency`
default: `high_urgency`
channel_settings
<oneOf>
Configuration for the associated channel, if necessary
Option 1
object
Configuration for using a phone notification channel in a notification rule
method [_required_]
enum
Specifies the method in which a phone is used in a notification rule Allowed enum values: `sms,voice`
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
delay_minutes
int64
The number of minutes that will elapse before this rule is evaluated. 0 indicates immediate evaluation
id
string
Unique identifier for the rule
relationships
object
Relationship object for creating a notification rule
channel
object
Relationship object for creating a notification rule
data [_required_]
object
Channel relationship data for creating a notification rule
id
string
ID of the notification channel
type
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
type [_required_]
enum
Indicates that the resource is of type 'notification_rules'. Allowed enum values: `notification_rules`
default: `notification_rules`
included
[ <oneOf>]
Option 1
object
Data for an on-call notification channel
attributes
object
Attributes for an on-call notification channel.
active
boolean
Whether the notification channel is currently active.
config
<oneOf>
Notification channel configuration
Option 1
object
Phone notification channel configuration
formatted_number [_required_]
string
The formatted international version of Number (e.g. +33 7 1 23 45 67).
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
region [_required_]
string
The ISO 3166-1 alpha-2 two-letter country code.
sms_subscribed_at
date-time
If present, the date the user subscribed this number to SMS messages
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
verified [_required_]
boolean
Indicates whether this phone has been verified by the user in Datadog On-Call
Option 2
object
Email notification channel configuration
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
Option 3
object
Push notification channel configuration
application_name [_required_]
string
The name of the application used to receive push notifications
device_name [_required_]
string
The name of the mobile device being used
type [_required_]
enum
Indicates that the notification channel is a mobile device for push notifications Allowed enum values: `push`
default: `push`
id
string
Unique identifier for the channel
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": {
    "attributes": {
      "category": "high_urgency",
      "channel_settings": {
        "method": "sms",
        "type": "phone"
      },
      "delay_minutes": 1
    },
    "id": "27590dae-47be-4a7d-9abf-8f4e45124020",
    "relationships": {
      "channel": {
        "data": {
          "id": "1562fab3-a8c2-49e2-8f3a-28dcda2405e2",
          "type": "notification_channels"
        }
      }
    },
    "type": "notification_rules"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)


#####  Create an On-Call notification rule for a user returns "Created" response
Copy
```
                          # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "category": "high_urgency",
      "delay_minutes": 0
    },
    "relationships": {
      "channel": {
        "data": {
          "id": "7c1ce93f-30a5-596a-0f7b-06bfe153704c",
          "type": "notification_channels"
        }
      }
    },
    "type": "notification_rules"
  }
}
EOF  

                        
```

* * *
## [List On-Call notification rules for a user](https://docs.datadoghq.com/api/latest/on-call/#list-on-call-notification-rules-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#list-on-call-notification-rules-for-a-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-ruleshttps://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules
### Overview
List the notification rules for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `channel`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationRules-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationRules-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationRules-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationRules-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationRules-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#ListUserNotificationRules-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Response type for listing notification rules for a user
Field
Type
Description
data
[object]
attributes
object
Attributes for an on-call notification rule.
category
enum
Specifies the category a notification rule will apply to Allowed enum values: `high_urgency,low_urgency`
default: `high_urgency`
channel_settings
<oneOf>
Configuration for the associated channel, if necessary
Option 1
object
Configuration for using a phone notification channel in a notification rule
method [_required_]
enum
Specifies the method in which a phone is used in a notification rule Allowed enum values: `sms,voice`
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
delay_minutes
int64
The number of minutes that will elapse before this rule is evaluated. 0 indicates immediate evaluation
id
string
Unique identifier for the rule
relationships
object
Relationship object for creating a notification rule
channel
object
Relationship object for creating a notification rule
data [_required_]
object
Channel relationship data for creating a notification rule
id
string
ID of the notification channel
type
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
type [_required_]
enum
Indicates that the resource is of type 'notification_rules'. Allowed enum values: `notification_rules`
default: `notification_rules`
included
[ <oneOf>]
Option 1
object
Data for an on-call notification channel
attributes
object
Attributes for an on-call notification channel.
active
boolean
Whether the notification channel is currently active.
config
<oneOf>
Notification channel configuration
Option 1
object
Phone notification channel configuration
formatted_number [_required_]
string
The formatted international version of Number (e.g. +33 7 1 23 45 67).
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
region [_required_]
string
The ISO 3166-1 alpha-2 two-letter country code.
sms_subscribed_at
date-time
If present, the date the user subscribed this number to SMS messages
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
verified [_required_]
boolean
Indicates whether this phone has been verified by the user in Datadog On-Call
Option 2
object
Email notification channel configuration
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
Option 3
object
Push notification channel configuration
application_name [_required_]
string
The name of the application used to receive push notifications
device_name [_required_]
string
The name of the mobile device being used
type [_required_]
enum
Indicates that the notification channel is a mobile device for push notifications Allowed enum values: `push`
default: `push`
id
string
Unique identifier for the channel
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": [
    {
      "attributes": {
        "category": "string",
        "channel_settings": {
          "method": "sms",
          "type": "phone"
        },
        "delay_minutes": "integer"
      },
      "id": "string",
      "relationships": {
        "channel": {
          "data": {
            "id": "string",
            "type": "notification_channels"
          }
        }
      },
      "type": "notification_rules"
    }
  ],
  "included": [
    {
      "attributes": {
        "active": false,
        "config": {
          "formatted_number": "",
          "number": "",
          "region": "",
          "sms_subscribed_at": "2019-09-19T10:00:00.000Z",
          "type": "phone",
          "verified": false
        }
      },
      "id": "string",
      "type": "notification_channels"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)


#####  List On-Call notification rules for a user
Copy
```
                  # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Delete an On-Call notification rule for a user](https://docs.datadoghq.com/api/latest/on-call/#delete-an-on-call-notification-rule-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#delete-an-on-call-notification-rule-for-a-user-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}
### Overview
Delete a notification rule for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_respond` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
rule_id [_required_]
string
The rule ID
### Response
  * [204](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationRule-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#DeleteUserNotificationRule-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)


#####  Delete an On-Call notification rule for a user
Copy
```
                  # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
export rule_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-rules/${rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Get an On-Call notification rule for a user](https://docs.datadoghq.com/api/latest/on-call/#get-an-on-call-notification-rule-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#get-an-on-call-notification-rule-for-a-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}
### Overview
Get a notification rule for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
rule_id [_required_]
string
The rule ID
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `channel`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#GetUserNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


A top-level wrapper for a notification rule
Field
Type
Description
data [_required_]
object
Data for an on-call notification rule
attributes
object
Attributes for an on-call notification rule.
category
enum
Specifies the category a notification rule will apply to Allowed enum values: `high_urgency,low_urgency`
default: `high_urgency`
channel_settings
<oneOf>
Configuration for the associated channel, if necessary
Option 1
object
Configuration for using a phone notification channel in a notification rule
method [_required_]
enum
Specifies the method in which a phone is used in a notification rule Allowed enum values: `sms,voice`
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
delay_minutes
int64
The number of minutes that will elapse before this rule is evaluated. 0 indicates immediate evaluation
id
string
Unique identifier for the rule
relationships
object
Relationship object for creating a notification rule
channel
object
Relationship object for creating a notification rule
data [_required_]
object
Channel relationship data for creating a notification rule
id
string
ID of the notification channel
type
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
type [_required_]
enum
Indicates that the resource is of type 'notification_rules'. Allowed enum values: `notification_rules`
default: `notification_rules`
included
[ <oneOf>]
Option 1
object
Data for an on-call notification channel
attributes
object
Attributes for an on-call notification channel.
active
boolean
Whether the notification channel is currently active.
config
<oneOf>
Notification channel configuration
Option 1
object
Phone notification channel configuration
formatted_number [_required_]
string
The formatted international version of Number (e.g. +33 7 1 23 45 67).
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
region [_required_]
string
The ISO 3166-1 alpha-2 two-letter country code.
sms_subscribed_at
date-time
If present, the date the user subscribed this number to SMS messages
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
verified [_required_]
boolean
Indicates whether this phone has been verified by the user in Datadog On-Call
Option 2
object
Email notification channel configuration
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
Option 3
object
Push notification channel configuration
application_name [_required_]
string
The name of the application used to receive push notifications
device_name [_required_]
string
The name of the mobile device being used
type [_required_]
enum
Indicates that the notification channel is a mobile device for push notifications Allowed enum values: `push`
default: `push`
id
string
Unique identifier for the channel
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": {
    "attributes": {
      "category": "high_urgency",
      "channel_settings": {
        "method": "sms",
        "type": "phone"
      },
      "delay_minutes": 1
    },
    "id": "27590dae-47be-4a7d-9abf-8f4e45124020",
    "relationships": {
      "channel": {
        "data": {
          "id": "1562fab3-a8c2-49e2-8f3a-28dcda2405e2",
          "type": "notification_channels"
        }
      }
    },
    "type": "notification_rules"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)


#####  Get an On-Call notification rule for a user
Copy
```
                  # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
export rule_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-rules/${rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Update an On-Call notification rule for a user](https://docs.datadoghq.com/api/latest/on-call/#update-an-on-call-notification-rule-for-a-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/on-call/#update-an-on-call-notification-rule-for-a-user-v2)


PUT https://api.ap1.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.datadoghq.eu/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.ddog-gov.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.us3.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}https://api.us5.datadoghq.com/api/v2/on-call/users/{user_id}/notification-rules/{rule_id}
### Overview
Update a notification rule for a user. The authenticated user must be the target user or have the `on_call_admin` permission This endpoint requires the `on_call_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The user ID
rule_id [_required_]
string
The rule ID
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of included relationships to be returned. Allowed values: `channel`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


Field
Type
Description
data [_required_]
object
Data for updating an on-call notification rule
attributes
object
Attributes for creating or modifying an on-call notification rule.
category
enum
Specifies the category a notification rule will apply to Allowed enum values: `high_urgency,low_urgency`
default: `high_urgency`
channel_settings
<oneOf>
Configuration for the associated channel, if necessary
Option 1
object
Configuration for using a phone notification channel in a notification rule
method [_required_]
enum
Specifies the method in which a phone is used in a notification rule Allowed enum values: `sms,voice`
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
delay_minutes
int64
The number of minutes that will elapse before this rule is evaluated. 0 indicates immediate evaluation
id
string
Unique identifier for the rule
relationships
object
Relationship object for creating a notification rule
channel
object
Relationship object for creating a notification rule
data [_required_]
object
Channel relationship data for creating a notification rule
id
string
ID of the notification channel
type
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
type [_required_]
enum
Indicates that the resource is of type 'notification_rules'. Allowed enum values: `notification_rules`
default: `notification_rules`
```
{
  "data": {
    "attributes": {
      "category": "high_urgency",
      "delay_minutes": 1
    },
    "id": "4d00de6b-e1c1-e5fa-b238-57acec728d0d",
    "relationships": {
      "channel": {
        "data": {
          "id": "7c1ce93f-30a5-596a-0f7b-06bfe153704c",
          "type": "notification_channels"
        }
      }
    },
    "type": "notification_rules"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/on-call/#UpdateUserNotificationRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/on-call/#UpdateUserNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/on-call/#UpdateUserNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/on-call/#UpdateUserNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/on-call/#UpdateUserNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/on-call/#UpdateUserNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


A top-level wrapper for a notification rule
Field
Type
Description
data [_required_]
object
Data for an on-call notification rule
attributes
object
Attributes for an on-call notification rule.
category
enum
Specifies the category a notification rule will apply to Allowed enum values: `high_urgency,low_urgency`
default: `high_urgency`
channel_settings
<oneOf>
Configuration for the associated channel, if necessary
Option 1
object
Configuration for using a phone notification channel in a notification rule
method [_required_]
enum
Specifies the method in which a phone is used in a notification rule Allowed enum values: `sms,voice`
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
delay_minutes
int64
The number of minutes that will elapse before this rule is evaluated. 0 indicates immediate evaluation
id
string
Unique identifier for the rule
relationships
object
Relationship object for creating a notification rule
channel
object
Relationship object for creating a notification rule
data [_required_]
object
Channel relationship data for creating a notification rule
id
string
ID of the notification channel
type
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
type [_required_]
enum
Indicates that the resource is of type 'notification_rules'. Allowed enum values: `notification_rules`
default: `notification_rules`
included
[ <oneOf>]
Option 1
object
Data for an on-call notification channel
attributes
object
Attributes for an on-call notification channel.
active
boolean
Whether the notification channel is currently active.
config
<oneOf>
Notification channel configuration
Option 1
object
Phone notification channel configuration
formatted_number [_required_]
string
The formatted international version of Number (e.g. +33 7 1 23 45 67).
number [_required_]
string
The E-164 formatted phone number (e.g. +3371234567)
region [_required_]
string
The ISO 3166-1 alpha-2 two-letter country code.
sms_subscribed_at
date-time
If present, the date the user subscribed this number to SMS messages
type [_required_]
enum
Indicates that the notification channel is a phone Allowed enum values: `phone`
default: `phone`
verified [_required_]
boolean
Indicates whether this phone has been verified by the user in Datadog On-Call
Option 2
object
Email notification channel configuration
address [_required_]
string
The e-mail address to be notified
formats [_required_]
[string]
Preferred content formats for notifications.
type [_required_]
enum
Indicates that the notification channel is an e-mail address Allowed enum values: `email`
default: `email`
Option 3
object
Push notification channel configuration
application_name [_required_]
string
The name of the application used to receive push notifications
device_name [_required_]
string
The name of the mobile device being used
type [_required_]
enum
Indicates that the notification channel is a mobile device for push notifications Allowed enum values: `push`
default: `push`
id
string
Unique identifier for the channel
type [_required_]
enum
Indicates that the resource is of type 'notification_channels'. Allowed enum values: `notification_channels`
default: `notification_channels`
```
{
  "data": {
    "attributes": {
      "category": "high_urgency",
      "channel_settings": {
        "method": "sms",
        "type": "phone"
      },
      "delay_minutes": 1
    },
    "id": "27590dae-47be-4a7d-9abf-8f4e45124020",
    "relationships": {
      "channel": {
        "data": {
          "id": "1562fab3-a8c2-49e2-8f3a-28dcda2405e2",
          "type": "notification_channels"
        }
      }
    },
    "type": "notification_rules"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/on-call/)
  * [Example](https://docs.datadoghq.com/api/latest/on-call/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/on-call/?code-lang=curl)


#####  Update an On-Call notification rule for a user returns "OK" response
Copy
```
                          # Path parameters  
export user_id="00000000-0000-0000-0000-000000000000"  
export rule_id="00000000-0000-0000-0000-000000000000"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/on-call/users/${user_id}/notification-rules/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "category": "high_urgency",
      "delay_minutes": 1
    },
    "id": "4d00de6b-e1c1-e5fa-b238-57acec728d0d",
    "relationships": {
      "channel": {
        "data": {
          "id": "7c1ce93f-30a5-596a-0f7b-06bfe153704c",
          "type": "notification_channels"
        }
      }
    },
    "type": "notification_rules"
  }
}
EOF  

                        
```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=cfb94027-a50e-457c-98cf-c9beba8ffeb9&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=714b9b91-9d30-40b7-8e91-ad83afe1c83a&pt=On-Call&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fon-call%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=cfb94027-a50e-457c-98cf-c9beba8ffeb9&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=714b9b91-9d30-40b7-8e91-ad83afe1c83a&pt=On-Call&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fon-call%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=78c49b8c-5517-4288-8957-ce38b985f3fb&bo=2&sid=c4ba0d50f0bf11f09afde9c0412ba014&vid=c4ba67e0f0bf11f099fcdb9b6c7a6b3e&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=On-Call&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fon-call%2F&r=&lt=3189&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=38258)
