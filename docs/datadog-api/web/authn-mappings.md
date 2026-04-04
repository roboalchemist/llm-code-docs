# Source: https://docs.datadoghq.com/api/latest/authn-mappings/

# AuthN Mappings
[The AuthN Mappings API](https://docs.datadoghq.com/account_management/authn_mapping/?tab=example) is used to automatically map groups of users to roles in Datadog using attributes sent from Identity Providers. Use these endpoints to manage your AuthN Mappings.
## [Get an AuthN Mapping by UUID](https://docs.datadoghq.com/api/latest/authn-mappings/#get-an-authn-mapping-by-uuid)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/authn-mappings/#get-an-authn-mapping-by-uuid-v2)


GET https://api.ap1.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.ap2.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.datadoghq.eu/api/v2/authn_mappings/{authn_mapping_id}https://api.ddog-gov.com/api/v2/authn_mappings/{authn_mapping_id}https://api.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.us3.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.us5.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}
### Overview
Get an AuthN Mapping specified by the AuthN Mapping UUID. This endpoint requires the `user_access_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
authn_mapping_id [_required_]
string
The UUID of the AuthN Mapping.
### Response
  * [200](https://docs.datadoghq.com/api/latest/authn-mappings/#GetAuthNMapping-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/authn-mappings/#GetAuthNMapping-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/authn-mappings/#GetAuthNMapping-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/authn-mappings/#GetAuthNMapping-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


AuthN Mapping response from the API.
Field
Type
Description
data
object
The AuthN Mapping object returned by API.
attributes
object
Attributes of AuthN Mapping.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
created_at
date-time
Creation time of the AuthN Mapping.
modified_at
date-time
Time of last AuthN Mapping modification.
saml_assertion_attribute_id
string
The ID of the SAML assertion attribute.
id [_required_]
string
ID of the AuthN Mapping.
relationships
object
All relationships associated with AuthN Mapping.
role
object
Relationship to role.
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
saml_assertion_attribute
object
AuthN Mapping relationship to SAML Assertion Attribute.
data [_required_]
object
Data of AuthN Mapping relationship to SAML Assertion Attribute.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
team
object
Relationship to team.
data
object
Relationship to Team object.
id
string
The unique identifier of the team.
type
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
AuthN Mappings resource type. Allowed enum values: `authn_mappings`
default: `authn_mappings`
included
[ <oneOf>]
Included data in the AuthN Mapping response.
Option 1
object
SAML assertion attribute.
attributes
object
Key/Value pair of attributes used in SAML assertion attributes.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
Option 2
object
Role object returned by the API.
attributes
object
Attributes of the role.
created_at
date-time
Creation time of the role.
modified_at
date-time
Time of last role modification.
name
string
The name of the role. The name is neither unique nor a stable identifier of the role.
user_count
int64
Number of users with that role.
id
string
The unique identifier of the role.
relationships
object
Relationships of the role object returned by the API.
permissions
object
Relationship to multiple permissions objects.
data
[object]
Relationships to permission objects.
id
string
ID of the permission.
type
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
Option 3
object
Team.
attributes
object
Team attributes.
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
handle
string
The team's identifier
link_count
int32
The number of links belonging to the team
name
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
id
string
The ID of the Team.
type
enum
Team type Allowed enum values: `team`
default: `team`
```
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development",
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "saml_assertion_attribute_id": "0"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
          "type": "roles"
        }
      },
      "saml_assertion_attribute": {
        "data": {
          "id": "0",
          "type": "saml_assertion_attributes"
        }
      },
      "team": {
        "data": {
          "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      }
    },
    "type": "authn_mappings"
  },
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
    }
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=typescript)


#####  Get an AuthN Mapping by UUID
Copy
```
                  # Path parameters  
export authn_mapping_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings/${authn_mapping_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an AuthN Mapping by UUID
```
"""
Get an AuthN Mapping by UUID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.get_authn_mapping(
        authn_mapping_id=AUTHN_MAPPING_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an AuthN Mapping by UUID
```
# Get an AuthN Mapping by UUID returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = ENV["AUTHN_MAPPING_DATA_ID"]
p api_instance.get_authn_mapping(AUTHN_MAPPING_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an AuthN Mapping by UUID
```
// Get an AuthN Mapping by UUID returns "OK" response

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
	// there is a valid "authn_mapping" in the system
	AuthnMappingDataID := os.Getenv("AUTHN_MAPPING_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.GetAuthNMapping(ctx, AuthnMappingDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.GetAuthNMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.GetAuthNMapping`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an AuthN Mapping by UUID
```
// Get an AuthN Mapping by UUID returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "authn_mapping" in the system
    String AUTHN_MAPPING_DATA_ID = System.getenv("AUTHN_MAPPING_DATA_ID");

    try {
      AuthNMappingResponse result = apiInstance.getAuthNMapping(AUTHN_MAPPING_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#getAuthNMapping");
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

#####  Get an AuthN Mapping by UUID
```
// Get an AuthN Mapping by UUID returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "authn_mapping" in the system
    let authn_mapping_data_id = std::env::var("AUTHN_MAPPING_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api.get_authn_mapping(authn_mapping_data_id.clone()).await;
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

#####  Get an AuthN Mapping by UUID
```
/**
 * Get an AuthN Mapping by UUID returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "authn_mapping" in the system
const AUTHN_MAPPING_DATA_ID = process.env.AUTHN_MAPPING_DATA_ID as string;

const params: v2.AuthNMappingsApiGetAuthNMappingRequest = {
  authnMappingId: AUTHN_MAPPING_DATA_ID,
};

apiInstance
  .getAuthNMapping(params)
  .then((data: v2.AuthNMappingResponse) => {
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
## [Edit an AuthN Mapping](https://docs.datadoghq.com/api/latest/authn-mappings/#edit-an-authn-mapping)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/authn-mappings/#edit-an-authn-mapping-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.ap2.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.datadoghq.eu/api/v2/authn_mappings/{authn_mapping_id}https://api.ddog-gov.com/api/v2/authn_mappings/{authn_mapping_id}https://api.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.us3.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.us5.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}
### Overview
Edit an AuthN Mapping. This endpoint requires the `user_access_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
authn_mapping_id [_required_]
string
The UUID of the AuthN Mapping.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


Field
Type
Description
data [_required_]
object
Data for updating an AuthN Mapping.
attributes
object
Key/Value pair of attributes used for update request.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
id [_required_]
string
ID of the AuthN Mapping.
relationships
<oneOf>
Relationship of AuthN Mapping update object to a Role or Team.
Option 1
object
Relationship of AuthN Mapping to a Role.
role [_required_]
object
Relationship to role.
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
Option 2
object
Relationship of AuthN Mapping to a Team.
team [_required_]
object
Relationship to team.
data
object
Relationship to Team object.
id
string
The unique identifier of the team.
type
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
AuthN Mappings resource type. Allowed enum values: `authn_mappings`
default: `authn_mappings`
```
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/authn-mappings/#UpdateAuthNMapping-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/authn-mappings/#UpdateAuthNMapping-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/authn-mappings/#UpdateAuthNMapping-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/authn-mappings/#UpdateAuthNMapping-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/authn-mappings/#UpdateAuthNMapping-409-v2)
  * [422](https://docs.datadoghq.com/api/latest/authn-mappings/#UpdateAuthNMapping-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/authn-mappings/#UpdateAuthNMapping-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


AuthN Mapping response from the API.
Field
Type
Description
data
object
The AuthN Mapping object returned by API.
attributes
object
Attributes of AuthN Mapping.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
created_at
date-time
Creation time of the AuthN Mapping.
modified_at
date-time
Time of last AuthN Mapping modification.
saml_assertion_attribute_id
string
The ID of the SAML assertion attribute.
id [_required_]
string
ID of the AuthN Mapping.
relationships
object
All relationships associated with AuthN Mapping.
role
object
Relationship to role.
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
saml_assertion_attribute
object
AuthN Mapping relationship to SAML Assertion Attribute.
data [_required_]
object
Data of AuthN Mapping relationship to SAML Assertion Attribute.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
team
object
Relationship to team.
data
object
Relationship to Team object.
id
string
The unique identifier of the team.
type
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
AuthN Mappings resource type. Allowed enum values: `authn_mappings`
default: `authn_mappings`
included
[ <oneOf>]
Included data in the AuthN Mapping response.
Option 1
object
SAML assertion attribute.
attributes
object
Key/Value pair of attributes used in SAML assertion attributes.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
Option 2
object
Role object returned by the API.
attributes
object
Attributes of the role.
created_at
date-time
Creation time of the role.
modified_at
date-time
Time of last role modification.
name
string
The name of the role. The name is neither unique nor a stable identifier of the role.
user_count
int64
Number of users with that role.
id
string
The unique identifier of the role.
relationships
object
Relationships of the role object returned by the API.
permissions
object
Relationship to multiple permissions objects.
data
[object]
Relationships to permission objects.
id
string
ID of the permission.
type
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
Option 3
object
Team.
attributes
object
Team attributes.
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
handle
string
The team's identifier
link_count
int32
The number of links belonging to the team
name
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
id
string
The ID of the Team.
type
enum
Team type Allowed enum values: `team`
default: `team`
```
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development",
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "saml_assertion_attribute_id": "0"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
          "type": "roles"
        }
      },
      "saml_assertion_attribute": {
        "data": {
          "id": "0",
          "type": "saml_assertion_attributes"
        }
      },
      "team": {
        "data": {
          "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      }
    },
    "type": "authn_mappings"
  },
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Unprocessable Entity
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=typescript)


#####  Edit an AuthN Mapping returns "OK" response
Copy
```
                          # Path parameters  
export authn_mapping_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings/${authn_mapping_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
EOF  

                        
```

#####  Edit an AuthN Mapping returns "OK" response
```
// Edit an AuthN Mapping returns "OK" response

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
	// there is a valid "authn_mapping" in the system
	AuthnMappingDataID := os.Getenv("AUTHN_MAPPING_DATA_ID")

	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	body := datadogV2.AuthNMappingUpdateRequest{
		Data: datadogV2.AuthNMappingUpdateData{
			Attributes: &datadogV2.AuthNMappingUpdateAttributes{
				AttributeKey:   datadog.PtrString("member-of"),
				AttributeValue: datadog.PtrString("Development"),
			},
			Id: AuthnMappingDataID,
			Relationships: &datadogV2.AuthNMappingUpdateRelationships{
				AuthNMappingRelationshipToRole: &datadogV2.AuthNMappingRelationshipToRole{
					Role: datadogV2.RelationshipToRole{
						Data: &datadogV2.RelationshipToRoleData{
							Id:   datadog.PtrString(RoleDataID),
							Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
						},
					},
				}},
			Type: datadogV2.AUTHNMAPPINGSTYPE_AUTHN_MAPPINGS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.UpdateAuthNMapping(ctx, AuthnMappingDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.UpdateAuthNMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.UpdateAuthNMapping`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit an AuthN Mapping returns "OK" response
```
// Edit an AuthN Mapping returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingRelationshipToRole;
import com.datadog.api.client.v2.model.AuthNMappingResponse;
import com.datadog.api.client.v2.model.AuthNMappingUpdateAttributes;
import com.datadog.api.client.v2.model.AuthNMappingUpdateData;
import com.datadog.api.client.v2.model.AuthNMappingUpdateRelationships;
import com.datadog.api.client.v2.model.AuthNMappingUpdateRequest;
import com.datadog.api.client.v2.model.AuthNMappingsType;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "authn_mapping" in the system
    String AUTHN_MAPPING_DATA_ID = System.getenv("AUTHN_MAPPING_DATA_ID");

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    AuthNMappingUpdateRequest body =
        new AuthNMappingUpdateRequest()
            .data(
                new AuthNMappingUpdateData()
                    .attributes(
                        new AuthNMappingUpdateAttributes()
                            .attributeKey("member-of")
                            .attributeValue("Development"))
                    .id(AUTHN_MAPPING_DATA_ID)
                    .relationships(
                        new AuthNMappingUpdateRelationships(
                            new AuthNMappingRelationshipToRole()
                                .role(
                                    new RelationshipToRole()
                                        .data(
                                            new RelationshipToRoleData()
                                                .id(ROLE_DATA_ID)
                                                .type(RolesType.ROLES)))))
                    .type(AuthNMappingsType.AUTHN_MAPPINGS));

    try {
      AuthNMappingResponse result = apiInstance.updateAuthNMapping(AUTHN_MAPPING_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#updateAuthNMapping");
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

#####  Edit an AuthN Mapping returns "OK" response
```
"""
Edit an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_relationship_to_role import AuthNMappingRelationshipToRole
from datadog_api_client.v2.model.authn_mapping_update_attributes import AuthNMappingUpdateAttributes
from datadog_api_client.v2.model.authn_mapping_update_data import AuthNMappingUpdateData
from datadog_api_client.v2.model.authn_mapping_update_request import AuthNMappingUpdateRequest
from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingUpdateRequest(
    data=AuthNMappingUpdateData(
        attributes=AuthNMappingUpdateAttributes(
            attribute_key="member-of",
            attribute_value="Development",
        ),
        id=AUTHN_MAPPING_DATA_ID,
        relationships=AuthNMappingRelationshipToRole(
            role=RelationshipToRole(
                data=RelationshipToRoleData(
                    id=ROLE_DATA_ID,
                    type=RolesType.ROLES,
                ),
            ),
        ),
        type=AuthNMappingsType.AUTHN_MAPPINGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.update_authn_mapping(authn_mapping_id=AUTHN_MAPPING_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit an AuthN Mapping returns "OK" response
```
# Edit an AuthN Mapping returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = ENV["AUTHN_MAPPING_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::AuthNMappingUpdateRequest.new({
  data: DatadogAPIClient::V2::AuthNMappingUpdateData.new({
    attributes: DatadogAPIClient::V2::AuthNMappingUpdateAttributes.new({
      attribute_key: "member-of",
      attribute_value: "Development",
    }),
    id: AUTHN_MAPPING_DATA_ID,
    relationships: DatadogAPIClient::V2::AuthNMappingRelationshipToRole.new({
      role: DatadogAPIClient::V2::RelationshipToRole.new({
        data: DatadogAPIClient::V2::RelationshipToRoleData.new({
          id: ROLE_DATA_ID,
          type: DatadogAPIClient::V2::RolesType::ROLES,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::AuthNMappingsType::AUTHN_MAPPINGS,
  }),
})
p api_instance.update_authn_mapping(AUTHN_MAPPING_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit an AuthN Mapping returns "OK" response
```
// Edit an AuthN Mapping returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;
use datadog_api_client::datadogV2::model::AuthNMappingRelationshipToRole;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateAttributes;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateData;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateRelationships;
use datadog_api_client::datadogV2::model::AuthNMappingUpdateRequest;
use datadog_api_client::datadogV2::model::AuthNMappingsType;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "authn_mapping" in the system
    let authn_mapping_data_id = std::env::var("AUTHN_MAPPING_DATA_ID").unwrap();

    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = AuthNMappingUpdateRequest::new(
        AuthNMappingUpdateData::new(
            authn_mapping_data_id.clone(),
            AuthNMappingsType::AUTHN_MAPPINGS,
        )
        .attributes(
            AuthNMappingUpdateAttributes::new()
                .attribute_key("member-of".to_string())
                .attribute_value("Development".to_string()),
        )
        .relationships(
            AuthNMappingUpdateRelationships::AuthNMappingRelationshipToRole(Box::new(
                AuthNMappingRelationshipToRole::new(
                    RelationshipToRole::new().data(
                        RelationshipToRoleData::new()
                            .id(role_data_id.clone())
                            .type_(RolesType::ROLES),
                    ),
                ),
            )),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api
        .update_authn_mapping(authn_mapping_data_id.clone(), body)
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

#####  Edit an AuthN Mapping returns "OK" response
```
/**
 * Edit an AuthN Mapping returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "authn_mapping" in the system
const AUTHN_MAPPING_DATA_ID = process.env.AUTHN_MAPPING_DATA_ID as string;

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.AuthNMappingsApiUpdateAuthNMappingRequest = {
  body: {
    data: {
      attributes: {
        attributeKey: "member-of",
        attributeValue: "Development",
      },
      id: AUTHN_MAPPING_DATA_ID,
      relationships: {
        role: {
          data: {
            id: ROLE_DATA_ID,
            type: "roles",
          },
        },
      },
      type: "authn_mappings",
    },
  },
  authnMappingId: AUTHN_MAPPING_DATA_ID,
};

apiInstance
  .updateAuthNMapping(params)
  .then((data: v2.AuthNMappingResponse) => {
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
## [Delete an AuthN Mapping](https://docs.datadoghq.com/api/latest/authn-mappings/#delete-an-authn-mapping)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/authn-mappings/#delete-an-authn-mapping-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.ap2.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.datadoghq.eu/api/v2/authn_mappings/{authn_mapping_id}https://api.ddog-gov.com/api/v2/authn_mappings/{authn_mapping_id}https://api.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.us3.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}https://api.us5.datadoghq.com/api/v2/authn_mappings/{authn_mapping_id}
### Overview
Delete an AuthN Mapping specified by AuthN Mapping UUID. This endpoint requires the `user_access_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
authn_mapping_id [_required_]
string
The UUID of the AuthN Mapping.
### Response
  * [204](https://docs.datadoghq.com/api/latest/authn-mappings/#DeleteAuthNMapping-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/authn-mappings/#DeleteAuthNMapping-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/authn-mappings/#DeleteAuthNMapping-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/authn-mappings/#DeleteAuthNMapping-429-v2)


OK
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=typescript)


#####  Delete an AuthN Mapping
Copy
```
                  # Path parameters  
export authn_mapping_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings/${authn_mapping_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an AuthN Mapping
```
"""
Delete an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    api_instance.delete_authn_mapping(
        authn_mapping_id=AUTHN_MAPPING_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an AuthN Mapping
```
# Delete an AuthN Mapping returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = ENV["AUTHN_MAPPING_DATA_ID"]
api_instance.delete_authn_mapping(AUTHN_MAPPING_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an AuthN Mapping
```
// Delete an AuthN Mapping returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "authn_mapping" in the system
	AuthnMappingDataID := os.Getenv("AUTHN_MAPPING_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	r, err := api.DeleteAuthNMapping(ctx, AuthnMappingDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.DeleteAuthNMapping`: %v\n", err)
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

#####  Delete an AuthN Mapping
```
// Delete an AuthN Mapping returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "authn_mapping" in the system
    String AUTHN_MAPPING_DATA_ID = System.getenv("AUTHN_MAPPING_DATA_ID");

    try {
      apiInstance.deleteAuthNMapping(AUTHN_MAPPING_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#deleteAuthNMapping");
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

#####  Delete an AuthN Mapping
```
// Delete an AuthN Mapping returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "authn_mapping" in the system
    let authn_mapping_data_id = std::env::var("AUTHN_MAPPING_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api
        .delete_authn_mapping(authn_mapping_data_id.clone())
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

#####  Delete an AuthN Mapping
```
/**
 * Delete an AuthN Mapping returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "authn_mapping" in the system
const AUTHN_MAPPING_DATA_ID = process.env.AUTHN_MAPPING_DATA_ID as string;

const params: v2.AuthNMappingsApiDeleteAuthNMappingRequest = {
  authnMappingId: AUTHN_MAPPING_DATA_ID,
};

apiInstance
  .deleteAuthNMapping(params)
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
## [List all AuthN Mappings](https://docs.datadoghq.com/api/latest/authn-mappings/#list-all-authn-mappings)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/authn-mappings/#list-all-authn-mappings-v2)


GET https://api.ap1.datadoghq.com/api/v2/authn_mappingshttps://api.ap2.datadoghq.com/api/v2/authn_mappingshttps://api.datadoghq.eu/api/v2/authn_mappingshttps://api.ddog-gov.com/api/v2/authn_mappingshttps://api.datadoghq.com/api/v2/authn_mappingshttps://api.us3.datadoghq.com/api/v2/authn_mappingshttps://api.us5.datadoghq.com/api/v2/authn_mappings
### Overview
List all AuthN Mappings in the org. This endpoint requires the `user_access_read` permission.
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
sort
enum
Sort AuthN Mappings depending on the given field.  
Allowed enum values: `created_at, -created_at, role_id, -role_id, saml_assertion_attribute_id, -saml_assertion_attribute_id, role.name, -role.name, saml_assertion_attribute.attribute_key, -saml_assertion_attribute.attribute_key, saml_assertion_attribute.attribute_value, -saml_assertion_attribute.attribute_value`
filter
string
Filter all mappings by the given string.
resource_type
enum
Filter by mapping resource type. Defaults to “role” if not specified.  
Allowed enum values: `role, team`
### Response
  * [200](https://docs.datadoghq.com/api/latest/authn-mappings/#ListAuthNMappings-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/authn-mappings/#ListAuthNMappings-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/authn-mappings/#ListAuthNMappings-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


Array of AuthN Mappings response.
Field
Type
Description
data
[object]
Array of returned AuthN Mappings.
attributes
object
Attributes of AuthN Mapping.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
created_at
date-time
Creation time of the AuthN Mapping.
modified_at
date-time
Time of last AuthN Mapping modification.
saml_assertion_attribute_id
string
The ID of the SAML assertion attribute.
id [_required_]
string
ID of the AuthN Mapping.
relationships
object
All relationships associated with AuthN Mapping.
role
object
Relationship to role.
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
saml_assertion_attribute
object
AuthN Mapping relationship to SAML Assertion Attribute.
data [_required_]
object
Data of AuthN Mapping relationship to SAML Assertion Attribute.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
team
object
Relationship to team.
data
object
Relationship to Team object.
id
string
The unique identifier of the team.
type
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
AuthN Mappings resource type. Allowed enum values: `authn_mappings`
default: `authn_mappings`
included
[ <oneOf>]
Included data in the AuthN Mapping response.
Option 1
object
SAML assertion attribute.
attributes
object
Key/Value pair of attributes used in SAML assertion attributes.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
Option 2
object
Role object returned by the API.
attributes
object
Attributes of the role.
created_at
date-time
Creation time of the role.
modified_at
date-time
Time of last role modification.
name
string
The name of the role. The name is neither unique nor a stable identifier of the role.
user_count
int64
Number of users with that role.
id
string
The unique identifier of the role.
relationships
object
Relationships of the role object returned by the API.
permissions
object
Relationship to multiple permissions objects.
data
[object]
Relationships to permission objects.
id
string
ID of the permission.
type
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
Option 3
object
Team.
attributes
object
Team attributes.
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
handle
string
The team's identifier
link_count
int32
The number of links belonging to the team
name
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
id
string
The ID of the Team.
type
enum
Team type Allowed enum values: `team`
default: `team`
meta
object
Object describing meta attributes of response.
page
object
Pagination object.
total_count
int64
Total count.
total_filtered_count
int64
Total count of elements matched by the filter.
```
{
  "data": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development",
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "saml_assertion_attribute_id": "0"
      },
      "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
      "relationships": {
        "role": {
          "data": {
            "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            "type": "roles"
          }
        },
        "saml_assertion_attribute": {
          "data": {
            "id": "0",
            "type": "saml_assertion_attributes"
          }
        },
        "team": {
          "data": {
            "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
            "type": "team"
          }
        }
      },
      "type": "authn_mappings"
    }
  ],
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
    }
  ],
  "meta": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=typescript)


#####  List all AuthN Mappings
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all AuthN Mappings
```
"""
List all AuthN Mappings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.list_authn_mappings()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List all AuthN Mappings
```
# List all AuthN Mappings returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new
p api_instance.list_authn_mappings()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all AuthN Mappings
```
// List all AuthN Mappings returns "OK" response

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
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.ListAuthNMappings(ctx, *datadogV2.NewListAuthNMappingsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.ListAuthNMappings`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.ListAuthNMappings`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List all AuthN Mappings
```
// List all AuthN Mappings returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    try {
      AuthNMappingsResponse result = apiInstance.listAuthNMappings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#listAuthNMappings");
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

#####  List all AuthN Mappings
```
// List all AuthN Mappings returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;
use datadog_api_client::datadogV2::api_authn_mappings::ListAuthNMappingsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api
        .list_authn_mappings(ListAuthNMappingsOptionalParams::default())
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

#####  List all AuthN Mappings
```
/**
 * List all AuthN Mappings returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

apiInstance
  .listAuthNMappings()
  .then((data: v2.AuthNMappingsResponse) => {
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
## [Create an AuthN Mapping](https://docs.datadoghq.com/api/latest/authn-mappings/#create-an-authn-mapping)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/authn-mappings/#create-an-authn-mapping-v2)


POST https://api.ap1.datadoghq.com/api/v2/authn_mappingshttps://api.ap2.datadoghq.com/api/v2/authn_mappingshttps://api.datadoghq.eu/api/v2/authn_mappingshttps://api.ddog-gov.com/api/v2/authn_mappingshttps://api.datadoghq.com/api/v2/authn_mappingshttps://api.us3.datadoghq.com/api/v2/authn_mappingshttps://api.us5.datadoghq.com/api/v2/authn_mappings
### Overview
Create an AuthN Mapping. This endpoint requires the `user_access_manage` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


Field
Type
Description
data [_required_]
object
Data for creating an AuthN Mapping.
attributes
object
Key/Value pair of attributes used for create request.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
relationships
<oneOf>
Relationship of AuthN Mapping create object to a Role or Team.
Option 1
object
Relationship of AuthN Mapping to a Role.
role [_required_]
object
Relationship to role.
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
Option 2
object
Relationship of AuthN Mapping to a Team.
team [_required_]
object
Relationship to team.
data
object
Relationship to Team object.
id
string
The unique identifier of the team.
type
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
AuthN Mappings resource type. Allowed enum values: `authn_mappings`
default: `authn_mappings`
```
{
  "data": {
    "attributes": {
      "attribute_key": "exampleauthnmapping",
      "attribute_value": "Example-AuthN-Mapping"
    },
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/authn-mappings/#CreateAuthNMapping-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/authn-mappings/#CreateAuthNMapping-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/authn-mappings/#CreateAuthNMapping-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/authn-mappings/#CreateAuthNMapping-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/authn-mappings/#CreateAuthNMapping-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


AuthN Mapping response from the API.
Field
Type
Description
data
object
The AuthN Mapping object returned by API.
attributes
object
Attributes of AuthN Mapping.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
created_at
date-time
Creation time of the AuthN Mapping.
modified_at
date-time
Time of last AuthN Mapping modification.
saml_assertion_attribute_id
string
The ID of the SAML assertion attribute.
id [_required_]
string
ID of the AuthN Mapping.
relationships
object
All relationships associated with AuthN Mapping.
role
object
Relationship to role.
data
object
Relationship to role object.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
saml_assertion_attribute
object
AuthN Mapping relationship to SAML Assertion Attribute.
data [_required_]
object
Data of AuthN Mapping relationship to SAML Assertion Attribute.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
team
object
Relationship to team.
data
object
Relationship to Team object.
id
string
The unique identifier of the team.
type
enum
Team type Allowed enum values: `team`
default: `team`
type [_required_]
enum
AuthN Mappings resource type. Allowed enum values: `authn_mappings`
default: `authn_mappings`
included
[ <oneOf>]
Included data in the AuthN Mapping response.
Option 1
object
SAML assertion attribute.
attributes
object
Key/Value pair of attributes used in SAML assertion attributes.
attribute_key
string
Key portion of a key/value pair of the attribute sent from the Identity Provider.
attribute_value
string
Value portion of a key/value pair of the attribute sent from the Identity Provider.
id [_required_]
string
The ID of the SAML assertion attribute.
type [_required_]
enum
SAML assertion attributes resource type. Allowed enum values: `saml_assertion_attributes`
default: `saml_assertion_attributes`
Option 2
object
Role object returned by the API.
attributes
object
Attributes of the role.
created_at
date-time
Creation time of the role.
modified_at
date-time
Time of last role modification.
name
string
The name of the role. The name is neither unique nor a stable identifier of the role.
user_count
int64
Number of users with that role.
id
string
The unique identifier of the role.
relationships
object
Relationships of the role object returned by the API.
permissions
object
Relationship to multiple permissions objects.
data
[object]
Relationships to permission objects.
id
string
ID of the permission.
type
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
Option 3
object
Team.
attributes
object
Team attributes.
avatar
string
Unicode representation of the avatar for the team, limited to a single grapheme
banner
int64
Banner selection for the team
handle
string
The team's identifier
link_count
int32
The number of links belonging to the team
name
string
The name of the team
summary
string
A brief summary of the team, derived from the `description`
user_count
int32
The number of users belonging to the team
id
string
The ID of the Team.
type
enum
Team type Allowed enum values: `team`
default: `team`
```
{
  "data": {
    "attributes": {
      "attribute_key": "member-of",
      "attribute_value": "Development",
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "saml_assertion_attribute_id": "0"
    },
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "relationships": {
      "role": {
        "data": {
          "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
          "type": "roles"
        }
      },
      "saml_assertion_attribute": {
        "data": {
          "id": "0",
          "type": "saml_assertion_attributes"
        }
      },
      "team": {
        "data": {
          "id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001",
          "type": "team"
        }
      }
    },
    "type": "authn_mappings"
  },
  "included": [
    {
      "attributes": {
        "attribute_key": "member-of",
        "attribute_value": "Development"
      },
      "id": "0",
      "type": "saml_assertion_attributes"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/authn-mappings/)
  * [Example](https://docs.datadoghq.com/api/latest/authn-mappings/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/authn-mappings/?code-lang=typescript)


#####  Create an AuthN Mapping returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/authn_mappings" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "attribute_key": "exampleauthnmapping",
      "attribute_value": "Example-AuthN-Mapping"
    },
    "relationships": {
      "role": {
        "data": {
          "id": "string",
          "type": "roles"
        }
      }
    },
    "type": "authn_mappings"
  }
}
EOF  

                        
```

#####  Create an AuthN Mapping returns "OK" response
```
// Create an AuthN Mapping returns "OK" response

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
	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	body := datadogV2.AuthNMappingCreateRequest{
		Data: datadogV2.AuthNMappingCreateData{
			Attributes: &datadogV2.AuthNMappingCreateAttributes{
				AttributeKey:   datadog.PtrString("exampleauthnmapping"),
				AttributeValue: datadog.PtrString("Example-AuthN-Mapping"),
			},
			Relationships: &datadogV2.AuthNMappingCreateRelationships{
				AuthNMappingRelationshipToRole: &datadogV2.AuthNMappingRelationshipToRole{
					Role: datadogV2.RelationshipToRole{
						Data: &datadogV2.RelationshipToRoleData{
							Id:   datadog.PtrString(RoleDataID),
							Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
						},
					},
				}},
			Type: datadogV2.AUTHNMAPPINGSTYPE_AUTHN_MAPPINGS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAuthNMappingsApi(apiClient)
	resp, r, err := api.CreateAuthNMapping(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthNMappingsApi.CreateAuthNMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthNMappingsApi.CreateAuthNMapping`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an AuthN Mapping returns "OK" response
```
// Create an AuthN Mapping returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AuthNMappingsApi;
import com.datadog.api.client.v2.model.AuthNMappingCreateAttributes;
import com.datadog.api.client.v2.model.AuthNMappingCreateData;
import com.datadog.api.client.v2.model.AuthNMappingCreateRelationships;
import com.datadog.api.client.v2.model.AuthNMappingCreateRequest;
import com.datadog.api.client.v2.model.AuthNMappingRelationshipToRole;
import com.datadog.api.client.v2.model.AuthNMappingResponse;
import com.datadog.api.client.v2.model.AuthNMappingsType;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthNMappingsApi apiInstance = new AuthNMappingsApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    AuthNMappingCreateRequest body =
        new AuthNMappingCreateRequest()
            .data(
                new AuthNMappingCreateData()
                    .attributes(
                        new AuthNMappingCreateAttributes()
                            .attributeKey("exampleauthnmapping")
                            .attributeValue("Example-AuthN-Mapping"))
                    .relationships(
                        new AuthNMappingCreateRelationships(
                            new AuthNMappingRelationshipToRole()
                                .role(
                                    new RelationshipToRole()
                                        .data(
                                            new RelationshipToRoleData()
                                                .id(ROLE_DATA_ID)
                                                .type(RolesType.ROLES)))))
                    .type(AuthNMappingsType.AUTHN_MAPPINGS));

    try {
      AuthNMappingResponse result = apiInstance.createAuthNMapping(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthNMappingsApi#createAuthNMapping");
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

#####  Create an AuthN Mapping returns "OK" response
```
"""
Create an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_create_attributes import AuthNMappingCreateAttributes
from datadog_api_client.v2.model.authn_mapping_create_data import AuthNMappingCreateData
from datadog_api_client.v2.model.authn_mapping_create_request import AuthNMappingCreateRequest
from datadog_api_client.v2.model.authn_mapping_relationship_to_role import AuthNMappingRelationshipToRole
from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingCreateRequest(
    data=AuthNMappingCreateData(
        attributes=AuthNMappingCreateAttributes(
            attribute_key="exampleauthnmapping",
            attribute_value="Example-AuthN-Mapping",
        ),
        relationships=AuthNMappingRelationshipToRole(
            role=RelationshipToRole(
                data=RelationshipToRoleData(
                    id=ROLE_DATA_ID,
                    type=RolesType.ROLES,
                ),
            ),
        ),
        type=AuthNMappingsType.AUTHN_MAPPINGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.create_authn_mapping(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an AuthN Mapping returns "OK" response
```
# Create an AuthN Mapping returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AuthNMappingsAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::AuthNMappingCreateRequest.new({
  data: DatadogAPIClient::V2::AuthNMappingCreateData.new({
    attributes: DatadogAPIClient::V2::AuthNMappingCreateAttributes.new({
      attribute_key: "exampleauthnmapping",
      attribute_value: "Example-AuthN-Mapping",
    }),
    relationships: DatadogAPIClient::V2::AuthNMappingRelationshipToRole.new({
      role: DatadogAPIClient::V2::RelationshipToRole.new({
        data: DatadogAPIClient::V2::RelationshipToRoleData.new({
          id: ROLE_DATA_ID,
          type: DatadogAPIClient::V2::RolesType::ROLES,
        }),
      }),
    }),
    type: DatadogAPIClient::V2::AuthNMappingsType::AUTHN_MAPPINGS,
  }),
})
p api_instance.create_authn_mapping(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an AuthN Mapping returns "OK" response
```
// Create an AuthN Mapping returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_authn_mappings::AuthNMappingsAPI;
use datadog_api_client::datadogV2::model::AuthNMappingCreateAttributes;
use datadog_api_client::datadogV2::model::AuthNMappingCreateData;
use datadog_api_client::datadogV2::model::AuthNMappingCreateRelationships;
use datadog_api_client::datadogV2::model::AuthNMappingCreateRequest;
use datadog_api_client::datadogV2::model::AuthNMappingRelationshipToRole;
use datadog_api_client::datadogV2::model::AuthNMappingsType;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = AuthNMappingCreateRequest::new(
        AuthNMappingCreateData::new(AuthNMappingsType::AUTHN_MAPPINGS)
            .attributes(
                AuthNMappingCreateAttributes::new()
                    .attribute_key("exampleauthnmapping".to_string())
                    .attribute_value("Example-AuthN-Mapping".to_string()),
            )
            .relationships(
                AuthNMappingCreateRelationships::AuthNMappingRelationshipToRole(Box::new(
                    AuthNMappingRelationshipToRole::new(
                        RelationshipToRole::new().data(
                            RelationshipToRoleData::new()
                                .id(role_data_id.clone())
                                .type_(RolesType::ROLES),
                        ),
                    ),
                )),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = AuthNMappingsAPI::with_config(configuration);
    let resp = api.create_authn_mapping(body).await;
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

#####  Create an AuthN Mapping returns "OK" response
```
/**
 * Create an AuthN Mapping returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AuthNMappingsApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.AuthNMappingsApiCreateAuthNMappingRequest = {
  body: {
    data: {
      attributes: {
        attributeKey: "exampleauthnmapping",
        attributeValue: "Example-AuthN-Mapping",
      },
      relationships: {
        role: {
          data: {
            id: ROLE_DATA_ID,
            type: "roles",
          },
        },
      },
      type: "authn_mappings",
    },
  },
};

apiInstance
  .createAuthNMapping(params)
  .then((data: v2.AuthNMappingResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c6420a0b-b50d-4e96-a616-9925242d4dc8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f96ad7bf-20b5-43ce-b0ac-72a4e6964e09&pt=AuthN%20Mappings&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fauthn-mappings%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c6420a0b-b50d-4e96-a616-9925242d4dc8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f96ad7bf-20b5-43ce-b0ac-72a4e6964e09&pt=AuthN%20Mappings&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fauthn-mappings%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
Feedback
## Was this page helpful?
Yes 🎉
No 👎
Next
![](https://survey-images.hotjar.com/surveys/logo/90f40352a7464c849f5ce82ccd0e758d)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=530b9e1b-8841-42af-bbc1-992c89badaa7&bo=2&sid=dc714880f0be11f0bce25d1b71a216d3&vid=dc7178d0f0be11f0a0bedbc5e643d3a9&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=AuthN%20Mappings&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fauthn-mappings%2F&r=&lt=1719&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=975028)
