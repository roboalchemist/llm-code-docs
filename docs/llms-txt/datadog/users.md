# Source: https://docs.datadoghq.com/api/latest/users.md

---
title: Users
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Users
---

# Users

Create, edit, and disable users.

## Create a user{% #create-a-user %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/user |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/user |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/user      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/user      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/user     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/user |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/user |

### Overview



Create a user for your organization.

**Note**: Users can only be created with the admin access role if application keys belong to administrators.
This endpoint requires the `user_access_invite` permission.


### Request

#### Body Data (required)

User object that needs to be created.

{% tab title="Model" %}

| Field       | Type    | Description                                                                                                                                               |
| ----------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access_role | enum    | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR` |
| disabled    | boolean | The new disabled status of the user.                                                                                                                      |
| email       | string  | The new email of the user.                                                                                                                                |
| handle      | string  | The user handle, must be a valid email.                                                                                                                   |
| icon        | string  | Gravatar icon associated to the user.                                                                                                                     |
| name        | string  | The name of the user.                                                                                                                                     |
| verified    | boolean | Whether or not the user logged in Datadog at least once.                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "access_role": null,
  "disabled": false,
  "email": "test@datadoghq.com",
  "handle": "test@datadoghq.com",
  "name": "test user"
}
```

{% /tab %}

### Response

{% tab title="200" %}
User created
{% tab title="Model" %}
A Datadog User.

| Parent field | Field       | Type    | Description                                                                                                                                               |
| ------------ | ----------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | user        | object  | Create, edit, and disable users.                                                                                                                          |
| user         | access_role | enum    | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR` |
| user         | disabled    | boolean | The new disabled status of the user.                                                                                                                      |
| user         | email       | string  | The new email of the user.                                                                                                                                |
| user         | handle      | string  | The user handle, must be a valid email.                                                                                                                   |
| user         | icon        | string  | Gravatar icon associated to the user.                                                                                                                     |
| user         | name        | string  | The name of the user.                                                                                                                                     |
| user         | verified    | boolean | Whether or not the user logged in Datadog at least once.                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                    |
| ----------------- | ----------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/users |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/users |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/users      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/users      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/users     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/users |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/users |

### Overview

Create a user for your organization. This endpoint requires the `user_access_invite` permission.

OAuth apps require the `user_access_invite` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                        | Type     | Description                                                   |
| ------------- | ---------------------------- | -------- | ------------------------------------------------------------- |
|               | data [*required*]       | object   | Object to create a user.                                      |
| data          | attributes [*required*] | object   | Attributes of the created user.                               |
| attributes    | email [*required*]      | string   | The email of the user.                                        |
| attributes    | name                         | string   | The name of the user.                                         |
| attributes    | title                        | string   | The title of the user.                                        |
| data          | relationships                | object   | Relationships of the user object.                             |
| relationships | roles                        | object   | Relationship to roles.                                        |
| roles         | data                         | [object] | An array containing type and the unique identifier of a role. |
| data          | id                           | string   | The unique identifier of the role.                            |
| data          | type                         | enum     | Roles type. Allowed enum values: `roles`                      |
| data          | type [*required*]       | enum     | Users resource type. Allowed enum values: `users`             |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Response containing information about a single user.

| Parent field  | Field                     | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                  | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                     | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                    | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                      | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time           | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled               | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at               | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                      | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account           | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                    | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                     | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                  | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| data          | id                        | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| data          | relationships             | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                       | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]    | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]    | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users               | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]    | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]      | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                     | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                      | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| data          | type                      | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
|               | included                  | [ <oneOf>] | Array of objects related to the user.                                                                                                                                                                                                                                                         |
| included      | Option 1                  | object          | Organization object.                                                                                                                                                                                                                                                                          |
| Option 1      | attributes                | object          | Attributes of the organization.                                                                                                                                                                                                                                                               |
| attributes    | created_at                | date-time       | Creation time of the organization.                                                                                                                                                                                                                                                            |
| attributes    | description               | string          | Description of the organization.                                                                                                                                                                                                                                                              |
| attributes    | disabled                  | boolean         | Whether or not the organization is disabled.                                                                                                                                                                                                                                                  |
| attributes    | modified_at               | date-time       | Time of last organization modification.                                                                                                                                                                                                                                                       |
| attributes    | name                      | string          | Name of the organization.                                                                                                                                                                                                                                                                     |
| attributes    | public_id                 | string          | Public ID of the organization.                                                                                                                                                                                                                                                                |
| attributes    | sharing                   | string          | Sharing type of the organization.                                                                                                                                                                                                                                                             |
| attributes    | url                       | string          | URL of the site that this organization exists at.                                                                                                                                                                                                                                             |
| Option 1      | id                        | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| Option 1      | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| included      | Option 2                  | object          | Permission object.                                                                                                                                                                                                                                                                            |
| Option 2      | attributes                | object          | Attributes of a permission.                                                                                                                                                                                                                                                                   |
| attributes    | created                   | date-time       | Creation time of the permission.                                                                                                                                                                                                                                                              |
| attributes    | description               | string          | Description of the permission.                                                                                                                                                                                                                                                                |
| attributes    | display_name              | string          | Displayed name for the permission.                                                                                                                                                                                                                                                            |
| attributes    | display_type              | string          | Display type.                                                                                                                                                                                                                                                                                 |
| attributes    | group_name                | string          | Name of the permission group.                                                                                                                                                                                                                                                                 |
| attributes    | name                      | string          | Name of the permission.                                                                                                                                                                                                                                                                       |
| attributes    | restricted                | boolean         | Whether or not the permission is restricted.                                                                                                                                                                                                                                                  |
| Option 2      | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| Option 2      | type [*required*]    | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| included      | Option 3                  | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 3      | attributes                | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 3      | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 3      | relationships             | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 3      | type [*required*]    | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List all users{% #list-all-users %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                  |
| ----------------- | --------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/user |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/user |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/user      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/user      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/user     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/user |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/user |

### Overview

List all users for your organization. This endpoint requires the `user_access_read` permission.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Array of Datadog users for a given organization.

| Parent field | Field       | Type     | Description                                                                                                                                               |
| ------------ | ----------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | users       | [object] | Array of users.                                                                                                                                           |
| users        | access_role | enum     | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR` |
| users        | disabled    | boolean  | The new disabled status of the user.                                                                                                                      |
| users        | email       | string   | The new email of the user.                                                                                                                                |
| users        | handle      | string   | The user handle, must be a valid email.                                                                                                                   |
| users        | icon        | string   | Gravatar icon associated to the user.                                                                                                                     |
| users        | name        | string   | The name of the user.                                                                                                                                     |
| users        | verified    | boolean  | Whether or not the user logged in Datadog at least once.                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List all users returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new
p api_instance.list_users()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/users |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/users |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/users      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/users      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/users     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/users |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/users |

### Overview

Get the list of all users in the organization. This list includes all users even if they are deactivated or unverified. This endpoint requires the `user_access_read` permission.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Arguments

#### Query Strings

| Name           | Type    | Description                                                                                                                                                                                                           |
| -------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]     | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                              |
| page[number]   | integer | Specific page number to return.                                                                                                                                                                                       |
| sort           | string  | User attribute to order results by. Sort order is ascending by default. Sort order is descending if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `modified_at`, `user_count`. |
| sort_dir       | enum    | Direction of sort. Options: `asc`, `desc`.Allowed enum values: `asc, desc`                                                                                                                                            |
| filter         | string  | Filter all users by the given string. Defaults to no filtering.                                                                                                                                                       |
| filter[status] | string  | Filter on status attribute. Comma separated list, with possible values `Active`, `Pending`, and `Disabled`. Defaults to no filtering.                                                                                 |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about multiple users.

| Parent field  | Field                     | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | [object]        | Array of returned users.                                                                                                                                                                                                                                                                      |
| data          | attributes                | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                  | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                     | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                    | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                      | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time           | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled               | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at               | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                      | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account           | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                    | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                     | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                  | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| data          | id                        | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| data          | relationships             | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                       | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]    | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]    | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users               | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]    | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]      | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                     | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                      | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| data          | type                      | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
|               | included                  | [ <oneOf>] | Array of objects related to the users.                                                                                                                                                                                                                                                        |
| included      | Option 1                  | object          | Organization object.                                                                                                                                                                                                                                                                          |
| Option 1      | attributes                | object          | Attributes of the organization.                                                                                                                                                                                                                                                               |
| attributes    | created_at                | date-time       | Creation time of the organization.                                                                                                                                                                                                                                                            |
| attributes    | description               | string          | Description of the organization.                                                                                                                                                                                                                                                              |
| attributes    | disabled                  | boolean         | Whether or not the organization is disabled.                                                                                                                                                                                                                                                  |
| attributes    | modified_at               | date-time       | Time of last organization modification.                                                                                                                                                                                                                                                       |
| attributes    | name                      | string          | Name of the organization.                                                                                                                                                                                                                                                                     |
| attributes    | public_id                 | string          | Public ID of the organization.                                                                                                                                                                                                                                                                |
| attributes    | sharing                   | string          | Sharing type of the organization.                                                                                                                                                                                                                                                             |
| attributes    | url                       | string          | URL of the site that this organization exists at.                                                                                                                                                                                                                                             |
| Option 1      | id                        | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| Option 1      | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| included      | Option 2                  | object          | Permission object.                                                                                                                                                                                                                                                                            |
| Option 2      | attributes                | object          | Attributes of a permission.                                                                                                                                                                                                                                                                   |
| attributes    | created                   | date-time       | Creation time of the permission.                                                                                                                                                                                                                                                              |
| attributes    | description               | string          | Description of the permission.                                                                                                                                                                                                                                                                |
| attributes    | display_name              | string          | Displayed name for the permission.                                                                                                                                                                                                                                                            |
| attributes    | display_type              | string          | Display type.                                                                                                                                                                                                                                                                                 |
| attributes    | group_name                | string          | Name of the permission group.                                                                                                                                                                                                                                                                 |
| attributes    | name                      | string          | Name of the permission.                                                                                                                                                                                                                                                                       |
| attributes    | restricted                | boolean         | Whether or not the permission is restricted.                                                                                                                                                                                                                                                  |
| Option 2      | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| Option 2      | type [*required*]    | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| included      | Option 3                  | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 3      | attributes                | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 3      | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 3      | relationships             | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 3      | type [*required*]    | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
|               | meta                      | object          | Object describing meta attributes of response.                                                                                                                                                                                                                                                |
| meta          | page                      | object          | Pagination object.                                                                                                                                                                                                                                                                            |
| page          | total_count               | int64           | Total count.                                                                                                                                                                                                                                                                                  |
| page          | total_filtered_count      | int64           | Total count of elements matched by the filter.                                                                                                                                                                                                                                                |

{% /tab %}

{% tab title="Example" %}

```json
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
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get user details{% #get-user-details %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/user/{user_handle} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/user/{user_handle} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/user/{user_handle}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/user/{user_handle}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/user/{user_handle}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/user/{user_handle} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/user/{user_handle} |

### Overview

Get a user's details.

### Arguments

#### Path Parameters

| Name                          | Type   | Description         |
| ----------------------------- | ------ | ------------------- |
| user_handle [*required*] | string | The ID of the user. |

### Response

{% tab title="200" %}
OK for get user
{% tab title="Model" %}
A Datadog User.

| Parent field | Field       | Type    | Description                                                                                                                                               |
| ------------ | ----------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | user        | object  | Create, edit, and disable users.                                                                                                                          |
| user         | access_role | enum    | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR` |
| user         | disabled    | boolean | The new disabled status of the user.                                                                                                                      |
| user         | email       | string  | The new email of the user.                                                                                                                                |
| user         | handle      | string  | The user handle, must be a valid email.                                                                                                                   |
| user         | icon        | string  | Gravatar icon associated to the user.                                                                                                                     |
| user         | name        | string  | The name of the user.                                                                                                                                     |
| user         | verified    | boolean | Whether or not the user logged in Datadog at least once.                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_handle="test@datadoghq.com"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user/${user_handle}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get user details returns "OK for get user" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new
p api_instance.get_user("test@datadoghq.com")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/users/{user_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/users/{user_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/users/{user_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/users/{user_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/users/{user_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/users/{user_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/users/{user_id} |

### Overview

Get a user in the organization specified by the user's `user_id`. This endpoint requires the `user_access_read` permission.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| user_id [*required*] | string | The ID of the user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single user.

| Parent field  | Field                     | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                  | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                     | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                    | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                      | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time           | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled               | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at               | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                      | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account           | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                    | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                     | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                  | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| data          | id                        | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| data          | relationships             | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                       | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]    | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]    | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users               | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]    | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]      | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                     | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                      | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| data          | type                      | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
|               | included                  | [ <oneOf>] | Array of objects related to the user.                                                                                                                                                                                                                                                         |
| included      | Option 1                  | object          | Organization object.                                                                                                                                                                                                                                                                          |
| Option 1      | attributes                | object          | Attributes of the organization.                                                                                                                                                                                                                                                               |
| attributes    | created_at                | date-time       | Creation time of the organization.                                                                                                                                                                                                                                                            |
| attributes    | description               | string          | Description of the organization.                                                                                                                                                                                                                                                              |
| attributes    | disabled                  | boolean         | Whether or not the organization is disabled.                                                                                                                                                                                                                                                  |
| attributes    | modified_at               | date-time       | Time of last organization modification.                                                                                                                                                                                                                                                       |
| attributes    | name                      | string          | Name of the organization.                                                                                                                                                                                                                                                                     |
| attributes    | public_id                 | string          | Public ID of the organization.                                                                                                                                                                                                                                                                |
| attributes    | sharing                   | string          | Sharing type of the organization.                                                                                                                                                                                                                                                             |
| attributes    | url                       | string          | URL of the site that this organization exists at.                                                                                                                                                                                                                                             |
| Option 1      | id                        | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| Option 1      | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| included      | Option 2                  | object          | Permission object.                                                                                                                                                                                                                                                                            |
| Option 2      | attributes                | object          | Attributes of a permission.                                                                                                                                                                                                                                                                   |
| attributes    | created                   | date-time       | Creation time of the permission.                                                                                                                                                                                                                                                              |
| attributes    | description               | string          | Description of the permission.                                                                                                                                                                                                                                                                |
| attributes    | display_name              | string          | Displayed name for the permission.                                                                                                                                                                                                                                                            |
| attributes    | display_type              | string          | Display type.                                                                                                                                                                                                                                                                                 |
| attributes    | group_name                | string          | Name of the permission group.                                                                                                                                                                                                                                                                 |
| attributes    | name                      | string          | Name of the permission.                                                                                                                                                                                                                                                                       |
| attributes    | restricted                | boolean         | Whether or not the permission is restricted.                                                                                                                                                                                                                                                  |
| Option 2      | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| Option 2      | type [*required*]    | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| included      | Option 3                  | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 3      | attributes                | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 3      | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 3      | relationships             | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 3      | type [*required*]    | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
Not found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_id="00000000-0000-9999-0000-000000000000"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get user details returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.get_user(USER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update a user{% #update-a-user %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/user/{user_handle} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/user/{user_handle} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/user/{user_handle}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/user/{user_handle}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/user/{user_handle}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/user/{user_handle} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/user/{user_handle} |

### Overview



Update a user information.

**Note**: It can only be used with application keys belonging to administrators.



### Arguments

#### Path Parameters

| Name                          | Type   | Description         |
| ----------------------------- | ------ | ------------------- |
| user_handle [*required*] | string | The ID of the user. |

### Request

#### Body Data (required)

Description of the update.

{% tab title="Model" %}

| Field       | Type    | Description                                                                                                                                               |
| ----------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access_role | enum    | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR` |
| disabled    | boolean | The new disabled status of the user.                                                                                                                      |
| email       | string  | The new email of the user.                                                                                                                                |
| handle      | string  | The user handle, must be a valid email.                                                                                                                   |
| icon        | string  | Gravatar icon associated to the user.                                                                                                                     |
| name        | string  | The name of the user.                                                                                                                                     |
| verified    | boolean | Whether or not the user logged in Datadog at least once.                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "access_role": "ro",
  "disabled": false,
  "email": "test@datadoghq.com",
  "handle": "test@datadoghq.com",
  "name": "test user"
}
```

{% /tab %}

### Response

{% tab title="200" %}
User updated
{% tab title="Model" %}
A Datadog User.

| Parent field | Field       | Type    | Description                                                                                                                                               |
| ------------ | ----------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | user        | object  | Create, edit, and disable users.                                                                                                                          |
| user         | access_role | enum    | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR` |
| user         | disabled    | boolean | The new disabled status of the user.                                                                                                                      |
| user         | email       | string  | The new email of the user.                                                                                                                                |
| user         | handle      | string  | The user handle, must be a valid email.                                                                                                                   |
| user         | icon        | string  | Gravatar icon associated to the user.                                                                                                                     |
| user         | name        | string  | The name of the user.                                                                                                                                     |
| user         | verified    | boolean | Whether or not the user logged in Datadog at least once.                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_handle="test@datadoghq.com"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user/${user_handle}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/users/{user_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/users/{user_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/users/{user_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/users/{user_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/users/{user_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/users/{user_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/users/{user_id} |

### Overview

Edit a user. Can only be used with an application key belonging to an administrator user. This endpoint requires any of the following permissions:
`user_access_manage``service_account_write`


OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| user_id [*required*] | string | The ID of the user. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                       |
| ------------ | ---------------------------- | ------- | ------------------------------------------------- |
|              | data [*required*]       | object  | Object to update a user.                          |
| data         | attributes [*required*] | object  | Attributes of the edited user.                    |
| attributes   | disabled                     | boolean | If the user is enabled or disabled.               |
| attributes   | email                        | string  | The email of the user.                            |
| attributes   | name                         | string  | The name of the user.                             |
| data         | id [*required*]         | string  | ID of the user.                                   |
| data         | type [*required*]       | enum    | Users resource type. Allowed enum values: `users` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single user.

| Parent field  | Field                     | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                  | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                     | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                    | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                      | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time           | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled               | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at               | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                      | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account           | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                    | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                     | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                  | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| data          | id                        | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| data          | relationships             | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                       | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]    | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]    | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users               | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]    | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]      | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                     | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                      | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| data          | type                      | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
|               | included                  | [ <oneOf>] | Array of objects related to the user.                                                                                                                                                                                                                                                         |
| included      | Option 1                  | object          | Organization object.                                                                                                                                                                                                                                                                          |
| Option 1      | attributes                | object          | Attributes of the organization.                                                                                                                                                                                                                                                               |
| attributes    | created_at                | date-time       | Creation time of the organization.                                                                                                                                                                                                                                                            |
| attributes    | description               | string          | Description of the organization.                                                                                                                                                                                                                                                              |
| attributes    | disabled                  | boolean         | Whether or not the organization is disabled.                                                                                                                                                                                                                                                  |
| attributes    | modified_at               | date-time       | Time of last organization modification.                                                                                                                                                                                                                                                       |
| attributes    | name                      | string          | Name of the organization.                                                                                                                                                                                                                                                                     |
| attributes    | public_id                 | string          | Public ID of the organization.                                                                                                                                                                                                                                                                |
| attributes    | sharing                   | string          | Sharing type of the organization.                                                                                                                                                                                                                                                             |
| attributes    | url                       | string          | URL of the site that this organization exists at.                                                                                                                                                                                                                                             |
| Option 1      | id                        | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| Option 1      | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| included      | Option 2                  | object          | Permission object.                                                                                                                                                                                                                                                                            |
| Option 2      | attributes                | object          | Attributes of a permission.                                                                                                                                                                                                                                                                   |
| attributes    | created                   | date-time       | Creation time of the permission.                                                                                                                                                                                                                                                              |
| attributes    | description               | string          | Description of the permission.                                                                                                                                                                                                                                                                |
| attributes    | display_name              | string          | Displayed name for the permission.                                                                                                                                                                                                                                                            |
| attributes    | display_type              | string          | Display type.                                                                                                                                                                                                                                                                                 |
| attributes    | group_name                | string          | Name of the permission group.                                                                                                                                                                                                                                                                 |
| attributes    | name                      | string          | Name of the permission.                                                                                                                                                                                                                                                                       |
| attributes    | restricted                | boolean         | Whether or not the permission is restricted.                                                                                                                                                                                                                                                  |
| Option 2      | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| Option 2      | type [*required*]    | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| included      | Option 3                  | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 3      | attributes                | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 3      | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 3      | relationships             | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 3      | type [*required*]    | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
Not found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
Unprocessable Entity
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                          \# Path parametersexport user_id="00000000-0000-9999-0000-000000000000"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Disable a user{% #disable-a-user %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/user/{user_handle} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/user/{user_handle} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/user/{user_handle}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/user/{user_handle}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/user/{user_handle}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/user/{user_handle} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/user/{user_handle} |

### Overview



Delete a user from an organization.

**Note**: This endpoint can only be used with application keys belonging to administrators.



### Arguments

#### Path Parameters

| Name                          | Type   | Description             |
| ----------------------------- | ------ | ----------------------- |
| user_handle [*required*] | string | The handle of the user. |

### Response

{% tab title="200" %}
User disabled
{% tab title="Model" %}
Array of user disabled for a given organization.

| Field   | Type   | Description                                                         |
| ------- | ------ | ------------------------------------------------------------------- |
| message | string | Information pertaining to a user disabled for a given organization. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "message": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_handle="test@datadoghq.com"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/user/${user_handle}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Disable a user returns "User disabled" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsersAPI.new
p api_instance.disable_user("test@datadoghq.com")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/users/{user_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/users/{user_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/users/{user_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/users/{user_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/users/{user_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/users/{user_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/users/{user_id} |

### Overview

Disable a user. Can only be used with an application key belonging to an administrator user. This endpoint requires any of the following permissions:
`user_access_manage``service_account_write`


OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| user_id [*required*] | string | The ID of the user. |

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
Not found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_id="00000000-0000-9999-0000-000000000000"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Disable a user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
api_instance.disable_user(USER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a user organization{% #get-a-user-organization %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/users/{user_id}/orgs |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/users/{user_id}/orgs |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/users/{user_id}/orgs      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/users/{user_id}/orgs      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/users/{user_id}/orgs     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/users/{user_id}/orgs |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/users/{user_id}/orgs |

### Overview

Get a user organization. Returns the user information and all organizations joined by this user.

### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| user_id [*required*] | string | The ID of the user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single user.

| Parent field  | Field                     | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                  | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                     | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                    | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                      | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time           | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled               | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at               | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                      | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account           | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                    | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                     | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                  | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| data          | id                        | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| data          | relationships             | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                       | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]    | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]    | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]      | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users               | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]    | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]      | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                     | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                      | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                      | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| data          | type                      | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
|               | included                  | [ <oneOf>] | Array of objects related to the user.                                                                                                                                                                                                                                                         |
| included      | Option 1                  | object          | Organization object.                                                                                                                                                                                                                                                                          |
| Option 1      | attributes                | object          | Attributes of the organization.                                                                                                                                                                                                                                                               |
| attributes    | created_at                | date-time       | Creation time of the organization.                                                                                                                                                                                                                                                            |
| attributes    | description               | string          | Description of the organization.                                                                                                                                                                                                                                                              |
| attributes    | disabled                  | boolean         | Whether or not the organization is disabled.                                                                                                                                                                                                                                                  |
| attributes    | modified_at               | date-time       | Time of last organization modification.                                                                                                                                                                                                                                                       |
| attributes    | name                      | string          | Name of the organization.                                                                                                                                                                                                                                                                     |
| attributes    | public_id                 | string          | Public ID of the organization.                                                                                                                                                                                                                                                                |
| attributes    | sharing                   | string          | Sharing type of the organization.                                                                                                                                                                                                                                                             |
| attributes    | url                       | string          | URL of the site that this organization exists at.                                                                                                                                                                                                                                             |
| Option 1      | id                        | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| Option 1      | type [*required*]    | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| included      | Option 2                  | object          | Permission object.                                                                                                                                                                                                                                                                            |
| Option 2      | attributes                | object          | Attributes of a permission.                                                                                                                                                                                                                                                                   |
| attributes    | created                   | date-time       | Creation time of the permission.                                                                                                                                                                                                                                                              |
| attributes    | description               | string          | Description of the permission.                                                                                                                                                                                                                                                                |
| attributes    | display_name              | string          | Displayed name for the permission.                                                                                                                                                                                                                                                            |
| attributes    | display_type              | string          | Display type.                                                                                                                                                                                                                                                                                 |
| attributes    | group_name                | string          | Name of the permission group.                                                                                                                                                                                                                                                                 |
| attributes    | name                      | string          | Name of the permission.                                                                                                                                                                                                                                                                       |
| attributes    | restricted                | boolean         | Whether or not the permission is restricted.                                                                                                                                                                                                                                                  |
| Option 2      | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| Option 2      | type [*required*]    | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| included      | Option 3                  | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 3      | attributes                | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 3      | id                        | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 3      | relationships             | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 3      | type [*required*]    | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
Not found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_id="00000000-0000-9999-0000-000000000000"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}/orgs" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a user organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new
p api_instance.list_user_organizations("00000000-0000-9999-0000-000000000000")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a user permissions{% #get-a-user-permissions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/users/{user_id}/permissions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/users/{user_id}/permissions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/users/{user_id}/permissions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/users/{user_id}/permissions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/users/{user_id}/permissions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/users/{user_id}/permissions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/users/{user_id}/permissions |

### Overview

Get a user permission set. Returns a list of the user's permissions granted by the associated user's roles. This endpoint requires the `user_access_read` permission.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| user_id [*required*] | string | The ID of the user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Payload with API-returned permissions.

| Parent field | Field                  | Type      | Description                                                   |
| ------------ | ---------------------- | --------- | ------------------------------------------------------------- |
|              | data                   | [object]  | Array of permissions.                                         |
| data         | attributes             | object    | Attributes of a permission.                                   |
| attributes   | created                | date-time | Creation time of the permission.                              |
| attributes   | description            | string    | Description of the permission.                                |
| attributes   | display_name           | string    | Displayed name for the permission.                            |
| attributes   | display_type           | string    | Display type.                                                 |
| attributes   | group_name             | string    | Name of the permission group.                                 |
| attributes   | name                   | string    | Name of the permission.                                       |
| attributes   | restricted             | boolean   | Whether or not the permission is restricted.                  |
| data         | id                     | string    | ID of the permission.                                         |
| data         | type [*required*] | enum      | Permissions resource type. Allowed enum values: `permissions` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
Not found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_id="00000000-0000-9999-0000-000000000000"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/users/${user_id}/permissions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a user permissions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.list_user_permissions(USER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Send invitation emails{% #send-invitation-emails %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/user_invitations |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/user_invitations |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/user_invitations      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/user_invitations      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/user_invitations     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/user_invitations |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/user_invitations |

### Overview

Sends emails to one or more users inviting them to join the organization. This endpoint requires the `user_access_invite` permission.

OAuth apps require the `user_access_invite` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                           | Type     | Description                                                    |
| ------------- | ------------------------------- | -------- | -------------------------------------------------------------- |
|               | data [*required*]          | [object] | List of user invitations.                                      |
| data          | relationships [*required*] | object   | Relationships data for user invitation.                        |
| relationships | user [*required*]          | object   | Relationship to user.                                          |
| user          | data [*required*]          | object   | Relationship to user object.                                   |
| data          | id [*required*]            | string   | A unique identifier that represents the user.                  |
| data          | type [*required*]          | enum     | Users resource type. Allowed enum values: `users`              |
| data          | type [*required*]          | enum     | User invitations type. Allowed enum values: `user_invitations` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
User invitations as returned by the API.

| Parent field  | Field                  | Type      | Description                                                    |
| ------------- | ---------------------- | --------- | -------------------------------------------------------------- |
|               | data                   | [object]  | Array of user invitations.                                     |
| data          | attributes             | object    | Attributes of a user invitation.                               |
| attributes    | created_at             | date-time | Creation time of the user invitation.                          |
| attributes    | expires_at             | date-time | Time of invitation expiration.                                 |
| attributes    | invite_type            | string    | Type of invitation.                                            |
| attributes    | uuid                   | string    | UUID of the user invitation.                                   |
| data          | id                     | string    | ID of the user invitation.                                     |
| data          | relationships          | object    | Relationships data for user invitation.                        |
| relationships | user [*required*] | object    | Relationship to user.                                          |
| user          | data [*required*] | object    | Relationship to user object.                                   |
| data          | id [*required*]   | string    | A unique identifier that represents the user.                  |
| data          | type [*required*] | enum      | Users resource type. Allowed enum values: `users`              |
| data          | type                   | enum      | User invitations type. Allowed enum values: `user_invitations` |

{% /tab %}

{% tab title="Example" %}

```json
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
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/user_invitations" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a user invitation{% #get-a-user-invitation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/user_invitations/{user_invitation_uuid}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/user_invitations/{user_invitation_uuid}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/user_invitations/{user_invitation_uuid} |

### Overview

Returns a single user invitation by its UUID. This endpoint requires the `user_access_invite` permission.

OAuth apps require the `user_access_invite` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#users) to access this endpoint.



### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| user_invitation_uuid [*required*] | string | The UUID of the user invitation. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
User invitation as returned by the API.

| Parent field  | Field                  | Type      | Description                                                    |
| ------------- | ---------------------- | --------- | -------------------------------------------------------------- |
|               | data                   | object    | Object of a user invitation returned by the API.               |
| data          | attributes             | object    | Attributes of a user invitation.                               |
| attributes    | created_at             | date-time | Creation time of the user invitation.                          |
| attributes    | expires_at             | date-time | Time of invitation expiration.                                 |
| attributes    | invite_type            | string    | Type of invitation.                                            |
| attributes    | uuid                   | string    | UUID of the user invitation.                                   |
| data          | id                     | string    | ID of the user invitation.                                     |
| data          | relationships          | object    | Relationships data for user invitation.                        |
| relationships | user [*required*] | object    | Relationship to user.                                          |
| user          | data [*required*] | object    | Relationship to user object.                                   |
| data          | id [*required*]   | string    | A unique identifier that represents the user.                  |
| data          | type [*required*] | enum      | Users resource type. Allowed enum values: `users`              |
| data          | type                   | enum      | User invitations type. Allowed enum values: `user_invitations` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
Not found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

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
                  \# Path parametersexport user_invitation_uuid="00000000-0000-0000-3456-000000000000"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/user_invitations/${user_invitation_uuid}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a user invitation returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsersAPI.new

# the "user" has a "user_invitation"
USER_INVITATION_ID = ENV["USER_INVITATION_ID"]
p api_instance.get_invitation(USER_INVITATION_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
