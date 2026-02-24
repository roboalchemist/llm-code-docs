# Source: https://docs.datadoghq.com/api/latest/roles.md

---
title: Roles
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Roles
---

# Roles

The Roles API is used to create and manage Datadog roles, what [global permissions](https://docs.datadoghq.com/account_management/rbac/) they grant, and which users belong to them.

Permissions related to specific account assets can be granted to roles in the Datadog application without using this API. For example, granting read access on a specific log index to a role can be done in Datadog from the [Pipelines page](https://app.datadoghq.com/logs/pipelines).

Roles can also be managed in bulk through the Datadog UI, which provides the capability to assign a single permission to multiple roles simultaneously.

## List permissions{% #list-permissions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/permissions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/permissions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/permissions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/permissions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/permissions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/permissions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/permissions |

### Overview

Returns a list of all permissions, including name, description, and ID. This endpoint requires the `user_access_read` permission.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/permissions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List permissions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.list_permissions()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List permissions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new
p api_instance.list_permissions()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List permissions returns "OK" response

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
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.ListPermissions(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.ListPermissions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.ListPermissions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List permissions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.PermissionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    try {
      PermissionsResponse result = apiInstance.listPermissions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#listPermissions");
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
// List permissions returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.list_permissions().await;
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
 * List permissions returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

apiInstance
  .listPermissions()
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

## List roles{% #list-roles %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/roles |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/roles |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/roles      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/roles      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/roles     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/roles |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/roles |

### Overview

Returns all roles, including their names and their unique identifiers. This endpoint requires the `user_access_read` permission.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                                                                                                                                                                                                 |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                                                                                    |
| page[number] | integer | Specific page number to return.                                                                                                                                                                                                                                             |
| sort         | enum    | Sort roles depending on the given field. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example: `sort=-name`.Allowed enum values: `name, -name, modified_at, -modified_at, user_count, -user_count` |
| filter       | string  | Filter all roles by the given string.                                                                                                                                                                                                                                       |
| filter[id]   | string  | Filter all roles by the given list of role IDs.                                                                                                                                                                                                                             |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about multiple roles.

| Parent field  | Field                     | Type      | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | [object]  | Array of returned roles.                                                                                                                                                                                                                                                                      |
| data          | attributes                | object    | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string    | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]  | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64     | Number of users with that role.                                                                                                                                                                                                                                                               |
| data          | id                        | string    | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | relationships             | object    | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object    | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]  | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string    | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum      | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum      | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |
|               | meta                      | object    | Object describing meta attributes of response.                                                                                                                                                                                                                                                |
| meta          | page                      | object    | Pagination object.                                                                                                                                                                                                                                                                            |
| page          | total_count               | int64     | Total count.                                                                                                                                                                                                                                                                                  |
| page          | total_filtered_count      | int64     | Total count of elements matched by the filter.                                                                                                                                                                                                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "receives_permissions_from": [],
        "user_count": "integer"
      },
      "id": "string",
      "relationships": {
        "permissions": {
          "data": [
            {
              "id": "string",
              "type": "permissions"
            }
          ]
        }
      },
      "type": "roles"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List roles returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = environ["ROLE_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.list_roles(
        filter=ROLE_DATA_ATTRIBUTES_NAME,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List roles returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = ENV["ROLE_DATA_ATTRIBUTES_NAME"]
opts = {
  filter: ROLE_DATA_ATTRIBUTES_NAME,
}
p api_instance.list_roles(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List roles returns "OK" response

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
	RoleDataAttributesName := os.Getenv("ROLE_DATA_ATTRIBUTES_NAME")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.ListRoles(ctx, *datadogV2.NewListRolesOptionalParameters().WithFilter(RoleDataAttributesName))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.ListRoles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.ListRoles`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List roles returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.api.RolesApi.ListRolesOptionalParameters;
import com.datadog.api.client.v2.model.RolesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ATTRIBUTES_NAME = System.getenv("ROLE_DATA_ATTRIBUTES_NAME");

    try {
      RolesResponse result =
          apiInstance.listRoles(
              new ListRolesOptionalParameters().filter(ROLE_DATA_ATTRIBUTES_NAME));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#listRoles");
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
// List roles returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::ListRolesOptionalParams;
use datadog_api_client::datadogV2::api_roles::RolesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_attributes_name = std::env::var("ROLE_DATA_ATTRIBUTES_NAME").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api
        .list_roles(ListRolesOptionalParams::default().filter(role_data_attributes_name.clone()))
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
 * List roles returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ATTRIBUTES_NAME = process.env
  .ROLE_DATA_ATTRIBUTES_NAME as string;

const params: v2.RolesApiListRolesRequest = {
  filter: ROLE_DATA_ATTRIBUTES_NAME,
};

apiInstance
  .listRoles(params)
  .then((data: v2.RolesResponse) => {
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

## Create role{% #create-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                    |
| ----------------- | ----------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/roles |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/roles |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/roles      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/roles      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/roles     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/roles |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/roles |

### Overview

Create a new role for your organization. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                        | Type      | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ---------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data [*required*]       | object    | Data related to the creation of a role.                                                                                                                                                                                                                                                       |
| data          | attributes [*required*] | object    | Attributes of the created role.                                                                                                                                                                                                                                                               |
| attributes    | created_at                   | date-time | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at                  | date-time | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name [*required*]       | string    | Name of the role.                                                                                                                                                                                                                                                                             |
| attributes    | receives_permissions_from    | [string]  | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| data          | relationships                | object    | Relationships of the role object.                                                                                                                                                                                                                                                             |
| relationships | permissions                  | object    | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                         | [object]  | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                           | string    | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                         | enum      | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| data          | type                         | enum      | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "roles",
    "attributes": {
      "name": "Example-Role"
    },
    "relationships": {
      "permissions": {
        "data": [
          {
            "id": "string",
            "type": "permissions"
          }
        ]
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a created role.

| Parent field  | Field                     | Type      | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object    | Role object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object    | Attributes of the created role.                                                                                                                                                                                                                                                               |
| attributes    | created_at                | date-time | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name [*required*]    | string    | Name of the role.                                                                                                                                                                                                                                                                             |
| attributes    | receives_permissions_from | [string]  | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| data          | id                        | string    | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | relationships             | object    | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object    | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]  | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string    | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum      | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum      | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "developers",
      "receives_permissions_from": []
    },
    "id": "string",
    "relationships": {
      "permissions": {
        "data": [
          {
            "id": "string",
            "type": "permissions"
          }
        ]
      }
    },
    "type": "roles"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "roles",
    "attributes": {
      "name": "Example-Role"
    },
    "relationships": {
      "permissions": {
        "data": [
          {
            "id": "string",
            "type": "permissions"
          }
        ]
      }
    }
  }
}
EOF
                        
##### 

```go
// Create role with a permission returns "OK" response

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
	// there is a valid "permission" in the system
	PermissionID := os.Getenv("PERMISSION_ID")

	body := datadogV2.RoleCreateRequest{
		Data: datadogV2.RoleCreateData{
			Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
			Attributes: datadogV2.RoleCreateAttributes{
				Name: "Example-Role",
			},
			Relationships: &datadogV2.RoleRelationships{
				Permissions: &datadogV2.RelationshipToPermissions{
					Data: []datadogV2.RelationshipToPermissionData{
						{
							Id:   datadog.PtrString(PermissionID),
							Type: datadogV2.PERMISSIONSTYPE_PERMISSIONS.Ptr(),
						},
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.CreateRole(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.CreateRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.CreateRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create role with a permission returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.PermissionsType;
import com.datadog.api.client.v2.model.RelationshipToPermissionData;
import com.datadog.api.client.v2.model.RelationshipToPermissions;
import com.datadog.api.client.v2.model.RoleCreateAttributes;
import com.datadog.api.client.v2.model.RoleCreateData;
import com.datadog.api.client.v2.model.RoleCreateRequest;
import com.datadog.api.client.v2.model.RoleCreateResponse;
import com.datadog.api.client.v2.model.RoleRelationships;
import com.datadog.api.client.v2.model.RolesType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "permission" in the system
    String PERMISSION_ID = System.getenv("PERMISSION_ID");

    RoleCreateRequest body =
        new RoleCreateRequest()
            .data(
                new RoleCreateData()
                    .type(RolesType.ROLES)
                    .attributes(new RoleCreateAttributes().name("Example-Role"))
                    .relationships(
                        new RoleRelationships()
                            .permissions(
                                new RelationshipToPermissions()
                                    .data(
                                        Collections.singletonList(
                                            new RelationshipToPermissionData()
                                                .id(PERMISSION_ID)
                                                .type(PermissionsType.PERMISSIONS))))));

    try {
      RoleCreateResponse result = apiInstance.createRole(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#createRole");
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
Create role with a permission returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.permissions_type import PermissionsType
from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData
from datadog_api_client.v2.model.relationship_to_permissions import RelationshipToPermissions
from datadog_api_client.v2.model.role_create_attributes import RoleCreateAttributes
from datadog_api_client.v2.model.role_create_data import RoleCreateData
from datadog_api_client.v2.model.role_create_request import RoleCreateRequest
from datadog_api_client.v2.model.role_relationships import RoleRelationships
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RoleCreateRequest(
    data=RoleCreateData(
        type=RolesType.ROLES,
        attributes=RoleCreateAttributes(
            name="Example-Role",
        ),
        relationships=RoleRelationships(
            permissions=RelationshipToPermissions(
                data=[
                    RelationshipToPermissionData(
                        id=PERMISSION_ID,
                        type=PermissionsType.PERMISSIONS,
                    ),
                ],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.create_role(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create role with a permission returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "permission" in the system
PERMISSION_ID = ENV["PERMISSION_ID"]

body = DatadogAPIClient::V2::RoleCreateRequest.new({
  data: DatadogAPIClient::V2::RoleCreateData.new({
    type: DatadogAPIClient::V2::RolesType::ROLES,
    attributes: DatadogAPIClient::V2::RoleCreateAttributes.new({
      name: "Example-Role",
    }),
    relationships: DatadogAPIClient::V2::RoleRelationships.new({
      permissions: DatadogAPIClient::V2::RelationshipToPermissions.new({
        data: [
          DatadogAPIClient::V2::RelationshipToPermissionData.new({
            id: PERMISSION_ID,
            type: DatadogAPIClient::V2::PermissionsType::PERMISSIONS,
          }),
        ],
      }),
    }),
  }),
})
p api_instance.create_role(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create role with a permission returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;
use datadog_api_client::datadogV2::model::PermissionsType;
use datadog_api_client::datadogV2::model::RelationshipToPermissionData;
use datadog_api_client::datadogV2::model::RelationshipToPermissions;
use datadog_api_client::datadogV2::model::RoleCreateAttributes;
use datadog_api_client::datadogV2::model::RoleCreateData;
use datadog_api_client::datadogV2::model::RoleCreateRequest;
use datadog_api_client::datadogV2::model::RoleRelationships;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "permission" in the system
    let permission_id = std::env::var("PERMISSION_ID").unwrap();
    let body = RoleCreateRequest::new(
        RoleCreateData::new(RoleCreateAttributes::new("Example-Role".to_string()))
            .relationships(RoleRelationships::new().permissions(
                RelationshipToPermissions::new().data(vec![
                                RelationshipToPermissionData::new()
                                    .id(permission_id.clone())
                                    .type_(PermissionsType::PERMISSIONS)
                            ]),
            ))
            .type_(RolesType::ROLES),
    );
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.create_role(body).await;
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
 * Create role with a permission returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "permission" in the system
const PERMISSION_ID = process.env.PERMISSION_ID as string;

const params: v2.RolesApiCreateRoleRequest = {
  body: {
    data: {
      type: "roles",
      attributes: {
        name: "Example-Role",
      },
      relationships: {
        permissions: {
          data: [
            {
              id: PERMISSION_ID,
              type: "permissions",
            },
          ],
        },
      },
    },
  },
};

apiInstance
  .createRole(params)
  .then((data: v2.RoleCreateResponse) => {
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

## Get a role{% #get-a-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/roles/{role_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/roles/{role_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/roles/{role_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/roles/{role_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/roles/{role_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/roles/{role_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/roles/{role_id} |

### Overview

Get a role in the organization specified by the role's `role_id`.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single role.

| Parent field  | Field                     | Type      | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object    | Role object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object    | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string    | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]  | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64     | Number of users with that role.                                                                                                                                                                                                                                                               |
| data          | id                        | string    | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | relationships             | object    | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object    | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]  | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string    | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum      | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum      | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "receives_permissions_from": [],
      "user_count": "integer"
    },
    "id": "string",
    "relationships": {
      "permissions": {
        "data": [
          {
            "id": "string",
            "type": "permissions"
          }
        ]
      }
    },
    "type": "roles"
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
                  \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.get_role(
        role_id=ROLE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.get_role(ROLE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a role returns "OK" response

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

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.GetRole(ctx, RoleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.GetRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.GetRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.RoleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    try {
      RoleResponse result = apiInstance.getRole(ROLE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#getRole");
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
// Get a role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.get_role(role_data_id.clone()).await;
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
 * Get a role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.RolesApiGetRoleRequest = {
  roleId: ROLE_DATA_ID,
};

apiInstance
  .getRole(params)
  .then((data: v2.RoleResponse) => {
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

## Update a role{% #update-a-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/roles/{role_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/roles/{role_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/roles/{role_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/roles/{role_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/roles/{role_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/roles/{role_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/roles/{role_id} |

### Overview

Edit a role. Can only be used with application keys belonging to administrators. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                        | Type      | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ---------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data [*required*]       | object    | Data related to the update of a role.                                                                                                                                                                                                                                                         |
| data          | attributes [*required*] | object    | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                   | date-time | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at                  | date-time | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                         | string    | Name of the role.                                                                                                                                                                                                                                                                             |
| attributes    | receives_permissions_from    | [string]  | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                   | int32     | The user count.                                                                                                                                                                                                                                                                               |
| data          | id [*required*]         | string    | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | relationships                | object    | Relationships of the role object.                                                                                                                                                                                                                                                             |
| relationships | permissions                  | object    | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                         | [object]  | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                           | string    | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                         | enum      | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| data          | type [*required*]       | enum      | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "string",
    "type": "roles",
    "attributes": {
      "name": "developers-updated"
    },
    "relationships": {
      "permissions": {
        "data": [
          {
            "id": "f2a8beb4-91f8-962d-b6d9-60215cda2214",
            "type": "permissions"
          }
        ]
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about an updated role.

| Parent field  | Field                     | Type      | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object    | Role object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object    | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string    | Name of the role.                                                                                                                                                                                                                                                                             |
| attributes    | receives_permissions_from | [string]  | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int32     | The user count.                                                                                                                                                                                                                                                                               |
| data          | id                        | string    | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | relationships             | object    | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object    | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]  | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string    | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum      | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum      | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "receives_permissions_from": [],
      "user_count": "integer"
    },
    "id": "string",
    "relationships": {
      "permissions": {
        "data": [
          {
            "id": "string",
            "type": "permissions"
          }
        ]
      }
    },
    "type": "roles"
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
                  \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {},
    "id": "00000000-0000-1111-0000-000000000000",
    "type": "roles"
  }
}
EOF
                
##### 

```python
"""
Update a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.permissions_type import PermissionsType
from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData
from datadog_api_client.v2.model.relationship_to_permissions import RelationshipToPermissions
from datadog_api_client.v2.model.role_relationships import RoleRelationships
from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes
from datadog_api_client.v2.model.role_update_data import RoleUpdateData
from datadog_api_client.v2.model.role_update_request import RoleUpdateRequest
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = environ["ROLE_DATA_ATTRIBUTES_NAME"]
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RoleUpdateRequest(
    data=RoleUpdateData(
        id=ROLE_DATA_ID,
        type=RolesType.ROLES,
        attributes=RoleUpdateAttributes(
            name="developers-updated",
        ),
        relationships=RoleRelationships(
            permissions=RelationshipToPermissions(
                data=[
                    RelationshipToPermissionData(
                        id=PERMISSION_ID,
                        type=PermissionsType.PERMISSIONS,
                    ),
                ],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.update_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = ENV["ROLE_DATA_ATTRIBUTES_NAME"]
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = ENV["PERMISSION_ID"]

body = DatadogAPIClient::V2::RoleUpdateRequest.new({
  data: DatadogAPIClient::V2::RoleUpdateData.new({
    id: ROLE_DATA_ID,
    type: DatadogAPIClient::V2::RolesType::ROLES,
    attributes: DatadogAPIClient::V2::RoleUpdateAttributes.new({
      name: "developers-updated",
    }),
    relationships: DatadogAPIClient::V2::RoleRelationships.new({
      permissions: DatadogAPIClient::V2::RelationshipToPermissions.new({
        data: [
          DatadogAPIClient::V2::RelationshipToPermissionData.new({
            id: PERMISSION_ID,
            type: DatadogAPIClient::V2::PermissionsType::PERMISSIONS,
          }),
        ],
      }),
    }),
  }),
})
p api_instance.update_role(ROLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Update a role returns "OK" response

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

	// there is a valid "permission" in the system
	PermissionID := os.Getenv("PERMISSION_ID")

	body := datadogV2.RoleUpdateRequest{
		Data: datadogV2.RoleUpdateData{
			Id:   RoleDataID,
			Type: datadogV2.ROLESTYPE_ROLES,
			Attributes: datadogV2.RoleUpdateAttributes{
				Name: datadog.PtrString("developers-updated"),
			},
			Relationships: &datadogV2.RoleRelationships{
				Permissions: &datadogV2.RelationshipToPermissions{
					Data: []datadogV2.RelationshipToPermissionData{
						{
							Id:   datadog.PtrString(PermissionID),
							Type: datadogV2.PERMISSIONSTYPE_PERMISSIONS.Ptr(),
						},
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.UpdateRole(ctx, RoleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.UpdateRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.UpdateRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update a role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.PermissionsType;
import com.datadog.api.client.v2.model.RelationshipToPermissionData;
import com.datadog.api.client.v2.model.RelationshipToPermissions;
import com.datadog.api.client.v2.model.RoleRelationships;
import com.datadog.api.client.v2.model.RoleUpdateAttributes;
import com.datadog.api.client.v2.model.RoleUpdateData;
import com.datadog.api.client.v2.model.RoleUpdateRequest;
import com.datadog.api.client.v2.model.RoleUpdateResponse;
import com.datadog.api.client.v2.model.RolesType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ATTRIBUTES_NAME = System.getenv("ROLE_DATA_ATTRIBUTES_NAME");
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    // there is a valid "permission" in the system
    String PERMISSION_ID = System.getenv("PERMISSION_ID");

    RoleUpdateRequest body =
        new RoleUpdateRequest()
            .data(
                new RoleUpdateData()
                    .id(ROLE_DATA_ID)
                    .type(RolesType.ROLES)
                    .attributes(new RoleUpdateAttributes().name("developers-updated"))
                    .relationships(
                        new RoleRelationships()
                            .permissions(
                                new RelationshipToPermissions()
                                    .data(
                                        Collections.singletonList(
                                            new RelationshipToPermissionData()
                                                .id(PERMISSION_ID)
                                                .type(PermissionsType.PERMISSIONS))))));

    try {
      RoleUpdateResponse result = apiInstance.updateRole(ROLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#updateRole");
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
// Update a role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;
use datadog_api_client::datadogV2::model::PermissionsType;
use datadog_api_client::datadogV2::model::RelationshipToPermissionData;
use datadog_api_client::datadogV2::model::RelationshipToPermissions;
use datadog_api_client::datadogV2::model::RoleRelationships;
use datadog_api_client::datadogV2::model::RoleUpdateAttributes;
use datadog_api_client::datadogV2::model::RoleUpdateData;
use datadog_api_client::datadogV2::model::RoleUpdateRequest;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();

    // there is a valid "permission" in the system
    let permission_id = std::env::var("PERMISSION_ID").unwrap();
    let body = RoleUpdateRequest::new(
        RoleUpdateData::new(
            RoleUpdateAttributes::new().name("developers-updated".to_string()),
            role_data_id.clone(),
            RolesType::ROLES,
        )
        .relationships(RoleRelationships::new().permissions(
            RelationshipToPermissions::new().data(vec![
                            RelationshipToPermissionData::new()
                                .id(permission_id.clone())
                                .type_(PermissionsType::PERMISSIONS)
                        ]),
        )),
    );
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.update_role(role_data_id.clone(), body).await;
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
 * Update a role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

// there is a valid "permission" in the system
const PERMISSION_ID = process.env.PERMISSION_ID as string;

const params: v2.RolesApiUpdateRoleRequest = {
  body: {
    data: {
      id: ROLE_DATA_ID,
      type: "roles",
      attributes: {
        name: "developers-updated",
      },
      relationships: {
        permissions: {
          data: [
            {
              id: PERMISSION_ID,
              type: "permissions",
            },
          ],
        },
      },
    },
  },
  roleId: ROLE_DATA_ID,
};

apiInstance
  .updateRole(params)
  .then((data: v2.RoleUpdateResponse) => {
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

## Delete role{% #delete-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/roles/{role_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/roles/{role_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/roles/{role_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/roles/{role_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/roles/{role_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/roles/{role_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/roles/{role_id} |

### Overview

Disables a role.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

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
                  \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    api_instance.delete_role(
        role_id=ROLE_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
api_instance.delete_role(ROLE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete role returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "role" in the system
	RoleDataID := os.Getenv("ROLE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	r, err := api.DeleteRole(ctx, RoleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.DeleteRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    try {
      apiInstance.deleteRole(ROLE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#deleteRole");
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
// Delete role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.delete_role(role_data_id.clone()).await;
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
 * Delete role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.RolesApiDeleteRoleRequest = {
  roleId: ROLE_DATA_ID,
};

apiInstance
  .deleteRole(params)
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

## List permissions for a role{% #list-permissions-for-a-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/permissions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/roles/{role_id}/permissions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/roles/{role_id}/permissions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/roles/{role_id}/permissions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/roles/{role_id}/permissions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/roles/{role_id}/permissions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/roles/{role_id}/permissions |

### Overview

Returns a list of all permissions for a single role.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

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
                  \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/permissions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List permissions for a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.list_role_permissions(
        role_id=ROLE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List permissions for a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.list_role_permissions(ROLE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List permissions for a role returns "OK" response

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

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.ListRolePermissions(ctx, RoleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.ListRolePermissions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.ListRolePermissions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List permissions for a role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.PermissionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    try {
      PermissionsResponse result = apiInstance.listRolePermissions(ROLE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#listRolePermissions");
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
// List permissions for a role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.list_role_permissions(role_data_id.clone()).await;
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
 * List permissions for a role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.RolesApiListRolePermissionsRequest = {
  roleId: ROLE_DATA_ID,
};

apiInstance
  .listRolePermissions(params)
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

## Grant permission to a role{% #grant-permission-to-a-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/permissions |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/roles/{role_id}/permissions |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/roles/{role_id}/permissions      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/roles/{role_id}/permissions      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/roles/{role_id}/permissions     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/roles/{role_id}/permissions |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/roles/{role_id}/permissions |

### Overview

Adds a permission to a role. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field | Type   | Description                                                   |
| ------------ | ----- | ------ | ------------------------------------------------------------- |
|              | data  | object | Relationship to permission object.                            |
| data         | id    | string | ID of the permission.                                         |
| data         | type  | enum   | Permissions resource type. Allowed enum values: `permissions` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "f2a8beb4-91f8-962d-b6d9-60215cda2214",
    "type": "permissions"
  }
}
```

{% /tab %}

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
                          \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/permissions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "f2a8beb4-91f8-962d-b6d9-60215cda2214",
    "type": "permissions"
  }
}
EOF
                        
##### 

```go
// Grant permission to a role returns "OK" response

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

	// there is a valid "permission" in the system
	PermissionID := os.Getenv("PERMISSION_ID")

	body := datadogV2.RelationshipToPermission{
		Data: &datadogV2.RelationshipToPermissionData{
			Id:   datadog.PtrString(PermissionID),
			Type: datadogV2.PERMISSIONSTYPE_PERMISSIONS.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.AddPermissionToRole(ctx, RoleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.AddPermissionToRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.AddPermissionToRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Grant permission to a role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.PermissionsResponse;
import com.datadog.api.client.v2.model.PermissionsType;
import com.datadog.api.client.v2.model.RelationshipToPermission;
import com.datadog.api.client.v2.model.RelationshipToPermissionData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    // there is a valid "permission" in the system
    String PERMISSION_ID = System.getenv("PERMISSION_ID");

    RelationshipToPermission body =
        new RelationshipToPermission()
            .data(
                new RelationshipToPermissionData()
                    .id(PERMISSION_ID)
                    .type(PermissionsType.PERMISSIONS));

    try {
      PermissionsResponse result = apiInstance.addPermissionToRole(ROLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#addPermissionToRole");
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
Grant permission to a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.permissions_type import PermissionsType
from datadog_api_client.v2.model.relationship_to_permission import RelationshipToPermission
from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RelationshipToPermission(
    data=RelationshipToPermissionData(
        id=PERMISSION_ID,
        type=PermissionsType.PERMISSIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.add_permission_to_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Grant permission to a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = ENV["PERMISSION_ID"]

body = DatadogAPIClient::V2::RelationshipToPermission.new({
  data: DatadogAPIClient::V2::RelationshipToPermissionData.new({
    id: PERMISSION_ID,
    type: DatadogAPIClient::V2::PermissionsType::PERMISSIONS,
  }),
})
p api_instance.add_permission_to_role(ROLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Grant permission to a role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;
use datadog_api_client::datadogV2::model::PermissionsType;
use datadog_api_client::datadogV2::model::RelationshipToPermission;
use datadog_api_client::datadogV2::model::RelationshipToPermissionData;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();

    // there is a valid "permission" in the system
    let permission_id = std::env::var("PERMISSION_ID").unwrap();
    let body = RelationshipToPermission::new().data(
        RelationshipToPermissionData::new()
            .id(permission_id.clone())
            .type_(PermissionsType::PERMISSIONS),
    );
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.add_permission_to_role(role_data_id.clone(), body).await;
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
 * Grant permission to a role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

// there is a valid "permission" in the system
const PERMISSION_ID = process.env.PERMISSION_ID as string;

const params: v2.RolesApiAddPermissionToRoleRequest = {
  body: {
    data: {
      id: PERMISSION_ID,
      type: "permissions",
    },
  },
  roleId: ROLE_DATA_ID,
};

apiInstance
  .addPermissionToRole(params)
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

## Revoke permission{% #revoke-permission %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/permissions |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/roles/{role_id}/permissions |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/roles/{role_id}/permissions      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/roles/{role_id}/permissions      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/roles/{role_id}/permissions     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/roles/{role_id}/permissions |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/roles/{role_id}/permissions |

### Overview

Removes a permission from a role. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field | Type   | Description                                                   |
| ------------ | ----- | ------ | ------------------------------------------------------------- |
|              | data  | object | Relationship to permission object.                            |
| data         | id    | string | ID of the permission.                                         |
| data         | type  | enum   | Permissions resource type. Allowed enum values: `permissions` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "f2a8beb4-91f8-962d-b6d9-60215cda2214",
    "type": "permissions"
  }
}
```

{% /tab %}

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
                          \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/permissions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "f2a8beb4-91f8-962d-b6d9-60215cda2214",
    "type": "permissions"
  }
}
EOF
                        
##### 

```go
// Revoke permission returns "OK" response

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

	// there is a valid "permission" in the system
	PermissionID := os.Getenv("PERMISSION_ID")

	body := datadogV2.RelationshipToPermission{
		Data: &datadogV2.RelationshipToPermissionData{
			Id:   datadog.PtrString(PermissionID),
			Type: datadogV2.PERMISSIONSTYPE_PERMISSIONS.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.RemovePermissionFromRole(ctx, RoleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.RemovePermissionFromRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.RemovePermissionFromRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Revoke permission returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.PermissionsResponse;
import com.datadog.api.client.v2.model.PermissionsType;
import com.datadog.api.client.v2.model.RelationshipToPermission;
import com.datadog.api.client.v2.model.RelationshipToPermissionData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    // there is a valid "permission" in the system
    String PERMISSION_ID = System.getenv("PERMISSION_ID");

    RelationshipToPermission body =
        new RelationshipToPermission()
            .data(
                new RelationshipToPermissionData()
                    .id(PERMISSION_ID)
                    .type(PermissionsType.PERMISSIONS));

    try {
      PermissionsResponse result = apiInstance.removePermissionFromRole(ROLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#removePermissionFromRole");
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
Revoke permission returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.permissions_type import PermissionsType
from datadog_api_client.v2.model.relationship_to_permission import RelationshipToPermission
from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RelationshipToPermission(
    data=RelationshipToPermissionData(
        id=PERMISSION_ID,
        type=PermissionsType.PERMISSIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.remove_permission_from_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Revoke permission returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = ENV["PERMISSION_ID"]

body = DatadogAPIClient::V2::RelationshipToPermission.new({
  data: DatadogAPIClient::V2::RelationshipToPermissionData.new({
    id: PERMISSION_ID,
    type: DatadogAPIClient::V2::PermissionsType::PERMISSIONS,
  }),
})
p api_instance.remove_permission_from_role(ROLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Revoke permission returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;
use datadog_api_client::datadogV2::model::PermissionsType;
use datadog_api_client::datadogV2::model::RelationshipToPermission;
use datadog_api_client::datadogV2::model::RelationshipToPermissionData;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();

    // there is a valid "permission" in the system
    let permission_id = std::env::var("PERMISSION_ID").unwrap();
    let body = RelationshipToPermission::new().data(
        RelationshipToPermissionData::new()
            .id(permission_id.clone())
            .type_(PermissionsType::PERMISSIONS),
    );
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api
        .remove_permission_from_role(role_data_id.clone(), body)
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
 * Revoke permission returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

// there is a valid "permission" in the system
const PERMISSION_ID = process.env.PERMISSION_ID as string;

const params: v2.RolesApiRemovePermissionFromRoleRequest = {
  body: {
    data: {
      id: PERMISSION_ID,
      type: "permissions",
    },
  },
  roleId: ROLE_DATA_ID,
};

apiInstance
  .removePermissionFromRole(params)
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

## Get all users of a role{% #get-all-users-of-a-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/users |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/roles/{role_id}/users |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/roles/{role_id}/users      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/roles/{role_id}/users      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/roles/{role_id}/users     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/roles/{role_id}/users |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/roles/{role_id}/users |

### Overview

Gets all users of a role.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

#### Query Strings

| Name         | Type    | Description                                                                                                                                                                                                         |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                            |
| page[number] | integer | Specific page number to return.                                                                                                                                                                                     |
| sort         | string  | User attribute to order results by. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `email`, `status`. |
| filter       | string  | Filter all users by the given string. Defaults to no filtering.                                                                                                                                                     |

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
                  \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/users" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all users of a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.list_role_users(
        role_id=ROLE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get all users of a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.list_role_users(ROLE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get all users of a role returns "OK" response

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

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.ListRoleUsers(ctx, RoleDataID, *datadogV2.NewListRoleUsersOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.ListRoleUsers`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.ListRoleUsers`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get all users of a role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.UsersResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    try {
      UsersResponse result = apiInstance.listRoleUsers(ROLE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#listRoleUsers");
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
// Get all users of a role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::ListRoleUsersOptionalParams;
use datadog_api_client::datadogV2::api_roles::RolesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api
        .list_role_users(role_data_id.clone(), ListRoleUsersOptionalParams::default())
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
 * Get all users of a role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.RolesApiListRoleUsersRequest = {
  roleId: ROLE_DATA_ID,
};

apiInstance
  .listRoleUsers(params)
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

## Add a user to a role{% #add-a-user-to-a-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/users |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/roles/{role_id}/users |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/roles/{role_id}/users      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/roles/{role_id}/users      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/roles/{role_id}/users     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/roles/{role_id}/users |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/roles/{role_id}/users |

### Overview

Adds a user to a role. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                       |
| ------------ | ---------------------- | ------ | ------------------------------------------------- |
|              | data [*required*] | object | Relationship to user object.                      |
| data         | id [*required*]   | string | A unique identifier that represents the user.     |
| data         | type [*required*] | enum   | Users resource type. Allowed enum values: `users` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "c1d4eb9e-8bb0-974d-85a5-a7dd9db46bee",
    "type": "users"
  }
}
```

{% /tab %}

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
                          \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/users" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "c1d4eb9e-8bb0-974d-85a5-a7dd9db46bee",
    "type": "users"
  }
}
EOF
                        
##### 

```go
// Add a user to a role returns "OK" response

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

	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	body := datadogV2.RelationshipToUser{
		Data: datadogV2.RelationshipToUserData{
			Id:   UserDataID,
			Type: datadogV2.USERSTYPE_USERS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.AddUserToRole(ctx, RoleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.AddUserToRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.AddUserToRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Add a user to a role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.RelationshipToUser;
import com.datadog.api.client.v2.model.RelationshipToUserData;
import com.datadog.api.client.v2.model.UsersResponse;
import com.datadog.api.client.v2.model.UsersType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    RelationshipToUser body =
        new RelationshipToUser()
            .data(new RelationshipToUserData().id(USER_DATA_ID).type(UsersType.USERS));

    try {
      UsersResponse result = apiInstance.addUserToRole(ROLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#addUserToRole");
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
Add a user to a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = RelationshipToUser(
    data=RelationshipToUserData(
        id=USER_DATA_ID,
        type=UsersType.USERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.add_user_to_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Add a user to a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::RelationshipToUser.new({
  data: DatadogAPIClient::V2::RelationshipToUserData.new({
    id: USER_DATA_ID,
    type: DatadogAPIClient::V2::UsersType::USERS,
  }),
})
p api_instance.add_user_to_role(ROLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Add a user to a role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;
use datadog_api_client::datadogV2::model::RelationshipToUser;
use datadog_api_client::datadogV2::model::RelationshipToUserData;
use datadog_api_client::datadogV2::model::UsersType;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();

    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = RelationshipToUser::new(RelationshipToUserData::new(
        user_data_id.clone(),
        UsersType::USERS,
    ));
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.add_user_to_role(role_data_id.clone(), body).await;
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
 * Add a user to a role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.RolesApiAddUserToRoleRequest = {
  body: {
    data: {
      id: USER_DATA_ID,
      type: "users",
    },
  },
  roleId: ROLE_DATA_ID,
};

apiInstance
  .addUserToRole(params)
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

## Remove a user from a role{% #remove-a-user-from-a-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/users |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/roles/{role_id}/users |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/roles/{role_id}/users      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/roles/{role_id}/users      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/roles/{role_id}/users     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/roles/{role_id}/users |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/roles/{role_id}/users |

### Overview

Removes a user from a role. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                       |
| ------------ | ---------------------- | ------ | ------------------------------------------------- |
|              | data [*required*] | object | Relationship to user object.                      |
| data         | id [*required*]   | string | A unique identifier that represents the user.     |
| data         | type [*required*] | enum   | Users resource type. Allowed enum values: `users` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "c1d4eb9e-8bb0-974d-85a5-a7dd9db46bee",
    "type": "users"
  }
}
```

{% /tab %}

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
                          \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/users" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "c1d4eb9e-8bb0-974d-85a5-a7dd9db46bee",
    "type": "users"
  }
}
EOF
                        
##### 

```go
// Remove a user from a role returns "OK" response

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

	// there is a valid "user" in the system
	UserDataID := os.Getenv("USER_DATA_ID")

	body := datadogV2.RelationshipToUser{
		Data: datadogV2.RelationshipToUserData{
			Id:   UserDataID,
			Type: datadogV2.USERSTYPE_USERS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.RemoveUserFromRole(ctx, RoleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.RemoveUserFromRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.RemoveUserFromRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Remove a user from a role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.RelationshipToUser;
import com.datadog.api.client.v2.model.RelationshipToUserData;
import com.datadog.api.client.v2.model.UsersResponse;
import com.datadog.api.client.v2.model.UsersType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    RelationshipToUser body =
        new RelationshipToUser()
            .data(new RelationshipToUserData().id(USER_DATA_ID).type(UsersType.USERS));

    try {
      UsersResponse result = apiInstance.removeUserFromRole(ROLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#removeUserFromRole");
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
Remove a user from a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = RelationshipToUser(
    data=RelationshipToUserData(
        id=USER_DATA_ID,
        type=UsersType.USERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.remove_user_from_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Remove a user from a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]

body = DatadogAPIClient::V2::RelationshipToUser.new({
  data: DatadogAPIClient::V2::RelationshipToUserData.new({
    id: USER_DATA_ID,
    type: DatadogAPIClient::V2::UsersType::USERS,
  }),
})
p api_instance.remove_user_from_role(ROLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Remove a user from a role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;
use datadog_api_client::datadogV2::model::RelationshipToUser;
use datadog_api_client::datadogV2::model::RelationshipToUserData;
use datadog_api_client::datadogV2::model::UsersType;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();

    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let body = RelationshipToUser::new(RelationshipToUserData::new(
        user_data_id.clone(),
        UsersType::USERS,
    ));
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.remove_user_from_role(role_data_id.clone(), body).await;
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
 * Remove a user from a role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.RolesApiRemoveUserFromRoleRequest = {
  body: {
    data: {
      id: USER_DATA_ID,
      type: "users",
    },
  },
  roleId: ROLE_DATA_ID,
};

apiInstance
  .removeUserFromRole(params)
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

## Create a new role by cloning an existing role{% #create-a-new-role-by-cloning-an-existing-role %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/clone |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/roles/{role_id}/clone |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/roles/{role_id}/clone      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/roles/{role_id}/clone      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/roles/{role_id}/clone     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/roles/{role_id}/clone |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/roles/{role_id}/clone |

### Overview

Clone an existing role This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| role_id [*required*] | string | The unique identifier of the role. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                                                                                                                                                                                   |
| ------------ | ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Data for the clone role request.                                                                                                                                                                                                                                                              |
| data         | attributes [*required*] | object   | Attributes required to create a new role by cloning an existing one.                                                                                                                                                                                                                          |
| attributes   | name [*required*]       | string   | Name of the new role that is cloned.                                                                                                                                                                                                                                                          |
| attributes   | receives_permissions_from    | [string] | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| data         | type [*required*]       | enum     | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Example-Role clone"
    },
    "type": "roles"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single role.

| Parent field  | Field                     | Type      | Description                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               | data                      | object    | Role object returned by the API.                                                                                                                                                                                                                                                              |
| data          | attributes                | object    | Attributes of the role.                                                                                                                                                                                                                                                                       |
| attributes    | created_at                | date-time | Creation time of the role.                                                                                                                                                                                                                                                                    |
| attributes    | modified_at               | date-time | Time of last role modification.                                                                                                                                                                                                                                                               |
| attributes    | name                      | string    | The name of the role. The name is neither unique nor a stable identifier of the role.                                                                                                                                                                                                         |
| attributes    | receives_permissions_from | [string]  | The managed role from which this role automatically inherits new permissions. Specify one of the following: "Datadog Admin Role", "Datadog Standard Role", or "Datadog Read Only Role". If empty or not specified, the role does not automatically inherit permissions from any managed role. |
| attributes    | user_count                | int64     | Number of users with that role.                                                                                                                                                                                                                                                               |
| data          | id                        | string    | The unique identifier of the role.                                                                                                                                                                                                                                                            |
| data          | relationships             | object    | Relationships of the role object returned by the API.                                                                                                                                                                                                                                         |
| relationships | permissions               | object    | Relationship to multiple permissions objects.                                                                                                                                                                                                                                                 |
| permissions   | data                      | [object]  | Relationships to permission objects.                                                                                                                                                                                                                                                          |
| data          | id                        | string    | ID of the permission.                                                                                                                                                                                                                                                                         |
| data          | type                      | enum      | Permissions resource type. Allowed enum values: `permissions`                                                                                                                                                                                                                                 |
| data          | type [*required*]    | enum      | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "receives_permissions_from": [],
      "user_count": "integer"
    },
    "id": "string",
    "relationships": {
      "permissions": {
        "data": [
          {
            "id": "string",
            "type": "permissions"
          }
        ]
      }
    },
    "type": "roles"
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

{% tab title="409" %}
Conflict
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
                          \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/clone" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-Role clone"
    },
    "type": "roles"
  }
}
EOF
                        
##### 

```go
// Create a new role by cloning an existing role returns "OK" response

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

	body := datadogV2.RoleCloneRequest{
		Data: datadogV2.RoleClone{
			Attributes: datadogV2.RoleCloneAttributes{
				Name: "Example-Role clone",
			},
			Type: datadogV2.ROLESTYPE_ROLES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.CloneRole(ctx, RoleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.CloneRole`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.CloneRole`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create a new role by cloning an existing role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.RoleClone;
import com.datadog.api.client.v2.model.RoleCloneAttributes;
import com.datadog.api.client.v2.model.RoleCloneRequest;
import com.datadog.api.client.v2.model.RoleResponse;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RolesApi apiInstance = new RolesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    RoleCloneRequest body =
        new RoleCloneRequest()
            .data(
                new RoleClone()
                    .attributes(new RoleCloneAttributes().name("Example-Role clone"))
                    .type(RolesType.ROLES));

    try {
      RoleResponse result = apiInstance.cloneRole(ROLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#cloneRole");
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
Create a new role by cloning an existing role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.role_clone import RoleClone
from datadog_api_client.v2.model.role_clone_attributes import RoleCloneAttributes
from datadog_api_client.v2.model.role_clone_request import RoleCloneRequest
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RoleCloneRequest(
    data=RoleClone(
        attributes=RoleCloneAttributes(
            name="Example-Role clone",
        ),
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.clone_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create a new role by cloning an existing role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::RoleCloneRequest.new({
  data: DatadogAPIClient::V2::RoleClone.new({
    attributes: DatadogAPIClient::V2::RoleCloneAttributes.new({
      name: "Example-Role clone",
    }),
    type: DatadogAPIClient::V2::RolesType::ROLES,
  }),
})
p api_instance.clone_role(ROLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create a new role by cloning an existing role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;
use datadog_api_client::datadogV2::model::RoleClone;
use datadog_api_client::datadogV2::model::RoleCloneAttributes;
use datadog_api_client::datadogV2::model::RoleCloneRequest;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = RoleCloneRequest::new(RoleClone::new(
        RoleCloneAttributes::new("Example-Role clone".to_string()),
        RolesType::ROLES,
    ));
    let configuration = datadog::Configuration::new();
    let api = RolesAPI::with_config(configuration);
    let resp = api.clone_role(role_data_id.clone(), body).await;
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
 * Create a new role by cloning an existing role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RolesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.RolesApiCloneRoleRequest = {
  body: {
    data: {
      attributes: {
        name: "Example-Role clone",
      },
      type: "roles",
    },
  },
  roleId: ROLE_DATA_ID,
};

apiInstance
  .cloneRole(params)
  .then((data: v2.RoleResponse) => {
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

## List role templates{% #list-role-templates %}

{% tab title="v2" %}
**Note**: This endpoint may be subject to changes.
| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/roles/templates |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/roles/templates |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/roles/templates      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/roles/templates      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/roles/templates     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/roles/templates |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/roles/templates |

### Overview

List all role templates

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `RoleTemplateArray` object.

| Parent field | Field                  | Type     | Description                                            |
| ------------ | ---------------------- | -------- | ------------------------------------------------------ |
|              | data [*required*] | [object] | The `RoleTemplateArray` `data`.                        |
| data         | attributes             | object   | The definition of `RoleTemplateDataAttributes` object. |
| attributes   | description            | string   | The `attributes` `description`.                        |
| attributes   | name                   | string   | The `attributes` `name`.                               |
| data         | id                     | string   | The `RoleTemplateData` `id`.                           |
| data         | type [*required*] | enum     | Roles resource type. Allowed enum values: `roles`      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "description": "string",
        "name": "string"
      },
      "id": "string",
      "type": "roles"
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/templates" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List role templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

configuration = Configuration()
configuration.unstable_operations["list_role_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.list_role_templates()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List role templates returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_role_templates".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RolesAPI.new
p api_instance.list_role_templates()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List role templates returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListRoleTemplates", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRolesApi(apiClient)
	resp, r, err := api.ListRoleTemplates(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolesApi.ListRoleTemplates`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RolesApi.ListRoleTemplates`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List role templates returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RolesApi;
import com.datadog.api.client.v2.model.RoleTemplateArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listRoleTemplates", true);
    RolesApi apiInstance = new RolesApi(defaultClient);

    try {
      RoleTemplateArray result = apiInstance.listRoleTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#listRoleTemplates");
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
// List role templates returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_roles::RolesAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListRoleTemplates", true);
    let api = RolesAPI::with_config(configuration);
    let resp = api.list_role_templates().await;
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
 * List role templates returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listRoleTemplates"] = true;
const apiInstance = new v2.RolesApi(configuration);

apiInstance
  .listRoleTemplates()
  .then((data: v2.RoleTemplateArray) => {
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
