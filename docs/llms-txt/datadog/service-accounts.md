# Source: https://docs.datadoghq.com/api/latest/service-accounts.md

---
title: Service Accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Service Accounts
---

Create, edit, and disable service accounts. See the [Service Accounts page](https://docs.datadoghq.com/account_management/org_settings/service_accounts/) for more information.

## Create a service account{% #create-a-service-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/service_accounts |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/service_accounts |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/service_accounts      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/service_accounts      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/service_accounts     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/service_accounts |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/service_accounts |

### Overview

Create a service account for your organization. This endpoint requires the `service_account_write` permission.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field  | Field                             | Type     | Description                                                   |
| ------------- | --------------------------------- | -------- | ------------------------------------------------------------- |
|               | data [*required*]            | object   | Object to create a service account User.                      |
| data          | attributes [*required*]      | object   | Attributes of the created user.                               |
| attributes    | email [*required*]           | string   | The email of the user.                                        |
| attributes    | name                              | string   | The name of the user.                                         |
| attributes    | service_account [*required*] | boolean  | Whether the user is a service account. Must be true.          |
| attributes    | title                             | string   | The title of the user.                                        |
| data          | relationships                     | object   | Relationships of the user object.                             |
| relationships | roles                             | object   | Relationship to roles.                                        |
| roles         | data                              | [object] | An array containing type and the unique identifier of a role. |
| data          | id                                | string   | The unique identifier of the role.                            |
| data          | type                              | enum     | Roles type. Allowed enum values: `roles`                      |
| data          | type [*required*]            | enum     | Users resource type. Allowed enum values: `users`             |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get one application key for this service account{% #get-one-application-key-for-this-service-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |

### Overview

Get an application key owned by this service account. This endpoint requires the `service_account_write` permission.

### Arguments

#### Path Parameters

| Name                                 | Type   | Description                    |
| ------------------------------------ | ------ | ------------------------------ |
| service_account_id [*required*] | string | The ID of the service account. |
| app_key_id [*required*]         | string | The ID of the application key. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for retrieving a partial application key.

| Parent field  | Field                        | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ---------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                         | object          | Partial Datadog application key.                                                                                                                                                                                                                                                              |
| data          | attributes                   | object          | Attributes of a partial application key.                                                                                                                                                                                                                                                      |
| attributes    | created_at                   | string          | Creation date of the application key.                                                                                                                                                                                                                                                         |
| attributes    | last4                        | string          | The last four characters of the application key.                                                                                                                                                                                                                                              |
| attributes    | last_used_at                 | string          | Last usage timestamp of the application key.                                                                                                                                                                                                                                                  |
| attributes    | name                         | string          | Name of the application key.                                                                                                                                                                                                                                                                  |
| attributes    | scopes                       | [string]        | Array of scopes to grant the application key.                                                                                                                                                                                                                                                 |
| data          | id                           | string          | ID of the application key.                                                                                                                                                                                                                                                                    |
| data          | relationships                | object          | Resources related to the application key.                                                                                                                                                                                                                                                     |
| relationships | owned_by                     | object          | Relationship to user.                                                                                                                                                                                                                                                                         |
| owned_by      | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                                                                                                                  |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| data          | type                         | enum            | Application Keys resource type. Allowed enum values: `application_keys`                                                                                                                                                                                                                       |
|               | included                     | [ <oneOf>] | Array of objects related to the application key.                                                                                                                                                                                                                                              |
| included      | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                        | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                       | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                         | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                         | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                       | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                        | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| Option 1      | id                           | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                          | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users                  | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                        | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| included      | Option 2                     | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2      | attributes                   | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                   | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at                  | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                         | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from    | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                   | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2      | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2      | relationships                | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions                  | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                         | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                           | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                         | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2      | type [*required*]       | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included      | Option 3                     | object          | The definition of LeakedKey object.                                                                                                                                                                                                                                                           |
| Option 3      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                                                                                                                                                                                                                                                 |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                                                                                                                                                                                                                                                 |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                                                                                                                                                                                                                                          |
| Option 3      | id [*required*]         | string          | The LeakedKey id.                                                                                                                                                                                                                                                                             |
| Option 3      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport service_account_id="00000000-0000-1234-0000-000000000000"export app_key_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get one application key for this service account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = ENV["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]
p api_instance.get_service_account_application_key(SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Edit an application key for this service account{% #edit-an-application-key-for-this-service-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                   |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |

### Overview

Edit an application key owned by this service account. This endpoint requires the `service_account_write` permission.

### Arguments

#### Path Parameters

| Name                                 | Type   | Description                    |
| ------------------------------------ | ------ | ------------------------------ |
| service_account_id [*required*] | string | The ID of the service account. |
| app_key_id [*required*]         | string | The ID of the application key. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                             |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------- |
|              | data [*required*]       | object   | Object used to update an application key.                               |
| data         | attributes [*required*] | object   | Attributes used to update an application Key.                           |
| attributes   | name                         | string   | Name of the application key.                                            |
| attributes   | scopes                       | [string] | Array of scopes to grant the application key.                           |
| data         | id [*required*]         | string   | ID of the application key.                                              |
| data         | type [*required*]       | enum     | Application Keys resource type. Allowed enum values: `application_keys` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for retrieving a partial application key.

| Parent field  | Field                        | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ---------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                         | object          | Partial Datadog application key.                                                                                                                                                                                                                                                              |
| data          | attributes                   | object          | Attributes of a partial application key.                                                                                                                                                                                                                                                      |
| attributes    | created_at                   | string          | Creation date of the application key.                                                                                                                                                                                                                                                         |
| attributes    | last4                        | string          | The last four characters of the application key.                                                                                                                                                                                                                                              |
| attributes    | last_used_at                 | string          | Last usage timestamp of the application key.                                                                                                                                                                                                                                                  |
| attributes    | name                         | string          | Name of the application key.                                                                                                                                                                                                                                                                  |
| attributes    | scopes                       | [string]        | Array of scopes to grant the application key.                                                                                                                                                                                                                                                 |
| data          | id                           | string          | ID of the application key.                                                                                                                                                                                                                                                                    |
| data          | relationships                | object          | Resources related to the application key.                                                                                                                                                                                                                                                     |
| relationships | owned_by                     | object          | Relationship to user.                                                                                                                                                                                                                                                                         |
| owned_by      | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                                                                                                                  |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| data          | type                         | enum            | Application Keys resource type. Allowed enum values: `application_keys`                                                                                                                                                                                                                       |
|               | included                     | [ <oneOf>] | Array of objects related to the application key.                                                                                                                                                                                                                                              |
| included      | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                        | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                       | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                         | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                         | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                       | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                        | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| Option 1      | id                           | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                          | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users                  | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                        | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| included      | Option 2                     | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2      | attributes                   | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                   | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at                  | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                         | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from    | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                   | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2      | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2      | relationships                | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions                  | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                         | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                           | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                         | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2      | type [*required*]       | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included      | Option 3                     | object          | The definition of LeakedKey object.                                                                                                                                                                                                                                                           |
| Option 3      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                                                                                                                                                                                                                                                 |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                                                                                                                                                                                                                                                 |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                                                                                                                                                                                                                                          |
| Option 3      | id [*required*]         | string          | The LeakedKey id.                                                                                                                                                                                                                                                                             |
| Option 3      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport service_account_id="00000000-0000-1234-0000-000000000000"export app_key_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys/${app_key_id}" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete an application key for this service account{% #delete-an-application-key-for-this-service-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} |

### Overview

Delete an application key owned by this service account. This endpoint requires the `service_account_write` permission.

### Arguments

#### Path Parameters

| Name                                 | Type   | Description                    |
| ------------------------------------ | ------ | ------------------------------ |
| service_account_id [*required*] | string | The ID of the service account. |
| app_key_id [*required*]         | string | The ID of the application key. |

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
                  \# Path parametersexport service_account_id="00000000-0000-1234-0000-000000000000"export app_key_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete an application key for this service account returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = ENV["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]
api_instance.delete_service_account_application_key(SERVICE_ACCOUNT_USER_DATA_ID, SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create an application key for this service account{% #create-an-application-key-for-this-service-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |

### Overview

Create an application key for this service account. This endpoint requires the `service_account_write` permission.

### Arguments

#### Path Parameters

| Name                                 | Type   | Description                    |
| ------------------------------------ | ------ | ------------------------------ |
| service_account_id [*required*] | string | The ID of the service account. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                             |
| ------------ | ---------------------------- | -------- | ----------------------------------------------------------------------- |
|              | data [*required*]       | object   | Object used to create an application key.                               |
| data         | attributes [*required*] | object   | Attributes used to create an application Key.                           |
| attributes   | name [*required*]       | string   | Name of the application key.                                            |
| attributes   | scopes                       | [string] | Array of scopes to grant the application key.                           |
| data         | type [*required*]       | enum     | Application Keys resource type. Allowed enum values: `application_keys` |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "name": "Example-Service-Account"
    },
    "type": "application_keys"
  }
}
```

#####

```json
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

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response for retrieving an application key.

| Parent field  | Field                        | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ---------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                         | object          | Datadog application key.                                                                                                                                                                                                                                                                      |
| data          | attributes                   | object          | Attributes of a full application key.                                                                                                                                                                                                                                                         |
| attributes    | created_at                   | date-time       | Creation date of the application key.                                                                                                                                                                                                                                                         |
| attributes    | key                          | string          | The application key.                                                                                                                                                                                                                                                                          |
| attributes    | last4                        | string          | The last four characters of the application key.                                                                                                                                                                                                                                              |
| attributes    | last_used_at                 | date-time       | Last usage timestamp of the application key.                                                                                                                                                                                                                                                  |
| attributes    | name                         | string          | Name of the application key.                                                                                                                                                                                                                                                                  |
| attributes    | scopes                       | [string]        | Array of scopes to grant the application key.                                                                                                                                                                                                                                                 |
| data          | id                           | string          | ID of the application key.                                                                                                                                                                                                                                                                    |
| data          | relationships                | object          | Resources related to the application key.                                                                                                                                                                                                                                                     |
| relationships | owned_by                     | object          | Relationship to user.                                                                                                                                                                                                                                                                         |
| owned_by      | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                                                                                                                  |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| data          | type                         | enum            | Application Keys resource type. Allowed enum values: `application_keys`                                                                                                                                                                                                                       |
|               | included                     | [ <oneOf>] | Array of objects related to the application key.                                                                                                                                                                                                                                              |
| included      | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                        | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                       | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                         | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                         | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                       | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                        | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| Option 1      | id                           | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                          | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users                  | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                        | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| included      | Option 2                     | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2      | attributes                   | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                   | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at                  | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                         | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from    | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                   | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2      | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2      | relationships                | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions                  | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                         | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                           | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                         | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2      | type [*required*]       | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included      | Option 3                     | object          | The definition of LeakedKey object.                                                                                                                                                                                                                                                           |
| Option 3      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                                                                                                                                                                                                                                                 |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                                                                                                                                                                                                                                                 |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                                                                                                                                                                                                                                          |
| Option 3      | id [*required*]         | string          | The LeakedKey id.                                                                                                                                                                                                                                                                             |
| Option 3      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport service_account_id="00000000-0000-1234-0000-000000000000"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys" \
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

#####
                          \# Path parametersexport service_account_id="00000000-0000-1234-0000-000000000000"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys" \
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

#####

```go
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
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

#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
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

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
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

#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
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

#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
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

#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## List application keys for this service account{% #list-application-keys-for-this-service-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/service_accounts/{service_account_id}/application_keys      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/service_accounts/{service_account_id}/application_keys      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/service_accounts/{service_account_id}/application_keys |

### Overview

List all application keys available for this service account. This endpoint requires the `service_account_write` permission.

### Arguments

#### Path Parameters

| Name                                 | Type   | Description                    |
| ------------------------------------ | ------ | ------------------------------ |
| service_account_id [*required*] | string | The ID of the service account. |

#### Query Strings

| Name                      | Type    | Description                                                                                                                                                                                                                                  |
| ------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]                | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                                                     |
| page[number]              | integer | Specific page number to return.                                                                                                                                                                                                              |
| sort                      | enum    | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign.Allowed enum values: `created_at, -created_at, last4, -last4, name, -name` |
| filter                    | string  | Filter application keys by the specified string.                                                                                                                                                                                             |
| filter[created_at][start] | string  | Only include application keys created on or after the specified date.                                                                                                                                                                        |
| filter[created_at][end]   | string  | Only include application keys created on or before the specified date.                                                                                                                                                                       |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a list of application keys.

| Parent field  | Field                        | Type            | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ---------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                         | [object]        | Array of application keys.                                                                                                                                                                                                                                                                    |
| data          | attributes                   | object          | Attributes of a partial application key.                                                                                                                                                                                                                                                      |
| attributes    | created_at                   | string          | Creation date of the application key.                                                                                                                                                                                                                                                         |
| attributes    | last4                        | string          | The last four characters of the application key.                                                                                                                                                                                                                                              |
| attributes    | last_used_at                 | string          | Last usage timestamp of the application key.                                                                                                                                                                                                                                                  |
| attributes    | name                         | string          | Name of the application key.                                                                                                                                                                                                                                                                  |
| attributes    | scopes                       | [string]        | Array of scopes to grant the application key.                                                                                                                                                                                                                                                 |
| data          | id                           | string          | ID of the application key.                                                                                                                                                                                                                                                                    |
| data          | relationships                | object          | Resources related to the application key.                                                                                                                                                                                                                                                     |
| relationships | owned_by                     | object          | Relationship to user.                                                                                                                                                                                                                                                                         |
| owned_by      | data [*required*]       | object          | Relationship to user object.                                                                                                                                                                                                                                                                  |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| data          | type                         | enum            | Application Keys resource type. Allowed enum values: `application_keys`                                                                                                                                                                                                                       |
|               | included                     | [ <oneOf>] | Array of objects related to the application key.                                                                                                                                                                                                                                              |
| included      | Option 1                     | object          | User object returned by the API.                                                                                                                                                                                                                                                              |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                    |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                 |
| attributes    | email                        | string          | Email of the user.                                                                                                                                                                                                                                                                            |
| attributes    | handle                       | string          | Handle of the user.                                                                                                                                                                                                                                                                           |
| attributes    | icon                         | string          | URL of the user's icon.                                                                                                                                                                                                                                                                       |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                             |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                      |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                         |
| attributes    | name                         | string          | Name of the user.                                                                                                                                                                                                                                                                             |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                        |
| attributes    | status                       | string          | Status of the user.                                                                                                                                                                                                                                                                           |
| attributes    | title                        | string          | Title of the user.                                                                                                                                                                                                                                                                            |
| attributes    | verified                     | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                 |
| Option 1      | id                           | string          | ID of the user.                                                                                                                                                                                                                                                                               |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                         |
| relationships | org                          | object          | Relationship to an organization.                                                                                                                                                                                                                                                              |
| org           | data [*required*]       | object          | Relationship to organization object.                                                                                                                                                                                                                                                          |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_orgs                   | object          | Relationship to organizations.                                                                                                                                                                                                                                                                |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                        |
| data          | id [*required*]         | string          | ID of the organization.                                                                                                                                                                                                                                                                       |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                      |
| relationships | other_users                  | object          | Relationship to users.                                                                                                                                                                                                                                                                        |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| relationships | roles                        | object          | Relationship to roles.                                                                                                                                                                                                                                                                        |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                 |
| data          | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                             |
| included      | Option 2                     | object          | Role object returned by the API.                                                                                                                                                                                                                                                              |
| Option 2      | attributes                   | object          | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                   | date-time       | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at                  | date-time       | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                         | string          | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from    | [string]        | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                   | int64           | Number of users with that role.                                                                                                                                                                                                                                                               |
| Option 2      | id                           | string          | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| Option 2      | relationships                | object          | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions                  | object          | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                         | [object]        | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                           | string          | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                         | enum            | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| Option 2      | type [*required*]       | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
| included      | Option 3                     | object          | The definition of LeakedKey object.                                                                                                                                                                                                                                                           |
| Option 3      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                                                                                                                                                                                                                                                 |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                                                                                                                                                                                                                                                 |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                                                                                                                                                                                                                                          |
| Option 3      | id [*required*]         | string          | The LeakedKey id.                                                                                                                                                                                                                                                                             |
| Option 3      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys`                                                                                                                                                                                                                    |
|               | meta                         | object          | Additional information related to the application key response.                                                                                                                                                                                                                               |
| meta          | max_allowed_per_user         | int64           | Max allowed number of application keys per user.                                                                                                                                                                                                                                              |
| meta          | page                         | object          | Additional information related to the application key response.                                                                                                                                                                                                                               |
| page          | total_filtered_count         | int64           | Total filtered application key count.                                                                                                                                                                                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport service_account_id="00000000-0000-1234-0000-000000000000"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/service_accounts/${service_account_id}/application_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List application keys for this service account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceAccountsAPI.new

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = ENV["SERVICE_ACCOUNT_USER_DATA_ID"]
p api_instance.list_service_account_application_keys(SERVICE_ACCOUNT_USER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
