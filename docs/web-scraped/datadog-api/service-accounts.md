# Source: https://docs.datadoghq.com/api/latest/service-accounts/

# Service Accounts
Create, edit, and disable service accounts. See the [Service Accounts page](https://docs.datadoghq.com/account_management/org_settings/service_accounts/) for more information.
## [Create a service account](https://docs.datadoghq.com/api/latest/service-accounts/#create-a-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-accounts/#create-a-service-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/service_accountshttps://api.ap2.datadoghq.com/api/v2/service_accountshttps://api.datadoghq.eu/api/v2/service_accountshttps://api.ddog-gov.com/api/v2/service_accountshttps://api.datadoghq.com/api/v2/service_accountshttps://api.us3.datadoghq.com/api/v2/service_accountshttps://api.us5.datadoghq.com/api/v2/service_accounts
### Overview
Create a service account for your organization. This endpoint requires the `service_account_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Field
Type
Description
data [_required_]
object
Object to create a service account User.
attributes [_required_]
object
Attributes of the created user.
email [_required_]
string
The email of the user.
name
string
The name of the user.
service_account [_required_]
boolean
Whether the user is a service account. Must be true.
title
string
The title of the user.
relationships
object
Relationships of the user object.
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
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "type": "users",
    "attributes": {
      "name": "Test API Client",
      "email": "Example-Service-Account@datadoghq.com",
      "service_account": true
    },
    "relationships": {
      "roles": {
        "data": [
          {
            "id": "string",
            "type": "roles"
          }
        ]
      }
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccount-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccount-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Response containing information about a single user.
Field
Type
Description
data
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
included
[ <oneOf>]
Array of objects related to the user.
Option 1
object
Organization object.
attributes
object
Attributes of the organization.
created_at
date-time
Creation time of the organization.
description
string
Description of the organization.
disabled
boolean
Whether or not the organization is disabled.
modified_at
date-time
Time of last organization modification.
name
string
Name of the organization.
public_id
string
Public ID of the organization.
sharing
string
Sharing type of the organization.
url
string
URL of the site that this organization exists at.
id
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
Option 2
object
Permission object.
attributes
object
Attributes of a permission.
created
date-time
Creation time of the permission.
description
string
Description of the permission.
display_name
string
Displayed name for the permission.
display_type
string
Display type.
group_name
string
Name of the permission group.
name
string
Name of the permission.
restricted
boolean
Whether or not the permission is restricted.
id
string
ID of the permission.
type [_required_]
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
Option 3
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
```
{
  "data": {
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
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "description": "string",
        "disabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "public_id": "string",
        "sharing": "string",
        "url": "string"
      },
      "id": "string",
      "type": "orgs"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=typescript)


#####  Create a service account returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "users",
    "attributes": {
      "name": "Test API Client",
      "email": "Example-Service-Account@datadoghq.com",
      "service_account": true
    },
    "relationships": {
      "roles": {
        "data": [
          {
            "id": "string",
            "type": "roles"
          }
        ]
      }
    }
  }
}
EOF  

                        
```

#####  Create a service account returns "OK" response
```
// Create a service account returns "OK" response

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

	body := datadogV2.ServiceAccountCreateRequest{
		Data: datadogV2.ServiceAccountCreateData{
			Type: datadogV2.USERSTYPE_USERS,
			Attributes: datadogV2.ServiceAccountCreateAttributes{
				Name:           datadog.PtrString("Test API Client"),
				Email:          "Example-Service-Account@datadoghq.com",
				ServiceAccount: true,
			},
			Relationships: &datadogV2.UserRelationships{
				Roles: &datadogV2.RelationshipToRoles{
					Data: []datadogV2.RelationshipToRoleData{
						{
							Id:   datadog.PtrString(RoleDataID),
							Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
						},
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceAccountsApi(apiClient)
	resp, r, err := api.CreateServiceAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceAccountsApi.CreateServiceAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceAccountsApi.CreateServiceAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a service account returns "OK" response
```
// Create a service account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceAccountsApi;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RelationshipToRoles;
import com.datadog.api.client.v2.model.RolesType;
import com.datadog.api.client.v2.model.ServiceAccountCreateAttributes;
import com.datadog.api.client.v2.model.ServiceAccountCreateData;
import com.datadog.api.client.v2.model.ServiceAccountCreateRequest;
import com.datadog.api.client.v2.model.UserRelationships;
import com.datadog.api.client.v2.model.UserResponse;
import com.datadog.api.client.v2.model.UsersType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceAccountsApi apiInstance = new ServiceAccountsApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    ServiceAccountCreateRequest body =
        new ServiceAccountCreateRequest()
            .data(
                new ServiceAccountCreateData()
                    .type(UsersType.USERS)
                    .attributes(
                        new ServiceAccountCreateAttributes()
                            .name("Test API Client")
                            .email("Example-Service-Account@datadoghq.com")
                            .serviceAccount(true))
                    .relationships(
                        new UserRelationships()
                            .roles(
                                new RelationshipToRoles()
                                    .data(
                                        Collections.singletonList(
                                            new RelationshipToRoleData()
                                                .id(ROLE_DATA_ID)
                                                .type(RolesType.ROLES))))));

    try {
      UserResponse result = apiInstance.createServiceAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceAccountsApi#createServiceAccount");
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

#####  Create a service account returns "OK" response
```
"""
Create a service account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles
from datadog_api_client.v2.model.roles_type import RolesType
from datadog_api_client.v2.model.service_account_create_attributes import ServiceAccountCreateAttributes
from datadog_api_client.v2.model.service_account_create_data import ServiceAccountCreateData
from datadog_api_client.v2.model.service_account_create_request import ServiceAccountCreateRequest
from datadog_api_client.v2.model.user_relationships import UserRelationships
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = ServiceAccountCreateRequest(
    data=ServiceAccountCreateData(
        type=UsersType.USERS,
        attributes=ServiceAccountCreateAttributes(
            name="Test API Client",
            email="Example-Service-Account@datadoghq.com",
            service_account=True,
        ),
        relationships=UserRelationships(
            roles=RelationshipToRoles(
                data=[
                    RelationshipToRoleData(
                        id=ROLE_DATA_ID,
                        type=RolesType.ROLES,
                    ),
                ],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a service account returns "OK" response
```
# Create a service account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::ServiceAccountCreateRequest.new({
  data: DatadogAPIClient::V2::ServiceAccountCreateData.new({
    type: DatadogAPIClient::V2::UsersType::USERS,
    attributes: DatadogAPIClient::V2::ServiceAccountCreateAttributes.new({
      name: "Test API Client",
      email: "Example-Service-Account@datadoghq.com",
      service_account: true,
    }),
    relationships: DatadogAPIClient::V2::UserRelationships.new({
      roles: DatadogAPIClient::V2::RelationshipToRoles.new({
        data: [
          DatadogAPIClient::V2::RelationshipToRoleData.new({
            id: ROLE_DATA_ID,
            type: DatadogAPIClient::V2::RolesType::ROLES,
          }),
        ],
      }),
    }),
  }),
})
p api_instance.create_service_account(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a service account returns "OK" response
```
// Create a service account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_accounts::ServiceAccountsAPI;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RelationshipToRoles;
use datadog_api_client::datadogV2::model::RolesType;
use datadog_api_client::datadogV2::model::ServiceAccountCreateAttributes;
use datadog_api_client::datadogV2::model::ServiceAccountCreateData;
use datadog_api_client::datadogV2::model::ServiceAccountCreateRequest;
use datadog_api_client::datadogV2::model::UserRelationships;
use datadog_api_client::datadogV2::model::UsersType;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body =
        ServiceAccountCreateRequest::new(
            ServiceAccountCreateData::new(
                ServiceAccountCreateAttributes::new(
                    "Example-Service-Account@datadoghq.com".to_string(),
                    true,
                )
                .name("Test API Client".to_string()),
                UsersType::USERS,
            )
            .relationships(UserRelationships::new().roles(
                RelationshipToRoles::new().data(vec![RelationshipToRoleData::new()
                    .id(role_data_id.clone())
                    .type_(RolesType::ROLES)]),
            )),
        );
    let configuration = datadog::Configuration::new();
    let api = ServiceAccountsAPI::with_config(configuration);
    let resp = api.create_service_account(body).await;
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

#####  Create a service account returns "OK" response
```
/**
 * Create a service account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceAccountsApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.ServiceAccountsApiCreateServiceAccountRequest = {
  body: {
    data: {
      type: "users",
      attributes: {
        name: "Test API Client",
        email: "Example-Service-Account@datadoghq.com",
        serviceAccount: true,
      },
      relationships: {
        roles: {
          data: [
            {
              id: ROLE_DATA_ID,
              type: "roles",
            },
          ],
        },
      },
    },
  },
};

apiInstance
  .createServiceAccount(params)
  .then((data: v2.UserResponse) => {
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
## [Get one application key for this service account](https://docs.datadoghq.com/api/latest/service-accounts/#get-one-application-key-for-this-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-accounts/#get-one-application-key-for-this-service-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}
### Overview
Get an application key owned by this service account. This endpoint requires the `service_account_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_account_id [_required_]
string
The ID of the service account.
app_key_id [_required_]
string
The ID of the application key.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-accounts/#GetServiceAccountApplicationKey-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-accounts/#GetServiceAccountApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-accounts/#GetServiceAccountApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-accounts/#GetServiceAccountApplicationKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Response for retrieving a partial application key.
Field
Type
Description
data
object
Partial Datadog application key.
attributes
object
Attributes of a partial application key.
created_at
string
Creation date of the application key.
last4
string
The last four characters of the application key.
last_used_at
string
Last usage timestamp of the application key.
name
string
Name of the application key.
scopes
[string]
Array of scopes to grant the application key.
id
string
ID of the application key.
relationships
object
Resources related to the application key.
owned_by
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
Application Keys resource type. Allowed enum values: `application_keys`
default: `application_keys`
included
[ <oneOf>]
Array of objects related to the application key.
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
The definition of LeakedKey object.
attributes [_required_]
object
The definition of LeakedKeyAttributes object.
date [_required_]
date-time
The LeakedKeyAttributes date.
leak_source
string
The LeakedKeyAttributes leak_source.
id [_required_]
string
The LeakedKey id.
type [_required_]
enum
The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`
default: `leaked_keys`
```
{
  "data": {
    "attributes": {
      "created_at": "2020-11-23T10:00:00.000Z",
      "last4": "abcd",
      "last_used_at": "2020-12-20T10:00:00.000Z",
      "name": "Application Key for managing dashboards",
      "scopes": [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share"
      ]
    },
    "id": "string",
    "relationships": {
      "owned_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "application_keys"
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=typescript)


#####  Get one application key for this service account
Copy
```
                  # Path parameters  
export service_account_id="00000000-0000-1234-0000-000000000000"  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get one application key for this service account
```
"""
Get one application key for this service account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = environ["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.get_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID,
        app_key_id=SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get one application key for this service account
```
# Get one application key for this service account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = ENV["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]
p api_instance.get_service_account_application_key(SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get one application key for this service account
```
// Get one application key for this service account returns "OK" response

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
	// there is a valid "service_account_user" in the system
	ServiceAccountUserDataID := os.Getenv("SERVICE_ACCOUNT_USER_DATA_ID")

	// there is a valid "service_account_application_key" for "service_account_user"
	ServiceAccountApplicationKeyDataID := os.Getenv("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceAccountsApi(apiClient)
	resp, r, err := api.GetServiceAccountApplicationKey(ctx, ServiceAccountUserDataID, ServiceAccountApplicationKeyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceAccountsApi.GetServiceAccountApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceAccountsApi.GetServiceAccountApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get one application key for this service account
```
// Get one application key for this service account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceAccountsApi;
import com.datadog.api.client.v2.model.PartialApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceAccountsApi apiInstance = new ServiceAccountsApi(defaultClient);

    // there is a valid "service_account_user" in the system
    String SERVICE_ACCOUNT_USER_DATA_ID = System.getenv("SERVICE_ACCOUNT_USER_DATA_ID");

    // there is a valid "service_account_application_key" for "service_account_user"
    String SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID =
        System.getenv("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID");

    try {
      PartialApplicationKeyResponse result =
          apiInstance.getServiceAccountApplicationKey(
              SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceAccountsApi#getServiceAccountApplicationKey");
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

#####  Get one application key for this service account
```
// Get one application key for this service account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_accounts::ServiceAccountsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "service_account_user" in the system
    let service_account_user_data_id = std::env::var("SERVICE_ACCOUNT_USER_DATA_ID").unwrap();

    // there is a valid "service_account_application_key" for "service_account_user"
    let service_account_application_key_data_id =
        std::env::var("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceAccountsAPI::with_config(configuration);
    let resp = api
        .get_service_account_application_key(
            service_account_user_data_id.clone(),
            service_account_application_key_data_id.clone(),
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get one application key for this service account
```
/**
 * Get one application key for this service account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceAccountsApi(configuration);

// there is a valid "service_account_user" in the system
const SERVICE_ACCOUNT_USER_DATA_ID = process.env
  .SERVICE_ACCOUNT_USER_DATA_ID as string;

// there is a valid "service_account_application_key" for "service_account_user"
const SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = process.env
  .SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID as string;

const params: v2.ServiceAccountsApiGetServiceAccountApplicationKeyRequest = {
  serviceAccountId: SERVICE_ACCOUNT_USER_DATA_ID,
  appKeyId: SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
};

apiInstance
  .getServiceAccountApplicationKey(params)
  .then((data: v2.PartialApplicationKeyResponse) => {
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
## [Edit an application key for this service account](https://docs.datadoghq.com/api/latest/service-accounts/#edit-an-application-key-for-this-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-accounts/#edit-an-application-key-for-this-service-account-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}
### Overview
Edit an application key owned by this service account. This endpoint requires the `service_account_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_account_id [_required_]
string
The ID of the service account.
app_key_id [_required_]
string
The ID of the application key.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Field
Type
Description
data [_required_]
object
Object used to update an application key.
attributes [_required_]
object
Attributes used to update an application Key.
name
string
Name of the application key.
scopes
[string]
Array of scopes to grant the application key.
id [_required_]
string
ID of the application key.
type [_required_]
enum
Application Keys resource type. Allowed enum values: `application_keys`
default: `application_keys`
```
{
  "data": {
    "id": "67963b57-d67c-dfa7-b180-62ee9301d2f6",
    "type": "application_keys",
    "attributes": {
      "name": "Application Key for managing dashboards-updated"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-accounts/#UpdateServiceAccountApplicationKey-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-accounts/#UpdateServiceAccountApplicationKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-accounts/#UpdateServiceAccountApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-accounts/#UpdateServiceAccountApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-accounts/#UpdateServiceAccountApplicationKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Response for retrieving a partial application key.
Field
Type
Description
data
object
Partial Datadog application key.
attributes
object
Attributes of a partial application key.
created_at
string
Creation date of the application key.
last4
string
The last four characters of the application key.
last_used_at
string
Last usage timestamp of the application key.
name
string
Name of the application key.
scopes
[string]
Array of scopes to grant the application key.
id
string
ID of the application key.
relationships
object
Resources related to the application key.
owned_by
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
Application Keys resource type. Allowed enum values: `application_keys`
default: `application_keys`
included
[ <oneOf>]
Array of objects related to the application key.
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
The definition of LeakedKey object.
attributes [_required_]
object
The definition of LeakedKeyAttributes object.
date [_required_]
date-time
The LeakedKeyAttributes date.
leak_source
string
The LeakedKeyAttributes leak_source.
id [_required_]
string
The LeakedKey id.
type [_required_]
enum
The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`
default: `leaked_keys`
```
{
  "data": {
    "attributes": {
      "created_at": "2020-11-23T10:00:00.000Z",
      "last4": "abcd",
      "last_used_at": "2020-12-20T10:00:00.000Z",
      "name": "Application Key for managing dashboards",
      "scopes": [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share"
      ]
    },
    "id": "string",
    "relationships": {
      "owned_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "application_keys"
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=typescript)


#####  Edit an application key for this service account returns "OK" response
Copy
```
                          # Path parameters  
export service_account_id="00000000-0000-1234-0000-000000000000"  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "67963b57-d67c-dfa7-b180-62ee9301d2f6",
    "type": "application_keys",
    "attributes": {
      "name": "Application Key for managing dashboards-updated"
    }
  }
}
EOF  

                        
```

#####  Edit an application key for this service account returns "OK" response
```
// Edit an application key for this service account returns "OK" response

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
	// there is a valid "service_account_user" in the system
	ServiceAccountUserDataID := os.Getenv("SERVICE_ACCOUNT_USER_DATA_ID")

	// there is a valid "service_account_application_key" for "service_account_user"
	ServiceAccountApplicationKeyDataID := os.Getenv("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID")

	body := datadogV2.ApplicationKeyUpdateRequest{
		Data: datadogV2.ApplicationKeyUpdateData{
			Id:   ServiceAccountApplicationKeyDataID,
			Type: datadogV2.APPLICATIONKEYSTYPE_APPLICATION_KEYS,
			Attributes: datadogV2.ApplicationKeyUpdateAttributes{
				Name: datadog.PtrString("Application Key for managing dashboards-updated"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceAccountsApi(apiClient)
	resp, r, err := api.UpdateServiceAccountApplicationKey(ctx, ServiceAccountUserDataID, ServiceAccountApplicationKeyDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceAccountsApi.UpdateServiceAccountApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceAccountsApi.UpdateServiceAccountApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit an application key for this service account returns "OK" response
```
// Edit an application key for this service account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceAccountsApi;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateAttributes;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateData;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateRequest;
import com.datadog.api.client.v2.model.ApplicationKeysType;
import com.datadog.api.client.v2.model.PartialApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceAccountsApi apiInstance = new ServiceAccountsApi(defaultClient);

    // there is a valid "service_account_user" in the system
    String SERVICE_ACCOUNT_USER_DATA_ID = System.getenv("SERVICE_ACCOUNT_USER_DATA_ID");

    // there is a valid "service_account_application_key" for "service_account_user"
    String SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME =
        System.getenv("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME");
    String SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID =
        System.getenv("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID");

    ApplicationKeyUpdateRequest body =
        new ApplicationKeyUpdateRequest()
            .data(
                new ApplicationKeyUpdateData()
                    .id(SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID)
                    .type(ApplicationKeysType.APPLICATION_KEYS)
                    .attributes(
                        new ApplicationKeyUpdateAttributes()
                            .name("Application Key for managing dashboards-updated")));

    try {
      PartialApplicationKeyResponse result =
          apiInstance.updateServiceAccountApplicationKey(
              SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceAccountsApi#updateServiceAccountApplicationKey");
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

#####  Edit an application key for this service account returns "OK" response
```
"""
Edit an application key for this service account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_update_attributes import ApplicationKeyUpdateAttributes
from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData
from datadog_api_client.v2.model.application_key_update_request import ApplicationKeyUpdateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME = environ["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME"]
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = environ["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]

body = ApplicationKeyUpdateRequest(
    data=ApplicationKeyUpdateData(
        id=SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
        type=ApplicationKeysType.APPLICATION_KEYS,
        attributes=ApplicationKeyUpdateAttributes(
            name="Application Key for managing dashboards-updated",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.update_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, app_key_id=SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID, body=body
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit an application key for this service account returns "OK" response
```
# Edit an application key for this service account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME = ENV["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME"]
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = ENV["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]

body = DatadogAPIClient::V2::ApplicationKeyUpdateRequest.new({
  data: DatadogAPIClient::V2::ApplicationKeyUpdateData.new({
    id: SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
    type: DatadogAPIClient::V2::ApplicationKeysType::APPLICATION_KEYS,
    attributes: DatadogAPIClient::V2::ApplicationKeyUpdateAttributes.new({
      name: "Application Key for managing dashboards-updated",
    }),
  }),
})
p api_instance.update_service_account_application_key(SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit an application key for this service account returns "OK" response
```
// Edit an application key for this service account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_accounts::ServiceAccountsAPI;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateAttributes;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateData;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateRequest;
use datadog_api_client::datadogV2::model::ApplicationKeysType;

#[tokio::main]
async fn main() {
    // there is a valid "service_account_user" in the system
    let service_account_user_data_id = std::env::var("SERVICE_ACCOUNT_USER_DATA_ID").unwrap();

    // there is a valid "service_account_application_key" for "service_account_user"
    let service_account_application_key_data_id =
        std::env::var("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID").unwrap();
    let body = ApplicationKeyUpdateRequest::new(ApplicationKeyUpdateData::new(
        ApplicationKeyUpdateAttributes::new()
            .name("Application Key for managing dashboards-updated".to_string()),
        service_account_application_key_data_id.clone(),
        ApplicationKeysType::APPLICATION_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceAccountsAPI::with_config(configuration);
    let resp = api
        .update_service_account_application_key(
            service_account_user_data_id.clone(),
            service_account_application_key_data_id.clone(),
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Edit an application key for this service account returns "OK" response
```
/**
 * Edit an application key for this service account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceAccountsApi(configuration);

// there is a valid "service_account_user" in the system
const SERVICE_ACCOUNT_USER_DATA_ID = process.env
  .SERVICE_ACCOUNT_USER_DATA_ID as string;

// there is a valid "service_account_application_key" for "service_account_user"
const SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = process.env
  .SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID as string;

const params: v2.ServiceAccountsApiUpdateServiceAccountApplicationKeyRequest = {
  body: {
    data: {
      id: SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
      type: "application_keys",
      attributes: {
        name: "Application Key for managing dashboards-updated",
      },
    },
  },
  serviceAccountId: SERVICE_ACCOUNT_USER_DATA_ID,
  appKeyId: SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
};

apiInstance
  .updateServiceAccountApplicationKey(params)
  .then((data: v2.PartialApplicationKeyResponse) => {
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
## [Delete an application key for this service account](https://docs.datadoghq.com/api/latest/service-accounts/#delete-an-application-key-for-this-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-accounts/#delete-an-application-key-for-this-service-account-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}
### Overview
Delete an application key owned by this service account. This endpoint requires the `service_account_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_account_id [_required_]
string
The ID of the service account.
app_key_id [_required_]
string
The ID of the application key.
### Response
  * [204](https://docs.datadoghq.com/api/latest/service-accounts/#DeleteServiceAccountApplicationKey-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-accounts/#DeleteServiceAccountApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-accounts/#DeleteServiceAccountApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-accounts/#DeleteServiceAccountApplicationKey-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=typescript)


#####  Delete an application key for this service account
Copy
```
                  # Path parameters  
export service_account_id="00000000-0000-1234-0000-000000000000"  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an application key for this service account
```
"""
Delete an application key for this service account returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = environ["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    api_instance.delete_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID,
        app_key_id=SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an application key for this service account
```
# Delete an application key for this service account returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = ENV["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]
api_instance.delete_service_account_application_key(SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an application key for this service account
```
// Delete an application key for this service account returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "service_account_user" in the system
	ServiceAccountUserDataID := os.Getenv("SERVICE_ACCOUNT_USER_DATA_ID")

	// there is a valid "service_account_application_key" for "service_account_user"
	ServiceAccountApplicationKeyDataID := os.Getenv("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceAccountsApi(apiClient)
	r, err := api.DeleteServiceAccountApplicationKey(ctx, ServiceAccountUserDataID, ServiceAccountApplicationKeyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceAccountsApi.DeleteServiceAccountApplicationKey`: %v\n", err)
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

#####  Delete an application key for this service account
```
// Delete an application key for this service account returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceAccountsApi apiInstance = new ServiceAccountsApi(defaultClient);

    // there is a valid "service_account_user" in the system
    String SERVICE_ACCOUNT_USER_DATA_ID = System.getenv("SERVICE_ACCOUNT_USER_DATA_ID");

    // there is a valid "service_account_application_key" for "service_account_user"
    String SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID =
        System.getenv("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID");

    try {
      apiInstance.deleteServiceAccountApplicationKey(
          SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceAccountsApi#deleteServiceAccountApplicationKey");
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

#####  Delete an application key for this service account
```
// Delete an application key for this service account returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_accounts::ServiceAccountsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "service_account_user" in the system
    let service_account_user_data_id = std::env::var("SERVICE_ACCOUNT_USER_DATA_ID").unwrap();

    // there is a valid "service_account_application_key" for "service_account_user"
    let service_account_application_key_data_id =
        std::env::var("SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceAccountsAPI::with_config(configuration);
    let resp = api
        .delete_service_account_application_key(
            service_account_user_data_id.clone(),
            service_account_application_key_data_id.clone(),
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete an application key for this service account
```
/**
 * Delete an application key for this service account returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceAccountsApi(configuration);

// there is a valid "service_account_user" in the system
const SERVICE_ACCOUNT_USER_DATA_ID = process.env
  .SERVICE_ACCOUNT_USER_DATA_ID as string;

// there is a valid "service_account_application_key" for "service_account_user"
const SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = process.env
  .SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID as string;

const params: v2.ServiceAccountsApiDeleteServiceAccountApplicationKeyRequest = {
  serviceAccountId: SERVICE_ACCOUNT_USER_DATA_ID,
  appKeyId: SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
};

apiInstance
  .deleteServiceAccountApplicationKey(params)
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
## [Create an application key for this service account](https://docs.datadoghq.com/api/latest/service-accounts/#create-an-application-key-for-this-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-accounts/#create-an-application-key-for-this-service-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys
### Overview
Create an application key for this service account. This endpoint requires the `service_account_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_account_id [_required_]
string
The ID of the service account.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Field
Type
Description
data [_required_]
object
Object used to create an application key.
attributes [_required_]
object
Attributes used to create an application Key.
name [_required_]
string
Name of the application key.
scopes
[string]
Array of scopes to grant the application key.
type [_required_]
enum
Application Keys resource type. Allowed enum values: `application_keys`
default: `application_keys`
#####  Create an application key for this service account returns "Created" response
```
{
  "data": {
    "attributes": {
      "name": "Example-Service-Account"
    },
    "type": "application_keys"
  }
}
```

Copy
#####  Create an application key with scopes for this service account returns "Created" response
```
{
  "data": {
    "attributes": {
      "name": "Example-Service-Account",
      "scopes": [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share"
      ]
    },
    "type": "application_keys"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccountApplicationKey-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccountApplicationKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccountApplicationKey-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-accounts/#CreateServiceAccountApplicationKey-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Response for retrieving an application key.
Field
Type
Description
data
object
Datadog application key.
attributes
object
Attributes of a full application key.
created_at
date-time
Creation date of the application key.
key
string
The application key.
last4
string
The last four characters of the application key.
last_used_at
date-time
Last usage timestamp of the application key.
name
string
Name of the application key.
scopes
[string]
Array of scopes to grant the application key.
id
string
ID of the application key.
relationships
object
Resources related to the application key.
owned_by
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
Application Keys resource type. Allowed enum values: `application_keys`
default: `application_keys`
included
[ <oneOf>]
Array of objects related to the application key.
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
The definition of LeakedKey object.
attributes [_required_]
object
The definition of LeakedKeyAttributes object.
date [_required_]
date-time
The LeakedKeyAttributes date.
leak_source
string
The LeakedKeyAttributes leak_source.
id [_required_]
string
The LeakedKey id.
type [_required_]
enum
The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`
default: `leaked_keys`
```
{
  "data": {
    "attributes": {
      "created_at": "2020-11-23T10:00:00.000Z",
      "key": "string",
      "last4": "abcd",
      "last_used_at": "2020-12-20T10:00:00.000Z",
      "name": "Application Key for managing dashboards",
      "scopes": [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share"
      ]
    },
    "id": "string",
    "relationships": {
      "owned_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "application_keys"
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=typescript)


#####  Create an application key for this service account returns "Created" response
Copy
```
                          # Path parameters  
export service_account_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-Service-Account"
    },
    "type": "application_keys"
  }
}
EOF  

                        
```

#####  Create an application key with scopes for this service account returns "Created" response
Copy
```
                          # Path parameters  
export service_account_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-Service-Account",
      "scopes": [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share"
      ]
    },
    "type": "application_keys"
  }
}
EOF  

                        
```

#####  Create an application key for this service account returns "Created" response 
```
// Create an application key for this service account returns "Created" response

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
	// there is a valid "service_account_user" in the system
	ServiceAccountUserDataID := os.Getenv("SERVICE_ACCOUNT_USER_DATA_ID")

	body := datadogV2.ApplicationKeyCreateRequest{
		Data: datadogV2.ApplicationKeyCreateData{
			Attributes: datadogV2.ApplicationKeyCreateAttributes{
				Name: "Example-Service-Account",
			},
			Type: datadogV2.APPLICATIONKEYSTYPE_APPLICATION_KEYS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceAccountsApi(apiClient)
	resp, r, err := api.CreateServiceAccountApplicationKey(ctx, ServiceAccountUserDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceAccountsApi.CreateServiceAccountApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceAccountsApi.CreateServiceAccountApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#####  Create an application key with scopes for this service account returns "Created" response 
```
// Create an application key with scopes for this service account returns "Created" response

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
	// there is a valid "service_account_user" in the system
	ServiceAccountUserDataID := os.Getenv("SERVICE_ACCOUNT_USER_DATA_ID")

	body := datadogV2.ApplicationKeyCreateRequest{
		Data: datadogV2.ApplicationKeyCreateData{
			Attributes: datadogV2.ApplicationKeyCreateAttributes{
				Name: "Example-Service-Account",
				Scopes: *datadog.NewNullableList(&[]string{
					"dashboards_read",
					"dashboards_write",
					"dashboards_public_share",
				}),
			},
			Type: datadogV2.APPLICATIONKEYSTYPE_APPLICATION_KEYS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceAccountsApi(apiClient)
	resp, r, err := api.CreateServiceAccountApplicationKey(ctx, ServiceAccountUserDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceAccountsApi.CreateServiceAccountApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceAccountsApi.CreateServiceAccountApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an application key for this service account returns "Created" response 
```
// Create an application key for this service account returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceAccountsApi;
import com.datadog.api.client.v2.model.ApplicationKeyCreateAttributes;
import com.datadog.api.client.v2.model.ApplicationKeyCreateData;
import com.datadog.api.client.v2.model.ApplicationKeyCreateRequest;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;
import com.datadog.api.client.v2.model.ApplicationKeysType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceAccountsApi apiInstance = new ServiceAccountsApi(defaultClient);

    // there is a valid "service_account_user" in the system
    String SERVICE_ACCOUNT_USER_DATA_ID = System.getenv("SERVICE_ACCOUNT_USER_DATA_ID");

    ApplicationKeyCreateRequest body =
        new ApplicationKeyCreateRequest()
            .data(
                new ApplicationKeyCreateData()
                    .attributes(
                        new ApplicationKeyCreateAttributes().name("Example-Service-Account"))
                    .type(ApplicationKeysType.APPLICATION_KEYS));

    try {
      ApplicationKeyResponse result =
          apiInstance.createServiceAccountApplicationKey(SERVICE_ACCOUNT_USER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceAccountsApi#createServiceAccountApplicationKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create an application key with scopes for this service account returns "Created" response 
```
// Create an application key with scopes for this service account returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceAccountsApi;
import com.datadog.api.client.v2.model.ApplicationKeyCreateAttributes;
import com.datadog.api.client.v2.model.ApplicationKeyCreateData;
import com.datadog.api.client.v2.model.ApplicationKeyCreateRequest;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;
import com.datadog.api.client.v2.model.ApplicationKeysType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceAccountsApi apiInstance = new ServiceAccountsApi(defaultClient);

    // there is a valid "service_account_user" in the system
    String SERVICE_ACCOUNT_USER_DATA_ID = System.getenv("SERVICE_ACCOUNT_USER_DATA_ID");

    ApplicationKeyCreateRequest body =
        new ApplicationKeyCreateRequest()
            .data(
                new ApplicationKeyCreateData()
                    .attributes(
                        new ApplicationKeyCreateAttributes()
                            .name("Example-Service-Account")
                            .scopes(
                                Arrays.asList(
                                    "dashboards_read",
                                    "dashboards_write",
                                    "dashboards_public_share")))
                    .type(ApplicationKeysType.APPLICATION_KEYS));

    try {
      ApplicationKeyResponse result =
          apiInstance.createServiceAccountApplicationKey(SERVICE_ACCOUNT_USER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceAccountsApi#createServiceAccountApplicationKey");
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

#####  Create an application key for this service account returns "Created" response 
```
"""
Create an application key for this service account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

body = ApplicationKeyCreateRequest(
    data=ApplicationKeyCreateData(
        attributes=ApplicationKeyCreateAttributes(
            name="Example-Service-Account",
        ),
        type=ApplicationKeysType.APPLICATION_KEYS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, body=body
    )

    print(response)

```

Copy
#####  Create an application key with scopes for this service account returns "Created" response 
```
"""
Create an application key with scopes for this service account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

body = ApplicationKeyCreateRequest(
    data=ApplicationKeyCreateData(
        attributes=ApplicationKeyCreateAttributes(
            name="Example-Service-Account",
            scopes=[
                "dashboards_read",
                "dashboards_write",
                "dashboards_public_share",
            ],
        ),
        type=ApplicationKeysType.APPLICATION_KEYS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, body=body
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an application key for this service account returns "Created" response 
```
# Create an application key for this service account returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]

body = DatadogAPIClient::V2::ApplicationKeyCreateRequest.new({
  data: DatadogAPIClient::V2::ApplicationKeyCreateData.new({
    attributes: DatadogAPIClient::V2::ApplicationKeyCreateAttributes.new({
      name: "Example-Service-Account",
    }),
    type: DatadogAPIClient::V2::ApplicationKeysType::APPLICATION_KEYS,
  }),
})
p api_instance.create_service_account_application_key(SERVICE_ACCOUNT_USER_DATA_ID, body)

```

Copy
#####  Create an application key with scopes for this service account returns "Created" response 
```
# Create an application key with scopes for this service account returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]

body = DatadogAPIClient::V2::ApplicationKeyCreateRequest.new({
  data: DatadogAPIClient::V2::ApplicationKeyCreateData.new({
    attributes: DatadogAPIClient::V2::ApplicationKeyCreateAttributes.new({
      name: "Example-Service-Account",
      scopes: [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share",
      ],
    }),
    type: DatadogAPIClient::V2::ApplicationKeysType::APPLICATION_KEYS,
  }),
})
p api_instance.create_service_account_application_key(SERVICE_ACCOUNT_USER_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an application key for this service account returns "Created" response 
```
// Create an application key for this service account returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_accounts::ServiceAccountsAPI;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateAttributes;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateData;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateRequest;
use datadog_api_client::datadogV2::model::ApplicationKeysType;

#[tokio::main]
async fn main() {
    // there is a valid "service_account_user" in the system
    let service_account_user_data_id = std::env::var("SERVICE_ACCOUNT_USER_DATA_ID").unwrap();
    let body = ApplicationKeyCreateRequest::new(ApplicationKeyCreateData::new(
        ApplicationKeyCreateAttributes::new("Example-Service-Account".to_string()),
        ApplicationKeysType::APPLICATION_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceAccountsAPI::with_config(configuration);
    let resp = api
        .create_service_account_application_key(service_account_user_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create an application key with scopes for this service account returns "Created" response 
```
// Create an application key with scopes for this service account returns
// "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_accounts::ServiceAccountsAPI;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateAttributes;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateData;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateRequest;
use datadog_api_client::datadogV2::model::ApplicationKeysType;

#[tokio::main]
async fn main() {
    // there is a valid "service_account_user" in the system
    let service_account_user_data_id = std::env::var("SERVICE_ACCOUNT_USER_DATA_ID").unwrap();
    let body = ApplicationKeyCreateRequest::new(ApplicationKeyCreateData::new(
        ApplicationKeyCreateAttributes::new("Example-Service-Account".to_string()).scopes(Some(
            vec![
                "dashboards_read".to_string(),
                "dashboards_write".to_string(),
                "dashboards_public_share".to_string(),
            ],
        )),
        ApplicationKeysType::APPLICATION_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceAccountsAPI::with_config(configuration);
    let resp = api
        .create_service_account_application_key(service_account_user_data_id.clone(), body)
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

#####  Create an application key for this service account returns "Created" response 
```
/**
 * Create an application key for this service account returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceAccountsApi(configuration);

// there is a valid "service_account_user" in the system
const SERVICE_ACCOUNT_USER_DATA_ID = process.env
  .SERVICE_ACCOUNT_USER_DATA_ID as string;

const params: v2.ServiceAccountsApiCreateServiceAccountApplicationKeyRequest = {
  body: {
    data: {
      attributes: {
        name: "Example-Service-Account",
      },
      type: "application_keys",
    },
  },
  serviceAccountId: SERVICE_ACCOUNT_USER_DATA_ID,
};

apiInstance
  .createServiceAccountApplicationKey(params)
  .then((data: v2.ApplicationKeyResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create an application key with scopes for this service account returns "Created" response 
```
/**
 * Create an application key with scopes for this service account returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceAccountsApi(configuration);

// there is a valid "service_account_user" in the system
const SERVICE_ACCOUNT_USER_DATA_ID = process.env
  .SERVICE_ACCOUNT_USER_DATA_ID as string;

const params: v2.ServiceAccountsApiCreateServiceAccountApplicationKeyRequest = {
  body: {
    data: {
      attributes: {
        name: "Example-Service-Account",
        scopes: [
          "dashboards_read",
          "dashboards_write",
          "dashboards_public_share",
        ],
      },
      type: "application_keys",
    },
  },
  serviceAccountId: SERVICE_ACCOUNT_USER_DATA_ID,
};

apiInstance
  .createServiceAccountApplicationKey(params)
  .then((data: v2.ApplicationKeyResponse) => {
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
## [List application keys for this service account](https://docs.datadoghq.com/api/latest/service-accounts/#list-application-keys-for-this-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-accounts/#list-application-keys-for-this-service-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keyshttps://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys
### Overview
List all application keys available for this service account. This endpoint requires the `service_account_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_account_id [_required_]
string
The ID of the service account.
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
Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign.  
Allowed enum values: `created_at, -created_at, last4, -last4, name, -name`
filter
string
Filter application keys by the specified string.
filter[created_at][start]
string
Only include application keys created on or after the specified date.
filter[created_at][end]
string
Only include application keys created on or before the specified date.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-accounts/#ListServiceAccountApplicationKeys-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-accounts/#ListServiceAccountApplicationKeys-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-accounts/#ListServiceAccountApplicationKeys-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-accounts/#ListServiceAccountApplicationKeys-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-accounts/#ListServiceAccountApplicationKeys-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


Response for a list of application keys.
Field
Type
Description
data
[object]
Array of application keys.
attributes
object
Attributes of a partial application key.
created_at
string
Creation date of the application key.
last4
string
The last four characters of the application key.
last_used_at
string
Last usage timestamp of the application key.
name
string
Name of the application key.
scopes
[string]
Array of scopes to grant the application key.
id
string
ID of the application key.
relationships
object
Resources related to the application key.
owned_by
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
Application Keys resource type. Allowed enum values: `application_keys`
default: `application_keys`
included
[ <oneOf>]
Array of objects related to the application key.
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
The definition of LeakedKey object.
attributes [_required_]
object
The definition of LeakedKeyAttributes object.
date [_required_]
date-time
The LeakedKeyAttributes date.
leak_source
string
The LeakedKeyAttributes leak_source.
id [_required_]
string
The LeakedKey id.
type [_required_]
enum
The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`
default: `leaked_keys`
meta
object
Additional information related to the application key response.
max_allowed_per_user
int64
Max allowed number of application keys per user.
page
object
Additional information related to the application key response.
total_filtered_count
int64
Total filtered application key count.
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2020-11-23T10:00:00.000Z",
        "last4": "abcd",
        "last_used_at": "2020-12-20T10:00:00.000Z",
        "name": "Application Key for managing dashboards",
        "scopes": [
          "dashboards_read",
          "dashboards_write",
          "dashboards_public_share"
        ]
      },
      "id": "string",
      "relationships": {
        "owned_by": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "application_keys"
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
    "max_allowed_per_user": "integer",
    "page": {
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/service-accounts/)
  * [Example](https://docs.datadoghq.com/api/latest/service-accounts/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-accounts/?code-lang=typescript)


#####  List application keys for this service account
Copy
```
                  # Path parameters  
export service_account_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List application keys for this service account
```
"""
List application keys for this service account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.list_service_account_application_keys(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List application keys for this service account
```
# List application keys for this service account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]
p api_instance.list_service_account_application_keys(SERVICE_ACCOUNT_USER_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List application keys for this service account
```
// List application keys for this service account returns "OK" response

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
	// there is a valid "service_account_user" in the system
	ServiceAccountUserDataID := os.Getenv("SERVICE_ACCOUNT_USER_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceAccountsApi(apiClient)
	resp, r, err := api.ListServiceAccountApplicationKeys(ctx, ServiceAccountUserDataID, *datadogV2.NewListServiceAccountApplicationKeysOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceAccountsApi.ListServiceAccountApplicationKeys`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceAccountsApi.ListServiceAccountApplicationKeys`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List application keys for this service account
```
// List application keys for this service account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceAccountsApi;
import com.datadog.api.client.v2.model.ListApplicationKeysResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceAccountsApi apiInstance = new ServiceAccountsApi(defaultClient);

    // there is a valid "service_account_user" in the system
    String SERVICE_ACCOUNT_USER_DATA_ID = System.getenv("SERVICE_ACCOUNT_USER_DATA_ID");

    try {
      ListApplicationKeysResponse result =
          apiInstance.listServiceAccountApplicationKeys(SERVICE_ACCOUNT_USER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceAccountsApi#listServiceAccountApplicationKeys");
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

#####  List application keys for this service account
```
// List application keys for this service account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_accounts::ListServiceAccountApplicationKeysOptionalParams;
use datadog_api_client::datadogV2::api_service_accounts::ServiceAccountsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "service_account_user" in the system
    let service_account_user_data_id = std::env::var("SERVICE_ACCOUNT_USER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceAccountsAPI::with_config(configuration);
    let resp = api
        .list_service_account_application_keys(
            service_account_user_data_id.clone(),
            ListServiceAccountApplicationKeysOptionalParams::default(),
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List application keys for this service account
```
/**
 * List application keys for this service account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceAccountsApi(configuration);

// there is a valid "service_account_user" in the system
const SERVICE_ACCOUNT_USER_DATA_ID = process.env
  .SERVICE_ACCOUNT_USER_DATA_ID as string;

const params: v2.ServiceAccountsApiListServiceAccountApplicationKeysRequest = {
  serviceAccountId: SERVICE_ACCOUNT_USER_DATA_ID,
};

apiInstance
  .listServiceAccountApplicationKeys(params)
  .then((data: v2.ListApplicationKeysResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=bfa410bd-738f-490b-997a-a1f334b0849d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=e1b859e5-bd30-44ab-896b-07da295847e3&pt=Service%20Accounts&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-accounts%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=bfa410bd-738f-490b-997a-a1f334b0849d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=e1b859e5-bd30-44ab-896b-07da295847e3&pt=Service%20Accounts&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-accounts%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
Feedback
## Was this page helpful?
Yes 🎉
No 👎
Next
![](https://survey-images.hotjar.com/surveys/logo/90f40352a7464c849f5ce82ccd0e758d)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=6deebc6f-5b46-4b20-b43b-463f07215e50&bo=2&sid=e7969980f0bf11f08c054320cbbd0092&vid=e7972810f0bf11f09bf29f699b2daf47&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Service%20Accounts&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-accounts%2F&r=&lt=1862&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=653679)
