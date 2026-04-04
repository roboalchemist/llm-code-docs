# Source: https://docs.datadoghq.com/api/latest/users

# Users
Create, edit, and disable users.
## [Create a user](https://docs.datadoghq.com/api/latest/users/#create-a-user)
  * [v1](https://docs.datadoghq.com/api/latest/users/#create-a-user-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#create-a-user-v2)


POST https://api.ap1.datadoghq.com/api/v1/userhttps://api.ap2.datadoghq.com/api/v1/userhttps://api.datadoghq.eu/api/v1/userhttps://api.ddog-gov.com/api/v1/userhttps://api.datadoghq.com/api/v1/userhttps://api.us3.datadoghq.com/api/v1/userhttps://api.us5.datadoghq.com/api/v1/user
### Overview
Create a user for your organization.
**Note** : Users can only be created with the admin access role if application keys belong to administrators.
This endpoint requires the `user_access_invite` permission.
### Request
#### Body Data (required)
User object that needs to be created.
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Expand All
Field
Type
Description
access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
disabled
boolean
The new disabled status of the user.
email
string
The new email of the user.
handle
string
The user handle, must be a valid email.
icon
string
Gravatar icon associated to the user.
name
string
The name of the user.
verified
boolean
Whether or not the user logged in Datadog at least once.
```
{
  "access_role": null,
  "disabled": false,
  "email": "test@datadoghq.com",
  "handle": "test@datadoghq.com",
  "name": "test user"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#CreateUser-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/users/#CreateUser-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/users/#CreateUser-403-v1)
  * [409](https://docs.datadoghq.com/api/latest/users/#CreateUser-409-v1)
  * [429](https://docs.datadoghq.com/api/latest/users/#CreateUser-429-v1)


User created
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


A Datadog User.
Field
Type
Description
user
object
Create, edit, and disable users.
access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
disabled
boolean
The new disabled status of the user.
email
string
The new email of the user.
handle
string
The user handle, must be a valid email.
icon
string
Gravatar icon associated to the user.
name
string
The name of the user.
verified
boolean
Whether or not the user logged in Datadog at least once.
```
{
  "user": {
    "access_role": "ro",
    "disabled": false,
    "email": "test@datadoghq.com",
    "handle": "test@datadoghq.com",
    "icon": "/path/to/matching/gravatar/icon",
    "name": "test user",
    "verified": true
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Create a user returns null access role
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "access_role": null,
  "disabled": false,
  "email": "test@datadoghq.com",
  "handle": "test@datadoghq.com",
  "name": "test user"
}
EOF  

                        
```

#####  Create a user returns null access role
```
// Create a user returns null access role

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.User{
		AccessRole: *datadogV1.NewNullableAccessRole(nil),
		Disabled:   datadog.PtrBool(false),
		Email:      datadog.PtrString("test@datadoghq.com"),
		Handle:     datadog.PtrString("test@datadoghq.com"),
		Name:       datadog.PtrString("test user"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsersApi(apiClient)
	resp, r, err := api.CreateUser(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.CreateUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.CreateUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a user returns null access role
```
// Create a user returns null access role

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsersApi;
import com.datadog.api.client.v1.model.User;
import com.datadog.api.client.v1.model.UserResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    User body =
        new User()
            .accessRole(null)
            .disabled(false)
            .email("test@datadoghq.com")
            .handle("test@datadoghq.com")
            .name("test user");

    try {
      UserResponse result = apiInstance.createUser(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#createUser");
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

#####  Create a user returns null access role
```
"""
Create a user returns null access role
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi
from datadog_api_client.v1.model.user import User

body = User(
    access_role=None,
    disabled=False,
    email="test@datadoghq.com",
    handle="test@datadoghq.com",
    name="test user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.create_user(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a user returns null access role
```
# Create a user returns null access role

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new

body = DatadogAPIClient::V1::User.new({
  access_role: nil,
  disabled: false,
  email: "test@datadoghq.com",
  handle: "test@datadoghq.com",
  name: "test user",
})
p api_instance.create_user(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a user returns null access role
```
// Create a user returns null access role
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_users::UsersAPI;
use datadog_api_client::datadogV1::model::User;

#[tokio::main]
async fn main() {
    let body = User::new()
        .access_role(None)
        .disabled(false)
        .email("test@datadoghq.com".to_string())
        .handle("test@datadoghq.com".to_string())
        .name("test user".to_string());
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.create_user(body).await;
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

#####  Create a user returns null access role
```
/**
 * Create a user returns null access role
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsersApi(configuration);

const params: v1.UsersApiCreateUserRequest = {
  body: {
    accessRole: undefined,
    disabled: false,
    email: "test@datadoghq.com",
    handle: "test@datadoghq.com",
    name: "test user",
  },
};

apiInstance
  .createUser(params)
  .then((data: v1.UserResponse) => {
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

POST https://api.ap1.datadoghq.com/api/v2/usershttps://api.ap2.datadoghq.com/api/v2/usershttps://api.datadoghq.eu/api/v2/usershttps://api.ddog-gov.com/api/v2/usershttps://api.datadoghq.com/api/v2/usershttps://api.us3.datadoghq.com/api/v2/usershttps://api.us5.datadoghq.com/api/v2/users
### Overview
Create a user for your organization. This endpoint requires the `user_access_invite` permission.
OAuth apps require the `user_access_invite` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Field
Type
Description
data [_required_]
object
Object to create a user.
attributes [_required_]
object
Attributes of the created user.
email [_required_]
string
The email of the user.
name
string
The name of the user.
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
      "name": "Datadog API Client Python",
      "email": "Example-User@datadoghq.com"
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/users/#CreateUser-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/users/#CreateUser-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#CreateUser-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#CreateUser-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Create a user returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "users",
    "attributes": {
      "name": "Datadog API Client Python",
      "email": "Example-User@datadoghq.com"
    }
  }
}
EOF  

                        
```

#####  Create a user returns "OK" response
```
// Create a user returns "OK" response

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
	body := datadogV2.UserCreateRequest{
		Data: datadogV2.UserCreateData{
			Type: datadogV2.USERSTYPE_USERS,
			Attributes: datadogV2.UserCreateAttributes{
				Name:  datadog.PtrString("Datadog API Client Python"),
				Email: "Example-User@datadoghq.com",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.CreateUser(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.CreateUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.CreateUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a user returns "OK" response
```
// Create a user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.model.UserCreateAttributes;
import com.datadog.api.client.v2.model.UserCreateData;
import com.datadog.api.client.v2.model.UserCreateRequest;
import com.datadog.api.client.v2.model.UserResponse;
import com.datadog.api.client.v2.model.UsersType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    UserCreateRequest body =
        new UserCreateRequest()
            .data(
                new UserCreateData()
                    .type(UsersType.USERS)
                    .attributes(
                        new UserCreateAttributes()
                            .name("Datadog API Client Python")
                            .email("Example-User@datadoghq.com")));

    try {
      UserResponse result = apiInstance.createUser(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#createUser");
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

#####  Create a user returns "OK" response
```
"""
Create a user returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.user_create_attributes import UserCreateAttributes
from datadog_api_client.v2.model.user_create_data import UserCreateData
from datadog_api_client.v2.model.user_create_request import UserCreateRequest
from datadog_api_client.v2.model.users_type import UsersType

body = UserCreateRequest(
    data=UserCreateData(
        type=UsersType.USERS,
        attributes=UserCreateAttributes(
            name="Datadog API Client Python",
            email="Example-User@datadoghq.com",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.create_user(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a user returns "OK" response
```
# Create a user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

body = DatadogAPIClient::V2::UserCreateRequest.new({
  data: DatadogAPIClient::V2::UserCreateData.new({
    type: DatadogAPIClient::V2::UsersType::USERS,
    attributes: DatadogAPIClient::V2::UserCreateAttributes.new({
      name: "Datadog API Client Python",
      email: "Example-User@datadoghq.com",
    }),
  }),
})
p api_instance.create_user(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a user returns "OK" response
```
// Create a user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;
use datadog_api_client::datadogV2::model::UserCreateAttributes;
use datadog_api_client::datadogV2::model::UserCreateData;
use datadog_api_client::datadogV2::model::UserCreateRequest;
use datadog_api_client::datadogV2::model::UsersType;

#[tokio::main]
async fn main() {
    let body = UserCreateRequest::new(UserCreateData::new(
        UserCreateAttributes::new("Example-User@datadoghq.com".to_string())
            .name("Datadog API Client Python".to_string()),
        UsersType::USERS,
    ));
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.create_user(body).await;
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

#####  Create a user returns "OK" response
```
/**
 * Create a user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

const params: v2.UsersApiCreateUserRequest = {
  body: {
    data: {
      type: "users",
      attributes: {
        name: "Datadog API Client Python",
        email: "Example-User@datadoghq.com",
      },
    },
  },
};

apiInstance
  .createUser(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List all users](https://docs.datadoghq.com/api/latest/users/#list-all-users)
  * [v1](https://docs.datadoghq.com/api/latest/users/#list-all-users-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#list-all-users-v2)


GET https://api.ap1.datadoghq.com/api/v1/userhttps://api.ap2.datadoghq.com/api/v1/userhttps://api.datadoghq.eu/api/v1/userhttps://api.ddog-gov.com/api/v1/userhttps://api.datadoghq.com/api/v1/userhttps://api.us3.datadoghq.com/api/v1/userhttps://api.us5.datadoghq.com/api/v1/user
### Overview
List all users for your organization. This endpoint requires the `user_access_read` permission.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#ListUsers-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/users/#ListUsers-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/users/#ListUsers-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Array of Datadog users for a given organization.
Field
Type
Description
users
[object]
Array of users.
access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
disabled
boolean
The new disabled status of the user.
email
string
The new email of the user.
handle
string
The user handle, must be a valid email.
icon
string
Gravatar icon associated to the user.
name
string
The name of the user.
verified
boolean
Whether or not the user logged in Datadog at least once.
```
{
  "users": [
    {
      "access_role": "ro",
      "disabled": false,
      "email": "test@datadoghq.com",
      "handle": "test@datadoghq.com",
      "icon": "/path/to/matching/gravatar/icon",
      "name": "test user",
      "verified": true
    }
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  List all users
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all users
```
"""
List all users returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.list_users()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List all users
```
# List all users returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new
p api_instance.list_users()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List all users
```
// List all users returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsersApi(apiClient)
	resp, r, err := api.ListUsers(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.ListUsers`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.ListUsers`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List all users
```
// List all users returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsersApi;
import com.datadog.api.client.v1.model.UserListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    try {
      UserListResponse result = apiInstance.listUsers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUsers");
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

#####  List all users
```
// List all users returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.list_users().await;
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

#####  List all users
```
/**
 * List all users returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsersApi(configuration);

apiInstance
  .listUsers()
  .then((data: v1.UserListResponse) => {
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

GET https://api.ap1.datadoghq.com/api/v2/usershttps://api.ap2.datadoghq.com/api/v2/usershttps://api.datadoghq.eu/api/v2/usershttps://api.ddog-gov.com/api/v2/usershttps://api.datadoghq.com/api/v2/usershttps://api.us3.datadoghq.com/api/v2/usershttps://api.us5.datadoghq.com/api/v2/users
### Overview
Get the list of all users in the organization. This list includes all users even if they are deactivated or unverified. This endpoint requires the `user_access_read` permission.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
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
string
User attribute to order results by. Sort order is ascending by default. Sort order is descending if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `modified_at`, `user_count`.
sort_dir
enum
Direction of sort. Options: `asc`, `desc`.  
Allowed enum values: `asc, desc`
filter
string
Filter all users by the given string. Defaults to no filtering.
filter[status]
string
Filter on status attribute. Comma separated list, with possible values `Active`, `Pending`, and `Disabled`. Defaults to no filtering.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#ListUsers-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/users/#ListUsers-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#ListUsers-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#ListUsers-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Response containing information about multiple users.
Field
Type
Description
data
[object]
Array of returned users.
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
Array of objects related to the users.
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
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  List all users
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all users
```
"""
List all users returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# there is a valid "user" in the system
USER_DATA_ATTRIBUTES_EMAIL = environ["USER_DATA_ATTRIBUTES_EMAIL"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.list_users(
        filter=USER_DATA_ATTRIBUTES_EMAIL,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List all users
```
# List all users returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ATTRIBUTES_EMAIL = ENV["USER_DATA_ATTRIBUTES_EMAIL"]
opts = {
  filter: USER_DATA_ATTRIBUTES_EMAIL,
}
p api_instance.list_users(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List all users
```
// List all users returns "OK" response

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
	UserDataAttributesEmail := os.Getenv("USER_DATA_ATTRIBUTES_EMAIL")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.ListUsers(ctx, *datadogV2.NewListUsersOptionalParameters().WithFilter(UserDataAttributesEmail))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.ListUsers`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.ListUsers`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List all users
```
// List all users returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.api.UsersApi.ListUsersOptionalParameters;
import com.datadog.api.client.v2.model.UsersResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ATTRIBUTES_EMAIL = System.getenv("USER_DATA_ATTRIBUTES_EMAIL");

    try {
      UsersResponse result =
          apiInstance.listUsers(
              new ListUsersOptionalParameters().filter(USER_DATA_ATTRIBUTES_EMAIL));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUsers");
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

#####  List all users
```
// List all users returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::ListUsersOptionalParams;
use datadog_api_client::datadogV2::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_attributes_email = std::env::var("USER_DATA_ATTRIBUTES_EMAIL").unwrap();
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api
        .list_users(ListUsersOptionalParams::default().filter(user_data_attributes_email.clone()))
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

#####  List all users
```
/**
 * List all users returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ATTRIBUTES_EMAIL = process.env
  .USER_DATA_ATTRIBUTES_EMAIL as string;

const params: v2.UsersApiListUsersRequest = {
  filter: USER_DATA_ATTRIBUTES_EMAIL,
};

apiInstance
  .listUsers(params)
  .then((data: v2.UsersResponse) => {
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
## [Get user details](https://docs.datadoghq.com/api/latest/users/#get-user-details)
  * [v1](https://docs.datadoghq.com/api/latest/users/#get-user-details-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#get-user-details-v2)


GET https://api.ap1.datadoghq.com/api/v1/user/{user_handle}https://api.ap2.datadoghq.com/api/v1/user/{user_handle}https://api.datadoghq.eu/api/v1/user/{user_handle}https://api.ddog-gov.com/api/v1/user/{user_handle}https://api.datadoghq.com/api/v1/user/{user_handle}https://api.us3.datadoghq.com/api/v1/user/{user_handle}https://api.us5.datadoghq.com/api/v1/user/{user_handle}
### Overview
Get a user’s details.
### Arguments
#### Path Parameters
Name
Type
Description
user_handle [_required_]
string
The ID of the user.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#GetUser-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/users/#GetUser-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/users/#GetUser-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/users/#GetUser-429-v1)


OK for get user
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


A Datadog User.
Field
Type
Description
user
object
Create, edit, and disable users.
access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
disabled
boolean
The new disabled status of the user.
email
string
The new email of the user.
handle
string
The user handle, must be a valid email.
icon
string
Gravatar icon associated to the user.
name
string
The name of the user.
verified
boolean
Whether or not the user logged in Datadog at least once.
```
{
  "user": {
    "access_role": "ro",
    "disabled": false,
    "email": "test@datadoghq.com",
    "handle": "test@datadoghq.com",
    "icon": "/path/to/matching/gravatar/icon",
    "name": "test user",
    "verified": true
  }
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Get user details
Copy
```
                  # Path parameters  
export user_handle="test@datadoghq.com"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user/${user_handle}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get user details
```
"""
Get user details returns "OK for get user" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.get_user(
        user_handle="test@datadoghq.com",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get user details
```
# Get user details returns "OK for get user" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new
p api_instance.get_user("test@datadoghq.com")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get user details
```
// Get user details returns "OK for get user" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsersApi(apiClient)
	resp, r, err := api.GetUser(ctx, "test@datadoghq.com")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.GetUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.GetUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get user details
```
// Get user details returns "OK for get user" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsersApi;
import com.datadog.api.client.v1.model.UserResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    try {
      UserResponse result = apiInstance.getUser("test@datadoghq.com");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUser");
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

#####  Get user details
```
// Get user details returns "OK for get user" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.get_user("test@datadoghq.com".to_string()).await;
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

#####  Get user details
```
/**
 * Get user details returns "OK for get user" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsersApi(configuration);

const params: v1.UsersApiGetUserRequest = {
  userHandle: "test@datadoghq.com",
};

apiInstance
  .getUser(params)
  .then((data: v1.UserResponse) => {
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

GET https://api.ap1.datadoghq.com/api/v2/users/{user_id}https://api.ap2.datadoghq.com/api/v2/users/{user_id}https://api.datadoghq.eu/api/v2/users/{user_id}https://api.ddog-gov.com/api/v2/users/{user_id}https://api.datadoghq.com/api/v2/users/{user_id}https://api.us3.datadoghq.com/api/v2/users/{user_id}https://api.us5.datadoghq.com/api/v2/users/{user_id}
### Overview
Get a user in the organization specified by the user’s `user_id`. This endpoint requires the `user_access_read` permission.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The ID of the user.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#GetUser-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#GetUser-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/users/#GetUser-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#GetUser-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Get user details
Copy
```
                  # Path parameters  
export user_id="00000000-0000-9999-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get user details
```
"""
Get user details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.get_user(
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

#####  Get user details
```
# Get user details returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.get_user(USER_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get user details
```
// Get user details returns "OK" response

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
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.GetUser(ctx, UserDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.GetUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.GetUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get user details
```
// Get user details returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.model.UserResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    try {
      UserResponse result = apiInstance.getUser(USER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUser");
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

#####  Get user details
```
// Get user details returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.get_user(user_data_id.clone()).await;
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

#####  Get user details
```
/**
 * Get user details returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.UsersApiGetUserRequest = {
  userId: USER_DATA_ID,
};

apiInstance
  .getUser(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update a user](https://docs.datadoghq.com/api/latest/users/#update-a-user)
  * [v1](https://docs.datadoghq.com/api/latest/users/#update-a-user-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#update-a-user-v2)


PUT https://api.ap1.datadoghq.com/api/v1/user/{user_handle}https://api.ap2.datadoghq.com/api/v1/user/{user_handle}https://api.datadoghq.eu/api/v1/user/{user_handle}https://api.ddog-gov.com/api/v1/user/{user_handle}https://api.datadoghq.com/api/v1/user/{user_handle}https://api.us3.datadoghq.com/api/v1/user/{user_handle}https://api.us5.datadoghq.com/api/v1/user/{user_handle}
### Overview
Update a user information.
**Note** : It can only be used with application keys belonging to administrators.
### Arguments
#### Path Parameters
Name
Type
Description
user_handle [_required_]
string
The ID of the user.
### Request
#### Body Data (required)
Description of the update.
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Expand All
Field
Type
Description
access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
disabled
boolean
The new disabled status of the user.
email
string
The new email of the user.
handle
string
The user handle, must be a valid email.
icon
string
Gravatar icon associated to the user.
name
string
The name of the user.
verified
boolean
Whether or not the user logged in Datadog at least once.
```
{
  "access_role": "ro",
  "disabled": false,
  "email": "test@datadoghq.com",
  "handle": "test@datadoghq.com",
  "name": "test user"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#UpdateUser-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/users/#UpdateUser-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/users/#UpdateUser-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/users/#UpdateUser-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/users/#UpdateUser-429-v1)


User updated
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


A Datadog User.
Field
Type
Description
user
object
Create, edit, and disable users.
access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
disabled
boolean
The new disabled status of the user.
email
string
The new email of the user.
handle
string
The user handle, must be a valid email.
icon
string
Gravatar icon associated to the user.
name
string
The name of the user.
verified
boolean
Whether or not the user logged in Datadog at least once.
```
{
  "user": {
    "access_role": "ro",
    "disabled": false,
    "email": "test@datadoghq.com",
    "handle": "test@datadoghq.com",
    "icon": "/path/to/matching/gravatar/icon",
    "name": "test user",
    "verified": true
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Update a user
Copy
```
                  # Path parameters  
export user_handle="test@datadoghq.com"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user/${user_handle}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Update a user
```
"""
Update a user returns "User updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi
from datadog_api_client.v1.model.access_role import AccessRole
from datadog_api_client.v1.model.user import User

body = User(
    access_role=AccessRole.READ_ONLY,
    disabled=False,
    email="test@datadoghq.com",
    handle="test@datadoghq.com",
    name="test user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.update_user(user_handle="test@datadoghq.com", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a user
```
# Update a user returns "User updated" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new

body = DatadogAPIClient::V1::User.new({
  access_role: DatadogAPIClient::V1::AccessRole::READ_ONLY,
  disabled: false,
  email: "test@datadoghq.com",
  handle: "test@datadoghq.com",
  name: "test user",
})
p api_instance.update_user("test@datadoghq.com", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a user
```
// Update a user returns "User updated" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.User{
		AccessRole: *datadogV1.NewNullableAccessRole(datadogV1.ACCESSROLE_READ_ONLY.Ptr()),
		Disabled:   datadog.PtrBool(false),
		Email:      datadog.PtrString("test@datadoghq.com"),
		Handle:     datadog.PtrString("test@datadoghq.com"),
		Name:       datadog.PtrString("test user"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsersApi(apiClient)
	resp, r, err := api.UpdateUser(ctx, "test@datadoghq.com", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.UpdateUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.UpdateUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a user
```
// Update a user returns "User updated" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsersApi;
import com.datadog.api.client.v1.model.AccessRole;
import com.datadog.api.client.v1.model.User;
import com.datadog.api.client.v1.model.UserResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    User body =
        new User()
            .accessRole(AccessRole.READ_ONLY)
            .disabled(false)
            .email("test@datadoghq.com")
            .handle("test@datadoghq.com")
            .name("test user");

    try {
      UserResponse result = apiInstance.updateUser("test@datadoghq.com", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateUser");
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

#####  Update a user
```
// Update a user returns "User updated" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_users::UsersAPI;
use datadog_api_client::datadogV1::model::AccessRole;
use datadog_api_client::datadogV1::model::User;

#[tokio::main]
async fn main() {
    let body = User::new()
        .access_role(Some(AccessRole::READ_ONLY))
        .disabled(false)
        .email("test@datadoghq.com".to_string())
        .handle("test@datadoghq.com".to_string())
        .name("test user".to_string());
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api
        .update_user("test@datadoghq.com".to_string(), body)
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

#####  Update a user
```
/**
 * Update a user returns "User updated" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsersApi(configuration);

const params: v1.UsersApiUpdateUserRequest = {
  body: {
    accessRole: "ro",
    disabled: false,
    email: "test@datadoghq.com",
    handle: "test@datadoghq.com",
    name: "test user",
  },
  userHandle: "test@datadoghq.com",
};

apiInstance
  .updateUser(params)
  .then((data: v1.UserResponse) => {
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

PATCH https://api.ap1.datadoghq.com/api/v2/users/{user_id}https://api.ap2.datadoghq.com/api/v2/users/{user_id}https://api.datadoghq.eu/api/v2/users/{user_id}https://api.ddog-gov.com/api/v2/users/{user_id}https://api.datadoghq.com/api/v2/users/{user_id}https://api.us3.datadoghq.com/api/v2/users/{user_id}https://api.us5.datadoghq.com/api/v2/users/{user_id}
### Overview
Edit a user. Can only be used with an application key belonging to an administrator user. This endpoint requires any of the following permissions:
* `user_access_manage`
* `service_account_write`
  

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The ID of the user.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Field
Type
Description
data [_required_]
object
Object to update a user.
attributes [_required_]
object
Attributes of the edited user.
disabled
boolean
If the user is enabled or disabled.
email
string
The email of the user.
name
string
The name of the user.
id [_required_]
string
ID of the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "id": "string",
    "type": "users",
    "attributes": {
      "name": "updated",
      "disabled": true
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#UpdateUser-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/users/#UpdateUser-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#UpdateUser-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/users/#UpdateUser-404-v2)
  * [422](https://docs.datadoghq.com/api/latest/users/#UpdateUser-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#UpdateUser-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Update a user returns "OK" response
Copy
```
                          # Path parameters  
export user_id="00000000-0000-9999-0000-000000000000"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "string",
    "type": "users",
    "attributes": {
      "name": "updated",
      "disabled": true
    }
  }
}
EOF  

                        
```

#####  Update a user returns "OK" response
```
// Update a user returns "OK" response

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

	body := datadogV2.UserUpdateRequest{
		Data: datadogV2.UserUpdateData{
			Id:   UserDataID,
			Type: datadogV2.USERSTYPE_USERS,
			Attributes: datadogV2.UserUpdateAttributes{
				Name:     datadog.PtrString("updated"),
				Disabled: datadog.PtrBool(true),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.UpdateUser(ctx, UserDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.UpdateUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.UpdateUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a user returns "OK" response
```
// Update a user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.model.UserResponse;
import com.datadog.api.client.v2.model.UserUpdateAttributes;
import com.datadog.api.client.v2.model.UserUpdateData;
import com.datadog.api.client.v2.model.UserUpdateRequest;
import com.datadog.api.client.v2.model.UsersType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    UserUpdateRequest body =
        new UserUpdateRequest()
            .data(
                new UserUpdateData()
                    .id(USER_DATA_ID)
                    .type(UsersType.USERS)
                    .attributes(new UserUpdateAttributes().name("updated").disabled(true)));

    try {
      UserResponse result = apiInstance.updateUser(USER_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateUser");
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

#####  Update a user returns "OK" response
```
"""
Update a user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.user_update_attributes import UserUpdateAttributes
from datadog_api_client.v2.model.user_update_data import UserUpdateData
from datadog_api_client.v2.model.user_update_request import UserUpdateRequest
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserUpdateRequest(
    data=UserUpdateData(
        id=USER_DATA_ID,
        type=UsersType.USERS,
        attributes=UserUpdateAttributes(
            name="updated",
            disabled=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.update_user(user_id=USER_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a user returns "OK" response
```
# Update a user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::UserUpdateRequest.new({
  data: DatadogAPIClient::V2::UserUpdateData.new({
    id: USER_DATA_ID,
    type: DatadogAPIClient::V2::UsersType::USERS,
    attributes: DatadogAPIClient::V2::UserUpdateAttributes.new({
      name: "updated",
      disabled: true,
    }),
  }),
})
p api_instance.update_user(USER_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a user returns "OK" response
```
// Update a user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;
use datadog_api_client::datadogV2::model::UserUpdateAttributes;
use datadog_api_client::datadogV2::model::UserUpdateData;
use datadog_api_client::datadogV2::model::UserUpdateRequest;
use datadog_api_client::datadogV2::model::UsersType;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = UserUpdateRequest::new(UserUpdateData::new(
        UserUpdateAttributes::new()
            .disabled(true)
            .name("updated".to_string()),
        user_data_id.clone(),
        UsersType::USERS,
    ));
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.update_user(user_data_id.clone(), body).await;
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

#####  Update a user returns "OK" response
```
/**
 * Update a user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.UsersApiUpdateUserRequest = {
  body: {
    data: {
      id: USER_DATA_ID,
      type: "users",
      attributes: {
        name: "updated",
        disabled: true,
      },
    },
  },
  userId: USER_DATA_ID,
};

apiInstance
  .updateUser(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Disable a user](https://docs.datadoghq.com/api/latest/users/#disable-a-user)
  * [v1](https://docs.datadoghq.com/api/latest/users/#disable-a-user-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#disable-a-user-v2)


DELETE https://api.ap1.datadoghq.com/api/v1/user/{user_handle}https://api.ap2.datadoghq.com/api/v1/user/{user_handle}https://api.datadoghq.eu/api/v1/user/{user_handle}https://api.ddog-gov.com/api/v1/user/{user_handle}https://api.datadoghq.com/api/v1/user/{user_handle}https://api.us3.datadoghq.com/api/v1/user/{user_handle}https://api.us5.datadoghq.com/api/v1/user/{user_handle}
### Overview
Delete a user from an organization.
**Note** : This endpoint can only be used with application keys belonging to administrators.
### Arguments
#### Path Parameters
Name
Type
Description
user_handle [_required_]
string
The handle of the user.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#DisableUser-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/users/#DisableUser-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/users/#DisableUser-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/users/#DisableUser-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/users/#DisableUser-429-v1)


User disabled
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Array of user disabled for a given organization.
Expand All
Field
Type
Description
message
string
Information pertaining to a user disabled for a given organization.
```
{
  "message": "string"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Disable a user
Copy
```
                  # Path parameters  
export user_handle="test@datadoghq.com"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user/${user_handle}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Disable a user
```
"""
Disable a user returns "User disabled" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.disable_user(
        user_handle="test@datadoghq.com",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Disable a user
```
# Disable a user returns "User disabled" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new
p api_instance.disable_user("test@datadoghq.com")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Disable a user
```
// Disable a user returns "User disabled" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsersApi(apiClient)
	resp, r, err := api.DisableUser(ctx, "test@datadoghq.com")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.DisableUser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.DisableUser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Disable a user
```
// Disable a user returns "User disabled" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsersApi;
import com.datadog.api.client.v1.model.UserDisableResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    try {
      UserDisableResponse result = apiInstance.disableUser("test@datadoghq.com");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#disableUser");
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

#####  Disable a user
```
// Disable a user returns "User disabled" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.disable_user("test@datadoghq.com".to_string()).await;
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

#####  Disable a user
```
/**
 * Disable a user returns "User disabled" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsersApi(configuration);

const params: v1.UsersApiDisableUserRequest = {
  userHandle: "test@datadoghq.com",
};

apiInstance
  .disableUser(params)
  .then((data: v1.UserDisableResponse) => {
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

DELETE https://api.ap1.datadoghq.com/api/v2/users/{user_id}https://api.ap2.datadoghq.com/api/v2/users/{user_id}https://api.datadoghq.eu/api/v2/users/{user_id}https://api.ddog-gov.com/api/v2/users/{user_id}https://api.datadoghq.com/api/v2/users/{user_id}https://api.us3.datadoghq.com/api/v2/users/{user_id}https://api.us5.datadoghq.com/api/v2/users/{user_id}
### Overview
Disable a user. Can only be used with an application key belonging to an administrator user. This endpoint requires any of the following permissions:
* `user_access_manage`
* `service_account_write`
  

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The ID of the user.
### Response
  * [204](https://docs.datadoghq.com/api/latest/users/#DisableUser-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#DisableUser-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/users/#DisableUser-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#DisableUser-429-v2)


OK
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Disable a user
Copy
```
                  # Path parameters  
export user_id="00000000-0000-9999-0000-000000000000"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Disable a user
```
"""
Disable a user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    api_instance.disable_user(
        user_id=USER_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Disable a user
```
# Disable a user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
api_instance.disable_user(USER_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Disable a user
```
// Disable a user returns "OK" response

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

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsersApi(apiClient)
	r, err := api.DisableUser(ctx, UserDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.DisableUser`: %v\n", err)
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

#####  Disable a user
```
// Disable a user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    try {
      apiInstance.disableUser(USER_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#disableUser");
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

#####  Disable a user
```
// Disable a user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.disable_user(user_data_id.clone()).await;
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

#####  Disable a user
```
/**
 * Disable a user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.UsersApiDisableUserRequest = {
  userId: USER_DATA_ID,
};

apiInstance
  .disableUser(params)
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
## [Get a user organization](https://docs.datadoghq.com/api/latest/users/#get-a-user-organization)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#get-a-user-organization-v2)


GET https://api.ap1.datadoghq.com/api/v2/users/{user_id}/orgshttps://api.ap2.datadoghq.com/api/v2/users/{user_id}/orgshttps://api.datadoghq.eu/api/v2/users/{user_id}/orgshttps://api.ddog-gov.com/api/v2/users/{user_id}/orgshttps://api.datadoghq.com/api/v2/users/{user_id}/orgshttps://api.us3.datadoghq.com/api/v2/users/{user_id}/orgshttps://api.us5.datadoghq.com/api/v2/users/{user_id}/orgs
### Overview
Get a user organization. Returns the user information and all organizations joined by this user.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The ID of the user.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#ListUserOrganizations-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#ListUserOrganizations-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/users/#ListUserOrganizations-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#ListUserOrganizations-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Get a user organization
Copy
```
                  # Path parameters  
export user_id="00000000-0000-9999-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}/orgs" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a user organization
```
"""
Get a user organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.list_user_organizations(
        user_id="00000000-0000-9999-0000-000000000000",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a user organization
```
# Get a user organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new
p api_instance.list_user_organizations("00000000-0000-9999-0000-000000000000")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a user organization
```
// Get a user organization returns "OK" response

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
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.ListUserOrganizations(ctx, "00000000-0000-9999-0000-000000000000")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.ListUserOrganizations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.ListUserOrganizations`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a user organization
```
// Get a user organization returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.model.UserResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    try {
      UserResponse result =
          apiInstance.listUserOrganizations("00000000-0000-9999-0000-000000000000");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUserOrganizations");
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

#####  Get a user organization
```
// Get a user organization returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api
        .list_user_organizations("00000000-0000-9999-0000-000000000000".to_string())
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

#####  Get a user organization
```
/**
 * Get a user organization returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

const params: v2.UsersApiListUserOrganizationsRequest = {
  userId: "00000000-0000-9999-0000-000000000000",
};

apiInstance
  .listUserOrganizations(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a user permissions](https://docs.datadoghq.com/api/latest/users/#get-a-user-permissions)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#get-a-user-permissions-v2)


GET https://api.ap1.datadoghq.com/api/v2/users/{user_id}/permissionshttps://api.ap2.datadoghq.com/api/v2/users/{user_id}/permissionshttps://api.datadoghq.eu/api/v2/users/{user_id}/permissionshttps://api.ddog-gov.com/api/v2/users/{user_id}/permissionshttps://api.datadoghq.com/api/v2/users/{user_id}/permissionshttps://api.us3.datadoghq.com/api/v2/users/{user_id}/permissionshttps://api.us5.datadoghq.com/api/v2/users/{user_id}/permissions
### Overview
Get a user permission set. Returns a list of the user’s permissions granted by the associated user’s roles. This endpoint requires the `user_access_read` permission.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
user_id [_required_]
string
The ID of the user.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#ListUserPermissions-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#ListUserPermissions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/users/#ListUserPermissions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#ListUserPermissions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Payload with API-returned permissions.
Field
Type
Description
data
[object]
Array of permissions.
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
```
{
  "data": [
    {
      "attributes": {
        "created": "2019-09-19T10:00:00.000Z",
        "description": "string",
        "display_name": "string",
        "display_type": "string",
        "group_name": "string",
        "name": "string",
        "restricted": false
      },
      "id": "string",
      "type": "permissions"
    }
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Get a user permissions
Copy
```
                  # Path parameters  
export user_id="00000000-0000-9999-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}/permissions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a user permissions
```
"""
Get a user permissions returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.list_user_permissions(
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

#####  Get a user permissions
```
# Get a user permissions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.list_user_permissions(USER_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a user permissions
```
// Get a user permissions returns "OK" response

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
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.ListUserPermissions(ctx, UserDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.ListUserPermissions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.ListUserPermissions`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a user permissions
```
// Get a user permissions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.model.PermissionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    try {
      PermissionsResponse result = apiInstance.listUserPermissions(USER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUserPermissions");
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

#####  Get a user permissions
```
// Get a user permissions returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.list_user_permissions(user_data_id.clone()).await;
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

#####  Get a user permissions
```
/**
 * Get a user permissions returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.UsersApiListUserPermissionsRequest = {
  userId: USER_DATA_ID,
};

apiInstance
  .listUserPermissions(params)
  .then((data: v2.PermissionsResponse) => {
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
## [Send invitation emails](https://docs.datadoghq.com/api/latest/users/#send-invitation-emails)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#send-invitation-emails-v2)


POST https://api.ap1.datadoghq.com/api/v2/user_invitationshttps://api.ap2.datadoghq.com/api/v2/user_invitationshttps://api.datadoghq.eu/api/v2/user_invitationshttps://api.ddog-gov.com/api/v2/user_invitationshttps://api.datadoghq.com/api/v2/user_invitationshttps://api.us3.datadoghq.com/api/v2/user_invitationshttps://api.us5.datadoghq.com/api/v2/user_invitations
### Overview
Sends emails to one or more users inviting them to join the organization. This endpoint requires the `user_access_invite` permission.
OAuth apps require the `user_access_invite` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


Field
Type
Description
data [_required_]
[object]
List of user invitations.
relationships [_required_]
object
Relationships data for user invitation.
user [_required_]
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
User invitations type. Allowed enum values: `user_invitations`
default: `user_invitations`
```
{
  "data": [
    {
      "type": "user_invitations",
      "relationships": {
        "user": {
          "data": {
            "type": "users",
            "id": "string"
          }
        }
      }
    }
  ]
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/users/#SendInvitations-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/users/#SendInvitations-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#SendInvitations-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#SendInvitations-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


User invitations as returned by the API.
Field
Type
Description
data
[object]
Array of user invitations.
attributes
object
Attributes of a user invitation.
created_at
date-time
Creation time of the user invitation.
expires_at
date-time
Time of invitation expiration.
invite_type
string
Type of invitation.
uuid
string
UUID of the user invitation.
id
string
ID of the user invitation.
relationships
object
Relationships data for user invitation.
user [_required_]
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
User invitations type. Allowed enum values: `user_invitations`
default: `user_invitations`
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "expires_at": "2019-09-19T10:00:00.000Z",
        "invite_type": "string",
        "uuid": "string"
      },
      "id": "string",
      "relationships": {
        "user": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "user_invitations"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Send invitation emails returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/user_invitations" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "type": "user_invitations",
      "relationships": {
        "user": {
          "data": {
            "type": "users",
            "id": "string"
          }
        }
      }
    }
  ]
}
EOF  

                        
```

#####  Send invitation emails returns "OK" response
```
// Send invitation emails returns "OK" response

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

	body := datadogV2.UserInvitationsRequest{
		Data: []datadogV2.UserInvitationData{
			{
				Type: datadogV2.USERINVITATIONSTYPE_USER_INVITATIONS,
				Relationships: datadogV2.UserInvitationRelationships{
					User: datadogV2.RelationshipToUser{
						Data: datadogV2.RelationshipToUserData{
							Type: datadogV2.USERSTYPE_USERS,
							Id:   UserDataID,
						},
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.SendInvitations(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.SendInvitations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.SendInvitations`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Send invitation emails returns "OK" response
```
// Send invitation emails returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.model.RelationshipToUser;
import com.datadog.api.client.v2.model.RelationshipToUserData;
import com.datadog.api.client.v2.model.UserInvitationData;
import com.datadog.api.client.v2.model.UserInvitationRelationships;
import com.datadog.api.client.v2.model.UserInvitationsRequest;
import com.datadog.api.client.v2.model.UserInvitationsResponse;
import com.datadog.api.client.v2.model.UserInvitationsType;
import com.datadog.api.client.v2.model.UsersType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    UserInvitationsRequest body =
        new UserInvitationsRequest()
            .data(
                Collections.singletonList(
                    new UserInvitationData()
                        .type(UserInvitationsType.USER_INVITATIONS)
                        .relationships(
                            new UserInvitationRelationships()
                                .user(
                                    new RelationshipToUser()
                                        .data(
                                            new RelationshipToUserData()
                                                .type(UsersType.USERS)
                                                .id(USER_DATA_ID))))));

    try {
      UserInvitationsResponse result = apiInstance.sendInvitations(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#sendInvitations");
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

#####  Send invitation emails returns "OK" response
```
"""
Send invitation emails returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData
from datadog_api_client.v2.model.user_invitation_data import UserInvitationData
from datadog_api_client.v2.model.user_invitation_relationships import UserInvitationRelationships
from datadog_api_client.v2.model.user_invitations_request import UserInvitationsRequest
from datadog_api_client.v2.model.user_invitations_type import UserInvitationsType
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserInvitationsRequest(
    data=[
        UserInvitationData(
            type=UserInvitationsType.USER_INVITATIONS,
            relationships=UserInvitationRelationships(
                user=RelationshipToUser(
                    data=RelationshipToUserData(
                        type=UsersType.USERS,
                        id=USER_DATA_ID,
                    ),
                ),
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.send_invitations(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Send invitation emails returns "OK" response
```
# Send invitation emails returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::UserInvitationsRequest.new({
  data: [
    DatadogAPIClient::V2::UserInvitationData.new({
      type: DatadogAPIClient::V2::UserInvitationsType::USER_INVITATIONS,
      relationships: DatadogAPIClient::V2::UserInvitationRelationships.new({
        user: DatadogAPIClient::V2::RelationshipToUser.new({
          data: DatadogAPIClient::V2::RelationshipToUserData.new({
            type: DatadogAPIClient::V2::UsersType::USERS,
            id: USER_DATA_ID,
          }),
        }),
      }),
    }),
  ],
})
p api_instance.send_invitations(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Send invitation emails returns "OK" response
```
// Send invitation emails returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;
use datadog_api_client::datadogV2::model::RelationshipToUser;
use datadog_api_client::datadogV2::model::RelationshipToUserData;
use datadog_api_client::datadogV2::model::UserInvitationData;
use datadog_api_client::datadogV2::model::UserInvitationRelationships;
use datadog_api_client::datadogV2::model::UserInvitationsRequest;
use datadog_api_client::datadogV2::model::UserInvitationsType;
use datadog_api_client::datadogV2::model::UsersType;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = UserInvitationsRequest::new(vec![UserInvitationData::new(
        UserInvitationRelationships::new(RelationshipToUser::new(RelationshipToUserData::new(
            user_data_id.clone(),
            UsersType::USERS,
        ))),
        UserInvitationsType::USER_INVITATIONS,
    )]);
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.send_invitations(body).await;
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

#####  Send invitation emails returns "OK" response
```
/**
 * Send invitation emails returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.UsersApiSendInvitationsRequest = {
  body: {
    data: [
      {
        type: "user_invitations",
        relationships: {
          user: {
            data: {
              type: "users",
              id: USER_DATA_ID,
            },
          },
        },
      },
    ],
  },
};

apiInstance
  .sendInvitations(params)
  .then((data: v2.UserInvitationsResponse) => {
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
## [Get a user invitation](https://docs.datadoghq.com/api/latest/users/#get-a-user-invitation)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/users/#get-a-user-invitation-v2)


GET https://api.ap1.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid}https://api.ap2.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid}https://api.datadoghq.eu/api/v2/user_invitations/{user_invitation_uuid}https://api.ddog-gov.com/api/v2/user_invitations/{user_invitation_uuid}https://api.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid}https://api.us3.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid}https://api.us5.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid}
### Overview
Returns a single user invitation by its UUID. This endpoint requires the `user_access_invite` permission.
OAuth apps require the `user_access_invite` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
user_invitation_uuid [_required_]
string
The UUID of the user invitation.
### Response
  * [200](https://docs.datadoghq.com/api/latest/users/#GetInvitation-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/users/#GetInvitation-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/users/#GetInvitation-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/users/#GetInvitation-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


User invitation as returned by the API.
Field
Type
Description
data
object
Object of a user invitation returned by the API.
attributes
object
Attributes of a user invitation.
created_at
date-time
Creation time of the user invitation.
expires_at
date-time
Time of invitation expiration.
invite_type
string
Type of invitation.
uuid
string
UUID of the user invitation.
id
string
ID of the user invitation.
relationships
object
Relationships data for user invitation.
user [_required_]
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
User invitations type. Allowed enum values: `user_invitations`
default: `user_invitations`
```
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "expires_at": "2019-09-19T10:00:00.000Z",
      "invite_type": "string",
      "uuid": "string"
    },
    "id": "string",
    "relationships": {
      "user": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "user_invitations"
  }
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/users/)
  * [Example](https://docs.datadoghq.com/api/latest/users/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/users/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/users/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/users/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/users/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/users/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/users/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/users/?code-lang=typescript)


#####  Get a user invitation
Copy
```
                  # Path parameters  
export user_invitation_uuid="00000000-0000-0000-3456-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/user_invitations/${user_invitation_uuid}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a user invitation
```
"""
Get a user invitation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# the "user" has a "user_invitation"
USER_INVITATION_ID = environ["USER_INVITATION_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.get_invitation(
        user_invitation_uuid=USER_INVITATION_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a user invitation
```
# Get a user invitation returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# the "user" has a "user_invitation"
USER_INVITATION_ID = ENV["USER_INVITATION_ID"]
p api_instance.get_invitation(USER_INVITATION_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a user invitation
```
// Get a user invitation returns "OK" response

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
	// the "user" has a "user_invitation"
	UserInvitationID := os.Getenv("USER_INVITATION_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsersApi(apiClient)
	resp, r, err := api.GetInvitation(ctx, UserInvitationID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersApi.GetInvitation`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsersApi.GetInvitation`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a user invitation
```
// Get a user invitation returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsersApi;
import com.datadog.api.client.v2.model.UserInvitationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsersApi apiInstance = new UsersApi(defaultClient);

    // the "user" has a "user_invitation"
    String USER_INVITATION_ID = System.getenv("USER_INVITATION_ID");

    try {
      UserInvitationResponse result = apiInstance.getInvitation(USER_INVITATION_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getInvitation");
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

#####  Get a user invitation
```
// Get a user invitation returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_users::UsersAPI;

#[tokio::main]
async fn main() {
    // the "user" has a "user_invitation"
    let user_invitation_id = std::env::var("USER_INVITATION_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = UsersAPI::with_config(configuration);
    let resp = api.get_invitation(user_invitation_id.clone()).await;
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

#####  Get a user invitation
```
/**
 * Get a user invitation returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsersApi(configuration);

// the "user" has a "user_invitation"
const USER_INVITATION_ID = process.env.USER_INVITATION_ID as string;

const params: v2.UsersApiGetInvitationRequest = {
  userInvitationUuid: USER_INVITATION_ID,
};

apiInstance
  .getInvitation(params)
  .then((data: v2.UserInvitationResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a6d08e02-1013-44cb-90dd-c6e03fac86fc&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2eb5d143-ead2-41d3-849e-714429653d0e&pt=Users&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusers%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a6d08e02-1013-44cb-90dd-c6e03fac86fc&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2eb5d143-ead2-41d3-849e-714429653d0e&pt=Users&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusers%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=0aaa9c65-8285-4915-82ac-f4a7e2772924&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Users&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusers%2F&r=&lt=9690&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=845438)
