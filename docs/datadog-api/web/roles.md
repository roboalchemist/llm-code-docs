# Source: https://docs.datadoghq.com/api/latest/roles

# Roles
The Roles API is used to create and manage Datadog roles, what [global permissions](https://docs.datadoghq.com/account_management/rbac/) they grant, and which users belong to them.
Permissions related to specific account assets can be granted to roles in the Datadog application without using this API. For example, granting read access on a specific log index to a role can be done in Datadog from the [Pipelines page](https://app.datadoghq.com/logs/pipelines).
## [List permissions](https://docs.datadoghq.com/api/latest/roles/#list-permissions)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#list-permissions-v2)


GET https://api.ap1.datadoghq.com/api/v2/permissionshttps://api.ap2.datadoghq.com/api/v2/permissionshttps://api.datadoghq.eu/api/v2/permissionshttps://api.ddog-gov.com/api/v2/permissionshttps://api.datadoghq.com/api/v2/permissionshttps://api.us3.datadoghq.com/api/v2/permissionshttps://api.us5.datadoghq.com/api/v2/permissions
### Overview
Returns a list of all permissions, including name, description, and ID. This endpoint requires the `user_access_read` permission.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#ListPermissions-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#ListPermissions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#ListPermissions-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#ListPermissions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


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
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  List permissions
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/permissions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List permissions
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List permissions
```
# List permissions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new
p api_instance.list_permissions()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List permissions
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List permissions
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List permissions
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List permissions
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List roles](https://docs.datadoghq.com/api/latest/roles/#list-roles)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#list-roles-v2)


GET https://api.ap1.datadoghq.com/api/v2/roleshttps://api.ap2.datadoghq.com/api/v2/roleshttps://api.datadoghq.eu/api/v2/roleshttps://api.ddog-gov.com/api/v2/roleshttps://api.datadoghq.com/api/v2/roleshttps://api.us3.datadoghq.com/api/v2/roleshttps://api.us5.datadoghq.com/api/v2/roles
### Overview
Returns all roles, including their names and their unique identifiers. This endpoint requires the `user_access_read` permission.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
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
Sort roles depending on the given field. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example: `sort=-name`.  
Allowed enum values: `name, -name, modified_at, -modified_at, user_count, -user_count`
filter
string
Filter all roles by the given string.
filter[id]
string
Filter all roles by the given list of role IDs.
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#ListRoles-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#ListRoles-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#ListRoles-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Response containing information about multiple roles.
Field
Type
Description
data
[object]
Array of returned roles.
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
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
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

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  List roles
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List roles
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List roles
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List roles
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List roles
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List roles
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List roles
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create role](https://docs.datadoghq.com/api/latest/roles/#create-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#create-role-v2)


POST https://api.ap1.datadoghq.com/api/v2/roleshttps://api.ap2.datadoghq.com/api/v2/roleshttps://api.datadoghq.eu/api/v2/roleshttps://api.ddog-gov.com/api/v2/roleshttps://api.datadoghq.com/api/v2/roleshttps://api.us3.datadoghq.com/api/v2/roleshttps://api.us5.datadoghq.com/api/v2/roles
### Overview
Create a new role for your organization. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Field
Type
Description
data [_required_]
object
Data related to the creation of a role.
attributes [_required_]
object
Attributes of the created role.
created_at
date-time
Creation time of the role.
modified_at
date-time
Time of last role modification.
name [_required_]
string
Name of the role.
relationships
object
Relationships of the role object.
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
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#CreateRole-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#CreateRole-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#CreateRole-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#CreateRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Response containing information about a created role.
Field
Type
Description
data
object
Role object returned by the API.
attributes
object
Attributes of the created role.
created_at
date-time
Creation time of the role.
modified_at
date-time
Time of last role modification.
name [_required_]
string
Name of the role.
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
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "developers"
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Create role with a permission returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles" \
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

                        
```

#####  Create role with a permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create role with a permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create role with a permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create role with a permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create role with a permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create role with a permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a role](https://docs.datadoghq.com/api/latest/roles/#get-a-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#get-a-role-v2)


GET https://api.ap1.datadoghq.com/api/v2/roles/{role_id}https://api.ap2.datadoghq.com/api/v2/roles/{role_id}https://api.datadoghq.eu/api/v2/roles/{role_id}https://api.ddog-gov.com/api/v2/roles/{role_id}https://api.datadoghq.com/api/v2/roles/{role_id}https://api.us3.datadoghq.com/api/v2/roles/{role_id}https://api.us5.datadoghq.com/api/v2/roles/{role_id}
### Overview
Get a role in the organization specified by the role’s `role_id`.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#GetRole-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#GetRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#GetRole-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#GetRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Response containing information about a single role.
Field
Type
Description
data
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
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
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

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Get a role
Copy
```
                  # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a role
```
# Get a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.get_role(ROLE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update a role](https://docs.datadoghq.com/api/latest/roles/#update-a-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#update-a-role-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/roles/{role_id}https://api.ap2.datadoghq.com/api/v2/roles/{role_id}https://api.datadoghq.eu/api/v2/roles/{role_id}https://api.ddog-gov.com/api/v2/roles/{role_id}https://api.datadoghq.com/api/v2/roles/{role_id}https://api.us3.datadoghq.com/api/v2/roles/{role_id}https://api.us5.datadoghq.com/api/v2/roles/{role_id}
### Overview
Edit a role. Can only be used with application keys belonging to administrators. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Field
Type
Description
data [_required_]
object
Data related to the update of a role.
attributes [_required_]
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
Name of the role.
user_count
int32
The user count.
id [_required_]
string
The unique identifier of the role.
relationships
object
Relationships of the role object.
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#UpdateRole-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#UpdateRole-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#UpdateRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#UpdateRole-404-v2)
  * [422](https://docs.datadoghq.com/api/latest/roles/#UpdateRole-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#UpdateRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Response containing information about an updated role.
Field
Type
Description
data
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
Name of the role.
user_count
int32
The user count.
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
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Update a role
Copy
```
                  # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}" \
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

                
```

#####  Update a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete role](https://docs.datadoghq.com/api/latest/roles/#delete-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#delete-role-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/roles/{role_id}https://api.ap2.datadoghq.com/api/v2/roles/{role_id}https://api.datadoghq.eu/api/v2/roles/{role_id}https://api.ddog-gov.com/api/v2/roles/{role_id}https://api.datadoghq.com/api/v2/roles/{role_id}https://api.us3.datadoghq.com/api/v2/roles/{role_id}https://api.us5.datadoghq.com/api/v2/roles/{role_id}
### Overview
Disables a role.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Response
  * [204](https://docs.datadoghq.com/api/latest/roles/#DeleteRole-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#DeleteRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#DeleteRole-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#DeleteRole-429-v2)


OK
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Delete role
Copy
```
                  # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete role
```
# Delete role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
api_instance.delete_role(ROLE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List permissions for a role](https://docs.datadoghq.com/api/latest/roles/#list-permissions-for-a-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#list-permissions-for-a-role-v2)


GET https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.ap2.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.datadoghq.eu/api/v2/roles/{role_id}/permissionshttps://api.ddog-gov.com/api/v2/roles/{role_id}/permissionshttps://api.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.us3.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.us5.datadoghq.com/api/v2/roles/{role_id}/permissions
### Overview
Returns a list of all permissions for a single role.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#ListRolePermissions-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#ListRolePermissions-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#ListRolePermissions-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#ListRolePermissions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  List permissions for a role
Copy
```
                  # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/permissions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List permissions for a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List permissions for a role
```
# List permissions for a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.list_role_permissions(ROLE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List permissions for a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List permissions for a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List permissions for a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List permissions for a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Grant permission to a role](https://docs.datadoghq.com/api/latest/roles/#grant-permission-to-a-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#grant-permission-to-a-role-v2)


POST https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.ap2.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.datadoghq.eu/api/v2/roles/{role_id}/permissionshttps://api.ddog-gov.com/api/v2/roles/{role_id}/permissionshttps://api.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.us3.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.us5.datadoghq.com/api/v2/roles/{role_id}/permissions
### Overview
Adds a permission to a role. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Field
Type
Description
data
object
Relationship to permission object.
id
string
ID of the permission.
type
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
```
{
  "data": {
    "id": "f2a8beb4-91f8-962d-b6d9-60215cda2214",
    "type": "permissions"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#AddPermissionToRole-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#AddPermissionToRole-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#AddPermissionToRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#AddPermissionToRole-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#AddPermissionToRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


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
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Grant permission to a role returns "OK" response
Copy
```
                          # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/permissions" \
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

                        
```

#####  Grant permission to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Grant permission to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Grant permission to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Grant permission to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Grant permission to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Grant permission to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Revoke permission](https://docs.datadoghq.com/api/latest/roles/#revoke-permission)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#revoke-permission-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.ap2.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.datadoghq.eu/api/v2/roles/{role_id}/permissionshttps://api.ddog-gov.com/api/v2/roles/{role_id}/permissionshttps://api.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.us3.datadoghq.com/api/v2/roles/{role_id}/permissionshttps://api.us5.datadoghq.com/api/v2/roles/{role_id}/permissions
### Overview
Removes a permission from a role. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Field
Type
Description
data
object
Relationship to permission object.
id
string
ID of the permission.
type
enum
Permissions resource type. Allowed enum values: `permissions`
default: `permissions`
```
{
  "data": {
    "id": "f2a8beb4-91f8-962d-b6d9-60215cda2214",
    "type": "permissions"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#RemovePermissionFromRole-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#RemovePermissionFromRole-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#RemovePermissionFromRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#RemovePermissionFromRole-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#RemovePermissionFromRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


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
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Revoke permission returns "OK" response
Copy
```
                          # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/permissions" \
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

                        
```

#####  Revoke permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Revoke permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Revoke permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Revoke permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Revoke permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Revoke permission returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get all users of a role](https://docs.datadoghq.com/api/latest/roles/#get-all-users-of-a-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#get-all-users-of-a-role-v2)


GET https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.ap2.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.datadoghq.eu/api/v2/roles/{role_id}/usershttps://api.ddog-gov.com/api/v2/roles/{role_id}/usershttps://api.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.us3.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.us5.datadoghq.com/api/v2/roles/{role_id}/users
### Overview
Gets all users of a role.
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
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
User attribute to order results by. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `email`, `status`.
filter
string
Filter all users by the given string. Defaults to no filtering.
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#ListRoleUsers-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#ListRoleUsers-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#ListRoleUsers-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#ListRoleUsers-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Get all users of a role
Copy
```
                  # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/users" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all users of a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all users of a role
```
# Get all users of a role returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RolesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.list_role_users(ROLE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all users of a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all users of a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get all users of a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get all users of a role
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Add a user to a role](https://docs.datadoghq.com/api/latest/roles/#add-a-user-to-a-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#add-a-user-to-a-role-v2)


POST https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.ap2.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.datadoghq.eu/api/v2/roles/{role_id}/usershttps://api.ddog-gov.com/api/v2/roles/{role_id}/usershttps://api.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.us3.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.us5.datadoghq.com/api/v2/roles/{role_id}/users
### Overview
Adds a user to a role. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Field
Type
Description
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
```
{
  "data": {
    "id": "c1d4eb9e-8bb0-974d-85a5-a7dd9db46bee",
    "type": "users"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#AddUserToRole-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#AddUserToRole-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#AddUserToRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#AddUserToRole-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#AddUserToRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Add a user to a role returns "OK" response
Copy
```
                          # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/users" \
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

                        
```

#####  Add a user to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Add a user to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Add a user to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Add a user to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Add a user to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Add a user to a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Remove a user from a role](https://docs.datadoghq.com/api/latest/roles/#remove-a-user-from-a-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#remove-a-user-from-a-role-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.ap2.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.datadoghq.eu/api/v2/roles/{role_id}/usershttps://api.ddog-gov.com/api/v2/roles/{role_id}/usershttps://api.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.us3.datadoghq.com/api/v2/roles/{role_id}/usershttps://api.us5.datadoghq.com/api/v2/roles/{role_id}/users
### Overview
Removes a user from a role. This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Field
Type
Description
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
```
{
  "data": {
    "id": "c1d4eb9e-8bb0-974d-85a5-a7dd9db46bee",
    "type": "users"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#RemoveUserFromRole-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#RemoveUserFromRole-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#RemoveUserFromRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#RemoveUserFromRole-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#RemoveUserFromRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Remove a user from a role returns "OK" response
Copy
```
                          # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/users" \
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

                        
```

#####  Remove a user from a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Remove a user from a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Remove a user from a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Remove a user from a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Remove a user from a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Remove a user from a role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create a new role by cloning an existing role](https://docs.datadoghq.com/api/latest/roles/#create-a-new-role-by-cloning-an-existing-role)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#create-a-new-role-by-cloning-an-existing-role-v2)


POST https://api.ap1.datadoghq.com/api/v2/roles/{role_id}/clonehttps://api.ap2.datadoghq.com/api/v2/roles/{role_id}/clonehttps://api.datadoghq.eu/api/v2/roles/{role_id}/clonehttps://api.ddog-gov.com/api/v2/roles/{role_id}/clonehttps://api.datadoghq.com/api/v2/roles/{role_id}/clonehttps://api.us3.datadoghq.com/api/v2/roles/{role_id}/clonehttps://api.us5.datadoghq.com/api/v2/roles/{role_id}/clone
### Overview
Clone an existing role This endpoint requires the `user_access_manage` permission.
OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
role_id [_required_]
string
The unique identifier of the role.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Field
Type
Description
data [_required_]
object
Data for the clone role request.
attributes [_required_]
object
Attributes required to create a new role by cloning an existing one.
name [_required_]
string
Name of the new role that is cloned.
type [_required_]
enum
Roles type. Allowed enum values: `roles`
default: `roles`
```
{
  "data": {
    "attributes": {
      "name": "Example-Role clone"
    },
    "type": "roles"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#CloneRole-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/roles/#CloneRole-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/roles/#CloneRole-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/roles/#CloneRole-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/roles/#CloneRole-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#CloneRole-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


Response containing information about a single role.
Field
Type
Description
data
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
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  Create a new role by cloning an existing role returns "OK" response
Copy
```
                          # Path parameters  
export role_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/${role_id}/clone" \
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

                        
```

#####  Create a new role by cloning an existing role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a new role by cloning an existing role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create a new role by cloning an existing role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a new role by cloning an existing role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a new role by cloning an existing role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create a new role by cloning an existing role returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [List role templates](https://docs.datadoghq.com/api/latest/roles/#list-role-templates)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/roles/#list-role-templates-v2)


**Note** : This endpoint may be subject to changes.
GET https://api.ap1.datadoghq.com/api/v2/roles/templateshttps://api.ap2.datadoghq.com/api/v2/roles/templateshttps://api.datadoghq.eu/api/v2/roles/templateshttps://api.ddog-gov.com/api/v2/roles/templateshttps://api.datadoghq.com/api/v2/roles/templateshttps://api.us3.datadoghq.com/api/v2/roles/templateshttps://api.us5.datadoghq.com/api/v2/roles/templates
### Overview
List all role templates
OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#roles) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/roles/#ListRoleTemplates-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/roles/#ListRoleTemplates-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


The definition of `RoleTemplateArray` object.
Field
Type
Description
data [_required_]
[object]
The `RoleTemplateArray` `data`.
attributes
object
The definition of `RoleTemplateDataAttributes` object.
description
string
The `attributes` `description`.
name
string
The `attributes` `name`.
id
string
The `RoleTemplateData` `id`.
type [_required_]
enum
Roles resource type. Allowed enum values: `roles`
default: `roles`
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/roles/)
  * [Example](https://docs.datadoghq.com/api/latest/roles/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/roles/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/roles/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/roles/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/roles/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/roles/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/roles/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/roles/?code-lang=typescript)


#####  List role templates
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/roles/templates" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List role templates
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List role templates
```
# List role templates returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_role_templates".to_sym] = true
end
api_instance = DatadogAPIClient::V2::RolesAPI.new
p api_instance.list_role_templates()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List role templates
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List role templates
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List role templates
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List role templates
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b32158b3-8c4c-4824-ad91-504395903cf4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b0502f15-e333-4ef8-95ec-8555b757071f&pt=Roles&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Froles%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b32158b3-8c4c-4824-ad91-504395903cf4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b0502f15-e333-4ef8-95ec-8555b757071f&pt=Roles&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Froles%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=343fae6d-f6a0-4dbe-a801-aa7f75ba9b1f&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Roles&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Froles%2F&r=&lt=21004&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=996563)
