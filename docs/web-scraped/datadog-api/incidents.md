# Source: https://docs.datadoghq.com/api/latest/incidents

# Incidents
Manage incident response, as well as associated attachments, metadata, and todos. See the [Incident Management page](https://docs.datadoghq.com/service_management/incident_management/) for more information.
## [Create an incident](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/incidentshttps://api.ap2.datadoghq.com/api/v2/incidentshttps://api.datadoghq.eu/api/v2/incidentshttps://api.ddog-gov.com/api/v2/incidentshttps://api.datadoghq.com/api/v2/incidentshttps://api.us3.datadoghq.com/api/v2/incidentshttps://api.us5.datadoghq.com/api/v2/incidents
### Overview
Create an incident. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Request
#### Body Data (required)
Incident payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident data for a create request.
attributes [_required_]
object
The incident's attributes for a create request.
customer_impact_scope
string
Required if `customer_impacted:"true"`. A summary of the impact customers experienced during the incident.
customer_impacted [_required_]
boolean
A flag indicating whether the incident caused customer impact.
fields
object
A condensed view of the user-defined fields for which to create initial selections.
<any-key>
<oneOf>
Dynamic fields for which selections can be made, with field names as keys.
Option 1
object
A field with a single value selected.
type
enum
Type of the single value field definitions. Allowed enum values: `dropdown,textbox`
default: `dropdown`
value
string
The single value selected for this field.
Option 2
object
A field with potentially multiple values selected.
type
enum
Type of the multiple value field definitions. Allowed enum values: `multiselect,textarray,metrictag,autocomplete`
default: `multiselect`
value
[string]
The multiple values selected for this field.
incident_type_uuid
string
A unique identifier that represents an incident type. The default incident type will be used if this property is not provided.
initial_cells
[ <oneOf>]
An array of initial timeline cells to be placed at the beginning of the incident timeline.
Option 1
object
Timeline cell data for Markdown timeline cells for a create request.
cell_type [_required_]
enum
Type of the Markdown timeline cell. Allowed enum values: `markdown`
default: `markdown`
content [_required_]
object
The Markdown timeline cell contents.
content
string
The Markdown content of the cell.
important
boolean
A flag indicating whether the timeline cell is important and should be highlighted.
is_test
boolean
A flag indicating whether the incident is a test incident.
notification_handles
[object]
Notification handles that will be notified of the incident at creation.
display_name
string
The name of the notified handle.
handle
string
The handle used for the notification. This includes an email address, Slack channel, or workflow.
title [_required_]
string
The title of the incident, which summarizes what happened.
relationships
object
The relationships the incident will have with other resources once created.
commander_user [_required_]
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
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
```
{
  "data": {
    "type": "incidents",
    "attributes": {
      "title": "Example-Incident",
      "customer_impacted": false,
      "fields": {
        "state": {
          "type": "dropdown",
          "value": "resolved"
        }
      }
    },
    "relationships": {
      "commander_user": {
        "data": {
          "type": "users",
          "id": "string"
        }
      }
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncident-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncident-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#CreateIncident-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncident-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#CreateIncident-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncident-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident.
Field
Type
Description
data [_required_]
object
Incident data from a response.
attributes
object
The incident's attributes from a response.
archived
date-time
Timestamp of when the incident was archived.
case_id
int64
The incident case id.
created
date-time
Timestamp when the incident was created.
customer_impact_duration
int64
Length of the incident's customer impact in seconds. Equals the difference between `customer_impact_start` and `customer_impact_end`.
customer_impact_end
date-time
Timestamp when customers were no longer impacted by the incident.
customer_impact_scope
string
A summary of the impact customers experienced during the incident.
customer_impact_start
date-time
Timestamp when customers began being impacted by the incident.
customer_impacted
boolean
A flag indicating whether the incident caused customer impact.
declared
date-time
Timestamp when the incident was declared.
declared_by
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
declared_by_uuid
string
UUID of the user who declared the incident.
detected
date-time
Timestamp when the incident was detected.
fields
object
A condensed view of the user-defined fields attached to incidents.
<any-key>
<oneOf>
Dynamic fields for which selections can be made, with field names as keys.
Option 1
object
A field with a single value selected.
type
enum
Type of the single value field definitions. Allowed enum values: `dropdown,textbox`
default: `dropdown`
value
string
The single value selected for this field.
Option 2
object
A field with potentially multiple values selected.
type
enum
Type of the multiple value field definitions. Allowed enum values: `multiselect,textarray,metrictag,autocomplete`
default: `multiselect`
value
[string]
The multiple values selected for this field.
incident_type_uuid
string
A unique identifier that represents an incident type.
is_test
boolean
A flag indicating whether the incident is a test incident.
modified
date-time
Timestamp when the incident was last modified.
non_datadog_creator
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
notification_handles
[object]
Notification handles that will be notified of the incident during update.
display_name
string
The name of the notified handle.
handle
string
The handle used for the notification. This includes an email address, Slack channel, or workflow.
public_id
int64
The monotonically increasing integer ID for the incident.
resolved
date-time
Timestamp when the incident's state was last changed from active or stable to resolved or completed.
severity
enum
The incident severity. Allowed enum values: `UNKNOWN,SEV-0,SEV-1,SEV-2,SEV-3,SEV-4,SEV-5`
state
string
The state incident.
time_to_detect
int64
The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`.
time_to_internal_response
int64
The amount of time in seconds to call incident after detection. Equals the difference of `detected` and `created`.
time_to_repair
int64
The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`.
time_to_resolve
int64
The amount of time in seconds to resolve the incident after it was created. Equals the difference between `created` and `resolved`.
title [_required_]
string
The title of the incident, which summarizes what happened.
visibility
string
The incident visibility status.
id [_required_]
string
The incident's ID.
relationships
object
The incident's relationships from a response.
attachments
object
A relationship reference for attachments.
data [_required_]
[object]
An array of incident attachments.
id [_required_]
string
A unique identifier that represents the attachment.
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
commander_user
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
created_by_user
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
declared_by_user
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
impacts
object
Relationship to impacts.
data [_required_]
[object]
An array of incident impacts.
id [_required_]
string
A unique identifier that represents the impact.
type [_required_]
enum
The incident impacts type. Allowed enum values: `incident_impacts`
integrations
object
A relationship reference for multiple integration metadata objects.
data [_required_]
[object]
Integration metadata relationship array
id [_required_]
string
A unique identifier that represents the integration metadata.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
last_modified_by_user
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
responders
object
Relationship to incident responders.
data [_required_]
[object]
An array of incident responders.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident responders type. Allowed enum values: `incident_responders`
user_defined_fields
object
Relationship to incident user defined fields.
data [_required_]
[object]
An array of user defined fields.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident user defined fields type. Allowed enum values: `user_defined_field`
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
included
[ <oneOf>]
Included related resources that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
uuid
string
UUID of the user.
id
string
ID of the user.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
```
{
  "data": {
    "attributes": {
      "archived": "2019-09-19T10:00:00.000Z",
      "case_id": "integer",
      "created": "2019-09-19T10:00:00.000Z",
      "customer_impact_duration": "integer",
      "customer_impact_end": "2019-09-19T10:00:00.000Z",
      "customer_impact_scope": "An example customer impact scope",
      "customer_impact_start": "2019-09-19T10:00:00.000Z",
      "customer_impacted": false,
      "declared": "2019-09-19T10:00:00.000Z",
      "declared_by": {
        "image_48_px": "string",
        "name": "string"
      },
      "declared_by_uuid": "string",
      "detected": "2019-09-19T10:00:00.000Z",
      "fields": {
        "<any-key>": "undefined"
      },
      "incident_type_uuid": "00000000-0000-0000-0000-000000000000",
      "is_test": false,
      "modified": "2019-09-19T10:00:00.000Z",
      "non_datadog_creator": {
        "image_48_px": "string",
        "name": "string"
      },
      "notification_handles": [
        {
          "display_name": "Jane Doe",
          "handle": "@test.user@test.com"
        }
      ],
      "public_id": 1,
      "resolved": "2019-09-19T10:00:00.000Z",
      "severity": "UNKNOWN",
      "state": "string",
      "time_to_detect": "integer",
      "time_to_internal_response": "integer",
      "time_to_repair": "integer",
      "time_to_resolve": "integer",
      "title": "A test incident title",
      "visibility": "string"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "attachments": {
        "data": [
          {
            "id": "00000000-0000-abcd-1000-000000000000",
            "type": "incident_attachments"
          }
        ]
      },
      "commander_user": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "users"
        }
      },
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "declared_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "impacts": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "incident_impacts"
          }
        ]
      },
      "integrations": {
        "data": [
          {
            "id": "00000000-abcd-0001-0000-000000000000",
            "type": "incident_integrations"
          }
        ]
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "responders": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "incident_responders"
          }
        ]
      },
      "user_defined_fields": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "user_defined_field"
          }
        ]
      }
    },
    "type": "incidents"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Create an incident returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "incidents",
    "attributes": {
      "title": "Example-Incident",
      "customer_impacted": false,
      "fields": {
        "state": {
          "type": "dropdown",
          "value": "resolved"
        }
      }
    },
    "relationships": {
      "commander_user": {
        "data": {
          "type": "users",
          "id": "string"
        }
      }
    }
  }
}
EOF  

                        
```

#####  Create an incident returns "CREATED" response
```
// Create an incident returns "CREATED" response

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

	body := datadogV2.IncidentCreateRequest{
		Data: datadogV2.IncidentCreateData{
			Type: datadogV2.INCIDENTTYPE_INCIDENTS,
			Attributes: datadogV2.IncidentCreateAttributes{
				Title:            "Example-Incident",
				CustomerImpacted: false,
				Fields: map[string]datadogV2.IncidentFieldAttributes{
					"state": datadogV2.IncidentFieldAttributes{
						IncidentFieldAttributesSingleValue: &datadogV2.IncidentFieldAttributesSingleValue{
							Type:  datadogV2.INCIDENTFIELDATTRIBUTESSINGLEVALUETYPE_DROPDOWN.Ptr(),
							Value: *datadog.NewNullableString(datadog.PtrString("resolved")),
						}},
				},
			},
			Relationships: &datadogV2.IncidentCreateRelationships{
				CommanderUser: *datadogV2.NewNullableNullableRelationshipToUser(&datadogV2.NullableRelationshipToUser{
					Data: *datadogV2.NewNullableNullableRelationshipToUserData(&datadogV2.NullableRelationshipToUserData{
						Type: datadogV2.USERSTYPE_USERS,
						Id:   UserDataID,
					}),
				}),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncident", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.CreateIncident(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.CreateIncident`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.CreateIncident`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create an incident returns "CREATED" response
```
// Create an incident returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentCreateAttributes;
import com.datadog.api.client.v2.model.IncidentCreateData;
import com.datadog.api.client.v2.model.IncidentCreateRelationships;
import com.datadog.api.client.v2.model.IncidentCreateRequest;
import com.datadog.api.client.v2.model.IncidentFieldAttributes;
import com.datadog.api.client.v2.model.IncidentFieldAttributesSingleValue;
import com.datadog.api.client.v2.model.IncidentFieldAttributesSingleValueType;
import com.datadog.api.client.v2.model.IncidentResponse;
import com.datadog.api.client.v2.model.IncidentType;
import com.datadog.api.client.v2.model.NullableRelationshipToUser;
import com.datadog.api.client.v2.model.NullableRelationshipToUserData;
import com.datadog.api.client.v2.model.UsersType;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncident", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    IncidentCreateRequest body =
        new IncidentCreateRequest()
            .data(
                new IncidentCreateData()
                    .type(IncidentType.INCIDENTS)
                    .attributes(
                        new IncidentCreateAttributes()
                            .title("Example-Incident")
                            .customerImpacted(false)
                            .fields(
                                Map.ofEntries(
                                    Map.entry(
                                        "state",
                                        new IncidentFieldAttributes(
                                            new IncidentFieldAttributesSingleValue()
                                                .type(
                                                    IncidentFieldAttributesSingleValueType.DROPDOWN)
                                                .value("resolved"))))))
                    .relationships(
                        new IncidentCreateRelationships()
                            .commanderUser(
                                new NullableRelationshipToUser()
                                    .data(
                                        new NullableRelationshipToUserData()
                                            .type(UsersType.USERS)
                                            .id(USER_DATA_ID)))));

    try {
      IncidentResponse result = apiInstance.createIncident(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#createIncident");
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

#####  Create an incident returns "CREATED" response
```
"""
Create an incident returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_create_attributes import IncidentCreateAttributes
from datadog_api_client.v2.model.incident_create_data import IncidentCreateData
from datadog_api_client.v2.model.incident_create_relationships import IncidentCreateRelationships
from datadog_api_client.v2.model.incident_create_request import IncidentCreateRequest
from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
from datadog_api_client.v2.model.incident_field_attributes_single_value_type import (
    IncidentFieldAttributesSingleValueType,
)
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser
from datadog_api_client.v2.model.nullable_relationship_to_user_data import NullableRelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = IncidentCreateRequest(
    data=IncidentCreateData(
        type=IncidentType.INCIDENTS,
        attributes=IncidentCreateAttributes(
            title="Example-Incident",
            customer_impacted=False,
            fields=dict(
                state=IncidentFieldAttributesSingleValue(
                    type=IncidentFieldAttributesSingleValueType.DROPDOWN,
                    value="resolved",
                ),
            ),
        ),
        relationships=IncidentCreateRelationships(
            commander_user=NullableRelationshipToUser(
                data=NullableRelationshipToUserData(
                    type=UsersType.USERS,
                    id=USER_DATA_ID,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an incident returns "CREATED" response
```
# Create an incident returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::IncidentCreateRequest.new({
  data: DatadogAPIClient::V2::IncidentCreateData.new({
    type: DatadogAPIClient::V2::IncidentType::INCIDENTS,
    attributes: DatadogAPIClient::V2::IncidentCreateAttributes.new({
      title: "Example-Incident",
      customer_impacted: false,
      fields: {
        state: DatadogAPIClient::V2::IncidentFieldAttributesSingleValue.new({
          type: DatadogAPIClient::V2::IncidentFieldAttributesSingleValueType::DROPDOWN,
          value: "resolved",
        }),
      },
    }),
    relationships: DatadogAPIClient::V2::IncidentCreateRelationships.new({
      commander_user: DatadogAPIClient::V2::NullableRelationshipToUser.new({
        data: DatadogAPIClient::V2::NullableRelationshipToUserData.new({
          type: DatadogAPIClient::V2::UsersType::USERS,
          id: USER_DATA_ID,
        }),
      }),
    }),
  }),
})
p api_instance.create_incident(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create an incident returns "CREATED" response
```
// Create an incident returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentCreateAttributes;
use datadog_api_client::datadogV2::model::IncidentCreateData;
use datadog_api_client::datadogV2::model::IncidentCreateRelationships;
use datadog_api_client::datadogV2::model::IncidentCreateRequest;
use datadog_api_client::datadogV2::model::IncidentFieldAttributes;
use datadog_api_client::datadogV2::model::IncidentFieldAttributesSingleValue;
use datadog_api_client::datadogV2::model::IncidentFieldAttributesSingleValueType;
use datadog_api_client::datadogV2::model::IncidentType;
use datadog_api_client::datadogV2::model::NullableRelationshipToUser;
use datadog_api_client::datadogV2::model::NullableRelationshipToUserData;
use datadog_api_client::datadogV2::model::UsersType;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = IncidentCreateRequest::new(
        IncidentCreateData::new(
            IncidentCreateAttributes::new(false, "Example-Incident".to_string()).fields(
                BTreeMap::from([(
                    "state".to_string(),
                    IncidentFieldAttributes::IncidentFieldAttributesSingleValue(Box::new(
                        IncidentFieldAttributesSingleValue::new()
                            .type_(IncidentFieldAttributesSingleValueType::DROPDOWN)
                            .value(Some("resolved".to_string())),
                    )),
                )]),
            ),
            IncidentType::INCIDENTS,
        )
        .relationships(IncidentCreateRelationships::new(Some(
            NullableRelationshipToUser::new(Some(NullableRelationshipToUserData::new(
                user_data_id.clone(),
                UsersType::USERS,
            ))),
        ))),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncident", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api.create_incident(body).await;
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

#####  Create an incident returns "CREATED" response
```
/**
 * Create an incident returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncident"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.IncidentsApiCreateIncidentRequest = {
  body: {
    data: {
      type: "incidents",
      attributes: {
        title: "Example-Incident",
        customerImpacted: false,
        fields: {
          state: {
            type: "dropdown",
            value: "resolved",
          },
        },
      },
      relationships: {
        commanderUser: {
          data: {
            type: "users",
            id: USER_DATA_ID,
          },
        },
      },
    },
  },
};

apiInstance
  .createIncident(params)
  .then((data: v2.IncidentResponse) => {
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
## [Get the details of an incident](https://docs.datadoghq.com/api/latest/incidents/#get-the-details-of-an-incident)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-the-details-of-an-incident-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}
### Overview
Get the details of an incident by `incident_id`. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
#### Query Strings
Name
Type
Description
include
array
Specifies which types of related objects should be included in the response.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#GetIncident-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#GetIncident-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#GetIncident-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#GetIncident-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#GetIncident-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#GetIncident-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident.
Field
Type
Description
data [_required_]
object
Incident data from a response.
attributes
object
The incident's attributes from a response.
archived
date-time
Timestamp of when the incident was archived.
case_id
int64
The incident case id.
created
date-time
Timestamp when the incident was created.
customer_impact_duration
int64
Length of the incident's customer impact in seconds. Equals the difference between `customer_impact_start` and `customer_impact_end`.
customer_impact_end
date-time
Timestamp when customers were no longer impacted by the incident.
customer_impact_scope
string
A summary of the impact customers experienced during the incident.
customer_impact_start
date-time
Timestamp when customers began being impacted by the incident.
customer_impacted
boolean
A flag indicating whether the incident caused customer impact.
declared
date-time
Timestamp when the incident was declared.
declared_by
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
declared_by_uuid
string
UUID of the user who declared the incident.
detected
date-time
Timestamp when the incident was detected.
fields
object
A condensed view of the user-defined fields attached to incidents.
<any-key>
<oneOf>
Dynamic fields for which selections can be made, with field names as keys.
Option 1
object
A field with a single value selected.
type
enum
Type of the single value field definitions. Allowed enum values: `dropdown,textbox`
default: `dropdown`
value
string
The single value selected for this field.
Option 2
object
A field with potentially multiple values selected.
type
enum
Type of the multiple value field definitions. Allowed enum values: `multiselect,textarray,metrictag,autocomplete`
default: `multiselect`
value
[string]
The multiple values selected for this field.
incident_type_uuid
string
A unique identifier that represents an incident type.
is_test
boolean
A flag indicating whether the incident is a test incident.
modified
date-time
Timestamp when the incident was last modified.
non_datadog_creator
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
notification_handles
[object]
Notification handles that will be notified of the incident during update.
display_name
string
The name of the notified handle.
handle
string
The handle used for the notification. This includes an email address, Slack channel, or workflow.
public_id
int64
The monotonically increasing integer ID for the incident.
resolved
date-time
Timestamp when the incident's state was last changed from active or stable to resolved or completed.
severity
enum
The incident severity. Allowed enum values: `UNKNOWN,SEV-0,SEV-1,SEV-2,SEV-3,SEV-4,SEV-5`
state
string
The state incident.
time_to_detect
int64
The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`.
time_to_internal_response
int64
The amount of time in seconds to call incident after detection. Equals the difference of `detected` and `created`.
time_to_repair
int64
The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`.
time_to_resolve
int64
The amount of time in seconds to resolve the incident after it was created. Equals the difference between `created` and `resolved`.
title [_required_]
string
The title of the incident, which summarizes what happened.
visibility
string
The incident visibility status.
id [_required_]
string
The incident's ID.
relationships
object
The incident's relationships from a response.
attachments
object
A relationship reference for attachments.
data [_required_]
[object]
An array of incident attachments.
id [_required_]
string
A unique identifier that represents the attachment.
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
commander_user
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
created_by_user
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
declared_by_user
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
impacts
object
Relationship to impacts.
data [_required_]
[object]
An array of incident impacts.
id [_required_]
string
A unique identifier that represents the impact.
type [_required_]
enum
The incident impacts type. Allowed enum values: `incident_impacts`
integrations
object
A relationship reference for multiple integration metadata objects.
data [_required_]
[object]
Integration metadata relationship array
id [_required_]
string
A unique identifier that represents the integration metadata.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
last_modified_by_user
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
responders
object
Relationship to incident responders.
data [_required_]
[object]
An array of incident responders.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident responders type. Allowed enum values: `incident_responders`
user_defined_fields
object
Relationship to incident user defined fields.
data [_required_]
[object]
An array of user defined fields.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident user defined fields type. Allowed enum values: `user_defined_field`
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
included
[ <oneOf>]
Included related resources that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
uuid
string
UUID of the user.
id
string
ID of the user.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
```
{
  "data": {
    "attributes": {
      "archived": "2019-09-19T10:00:00.000Z",
      "case_id": "integer",
      "created": "2019-09-19T10:00:00.000Z",
      "customer_impact_duration": "integer",
      "customer_impact_end": "2019-09-19T10:00:00.000Z",
      "customer_impact_scope": "An example customer impact scope",
      "customer_impact_start": "2019-09-19T10:00:00.000Z",
      "customer_impacted": false,
      "declared": "2019-09-19T10:00:00.000Z",
      "declared_by": {
        "image_48_px": "string",
        "name": "string"
      },
      "declared_by_uuid": "string",
      "detected": "2019-09-19T10:00:00.000Z",
      "fields": {
        "<any-key>": "undefined"
      },
      "incident_type_uuid": "00000000-0000-0000-0000-000000000000",
      "is_test": false,
      "modified": "2019-09-19T10:00:00.000Z",
      "non_datadog_creator": {
        "image_48_px": "string",
        "name": "string"
      },
      "notification_handles": [
        {
          "display_name": "Jane Doe",
          "handle": "@test.user@test.com"
        }
      ],
      "public_id": 1,
      "resolved": "2019-09-19T10:00:00.000Z",
      "severity": "UNKNOWN",
      "state": "string",
      "time_to_detect": "integer",
      "time_to_internal_response": "integer",
      "time_to_repair": "integer",
      "time_to_resolve": "integer",
      "title": "A test incident title",
      "visibility": "string"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "attachments": {
        "data": [
          {
            "id": "00000000-0000-abcd-1000-000000000000",
            "type": "incident_attachments"
          }
        ]
      },
      "commander_user": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "users"
        }
      },
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "declared_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "impacts": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "incident_impacts"
          }
        ]
      },
      "integrations": {
        "data": [
          {
            "id": "00000000-abcd-0001-0000-000000000000",
            "type": "incident_integrations"
          }
        ]
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "responders": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "incident_responders"
          }
        ]
      },
      "user_defined_fields": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "user_defined_field"
          }
        ]
      }
    },
    "type": "incidents"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get the details of an incident
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the details of an incident
```
"""
Get the details of an incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident(
        incident_id=INCIDENT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get the details of an incident
```
# Get the details of an incident returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]
p api_instance.get_incident(INCIDENT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get the details of an incident
```
// Get the details of an incident returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetIncident", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.GetIncident(ctx, IncidentDataID, *datadogV2.NewGetIncidentOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.GetIncident`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.GetIncident`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get the details of an incident
```
// Get the details of an incident returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncident", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    try {
      IncidentResponse result = apiInstance.getIncident(INCIDENT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getIncident");
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

#####  Get the details of an incident
```
// Get the details of an incident returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::GetIncidentOptionalParams;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncident", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .get_incident(
            incident_data_id.clone(),
            GetIncidentOptionalParams::default(),
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

#####  Get the details of an incident
```
/**
 * Get the details of an incident returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncident"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiGetIncidentRequest = {
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .getIncident(params)
  .then((data: v2.IncidentResponse) => {
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
## [Update an existing incident](https://docs.datadoghq.com/api/latest/incidents/#update-an-existing-incident)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#update-an-existing-incident-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PATCH https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}
### Overview
Updates an incident. Provide only the attributes that should be updated as this request is a partial update. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
#### Query Strings
Name
Type
Description
include
array
Specifies which types of related objects should be included in the response.
### Request
#### Body Data (required)
Incident Payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident data for an update request.
attributes
object
The incident's attributes for an update request.
customer_impact_end
date-time
Timestamp when customers were no longer impacted by the incident.
customer_impact_scope
string
A summary of the impact customers experienced during the incident.
customer_impact_start
date-time
Timestamp when customers began being impacted by the incident.
customer_impacted
boolean
A flag indicating whether the incident caused customer impact.
detected
date-time
Timestamp when the incident was detected.
fields
object
A condensed view of the user-defined fields for which to update selections.
<any-key>
<oneOf>
Dynamic fields for which selections can be made, with field names as keys.
Option 1
object
A field with a single value selected.
type
enum
Type of the single value field definitions. Allowed enum values: `dropdown,textbox`
default: `dropdown`
value
string
The single value selected for this field.
Option 2
object
A field with potentially multiple values selected.
type
enum
Type of the multiple value field definitions. Allowed enum values: `multiselect,textarray,metrictag,autocomplete`
default: `multiselect`
value
[string]
The multiple values selected for this field.
notification_handles
[object]
Notification handles that will be notified of the incident during update.
display_name
string
The name of the notified handle.
handle
string
The handle used for the notification. This includes an email address, Slack channel, or workflow.
title
string
The title of the incident, which summarizes what happened.
id [_required_]
string
The incident's ID.
relationships
object
The incident's relationships for an update request.
commander_user
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
integrations
object
A relationship reference for multiple integration metadata objects.
data [_required_]
[object]
Integration metadata relationship array
id [_required_]
string
A unique identifier that represents the integration metadata.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
postmortem
object
A relationship reference for postmortems.
data [_required_]
object
The postmortem relationship data.
id [_required_]
string
A unique identifier that represents the postmortem.
type [_required_]
enum
Incident postmortem resource type. Allowed enum values: `incident_postmortems`
default: `incident_postmortems`
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
#####  Add commander to an incident returns "OK" response
```
{
  "data": {
    "id": "00000000-0000-0000-1234-000000000000",
    "type": "incidents",
    "relationships": {
      "commander_user": {
        "data": {
          "id": "string",
          "type": "users"
        }
      }
    }
  }
}
```

Copy
#####  Remove commander from an incident returns "OK" response
```
{
  "data": {
    "id": "00000000-0000-0000-1234-000000000000",
    "type": "incidents",
    "relationships": {
      "commander_user": {
        "data": null
      }
    }
  }
}
```

Copy
#####  Update an existing incident returns "OK" response
```
{
  "data": {
    "id": "00000000-0000-0000-1234-000000000000",
    "type": "incidents",
    "attributes": {
      "fields": {
        "state": {
          "type": "dropdown",
          "value": "resolved"
        }
      },
      "title": "A test incident title-updated"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncident-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncident-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncident-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncident-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncident-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncident-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident.
Field
Type
Description
data [_required_]
object
Incident data from a response.
attributes
object
The incident's attributes from a response.
archived
date-time
Timestamp of when the incident was archived.
case_id
int64
The incident case id.
created
date-time
Timestamp when the incident was created.
customer_impact_duration
int64
Length of the incident's customer impact in seconds. Equals the difference between `customer_impact_start` and `customer_impact_end`.
customer_impact_end
date-time
Timestamp when customers were no longer impacted by the incident.
customer_impact_scope
string
A summary of the impact customers experienced during the incident.
customer_impact_start
date-time
Timestamp when customers began being impacted by the incident.
customer_impacted
boolean
A flag indicating whether the incident caused customer impact.
declared
date-time
Timestamp when the incident was declared.
declared_by
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
declared_by_uuid
string
UUID of the user who declared the incident.
detected
date-time
Timestamp when the incident was detected.
fields
object
A condensed view of the user-defined fields attached to incidents.
<any-key>
<oneOf>
Dynamic fields for which selections can be made, with field names as keys.
Option 1
object
A field with a single value selected.
type
enum
Type of the single value field definitions. Allowed enum values: `dropdown,textbox`
default: `dropdown`
value
string
The single value selected for this field.
Option 2
object
A field with potentially multiple values selected.
type
enum
Type of the multiple value field definitions. Allowed enum values: `multiselect,textarray,metrictag,autocomplete`
default: `multiselect`
value
[string]
The multiple values selected for this field.
incident_type_uuid
string
A unique identifier that represents an incident type.
is_test
boolean
A flag indicating whether the incident is a test incident.
modified
date-time
Timestamp when the incident was last modified.
non_datadog_creator
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
notification_handles
[object]
Notification handles that will be notified of the incident during update.
display_name
string
The name of the notified handle.
handle
string
The handle used for the notification. This includes an email address, Slack channel, or workflow.
public_id
int64
The monotonically increasing integer ID for the incident.
resolved
date-time
Timestamp when the incident's state was last changed from active or stable to resolved or completed.
severity
enum
The incident severity. Allowed enum values: `UNKNOWN,SEV-0,SEV-1,SEV-2,SEV-3,SEV-4,SEV-5`
state
string
The state incident.
time_to_detect
int64
The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`.
time_to_internal_response
int64
The amount of time in seconds to call incident after detection. Equals the difference of `detected` and `created`.
time_to_repair
int64
The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`.
time_to_resolve
int64
The amount of time in seconds to resolve the incident after it was created. Equals the difference between `created` and `resolved`.
title [_required_]
string
The title of the incident, which summarizes what happened.
visibility
string
The incident visibility status.
id [_required_]
string
The incident's ID.
relationships
object
The incident's relationships from a response.
attachments
object
A relationship reference for attachments.
data [_required_]
[object]
An array of incident attachments.
id [_required_]
string
A unique identifier that represents the attachment.
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
commander_user
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
created_by_user
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
declared_by_user
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
impacts
object
Relationship to impacts.
data [_required_]
[object]
An array of incident impacts.
id [_required_]
string
A unique identifier that represents the impact.
type [_required_]
enum
The incident impacts type. Allowed enum values: `incident_impacts`
integrations
object
A relationship reference for multiple integration metadata objects.
data [_required_]
[object]
Integration metadata relationship array
id [_required_]
string
A unique identifier that represents the integration metadata.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
last_modified_by_user
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
responders
object
Relationship to incident responders.
data [_required_]
[object]
An array of incident responders.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident responders type. Allowed enum values: `incident_responders`
user_defined_fields
object
Relationship to incident user defined fields.
data [_required_]
[object]
An array of user defined fields.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident user defined fields type. Allowed enum values: `user_defined_field`
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
included
[ <oneOf>]
Included related resources that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
uuid
string
UUID of the user.
id
string
ID of the user.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
```
{
  "data": {
    "attributes": {
      "archived": "2019-09-19T10:00:00.000Z",
      "case_id": "integer",
      "created": "2019-09-19T10:00:00.000Z",
      "customer_impact_duration": "integer",
      "customer_impact_end": "2019-09-19T10:00:00.000Z",
      "customer_impact_scope": "An example customer impact scope",
      "customer_impact_start": "2019-09-19T10:00:00.000Z",
      "customer_impacted": false,
      "declared": "2019-09-19T10:00:00.000Z",
      "declared_by": {
        "image_48_px": "string",
        "name": "string"
      },
      "declared_by_uuid": "string",
      "detected": "2019-09-19T10:00:00.000Z",
      "fields": {
        "<any-key>": "undefined"
      },
      "incident_type_uuid": "00000000-0000-0000-0000-000000000000",
      "is_test": false,
      "modified": "2019-09-19T10:00:00.000Z",
      "non_datadog_creator": {
        "image_48_px": "string",
        "name": "string"
      },
      "notification_handles": [
        {
          "display_name": "Jane Doe",
          "handle": "@test.user@test.com"
        }
      ],
      "public_id": 1,
      "resolved": "2019-09-19T10:00:00.000Z",
      "severity": "UNKNOWN",
      "state": "string",
      "time_to_detect": "integer",
      "time_to_internal_response": "integer",
      "time_to_repair": "integer",
      "time_to_resolve": "integer",
      "title": "A test incident title",
      "visibility": "string"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "attachments": {
        "data": [
          {
            "id": "00000000-0000-abcd-1000-000000000000",
            "type": "incident_attachments"
          }
        ]
      },
      "commander_user": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "users"
        }
      },
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "declared_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "impacts": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "incident_impacts"
          }
        ]
      },
      "integrations": {
        "data": [
          {
            "id": "00000000-abcd-0001-0000-000000000000",
            "type": "incident_integrations"
          }
        ]
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "responders": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "incident_responders"
          }
        ]
      },
      "user_defined_fields": {
        "data": [
          {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "user_defined_field"
          }
        ]
      }
    },
    "type": "incidents"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Add commander to an incident returns "OK" response
Copy
```
                          # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "00000000-0000-0000-1234-000000000000",
    "type": "incidents",
    "relationships": {
      "commander_user": {
        "data": {
          "id": "string",
          "type": "users"
        }
      }
    }
  }
}
EOF  

                        
```

#####  Remove commander from an incident returns "OK" response
Copy
```
                          # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "00000000-0000-0000-1234-000000000000",
    "type": "incidents",
    "relationships": {
      "commander_user": {
        "data": null
      }
    }
  }
}
EOF  

                        
```

#####  Update an existing incident returns "OK" response
Copy
```
                          # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "00000000-0000-0000-1234-000000000000",
    "type": "incidents",
    "attributes": {
      "fields": {
        "state": {
          "type": "dropdown",
          "value": "resolved"
        }
      },
      "title": "A test incident title-updated"
    }
  }
}
EOF  

                        
```

#####  Add commander to an incident returns "OK" response 
```
// Add commander to an incident returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	body := datadogV2.IncidentUpdateRequest{
		Data: datadogV2.IncidentUpdateData{
			Id:   IncidentDataID,
			Type: datadogV2.INCIDENTTYPE_INCIDENTS,
			Relationships: &datadogV2.IncidentUpdateRelationships{
				CommanderUser: *datadogV2.NewNullableNullableRelationshipToUser(&datadogV2.NullableRelationshipToUser{
					Data: *datadogV2.NewNullableNullableRelationshipToUserData(&datadogV2.NullableRelationshipToUserData{
						Id:   UserDataID,
						Type: datadogV2.USERSTYPE_USERS,
					}),
				}),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncident", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncident(ctx, IncidentDataID, body, *datadogV2.NewUpdateIncidentOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncident`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncident`:\n%s\n", responseContent)
}

```

Copy
#####  Remove commander from an incident returns "OK" response 
```
// Remove commander from an incident returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	body := datadogV2.IncidentUpdateRequest{
		Data: datadogV2.IncidentUpdateData{
			Id:   IncidentDataID,
			Type: datadogV2.INCIDENTTYPE_INCIDENTS,
			Relationships: &datadogV2.IncidentUpdateRelationships{
				CommanderUser: *datadogV2.NewNullableNullableRelationshipToUser(&datadogV2.NullableRelationshipToUser{
					Data: *datadogV2.NewNullableNullableRelationshipToUserData(nil),
				}),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncident", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncident(ctx, IncidentDataID, body, *datadogV2.NewUpdateIncidentOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncident`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncident`:\n%s\n", responseContent)
}

```

Copy
#####  Update an existing incident returns "OK" response 
```
// Update an existing incident returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	body := datadogV2.IncidentUpdateRequest{
		Data: datadogV2.IncidentUpdateData{
			Id:   IncidentDataID,
			Type: datadogV2.INCIDENTTYPE_INCIDENTS,
			Attributes: &datadogV2.IncidentUpdateAttributes{
				Fields: map[string]datadogV2.IncidentFieldAttributes{
					"state": datadogV2.IncidentFieldAttributes{
						IncidentFieldAttributesSingleValue: &datadogV2.IncidentFieldAttributesSingleValue{
							Type:  datadogV2.INCIDENTFIELDATTRIBUTESSINGLEVALUETYPE_DROPDOWN.Ptr(),
							Value: *datadog.NewNullableString(datadog.PtrString("resolved")),
						}},
				},
				Title: datadog.PtrString("A test incident title-updated"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncident", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncident(ctx, IncidentDataID, body, *datadogV2.NewUpdateIncidentOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncident`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncident`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Add commander to an incident returns "OK" response 
```
// Add commander to an incident returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentResponse;
import com.datadog.api.client.v2.model.IncidentType;
import com.datadog.api.client.v2.model.IncidentUpdateData;
import com.datadog.api.client.v2.model.IncidentUpdateRelationships;
import com.datadog.api.client.v2.model.IncidentUpdateRequest;
import com.datadog.api.client.v2.model.NullableRelationshipToUser;
import com.datadog.api.client.v2.model.NullableRelationshipToUserData;
import com.datadog.api.client.v2.model.UsersType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncident", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    IncidentUpdateRequest body =
        new IncidentUpdateRequest()
            .data(
                new IncidentUpdateData()
                    .id(INCIDENT_DATA_ID)
                    .type(IncidentType.INCIDENTS)
                    .relationships(
                        new IncidentUpdateRelationships()
                            .commanderUser(
                                new NullableRelationshipToUser()
                                    .data(
                                        new NullableRelationshipToUserData()
                                            .id(USER_DATA_ID)
                                            .type(UsersType.USERS)))));

    try {
      IncidentResponse result = apiInstance.updateIncident(INCIDENT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncident");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Remove commander from an incident returns "OK" response 
```
// Remove commander from an incident returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentResponse;
import com.datadog.api.client.v2.model.IncidentType;
import com.datadog.api.client.v2.model.IncidentUpdateData;
import com.datadog.api.client.v2.model.IncidentUpdateRelationships;
import com.datadog.api.client.v2.model.IncidentUpdateRequest;
import com.datadog.api.client.v2.model.NullableRelationshipToUser;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncident", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    IncidentUpdateRequest body =
        new IncidentUpdateRequest()
            .data(
                new IncidentUpdateData()
                    .id(INCIDENT_DATA_ID)
                    .type(IncidentType.INCIDENTS)
                    .relationships(
                        new IncidentUpdateRelationships()
                            .commanderUser(new NullableRelationshipToUser().data(null))));

    try {
      IncidentResponse result = apiInstance.updateIncident(INCIDENT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncident");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Update an existing incident returns "OK" response 
```
// Update an existing incident returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentFieldAttributes;
import com.datadog.api.client.v2.model.IncidentFieldAttributesSingleValue;
import com.datadog.api.client.v2.model.IncidentFieldAttributesSingleValueType;
import com.datadog.api.client.v2.model.IncidentResponse;
import com.datadog.api.client.v2.model.IncidentType;
import com.datadog.api.client.v2.model.IncidentUpdateAttributes;
import com.datadog.api.client.v2.model.IncidentUpdateData;
import com.datadog.api.client.v2.model.IncidentUpdateRequest;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncident", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ATTRIBUTES_TITLE = System.getenv("INCIDENT_DATA_ATTRIBUTES_TITLE");
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    IncidentUpdateRequest body =
        new IncidentUpdateRequest()
            .data(
                new IncidentUpdateData()
                    .id(INCIDENT_DATA_ID)
                    .type(IncidentType.INCIDENTS)
                    .attributes(
                        new IncidentUpdateAttributes()
                            .fields(
                                Map.ofEntries(
                                    Map.entry(
                                        "state",
                                        new IncidentFieldAttributes(
                                            new IncidentFieldAttributesSingleValue()
                                                .type(
                                                    IncidentFieldAttributesSingleValueType.DROPDOWN)
                                                .value("resolved")))))
                            .title("A test incident title-updated")));

    try {
      IncidentResponse result = apiInstance.updateIncident(INCIDENT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncident");
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

#####  Add commander to an incident returns "OK" response 
```
"""
Add commander to an incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData
from datadog_api_client.v2.model.incident_update_relationships import IncidentUpdateRelationships
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest
from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser
from datadog_api_client.v2.model.nullable_relationship_to_user_data import NullableRelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = IncidentUpdateRequest(
    data=IncidentUpdateData(
        id=INCIDENT_DATA_ID,
        type=IncidentType.INCIDENTS,
        relationships=IncidentUpdateRelationships(
            commander_user=NullableRelationshipToUser(
                data=NullableRelationshipToUserData(
                    id=USER_DATA_ID,
                    type=UsersType.USERS,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)

```

Copy
#####  Remove commander from an incident returns "OK" response 
```
"""
Remove commander from an incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData
from datadog_api_client.v2.model.incident_update_relationships import IncidentUpdateRelationships
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest
from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentUpdateRequest(
    data=IncidentUpdateData(
        id=INCIDENT_DATA_ID,
        type=IncidentType.INCIDENTS,
        relationships=IncidentUpdateRelationships(
            commander_user=NullableRelationshipToUser(
                data=None,
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)

```

Copy
#####  Update an existing incident returns "OK" response 
```
"""
Update an existing incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
from datadog_api_client.v2.model.incident_field_attributes_single_value_type import (
    IncidentFieldAttributesSingleValueType,
)
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.incident_update_attributes import IncidentUpdateAttributes
from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest

# there is a valid "incident" in the system
INCIDENT_DATA_ATTRIBUTES_TITLE = environ["INCIDENT_DATA_ATTRIBUTES_TITLE"]
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentUpdateRequest(
    data=IncidentUpdateData(
        id=INCIDENT_DATA_ID,
        type=IncidentType.INCIDENTS,
        attributes=IncidentUpdateAttributes(
            fields=dict(
                state=IncidentFieldAttributesSingleValue(
                    type=IncidentFieldAttributesSingleValueType.DROPDOWN,
                    value="resolved",
                ),
            ),
            title="A test incident title-updated",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Add commander to an incident returns "OK" response 
```
# Add commander to an incident returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::IncidentUpdateRequest.new({
  data: DatadogAPIClient::V2::IncidentUpdateData.new({
    id: INCIDENT_DATA_ID,
    type: DatadogAPIClient::V2::IncidentType::INCIDENTS,
    relationships: DatadogAPIClient::V2::IncidentUpdateRelationships.new({
      commander_user: DatadogAPIClient::V2::NullableRelationshipToUser.new({
        data: DatadogAPIClient::V2::NullableRelationshipToUserData.new({
          id: USER_DATA_ID,
          type: DatadogAPIClient::V2::UsersType::USERS,
        }),
      }),
    }),
  }),
})
p api_instance.update_incident(INCIDENT_DATA_ID, body)

```

Copy
#####  Remove commander from an incident returns "OK" response 
```
# Remove commander from an incident returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

body = DatadogAPIClient::V2::IncidentUpdateRequest.new({
  data: DatadogAPIClient::V2::IncidentUpdateData.new({
    id: INCIDENT_DATA_ID,
    type: DatadogAPIClient::V2::IncidentType::INCIDENTS,
    relationships: DatadogAPIClient::V2::IncidentUpdateRelationships.new({
      commander_user: DatadogAPIClient::V2::NullableRelationshipToUser.new({
        data: nil,
      }),
    }),
  }),
})
p api_instance.update_incident(INCIDENT_DATA_ID, body)

```

Copy
#####  Update an existing incident returns "OK" response 
```
# Update an existing incident returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ATTRIBUTES_TITLE = ENV["INCIDENT_DATA_ATTRIBUTES_TITLE"]
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

body = DatadogAPIClient::V2::IncidentUpdateRequest.new({
  data: DatadogAPIClient::V2::IncidentUpdateData.new({
    id: INCIDENT_DATA_ID,
    type: DatadogAPIClient::V2::IncidentType::INCIDENTS,
    attributes: DatadogAPIClient::V2::IncidentUpdateAttributes.new({
      fields: {
        state: DatadogAPIClient::V2::IncidentFieldAttributesSingleValue.new({
          type: DatadogAPIClient::V2::IncidentFieldAttributesSingleValueType::DROPDOWN,
          value: "resolved",
        }),
      },
      title: "A test incident title-updated",
    }),
  }),
})
p api_instance.update_incident(INCIDENT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Add commander to an incident returns "OK" response 
```
// Add commander to an incident returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::UpdateIncidentOptionalParams;
use datadog_api_client::datadogV2::model::IncidentType;
use datadog_api_client::datadogV2::model::IncidentUpdateData;
use datadog_api_client::datadogV2::model::IncidentUpdateRelationships;
use datadog_api_client::datadogV2::model::IncidentUpdateRequest;
use datadog_api_client::datadogV2::model::NullableRelationshipToUser;
use datadog_api_client::datadogV2::model::NullableRelationshipToUserData;
use datadog_api_client::datadogV2::model::UsersType;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();

    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = IncidentUpdateRequest::new(
        IncidentUpdateData::new(incident_data_id.clone(), IncidentType::INCIDENTS).relationships(
            IncidentUpdateRelationships::new().commander_user(Some(
                NullableRelationshipToUser::new(Some(NullableRelationshipToUserData::new(
                    user_data_id.clone(),
                    UsersType::USERS,
                ))),
            )),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncident", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident(
            incident_data_id.clone(),
            body,
            UpdateIncidentOptionalParams::default(),
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
#####  Remove commander from an incident returns "OK" response 
```
// Remove commander from an incident returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::UpdateIncidentOptionalParams;
use datadog_api_client::datadogV2::model::IncidentType;
use datadog_api_client::datadogV2::model::IncidentUpdateData;
use datadog_api_client::datadogV2::model::IncidentUpdateRelationships;
use datadog_api_client::datadogV2::model::IncidentUpdateRequest;
use datadog_api_client::datadogV2::model::NullableRelationshipToUser;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let body = IncidentUpdateRequest::new(
        IncidentUpdateData::new(incident_data_id.clone(), IncidentType::INCIDENTS).relationships(
            IncidentUpdateRelationships::new()
                .commander_user(Some(NullableRelationshipToUser::new(None))),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncident", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident(
            incident_data_id.clone(),
            body,
            UpdateIncidentOptionalParams::default(),
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
#####  Update an existing incident returns "OK" response 
```
// Update an existing incident returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::UpdateIncidentOptionalParams;
use datadog_api_client::datadogV2::model::IncidentFieldAttributes;
use datadog_api_client::datadogV2::model::IncidentFieldAttributesSingleValue;
use datadog_api_client::datadogV2::model::IncidentFieldAttributesSingleValueType;
use datadog_api_client::datadogV2::model::IncidentType;
use datadog_api_client::datadogV2::model::IncidentUpdateAttributes;
use datadog_api_client::datadogV2::model::IncidentUpdateData;
use datadog_api_client::datadogV2::model::IncidentUpdateRequest;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let body = IncidentUpdateRequest::new(
        IncidentUpdateData::new(incident_data_id.clone(), IncidentType::INCIDENTS).attributes(
            IncidentUpdateAttributes::new()
                .fields(BTreeMap::from([(
                    "state".to_string(),
                    IncidentFieldAttributes::IncidentFieldAttributesSingleValue(Box::new(
                        IncidentFieldAttributesSingleValue::new()
                            .type_(IncidentFieldAttributesSingleValueType::DROPDOWN)
                            .value(Some("resolved".to_string())),
                    )),
                )]))
                .title("A test incident title-updated".to_string()),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncident", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident(
            incident_data_id.clone(),
            body,
            UpdateIncidentOptionalParams::default(),
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

#####  Add commander to an incident returns "OK" response 
```
/**
 * Add commander to an incident returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncident"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentRequest = {
  body: {
    data: {
      id: INCIDENT_DATA_ID,
      type: "incidents",
      relationships: {
        commanderUser: {
          data: {
            id: USER_DATA_ID,
            type: "users",
          },
        },
      },
    },
  },
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .updateIncident(params)
  .then((data: v2.IncidentResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Remove commander from an incident returns "OK" response 
```
/**
 * Remove commander from an incident returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncident"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentRequest = {
  body: {
    data: {
      id: INCIDENT_DATA_ID,
      type: "incidents",
      relationships: {
        commanderUser: {
          data: null,
        },
      },
    },
  },
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .updateIncident(params)
  .then((data: v2.IncidentResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Update an existing incident returns "OK" response 
```
/**
 * Update an existing incident returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncident"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentRequest = {
  body: {
    data: {
      id: INCIDENT_DATA_ID,
      type: "incidents",
      attributes: {
        fields: {
          state: {
            type: "dropdown",
            value: "resolved",
          },
        },
        title: "A test incident title-updated",
      },
    },
  },
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .updateIncident(params)
  .then((data: v2.IncidentResponse) => {
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
## [Delete an existing incident](https://docs.datadoghq.com/api/latest/incidents/#delete-an-existing-incident)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-an-existing-incident-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}
### Overview
Deletes an existing incident from the users organization. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncident-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncident-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncident-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncident-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncident-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncident-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Delete an existing incident
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an existing incident
```
"""
Delete an existing incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident(
        incident_id=INCIDENT_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an existing incident
```
# Delete an existing incident returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]
api_instance.delete_incident(INCIDENT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an existing incident
```
// Delete an existing incident returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncident", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	r, err := api.DeleteIncident(ctx, IncidentDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.DeleteIncident`: %v\n", err)
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

#####  Delete an existing incident
```
// Delete an existing incident returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncident", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    try {
      apiInstance.deleteIncident(INCIDENT_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#deleteIncident");
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

#####  Delete an existing incident
```
// Delete an existing incident returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncident", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api.delete_incident(incident_data_id.clone()).await;
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

#####  Delete an existing incident
```
/**
 * Delete an existing incident returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncident"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiDeleteIncidentRequest = {
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .deleteIncident(params)
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
## [Get a list of incidents](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-incidents)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-incidents-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidentshttps://api.ap2.datadoghq.com/api/v2/incidentshttps://api.datadoghq.eu/api/v2/incidentshttps://api.ddog-gov.com/api/v2/incidentshttps://api.datadoghq.com/api/v2/incidentshttps://api.us3.datadoghq.com/api/v2/incidentshttps://api.us5.datadoghq.com/api/v2/incidents
### Overview
Get all incidents for the user’s organization. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
include
array
Specifies which types of related objects should be included in the response.
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[offset]
integer
Specific offset to use as the beginning of the returned page.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidents-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidents-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#ListIncidents-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#ListIncidents-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#ListIncidents-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidents-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a list of incidents.
Field
Type
Description
data [_required_]
[object]
An array of incidents.
attributes
object
The incident's attributes from a response.
archived
date-time
Timestamp of when the incident was archived.
case_id
int64
The incident case id.
created
date-time
Timestamp when the incident was created.
customer_impact_duration
int64
Length of the incident's customer impact in seconds. Equals the difference between `customer_impact_start` and `customer_impact_end`.
customer_impact_end
date-time
Timestamp when customers were no longer impacted by the incident.
customer_impact_scope
string
A summary of the impact customers experienced during the incident.
customer_impact_start
date-time
Timestamp when customers began being impacted by the incident.
customer_impacted
boolean
A flag indicating whether the incident caused customer impact.
declared
date-time
Timestamp when the incident was declared.
declared_by
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
declared_by_uuid
string
UUID of the user who declared the incident.
detected
date-time
Timestamp when the incident was detected.
fields
object
A condensed view of the user-defined fields attached to incidents.
<any-key>
<oneOf>
Dynamic fields for which selections can be made, with field names as keys.
Option 1
object
A field with a single value selected.
type
enum
Type of the single value field definitions. Allowed enum values: `dropdown,textbox`
default: `dropdown`
value
string
The single value selected for this field.
Option 2
object
A field with potentially multiple values selected.
type
enum
Type of the multiple value field definitions. Allowed enum values: `multiselect,textarray,metrictag,autocomplete`
default: `multiselect`
value
[string]
The multiple values selected for this field.
incident_type_uuid
string
A unique identifier that represents an incident type.
is_test
boolean
A flag indicating whether the incident is a test incident.
modified
date-time
Timestamp when the incident was last modified.
non_datadog_creator
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
notification_handles
[object]
Notification handles that will be notified of the incident during update.
display_name
string
The name of the notified handle.
handle
string
The handle used for the notification. This includes an email address, Slack channel, or workflow.
public_id
int64
The monotonically increasing integer ID for the incident.
resolved
date-time
Timestamp when the incident's state was last changed from active or stable to resolved or completed.
severity
enum
The incident severity. Allowed enum values: `UNKNOWN,SEV-0,SEV-1,SEV-2,SEV-3,SEV-4,SEV-5`
state
string
The state incident.
time_to_detect
int64
The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`.
time_to_internal_response
int64
The amount of time in seconds to call incident after detection. Equals the difference of `detected` and `created`.
time_to_repair
int64
The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`.
time_to_resolve
int64
The amount of time in seconds to resolve the incident after it was created. Equals the difference between `created` and `resolved`.
title [_required_]
string
The title of the incident, which summarizes what happened.
visibility
string
The incident visibility status.
id [_required_]
string
The incident's ID.
relationships
object
The incident's relationships from a response.
attachments
object
A relationship reference for attachments.
data [_required_]
[object]
An array of incident attachments.
id [_required_]
string
A unique identifier that represents the attachment.
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
commander_user
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
created_by_user
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
declared_by_user
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
impacts
object
Relationship to impacts.
data [_required_]
[object]
An array of incident impacts.
id [_required_]
string
A unique identifier that represents the impact.
type [_required_]
enum
The incident impacts type. Allowed enum values: `incident_impacts`
integrations
object
A relationship reference for multiple integration metadata objects.
data [_required_]
[object]
Integration metadata relationship array
id [_required_]
string
A unique identifier that represents the integration metadata.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
last_modified_by_user
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
responders
object
Relationship to incident responders.
data [_required_]
[object]
An array of incident responders.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident responders type. Allowed enum values: `incident_responders`
user_defined_fields
object
Relationship to incident user defined fields.
data [_required_]
[object]
An array of user defined fields.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident user defined fields type. Allowed enum values: `user_defined_field`
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
included
[ <oneOf>]
Included related resources that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
uuid
string
UUID of the user.
id
string
ID of the user.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
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
        "archived": "2019-09-19T10:00:00.000Z",
        "case_id": "integer",
        "created": "2019-09-19T10:00:00.000Z",
        "customer_impact_duration": "integer",
        "customer_impact_end": "2019-09-19T10:00:00.000Z",
        "customer_impact_scope": "An example customer impact scope",
        "customer_impact_start": "2019-09-19T10:00:00.000Z",
        "customer_impacted": false,
        "declared": "2019-09-19T10:00:00.000Z",
        "declared_by": {
          "image_48_px": "string",
          "name": "string"
        },
        "declared_by_uuid": "string",
        "detected": "2019-09-19T10:00:00.000Z",
        "fields": {
          "<any-key>": "undefined"
        },
        "incident_type_uuid": "00000000-0000-0000-0000-000000000000",
        "is_test": false,
        "modified": "2019-09-19T10:00:00.000Z",
        "non_datadog_creator": {
          "image_48_px": "string",
          "name": "string"
        },
        "notification_handles": [
          {
            "display_name": "Jane Doe",
            "handle": "@test.user@test.com"
          }
        ],
        "public_id": 1,
        "resolved": "2019-09-19T10:00:00.000Z",
        "severity": "UNKNOWN",
        "state": "string",
        "time_to_detect": "integer",
        "time_to_internal_response": "integer",
        "time_to_repair": "integer",
        "time_to_resolve": "integer",
        "title": "A test incident title",
        "visibility": "string"
      },
      "id": "00000000-0000-0000-1234-000000000000",
      "relationships": {
        "attachments": {
          "data": [
            {
              "id": "00000000-0000-abcd-1000-000000000000",
              "type": "incident_attachments"
            }
          ]
        },
        "commander_user": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "users"
          }
        },
        "created_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "declared_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "impacts": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "incident_impacts"
            }
          ]
        },
        "integrations": {
          "data": [
            {
              "id": "00000000-abcd-0001-0000-000000000000",
              "type": "incident_integrations"
            }
          ]
        },
        "last_modified_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "responders": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "incident_responders"
            }
          ]
        },
        "user_defined_fields": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "user_defined_field"
            }
          ]
        }
      },
      "type": "incidents"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get a list of incidents
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of incidents
```
"""
Get a list of incidents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["list_incidents"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incidents()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of incidents
```
# Get a list of incidents returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incidents".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.list_incidents()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of incidents
```
// Get a list of incidents returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListIncidents", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidents(ctx, *datadogV2.NewListIncidentsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidents`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of incidents
```
// Get a list of incidents returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidents", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentsResponse result = apiInstance.listIncidents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidents");
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

#####  Get a list of incidents
```
// Get a list of incidents returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::ListIncidentsOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidents", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .list_incidents(ListIncidentsOptionalParams::default())
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

#####  Get a list of incidents
```
/**
 * Get a list of incidents returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidents"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

apiInstance
  .listIncidents()
  .then((data: v2.IncidentsResponse) => {
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
## [Search for incidents](https://docs.datadoghq.com/api/latest/incidents/#search-for-incidents)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#search-for-incidents-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/searchhttps://api.ap2.datadoghq.com/api/v2/incidents/searchhttps://api.datadoghq.eu/api/v2/incidents/searchhttps://api.ddog-gov.com/api/v2/incidents/searchhttps://api.datadoghq.com/api/v2/incidents/searchhttps://api.us3.datadoghq.com/api/v2/incidents/searchhttps://api.us5.datadoghq.com/api/v2/incidents/search
### Overview
Search for incidents matching a certain query. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
include
enum
Specifies which types of related objects should be included in the response.  
Allowed enum values: `users, attachments`
query [_required_]
string
Specifies which incidents should be returned. The query can contain any number of incident facets joined by `ANDs`, along with multiple values for each of those facets joined by `OR`s. For example: `state:active AND severity:(SEV-2 OR SEV-1)`.
sort
enum
Specifies the order of returned incidents.  
Allowed enum values: `created, -created`
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[offset]
integer
Specific offset to use as the beginning of the returned page.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#SearchIncidents-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#SearchIncidents-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#SearchIncidents-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#SearchIncidents-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#SearchIncidents-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#SearchIncidents-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with incidents and facets.
Field
Type
Description
data [_required_]
object
Data returned by an incident search.
attributes
object
Attributes returned by an incident search.
facets [_required_]
object
Facet data for incidents returned by a search query.
commander
[object]
Facet data for incident commander users.
count
int32
Count of the facet value appearing in search results.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
uuid
string
ID of the user.
created_by
[object]
Facet data for incident creator users.
count
int32
Count of the facet value appearing in search results.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
uuid
string
ID of the user.
fields
[object]
Facet data for incident property fields.
aggregates
object
Aggregate information for numeric incident data.
max
double
Maximum value of the numeric aggregates.
min
double
Minimum value of the numeric aggregates.
facets [_required_]
[object]
Facet data for the property field of an incident.
count
int32
Count of the facet value appearing in search results.
name
string
The facet value appearing in search results.
name [_required_]
string
Name of the incident property field.
impact
[object]
Facet data for incident impact attributes.
count
int32
Count of the facet value appearing in search results.
name
string
The facet value appearing in search results.
last_modified_by
[object]
Facet data for incident last modified by users.
count
int32
Count of the facet value appearing in search results.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
uuid
string
ID of the user.
postmortem
[object]
Facet data for incident postmortem existence.
count
int32
Count of the facet value appearing in search results.
name
string
The facet value appearing in search results.
responder
[object]
Facet data for incident responder users.
count
int32
Count of the facet value appearing in search results.
email
string
Email of the user.
handle
string
Handle of the user.
name
string
Name of the user.
uuid
string
ID of the user.
severity
[object]
Facet data for incident severity attributes.
count
int32
Count of the facet value appearing in search results.
name
string
The facet value appearing in search results.
state
[object]
Facet data for incident state attributes.
count
int32
Count of the facet value appearing in search results.
name
string
The facet value appearing in search results.
time_to_repair
[object]
Facet data for incident time to repair metrics.
aggregates [_required_]
object
Aggregate information for numeric incident data.
max
double
Maximum value of the numeric aggregates.
min
double
Minimum value of the numeric aggregates.
name [_required_]
string
Name of the incident property field.
time_to_resolve
[object]
Facet data for incident time to resolve metrics.
aggregates [_required_]
object
Aggregate information for numeric incident data.
max
double
Maximum value of the numeric aggregates.
min
double
Minimum value of the numeric aggregates.
name [_required_]
string
Name of the incident property field.
incidents [_required_]
[object]
Incidents returned by the search.
data [_required_]
object
Incident data from a response.
attributes
object
The incident's attributes from a response.
archived
date-time
Timestamp of when the incident was archived.
case_id
int64
The incident case id.
created
date-time
Timestamp when the incident was created.
customer_impact_duration
int64
Length of the incident's customer impact in seconds. Equals the difference between `customer_impact_start` and `customer_impact_end`.
customer_impact_end
date-time
Timestamp when customers were no longer impacted by the incident.
customer_impact_scope
string
A summary of the impact customers experienced during the incident.
customer_impact_start
date-time
Timestamp when customers began being impacted by the incident.
customer_impacted
boolean
A flag indicating whether the incident caused customer impact.
declared
date-time
Timestamp when the incident was declared.
declared_by
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
declared_by_uuid
string
UUID of the user who declared the incident.
detected
date-time
Timestamp when the incident was detected.
fields
object
A condensed view of the user-defined fields attached to incidents.
<any-key>
<oneOf>
Dynamic fields for which selections can be made, with field names as keys.
Option 1
object
A field with a single value selected.
type
enum
Type of the single value field definitions. Allowed enum values: `dropdown,textbox`
default: `dropdown`
value
string
The single value selected for this field.
Option 2
object
A field with potentially multiple values selected.
type
enum
Type of the multiple value field definitions. Allowed enum values: `multiselect,textarray,metrictag,autocomplete`
default: `multiselect`
value
[string]
The multiple values selected for this field.
incident_type_uuid
string
A unique identifier that represents an incident type.
is_test
boolean
A flag indicating whether the incident is a test incident.
modified
date-time
Timestamp when the incident was last modified.
non_datadog_creator
object
Incident's non Datadog creator.
image_48_px
string
Non Datadog creator `48px` image.
name
string
Non Datadog creator name.
notification_handles
[object]
Notification handles that will be notified of the incident during update.
display_name
string
The name of the notified handle.
handle
string
The handle used for the notification. This includes an email address, Slack channel, or workflow.
public_id
int64
The monotonically increasing integer ID for the incident.
resolved
date-time
Timestamp when the incident's state was last changed from active or stable to resolved or completed.
severity
enum
The incident severity. Allowed enum values: `UNKNOWN,SEV-0,SEV-1,SEV-2,SEV-3,SEV-4,SEV-5`
state
string
The state incident.
time_to_detect
int64
The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`.
time_to_internal_response
int64
The amount of time in seconds to call incident after detection. Equals the difference of `detected` and `created`.
time_to_repair
int64
The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`.
time_to_resolve
int64
The amount of time in seconds to resolve the incident after it was created. Equals the difference between `created` and `resolved`.
title [_required_]
string
The title of the incident, which summarizes what happened.
visibility
string
The incident visibility status.
id [_required_]
string
The incident's ID.
relationships
object
The incident's relationships from a response.
attachments
object
A relationship reference for attachments.
data [_required_]
[object]
An array of incident attachments.
id [_required_]
string
A unique identifier that represents the attachment.
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
commander_user
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
created_by_user
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
declared_by_user
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
impacts
object
Relationship to impacts.
data [_required_]
[object]
An array of incident impacts.
id [_required_]
string
A unique identifier that represents the impact.
type [_required_]
enum
The incident impacts type. Allowed enum values: `incident_impacts`
integrations
object
A relationship reference for multiple integration metadata objects.
data [_required_]
[object]
Integration metadata relationship array
id [_required_]
string
A unique identifier that represents the integration metadata.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
last_modified_by_user
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
responders
object
Relationship to incident responders.
data [_required_]
[object]
An array of incident responders.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident responders type. Allowed enum values: `incident_responders`
user_defined_fields
object
Relationship to incident user defined fields.
data [_required_]
[object]
An array of user defined fields.
id [_required_]
string
A unique identifier that represents the responder.
type [_required_]
enum
The incident user defined fields type. Allowed enum values: `user_defined_field`
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
total [_required_]
int32
Number of incidents returned by the search.
type
enum
Incident search result type. Allowed enum values: `incidents_search_results`
default: `incidents_search_results`
included
[ <oneOf>]
Included related resources that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
uuid
string
UUID of the user.
id
string
ID of the user.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
Option 2
object
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
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
  "data": {
    "attributes": {
      "facets": {
        "commander": [
          {
            "count": 5,
            "email": "datadog.user@example.com",
            "handle": "@datadog.user@example.com",
            "name": "Datadog User",
            "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"
          }
        ],
        "created_by": [
          {
            "count": 5,
            "email": "datadog.user@example.com",
            "handle": "@datadog.user@example.com",
            "name": "Datadog User",
            "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"
          }
        ],
        "fields": [
          {
            "aggregates": {
              "max": 1234,
              "min": 20
            },
            "facets": [
              {
                "count": 5,
                "name": "SEV-2"
              }
            ],
            "name": "Severity"
          }
        ],
        "impact": [
          {
            "count": 5,
            "name": "SEV-2"
          }
        ],
        "last_modified_by": [
          {
            "count": 5,
            "email": "datadog.user@example.com",
            "handle": "@datadog.user@example.com",
            "name": "Datadog User",
            "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"
          }
        ],
        "postmortem": [
          {
            "count": 5,
            "name": "SEV-2"
          }
        ],
        "responder": [
          {
            "count": 5,
            "email": "datadog.user@example.com",
            "handle": "@datadog.user@example.com",
            "name": "Datadog User",
            "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"
          }
        ],
        "severity": [
          {
            "count": 5,
            "name": "SEV-2"
          }
        ],
        "state": [
          {
            "count": 5,
            "name": "SEV-2"
          }
        ],
        "time_to_repair": [
          {
            "aggregates": {
              "max": 1234,
              "min": 20
            },
            "name": "time_to_repair"
          }
        ],
        "time_to_resolve": [
          {
            "aggregates": {
              "max": 1234,
              "min": 20
            },
            "name": "time_to_repair"
          }
        ]
      },
      "incidents": [
        {
          "data": {
            "attributes": {
              "archived": "2019-09-19T10:00:00.000Z",
              "case_id": "integer",
              "created": "2019-09-19T10:00:00.000Z",
              "customer_impact_duration": "integer",
              "customer_impact_end": "2019-09-19T10:00:00.000Z",
              "customer_impact_scope": "An example customer impact scope",
              "customer_impact_start": "2019-09-19T10:00:00.000Z",
              "customer_impacted": false,
              "declared": "2019-09-19T10:00:00.000Z",
              "declared_by": {
                "image_48_px": "string",
                "name": "string"
              },
              "declared_by_uuid": "string",
              "detected": "2019-09-19T10:00:00.000Z",
              "fields": {
                "<any-key>": "undefined"
              },
              "incident_type_uuid": "00000000-0000-0000-0000-000000000000",
              "is_test": false,
              "modified": "2019-09-19T10:00:00.000Z",
              "non_datadog_creator": {
                "image_48_px": "string",
                "name": "string"
              },
              "notification_handles": [
                {
                  "display_name": "Jane Doe",
                  "handle": "@test.user@test.com"
                }
              ],
              "public_id": 1,
              "resolved": "2019-09-19T10:00:00.000Z",
              "severity": "UNKNOWN",
              "state": "string",
              "time_to_detect": "integer",
              "time_to_internal_response": "integer",
              "time_to_repair": "integer",
              "time_to_resolve": "integer",
              "title": "A test incident title",
              "visibility": "string"
            },
            "id": "00000000-0000-0000-1234-000000000000",
            "relationships": {
              "attachments": {
                "data": [
                  {
                    "id": "00000000-0000-abcd-1000-000000000000",
                    "type": "incident_attachments"
                  }
                ]
              },
              "commander_user": {
                "data": {
                  "id": "00000000-0000-0000-0000-000000000000",
                  "type": "users"
                }
              },
              "created_by_user": {
                "data": {
                  "id": "00000000-0000-0000-2345-000000000000",
                  "type": "users"
                }
              },
              "declared_by_user": {
                "data": {
                  "id": "00000000-0000-0000-2345-000000000000",
                  "type": "users"
                }
              },
              "impacts": {
                "data": [
                  {
                    "id": "00000000-0000-0000-2345-000000000000",
                    "type": "incident_impacts"
                  }
                ]
              },
              "integrations": {
                "data": [
                  {
                    "id": "00000000-abcd-0001-0000-000000000000",
                    "type": "incident_integrations"
                  }
                ]
              },
              "last_modified_by_user": {
                "data": {
                  "id": "00000000-0000-0000-2345-000000000000",
                  "type": "users"
                }
              },
              "responders": {
                "data": [
                  {
                    "id": "00000000-0000-0000-2345-000000000000",
                    "type": "incident_responders"
                  }
                ]
              },
              "user_defined_fields": {
                "data": [
                  {
                    "id": "00000000-0000-0000-2345-000000000000",
                    "type": "user_defined_field"
                  }
                ]
              }
            },
            "type": "incidents"
          }
        }
      ],
      "total": 10
    },
    "type": "incidents_search_results"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Search for incidents
Copy
```
                  # Required query arguments  
export query="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/search?query=${query}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Search for incidents
```
"""
Search for incidents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["search_incidents"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.search_incidents(
        query="state:(active OR stable OR resolved)",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search for incidents
```
# Search for incidents returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.search_incidents".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.search_incidents("state:(active OR stable OR resolved)")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search for incidents
```
// Search for incidents returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.SearchIncidents", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.SearchIncidents(ctx, "state:(active OR stable OR resolved)", *datadogV2.NewSearchIncidentsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.SearchIncidents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.SearchIncidents`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Search for incidents
```
// Search for incidents returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentSearchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.searchIncidents", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentSearchResponse result =
          apiInstance.searchIncidents("state:(active OR stable OR resolved)");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#searchIncidents");
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

#####  Search for incidents
```
// Search for incidents returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::SearchIncidentsOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.SearchIncidents", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .search_incidents(
            "state:(active OR stable OR resolved)".to_string(),
            SearchIncidentsOptionalParams::default(),
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

#####  Search for incidents
```
/**
 * Search for incidents returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.searchIncidents"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

const params: v2.IncidentsApiSearchIncidentsRequest = {
  query: "state:(active OR stable OR resolved)",
};

apiInstance
  .searchIncidents(params)
  .then((data: v2.IncidentSearchResponse) => {
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
## [List an incident's impacts](https://docs.datadoghq.com/api/latest/incidents/#list-an-incidents-impacts)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#list-an-incidents-impacts-v2)


GET https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/impactshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/impactshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/impacts
### Overview
Get all impacts for an incident. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
#### Query Strings
Name
Type
Description
include
array
Specifies which related resources should be included in the response.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentImpacts-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentImpacts-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentImpacts-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentImpacts-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentImpacts-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentImpacts-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a list of incident impacts.
Field
Type
Description
data [_required_]
[object]
An array of incident impacts.
attributes
object
The incident impact's attributes.
created
date-time
Timestamp when the impact was created.
description [_required_]
string
Description of the impact.
end_at
date-time
Timestamp when the impact ended.
fields
object
An object mapping impact field names to field values.
impact_type
string
The type of impact.
modified
date-time
Timestamp when the impact was last modified.
start_at [_required_]
date-time
Timestamp representing when the impact started.
id [_required_]
string
The incident impact's ID.
relationships
object
The incident impact's resource relationships.
created_by_user
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
incident
object
Relationship to incident.
data [_required_]
object
Relationship to incident object.
id [_required_]
string
A unique identifier that represents the incident.
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
last_modified_by_user
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
Incident impact resource type. Allowed enum values: `incident_impacts`
default: `incident_impacts`
included
[object]
Included related resources that the user requested.
attributes
object
Attributes of user object returned by the API.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
uuid
string
UUID of the user.
id
string
ID of the user.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": [
    {
      "attributes": {
        "created": "2025-08-29T13:17:00Z",
        "description": "Service was unavailable for external users",
        "end_at": "2025-08-29T13:17:00Z",
        "fields": {
          "customers_impacted": "all",
          "products_impacted": [
            "shopping",
            "marketing"
          ]
        },
        "impact_type": "customer",
        "modified": "2025-08-29T13:17:00Z",
        "start_at": "2025-08-28T13:17:00Z"
      },
      "id": "00000000-0000-0000-1234-000000000000",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "incident": {
          "data": {
            "id": "00000000-0000-0000-1234-000000000000",
            "type": "incidents"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "incident_impacts"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  List an incident's impacts
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/impacts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List an incident's impacts
```
"""
List an incident's impacts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_incident_impacts"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_impacts(
        incident_id=INCIDENT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List an incident's impacts
```
# List an incident's impacts returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_impacts".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]
p api_instance.list_incident_impacts(INCIDENT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List an incident's impacts
```
// List an incident's impacts returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ListIncidentImpacts", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidentImpacts(ctx, IncidentDataID, *datadogV2.NewListIncidentImpactsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidentImpacts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidentImpacts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List an incident's impacts
```
// List an incident's impacts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentImpactsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentImpacts", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    try {
      IncidentImpactsResponse result = apiInstance.listIncidentImpacts(INCIDENT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidentImpacts");
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

#####  List an incident's impacts
```
// List an incident's impacts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::ListIncidentImpactsOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentImpacts", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .list_incident_impacts(
            incident_data_id.clone(),
            ListIncidentImpactsOptionalParams::default(),
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

#####  List an incident's impacts
```
/**
 * List an incident's impacts returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentImpacts"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiListIncidentImpactsRequest = {
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .listIncidentImpacts(params)
  .then((data: v2.IncidentImpactsResponse) => {
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
## [Create an incident impact](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-impact)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-impact-v2)


POST https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/impactshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/impactshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/impactshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/impacts
### Overview
Create an impact for an incident. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
#### Query Strings
Name
Type
Description
include
array
Specifies which related resources should be included in the response.
### Request
#### Body Data (required)
Incident impact payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident impact data for a create request.
attributes [_required_]
object
The incident impact's attributes for a create request.
description [_required_]
string
Description of the impact.
end_at
date-time
Timestamp when the impact ended.
fields
object
An object mapping impact field names to field values.
start_at [_required_]
date-time
Timestamp when the impact started.
type [_required_]
enum
Incident impact resource type. Allowed enum values: `incident_impacts`
default: `incident_impacts`
```
{
  "data": {
    "attributes": {
      "description": "Service was unavailable for external users",
      "end_at": "2025-08-29T13:17:00Z",
      "fields": {
        "customers_impacted": "all",
        "products_impacted": [
          "shopping",
          "marketing"
        ]
      },
      "start_at": "2025-08-28T13:17:00Z"
    },
    "type": "incident_impacts"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentImpact-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentImpact-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentImpact-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentImpact-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentImpact-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentImpact-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident impact.
Field
Type
Description
data [_required_]
object
Incident impact data from a response.
attributes
object
The incident impact's attributes.
created
date-time
Timestamp when the impact was created.
description [_required_]
string
Description of the impact.
end_at
date-time
Timestamp when the impact ended.
fields
object
An object mapping impact field names to field values.
impact_type
string
The type of impact.
modified
date-time
Timestamp when the impact was last modified.
start_at [_required_]
date-time
Timestamp representing when the impact started.
id [_required_]
string
The incident impact's ID.
relationships
object
The incident impact's resource relationships.
created_by_user
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
incident
object
Relationship to incident.
data [_required_]
object
Relationship to incident object.
id [_required_]
string
A unique identifier that represents the incident.
type [_required_]
enum
Incident resource type. Allowed enum values: `incidents`
default: `incidents`
last_modified_by_user
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
Incident impact resource type. Allowed enum values: `incident_impacts`
default: `incident_impacts`
included
[object]
Included related resources that the user requested.
attributes
object
Attributes of user object returned by the API.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
uuid
string
UUID of the user.
id
string
ID of the user.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "created": "2025-08-29T13:17:00Z",
      "description": "Service was unavailable for external users",
      "end_at": "2025-08-29T13:17:00Z",
      "fields": {
        "customers_impacted": "all",
        "products_impacted": [
          "shopping",
          "marketing"
        ]
      },
      "impact_type": "customer",
      "modified": "2025-08-29T13:17:00Z",
      "start_at": "2025-08-28T13:17:00Z"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "incident": {
        "data": {
          "id": "00000000-0000-0000-1234-000000000000",
          "type": "incidents"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "incident_impacts"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Create an incident impact
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/impacts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Service was unavailable for external users",
      "start_at": "2025-08-28T13:17:00Z"
    },
    "type": "incident_impacts"
  }
}
EOF  

                
```

#####  Create an incident impact
```
"""
Create an incident impact returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_impact_create_attributes import IncidentImpactCreateAttributes
from datadog_api_client.v2.model.incident_impact_create_data import IncidentImpactCreateData
from datadog_api_client.v2.model.incident_impact_create_request import IncidentImpactCreateRequest
from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType
from datetime import datetime
from dateutil.tz import tzutc

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentImpactCreateRequest(
    data=IncidentImpactCreateData(
        type=IncidentImpactType.INCIDENT_IMPACTS,
        attributes=IncidentImpactCreateAttributes(
            start_at=datetime(2025, 9, 12, 13, 50, tzinfo=tzutc()),
            end_at=datetime(2025, 9, 12, 14, 50, tzinfo=tzutc()),
            description="Outage in the us-east-1 region",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_impact"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_impact(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an incident impact
```
# Create an incident impact returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_impact".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

body = DatadogAPIClient::V2::IncidentImpactCreateRequest.new({
  data: DatadogAPIClient::V2::IncidentImpactCreateData.new({
    type: DatadogAPIClient::V2::IncidentImpactType::INCIDENT_IMPACTS,
    attributes: DatadogAPIClient::V2::IncidentImpactCreateAttributes.new({
      start_at: "2025-09-12T13:50:00.000Z",
      end_at: "2025-09-12T14:50:00.000Z",
      description: "Outage in the us-east-1 region",
    }),
  }),
})
p api_instance.create_incident_impact(INCIDENT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create an incident impact
```
// Create an incident impact returns "CREATED" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	body := datadogV2.IncidentImpactCreateRequest{
		Data: datadogV2.IncidentImpactCreateData{
			Type: datadogV2.INCIDENTIMPACTTYPE_INCIDENT_IMPACTS,
			Attributes: datadogV2.IncidentImpactCreateAttributes{
				StartAt:     time.Date(2025, 9, 12, 13, 50, 0, 0, time.UTC),
				EndAt:       *datadog.NewNullableTime(datadog.PtrTime(time.Date(2025, 9, 12, 14, 50, 0, 0, time.UTC))),
				Description: "Outage in the us-east-1 region",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncidentImpact", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.CreateIncidentImpact(ctx, IncidentDataID, body, *datadogV2.NewCreateIncidentImpactOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.CreateIncidentImpact`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.CreateIncidentImpact`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create an incident impact
```
// Create an incident impact returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentImpactCreateAttributes;
import com.datadog.api.client.v2.model.IncidentImpactCreateData;
import com.datadog.api.client.v2.model.IncidentImpactCreateRequest;
import com.datadog.api.client.v2.model.IncidentImpactResponse;
import com.datadog.api.client.v2.model.IncidentImpactType;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentImpact", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    IncidentImpactCreateRequest body =
        new IncidentImpactCreateRequest()
            .data(
                new IncidentImpactCreateData()
                    .type(IncidentImpactType.INCIDENT_IMPACTS)
                    .attributes(
                        new IncidentImpactCreateAttributes()
                            .startAt(OffsetDateTime.parse("2025-09-12T13:50:00.000Z"))
                            .endAt(OffsetDateTime.parse("2025-09-12T14:50:00.000Z"))
                            .description("Outage in the us-east-1 region")));

    try {
      IncidentImpactResponse result = apiInstance.createIncidentImpact(INCIDENT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#createIncidentImpact");
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

#####  Create an incident impact
```
// Create an incident impact returns "CREATED" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::CreateIncidentImpactOptionalParams;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentImpactCreateAttributes;
use datadog_api_client::datadogV2::model::IncidentImpactCreateData;
use datadog_api_client::datadogV2::model::IncidentImpactCreateRequest;
use datadog_api_client::datadogV2::model::IncidentImpactType;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let body = IncidentImpactCreateRequest::new(IncidentImpactCreateData::new(
        IncidentImpactCreateAttributes::new(
            "Outage in the us-east-1 region".to_string(),
            DateTime::parse_from_rfc3339("2025-09-12T13:50:00+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
        )
        .end_at(Some(
            DateTime::parse_from_rfc3339("2025-09-12T14:50:00+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
        )),
        IncidentImpactType::INCIDENT_IMPACTS,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentImpact", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .create_incident_impact(
            incident_data_id.clone(),
            body,
            CreateIncidentImpactOptionalParams::default(),
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

#####  Create an incident impact
```
/**
 * Create an incident impact returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentImpact"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiCreateIncidentImpactRequest = {
  body: {
    data: {
      type: "incident_impacts",
      attributes: {
        startAt: new Date(2025, 9, 12, 13, 50, 0, 0),
        endAt: new Date(2025, 9, 12, 14, 50, 0, 0),
        description: "Outage in the us-east-1 region",
      },
    },
  },
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .createIncidentImpact(params)
  .then((data: v2.IncidentImpactResponse) => {
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
## [Delete an incident impact](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-impact)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-impact-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/impacts/{impact_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/impacts/{impact_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/impacts/{impact_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/impacts/{impact_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/impacts/{impact_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/impacts/{impact_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/impacts/{impact_id}
### Overview
Delete an incident impact. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
impact_id [_required_]
string
The UUID of the incident impact.
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentImpact-204-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentImpact-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentImpact-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentImpact-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentImpact-429-v2)


No Content
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Delete an incident impact
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
export impact_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/impacts/${impact_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an incident impact
```
"""
Delete an incident impact returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# the "incident" has an "incident_impact"
INCIDENT_IMPACT_DATA_ID = environ["INCIDENT_IMPACT_DATA_ID"]
INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID = environ["INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_impact"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_impact(
        incident_id=INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID,
        impact_id=INCIDENT_IMPACT_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an incident impact
```
# Delete an incident impact returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_impact".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# the "incident" has an "incident_impact"
INCIDENT_IMPACT_DATA_ID = ENV["INCIDENT_IMPACT_DATA_ID"]
INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID = ENV["INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID"]
api_instance.delete_incident_impact(INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID, INCIDENT_IMPACT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an incident impact
```
// Delete an incident impact returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// the "incident" has an "incident_impact"
	IncidentImpactDataID := os.Getenv("INCIDENT_IMPACT_DATA_ID")
	IncidentImpactDataRelationshipsIncidentDataID := os.Getenv("INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncidentImpact", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	r, err := api.DeleteIncidentImpact(ctx, IncidentImpactDataRelationshipsIncidentDataID, IncidentImpactDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.DeleteIncidentImpact`: %v\n", err)
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

#####  Delete an incident impact
```
// Delete an incident impact returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentImpact", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // the "incident" has an "incident_impact"
    String INCIDENT_IMPACT_DATA_ID = System.getenv("INCIDENT_IMPACT_DATA_ID");
    String INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID =
        System.getenv("INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID");

    try {
      apiInstance.deleteIncidentImpact(
          INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID, INCIDENT_IMPACT_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#deleteIncidentImpact");
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

#####  Delete an incident impact
```
// Delete an incident impact returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // the "incident" has an "incident_impact"
    let incident_impact_data_id = std::env::var("INCIDENT_IMPACT_DATA_ID").unwrap();
    let incident_impact_data_relationships_incident_data_id =
        std::env::var("INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentImpact", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .delete_incident_impact(
            incident_impact_data_relationships_incident_data_id.clone(),
            incident_impact_data_id.clone(),
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

#####  Delete an incident impact
```
/**
 * Delete an incident impact returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentImpact"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// the "incident" has an "incident_impact"
const INCIDENT_IMPACT_DATA_ID = process.env.INCIDENT_IMPACT_DATA_ID as string;
const INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID = process.env
  .INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiDeleteIncidentImpactRequest = {
  incidentId: INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID,
  impactId: INCIDENT_IMPACT_DATA_ID,
};

apiInstance
  .deleteIncidentImpact(params)
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
## [Get a list of an incident's integration metadata](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-an-incidents-integration-metadata)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-an-incidents-integration-metadata-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations
### Overview
Get all integration metadata for an incident. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentIntegrations-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentIntegrations-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentIntegrations-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentIntegrations-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentIntegrations-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentIntegrations-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a list of incident integration metadata.
Field
Type
Description
data [_required_]
[object]
An array of incident integration metadata.
attributes
object
Incident integration metadata's attributes for a create request.
created
date-time
Timestamp when the incident todo was created.
incident_id
string
UUID of the incident this integration metadata is connected to.
integration_type [_required_]
int32
A number indicating the type of integration this metadata is for. 1 indicates Slack; 8 indicates Jira.
metadata [_required_]
<oneOf>
Incident integration metadata's metadata attribute.
Option 1
object
Incident integration metadata for the Slack integration.
channels [_required_]
[object]
Array of Slack channels in this integration metadata.
channel_id [_required_]
string
Slack channel ID.
channel_name [_required_]
string
Name of the Slack channel.
redirect_url [_required_]
string
URL redirecting to the Slack channel.
team_id
string
Slack team ID.
Option 2
object
Incident integration metadata for the Jira integration.
issues [_required_]
[object]
Array of Jira issues in this integration metadata.
account [_required_]
string
URL of issue's Jira account.
issue_key
string
Jira issue's issue key.
issuetype_id
string
Jira issue's issue type.
project_key [_required_]
string
Jira issue's project keys.
redirect_url
string
URL redirecting to the Jira issue.
Option 3
object
Incident integration metadata for the Microsoft Teams integration.
teams [_required_]
[object]
Array of Microsoft Teams in this integration metadata.
ms_channel_id [_required_]
string
Microsoft Teams channel ID.
ms_channel_name [_required_]
string
Microsoft Teams channel name.
ms_tenant_id [_required_]
string
Microsoft Teams tenant ID.
redirect_url [_required_]
string
URL redirecting to the Microsoft Teams channel.
modified
date-time
Timestamp when the incident todo was last modified.
status
int32
A number indicating the status of this integration metadata. 0 indicates unknown; 1 indicates pending; 2 indicates complete; 3 indicates manually created; 4 indicates manually updated; 5 indicates failed.
id [_required_]
string
The incident integration metadata's ID.
relationships
object
The incident's integration relationships from a response.
created_by_user
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
last_modified_by_user
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
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
included
[ <oneOf>]
Included related resources that the user requested.
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
        "incident_id": "00000000-aaaa-0000-0000-000000000000",
        "integration_type": 1,
        "metadata": {
          "channels": [
            {
              "channel_id": "C0123456789",
              "channel_name": "#example-channel-name",
              "redirect_url": "https://slack.com/app_redirect?channel=C0123456789\u0026team=T01234567",
              "team_id": "T01234567"
            }
          ]
        },
        "modified": "2019-09-19T10:00:00.000Z",
        "status": "integer"
      },
      "id": "00000000-0000-0000-1234-000000000000",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "incident_integrations"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get a list of an incident's integration metadata
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/integrations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of an incident's integration metadata
```
"""
Get a list of an incident's integration metadata returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_incident_integrations"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_integrations(
        incident_id=INCIDENT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of an incident's integration metadata
```
# Get a list of an incident's integration metadata returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_integrations".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]
p api_instance.list_incident_integrations(INCIDENT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of an incident's integration metadata
```
// Get a list of an incident's integration metadata returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ListIncidentIntegrations", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidentIntegrations(ctx, IncidentDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidentIntegrations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidentIntegrations`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of an incident's integration metadata
```
// Get a list of an incident's integration metadata returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentIntegrations", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    try {
      IncidentIntegrationMetadataListResponse result =
          apiInstance.listIncidentIntegrations(INCIDENT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidentIntegrations");
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

#####  Get a list of an incident's integration metadata
```
// Get a list of an incident's integration metadata returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentIntegrations", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .list_incident_integrations(incident_data_id.clone())
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

#####  Get a list of an incident's integration metadata
```
/**
 * Get a list of an incident's integration metadata returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentIntegrations"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiListIncidentIntegrationsRequest = {
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .listIncidentIntegrations(params)
  .then((data: v2.IncidentIntegrationMetadataListResponse) => {
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
## [Create an incident integration metadata](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-integration-metadata)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-integration-metadata-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrationshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations
### Overview
Create an incident integration metadata. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
### Request
#### Body Data (required)
Incident integration metadata payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident integration metadata data for a create request.
attributes [_required_]
object
Incident integration metadata's attributes for a create request.
created
date-time
Timestamp when the incident todo was created.
incident_id
string
UUID of the incident this integration metadata is connected to.
integration_type [_required_]
int32
A number indicating the type of integration this metadata is for. 1 indicates Slack; 8 indicates Jira.
metadata [_required_]
<oneOf>
Incident integration metadata's metadata attribute.
Option 1
object
Incident integration metadata for the Slack integration.
channels [_required_]
[object]
Array of Slack channels in this integration metadata.
channel_id [_required_]
string
Slack channel ID.
channel_name [_required_]
string
Name of the Slack channel.
redirect_url [_required_]
string
URL redirecting to the Slack channel.
team_id
string
Slack team ID.
Option 2
object
Incident integration metadata for the Jira integration.
issues [_required_]
[object]
Array of Jira issues in this integration metadata.
account [_required_]
string
URL of issue's Jira account.
issue_key
string
Jira issue's issue key.
issuetype_id
string
Jira issue's issue type.
project_key [_required_]
string
Jira issue's project keys.
redirect_url
string
URL redirecting to the Jira issue.
Option 3
object
Incident integration metadata for the Microsoft Teams integration.
teams [_required_]
[object]
Array of Microsoft Teams in this integration metadata.
ms_channel_id [_required_]
string
Microsoft Teams channel ID.
ms_channel_name [_required_]
string
Microsoft Teams channel name.
ms_tenant_id [_required_]
string
Microsoft Teams tenant ID.
redirect_url [_required_]
string
URL redirecting to the Microsoft Teams channel.
modified
date-time
Timestamp when the incident todo was last modified.
status
int32
A number indicating the status of this integration metadata. 0 indicates unknown; 1 indicates pending; 2 indicates complete; 3 indicates manually created; 4 indicates manually updated; 5 indicates failed.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
```
{
  "data": {
    "attributes": {
      "incident_id": "00000000-0000-0000-1234-000000000000",
      "integration_type": 1,
      "metadata": {
        "channels": [
          {
            "channel_id": "C0123456789",
            "channel_name": "#new-channel",
            "team_id": "T01234567",
            "redirect_url": "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"
          }
        ]
      }
    },
    "type": "incident_integrations"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentIntegration-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentIntegration-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentIntegration-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentIntegration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentIntegration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentIntegration-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident integration metadata.
Field
Type
Description
data [_required_]
object
Incident integration metadata from a response.
attributes
object
Incident integration metadata's attributes for a create request.
created
date-time
Timestamp when the incident todo was created.
incident_id
string
UUID of the incident this integration metadata is connected to.
integration_type [_required_]
int32
A number indicating the type of integration this metadata is for. 1 indicates Slack; 8 indicates Jira.
metadata [_required_]
<oneOf>
Incident integration metadata's metadata attribute.
Option 1
object
Incident integration metadata for the Slack integration.
channels [_required_]
[object]
Array of Slack channels in this integration metadata.
channel_id [_required_]
string
Slack channel ID.
channel_name [_required_]
string
Name of the Slack channel.
redirect_url [_required_]
string
URL redirecting to the Slack channel.
team_id
string
Slack team ID.
Option 2
object
Incident integration metadata for the Jira integration.
issues [_required_]
[object]
Array of Jira issues in this integration metadata.
account [_required_]
string
URL of issue's Jira account.
issue_key
string
Jira issue's issue key.
issuetype_id
string
Jira issue's issue type.
project_key [_required_]
string
Jira issue's project keys.
redirect_url
string
URL redirecting to the Jira issue.
Option 3
object
Incident integration metadata for the Microsoft Teams integration.
teams [_required_]
[object]
Array of Microsoft Teams in this integration metadata.
ms_channel_id [_required_]
string
Microsoft Teams channel ID.
ms_channel_name [_required_]
string
Microsoft Teams channel name.
ms_tenant_id [_required_]
string
Microsoft Teams tenant ID.
redirect_url [_required_]
string
URL redirecting to the Microsoft Teams channel.
modified
date-time
Timestamp when the incident todo was last modified.
status
int32
A number indicating the status of this integration metadata. 0 indicates unknown; 1 indicates pending; 2 indicates complete; 3 indicates manually created; 4 indicates manually updated; 5 indicates failed.
id [_required_]
string
The incident integration metadata's ID.
relationships
object
The incident's integration relationships from a response.
created_by_user
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
last_modified_by_user
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
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
included
[ <oneOf>]
Included related resources that the user requested.
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
      "incident_id": "00000000-aaaa-0000-0000-000000000000",
      "integration_type": 1,
      "metadata": {
        "channels": [
          {
            "channel_id": "C0123456789",
            "channel_name": "#example-channel-name",
            "redirect_url": "https://slack.com/app_redirect?channel=C0123456789\u0026team=T01234567",
            "team_id": "T01234567"
          }
        ]
      },
      "modified": "2019-09-19T10:00:00.000Z",
      "status": "integer"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "incident_integrations"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Create an incident integration metadata returns "CREATED" response
Copy
```
                          # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/integrations" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "incident_id": "00000000-0000-0000-1234-000000000000",
      "integration_type": 1,
      "metadata": {
        "channels": [
          {
            "channel_id": "C0123456789",
            "channel_name": "#new-channel",
            "team_id": "T01234567",
            "redirect_url": "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"
          }
        ]
      }
    },
    "type": "incident_integrations"
  }
}
EOF  

                        
```

#####  Create an incident integration metadata returns "CREATED" response
```
// Create an incident integration metadata returns "CREATED" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	body := datadogV2.IncidentIntegrationMetadataCreateRequest{
		Data: datadogV2.IncidentIntegrationMetadataCreateData{
			Attributes: datadogV2.IncidentIntegrationMetadataAttributes{
				IncidentId:      datadog.PtrString(IncidentDataID),
				IntegrationType: 1,
				Metadata: datadogV2.IncidentIntegrationMetadataMetadata{
					SlackIntegrationMetadata: &datadogV2.SlackIntegrationMetadata{
						Channels: []datadogV2.SlackIntegrationMetadataChannelItem{
							{
								ChannelId:   "C0123456789",
								ChannelName: "#new-channel",
								TeamId:      datadog.PtrString("T01234567"),
								RedirectUrl: "https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
							},
						},
					}},
			},
			Type: datadogV2.INCIDENTINTEGRATIONMETADATATYPE_INCIDENT_INTEGRATIONS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncidentIntegration", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.CreateIncidentIntegration(ctx, IncidentDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.CreateIncidentIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.CreateIncidentIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create an incident integration metadata returns "CREATED" response
```
// Create an incident integration metadata returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataAttributes;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataCreateData;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataCreateRequest;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataMetadata;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataResponse;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataType;
import com.datadog.api.client.v2.model.SlackIntegrationMetadata;
import com.datadog.api.client.v2.model.SlackIntegrationMetadataChannelItem;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentIntegration", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    IncidentIntegrationMetadataCreateRequest body =
        new IncidentIntegrationMetadataCreateRequest()
            .data(
                new IncidentIntegrationMetadataCreateData()
                    .attributes(
                        new IncidentIntegrationMetadataAttributes()
                            .incidentId(INCIDENT_DATA_ID)
                            .integrationType(1)
                            .metadata(
                                new IncidentIntegrationMetadataMetadata(
                                    new SlackIntegrationMetadata()
                                        .channels(
                                            Collections.singletonList(
                                                new SlackIntegrationMetadataChannelItem()
                                                    .channelId("C0123456789")
                                                    .channelName("#new-channel")
                                                    .teamId("T01234567")
                                                    .redirectUrl(
                                                        "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"))))))
                    .type(IncidentIntegrationMetadataType.INCIDENT_INTEGRATIONS));

    try {
      IncidentIntegrationMetadataResponse result =
          apiInstance.createIncidentIntegration(INCIDENT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#createIncidentIntegration");
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

#####  Create an incident integration metadata returns "CREATED" response
```
"""
Create an incident integration metadata returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_integration_metadata_attributes import IncidentIntegrationMetadataAttributes
from datadog_api_client.v2.model.incident_integration_metadata_create_data import IncidentIntegrationMetadataCreateData
from datadog_api_client.v2.model.incident_integration_metadata_create_request import (
    IncidentIntegrationMetadataCreateRequest,
)
from datadog_api_client.v2.model.incident_integration_metadata_type import IncidentIntegrationMetadataType
from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
from datadog_api_client.v2.model.slack_integration_metadata_channel_item import SlackIntegrationMetadataChannelItem

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentIntegrationMetadataCreateRequest(
    data=IncidentIntegrationMetadataCreateData(
        attributes=IncidentIntegrationMetadataAttributes(
            incident_id=INCIDENT_DATA_ID,
            integration_type=1,
            metadata=SlackIntegrationMetadata(
                channels=[
                    SlackIntegrationMetadataChannelItem(
                        channel_id="C0123456789",
                        channel_name="#new-channel",
                        team_id="T01234567",
                        redirect_url="https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
                    ),
                ],
            ),
        ),
        type=IncidentIntegrationMetadataType.INCIDENT_INTEGRATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_integration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_integration(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an incident integration metadata returns "CREATED" response
```
# Create an incident integration metadata returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_integration".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

body = DatadogAPIClient::V2::IncidentIntegrationMetadataCreateRequest.new({
  data: DatadogAPIClient::V2::IncidentIntegrationMetadataCreateData.new({
    attributes: DatadogAPIClient::V2::IncidentIntegrationMetadataAttributes.new({
      incident_id: INCIDENT_DATA_ID,
      integration_type: 1,
      metadata: DatadogAPIClient::V2::SlackIntegrationMetadata.new({
        channels: [
          DatadogAPIClient::V2::SlackIntegrationMetadataChannelItem.new({
            channel_id: "C0123456789",
            channel_name: "#new-channel",
            team_id: "T01234567",
            redirect_url: "https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::IncidentIntegrationMetadataType::INCIDENT_INTEGRATIONS,
  }),
})
p api_instance.create_incident_integration(INCIDENT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create an incident integration metadata returns "CREATED" response
```
// Create an incident integration metadata returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataAttributes;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataCreateData;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataCreateRequest;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataMetadata;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataType;
use datadog_api_client::datadogV2::model::SlackIntegrationMetadata;
use datadog_api_client::datadogV2::model::SlackIntegrationMetadataChannelItem;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let body =
        IncidentIntegrationMetadataCreateRequest::new(IncidentIntegrationMetadataCreateData::new(
            IncidentIntegrationMetadataAttributes::new(
                1,
                IncidentIntegrationMetadataMetadata::SlackIntegrationMetadata(Box::new(
                    SlackIntegrationMetadata::new(vec![SlackIntegrationMetadataChannelItem::new(
                        "C0123456789".to_string(),
                        "#new-channel".to_string(),
                        "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"
                            .to_string(),
                    )
                    .team_id("T01234567".to_string())]),
                )),
            )
            .incident_id(incident_data_id.clone()),
            IncidentIntegrationMetadataType::INCIDENT_INTEGRATIONS,
        ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentIntegration", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .create_incident_integration(incident_data_id.clone(), body)
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

#####  Create an incident integration metadata returns "CREATED" response
```
/**
 * Create an incident integration metadata returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentIntegration"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiCreateIncidentIntegrationRequest = {
  body: {
    data: {
      attributes: {
        incidentId: INCIDENT_DATA_ID,
        integrationType: 1,
        metadata: {
          channels: [
            {
              channelId: "C0123456789",
              channelName: "#new-channel",
              teamId: "T01234567",
              redirectUrl:
                "https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
            },
          ],
        },
      },
      type: "incident_integrations",
    },
  },
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .createIncidentIntegration(params)
  .then((data: v2.IncidentIntegrationMetadataResponse) => {
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
## [Get incident integration metadata details](https://docs.datadoghq.com/api/latest/incidents/#get-incident-integration-metadata-details)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-incident-integration-metadata-details-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}
### Overview
Get incident integration metadata details.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
integration_metadata_id [_required_]
string
The UUID of the incident integration metadata.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentIntegration-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentIntegration-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentIntegration-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentIntegration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentIntegration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentIntegration-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident integration metadata.
Field
Type
Description
data [_required_]
object
Incident integration metadata from a response.
attributes
object
Incident integration metadata's attributes for a create request.
created
date-time
Timestamp when the incident todo was created.
incident_id
string
UUID of the incident this integration metadata is connected to.
integration_type [_required_]
int32
A number indicating the type of integration this metadata is for. 1 indicates Slack; 8 indicates Jira.
metadata [_required_]
<oneOf>
Incident integration metadata's metadata attribute.
Option 1
object
Incident integration metadata for the Slack integration.
channels [_required_]
[object]
Array of Slack channels in this integration metadata.
channel_id [_required_]
string
Slack channel ID.
channel_name [_required_]
string
Name of the Slack channel.
redirect_url [_required_]
string
URL redirecting to the Slack channel.
team_id
string
Slack team ID.
Option 2
object
Incident integration metadata for the Jira integration.
issues [_required_]
[object]
Array of Jira issues in this integration metadata.
account [_required_]
string
URL of issue's Jira account.
issue_key
string
Jira issue's issue key.
issuetype_id
string
Jira issue's issue type.
project_key [_required_]
string
Jira issue's project keys.
redirect_url
string
URL redirecting to the Jira issue.
Option 3
object
Incident integration metadata for the Microsoft Teams integration.
teams [_required_]
[object]
Array of Microsoft Teams in this integration metadata.
ms_channel_id [_required_]
string
Microsoft Teams channel ID.
ms_channel_name [_required_]
string
Microsoft Teams channel name.
ms_tenant_id [_required_]
string
Microsoft Teams tenant ID.
redirect_url [_required_]
string
URL redirecting to the Microsoft Teams channel.
modified
date-time
Timestamp when the incident todo was last modified.
status
int32
A number indicating the status of this integration metadata. 0 indicates unknown; 1 indicates pending; 2 indicates complete; 3 indicates manually created; 4 indicates manually updated; 5 indicates failed.
id [_required_]
string
The incident integration metadata's ID.
relationships
object
The incident's integration relationships from a response.
created_by_user
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
last_modified_by_user
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
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
included
[ <oneOf>]
Included related resources that the user requested.
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
      "incident_id": "00000000-aaaa-0000-0000-000000000000",
      "integration_type": 1,
      "metadata": {
        "channels": [
          {
            "channel_id": "C0123456789",
            "channel_name": "#example-channel-name",
            "redirect_url": "https://slack.com/app_redirect?channel=C0123456789\u0026team=T01234567",
            "team_id": "T01234567"
          }
        ]
      },
      "modified": "2019-09-19T10:00:00.000Z",
      "status": "integer"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "incident_integrations"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get incident integration metadata details
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
export integration_metadata_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/integrations/${integration_metadata_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get incident integration metadata details
```
"""
Get incident integration metadata details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_integration_metadata"
INCIDENT_INTEGRATION_METADATA_DATA_ID = environ["INCIDENT_INTEGRATION_METADATA_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident_integration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_integration(
        incident_id=INCIDENT_DATA_ID,
        integration_metadata_id=INCIDENT_INTEGRATION_METADATA_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get incident integration metadata details
```
# Get incident integration metadata details returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident_integration".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

# the "incident" has an "incident_integration_metadata"
INCIDENT_INTEGRATION_METADATA_DATA_ID = ENV["INCIDENT_INTEGRATION_METADATA_DATA_ID"]
p api_instance.get_incident_integration(INCIDENT_DATA_ID, INCIDENT_INTEGRATION_METADATA_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get incident integration metadata details
```
// Get incident integration metadata details returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	// the "incident" has an "incident_integration_metadata"
	IncidentIntegrationMetadataDataID := os.Getenv("INCIDENT_INTEGRATION_METADATA_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetIncidentIntegration", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.GetIncidentIntegration(ctx, IncidentDataID, IncidentIntegrationMetadataDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.GetIncidentIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.GetIncidentIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get incident integration metadata details
```
// Get incident integration metadata details returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncidentIntegration", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    // the "incident" has an "incident_integration_metadata"
    String INCIDENT_INTEGRATION_METADATA_DATA_ID =
        System.getenv("INCIDENT_INTEGRATION_METADATA_DATA_ID");

    try {
      IncidentIntegrationMetadataResponse result =
          apiInstance.getIncidentIntegration(
              INCIDENT_DATA_ID, INCIDENT_INTEGRATION_METADATA_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getIncidentIntegration");
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

#####  Get incident integration metadata details
```
// Get incident integration metadata details returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();

    // the "incident" has an "incident_integration_metadata"
    let incident_integration_metadata_data_id =
        std::env::var("INCIDENT_INTEGRATION_METADATA_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncidentIntegration", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .get_incident_integration(
            incident_data_id.clone(),
            incident_integration_metadata_data_id.clone(),
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

#####  Get incident integration metadata details
```
/**
 * Get incident integration metadata details returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncidentIntegration"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

// the "incident" has an "incident_integration_metadata"
const INCIDENT_INTEGRATION_METADATA_DATA_ID = process.env
  .INCIDENT_INTEGRATION_METADATA_DATA_ID as string;

const params: v2.IncidentsApiGetIncidentIntegrationRequest = {
  incidentId: INCIDENT_DATA_ID,
  integrationMetadataId: INCIDENT_INTEGRATION_METADATA_DATA_ID,
};

apiInstance
  .getIncidentIntegration(params)
  .then((data: v2.IncidentIntegrationMetadataResponse) => {
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
## [Update an existing incident integration metadata](https://docs.datadoghq.com/api/latest/incidents/#update-an-existing-incident-integration-metadata)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#update-an-existing-incident-integration-metadata-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PATCH https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}
### Overview
Update an existing incident integration metadata.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
integration_metadata_id [_required_]
string
The UUID of the incident integration metadata.
### Request
#### Body Data (required)
Incident integration metadata payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident integration metadata data for a patch request.
attributes [_required_]
object
Incident integration metadata's attributes for a create request.
created
date-time
Timestamp when the incident todo was created.
incident_id
string
UUID of the incident this integration metadata is connected to.
integration_type [_required_]
int32
A number indicating the type of integration this metadata is for. 1 indicates Slack; 8 indicates Jira.
metadata [_required_]
<oneOf>
Incident integration metadata's metadata attribute.
Option 1
object
Incident integration metadata for the Slack integration.
channels [_required_]
[object]
Array of Slack channels in this integration metadata.
channel_id [_required_]
string
Slack channel ID.
channel_name [_required_]
string
Name of the Slack channel.
redirect_url [_required_]
string
URL redirecting to the Slack channel.
team_id
string
Slack team ID.
Option 2
object
Incident integration metadata for the Jira integration.
issues [_required_]
[object]
Array of Jira issues in this integration metadata.
account [_required_]
string
URL of issue's Jira account.
issue_key
string
Jira issue's issue key.
issuetype_id
string
Jira issue's issue type.
project_key [_required_]
string
Jira issue's project keys.
redirect_url
string
URL redirecting to the Jira issue.
Option 3
object
Incident integration metadata for the Microsoft Teams integration.
teams [_required_]
[object]
Array of Microsoft Teams in this integration metadata.
ms_channel_id [_required_]
string
Microsoft Teams channel ID.
ms_channel_name [_required_]
string
Microsoft Teams channel name.
ms_tenant_id [_required_]
string
Microsoft Teams tenant ID.
redirect_url [_required_]
string
URL redirecting to the Microsoft Teams channel.
modified
date-time
Timestamp when the incident todo was last modified.
status
int32
A number indicating the status of this integration metadata. 0 indicates unknown; 1 indicates pending; 2 indicates complete; 3 indicates manually created; 4 indicates manually updated; 5 indicates failed.
type [_required_]
enum
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
```
{
  "data": {
    "attributes": {
      "incident_id": "00000000-0000-0000-1234-000000000000",
      "integration_type": 1,
      "metadata": {
        "channels": [
          {
            "channel_id": "C0123456789",
            "channel_name": "#updated-channel-name",
            "team_id": "T01234567",
            "redirect_url": "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"
          }
        ]
      }
    },
    "type": "incident_integrations"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentIntegration-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentIntegration-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentIntegration-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentIntegration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentIntegration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentIntegration-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident integration metadata.
Field
Type
Description
data [_required_]
object
Incident integration metadata from a response.
attributes
object
Incident integration metadata's attributes for a create request.
created
date-time
Timestamp when the incident todo was created.
incident_id
string
UUID of the incident this integration metadata is connected to.
integration_type [_required_]
int32
A number indicating the type of integration this metadata is for. 1 indicates Slack; 8 indicates Jira.
metadata [_required_]
<oneOf>
Incident integration metadata's metadata attribute.
Option 1
object
Incident integration metadata for the Slack integration.
channels [_required_]
[object]
Array of Slack channels in this integration metadata.
channel_id [_required_]
string
Slack channel ID.
channel_name [_required_]
string
Name of the Slack channel.
redirect_url [_required_]
string
URL redirecting to the Slack channel.
team_id
string
Slack team ID.
Option 2
object
Incident integration metadata for the Jira integration.
issues [_required_]
[object]
Array of Jira issues in this integration metadata.
account [_required_]
string
URL of issue's Jira account.
issue_key
string
Jira issue's issue key.
issuetype_id
string
Jira issue's issue type.
project_key [_required_]
string
Jira issue's project keys.
redirect_url
string
URL redirecting to the Jira issue.
Option 3
object
Incident integration metadata for the Microsoft Teams integration.
teams [_required_]
[object]
Array of Microsoft Teams in this integration metadata.
ms_channel_id [_required_]
string
Microsoft Teams channel ID.
ms_channel_name [_required_]
string
Microsoft Teams channel name.
ms_tenant_id [_required_]
string
Microsoft Teams tenant ID.
redirect_url [_required_]
string
URL redirecting to the Microsoft Teams channel.
modified
date-time
Timestamp when the incident todo was last modified.
status
int32
A number indicating the status of this integration metadata. 0 indicates unknown; 1 indicates pending; 2 indicates complete; 3 indicates manually created; 4 indicates manually updated; 5 indicates failed.
id [_required_]
string
The incident integration metadata's ID.
relationships
object
The incident's integration relationships from a response.
created_by_user
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
last_modified_by_user
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
Integration metadata resource type. Allowed enum values: `incident_integrations`
default: `incident_integrations`
included
[ <oneOf>]
Included related resources that the user requested.
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
      "incident_id": "00000000-aaaa-0000-0000-000000000000",
      "integration_type": 1,
      "metadata": {
        "channels": [
          {
            "channel_id": "C0123456789",
            "channel_name": "#example-channel-name",
            "redirect_url": "https://slack.com/app_redirect?channel=C0123456789\u0026team=T01234567",
            "team_id": "T01234567"
          }
        ]
      },
      "modified": "2019-09-19T10:00:00.000Z",
      "status": "integer"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "incident_integrations"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Update an existing incident integration metadata returns "OK" response
Copy
```
                          # Path parameters  
export incident_id="CHANGE_ME"  
export integration_metadata_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/integrations/${integration_metadata_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "incident_id": "00000000-0000-0000-1234-000000000000",
      "integration_type": 1,
      "metadata": {
        "channels": [
          {
            "channel_id": "C0123456789",
            "channel_name": "#updated-channel-name",
            "team_id": "T01234567",
            "redirect_url": "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"
          }
        ]
      }
    },
    "type": "incident_integrations"
  }
}
EOF  

                        
```

#####  Update an existing incident integration metadata returns "OK" response
```
// Update an existing incident integration metadata returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	// the "incident" has an "incident_integration_metadata"
	IncidentIntegrationMetadataDataID := os.Getenv("INCIDENT_INTEGRATION_METADATA_DATA_ID")

	body := datadogV2.IncidentIntegrationMetadataPatchRequest{
		Data: datadogV2.IncidentIntegrationMetadataPatchData{
			Attributes: datadogV2.IncidentIntegrationMetadataAttributes{
				IncidentId:      datadog.PtrString(IncidentDataID),
				IntegrationType: 1,
				Metadata: datadogV2.IncidentIntegrationMetadataMetadata{
					SlackIntegrationMetadata: &datadogV2.SlackIntegrationMetadata{
						Channels: []datadogV2.SlackIntegrationMetadataChannelItem{
							{
								ChannelId:   "C0123456789",
								ChannelName: "#updated-channel-name",
								TeamId:      datadog.PtrString("T01234567"),
								RedirectUrl: "https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
							},
						},
					}},
			},
			Type: datadogV2.INCIDENTINTEGRATIONMETADATATYPE_INCIDENT_INTEGRATIONS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncidentIntegration", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncidentIntegration(ctx, IncidentDataID, IncidentIntegrationMetadataDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncidentIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncidentIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update an existing incident integration metadata returns "OK" response
```
// Update an existing incident integration metadata returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataAttributes;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataMetadata;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataPatchData;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataPatchRequest;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataResponse;
import com.datadog.api.client.v2.model.IncidentIntegrationMetadataType;
import com.datadog.api.client.v2.model.SlackIntegrationMetadata;
import com.datadog.api.client.v2.model.SlackIntegrationMetadataChannelItem;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncidentIntegration", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    // the "incident" has an "incident_integration_metadata"
    String INCIDENT_INTEGRATION_METADATA_DATA_ID =
        System.getenv("INCIDENT_INTEGRATION_METADATA_DATA_ID");

    IncidentIntegrationMetadataPatchRequest body =
        new IncidentIntegrationMetadataPatchRequest()
            .data(
                new IncidentIntegrationMetadataPatchData()
                    .attributes(
                        new IncidentIntegrationMetadataAttributes()
                            .incidentId(INCIDENT_DATA_ID)
                            .integrationType(1)
                            .metadata(
                                new IncidentIntegrationMetadataMetadata(
                                    new SlackIntegrationMetadata()
                                        .channels(
                                            Collections.singletonList(
                                                new SlackIntegrationMetadataChannelItem()
                                                    .channelId("C0123456789")
                                                    .channelName("#updated-channel-name")
                                                    .teamId("T01234567")
                                                    .redirectUrl(
                                                        "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"))))))
                    .type(IncidentIntegrationMetadataType.INCIDENT_INTEGRATIONS));

    try {
      IncidentIntegrationMetadataResponse result =
          apiInstance.updateIncidentIntegration(
              INCIDENT_DATA_ID, INCIDENT_INTEGRATION_METADATA_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncidentIntegration");
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

#####  Update an existing incident integration metadata returns "OK" response
```
"""
Update an existing incident integration metadata returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_integration_metadata_attributes import IncidentIntegrationMetadataAttributes
from datadog_api_client.v2.model.incident_integration_metadata_patch_data import IncidentIntegrationMetadataPatchData
from datadog_api_client.v2.model.incident_integration_metadata_patch_request import (
    IncidentIntegrationMetadataPatchRequest,
)
from datadog_api_client.v2.model.incident_integration_metadata_type import IncidentIntegrationMetadataType
from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
from datadog_api_client.v2.model.slack_integration_metadata_channel_item import SlackIntegrationMetadataChannelItem

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_integration_metadata"
INCIDENT_INTEGRATION_METADATA_DATA_ID = environ["INCIDENT_INTEGRATION_METADATA_DATA_ID"]

body = IncidentIntegrationMetadataPatchRequest(
    data=IncidentIntegrationMetadataPatchData(
        attributes=IncidentIntegrationMetadataAttributes(
            incident_id=INCIDENT_DATA_ID,
            integration_type=1,
            metadata=SlackIntegrationMetadata(
                channels=[
                    SlackIntegrationMetadataChannelItem(
                        channel_id="C0123456789",
                        channel_name="#updated-channel-name",
                        team_id="T01234567",
                        redirect_url="https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
                    ),
                ],
            ),
        ),
        type=IncidentIntegrationMetadataType.INCIDENT_INTEGRATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_integration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_integration(
        incident_id=INCIDENT_DATA_ID, integration_metadata_id=INCIDENT_INTEGRATION_METADATA_DATA_ID, body=body
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update an existing incident integration metadata returns "OK" response
```
# Update an existing incident integration metadata returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident_integration".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

# the "incident" has an "incident_integration_metadata"
INCIDENT_INTEGRATION_METADATA_DATA_ID = ENV["INCIDENT_INTEGRATION_METADATA_DATA_ID"]

body = DatadogAPIClient::V2::IncidentIntegrationMetadataPatchRequest.new({
  data: DatadogAPIClient::V2::IncidentIntegrationMetadataPatchData.new({
    attributes: DatadogAPIClient::V2::IncidentIntegrationMetadataAttributes.new({
      incident_id: INCIDENT_DATA_ID,
      integration_type: 1,
      metadata: DatadogAPIClient::V2::SlackIntegrationMetadata.new({
        channels: [
          DatadogAPIClient::V2::SlackIntegrationMetadataChannelItem.new({
            channel_id: "C0123456789",
            channel_name: "#updated-channel-name",
            team_id: "T01234567",
            redirect_url: "https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::IncidentIntegrationMetadataType::INCIDENT_INTEGRATIONS,
  }),
})
p api_instance.update_incident_integration(INCIDENT_DATA_ID, INCIDENT_INTEGRATION_METADATA_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update an existing incident integration metadata returns "OK" response
```
// Update an existing incident integration metadata returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataAttributes;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataMetadata;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataPatchData;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataPatchRequest;
use datadog_api_client::datadogV2::model::IncidentIntegrationMetadataType;
use datadog_api_client::datadogV2::model::SlackIntegrationMetadata;
use datadog_api_client::datadogV2::model::SlackIntegrationMetadataChannelItem;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();

    // the "incident" has an "incident_integration_metadata"
    let incident_integration_metadata_data_id =
        std::env::var("INCIDENT_INTEGRATION_METADATA_DATA_ID").unwrap();
    let body =
        IncidentIntegrationMetadataPatchRequest::new(IncidentIntegrationMetadataPatchData::new(
            IncidentIntegrationMetadataAttributes::new(
                1,
                IncidentIntegrationMetadataMetadata::SlackIntegrationMetadata(Box::new(
                    SlackIntegrationMetadata::new(vec![SlackIntegrationMetadataChannelItem::new(
                        "C0123456789".to_string(),
                        "#updated-channel-name".to_string(),
                        "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"
                            .to_string(),
                    )
                    .team_id("T01234567".to_string())]),
                )),
            )
            .incident_id(incident_data_id.clone()),
            IncidentIntegrationMetadataType::INCIDENT_INTEGRATIONS,
        ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncidentIntegration", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident_integration(
            incident_data_id.clone(),
            incident_integration_metadata_data_id.clone(),
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

#####  Update an existing incident integration metadata returns "OK" response
```
/**
 * Update an existing incident integration metadata returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncidentIntegration"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

// the "incident" has an "incident_integration_metadata"
const INCIDENT_INTEGRATION_METADATA_DATA_ID = process.env
  .INCIDENT_INTEGRATION_METADATA_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentIntegrationRequest = {
  body: {
    data: {
      attributes: {
        incidentId: INCIDENT_DATA_ID,
        integrationType: 1,
        metadata: {
          channels: [
            {
              channelId: "C0123456789",
              channelName: "#updated-channel-name",
              teamId: "T01234567",
              redirectUrl:
                "https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
            },
          ],
        },
      },
      type: "incident_integrations",
    },
  },
  incidentId: INCIDENT_DATA_ID,
  integrationMetadataId: INCIDENT_INTEGRATION_METADATA_DATA_ID,
};

apiInstance
  .updateIncidentIntegration(params)
  .then((data: v2.IncidentIntegrationMetadataResponse) => {
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
## [Delete an incident integration metadata](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-integration-metadata)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-integration-metadata-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}
### Overview
Delete an incident integration metadata.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
integration_metadata_id [_required_]
string
The UUID of the incident integration metadata.
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentIntegration-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentIntegration-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentIntegration-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentIntegration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentIntegration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentIntegration-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Delete an incident integration metadata
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
export integration_metadata_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/integrations/${integration_metadata_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an incident integration metadata
```
"""
Delete an incident integration metadata returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_integration_metadata"
INCIDENT_INTEGRATION_METADATA_DATA_ID = environ["INCIDENT_INTEGRATION_METADATA_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_integration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_integration(
        incident_id=INCIDENT_DATA_ID,
        integration_metadata_id=INCIDENT_INTEGRATION_METADATA_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an incident integration metadata
```
# Delete an incident integration metadata returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_integration".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

# the "incident" has an "incident_integration_metadata"
INCIDENT_INTEGRATION_METADATA_DATA_ID = ENV["INCIDENT_INTEGRATION_METADATA_DATA_ID"]
api_instance.delete_incident_integration(INCIDENT_DATA_ID, INCIDENT_INTEGRATION_METADATA_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an incident integration metadata
```
// Delete an incident integration metadata returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	// the "incident" has an "incident_integration_metadata"
	IncidentIntegrationMetadataDataID := os.Getenv("INCIDENT_INTEGRATION_METADATA_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncidentIntegration", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	r, err := api.DeleteIncidentIntegration(ctx, IncidentDataID, IncidentIntegrationMetadataDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.DeleteIncidentIntegration`: %v\n", err)
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

#####  Delete an incident integration metadata
```
// Delete an incident integration metadata returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentIntegration", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    // the "incident" has an "incident_integration_metadata"
    String INCIDENT_INTEGRATION_METADATA_DATA_ID =
        System.getenv("INCIDENT_INTEGRATION_METADATA_DATA_ID");

    try {
      apiInstance.deleteIncidentIntegration(
          INCIDENT_DATA_ID, INCIDENT_INTEGRATION_METADATA_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#deleteIncidentIntegration");
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

#####  Delete an incident integration metadata
```
// Delete an incident integration metadata returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();

    // the "incident" has an "incident_integration_metadata"
    let incident_integration_metadata_data_id =
        std::env::var("INCIDENT_INTEGRATION_METADATA_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentIntegration", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .delete_incident_integration(
            incident_data_id.clone(),
            incident_integration_metadata_data_id.clone(),
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

#####  Delete an incident integration metadata
```
/**
 * Delete an incident integration metadata returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentIntegration"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

// the "incident" has an "incident_integration_metadata"
const INCIDENT_INTEGRATION_METADATA_DATA_ID = process.env
  .INCIDENT_INTEGRATION_METADATA_DATA_ID as string;

const params: v2.IncidentsApiDeleteIncidentIntegrationRequest = {
  incidentId: INCIDENT_DATA_ID,
  integrationMetadataId: INCIDENT_INTEGRATION_METADATA_DATA_ID,
};

apiInstance
  .deleteIncidentIntegration(params)
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
## [Get a list of an incident's todos](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-an-incidents-todos)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-an-incidents-todos-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/todoshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos
### Overview
Get all todos for an incident. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTodos-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTodos-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTodos-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTodos-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTodos-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTodos-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a list of incident todos.
Field
Type
Description
data [_required_]
[object]
An array of incident todos.
attributes
object
Incident todo's attributes.
assignees [_required_]
[ <oneOf>]
Array of todo assignees.
Option 1
string
Assignee's @-handle.
Option 2
object
Anonymous assignee entity.
icon [_required_]
string
URL for assignee's icon.
id [_required_]
string
Anonymous assignee's ID.
name [_required_]
string
Assignee's name.
source [_required_]
enum
The source of the anonymous assignee. Allowed enum values: `slack,microsoft_teams`
default: `slack`
completed
string
Timestamp when the todo was completed.
content [_required_]
string
The follow-up task's content.
created
date-time
Timestamp when the incident todo was created.
due_date
string
Timestamp when the todo should be completed by.
incident_id
string
UUID of the incident this todo is connected to.
modified
date-time
Timestamp when the incident todo was last modified.
id [_required_]
string
The incident todo's ID.
relationships
object
The incident's relationships from a response.
created_by_user
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
last_modified_by_user
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
Todo resource type. Allowed enum values: `incident_todos`
default: `incident_todos`
included
[ <oneOf>]
Included related resources that the user requested.
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
        "assignees": [
          {
            "description": "@test.user@test.com",
            "example": "@test.user@test.com",
            "type": "@test.user@test.com"
          }
        ],
        "completed": "2023-03-06T22:00:00.000000+00:00",
        "content": "Restore lost data.",
        "created": "2019-09-19T10:00:00.000Z",
        "due_date": "2023-07-10T05:00:00.000000+00:00",
        "incident_id": "00000000-aaaa-0000-0000-000000000000",
        "modified": "2019-09-19T10:00:00.000Z"
      },
      "id": "00000000-0000-0000-1234-000000000000",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "incident_todos"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get a list of an incident's todos
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/todos" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of an incident's todos
```
"""
Get a list of an incident's todos returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_incident_todos"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_todos(
        incident_id=INCIDENT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of an incident's todos
```
# Get a list of an incident's todos returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_todos".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]
p api_instance.list_incident_todos(INCIDENT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of an incident's todos
```
// Get a list of an incident's todos returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ListIncidentTodos", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidentTodos(ctx, IncidentDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidentTodos`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidentTodos`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of an incident's todos
```
// Get a list of an incident's todos returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTodoListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentTodos", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    try {
      IncidentTodoListResponse result = apiInstance.listIncidentTodos(INCIDENT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidentTodos");
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

#####  Get a list of an incident's todos
```
// Get a list of an incident's todos returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentTodos", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api.list_incident_todos(incident_data_id.clone()).await;
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

#####  Get a list of an incident's todos
```
/**
 * Get a list of an incident's todos returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentTodos"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiListIncidentTodosRequest = {
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .listIncidentTodos(params)
  .then((data: v2.IncidentTodoListResponse) => {
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
## [Create an incident todo](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-todo)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-todo-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/todoshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todoshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos
### Overview
Create an incident todo. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
### Request
#### Body Data (required)
Incident todo payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident todo data for a create request.
attributes [_required_]
object
Incident todo's attributes.
assignees [_required_]
[ <oneOf>]
Array of todo assignees.
Option 1
string
Assignee's @-handle.
Option 2
object
Anonymous assignee entity.
icon [_required_]
string
URL for assignee's icon.
id [_required_]
string
Anonymous assignee's ID.
name [_required_]
string
Assignee's name.
source [_required_]
enum
The source of the anonymous assignee. Allowed enum values: `slack,microsoft_teams`
default: `slack`
completed
string
Timestamp when the todo was completed.
content [_required_]
string
The follow-up task's content.
created
date-time
Timestamp when the incident todo was created.
due_date
string
Timestamp when the todo should be completed by.
incident_id
string
UUID of the incident this todo is connected to.
modified
date-time
Timestamp when the incident todo was last modified.
type [_required_]
enum
Todo resource type. Allowed enum values: `incident_todos`
default: `incident_todos`
```
{
  "data": {
    "attributes": {
      "assignees": [
        "@test.user@test.com"
      ],
      "content": "Restore lost data."
    },
    "type": "incident_todos"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentTodo-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentTodo-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentTodo-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentTodo-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentTodo-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentTodo-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident todo.
Field
Type
Description
data [_required_]
object
Incident todo response data.
attributes
object
Incident todo's attributes.
assignees [_required_]
[ <oneOf>]
Array of todo assignees.
Option 1
string
Assignee's @-handle.
Option 2
object
Anonymous assignee entity.
icon [_required_]
string
URL for assignee's icon.
id [_required_]
string
Anonymous assignee's ID.
name [_required_]
string
Assignee's name.
source [_required_]
enum
The source of the anonymous assignee. Allowed enum values: `slack,microsoft_teams`
default: `slack`
completed
string
Timestamp when the todo was completed.
content [_required_]
string
The follow-up task's content.
created
date-time
Timestamp when the incident todo was created.
due_date
string
Timestamp when the todo should be completed by.
incident_id
string
UUID of the incident this todo is connected to.
modified
date-time
Timestamp when the incident todo was last modified.
id [_required_]
string
The incident todo's ID.
relationships
object
The incident's relationships from a response.
created_by_user
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
last_modified_by_user
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
Todo resource type. Allowed enum values: `incident_todos`
default: `incident_todos`
included
[ <oneOf>]
Included related resources that the user requested.
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
      "assignees": [
        {
          "description": "@test.user@test.com",
          "example": "@test.user@test.com",
          "type": "@test.user@test.com"
        }
      ],
      "completed": "2023-03-06T22:00:00.000000+00:00",
      "content": "Restore lost data.",
      "created": "2019-09-19T10:00:00.000Z",
      "due_date": "2023-07-10T05:00:00.000000+00:00",
      "incident_id": "00000000-aaaa-0000-0000-000000000000",
      "modified": "2019-09-19T10:00:00.000Z"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "incident_todos"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Create an incident todo returns "CREATED" response
Copy
```
                          # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/todos" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "assignees": [
        "@test.user@test.com"
      ],
      "content": "Restore lost data."
    },
    "type": "incident_todos"
  }
}
EOF  

                        
```

#####  Create an incident todo returns "CREATED" response
```
// Create an incident todo returns "CREATED" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	body := datadogV2.IncidentTodoCreateRequest{
		Data: datadogV2.IncidentTodoCreateData{
			Attributes: datadogV2.IncidentTodoAttributes{
				Assignees: []datadogV2.IncidentTodoAssignee{
					datadogV2.IncidentTodoAssignee{
						IncidentTodoAssigneeHandle: datadog.PtrString("@test.user@test.com")},
				},
				Content: "Restore lost data.",
			},
			Type: datadogV2.INCIDENTTODOTYPE_INCIDENT_TODOS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncidentTodo", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.CreateIncidentTodo(ctx, IncidentDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.CreateIncidentTodo`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.CreateIncidentTodo`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create an incident todo returns "CREATED" response
```
// Create an incident todo returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTodoAssignee;
import com.datadog.api.client.v2.model.IncidentTodoAttributes;
import com.datadog.api.client.v2.model.IncidentTodoCreateData;
import com.datadog.api.client.v2.model.IncidentTodoCreateRequest;
import com.datadog.api.client.v2.model.IncidentTodoResponse;
import com.datadog.api.client.v2.model.IncidentTodoType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentTodo", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    IncidentTodoCreateRequest body =
        new IncidentTodoCreateRequest()
            .data(
                new IncidentTodoCreateData()
                    .attributes(
                        new IncidentTodoAttributes()
                            .assignees(
                                Collections.singletonList(
                                    new IncidentTodoAssignee("@test.user@test.com")))
                            .content("Restore lost data."))
                    .type(IncidentTodoType.INCIDENT_TODOS));

    try {
      IncidentTodoResponse result = apiInstance.createIncidentTodo(INCIDENT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#createIncidentTodo");
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

#####  Create an incident todo returns "CREATED" response
```
"""
Create an incident todo returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray
from datadog_api_client.v2.model.incident_todo_attributes import IncidentTodoAttributes
from datadog_api_client.v2.model.incident_todo_create_data import IncidentTodoCreateData
from datadog_api_client.v2.model.incident_todo_create_request import IncidentTodoCreateRequest
from datadog_api_client.v2.model.incident_todo_type import IncidentTodoType

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentTodoCreateRequest(
    data=IncidentTodoCreateData(
        attributes=IncidentTodoAttributes(
            assignees=IncidentTodoAssigneeArray(
                [
                    "@test.user@test.com",
                ]
            ),
            content="Restore lost data.",
        ),
        type=IncidentTodoType.INCIDENT_TODOS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_todo"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_todo(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an incident todo returns "CREATED" response
```
# Create an incident todo returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_todo".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

body = DatadogAPIClient::V2::IncidentTodoCreateRequest.new({
  data: DatadogAPIClient::V2::IncidentTodoCreateData.new({
    attributes: DatadogAPIClient::V2::IncidentTodoAttributes.new({
      assignees: [
        "@test.user@test.com",
      ],
      content: "Restore lost data.",
    }),
    type: DatadogAPIClient::V2::IncidentTodoType::INCIDENT_TODOS,
  }),
})
p api_instance.create_incident_todo(INCIDENT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create an incident todo returns "CREATED" response
```
// Create an incident todo returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentTodoAssignee;
use datadog_api_client::datadogV2::model::IncidentTodoAttributes;
use datadog_api_client::datadogV2::model::IncidentTodoCreateData;
use datadog_api_client::datadogV2::model::IncidentTodoCreateRequest;
use datadog_api_client::datadogV2::model::IncidentTodoType;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();
    let body = IncidentTodoCreateRequest::new(IncidentTodoCreateData::new(
        IncidentTodoAttributes::new(
            vec![IncidentTodoAssignee::IncidentTodoAssigneeHandle(
                "@test.user@test.com".to_string(),
            )],
            "Restore lost data.".to_string(),
        ),
        IncidentTodoType::INCIDENT_TODOS,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentTodo", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .create_incident_todo(incident_data_id.clone(), body)
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

#####  Create an incident todo returns "CREATED" response
```
/**
 * Create an incident todo returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentTodo"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

const params: v2.IncidentsApiCreateIncidentTodoRequest = {
  body: {
    data: {
      attributes: {
        assignees: ["@test.user@test.com"],
        content: "Restore lost data.",
      },
      type: "incident_todos",
    },
  },
  incidentId: INCIDENT_DATA_ID,
};

apiInstance
  .createIncidentTodo(params)
  .then((data: v2.IncidentTodoResponse) => {
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
## [Get incident todo details](https://docs.datadoghq.com/api/latest/incidents/#get-incident-todo-details)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-incident-todo-details-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}
### Overview
Get incident todo details. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
todo_id [_required_]
string
The UUID of the incident todo.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentTodo-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentTodo-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentTodo-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentTodo-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentTodo-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentTodo-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident todo.
Field
Type
Description
data [_required_]
object
Incident todo response data.
attributes
object
Incident todo's attributes.
assignees [_required_]
[ <oneOf>]
Array of todo assignees.
Option 1
string
Assignee's @-handle.
Option 2
object
Anonymous assignee entity.
icon [_required_]
string
URL for assignee's icon.
id [_required_]
string
Anonymous assignee's ID.
name [_required_]
string
Assignee's name.
source [_required_]
enum
The source of the anonymous assignee. Allowed enum values: `slack,microsoft_teams`
default: `slack`
completed
string
Timestamp when the todo was completed.
content [_required_]
string
The follow-up task's content.
created
date-time
Timestamp when the incident todo was created.
due_date
string
Timestamp when the todo should be completed by.
incident_id
string
UUID of the incident this todo is connected to.
modified
date-time
Timestamp when the incident todo was last modified.
id [_required_]
string
The incident todo's ID.
relationships
object
The incident's relationships from a response.
created_by_user
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
last_modified_by_user
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
Todo resource type. Allowed enum values: `incident_todos`
default: `incident_todos`
included
[ <oneOf>]
Included related resources that the user requested.
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
      "assignees": [
        {
          "description": "@test.user@test.com",
          "example": "@test.user@test.com",
          "type": "@test.user@test.com"
        }
      ],
      "completed": "2023-03-06T22:00:00.000000+00:00",
      "content": "Restore lost data.",
      "created": "2019-09-19T10:00:00.000Z",
      "due_date": "2023-07-10T05:00:00.000000+00:00",
      "incident_id": "00000000-aaaa-0000-0000-000000000000",
      "modified": "2019-09-19T10:00:00.000Z"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "incident_todos"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get incident todo details
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
export todo_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/todos/${todo_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get incident todo details
```
"""
Get incident todo details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = environ["INCIDENT_TODO_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident_todo"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_todo(
        incident_id=INCIDENT_DATA_ID,
        todo_id=INCIDENT_TODO_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get incident todo details
```
# Get incident todo details returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident_todo".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = ENV["INCIDENT_TODO_DATA_ID"]
p api_instance.get_incident_todo(INCIDENT_DATA_ID, INCIDENT_TODO_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get incident todo details
```
// Get incident todo details returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	// the "incident" has an "incident_todo"
	IncidentTodoDataID := os.Getenv("INCIDENT_TODO_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetIncidentTodo", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.GetIncidentTodo(ctx, IncidentDataID, IncidentTodoDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.GetIncidentTodo`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.GetIncidentTodo`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get incident todo details
```
// Get incident todo details returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTodoResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncidentTodo", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    // the "incident" has an "incident_todo"
    String INCIDENT_TODO_DATA_ID = System.getenv("INCIDENT_TODO_DATA_ID");

    try {
      IncidentTodoResponse result =
          apiInstance.getIncidentTodo(INCIDENT_DATA_ID, INCIDENT_TODO_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getIncidentTodo");
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

#####  Get incident todo details
```
// Get incident todo details returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();

    // the "incident" has an "incident_todo"
    let incident_todo_data_id = std::env::var("INCIDENT_TODO_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncidentTodo", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .get_incident_todo(incident_data_id.clone(), incident_todo_data_id.clone())
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

#####  Get incident todo details
```
/**
 * Get incident todo details returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncidentTodo"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

// the "incident" has an "incident_todo"
const INCIDENT_TODO_DATA_ID = process.env.INCIDENT_TODO_DATA_ID as string;

const params: v2.IncidentsApiGetIncidentTodoRequest = {
  incidentId: INCIDENT_DATA_ID,
  todoId: INCIDENT_TODO_DATA_ID,
};

apiInstance
  .getIncidentTodo(params)
  .then((data: v2.IncidentTodoResponse) => {
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
## [Update an incident todo](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-todo)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-todo-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PATCH https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}
### Overview
Update an incident todo. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
todo_id [_required_]
string
The UUID of the incident todo.
### Request
#### Body Data (required)
Incident todo payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident todo data for a patch request.
attributes [_required_]
object
Incident todo's attributes.
assignees [_required_]
[ <oneOf>]
Array of todo assignees.
Option 1
string
Assignee's @-handle.
Option 2
object
Anonymous assignee entity.
icon [_required_]
string
URL for assignee's icon.
id [_required_]
string
Anonymous assignee's ID.
name [_required_]
string
Assignee's name.
source [_required_]
enum
The source of the anonymous assignee. Allowed enum values: `slack,microsoft_teams`
default: `slack`
completed
string
Timestamp when the todo was completed.
content [_required_]
string
The follow-up task's content.
created
date-time
Timestamp when the incident todo was created.
due_date
string
Timestamp when the todo should be completed by.
incident_id
string
UUID of the incident this todo is connected to.
modified
date-time
Timestamp when the incident todo was last modified.
type [_required_]
enum
Todo resource type. Allowed enum values: `incident_todos`
default: `incident_todos`
```
{
  "data": {
    "attributes": {
      "assignees": [
        "@test.user@test.com"
      ],
      "content": "Restore lost data.",
      "completed": "2023-03-06T22:00:00.000000+00:00",
      "due_date": "2023-07-10T05:00:00.000000+00:00"
    },
    "type": "incident_todos"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentTodo-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentTodo-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentTodo-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentTodo-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentTodo-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentTodo-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with an incident todo.
Field
Type
Description
data [_required_]
object
Incident todo response data.
attributes
object
Incident todo's attributes.
assignees [_required_]
[ <oneOf>]
Array of todo assignees.
Option 1
string
Assignee's @-handle.
Option 2
object
Anonymous assignee entity.
icon [_required_]
string
URL for assignee's icon.
id [_required_]
string
Anonymous assignee's ID.
name [_required_]
string
Assignee's name.
source [_required_]
enum
The source of the anonymous assignee. Allowed enum values: `slack,microsoft_teams`
default: `slack`
completed
string
Timestamp when the todo was completed.
content [_required_]
string
The follow-up task's content.
created
date-time
Timestamp when the incident todo was created.
due_date
string
Timestamp when the todo should be completed by.
incident_id
string
UUID of the incident this todo is connected to.
modified
date-time
Timestamp when the incident todo was last modified.
id [_required_]
string
The incident todo's ID.
relationships
object
The incident's relationships from a response.
created_by_user
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
last_modified_by_user
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
Todo resource type. Allowed enum values: `incident_todos`
default: `incident_todos`
included
[ <oneOf>]
Included related resources that the user requested.
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
      "assignees": [
        {
          "description": "@test.user@test.com",
          "example": "@test.user@test.com",
          "type": "@test.user@test.com"
        }
      ],
      "completed": "2023-03-06T22:00:00.000000+00:00",
      "content": "Restore lost data.",
      "created": "2019-09-19T10:00:00.000Z",
      "due_date": "2023-07-10T05:00:00.000000+00:00",
      "incident_id": "00000000-aaaa-0000-0000-000000000000",
      "modified": "2019-09-19T10:00:00.000Z"
    },
    "id": "00000000-0000-0000-1234-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "incident_todos"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Update an incident todo returns "OK" response
Copy
```
                          # Path parameters  
export incident_id="CHANGE_ME"  
export todo_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/todos/${todo_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "assignees": [
        "@test.user@test.com"
      ],
      "content": "Restore lost data.",
      "completed": "2023-03-06T22:00:00.000000+00:00",
      "due_date": "2023-07-10T05:00:00.000000+00:00"
    },
    "type": "incident_todos"
  }
}
EOF  

                        
```

#####  Update an incident todo returns "OK" response
```
// Update an incident todo returns "OK" response

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
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	// the "incident" has an "incident_todo"
	IncidentTodoDataID := os.Getenv("INCIDENT_TODO_DATA_ID")

	body := datadogV2.IncidentTodoPatchRequest{
		Data: datadogV2.IncidentTodoPatchData{
			Attributes: datadogV2.IncidentTodoAttributes{
				Assignees: []datadogV2.IncidentTodoAssignee{
					datadogV2.IncidentTodoAssignee{
						IncidentTodoAssigneeHandle: datadog.PtrString("@test.user@test.com")},
				},
				Content:   "Restore lost data.",
				Completed: *datadog.NewNullableString(datadog.PtrString("2023-03-06T22:00:00.000000+00:00")),
				DueDate:   *datadog.NewNullableString(datadog.PtrString("2023-07-10T05:00:00.000000+00:00")),
			},
			Type: datadogV2.INCIDENTTODOTYPE_INCIDENT_TODOS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncidentTodo", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncidentTodo(ctx, IncidentDataID, IncidentTodoDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncidentTodo`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncidentTodo`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update an incident todo returns "OK" response
```
// Update an incident todo returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTodoAssignee;
import com.datadog.api.client.v2.model.IncidentTodoAttributes;
import com.datadog.api.client.v2.model.IncidentTodoPatchData;
import com.datadog.api.client.v2.model.IncidentTodoPatchRequest;
import com.datadog.api.client.v2.model.IncidentTodoResponse;
import com.datadog.api.client.v2.model.IncidentTodoType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncidentTodo", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    // the "incident" has an "incident_todo"
    String INCIDENT_TODO_DATA_ID = System.getenv("INCIDENT_TODO_DATA_ID");

    IncidentTodoPatchRequest body =
        new IncidentTodoPatchRequest()
            .data(
                new IncidentTodoPatchData()
                    .attributes(
                        new IncidentTodoAttributes()
                            .assignees(
                                Collections.singletonList(
                                    new IncidentTodoAssignee("@test.user@test.com")))
                            .content("Restore lost data.")
                            .completed("2023-03-06T22:00:00.000000+00:00")
                            .dueDate("2023-07-10T05:00:00.000000+00:00"))
                    .type(IncidentTodoType.INCIDENT_TODOS));

    try {
      IncidentTodoResponse result =
          apiInstance.updateIncidentTodo(INCIDENT_DATA_ID, INCIDENT_TODO_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncidentTodo");
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

#####  Update an incident todo returns "OK" response
```
"""
Update an incident todo returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray
from datadog_api_client.v2.model.incident_todo_attributes import IncidentTodoAttributes
from datadog_api_client.v2.model.incident_todo_patch_data import IncidentTodoPatchData
from datadog_api_client.v2.model.incident_todo_patch_request import IncidentTodoPatchRequest
from datadog_api_client.v2.model.incident_todo_type import IncidentTodoType

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = environ["INCIDENT_TODO_DATA_ID"]

body = IncidentTodoPatchRequest(
    data=IncidentTodoPatchData(
        attributes=IncidentTodoAttributes(
            assignees=IncidentTodoAssigneeArray(
                [
                    "@test.user@test.com",
                ]
            ),
            content="Restore lost data.",
            completed="2023-03-06T22:00:00.000000+00:00",
            due_date="2023-07-10T05:00:00.000000+00:00",
        ),
        type=IncidentTodoType.INCIDENT_TODOS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_todo"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_todo(incident_id=INCIDENT_DATA_ID, todo_id=INCIDENT_TODO_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update an incident todo returns "OK" response
```
# Update an incident todo returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident_todo".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = ENV["INCIDENT_TODO_DATA_ID"]

body = DatadogAPIClient::V2::IncidentTodoPatchRequest.new({
  data: DatadogAPIClient::V2::IncidentTodoPatchData.new({
    attributes: DatadogAPIClient::V2::IncidentTodoAttributes.new({
      assignees: [
        "@test.user@test.com",
      ],
      content: "Restore lost data.",
      completed: "2023-03-06T22:00:00.000000+00:00",
      due_date: "2023-07-10T05:00:00.000000+00:00",
    }),
    type: DatadogAPIClient::V2::IncidentTodoType::INCIDENT_TODOS,
  }),
})
p api_instance.update_incident_todo(INCIDENT_DATA_ID, INCIDENT_TODO_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update an incident todo returns "OK" response
```
// Update an incident todo returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentTodoAssignee;
use datadog_api_client::datadogV2::model::IncidentTodoAttributes;
use datadog_api_client::datadogV2::model::IncidentTodoPatchData;
use datadog_api_client::datadogV2::model::IncidentTodoPatchRequest;
use datadog_api_client::datadogV2::model::IncidentTodoType;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();

    // the "incident" has an "incident_todo"
    let incident_todo_data_id = std::env::var("INCIDENT_TODO_DATA_ID").unwrap();
    let body = IncidentTodoPatchRequest::new(IncidentTodoPatchData::new(
        IncidentTodoAttributes::new(
            vec![IncidentTodoAssignee::IncidentTodoAssigneeHandle(
                "@test.user@test.com".to_string(),
            )],
            "Restore lost data.".to_string(),
        )
        .completed(Some("2023-03-06T22:00:00.000000+00:00".to_string()))
        .due_date(Some("2023-07-10T05:00:00.000000+00:00".to_string())),
        IncidentTodoType::INCIDENT_TODOS,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncidentTodo", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident_todo(
            incident_data_id.clone(),
            incident_todo_data_id.clone(),
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

#####  Update an incident todo returns "OK" response
```
/**
 * Update an incident todo returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncidentTodo"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

// the "incident" has an "incident_todo"
const INCIDENT_TODO_DATA_ID = process.env.INCIDENT_TODO_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentTodoRequest = {
  body: {
    data: {
      attributes: {
        assignees: ["@test.user@test.com"],
        content: "Restore lost data.",
        completed: "2023-03-06T22:00:00.000000+00:00",
        dueDate: "2023-07-10T05:00:00.000000+00:00",
      },
      type: "incident_todos",
    },
  },
  incidentId: INCIDENT_DATA_ID,
  todoId: INCIDENT_TODO_DATA_ID,
};

apiInstance
  .updateIncidentTodo(params)
  .then((data: v2.IncidentTodoResponse) => {
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
## [Delete an incident todo](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-todo)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-todo-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}
### Overview
Delete an incident todo. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
todo_id [_required_]
string
The UUID of the incident todo.
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentTodo-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentTodo-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentTodo-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentTodo-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentTodo-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentTodo-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Delete an incident todo
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
export todo_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/relationships/todos/${todo_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an incident todo
```
"""
Delete an incident todo returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = environ["INCIDENT_TODO_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_todo"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_todo(
        incident_id=INCIDENT_DATA_ID,
        todo_id=INCIDENT_TODO_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an incident todo
```
# Delete an incident todo returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_todo".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident" in the system
INCIDENT_DATA_ID = ENV["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = ENV["INCIDENT_TODO_DATA_ID"]
api_instance.delete_incident_todo(INCIDENT_DATA_ID, INCIDENT_TODO_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an incident todo
```
// Delete an incident todo returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "incident" in the system
	IncidentDataID := os.Getenv("INCIDENT_DATA_ID")

	// the "incident" has an "incident_todo"
	IncidentTodoDataID := os.Getenv("INCIDENT_TODO_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncidentTodo", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	r, err := api.DeleteIncidentTodo(ctx, IncidentDataID, IncidentTodoDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.DeleteIncidentTodo`: %v\n", err)
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

#####  Delete an incident todo
```
// Delete an incident todo returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentTodo", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident" in the system
    String INCIDENT_DATA_ID = System.getenv("INCIDENT_DATA_ID");

    // the "incident" has an "incident_todo"
    String INCIDENT_TODO_DATA_ID = System.getenv("INCIDENT_TODO_DATA_ID");

    try {
      apiInstance.deleteIncidentTodo(INCIDENT_DATA_ID, INCIDENT_TODO_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#deleteIncidentTodo");
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

#####  Delete an incident todo
```
// Delete an incident todo returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident" in the system
    let incident_data_id = std::env::var("INCIDENT_DATA_ID").unwrap();

    // the "incident" has an "incident_todo"
    let incident_todo_data_id = std::env::var("INCIDENT_TODO_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentTodo", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .delete_incident_todo(incident_data_id.clone(), incident_todo_data_id.clone())
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

#####  Delete an incident todo
```
/**
 * Delete an incident todo returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentTodo"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident" in the system
const INCIDENT_DATA_ID = process.env.INCIDENT_DATA_ID as string;

// the "incident" has an "incident_todo"
const INCIDENT_TODO_DATA_ID = process.env.INCIDENT_TODO_DATA_ID as string;

const params: v2.IncidentsApiDeleteIncidentTodoRequest = {
  incidentId: INCIDENT_DATA_ID,
  todoId: INCIDENT_TODO_DATA_ID,
};

apiInstance
  .deleteIncidentTodo(params)
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
## [Create an incident type](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-type)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-type-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/incidents/config/typeshttps://api.ap2.datadoghq.com/api/v2/incidents/config/typeshttps://api.datadoghq.eu/api/v2/incidents/config/typeshttps://api.ddog-gov.com/api/v2/incidents/config/typeshttps://api.datadoghq.com/api/v2/incidents/config/typeshttps://api.us3.datadoghq.com/api/v2/incidents/config/typeshttps://api.us5.datadoghq.com/api/v2/incidents/config/types
### Overview
Create an incident type. This endpoint requires the `incident_settings_write` permission.
OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Request
#### Body Data (required)
Incident type payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident type data for a create request.
attributes [_required_]
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "attributes": {
      "description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
      "is_default": false,
      "name": "Security Incident"
    },
    "type": "incident_types"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentType-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentType-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentType-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentType-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentType-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentType-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Incident type response data.
Field
Type
Description
data [_required_]
object
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "attributes": {
      "createdAt": "2019-09-19T10:00:00.000Z",
      "createdBy": "00000000-0000-0000-0000-000000000000",
      "description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
      "is_default": false,
      "lastModifiedBy": "00000000-0000-0000-0000-000000000000",
      "modifiedAt": "2019-09-19T10:00:00.000Z",
      "name": "Security Incident",
      "prefix": "IR"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "google_meet_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "google_meet_configurations"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "microsoft_teams_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "microsoft_teams_configurations"
        }
      },
      "zoom_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "zoom_configurations"
        }
      }
    },
    "type": "incident_types"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Create an incident type returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/types" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
      "is_default": false,
      "name": "Security Incident"
    },
    "type": "incident_types"
  }
}
EOF  

                        
```

#####  Create an incident type returns "CREATED" response
```
// Create an incident type returns "CREATED" response

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
	body := datadogV2.IncidentTypeCreateRequest{
		Data: datadogV2.IncidentTypeCreateData{
			Attributes: datadogV2.IncidentTypeAttributes{
				Description: datadog.PtrString("Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data."),
				IsDefault:   datadog.PtrBool(false),
				Name:        "Security Incident",
			},
			Type: datadogV2.INCIDENTTYPETYPE_INCIDENT_TYPES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncidentType", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.CreateIncidentType(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.CreateIncidentType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.CreateIncidentType`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create an incident type returns "CREATED" response
```
// Create an incident type returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTypeAttributes;
import com.datadog.api.client.v2.model.IncidentTypeCreateData;
import com.datadog.api.client.v2.model.IncidentTypeCreateRequest;
import com.datadog.api.client.v2.model.IncidentTypeResponse;
import com.datadog.api.client.v2.model.IncidentTypeType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentType", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    IncidentTypeCreateRequest body =
        new IncidentTypeCreateRequest()
            .data(
                new IncidentTypeCreateData()
                    .attributes(
                        new IncidentTypeAttributes()
                            .description(
                                "Any incidents that harm (or have the potential to) the"
                                    + " confidentiality, integrity, or availability of our data.")
                            .isDefault(false)
                            .name("Security Incident"))
                    .type(IncidentTypeType.INCIDENT_TYPES));

    try {
      IncidentTypeResponse result = apiInstance.createIncidentType(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#createIncidentType");
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

#####  Create an incident type returns "CREATED" response
```
"""
Create an incident type returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type_attributes import IncidentTypeAttributes
from datadog_api_client.v2.model.incident_type_create_data import IncidentTypeCreateData
from datadog_api_client.v2.model.incident_type_create_request import IncidentTypeCreateRequest
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType

body = IncidentTypeCreateRequest(
    data=IncidentTypeCreateData(
        attributes=IncidentTypeAttributes(
            description="Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
            is_default=False,
            name="Security Incident",
        ),
        type=IncidentTypeType.INCIDENT_TYPES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_type(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an incident type returns "CREATED" response
```
# Create an incident type returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_type".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

body = DatadogAPIClient::V2::IncidentTypeCreateRequest.new({
  data: DatadogAPIClient::V2::IncidentTypeCreateData.new({
    attributes: DatadogAPIClient::V2::IncidentTypeAttributes.new({
      description: "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
      is_default: false,
      name: "Security Incident",
    }),
    type: DatadogAPIClient::V2::IncidentTypeType::INCIDENT_TYPES,
  }),
})
p api_instance.create_incident_type(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create an incident type returns "CREATED" response
```
// Create an incident type returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentTypeAttributes;
use datadog_api_client::datadogV2::model::IncidentTypeCreateData;
use datadog_api_client::datadogV2::model::IncidentTypeCreateRequest;
use datadog_api_client::datadogV2::model::IncidentTypeType;

#[tokio::main]
async fn main() {
    let body =
        IncidentTypeCreateRequest::new(
            IncidentTypeCreateData::new(
                IncidentTypeAttributes::new("Security Incident".to_string())
                    .description(
                        "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.".to_string(),
                    )
                    .is_default(false),
                IncidentTypeType::INCIDENT_TYPES,
            ),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentType", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api.create_incident_type(body).await;
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

#####  Create an incident type returns "CREATED" response
```
/**
 * Create an incident type returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentType"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

const params: v2.IncidentsApiCreateIncidentTypeRequest = {
  body: {
    data: {
      attributes: {
        description:
          "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
        isDefault: false,
        name: "Security Incident",
      },
      type: "incident_types",
    },
  },
};

apiInstance
  .createIncidentType(params)
  .then((data: v2.IncidentTypeResponse) => {
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
## [Get a list of incident types](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-incident-types)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-incident-types-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/config/typeshttps://api.ap2.datadoghq.com/api/v2/incidents/config/typeshttps://api.datadoghq.eu/api/v2/incidents/config/typeshttps://api.ddog-gov.com/api/v2/incidents/config/typeshttps://api.datadoghq.com/api/v2/incidents/config/typeshttps://api.us3.datadoghq.com/api/v2/incidents/config/typeshttps://api.us5.datadoghq.com/api/v2/incidents/config/types
### Overview
Get all incident types. This endpoint requires any of the following permissions:
* `incident_settings_read`
* `incident_read`
  

OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
include_deleted
boolean
Include deleted incident types in the response.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTypes-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTypes-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTypes-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTypes-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentTypes-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a list of incident types.
Field
Type
Description
data [_required_]
[object]
An array of incident type objects.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": [
    {
      "attributes": {
        "createdAt": "2019-09-19T10:00:00.000Z",
        "createdBy": "00000000-0000-0000-0000-000000000000",
        "description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
        "is_default": false,
        "lastModifiedBy": "00000000-0000-0000-0000-000000000000",
        "modifiedAt": "2019-09-19T10:00:00.000Z",
        "name": "Security Incident",
        "prefix": "IR"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "google_meet_configuration": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "google_meet_configurations"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "microsoft_teams_configuration": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "microsoft_teams_configurations"
          }
        },
        "zoom_configuration": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "zoom_configurations"
          }
        }
      },
      "type": "incident_types"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get a list of incident types
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/types" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of incident types
```
"""
Get a list of incident types returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["list_incident_types"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_types()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of incident types
```
# Get a list of incident types returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_types".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.list_incident_types()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of incident types
```
// Get a list of incident types returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListIncidentTypes", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidentTypes(ctx, *datadogV2.NewListIncidentTypesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidentTypes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidentTypes`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of incident types
```
// Get a list of incident types returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTypeListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentTypes", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentTypeListResponse result = apiInstance.listIncidentTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidentTypes");
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

#####  Get a list of incident types
```
// Get a list of incident types returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::ListIncidentTypesOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentTypes", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .list_incident_types(ListIncidentTypesOptionalParams::default())
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

#####  Get a list of incident types
```
/**
 * Get a list of incident types returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentTypes"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

apiInstance
  .listIncidentTypes()
  .then((data: v2.IncidentTypeListResponse) => {
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
## [Get incident type details](https://docs.datadoghq.com/api/latest/incidents/#get-incident-type-details)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-incident-type-details-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.ap2.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.datadoghq.eu/api/v2/incidents/config/types/{incident_type_id}https://api.ddog-gov.com/api/v2/incidents/config/types/{incident_type_id}https://api.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.us3.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.us5.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}
### Overview
Get incident type details. This endpoint requires the `incident_read` permission.
OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_type_id [_required_]
string
The UUID of the incident type.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentType-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentType-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentType-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentType-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentType-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentType-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Incident type response data.
Field
Type
Description
data [_required_]
object
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "attributes": {
      "createdAt": "2019-09-19T10:00:00.000Z",
      "createdBy": "00000000-0000-0000-0000-000000000000",
      "description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
      "is_default": false,
      "lastModifiedBy": "00000000-0000-0000-0000-000000000000",
      "modifiedAt": "2019-09-19T10:00:00.000Z",
      "name": "Security Incident",
      "prefix": "IR"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "google_meet_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "google_meet_configurations"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "microsoft_teams_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "microsoft_teams_configurations"
        }
      },
      "zoom_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "zoom_configurations"
        }
      }
    },
    "type": "incident_types"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get incident type details
Copy
```
                  # Path parameters  
export incident_type_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/types/${incident_type_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get incident type details
```
"""
Get incident type details returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["get_incident_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_type(
        incident_type_id="incident_type_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get incident type details
```
# Get incident type details returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident_type".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.get_incident_type("incident_type_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get incident type details
```
// Get incident type details returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.GetIncidentType", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.GetIncidentType(ctx, "incident_type_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.GetIncidentType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.GetIncidentType`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get incident type details
```
// Get incident type details returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTypeResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncidentType", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentTypeResponse result = apiInstance.getIncidentType("incident_type_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getIncidentType");
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

#####  Get incident type details
```
// Get incident type details returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncidentType", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api.get_incident_type("incident_type_id".to_string()).await;
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

#####  Get incident type details
```
/**
 * Get incident type details returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncidentType"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

const params: v2.IncidentsApiGetIncidentTypeRequest = {
  incidentTypeId: "incident_type_id",
};

apiInstance
  .getIncidentType(params)
  .then((data: v2.IncidentTypeResponse) => {
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
## [Update an incident type](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-type)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-type-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PATCH https://api.ap1.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.ap2.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.datadoghq.eu/api/v2/incidents/config/types/{incident_type_id}https://api.ddog-gov.com/api/v2/incidents/config/types/{incident_type_id}https://api.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.us3.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.us5.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}
### Overview
Update an incident type. This endpoint requires the `incident_settings_write` permission.
OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_type_id [_required_]
string
The UUID of the incident type.
### Request
#### Body Data (required)
Incident type payload.
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Incident type data for a patch request.
attributes [_required_]
object
Incident type's attributes for updates.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
When true, this incident type will be used as the default type when an incident type is not specified.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "attributes": {
      "name": "Security Incident-updated"
    },
    "type": "incident_types"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentType-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentType-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentType-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentType-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentType-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentType-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Incident type response data.
Field
Type
Description
data [_required_]
object
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "attributes": {
      "createdAt": "2019-09-19T10:00:00.000Z",
      "createdBy": "00000000-0000-0000-0000-000000000000",
      "description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.",
      "is_default": false,
      "lastModifiedBy": "00000000-0000-0000-0000-000000000000",
      "modifiedAt": "2019-09-19T10:00:00.000Z",
      "name": "Security Incident",
      "prefix": "IR"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "google_meet_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "google_meet_configurations"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "microsoft_teams_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "microsoft_teams_configurations"
        }
      },
      "zoom_configuration": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "zoom_configurations"
        }
      }
    },
    "type": "incident_types"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Update an incident type returns "OK" response
Copy
```
                          # Path parameters  
export incident_type_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/types/${incident_type_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "attributes": {
      "name": "Security Incident-updated"
    },
    "type": "incident_types"
  }
}
EOF  

                        
```

#####  Update an incident type returns "OK" response
```
// Update an incident type returns "OK" response

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
	// there is a valid "incident_type" in the system
	IncidentTypeDataID := os.Getenv("INCIDENT_TYPE_DATA_ID")

	body := datadogV2.IncidentTypePatchRequest{
		Data: datadogV2.IncidentTypePatchData{
			Id: IncidentTypeDataID,
			Attributes: datadogV2.IncidentTypeUpdateAttributes{
				Name: datadog.PtrString("Security Incident-updated"),
			},
			Type: datadogV2.INCIDENTTYPETYPE_INCIDENT_TYPES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncidentType", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncidentType(ctx, IncidentTypeDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncidentType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncidentType`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update an incident type returns "OK" response
```
// Update an incident type returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentTypePatchData;
import com.datadog.api.client.v2.model.IncidentTypePatchRequest;
import com.datadog.api.client.v2.model.IncidentTypeResponse;
import com.datadog.api.client.v2.model.IncidentTypeType;
import com.datadog.api.client.v2.model.IncidentTypeUpdateAttributes;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncidentType", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident_type" in the system
    String INCIDENT_TYPE_DATA_ATTRIBUTES_NAME = System.getenv("INCIDENT_TYPE_DATA_ATTRIBUTES_NAME");
    String INCIDENT_TYPE_DATA_ID = System.getenv("INCIDENT_TYPE_DATA_ID");

    IncidentTypePatchRequest body =
        new IncidentTypePatchRequest()
            .data(
                new IncidentTypePatchData()
                    .id(INCIDENT_TYPE_DATA_ID)
                    .attributes(
                        new IncidentTypeUpdateAttributes().name("Security Incident-updated"))
                    .type(IncidentTypeType.INCIDENT_TYPES));

    try {
      IncidentTypeResponse result = apiInstance.updateIncidentType(INCIDENT_TYPE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncidentType");
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

#####  Update an incident type returns "OK" response
```
"""
Update an incident type returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type_patch_data import IncidentTypePatchData
from datadog_api_client.v2.model.incident_type_patch_request import IncidentTypePatchRequest
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.incident_type_update_attributes import IncidentTypeUpdateAttributes

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ATTRIBUTES_NAME = environ["INCIDENT_TYPE_DATA_ATTRIBUTES_NAME"]
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

body = IncidentTypePatchRequest(
    data=IncidentTypePatchData(
        id=INCIDENT_TYPE_DATA_ID,
        attributes=IncidentTypeUpdateAttributes(
            name="Security Incident-updated",
        ),
        type=IncidentTypeType.INCIDENT_TYPES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_type(incident_type_id=INCIDENT_TYPE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update an incident type returns "OK" response
```
# Update an incident type returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident_type".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ATTRIBUTES_NAME = ENV["INCIDENT_TYPE_DATA_ATTRIBUTES_NAME"]
INCIDENT_TYPE_DATA_ID = ENV["INCIDENT_TYPE_DATA_ID"]

body = DatadogAPIClient::V2::IncidentTypePatchRequest.new({
  data: DatadogAPIClient::V2::IncidentTypePatchData.new({
    id: INCIDENT_TYPE_DATA_ID,
    attributes: DatadogAPIClient::V2::IncidentTypeUpdateAttributes.new({
      name: "Security Incident-updated",
    }),
    type: DatadogAPIClient::V2::IncidentTypeType::INCIDENT_TYPES,
  }),
})
p api_instance.update_incident_type(INCIDENT_TYPE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update an incident type returns "OK" response
```
// Update an incident type returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::IncidentTypePatchData;
use datadog_api_client::datadogV2::model::IncidentTypePatchRequest;
use datadog_api_client::datadogV2::model::IncidentTypeType;
use datadog_api_client::datadogV2::model::IncidentTypeUpdateAttributes;

#[tokio::main]
async fn main() {
    // there is a valid "incident_type" in the system
    let incident_type_data_id = std::env::var("INCIDENT_TYPE_DATA_ID").unwrap();
    let body = IncidentTypePatchRequest::new(IncidentTypePatchData::new(
        IncidentTypeUpdateAttributes::new().name("Security Incident-updated".to_string()),
        incident_type_data_id.clone(),
        IncidentTypeType::INCIDENT_TYPES,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncidentType", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident_type(incident_type_data_id.clone(), body)
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

#####  Update an incident type returns "OK" response
```
/**
 * Update an incident type returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncidentType"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident_type" in the system
const INCIDENT_TYPE_DATA_ID = process.env.INCIDENT_TYPE_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentTypeRequest = {
  body: {
    data: {
      id: INCIDENT_TYPE_DATA_ID,
      attributes: {
        name: "Security Incident-updated",
      },
      type: "incident_types",
    },
  },
  incidentTypeId: INCIDENT_TYPE_DATA_ID,
};

apiInstance
  .updateIncidentType(params)
  .then((data: v2.IncidentTypeResponse) => {
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
## [Delete an incident type](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-type)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-type-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.ap2.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.datadoghq.eu/api/v2/incidents/config/types/{incident_type_id}https://api.ddog-gov.com/api/v2/incidents/config/types/{incident_type_id}https://api.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.us3.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}https://api.us5.datadoghq.com/api/v2/incidents/config/types/{incident_type_id}
### Overview
Delete an incident type. This endpoint requires the `incident_settings_write` permission.
OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_type_id [_required_]
string
The UUID of the incident type.
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentType-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentType-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentType-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentType-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentType-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentType-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Delete an incident type
Copy
```
                  # Path parameters  
export incident_type_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/types/${incident_type_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an incident type
```
"""
Delete an incident type returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_type(
        incident_type_id=INCIDENT_TYPE_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an incident type
```
# Delete an incident type returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_type".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = ENV["INCIDENT_TYPE_DATA_ID"]
api_instance.delete_incident_type(INCIDENT_TYPE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an incident type
```
// Delete an incident type returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "incident_type" in the system
	IncidentTypeDataID := os.Getenv("INCIDENT_TYPE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncidentType", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	r, err := api.DeleteIncidentType(ctx, IncidentTypeDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.DeleteIncidentType`: %v\n", err)
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

#####  Delete an incident type
```
// Delete an incident type returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentType", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident_type" in the system
    String INCIDENT_TYPE_DATA_ID = System.getenv("INCIDENT_TYPE_DATA_ID");

    try {
      apiInstance.deleteIncidentType(INCIDENT_TYPE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#deleteIncidentType");
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

#####  Delete an incident type
```
// Delete an incident type returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "incident_type" in the system
    let incident_type_data_id = std::env::var("INCIDENT_TYPE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentType", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .delete_incident_type(incident_type_data_id.clone())
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

#####  Delete an incident type
```
/**
 * Delete an incident type returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentType"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident_type" in the system
const INCIDENT_TYPE_DATA_ID = process.env.INCIDENT_TYPE_DATA_ID as string;

const params: v2.IncidentsApiDeleteIncidentTypeRequest = {
  incidentTypeId: INCIDENT_TYPE_DATA_ID,
};

apiInstance
  .deleteIncidentType(params)
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
## [List incident notification templates](https://docs.datadoghq.com/api/latest/incidents/#list-incident-notification-templates)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#list-incident-notification-templates-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.ap2.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.datadoghq.eu/api/v2/incidents/config/notification-templateshttps://api.ddog-gov.com/api/v2/incidents/config/notification-templateshttps://api.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.us3.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates
### Overview
Lists all notification templates. Optionally filter by incident type. This endpoint requires the `incident_notification_settings_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
filter[incident-type]
string
Optional incident type ID filter.
include
string
Comma-separated list of relationships to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationTemplates-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationTemplates-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationTemplates-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationTemplates-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationTemplates-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationTemplates-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with notification templates.
Field
Type
Description
data [_required_]
[object]
The `NotificationTemplateArray` `data`.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
meta
object
Response metadata.
page
object
Pagination metadata.
total_count
int64
Total number of notification templates.
total_filtered_count
int64
Total number of notification templates matching the filter.
```
{
  "data": [
    {
      "attributes": {
        "category": "alert",
        "content": "An incident has been declared.\n\nTitle: {{incident.title}}\nSeverity: {{incident.severity}}\nAffected Services: {{incident.services}}\nStatus: {{incident.state}}\n\nPlease join the incident channel for updates.",
        "created": "2025-01-15T10:30:00Z",
        "modified": "2025-01-15T14:45:00Z",
        "name": "Incident Alert Template",
        "subject": "{{incident.severity}} Incident: {{incident.title}}"
      },
      "id": "00000000-0000-0000-0000-000000000001",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "incident_type": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "incident_types"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "notification_templates"
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
    "page": {
      "total_count": 42,
      "total_filtered_count": 15
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  List incident notification templates
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List incident notification templates
```
"""
List incident notification templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["list_incident_notification_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_notification_templates()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List incident notification templates
```
# List incident notification templates returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_notification_templates".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.list_incident_notification_templates()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List incident notification templates
```
// List incident notification templates returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListIncidentNotificationTemplates", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidentNotificationTemplates(ctx, *datadogV2.NewListIncidentNotificationTemplatesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidentNotificationTemplates`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidentNotificationTemplates`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List incident notification templates
```
// List incident notification templates returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentNotificationTemplates", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentNotificationTemplateArray result = apiInstance.listIncidentNotificationTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidentNotificationTemplates");
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

#####  List incident notification templates
```
// List incident notification templates returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::ListIncidentNotificationTemplatesOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentNotificationTemplates", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .list_incident_notification_templates(
            ListIncidentNotificationTemplatesOptionalParams::default(),
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

#####  List incident notification templates
```
/**
 * List incident notification templates returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentNotificationTemplates"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

apiInstance
  .listIncidentNotificationTemplates()
  .then((data: v2.IncidentNotificationTemplateArray) => {
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
## [Create incident notification template](https://docs.datadoghq.com/api/latest/incidents/#create-incident-notification-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-incident-notification-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.ap2.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.datadoghq.eu/api/v2/incidents/config/notification-templateshttps://api.ddog-gov.com/api/v2/incidents/config/notification-templateshttps://api.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.us3.datadoghq.com/api/v2/incidents/config/notification-templateshttps://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates
### Overview
Creates a new notification template. This endpoint requires the `incident_notification_settings_write` permission.
OAuth apps require the `incident_notification_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Notification template data for a create request.
attributes [_required_]
object
The attributes for creating a notification template.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
relationships
object
The definition of `NotificationTemplateCreateDataRelationships` object.
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
```
{
  "data": {
    "attributes": {
      "category": "alert",
      "content": "An incident has been declared.\n\nTitle: Sample Incident Title\nSeverity: SEV-2\nAffected Services: web-service, database-service\nStatus: active\n\nPlease join the incident channel for updates.",
      "name": "Example-Incident",
      "subject": "SEV-2 Incident: Sample Incident Title"
    },
    "relationships": {
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      }
    },
    "type": "notification_templates"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationTemplate-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationTemplate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationTemplate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationTemplate-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationTemplate-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a notification template.
Field
Type
Description
data [_required_]
object
Notification template data from a response.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "attributes": {
      "category": "alert",
      "content": "An incident has been declared.\n\nTitle: {{incident.title}}\nSeverity: {{incident.severity}}\nAffected Services: {{incident.services}}\nStatus: {{incident.state}}\n\nPlease join the incident channel for updates.",
      "created": "2025-01-15T10:30:00Z",
      "modified": "2025-01-15T14:45:00Z",
      "name": "Incident Alert Template",
      "subject": "{{incident.severity}} Incident: {{incident.title}}"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "notification_templates"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Create incident notification template returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "category": "alert",
      "content": "An incident has been declared.\n\nTitle: Sample Incident Title\nSeverity: SEV-2\nAffected Services: web-service, database-service\nStatus: active\n\nPlease join the incident channel for updates.",
      "name": "Example-Incident",
      "subject": "SEV-2 Incident: Sample Incident Title"
    },
    "relationships": {
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      }
    },
    "type": "notification_templates"
  }
}
EOF  

                        
```

#####  Create incident notification template returns "Created" response
```
// Create incident notification template returns "Created" response

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
	// there is a valid "incident_type" in the system
	IncidentTypeDataID := os.Getenv("INCIDENT_TYPE_DATA_ID")

	body := datadogV2.CreateIncidentNotificationTemplateRequest{
		Data: datadogV2.IncidentNotificationTemplateCreateData{
			Attributes: datadogV2.IncidentNotificationTemplateCreateAttributes{
				Category: "alert",
				Content: `An incident has been declared.

Title: Sample Incident Title
Severity: SEV-2
Affected Services: web-service, database-service
Status: active

Please join the incident channel for updates.`,
				Name:    "Example-Incident",
				Subject: "SEV-2 Incident: Sample Incident Title",
			},
			Relationships: &datadogV2.IncidentNotificationTemplateCreateDataRelationships{
				IncidentType: &datadogV2.RelationshipToIncidentType{
					Data: datadogV2.RelationshipToIncidentTypeData{
						Id:   IncidentTypeDataID,
						Type: datadogV2.INCIDENTTYPETYPE_INCIDENT_TYPES,
					},
				},
			},
			Type: datadogV2.INCIDENTNOTIFICATIONTEMPLATETYPE_NOTIFICATION_TEMPLATES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncidentNotificationTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.CreateIncidentNotificationTemplate(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.CreateIncidentNotificationTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.CreateIncidentNotificationTemplate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create incident notification template returns "Created" response
```
// Create incident notification template returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.CreateIncidentNotificationTemplateRequest;
import com.datadog.api.client.v2.model.IncidentNotificationTemplate;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateCreateAttributes;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateCreateData;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateCreateDataRelationships;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateType;
import com.datadog.api.client.v2.model.IncidentTypeType;
import com.datadog.api.client.v2.model.RelationshipToIncidentType;
import com.datadog.api.client.v2.model.RelationshipToIncidentTypeData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentNotificationTemplate", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident_type" in the system
    String INCIDENT_TYPE_DATA_ID = System.getenv("INCIDENT_TYPE_DATA_ID");

    CreateIncidentNotificationTemplateRequest body =
        new CreateIncidentNotificationTemplateRequest()
            .data(
                new IncidentNotificationTemplateCreateData()
                    .attributes(
                        new IncidentNotificationTemplateCreateAttributes()
                            .category("alert")
                            .content(
                                """
An incident has been declared.

Title: Sample Incident Title
Severity: SEV-2
Affected Services: web-service, database-service
Status: active

Please join the incident channel for updates.
""")
                            .name("Example-Incident")
                            .subject("SEV-2 Incident: Sample Incident Title"))
                    .relationships(
                        new IncidentNotificationTemplateCreateDataRelationships()
                            .incidentType(
                                new RelationshipToIncidentType()
                                    .data(
                                        new RelationshipToIncidentTypeData()
                                            .id(INCIDENT_TYPE_DATA_ID)
                                            .type(IncidentTypeType.INCIDENT_TYPES))))
                    .type(IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES));

    try {
      IncidentNotificationTemplate result = apiInstance.createIncidentNotificationTemplate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#createIncidentNotificationTemplate");
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

#####  Create incident notification template returns "Created" response
```
"""
Create incident notification template returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.create_incident_notification_template_request import (
    CreateIncidentNotificationTemplateRequest,
)
from datadog_api_client.v2.model.incident_notification_template_create_attributes import (
    IncidentNotificationTemplateCreateAttributes,
)
from datadog_api_client.v2.model.incident_notification_template_create_data import (
    IncidentNotificationTemplateCreateData,
)
from datadog_api_client.v2.model.incident_notification_template_create_data_relationships import (
    IncidentNotificationTemplateCreateDataRelationships,
)
from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
from datadog_api_client.v2.model.relationship_to_incident_type_data import RelationshipToIncidentTypeData

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

body = CreateIncidentNotificationTemplateRequest(
    data=IncidentNotificationTemplateCreateData(
        attributes=IncidentNotificationTemplateCreateAttributes(
            category="alert",
            content="An incident has been declared.\n\nTitle: Sample Incident Title\nSeverity: SEV-2\nAffected Services: web-service, database-service\nStatus: active\n\nPlease join the incident channel for updates.",
            name="Example-Incident",
            subject="SEV-2 Incident: Sample Incident Title",
        ),
        relationships=IncidentNotificationTemplateCreateDataRelationships(
            incident_type=RelationshipToIncidentType(
                data=RelationshipToIncidentTypeData(
                    id=INCIDENT_TYPE_DATA_ID,
                    type=IncidentTypeType.INCIDENT_TYPES,
                ),
            ),
        ),
        type=IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_notification_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_notification_template(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create incident notification template returns "Created" response
```
# Create incident notification template returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_notification_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = ENV["INCIDENT_TYPE_DATA_ID"]

body = DatadogAPIClient::V2::CreateIncidentNotificationTemplateRequest.new({
  data: DatadogAPIClient::V2::IncidentNotificationTemplateCreateData.new({
    attributes: DatadogAPIClient::V2::IncidentNotificationTemplateCreateAttributes.new({
      category: "alert",
      content: 'An incident has been declared.\n\nTitle: Sample Incident Title\nSeverity: SEV-2\nAffected Services: web-service, database-service\nStatus: active\n\nPlease join the incident channel for updates.',
      name: "Example-Incident",
      subject: "SEV-2 Incident: Sample Incident Title",
    }),
    relationships: DatadogAPIClient::V2::IncidentNotificationTemplateCreateDataRelationships.new({
      incident_type: DatadogAPIClient::V2::RelationshipToIncidentType.new({
        data: DatadogAPIClient::V2::RelationshipToIncidentTypeData.new({
          id: INCIDENT_TYPE_DATA_ID,
          type: DatadogAPIClient::V2::IncidentTypeType::INCIDENT_TYPES,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::IncidentNotificationTemplateType::NOTIFICATION_TEMPLATES,
  }),
})
p api_instance.create_incident_notification_template(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create incident notification template returns "Created" response
```
// Create incident notification template returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::CreateIncidentNotificationTemplateRequest;
use datadog_api_client::datadogV2::model::IncidentNotificationTemplateCreateAttributes;
use datadog_api_client::datadogV2::model::IncidentNotificationTemplateCreateData;
use datadog_api_client::datadogV2::model::IncidentNotificationTemplateCreateDataRelationships;
use datadog_api_client::datadogV2::model::IncidentNotificationTemplateType;
use datadog_api_client::datadogV2::model::IncidentTypeType;
use datadog_api_client::datadogV2::model::RelationshipToIncidentType;
use datadog_api_client::datadogV2::model::RelationshipToIncidentTypeData;

#[tokio::main]
async fn main() {
    // there is a valid "incident_type" in the system
    let incident_type_data_id = std::env::var("INCIDENT_TYPE_DATA_ID").unwrap();
    let body = CreateIncidentNotificationTemplateRequest::new(
        IncidentNotificationTemplateCreateData::new(
            IncidentNotificationTemplateCreateAttributes::new(
                "alert".to_string(),
                r#"An incident has been declared.

Title: Sample Incident Title
Severity: SEV-2
Affected Services: web-service, database-service
Status: active

Please join the incident channel for updates."#
                    .to_string(),
                "Example-Incident".to_string(),
                "SEV-2 Incident: Sample Incident Title".to_string(),
            ),
            IncidentNotificationTemplateType::NOTIFICATION_TEMPLATES,
        )
        .relationships(
            IncidentNotificationTemplateCreateDataRelationships::new().incident_type(
                RelationshipToIncidentType::new(RelationshipToIncidentTypeData::new(
                    incident_type_data_id.clone(),
                    IncidentTypeType::INCIDENT_TYPES,
                )),
            ),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentNotificationTemplate", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api.create_incident_notification_template(body).await;
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

#####  Create incident notification template returns "Created" response
```
/**
 * Create incident notification template returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentNotificationTemplate"] =
  true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident_type" in the system
const INCIDENT_TYPE_DATA_ID = process.env.INCIDENT_TYPE_DATA_ID as string;

const params: v2.IncidentsApiCreateIncidentNotificationTemplateRequest = {
  body: {
    data: {
      attributes: {
        category: "alert",
        content:
          "An incident has been declared.\n\nTitle: Sample Incident Title\nSeverity: SEV-2\nAffected Services: web-service, database-service\nStatus: active\n\nPlease join the incident channel for updates.",
        name: "Example-Incident",
        subject: "SEV-2 Incident: Sample Incident Title",
      },
      relationships: {
        incidentType: {
          data: {
            id: INCIDENT_TYPE_DATA_ID,
            type: "incident_types",
          },
        },
      },
      type: "notification_templates",
    },
  },
};

apiInstance
  .createIncidentNotificationTemplate(params)
  .then((data: v2.IncidentNotificationTemplate) => {
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
## [Get incident notification template](https://docs.datadoghq.com/api/latest/incidents/#get-incident-notification-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-incident-notification-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.ap2.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.datadoghq.eu/api/v2/incidents/config/notification-templates/{id}https://api.ddog-gov.com/api/v2/incidents/config/notification-templates/{id}https://api.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.us3.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates/{id}
### Overview
Retrieves a specific notification template by its ID. This endpoint requires any of the following permissions:
* `incident_settings_read`
* `incident_write`
* `incident_read`
  

OAuth apps require the `incident_read, incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the notification template.
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of relationships to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationTemplate-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationTemplate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationTemplate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationTemplate-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationTemplate-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a notification template.
Field
Type
Description
data [_required_]
object
Notification template data from a response.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "attributes": {
      "category": "alert",
      "content": "An incident has been declared.\n\nTitle: {{incident.title}}\nSeverity: {{incident.severity}}\nAffected Services: {{incident.services}}\nStatus: {{incident.state}}\n\nPlease join the incident channel for updates.",
      "created": "2025-01-15T10:30:00Z",
      "modified": "2025-01-15T14:45:00Z",
      "name": "Incident Alert Template",
      "subject": "{{incident.severity}} Incident: {{incident.title}}"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "notification_templates"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get incident notification template
Copy
```
                  # Path parameters  
export id="00000000-0000-0000-0000-000000000001"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get incident notification template
```
"""
Get incident notification template returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "notification_template" in the system
NOTIFICATION_TEMPLATE_DATA_ID = environ["NOTIFICATION_TEMPLATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident_notification_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_notification_template(
        id=NOTIFICATION_TEMPLATE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get incident notification template
```
# Get incident notification template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident_notification_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "notification_template" in the system
NOTIFICATION_TEMPLATE_DATA_ID = ENV["NOTIFICATION_TEMPLATE_DATA_ID"]
p api_instance.get_incident_notification_template(NOTIFICATION_TEMPLATE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get incident notification template
```
// Get incident notification template returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "notification_template" in the system
	NotificationTemplateDataID := uuid.MustParse(os.Getenv("NOTIFICATION_TEMPLATE_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetIncidentNotificationTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.GetIncidentNotificationTemplate(ctx, NotificationTemplateDataID, *datadogV2.NewGetIncidentNotificationTemplateOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.GetIncidentNotificationTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.GetIncidentNotificationTemplate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get incident notification template
```
// Get incident notification template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentNotificationTemplate;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncidentNotificationTemplate", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "notification_template" in the system
    UUID NOTIFICATION_TEMPLATE_DATA_ID = null;
    try {
      NOTIFICATION_TEMPLATE_DATA_ID =
          UUID.fromString(System.getenv("NOTIFICATION_TEMPLATE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      IncidentNotificationTemplate result =
          apiInstance.getIncidentNotificationTemplate(NOTIFICATION_TEMPLATE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getIncidentNotificationTemplate");
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

#####  Get incident notification template
```
// Get incident notification template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::GetIncidentNotificationTemplateOptionalParams;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "notification_template" in the system
    let notification_template_data_id =
        uuid::Uuid::parse_str(&std::env::var("NOTIFICATION_TEMPLATE_DATA_ID").unwrap())
            .expect("Invalid UUID");
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncidentNotificationTemplate", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .get_incident_notification_template(
            notification_template_data_id.clone(),
            GetIncidentNotificationTemplateOptionalParams::default(),
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

#####  Get incident notification template
```
/**
 * Get incident notification template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncidentNotificationTemplate"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "notification_template" in the system
const NOTIFICATION_TEMPLATE_DATA_ID = process.env
  .NOTIFICATION_TEMPLATE_DATA_ID as string;

const params: v2.IncidentsApiGetIncidentNotificationTemplateRequest = {
  id: NOTIFICATION_TEMPLATE_DATA_ID,
};

apiInstance
  .getIncidentNotificationTemplate(params)
  .then((data: v2.IncidentNotificationTemplate) => {
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
## [Update incident notification template](https://docs.datadoghq.com/api/latest/incidents/#update-incident-notification-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#update-incident-notification-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PATCH https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.ap2.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.datadoghq.eu/api/v2/incidents/config/notification-templates/{id}https://api.ddog-gov.com/api/v2/incidents/config/notification-templates/{id}https://api.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.us3.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates/{id}
### Overview
Updates an existing notification template’s attributes. This endpoint requires the `incident_notification_settings_write` permission.
OAuth apps require the `incident_notification_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the notification template.
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of relationships to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Notification template data for an update request.
attributes
object
The attributes to update on a notification template.
category
string
The category of the notification template.
content
string
The content body of the notification template.
name
string
The name of the notification template.
subject
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
```
{
  "data": {
    "attributes": {
      "category": "update",
      "content": "Incident Status Update:\n\nTitle: Sample Incident Title\nNew Status: resolved\nSeverity: SEV-2\nServices: web-service, database-service\nCommander: John Doe\n\nFor more details, visit the incident page.",
      "name": "Example-Incident",
      "subject": "Incident Update: Sample Incident Title - resolved"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "type": "notification_templates"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationTemplate-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationTemplate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationTemplate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationTemplate-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationTemplate-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a notification template.
Field
Type
Description
data [_required_]
object
Notification template data from a response.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
```
{
  "data": {
    "attributes": {
      "category": "alert",
      "content": "An incident has been declared.\n\nTitle: {{incident.title}}\nSeverity: {{incident.severity}}\nAffected Services: {{incident.services}}\nStatus: {{incident.state}}\n\nPlease join the incident channel for updates.",
      "created": "2025-01-15T10:30:00Z",
      "modified": "2025-01-15T14:45:00Z",
      "name": "Incident Alert Template",
      "subject": "{{incident.severity}} Incident: {{incident.title}}"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "notification_templates"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Update incident notification template returns "OK" response
Copy
```
                          # Path parameters  
export id="00000000-0000-0000-0000-000000000001"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "category": "update",
      "content": "Incident Status Update:\n\nTitle: Sample Incident Title\nNew Status: resolved\nSeverity: SEV-2\nServices: web-service, database-service\nCommander: John Doe\n\nFor more details, visit the incident page.",
      "name": "Example-Incident",
      "subject": "Incident Update: Sample Incident Title - resolved"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "type": "notification_templates"
  }
}
EOF  

                        
```

#####  Update incident notification template returns "OK" response
```
// Update incident notification template returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "notification_template" in the system
	NotificationTemplateDataID := uuid.MustParse(os.Getenv("NOTIFICATION_TEMPLATE_DATA_ID"))

	body := datadogV2.PatchIncidentNotificationTemplateRequest{
		Data: datadogV2.IncidentNotificationTemplateUpdateData{
			Attributes: &datadogV2.IncidentNotificationTemplateUpdateAttributes{
				Category: datadog.PtrString("update"),
				Content: datadog.PtrString(`Incident Status Update:

Title: Sample Incident Title
New Status: resolved
Severity: SEV-2
Services: web-service, database-service
Commander: John Doe

For more details, visit the incident page.`),
				Name:    datadog.PtrString("Example-Incident"),
				Subject: datadog.PtrString("Incident Update: Sample Incident Title - resolved"),
			},
			Id:   NotificationTemplateDataID,
			Type: datadogV2.INCIDENTNOTIFICATIONTEMPLATETYPE_NOTIFICATION_TEMPLATES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncidentNotificationTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncidentNotificationTemplate(ctx, NotificationTemplateDataID, body, *datadogV2.NewUpdateIncidentNotificationTemplateOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncidentNotificationTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncidentNotificationTemplate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update incident notification template returns "OK" response
```
// Update incident notification template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentNotificationTemplate;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateType;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateUpdateAttributes;
import com.datadog.api.client.v2.model.IncidentNotificationTemplateUpdateData;
import com.datadog.api.client.v2.model.PatchIncidentNotificationTemplateRequest;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncidentNotificationTemplate", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "notification_template" in the system
    UUID NOTIFICATION_TEMPLATE_DATA_ID = null;
    try {
      NOTIFICATION_TEMPLATE_DATA_ID =
          UUID.fromString(System.getenv("NOTIFICATION_TEMPLATE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    PatchIncidentNotificationTemplateRequest body =
        new PatchIncidentNotificationTemplateRequest()
            .data(
                new IncidentNotificationTemplateUpdateData()
                    .attributes(
                        new IncidentNotificationTemplateUpdateAttributes()
                            .category("update")
                            .content(
                                """
Incident Status Update:

Title: Sample Incident Title
New Status: resolved
Severity: SEV-2
Services: web-service, database-service
Commander: John Doe

For more details, visit the incident page.
""")
                            .name("Example-Incident")
                            .subject("Incident Update: Sample Incident Title - resolved"))
                    .id(NOTIFICATION_TEMPLATE_DATA_ID)
                    .type(IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES));

    try {
      IncidentNotificationTemplate result =
          apiInstance.updateIncidentNotificationTemplate(NOTIFICATION_TEMPLATE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncidentNotificationTemplate");
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

#####  Update incident notification template returns "OK" response
```
"""
Update incident notification template returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType
from datadog_api_client.v2.model.incident_notification_template_update_attributes import (
    IncidentNotificationTemplateUpdateAttributes,
)
from datadog_api_client.v2.model.incident_notification_template_update_data import (
    IncidentNotificationTemplateUpdateData,
)
from datadog_api_client.v2.model.patch_incident_notification_template_request import (
    PatchIncidentNotificationTemplateRequest,
)

# there is a valid "notification_template" in the system
NOTIFICATION_TEMPLATE_DATA_ID = environ["NOTIFICATION_TEMPLATE_DATA_ID"]

body = PatchIncidentNotificationTemplateRequest(
    data=IncidentNotificationTemplateUpdateData(
        attributes=IncidentNotificationTemplateUpdateAttributes(
            category="update",
            content="Incident Status Update:\n\nTitle: Sample Incident Title\nNew Status: resolved\nSeverity: SEV-2\nServices: web-service, database-service\nCommander: John Doe\n\nFor more details, visit the incident page.",
            name="Example-Incident",
            subject="Incident Update: Sample Incident Title - resolved",
        ),
        id=NOTIFICATION_TEMPLATE_DATA_ID,
        type=IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_notification_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_notification_template(id=NOTIFICATION_TEMPLATE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update incident notification template returns "OK" response
```
# Update incident notification template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident_notification_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "notification_template" in the system
NOTIFICATION_TEMPLATE_DATA_ID = ENV["NOTIFICATION_TEMPLATE_DATA_ID"]

body = DatadogAPIClient::V2::PatchIncidentNotificationTemplateRequest.new({
  data: DatadogAPIClient::V2::IncidentNotificationTemplateUpdateData.new({
    attributes: DatadogAPIClient::V2::IncidentNotificationTemplateUpdateAttributes.new({
      category: "update",
      content: 'Incident Status Update:\n\nTitle: Sample Incident Title\nNew Status: resolved\nSeverity: SEV-2\nServices: web-service, database-service\nCommander: John Doe\n\nFor more details, visit the incident page.',
      name: "Example-Incident",
      subject: "Incident Update: Sample Incident Title - resolved",
    }),
    id: NOTIFICATION_TEMPLATE_DATA_ID,
    type: DatadogAPIClient::V2::IncidentNotificationTemplateType::NOTIFICATION_TEMPLATES,
  }),
})
p api_instance.update_incident_notification_template(NOTIFICATION_TEMPLATE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update incident notification template returns "OK" response
```
// Update incident notification template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::UpdateIncidentNotificationTemplateOptionalParams;
use datadog_api_client::datadogV2::model::IncidentNotificationTemplateType;
use datadog_api_client::datadogV2::model::IncidentNotificationTemplateUpdateAttributes;
use datadog_api_client::datadogV2::model::IncidentNotificationTemplateUpdateData;
use datadog_api_client::datadogV2::model::PatchIncidentNotificationTemplateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "notification_template" in the system
    let notification_template_data_id =
        uuid::Uuid::parse_str(&std::env::var("NOTIFICATION_TEMPLATE_DATA_ID").unwrap())
            .expect("Invalid UUID");
    let body = PatchIncidentNotificationTemplateRequest::new(
        IncidentNotificationTemplateUpdateData::new(
            notification_template_data_id.clone(),
            IncidentNotificationTemplateType::NOTIFICATION_TEMPLATES,
        )
        .attributes(
            IncidentNotificationTemplateUpdateAttributes::new()
                .category("update".to_string())
                .content(
                    r#"Incident Status Update:

Title: Sample Incident Title
New Status: resolved
Severity: SEV-2
Services: web-service, database-service
Commander: John Doe

For more details, visit the incident page."#
                        .to_string(),
                )
                .name("Example-Incident".to_string())
                .subject("Incident Update: Sample Incident Title - resolved".to_string()),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncidentNotificationTemplate", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident_notification_template(
            notification_template_data_id.clone(),
            body,
            UpdateIncidentNotificationTemplateOptionalParams::default(),
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

#####  Update incident notification template returns "OK" response
```
/**
 * Update incident notification template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncidentNotificationTemplate"] =
  true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "notification_template" in the system
const NOTIFICATION_TEMPLATE_DATA_ID = process.env
  .NOTIFICATION_TEMPLATE_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentNotificationTemplateRequest = {
  body: {
    data: {
      attributes: {
        category: "update",
        content:
          "Incident Status Update:\n\nTitle: Sample Incident Title\nNew Status: resolved\nSeverity: SEV-2\nServices: web-service, database-service\nCommander: John Doe\n\nFor more details, visit the incident page.",
        name: "Example-Incident",
        subject: "Incident Update: Sample Incident Title - resolved",
      },
      id: NOTIFICATION_TEMPLATE_DATA_ID,
      type: "notification_templates",
    },
  },
  id: NOTIFICATION_TEMPLATE_DATA_ID,
};

apiInstance
  .updateIncidentNotificationTemplate(params)
  .then((data: v2.IncidentNotificationTemplate) => {
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
## [Delete a notification template](https://docs.datadoghq.com/api/latest/incidents/#delete-a-notification-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-a-notification-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.ap2.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.datadoghq.eu/api/v2/incidents/config/notification-templates/{id}https://api.ddog-gov.com/api/v2/incidents/config/notification-templates/{id}https://api.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.us3.datadoghq.com/api/v2/incidents/config/notification-templates/{id}https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates/{id}
### Overview
Deletes a notification template by its ID. This endpoint requires the `incident_notification_settings_write` permission.
OAuth apps require the `incident_notification_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the notification template.
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of relationships to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationTemplate-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationTemplate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationTemplate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationTemplate-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationTemplate-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Delete a notification template
Copy
```
                  # Path parameters  
export id="00000000-0000-0000-0000-000000000001"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-templates/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a notification template
```
"""
Delete a notification template returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_incident_notification_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_notification_template(
        id=UUID("00000000-0000-0000-0000-000000000001"),
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a notification template
```
# Delete a notification template returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_notification_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
api_instance.delete_incident_notification_template("00000000-0000-0000-0000-000000000001")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a notification template
```
// Delete a notification template returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncidentNotificationTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	r, err := api.DeleteIncidentNotificationTemplate(ctx, uuid.MustParse("00000000-0000-0000-0000-000000000001"), *datadogV2.NewDeleteIncidentNotificationTemplateOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.DeleteIncidentNotificationTemplate`: %v\n", err)
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

#####  Delete a notification template
```
// Delete a notification template returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentNotificationTemplate", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      apiInstance.deleteIncidentNotificationTemplate(
          UUID.fromString("00000000-0000-0000-0000-000000000001"));
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#deleteIncidentNotificationTemplate");
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

#####  Delete a notification template
```
// Delete a notification template returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::DeleteIncidentNotificationTemplateOptionalParams;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentNotificationTemplate", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .delete_incident_notification_template(
            Uuid::parse_str("00000000-0000-0000-0000-000000000001").expect("invalid UUID"),
            DeleteIncidentNotificationTemplateOptionalParams::default(),
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

#####  Delete a notification template
```
/**
 * Delete a notification template returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentNotificationTemplate"] =
  true;
const apiInstance = new v2.IncidentsApi(configuration);

const params: v2.IncidentsApiDeleteIncidentNotificationTemplateRequest = {
  id: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .deleteIncidentNotificationTemplate(params)
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
## [List incident notification rules](https://docs.datadoghq.com/api/latest/incidents/#list-incident-notification-rules)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#list-incident-notification-rules-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.ap2.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.datadoghq.eu/api/v2/incidents/config/notification-ruleshttps://api.ddog-gov.com/api/v2/incidents/config/notification-ruleshttps://api.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.us3.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules
### Overview
Lists all notification rules for the organization. Optionally filter by incident type. This endpoint requires the `incident_notification_settings_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of resources to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`, `notification_template`
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationRules-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationRules-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationRules-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationRules-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationRules-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentNotificationRules-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with notification rules.
Field
Type
Description
data [_required_]
[object]
The `NotificationRuleArray` `data`.
attributes
object
The notification rule's attributes.
conditions [_required_]
[object]
The conditions that trigger this notification rule.
field [_required_]
string
The incident field to evaluate
values [_required_]
[string]
The value(s) to compare against. Multiple values are `ORed` together.
created [_required_]
date-time
Timestamp when the notification rule was created.
enabled [_required_]
boolean
Whether the notification rule is enabled.
handles [_required_]
[string]
The notification handles (targets) for this rule.
modified [_required_]
date-time
Timestamp when the notification rule was last modified.
renotify_on
[string]
List of incident fields that trigger re-notification when changed.
trigger [_required_]
string
The trigger event for this notification rule.
visibility [_required_]
enum
The visibility of the notification rule. Allowed enum values: `all,organization,private`
id [_required_]
uuid
The unique identifier of the notification rule.
relationships
object
The notification rule's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
notification_template
object
A relationship reference to a notification template.
data [_required_]
object
The notification template relationship data.
id [_required_]
uuid
The unique identifier of the notification template.
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
type [_required_]
enum
Notification rules resource type. Allowed enum values: `incident_notification_rules`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
Option 3
object
A notification template object for inclusion in other resources.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
meta
object
Response metadata.
pagination
object
Pagination metadata.
next_offset
int64
The offset for the next page of results.
offset
int64
The current offset in the results.
size
int64
The number of results returned per page.
```
{
  "data": [
    {
      "attributes": {
        "conditions": [
          {
            "field": "severity",
            "values": [
              "SEV-1",
              "SEV-2"
            ]
          }
        ],
        "created": "2025-01-15T10:30:00Z",
        "enabled": true,
        "handles": [
          "@team-email@company.com",
          "@slack-channel"
        ],
        "modified": "2025-01-15T14:45:00Z",
        "renotify_on": [
          "status",
          "severity"
        ],
        "trigger": "incident_created_trigger",
        "visibility": "organization"
      },
      "id": "00000000-0000-0000-0000-000000000001",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "incident_type": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "incident_types"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "notification_template": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000001",
            "type": "notification_templates"
          }
        }
      },
      "type": "incident_notification_rules"
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
      "next_offset": 15,
      "offset": 0,
      "size": 15
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  List incident notification rules
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List incident notification rules
```
"""
List incident notification rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["list_incident_notification_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_notification_rules()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List incident notification rules
```
# List incident notification rules returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_notification_rules".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.list_incident_notification_rules()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List incident notification rules
```
// List incident notification rules returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListIncidentNotificationRules", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidentNotificationRules(ctx, *datadogV2.NewListIncidentNotificationRulesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidentNotificationRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidentNotificationRules`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List incident notification rules
```
// List incident notification rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentNotificationRuleArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentNotificationRules", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentNotificationRuleArray result = apiInstance.listIncidentNotificationRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidentNotificationRules");
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

#####  List incident notification rules
```
// List incident notification rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::ListIncidentNotificationRulesOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentNotificationRules", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .list_incident_notification_rules(ListIncidentNotificationRulesOptionalParams::default())
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

#####  List incident notification rules
```
/**
 * List incident notification rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentNotificationRules"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

apiInstance
  .listIncidentNotificationRules()
  .then((data: v2.IncidentNotificationRuleArray) => {
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
## [Create an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-notification-rule-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.ap2.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.datadoghq.eu/api/v2/incidents/config/notification-ruleshttps://api.ddog-gov.com/api/v2/incidents/config/notification-ruleshttps://api.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.us3.datadoghq.com/api/v2/incidents/config/notification-ruleshttps://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules
### Overview
Creates a new notification rule. This endpoint requires the `incident_notification_settings_write` permission.
OAuth apps require the `incident_notification_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Notification rule data for a create request.
attributes [_required_]
object
The attributes for creating a notification rule.
conditions [_required_]
[object]
The conditions that trigger this notification rule.
field [_required_]
string
The incident field to evaluate
values [_required_]
[string]
The value(s) to compare against. Multiple values are `ORed` together.
enabled
boolean
Whether the notification rule is enabled.
handles [_required_]
[string]
The notification handles (targets) for this rule.
renotify_on
[string]
List of incident fields that trigger re-notification when changed.
trigger [_required_]
string
The trigger event for this notification rule.
visibility
enum
The visibility of the notification rule. Allowed enum values: `all,organization,private`
relationships
object
The definition of `NotificationRuleCreateDataRelationships` object.
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
notification_template
object
A relationship reference to a notification template.
data [_required_]
object
The notification template relationship data.
id [_required_]
uuid
The unique identifier of the notification template.
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
type [_required_]
enum
Notification rules resource type. Allowed enum values: `incident_notification_rules`
```
{
  "data": {
    "attributes": {
      "conditions": [
        {
          "field": "severity",
          "values": [
            "SEV-1",
            "SEV-2"
          ]
        }
      ],
      "handles": [
        "@test-email@company.com"
      ],
      "visibility": "organization",
      "trigger": "incident_created_trigger",
      "enabled": true
    },
    "relationships": {
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      }
    },
    "type": "incident_notification_rules"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationRule-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentNotificationRule-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a notification rule.
Field
Type
Description
data [_required_]
object
Notification rule data from a response.
attributes
object
The notification rule's attributes.
conditions [_required_]
[object]
The conditions that trigger this notification rule.
field [_required_]
string
The incident field to evaluate
values [_required_]
[string]
The value(s) to compare against. Multiple values are `ORed` together.
created [_required_]
date-time
Timestamp when the notification rule was created.
enabled [_required_]
boolean
Whether the notification rule is enabled.
handles [_required_]
[string]
The notification handles (targets) for this rule.
modified [_required_]
date-time
Timestamp when the notification rule was last modified.
renotify_on
[string]
List of incident fields that trigger re-notification when changed.
trigger [_required_]
string
The trigger event for this notification rule.
visibility [_required_]
enum
The visibility of the notification rule. Allowed enum values: `all,organization,private`
id [_required_]
uuid
The unique identifier of the notification rule.
relationships
object
The notification rule's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
notification_template
object
A relationship reference to a notification template.
data [_required_]
object
The notification template relationship data.
id [_required_]
uuid
The unique identifier of the notification template.
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
type [_required_]
enum
Notification rules resource type. Allowed enum values: `incident_notification_rules`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
Option 3
object
A notification template object for inclusion in other resources.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
```
{
  "data": {
    "attributes": {
      "conditions": [
        {
          "field": "severity",
          "values": [
            "SEV-1",
            "SEV-2"
          ]
        }
      ],
      "created": "2025-01-15T10:30:00Z",
      "enabled": true,
      "handles": [
        "@team-email@company.com",
        "@slack-channel"
      ],
      "modified": "2025-01-15T14:45:00Z",
      "renotify_on": [
        "status",
        "severity"
      ],
      "trigger": "incident_created_trigger",
      "visibility": "organization"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "notification_template": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000001",
          "type": "notification_templates"
        }
      }
    },
    "type": "incident_notification_rules"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Create incident notification rule returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "conditions": [
        {
          "field": "severity",
          "values": [
            "SEV-1",
            "SEV-2"
          ]
        }
      ],
      "handles": [
        "@test-email@company.com"
      ],
      "visibility": "organization",
      "trigger": "incident_created_trigger",
      "enabled": true
    },
    "relationships": {
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      }
    },
    "type": "incident_notification_rules"
  }
}
EOF  

                        
```

#####  Create incident notification rule returns "Created" response
```
// Create incident notification rule returns "Created" response

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
	// there is a valid "incident_type" in the system
	IncidentTypeDataID := os.Getenv("INCIDENT_TYPE_DATA_ID")

	body := datadogV2.CreateIncidentNotificationRuleRequest{
		Data: datadogV2.IncidentNotificationRuleCreateData{
			Attributes: datadogV2.IncidentNotificationRuleCreateAttributes{
				Conditions: []datadogV2.IncidentNotificationRuleConditionsItems{
					{
						Field: "severity",
						Values: []string{
							"SEV-1",
							"SEV-2",
						},
					},
				},
				Handles: []string{
					"@test-email@company.com",
				},
				Visibility: datadogV2.INCIDENTNOTIFICATIONRULECREATEATTRIBUTESVISIBILITY_ORGANIZATION.Ptr(),
				Trigger:    "incident_created_trigger",
				Enabled:    datadog.PtrBool(true),
			},
			Relationships: &datadogV2.IncidentNotificationRuleCreateDataRelationships{
				IncidentType: &datadogV2.RelationshipToIncidentType{
					Data: datadogV2.RelationshipToIncidentTypeData{
						Id:   IncidentTypeDataID,
						Type: datadogV2.INCIDENTTYPETYPE_INCIDENT_TYPES,
					},
				},
			},
			Type: datadogV2.INCIDENTNOTIFICATIONRULETYPE_INCIDENT_NOTIFICATION_RULES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateIncidentNotificationRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.CreateIncidentNotificationRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.CreateIncidentNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.CreateIncidentNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create incident notification rule returns "Created" response
```
// Create incident notification rule returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.CreateIncidentNotificationRuleRequest;
import com.datadog.api.client.v2.model.IncidentNotificationRule;
import com.datadog.api.client.v2.model.IncidentNotificationRuleConditionsItems;
import com.datadog.api.client.v2.model.IncidentNotificationRuleCreateAttributes;
import com.datadog.api.client.v2.model.IncidentNotificationRuleCreateAttributesVisibility;
import com.datadog.api.client.v2.model.IncidentNotificationRuleCreateData;
import com.datadog.api.client.v2.model.IncidentNotificationRuleCreateDataRelationships;
import com.datadog.api.client.v2.model.IncidentNotificationRuleType;
import com.datadog.api.client.v2.model.IncidentTypeType;
import com.datadog.api.client.v2.model.RelationshipToIncidentType;
import com.datadog.api.client.v2.model.RelationshipToIncidentTypeData;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentNotificationRule", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "incident_type" in the system
    String INCIDENT_TYPE_DATA_ID = System.getenv("INCIDENT_TYPE_DATA_ID");

    CreateIncidentNotificationRuleRequest body =
        new CreateIncidentNotificationRuleRequest()
            .data(
                new IncidentNotificationRuleCreateData()
                    .attributes(
                        new IncidentNotificationRuleCreateAttributes()
                            .conditions(
                                Collections.singletonList(
                                    new IncidentNotificationRuleConditionsItems()
                                        .field("severity")
                                        .values(Arrays.asList("SEV-1", "SEV-2"))))
                            .handles(Collections.singletonList("@test-email@company.com"))
                            .visibility(
                                IncidentNotificationRuleCreateAttributesVisibility.ORGANIZATION)
                            .trigger("incident_created_trigger")
                            .enabled(true))
                    .relationships(
                        new IncidentNotificationRuleCreateDataRelationships()
                            .incidentType(
                                new RelationshipToIncidentType()
                                    .data(
                                        new RelationshipToIncidentTypeData()
                                            .id(INCIDENT_TYPE_DATA_ID)
                                            .type(IncidentTypeType.INCIDENT_TYPES))))
                    .type(IncidentNotificationRuleType.INCIDENT_NOTIFICATION_RULES));

    try {
      IncidentNotificationRule result = apiInstance.createIncidentNotificationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#createIncidentNotificationRule");
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

#####  Create incident notification rule returns "Created" response
```
"""
Create incident notification rule returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.create_incident_notification_rule_request import CreateIncidentNotificationRuleRequest
from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
    IncidentNotificationRuleConditionsItems,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes import (
    IncidentNotificationRuleCreateAttributes,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes_visibility import (
    IncidentNotificationRuleCreateAttributesVisibility,
)
from datadog_api_client.v2.model.incident_notification_rule_create_data import IncidentNotificationRuleCreateData
from datadog_api_client.v2.model.incident_notification_rule_create_data_relationships import (
    IncidentNotificationRuleCreateDataRelationships,
)
from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
from datadog_api_client.v2.model.relationship_to_incident_type_data import RelationshipToIncidentTypeData

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

body = CreateIncidentNotificationRuleRequest(
    data=IncidentNotificationRuleCreateData(
        attributes=IncidentNotificationRuleCreateAttributes(
            conditions=[
                IncidentNotificationRuleConditionsItems(
                    field="severity",
                    values=[
                        "SEV-1",
                        "SEV-2",
                    ],
                ),
            ],
            handles=[
                "@test-email@company.com",
            ],
            visibility=IncidentNotificationRuleCreateAttributesVisibility.ORGANIZATION,
            trigger="incident_created_trigger",
            enabled=True,
        ),
        relationships=IncidentNotificationRuleCreateDataRelationships(
            incident_type=RelationshipToIncidentType(
                data=RelationshipToIncidentTypeData(
                    id=INCIDENT_TYPE_DATA_ID,
                    type=IncidentTypeType.INCIDENT_TYPES,
                ),
            ),
        ),
        type=IncidentNotificationRuleType.INCIDENT_NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_notification_rule(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create incident notification rule returns "Created" response
```
# Create incident notification rule returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_notification_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = ENV["INCIDENT_TYPE_DATA_ID"]

body = DatadogAPIClient::V2::CreateIncidentNotificationRuleRequest.new({
  data: DatadogAPIClient::V2::IncidentNotificationRuleCreateData.new({
    attributes: DatadogAPIClient::V2::IncidentNotificationRuleCreateAttributes.new({
      conditions: [
        DatadogAPIClient::V2::IncidentNotificationRuleConditionsItems.new({
          field: "severity",
          values: [
            "SEV-1",
            "SEV-2",
          ],
        }),
      ],
      handles: [
        "@test-email@company.com",
      ],
      visibility: DatadogAPIClient::V2::IncidentNotificationRuleCreateAttributesVisibility::ORGANIZATION,
      trigger: "incident_created_trigger",
      enabled: true,
    }),
    relationships: DatadogAPIClient::V2::IncidentNotificationRuleCreateDataRelationships.new({
      incident_type: DatadogAPIClient::V2::RelationshipToIncidentType.new({
        data: DatadogAPIClient::V2::RelationshipToIncidentTypeData.new({
          id: INCIDENT_TYPE_DATA_ID,
          type: DatadogAPIClient::V2::IncidentTypeType::INCIDENT_TYPES,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::IncidentNotificationRuleType::INCIDENT_NOTIFICATION_RULES,
  }),
})
p api_instance.create_incident_notification_rule(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create incident notification rule returns "Created" response
```
// Create incident notification rule returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::model::CreateIncidentNotificationRuleRequest;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleConditionsItems;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleCreateAttributes;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleCreateAttributesVisibility;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleCreateData;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleCreateDataRelationships;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleType;
use datadog_api_client::datadogV2::model::IncidentTypeType;
use datadog_api_client::datadogV2::model::RelationshipToIncidentType;
use datadog_api_client::datadogV2::model::RelationshipToIncidentTypeData;

#[tokio::main]
async fn main() {
    // there is a valid "incident_type" in the system
    let incident_type_data_id = std::env::var("INCIDENT_TYPE_DATA_ID").unwrap();
    let body = CreateIncidentNotificationRuleRequest::new(
        IncidentNotificationRuleCreateData::new(
            IncidentNotificationRuleCreateAttributes::new(
                vec![IncidentNotificationRuleConditionsItems::new(
                    "severity".to_string(),
                    vec!["SEV-1".to_string(), "SEV-2".to_string()],
                )],
                vec!["@test-email@company.com".to_string()],
                "incident_created_trigger".to_string(),
            )
            .enabled(true)
            .visibility(IncidentNotificationRuleCreateAttributesVisibility::ORGANIZATION),
            IncidentNotificationRuleType::INCIDENT_NOTIFICATION_RULES,
        )
        .relationships(
            IncidentNotificationRuleCreateDataRelationships::new().incident_type(
                RelationshipToIncidentType::new(RelationshipToIncidentTypeData::new(
                    incident_type_data_id.clone(),
                    IncidentTypeType::INCIDENT_TYPES,
                )),
            ),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentNotificationRule", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api.create_incident_notification_rule(body).await;
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

#####  Create incident notification rule returns "Created" response
```
/**
 * Create incident notification rule returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentNotificationRule"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "incident_type" in the system
const INCIDENT_TYPE_DATA_ID = process.env.INCIDENT_TYPE_DATA_ID as string;

const params: v2.IncidentsApiCreateIncidentNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        conditions: [
          {
            field: "severity",
            values: ["SEV-1", "SEV-2"],
          },
        ],
        handles: ["@test-email@company.com"],
        visibility: "organization",
        trigger: "incident_created_trigger",
        enabled: true,
      },
      relationships: {
        incidentType: {
          data: {
            id: INCIDENT_TYPE_DATA_ID,
            type: "incident_types",
          },
        },
      },
      type: "incident_notification_rules",
    },
  },
};

apiInstance
  .createIncidentNotificationRule(params)
  .then((data: v2.IncidentNotificationRule) => {
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
## [Get an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#get-an-incident-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#get-an-incident-notification-rule-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.ap2.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.datadoghq.eu/api/v2/incidents/config/notification-rules/{id}https://api.ddog-gov.com/api/v2/incidents/config/notification-rules/{id}https://api.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.us3.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules/{id}
### Overview
Retrieves a specific notification rule by its ID. This endpoint requires the `incident_notification_settings_read` permission.
OAuth apps require the `incident_notification_settings_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the notification rule.
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of resources to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`, `notification_template`
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#GetIncidentNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a notification rule.
Field
Type
Description
data [_required_]
object
Notification rule data from a response.
attributes
object
The notification rule's attributes.
conditions [_required_]
[object]
The conditions that trigger this notification rule.
field [_required_]
string
The incident field to evaluate
values [_required_]
[string]
The value(s) to compare against. Multiple values are `ORed` together.
created [_required_]
date-time
Timestamp when the notification rule was created.
enabled [_required_]
boolean
Whether the notification rule is enabled.
handles [_required_]
[string]
The notification handles (targets) for this rule.
modified [_required_]
date-time
Timestamp when the notification rule was last modified.
renotify_on
[string]
List of incident fields that trigger re-notification when changed.
trigger [_required_]
string
The trigger event for this notification rule.
visibility [_required_]
enum
The visibility of the notification rule. Allowed enum values: `all,organization,private`
id [_required_]
uuid
The unique identifier of the notification rule.
relationships
object
The notification rule's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
notification_template
object
A relationship reference to a notification template.
data [_required_]
object
The notification template relationship data.
id [_required_]
uuid
The unique identifier of the notification template.
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
type [_required_]
enum
Notification rules resource type. Allowed enum values: `incident_notification_rules`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
Option 3
object
A notification template object for inclusion in other resources.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
```
{
  "data": {
    "attributes": {
      "conditions": [
        {
          "field": "severity",
          "values": [
            "SEV-1",
            "SEV-2"
          ]
        }
      ],
      "created": "2025-01-15T10:30:00Z",
      "enabled": true,
      "handles": [
        "@team-email@company.com",
        "@slack-channel"
      ],
      "modified": "2025-01-15T14:45:00Z",
      "renotify_on": [
        "status",
        "severity"
      ],
      "trigger": "incident_created_trigger",
      "visibility": "organization"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "notification_template": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000001",
          "type": "notification_templates"
        }
      }
    },
    "type": "incident_notification_rules"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Get an incident notification rule
Copy
```
                  # Path parameters  
export id="00000000-0000-0000-0000-000000000001"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an incident notification rule
```
"""
Get an incident notification rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_notification_rule(
        id=UUID("00000000-0000-0000-0000-000000000001"),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get an incident notification rule
```
# Get an incident notification rule returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident_notification_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.get_incident_notification_rule("00000000-0000-0000-0000-000000000001")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get an incident notification rule
```
// Get an incident notification rule returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetIncidentNotificationRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.GetIncidentNotificationRule(ctx, uuid.MustParse("00000000-0000-0000-0000-000000000001"), *datadogV2.NewGetIncidentNotificationRuleOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.GetIncidentNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.GetIncidentNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get an incident notification rule
```
// Get an incident notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentNotificationRule;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncidentNotificationRule", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentNotificationRule result =
          apiInstance.getIncidentNotificationRule(
              UUID.fromString("00000000-0000-0000-0000-000000000001"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getIncidentNotificationRule");
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

#####  Get an incident notification rule
```
// Get an incident notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::GetIncidentNotificationRuleOptionalParams;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncidentNotificationRule", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .get_incident_notification_rule(
            Uuid::parse_str("00000000-0000-0000-0000-000000000001").expect("invalid UUID"),
            GetIncidentNotificationRuleOptionalParams::default(),
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

#####  Get an incident notification rule
```
/**
 * Get an incident notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncidentNotificationRule"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

const params: v2.IncidentsApiGetIncidentNotificationRuleRequest = {
  id: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .getIncidentNotificationRule(params)
  .then((data: v2.IncidentNotificationRule) => {
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
## [Update an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-notification-rule-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PUT https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.ap2.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.datadoghq.eu/api/v2/incidents/config/notification-rules/{id}https://api.ddog-gov.com/api/v2/incidents/config/notification-rules/{id}https://api.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.us3.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules/{id}
### Overview
Updates an existing notification rule with a complete replacement. This endpoint requires the `incident_notification_settings_write` permission.
OAuth apps require the `incident_notification_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the notification rule.
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of resources to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`, `notification_template`
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
object
Notification rule data for an update request.
attributes [_required_]
object
The attributes for creating a notification rule.
conditions [_required_]
[object]
The conditions that trigger this notification rule.
field [_required_]
string
The incident field to evaluate
values [_required_]
[string]
The value(s) to compare against. Multiple values are `ORed` together.
enabled
boolean
Whether the notification rule is enabled.
handles [_required_]
[string]
The notification handles (targets) for this rule.
renotify_on
[string]
List of incident fields that trigger re-notification when changed.
trigger [_required_]
string
The trigger event for this notification rule.
visibility
enum
The visibility of the notification rule. Allowed enum values: `all,organization,private`
id [_required_]
uuid
The unique identifier of the notification rule.
relationships
object
The definition of `NotificationRuleCreateDataRelationships` object.
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
notification_template
object
A relationship reference to a notification template.
data [_required_]
object
The notification template relationship data.
id [_required_]
uuid
The unique identifier of the notification template.
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
type [_required_]
enum
Notification rules resource type. Allowed enum values: `incident_notification_rules`
```
{
  "data": {
    "attributes": {
      "enabled": false,
      "conditions": [
        {
          "field": "severity",
          "values": [
            "SEV-1"
          ]
        }
      ],
      "handles": [
        "@updated-team-email@company.com"
      ],
      "visibility": "private",
      "trigger": "incident_modified_trigger"
    },
    "relationships": {
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      }
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "type": "incident_notification_rules"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Response with a notification rule.
Field
Type
Description
data [_required_]
object
Notification rule data from a response.
attributes
object
The notification rule's attributes.
conditions [_required_]
[object]
The conditions that trigger this notification rule.
field [_required_]
string
The incident field to evaluate
values [_required_]
[string]
The value(s) to compare against. Multiple values are `ORed` together.
created [_required_]
date-time
Timestamp when the notification rule was created.
enabled [_required_]
boolean
Whether the notification rule is enabled.
handles [_required_]
[string]
The notification handles (targets) for this rule.
modified [_required_]
date-time
Timestamp when the notification rule was last modified.
renotify_on
[string]
List of incident fields that trigger re-notification when changed.
trigger [_required_]
string
The trigger event for this notification rule.
visibility [_required_]
enum
The visibility of the notification rule. Allowed enum values: `all,organization,private`
id [_required_]
uuid
The unique identifier of the notification rule.
relationships
object
The notification rule's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
notification_template
object
A relationship reference to a notification template.
data [_required_]
object
The notification template relationship data.
id [_required_]
uuid
The unique identifier of the notification template.
type [_required_]
enum
Notification templates resource type. Allowed enum values: `notification_templates`
type [_required_]
enum
Notification rules resource type. Allowed enum values: `incident_notification_rules`
included
[ <oneOf>]
Related objects that are included in the response.
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
Incident type response data.
attributes
object
Incident type's attributes.
createdAt
date-time
Timestamp when the incident type was created.
createdBy
string
A unique identifier that represents the user that created the incident type.
description
string
Text that describes the incident type.
is_default
boolean
If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
lastModifiedBy
string
A unique identifier that represents the user that last modified the incident type.
modifiedAt
date-time
Timestamp when the incident type was last modified.
name [_required_]
string
The name of the incident type.
prefix
string
The string that will be prepended to the incident title across the Datadog app.
id [_required_]
string
The incident type's ID.
relationships
object
The incident type's resource relationships.
created_by_user
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
google_meet_configuration
object
A reference to a Google Meet Configuration resource.
data [_required_]
object
The Google Meet configuration relationship data object.
id [_required_]
string
The unique identifier of the Google Meet configuration.
type [_required_]
string
The type of the Google Meet configuration.
last_modified_by_user
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
microsoft_teams_configuration
object
A reference to a Microsoft Teams Configuration resource.
data [_required_]
object
The Microsoft Teams configuration relationship data object.
id [_required_]
string
The unique identifier of the Microsoft Teams configuration.
type [_required_]
string
The type of the Microsoft Teams configuration.
zoom_configuration
object
A reference to a Zoom configuration resource.
data [_required_]
object
The Zoom configuration relationship data object.
id [_required_]
string
The unique identifier of the Zoom configuration.
type [_required_]
string
The type of the Zoom configuration.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
Option 3
object
A notification template object for inclusion in other resources.
attributes
object
The notification template's attributes.
category [_required_]
string
The category of the notification template.
content [_required_]
string
The content body of the notification template.
created [_required_]
date-time
Timestamp when the notification template was created.
modified [_required_]
date-time
Timestamp when the notification template was last modified.
name [_required_]
string
The name of the notification template.
subject [_required_]
string
The subject line of the notification template.
id [_required_]
uuid
The unique identifier of the notification template.
relationships
object
The notification template's resource relationships.
created_by_user
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
incident_type
object
Relationship to an incident type.
data [_required_]
object
Relationship to incident type object.
id [_required_]
string
The incident type's ID.
type [_required_]
enum
Incident type resource type. Allowed enum values: `incident_types`
default: `incident_types`
last_modified_by_user
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
Notification templates resource type. Allowed enum values: `notification_templates`
```
{
  "data": {
    "attributes": {
      "conditions": [
        {
          "field": "severity",
          "values": [
            "SEV-1",
            "SEV-2"
          ]
        }
      ],
      "created": "2025-01-15T10:30:00Z",
      "enabled": true,
      "handles": [
        "@team-email@company.com",
        "@slack-channel"
      ],
      "modified": "2025-01-15T14:45:00Z",
      "renotify_on": [
        "status",
        "severity"
      ],
      "trigger": "incident_created_trigger",
      "visibility": "organization"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "notification_template": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000001",
          "type": "notification_templates"
        }
      }
    },
    "type": "incident_notification_rules"
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Update incident notification rule returns "OK" response
Copy
```
                          # Path parameters  
export id="00000000-0000-0000-0000-000000000001"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": false,
      "conditions": [
        {
          "field": "severity",
          "values": [
            "SEV-1"
          ]
        }
      ],
      "handles": [
        "@updated-team-email@company.com"
      ],
      "visibility": "private",
      "trigger": "incident_modified_trigger"
    },
    "relationships": {
      "incident_type": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "incident_types"
        }
      }
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "type": "incident_notification_rules"
  }
}
EOF  

                        
```

#####  Update incident notification rule returns "OK" response
```
// Update incident notification rule returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "notification_rule" in the system
	NotificationRuleDataID := uuid.MustParse(os.Getenv("NOTIFICATION_RULE_DATA_ID"))

	// there is a valid "incident_type" in the system
	IncidentTypeDataID := os.Getenv("INCIDENT_TYPE_DATA_ID")

	body := datadogV2.PutIncidentNotificationRuleRequest{
		Data: datadogV2.IncidentNotificationRuleUpdateData{
			Attributes: datadogV2.IncidentNotificationRuleCreateAttributes{
				Enabled: datadog.PtrBool(false),
				Conditions: []datadogV2.IncidentNotificationRuleConditionsItems{
					{
						Field: "severity",
						Values: []string{
							"SEV-1",
						},
					},
				},
				Handles: []string{
					"@updated-team-email@company.com",
				},
				Visibility: datadogV2.INCIDENTNOTIFICATIONRULECREATEATTRIBUTESVISIBILITY_PRIVATE.Ptr(),
				Trigger:    "incident_modified_trigger",
			},
			Relationships: &datadogV2.IncidentNotificationRuleCreateDataRelationships{
				IncidentType: &datadogV2.RelationshipToIncidentType{
					Data: datadogV2.RelationshipToIncidentTypeData{
						Id:   IncidentTypeDataID,
						Type: datadogV2.INCIDENTTYPETYPE_INCIDENT_TYPES,
					},
				},
			},
			Id:   NotificationRuleDataID,
			Type: datadogV2.INCIDENTNOTIFICATIONRULETYPE_INCIDENT_NOTIFICATION_RULES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateIncidentNotificationRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.UpdateIncidentNotificationRule(ctx, NotificationRuleDataID, body, *datadogV2.NewUpdateIncidentNotificationRuleOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.UpdateIncidentNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.UpdateIncidentNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update incident notification rule returns "OK" response
```
// Update incident notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentNotificationRule;
import com.datadog.api.client.v2.model.IncidentNotificationRuleConditionsItems;
import com.datadog.api.client.v2.model.IncidentNotificationRuleCreateAttributes;
import com.datadog.api.client.v2.model.IncidentNotificationRuleCreateAttributesVisibility;
import com.datadog.api.client.v2.model.IncidentNotificationRuleCreateDataRelationships;
import com.datadog.api.client.v2.model.IncidentNotificationRuleType;
import com.datadog.api.client.v2.model.IncidentNotificationRuleUpdateData;
import com.datadog.api.client.v2.model.IncidentTypeType;
import com.datadog.api.client.v2.model.PutIncidentNotificationRuleRequest;
import com.datadog.api.client.v2.model.RelationshipToIncidentType;
import com.datadog.api.client.v2.model.RelationshipToIncidentTypeData;
import java.util.Collections;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncidentNotificationRule", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    // there is a valid "notification_rule" in the system
    UUID NOTIFICATION_RULE_DATA_ID = null;
    try {
      NOTIFICATION_RULE_DATA_ID = UUID.fromString(System.getenv("NOTIFICATION_RULE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    // there is a valid "incident_type" in the system
    String INCIDENT_TYPE_DATA_ID = System.getenv("INCIDENT_TYPE_DATA_ID");

    PutIncidentNotificationRuleRequest body =
        new PutIncidentNotificationRuleRequest()
            .data(
                new IncidentNotificationRuleUpdateData()
                    .attributes(
                        new IncidentNotificationRuleCreateAttributes()
                            .enabled(false)
                            .conditions(
                                Collections.singletonList(
                                    new IncidentNotificationRuleConditionsItems()
                                        .field("severity")
                                        .values(Collections.singletonList("SEV-1"))))
                            .handles(Collections.singletonList("@updated-team-email@company.com"))
                            .visibility(IncidentNotificationRuleCreateAttributesVisibility.PRIVATE)
                            .trigger("incident_modified_trigger"))
                    .relationships(
                        new IncidentNotificationRuleCreateDataRelationships()
                            .incidentType(
                                new RelationshipToIncidentType()
                                    .data(
                                        new RelationshipToIncidentTypeData()
                                            .id(INCIDENT_TYPE_DATA_ID)
                                            .type(IncidentTypeType.INCIDENT_TYPES))))
                    .id(NOTIFICATION_RULE_DATA_ID)
                    .type(IncidentNotificationRuleType.INCIDENT_NOTIFICATION_RULES));

    try {
      IncidentNotificationRule result =
          apiInstance.updateIncidentNotificationRule(NOTIFICATION_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#updateIncidentNotificationRule");
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

#####  Update incident notification rule returns "OK" response
```
"""
Update incident notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
    IncidentNotificationRuleConditionsItems,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes import (
    IncidentNotificationRuleCreateAttributes,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes_visibility import (
    IncidentNotificationRuleCreateAttributesVisibility,
)
from datadog_api_client.v2.model.incident_notification_rule_create_data_relationships import (
    IncidentNotificationRuleCreateDataRelationships,
)
from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType
from datadog_api_client.v2.model.incident_notification_rule_update_data import IncidentNotificationRuleUpdateData
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.put_incident_notification_rule_request import PutIncidentNotificationRuleRequest
from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
from datadog_api_client.v2.model.relationship_to_incident_type_data import RelationshipToIncidentTypeData

# there is a valid "notification_rule" in the system
NOTIFICATION_RULE_DATA_ID = environ["NOTIFICATION_RULE_DATA_ID"]

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

body = PutIncidentNotificationRuleRequest(
    data=IncidentNotificationRuleUpdateData(
        attributes=IncidentNotificationRuleCreateAttributes(
            enabled=False,
            conditions=[
                IncidentNotificationRuleConditionsItems(
                    field="severity",
                    values=[
                        "SEV-1",
                    ],
                ),
            ],
            handles=[
                "@updated-team-email@company.com",
            ],
            visibility=IncidentNotificationRuleCreateAttributesVisibility.PRIVATE,
            trigger="incident_modified_trigger",
        ),
        relationships=IncidentNotificationRuleCreateDataRelationships(
            incident_type=RelationshipToIncidentType(
                data=RelationshipToIncidentTypeData(
                    id=INCIDENT_TYPE_DATA_ID,
                    type=IncidentTypeType.INCIDENT_TYPES,
                ),
            ),
        ),
        id=NOTIFICATION_RULE_DATA_ID,
        type=IncidentNotificationRuleType.INCIDENT_NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_notification_rule(id=NOTIFICATION_RULE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update incident notification rule returns "OK" response
```
# Update incident notification rule returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident_notification_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new

# there is a valid "notification_rule" in the system
NOTIFICATION_RULE_DATA_ID = ENV["NOTIFICATION_RULE_DATA_ID"]

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = ENV["INCIDENT_TYPE_DATA_ID"]

body = DatadogAPIClient::V2::PutIncidentNotificationRuleRequest.new({
  data: DatadogAPIClient::V2::IncidentNotificationRuleUpdateData.new({
    attributes: DatadogAPIClient::V2::IncidentNotificationRuleCreateAttributes.new({
      enabled: false,
      conditions: [
        DatadogAPIClient::V2::IncidentNotificationRuleConditionsItems.new({
          field: "severity",
          values: [
            "SEV-1",
          ],
        }),
      ],
      handles: [
        "@updated-team-email@company.com",
      ],
      visibility: DatadogAPIClient::V2::IncidentNotificationRuleCreateAttributesVisibility::PRIVATE,
      trigger: "incident_modified_trigger",
    }),
    relationships: DatadogAPIClient::V2::IncidentNotificationRuleCreateDataRelationships.new({
      incident_type: DatadogAPIClient::V2::RelationshipToIncidentType.new({
        data: DatadogAPIClient::V2::RelationshipToIncidentTypeData.new({
          id: INCIDENT_TYPE_DATA_ID,
          type: DatadogAPIClient::V2::IncidentTypeType::INCIDENT_TYPES,
        }),
      }),
    }),
    id: NOTIFICATION_RULE_DATA_ID,
    type: DatadogAPIClient::V2::IncidentNotificationRuleType::INCIDENT_NOTIFICATION_RULES,
  }),
})
p api_instance.update_incident_notification_rule(NOTIFICATION_RULE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update incident notification rule returns "OK" response
```
// Update incident notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::UpdateIncidentNotificationRuleOptionalParams;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleConditionsItems;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleCreateAttributes;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleCreateAttributesVisibility;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleCreateDataRelationships;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleType;
use datadog_api_client::datadogV2::model::IncidentNotificationRuleUpdateData;
use datadog_api_client::datadogV2::model::IncidentTypeType;
use datadog_api_client::datadogV2::model::PutIncidentNotificationRuleRequest;
use datadog_api_client::datadogV2::model::RelationshipToIncidentType;
use datadog_api_client::datadogV2::model::RelationshipToIncidentTypeData;

#[tokio::main]
async fn main() {
    // there is a valid "notification_rule" in the system
    let notification_rule_data_id =
        uuid::Uuid::parse_str(&std::env::var("NOTIFICATION_RULE_DATA_ID").unwrap())
            .expect("Invalid UUID");

    // there is a valid "incident_type" in the system
    let incident_type_data_id = std::env::var("INCIDENT_TYPE_DATA_ID").unwrap();
    let body = PutIncidentNotificationRuleRequest::new(
        IncidentNotificationRuleUpdateData::new(
            IncidentNotificationRuleCreateAttributes::new(
                vec![IncidentNotificationRuleConditionsItems::new(
                    "severity".to_string(),
                    vec!["SEV-1".to_string()],
                )],
                vec!["@updated-team-email@company.com".to_string()],
                "incident_modified_trigger".to_string(),
            )
            .enabled(false)
            .visibility(IncidentNotificationRuleCreateAttributesVisibility::PRIVATE),
            notification_rule_data_id.clone(),
            IncidentNotificationRuleType::INCIDENT_NOTIFICATION_RULES,
        )
        .relationships(
            IncidentNotificationRuleCreateDataRelationships::new().incident_type(
                RelationshipToIncidentType::new(RelationshipToIncidentTypeData::new(
                    incident_type_data_id.clone(),
                    IncidentTypeType::INCIDENT_TYPES,
                )),
            ),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncidentNotificationRule", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .update_incident_notification_rule(
            notification_rule_data_id.clone(),
            body,
            UpdateIncidentNotificationRuleOptionalParams::default(),
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

#####  Update incident notification rule returns "OK" response
```
/**
 * Update incident notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncidentNotificationRule"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

// there is a valid "notification_rule" in the system
const NOTIFICATION_RULE_DATA_ID = process.env
  .NOTIFICATION_RULE_DATA_ID as string;

// there is a valid "incident_type" in the system
const INCIDENT_TYPE_DATA_ID = process.env.INCIDENT_TYPE_DATA_ID as string;

const params: v2.IncidentsApiUpdateIncidentNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        enabled: false,
        conditions: [
          {
            field: "severity",
            values: ["SEV-1"],
          },
        ],
        handles: ["@updated-team-email@company.com"],
        visibility: "private",
        trigger: "incident_modified_trigger",
      },
      relationships: {
        incidentType: {
          data: {
            id: INCIDENT_TYPE_DATA_ID,
            type: "incident_types",
          },
        },
      },
      id: NOTIFICATION_RULE_DATA_ID,
      type: "incident_notification_rules",
    },
  },
  id: NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .updateIncidentNotificationRule(params)
  .then((data: v2.IncidentNotificationRule) => {
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
## [Delete an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-notification-rule-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.ap2.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.datadoghq.eu/api/v2/incidents/config/notification-rules/{id}https://api.ddog-gov.com/api/v2/incidents/config/notification-rules/{id}https://api.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.us3.datadoghq.com/api/v2/incidents/config/notification-rules/{id}https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules/{id}
### Overview
Deletes a notification rule by its ID. This endpoint requires the `incident_notification_settings_write` permission.
OAuth apps require the `incident_notification_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the notification rule.
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of resources to include. Supported values: `created_by_user`, `last_modified_by_user`, `incident_type`, `notification_template`
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationRule-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentNotificationRule-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  Delete an incident notification rule
Copy
```
                  # Path parameters  
export id="00000000-0000-0000-0000-000000000001"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/config/notification-rules/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an incident notification rule
```
"""
Delete an incident notification rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_notification_rule(
        id=UUID("00000000-0000-0000-0000-000000000001"),
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an incident notification rule
```
# Delete an incident notification rule returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_notification_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
api_instance.delete_incident_notification_rule("00000000-0000-0000-0000-000000000001")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an incident notification rule
```
// Delete an incident notification rule returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteIncidentNotificationRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	r, err := api.DeleteIncidentNotificationRule(ctx, uuid.MustParse("00000000-0000-0000-0000-000000000001"), *datadogV2.NewDeleteIncidentNotificationRuleOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.DeleteIncidentNotificationRule`: %v\n", err)
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

#####  Delete an incident notification rule
```
// Delete an incident notification rule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentNotificationRule", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      apiInstance.deleteIncidentNotificationRule(
          UUID.fromString("00000000-0000-0000-0000-000000000001"));
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#deleteIncidentNotificationRule");
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

#####  Delete an incident notification rule
```
// Delete an incident notification rule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::DeleteIncidentNotificationRuleOptionalParams;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentNotificationRule", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .delete_incident_notification_rule(
            Uuid::parse_str("00000000-0000-0000-0000-000000000001").expect("invalid UUID"),
            DeleteIncidentNotificationRuleOptionalParams::default(),
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

#####  Delete an incident notification rule
```
/**
 * Delete an incident notification rule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentNotificationRule"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

const params: v2.IncidentsApiDeleteIncidentNotificationRuleRequest = {
  id: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .deleteIncidentNotificationRule(params)
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
## [List incident attachments](https://docs.datadoghq.com/api/latest/incidents/#list-incident-attachments)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#list-incident-attachments-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/attachmentshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/attachmentshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/attachments
### Overview
List incident attachments. This endpoint requires the `incident_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
#### Query Strings
Name
Type
Description
filter[attachment_type]
string
Filter attachments by type. Supported values are `1` (`postmortem`) and `2` (`link`).
include
string
Resource to include in the response. Supported value: `last_modified_by_user`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentAttachments-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentAttachments-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#ListIncidentAttachments-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data [_required_]
[object]
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
included
[ <oneOf>]
Option 1
object
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
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": [
    {
      "attributes": {
        "attachment": {
          "documentUrl": "string",
          "title": "string"
        },
        "attachment_type": "string",
        "modified": "2019-09-19T10:00:00.000Z"
      },
      "id": "00000000-abcd-0002-0000-000000000000",
      "relationships": {
        "last_modified_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        }
      },
      "type": "incident_attachments"
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
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/incidents/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/incidents/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/incidents/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/incidents/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/incidents/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/incidents/?code-lang=typescript)


#####  List incident attachments
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/attachments" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List incident attachments
```
"""
Get a list of attachments returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["list_incident_attachments"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_attachments(
        incident_id="incident_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List incident attachments
```
# Get a list of attachments returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_attachments".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentsAPI.new
p api_instance.list_incident_attachments("incident_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List incident attachments
```
// Get a list of attachments returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListIncidentAttachments", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIncidentsApi(apiClient)
	resp, r, err := api.ListIncidentAttachments(ctx, "incident_id", *datadogV2.NewListIncidentAttachmentsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IncidentsApi.ListIncidentAttachments`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IncidentsApi.ListIncidentAttachments`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List incident attachments
```
// Get a list of attachments returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentsApi;
import com.datadog.api.client.v2.model.IncidentAttachmentsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentAttachments", true);
    IncidentsApi apiInstance = new IncidentsApi(defaultClient);

    try {
      IncidentAttachmentsResponse result = apiInstance.listIncidentAttachments("incident_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#listIncidentAttachments");
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

#####  List incident attachments
```
// Get a list of attachments returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incidents::IncidentsAPI;
use datadog_api_client::datadogV2::api_incidents::ListIncidentAttachmentsOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentAttachments", true);
    let api = IncidentsAPI::with_config(configuration);
    let resp = api
        .list_incident_attachments(
            "incident_id".to_string(),
            ListIncidentAttachmentsOptionalParams::default(),
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

#####  List incident attachments
```
/**
 * Get a list of attachments returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentAttachments"] = true;
const apiInstance = new v2.IncidentsApi(configuration);

const params: v2.IncidentsApiListIncidentAttachmentsRequest = {
  incidentId: "incident_id",
};

apiInstance
  .listIncidentAttachments(params)
  .then((data: v2.IncidentAttachmentsResponse) => {
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
## [Create incident attachment](https://docs.datadoghq.com/api/latest/incidents/#create-incident-attachment)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#create-incident-attachment-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.datadoghq.eu/api/v2/incidents/{incident_id}/attachmentshttps://api.ddog-gov.com/api/v2/incidents/{incident_id}/attachmentshttps://api.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/attachmentshttps://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/attachments
### Overview
Create an incident attachment. This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
#### Query Strings
Name
Type
Description
include
string
Resource to include in the response. Supported value: `last_modified_by_user`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data
object
attributes
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
id
string
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
```
{
  "data": {
    "attributes": {
      "attachment": {
        "documentUrl": "string",
        "title": "string"
      },
      "attachment_type": "string"
    },
    "id": "string",
    "type": "incident_attachments"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentAttachment-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentAttachment-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentAttachment-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#CreateIncidentAttachment-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data
object
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
included
[ <oneOf>]
Option 1
object
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
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "attachment": {
        "documentUrl": "string",
        "title": "string"
      },
      "attachment_type": "string",
      "modified": "2019-09-19T10:00:00.000Z"
    },
    "id": "00000000-abcd-0002-0000-000000000000",
    "relationships": {
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "incident_attachments"
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
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)


#####  Create incident attachment
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/attachments" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "incident_attachments"
  }
}
EOF  

                
```

* * *
## [Delete incident attachment](https://docs.datadoghq.com/api/latest/incidents/#delete-incident-attachment)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#delete-incident-attachment-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}
### Overview
This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
attachment_id [_required_]
The ID of the attachment.
### Response
  * [204](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentAttachment-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentAttachment-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentAttachment-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentAttachment-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#DeleteIncidentAttachment-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)


#####  Delete incident attachment
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
export attachment_id="00000000-0000-0000-0000-000000000002"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/attachments/${attachment_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Update incident attachment](https://docs.datadoghq.com/api/latest/incidents/#update-incident-attachment)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/incidents/#update-incident-attachment-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PATCH https://api.ap1.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.ap2.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.datadoghq.eu/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.ddog-gov.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.us3.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}https://api.us5.datadoghq.com/api/v2/incidents/{incident_id}/attachments/{attachment_id}
### Overview
This endpoint requires the `incident_write` permission.
OAuth apps require the `incident_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incidents) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
incident_id [_required_]
string
The UUID of the incident.
attachment_id [_required_]
The ID of the attachment.
#### Query Strings
Name
Type
Description
include
string
Resource to include in the response. Supported value: `last_modified_by_user`.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data
object
attributes
object
attachment
object
documentUrl
string
title
string
id
string
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
```
{
  "data": {
    "attributes": {
      "attachment": {
        "documentUrl": "string",
        "title": "string"
      }
    },
    "id": "string",
    "type": "incident_attachments"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentAttachment-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentAttachment-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentAttachment-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentAttachment-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/incidents/#UpdateIncidentAttachment-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


Field
Type
Description
data
object
attributes [_required_]
object
attachment
object
documentUrl
string
title
string
attachment_type
enum
modified
date-time
id [_required_]
string
relationships [_required_]
object
last_modified_by_user
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type [_required_]
enum
The incident attachment resource type. Allowed enum values: `incident_attachments`
default: `incident_attachments`
included
[ <oneOf>]
Option 1
object
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
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "attachment": {
        "documentUrl": "string",
        "title": "string"
      },
      "attachment_type": "string",
      "modified": "2019-09-19T10:00:00.000Z"
    },
    "id": "00000000-abcd-0002-0000-000000000000",
    "relationships": {
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "incident_attachments"
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
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/incidents/)
  * [Example](https://docs.datadoghq.com/api/latest/incidents/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/incidents/?code-lang=curl)


#####  Update incident attachment
Copy
```
                  # Path parameters  
export incident_id="CHANGE_ME"  
export attachment_id="00000000-0000-0000-0000-000000000002"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/incidents/${incident_id}/attachments/${attachment_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "incident_attachments"
  }
}
EOF  

                
```

* * *
![](https://id.rlcdn.com/464526.gif)
##### Get Started with Datadog
