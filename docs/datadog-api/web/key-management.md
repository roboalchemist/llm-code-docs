# Source: https://docs.datadoghq.com/api/latest/key-management/

# Key Management
Manage your Datadog API and application keys. You need an API key and an application key for a user with the required permissions to interact with these endpoints.
Consult the following pages to view and manage your keys:
  * [API Keys](https://app.datadoghq.com/organization-settings/api-keys)
  * [Application Keys](https://app.datadoghq.com/personal-settings/application-keys)


## [Delete an application key owned by current user](https://docs.datadoghq.com/api/latest/key-management/#delete-an-application-key-owned-by-current-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#delete-an-application-key-owned-by-current-user-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/current_user/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/current_user/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}
### Overview
Delete an application key owned by current user This endpoint requires the `user_app_keys` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the application key.
### Response
  * [204](https://docs.datadoghq.com/api/latest/key-management/#DeleteCurrentUserApplicationKey-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#DeleteCurrentUserApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#DeleteCurrentUserApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#DeleteCurrentUserApplicationKey-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Delete an application key owned by current user
Copy
```
                  # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an application key owned by current user
```
"""
Delete an application key owned by current user returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = environ["APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    api_instance.delete_current_user_application_key(
        app_key_id=APPLICATION_KEY_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an application key owned by current user
```
# Delete an application key owned by current user returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
api_instance.delete_current_user_application_key(APPLICATION_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an application key owned by current user
```
// Delete an application key owned by current user returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "application_key" in the system
	ApplicationKeyDataID := os.Getenv("APPLICATION_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	r, err := api.DeleteCurrentUserApplicationKey(ctx, ApplicationKeyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.DeleteCurrentUserApplicationKey`: %v\n", err)
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

#####  Delete an application key owned by current user
```
// Delete an application key owned by current user returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "application_key" in the system
    String APPLICATION_KEY_DATA_ID = System.getenv("APPLICATION_KEY_DATA_ID");

    try {
      apiInstance.deleteCurrentUserApplicationKey(APPLICATION_KEY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#deleteCurrentUserApplicationKey");
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

#####  Delete an application key owned by current user
```
// Delete an application key owned by current user returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "application_key" in the system
    let application_key_data_id = std::env::var("APPLICATION_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .delete_current_user_application_key(application_key_data_id.clone())
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

#####  Delete an application key owned by current user
```
/**
 * Delete an application key owned by current user returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "application_key" in the system
const APPLICATION_KEY_DATA_ID = process.env.APPLICATION_KEY_DATA_ID as string;

const params: v2.KeyManagementApiDeleteCurrentUserApplicationKeyRequest = {
  appKeyId: APPLICATION_KEY_DATA_ID,
};

apiInstance
  .deleteCurrentUserApplicationKey(params)
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
## [Get all API keys](https://docs.datadoghq.com/api/latest/key-management/#get-all-api-keys)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#get-all-api-keys-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#get-all-api-keys-v2)


GET https://api.ap1.datadoghq.com/api/v1/api_keyhttps://api.ap2.datadoghq.com/api/v1/api_keyhttps://api.datadoghq.eu/api/v1/api_keyhttps://api.ddog-gov.com/api/v1/api_keyhttps://api.datadoghq.com/api/v1/api_keyhttps://api.us3.datadoghq.com/api/v1/api_keyhttps://api.us5.datadoghq.com/api/v1/api_key
### Overview
Get all API keys available for your account. This endpoint requires the `api_keys_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#ListAPIKeys-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#ListAPIKeys-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#ListAPIKeys-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


List of API and application keys available for a given organization.
Field
Type
Description
api_keys
[object]
Array of API keys.
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
```
{
  "api_keys": [
    {
      "created_by": "test_user",
      "key": "1234512345123456abcabc912349abcd",
      "name": "app_key"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get all API keys
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all API keys
```
"""
Get all API keys returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_api_keys()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all API keys
```
# Get all API keys returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.list_api_keys()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all API keys
```
// Get all API keys returns "OK" response

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
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.ListAPIKeys(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.ListAPIKeys`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.ListAPIKeys`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all API keys
```
// Get all API keys returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApiKeyListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ApiKeyListResponse result = apiInstance.listAPIKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#listAPIKeys");
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

#####  Get all API keys
```
// Get all API keys returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.list_api_keys().await;
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

#####  Get all API keys
```
/**
 * Get all API keys returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

apiInstance
  .listAPIKeys()
  .then((data: v1.ApiKeyListResponse) => {
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

GET https://api.ap1.datadoghq.com/api/v2/api_keyshttps://api.ap2.datadoghq.com/api/v2/api_keyshttps://api.datadoghq.eu/api/v2/api_keyshttps://api.ddog-gov.com/api/v2/api_keyshttps://api.datadoghq.com/api/v2/api_keyshttps://api.us3.datadoghq.com/api/v2/api_keyshttps://api.us5.datadoghq.com/api/v2/api_keys
### Overview
List all API keys available for your account. This endpoint requires the `api_keys_read` permission.
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
API key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign.  
Allowed enum values: `created_at, -created_at, last4, -last4, modified_at, -modified_at, name, -name`
filter
string
Filter API keys by the specified string.
filter[created_at][start]
string
Only include API keys created on or after the specified date.
filter[created_at][end]
string
Only include API keys created on or before the specified date.
filter[modified_at][start]
string
Only include API keys modified on or after the specified date.
filter[modified_at][end]
string
Only include API keys modified on or before the specified date.
include
string
Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`.
filter[remote_config_read_enabled]
boolean
Filter API keys by remote config read enabled status.
filter[category]
string
Filter API keys by category.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#ListAPIKeys-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#ListAPIKeys-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#ListAPIKeys-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#ListAPIKeys-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Response for a list of API keys.
Field
Type
Description
data
[object]
Array of API keys.
attributes
object
Attributes of a partial API key.
category
string
The category of the API key.
created_at
string
Creation date of the API key.
date_last_used
date-time
Date the API Key was last used.
last4
string
The last four characters of the API key.
modified_at
string
Date the API key was last modified.
name
string
Name of the API key.
remote_config_read_enabled
boolean
The remote config read enabled status.
id
string
ID of the API key.
relationships
object
Resources related to the API key.
created_by
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
modified_by
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
API Keys resource type. Allowed enum values: `api_keys`
default: `api_keys`
included
[ <oneOf>]
Array of objects related to the API key.
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
Additional information related to api keys response.
max_allowed
int64
Max allowed number of API keys.
page
object
Additional information related to the API keys response.
total_filtered_count
int64
Total filtered application key count.
```
{
  "data": [
    {
      "attributes": {
        "category": "string",
        "created_at": "2020-11-23T10:00:00.000Z",
        "date_last_used": "2020-11-27T10:00:00.000Z",
        "last4": "abcd",
        "modified_at": "2020-11-23T10:00:00.000Z",
        "name": "API Key for submitting metrics",
        "remote_config_read_enabled": false
      },
      "id": "string",
      "relationships": {
        "created_by": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "modified_by": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "users"
          }
        }
      },
      "type": "api_keys"
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
    "max_allowed": "integer",
    "page": {
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get all API keys
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all API keys
```
"""
Get all API keys returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "api_key" in the system
API_KEY_DATA_ATTRIBUTES_NAME = environ["API_KEY_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_api_keys(
        filter=API_KEY_DATA_ATTRIBUTES_NAME,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all API keys
```
# Get all API keys returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "api_key" in the system
API_KEY_DATA_ATTRIBUTES_NAME = ENV["API_KEY_DATA_ATTRIBUTES_NAME"]
opts = {
  filter: API_KEY_DATA_ATTRIBUTES_NAME,
}
p api_instance.list_api_keys(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all API keys
```
// Get all API keys returns "OK" response

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
	// there is a valid "api_key" in the system
	APIKeyDataAttributesName := os.Getenv("API_KEY_DATA_ATTRIBUTES_NAME")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.ListAPIKeys(ctx, *datadogV2.NewListAPIKeysOptionalParameters().WithFilter(APIKeyDataAttributesName))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.ListAPIKeys`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.ListAPIKeys`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all API keys
```
// Get all API keys returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.api.KeyManagementApi.ListAPIKeysOptionalParameters;
import com.datadog.api.client.v2.model.APIKeysResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "api_key" in the system
    String API_KEY_DATA_ATTRIBUTES_NAME = System.getenv("API_KEY_DATA_ATTRIBUTES_NAME");

    try {
      APIKeysResponse result =
          apiInstance.listAPIKeys(
              new ListAPIKeysOptionalParameters().filter(API_KEY_DATA_ATTRIBUTES_NAME));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#listAPIKeys");
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

#####  Get all API keys
```
// Get all API keys returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::api_key_management::ListAPIKeysOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "api_key" in the system
    let api_key_data_attributes_name = std::env::var("API_KEY_DATA_ATTRIBUTES_NAME").unwrap();
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .list_api_keys(
            ListAPIKeysOptionalParams::default().filter(api_key_data_attributes_name.clone()),
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

#####  Get all API keys
```
/**
 * Get all API keys returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "api_key" in the system
const API_KEY_DATA_ATTRIBUTES_NAME = process.env
  .API_KEY_DATA_ATTRIBUTES_NAME as string;

const params: v2.KeyManagementApiListAPIKeysRequest = {
  filter: API_KEY_DATA_ATTRIBUTES_NAME,
};

apiInstance
  .listAPIKeys(params)
  .then((data: v2.APIKeysResponse) => {
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
## [Create an API key](https://docs.datadoghq.com/api/latest/key-management/#create-an-api-key)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#create-an-api-key-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#create-an-api-key-v2)


POST https://api.ap1.datadoghq.com/api/v1/api_keyhttps://api.ap2.datadoghq.com/api/v1/api_keyhttps://api.datadoghq.eu/api/v1/api_keyhttps://api.ddog-gov.com/api/v1/api_keyhttps://api.datadoghq.com/api/v1/api_keyhttps://api.us3.datadoghq.com/api/v1/api_keyhttps://api.us5.datadoghq.com/api/v1/api_key
### Overview
Creates an API key with a given name. This endpoint requires the `api_keys_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Expand All
Field
Type
Description
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
```
{
  "name": "example user"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An API key with its associated metadata.
Field
Type
Description
api_key
object
Datadog API key.
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
```
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Create an API key
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Create an API key
```
"""
Create an API key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.api_key import ApiKey

body = ApiKey(
    name="example user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_api_key(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an API key
```
# Create an API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApiKey.new({
  name: "example user",
})
p api_instance.create_api_key(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an API key
```
// Create an API key returns "OK" response

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
	body := datadogV1.ApiKey{
		Name: datadog.PtrString("example user"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.CreateAPIKey(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.CreateAPIKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.CreateAPIKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an API key
```
// Create an API key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApiKey;
import com.datadog.api.client.v1.model.ApiKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    ApiKey body = new ApiKey().name("example user");

    try {
      ApiKeyResponse result = apiInstance.createAPIKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#createAPIKey");
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

#####  Create an API key
```
// Create an API key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV1::model::ApiKey;

#[tokio::main]
async fn main() {
    let body = ApiKey::new().name("example user".to_string());
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.create_api_key(body).await;
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

#####  Create an API key
```
/**
 * Create an API key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiCreateAPIKeyRequest = {
  body: {
    name: "example user",
  },
};

apiInstance
  .createAPIKey(params)
  .then((data: v1.ApiKeyResponse) => {
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

POST https://api.ap1.datadoghq.com/api/v2/api_keyshttps://api.ap2.datadoghq.com/api/v2/api_keyshttps://api.datadoghq.eu/api/v2/api_keyshttps://api.ddog-gov.com/api/v2/api_keyshttps://api.datadoghq.com/api/v2/api_keyshttps://api.us3.datadoghq.com/api/v2/api_keyshttps://api.us5.datadoghq.com/api/v2/api_keys
### Overview
Create an API key. This endpoint requires the `api_keys_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Field
Type
Description
data [_required_]
object
Object used to create an API key.
attributes [_required_]
object
Attributes used to create an API Key.
category
string
The APIKeyCreateAttributes category.
name [_required_]
string
Name of the API key.
remote_config_read_enabled
boolean
The APIKeyCreateAttributes remote_config_read_enabled.
type [_required_]
enum
API Keys resource type. Allowed enum values: `api_keys`
default: `api_keys`
```
{
  "data": {
    "type": "api_keys",
    "attributes": {
      "name": "Example-Key-Management"
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#CreateAPIKey-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Response for retrieving an API key.
Field
Type
Description
data
object
Datadog API key.
attributes
object
Attributes of a full API key.
category
string
The category of the API key.
created_at
date-time
Creation date of the API key.
date_last_used
date-time
Date the API Key was last used
key
string
The API key.
last4
string
The last four characters of the API key.
modified_at
date-time
Date the API key was last modified.
name
string
Name of the API key.
remote_config_read_enabled
boolean
The remote config read enabled status.
id
string
ID of the API key.
relationships
object
Resources related to the API key.
created_by
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
modified_by
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
API Keys resource type. Allowed enum values: `api_keys`
default: `api_keys`
included
[ <oneOf>]
Array of objects related to the API key.
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
      "category": "string",
      "created_at": "2020-11-23T10:00:00.000Z",
      "date_last_used": "2020-11-27T10:00:00.000Z",
      "key": "string",
      "last4": "abcd",
      "modified_at": "2020-11-23T10:00:00.000Z",
      "name": "API Key for submitting metrics",
      "remote_config_read_enabled": false
    },
    "id": "string",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "users"
        }
      }
    },
    "type": "api_keys"
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Create an API key returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "api_keys",
    "attributes": {
      "name": "Example-Key-Management"
    }
  }
}
EOF  

                        
```

#####  Create an API key returns "Created" response
```
// Create an API key returns "Created" response

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
	body := datadogV2.APIKeyCreateRequest{
		Data: datadogV2.APIKeyCreateData{
			Type: datadogV2.APIKEYSTYPE_API_KEYS,
			Attributes: datadogV2.APIKeyCreateAttributes{
				Name: "Example-Key-Management",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.CreateAPIKey(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.CreateAPIKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.CreateAPIKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an API key returns "Created" response
```
// Create an API key returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.APIKeyCreateAttributes;
import com.datadog.api.client.v2.model.APIKeyCreateData;
import com.datadog.api.client.v2.model.APIKeyCreateRequest;
import com.datadog.api.client.v2.model.APIKeyResponse;
import com.datadog.api.client.v2.model.APIKeysType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    APIKeyCreateRequest body =
        new APIKeyCreateRequest()
            .data(
                new APIKeyCreateData()
                    .type(APIKeysType.API_KEYS)
                    .attributes(new APIKeyCreateAttributes().name("Example-Key-Management")));

    try {
      APIKeyResponse result = apiInstance.createAPIKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#createAPIKey");
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

#####  Create an API key returns "Created" response
```
"""
Create an API key returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.api_key_create_attributes import APIKeyCreateAttributes
from datadog_api_client.v2.model.api_key_create_data import APIKeyCreateData
from datadog_api_client.v2.model.api_key_create_request import APIKeyCreateRequest
from datadog_api_client.v2.model.api_keys_type import APIKeysType

body = APIKeyCreateRequest(
    data=APIKeyCreateData(
        type=APIKeysType.API_KEYS,
        attributes=APIKeyCreateAttributes(
            name="Example-Key-Management",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_api_key(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an API key returns "Created" response
```
# Create an API key returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

body = DatadogAPIClient::V2::APIKeyCreateRequest.new({
  data: DatadogAPIClient::V2::APIKeyCreateData.new({
    type: DatadogAPIClient::V2::APIKeysType::API_KEYS,
    attributes: DatadogAPIClient::V2::APIKeyCreateAttributes.new({
      name: "Example-Key-Management",
    }),
  }),
})
p api_instance.create_api_key(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an API key returns "Created" response
```
// Create an API key returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::model::APIKeyCreateAttributes;
use datadog_api_client::datadogV2::model::APIKeyCreateData;
use datadog_api_client::datadogV2::model::APIKeyCreateRequest;
use datadog_api_client::datadogV2::model::APIKeysType;

#[tokio::main]
async fn main() {
    let body = APIKeyCreateRequest::new(APIKeyCreateData::new(
        APIKeyCreateAttributes::new("Example-Key-Management".to_string()),
        APIKeysType::API_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.create_api_key(body).await;
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

#####  Create an API key returns "Created" response
```
/**
 * Create an API key returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

const params: v2.KeyManagementApiCreateAPIKeyRequest = {
  body: {
    data: {
      type: "api_keys",
      attributes: {
        name: "Example-Key-Management",
      },
    },
  },
};

apiInstance
  .createAPIKey(params)
  .then((data: v2.APIKeyResponse) => {
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
## [Edit an application key owned by current user](https://docs.datadoghq.com/api/latest/key-management/#edit-an-application-key-owned-by-current-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#edit-an-application-key-owned-by-current-user-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/current_user/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/current_user/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}
### Overview
Edit an application key owned by current user. The `key` field is not returned for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires the `user_app_keys` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the application key.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
    "id": "string",
    "type": "application_keys",
    "attributes": {
      "name": "Application Key for managing dashboards-updated"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#UpdateCurrentUserApplicationKey-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#UpdateCurrentUserApplicationKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#UpdateCurrentUserApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#UpdateCurrentUserApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#UpdateCurrentUserApplicationKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Edit an application key owned by current user returns "OK" response
Copy
```
                          # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "string",
    "type": "application_keys",
    "attributes": {
      "name": "Application Key for managing dashboards-updated"
    }
  }
}
EOF  

                        
```

#####  Edit an application key owned by current user returns "OK" response
```
// Edit an application key owned by current user returns "OK" response

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
	// there is a valid "application_key" in the system
	ApplicationKeyDataID := os.Getenv("APPLICATION_KEY_DATA_ID")

	body := datadogV2.ApplicationKeyUpdateRequest{
		Data: datadogV2.ApplicationKeyUpdateData{
			Id:   ApplicationKeyDataID,
			Type: datadogV2.APPLICATIONKEYSTYPE_APPLICATION_KEYS,
			Attributes: datadogV2.ApplicationKeyUpdateAttributes{
				Name: datadog.PtrString("Application Key for managing dashboards-updated"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.UpdateCurrentUserApplicationKey(ctx, ApplicationKeyDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.UpdateCurrentUserApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.UpdateCurrentUserApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit an application key owned by current user returns "OK" response
```
// Edit an application key owned by current user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateAttributes;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateData;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateRequest;
import com.datadog.api.client.v2.model.ApplicationKeysType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "application_key" in the system
    String APPLICATION_KEY_DATA_ATTRIBUTES_NAME =
        System.getenv("APPLICATION_KEY_DATA_ATTRIBUTES_NAME");
    String APPLICATION_KEY_DATA_ID = System.getenv("APPLICATION_KEY_DATA_ID");

    ApplicationKeyUpdateRequest body =
        new ApplicationKeyUpdateRequest()
            .data(
                new ApplicationKeyUpdateData()
                    .id(APPLICATION_KEY_DATA_ID)
                    .type(ApplicationKeysType.APPLICATION_KEYS)
                    .attributes(
                        new ApplicationKeyUpdateAttributes()
                            .name("Application Key for managing dashboards-updated")));

    try {
      ApplicationKeyResponse result =
          apiInstance.updateCurrentUserApplicationKey(APPLICATION_KEY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#updateCurrentUserApplicationKey");
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

#####  Edit an application key owned by current user returns "OK" response
```
"""
Edit an application key owned by current user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.application_key_update_attributes import ApplicationKeyUpdateAttributes
from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData
from datadog_api_client.v2.model.application_key_update_request import ApplicationKeyUpdateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ATTRIBUTES_NAME = environ["APPLICATION_KEY_DATA_ATTRIBUTES_NAME"]
APPLICATION_KEY_DATA_ID = environ["APPLICATION_KEY_DATA_ID"]

body = ApplicationKeyUpdateRequest(
    data=ApplicationKeyUpdateData(
        id=APPLICATION_KEY_DATA_ID,
        type=ApplicationKeysType.APPLICATION_KEYS,
        attributes=ApplicationKeyUpdateAttributes(
            name="Application Key for managing dashboards-updated",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_current_user_application_key(app_key_id=APPLICATION_KEY_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit an application key owned by current user returns "OK" response
```
# Edit an application key owned by current user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ATTRIBUTES_NAME = ENV["APPLICATION_KEY_DATA_ATTRIBUTES_NAME"]
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]

body = DatadogAPIClient::V2::ApplicationKeyUpdateRequest.new({
  data: DatadogAPIClient::V2::ApplicationKeyUpdateData.new({
    id: APPLICATION_KEY_DATA_ID,
    type: DatadogAPIClient::V2::ApplicationKeysType::APPLICATION_KEYS,
    attributes: DatadogAPIClient::V2::ApplicationKeyUpdateAttributes.new({
      name: "Application Key for managing dashboards-updated",
    }),
  }),
})
p api_instance.update_current_user_application_key(APPLICATION_KEY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit an application key owned by current user returns "OK" response
```
// Edit an application key owned by current user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateAttributes;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateData;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateRequest;
use datadog_api_client::datadogV2::model::ApplicationKeysType;

#[tokio::main]
async fn main() {
    // there is a valid "application_key" in the system
    let application_key_data_id = std::env::var("APPLICATION_KEY_DATA_ID").unwrap();
    let body = ApplicationKeyUpdateRequest::new(ApplicationKeyUpdateData::new(
        ApplicationKeyUpdateAttributes::new()
            .name("Application Key for managing dashboards-updated".to_string()),
        application_key_data_id.clone(),
        ApplicationKeysType::APPLICATION_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .update_current_user_application_key(application_key_data_id.clone(), body)
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

#####  Edit an application key owned by current user returns "OK" response
```
/**
 * Edit an application key owned by current user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "application_key" in the system
const APPLICATION_KEY_DATA_ID = process.env.APPLICATION_KEY_DATA_ID as string;

const params: v2.KeyManagementApiUpdateCurrentUserApplicationKeyRequest = {
  body: {
    data: {
      id: APPLICATION_KEY_DATA_ID,
      type: "application_keys",
      attributes: {
        name: "Application Key for managing dashboards-updated",
      },
    },
  },
  appKeyId: APPLICATION_KEY_DATA_ID,
};

apiInstance
  .updateCurrentUserApplicationKey(params)
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
## [Get API key](https://docs.datadoghq.com/api/latest/key-management/#get-api-key)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#get-api-key-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#get-api-key-v2)


GET https://api.ap1.datadoghq.com/api/v1/api_key/{key}https://api.ap2.datadoghq.com/api/v1/api_key/{key}https://api.datadoghq.eu/api/v1/api_key/{key}https://api.ddog-gov.com/api/v1/api_key/{key}https://api.datadoghq.com/api/v1/api_key/{key}https://api.us3.datadoghq.com/api/v1/api_key/{key}https://api.us5.datadoghq.com/api/v1/api_key/{key}
### Overview
Get a given API key. This endpoint requires the `api_keys_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
key [_required_]
string
The specific API key you are working with.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An API key with its associated metadata.
Field
Type
Description
api_key
object
Datadog API key.
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
```
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get API key
Copy
```
                  # Path parameters  
export key="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get API key
```
"""
Get API key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_api_key(
        key="key",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get API key
```
# Get API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.get_api_key("key")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get API key
```
// Get API key returns "OK" response

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
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.GetAPIKey(ctx, "key")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.GetAPIKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.GetAPIKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get API key
```
// Get API key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApiKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ApiKeyResponse result = apiInstance.getAPIKey("key");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#getAPIKey");
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

#####  Get API key
```
// Get API key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.get_api_key("key".to_string()).await;
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

#####  Get API key
```
/**
 * Get API key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiGetAPIKeyRequest = {
  key: "key",
};

apiInstance
  .getAPIKey(params)
  .then((data: v1.ApiKeyResponse) => {
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

GET https://api.ap1.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.ap2.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.datadoghq.eu/api/v2/api_keys/{api_key_id}https://api.ddog-gov.com/api/v2/api_keys/{api_key_id}https://api.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.us3.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.us5.datadoghq.com/api/v2/api_keys/{api_key_id}
### Overview
Get an API key. This endpoint requires the `api_keys_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
api_key_id [_required_]
string
The ID of the API key.
#### Query Strings
Name
Type
Description
include
string
Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#GetAPIKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Response for retrieving an API key.
Field
Type
Description
data
object
Datadog API key.
attributes
object
Attributes of a full API key.
category
string
The category of the API key.
created_at
date-time
Creation date of the API key.
date_last_used
date-time
Date the API Key was last used
key
string
The API key.
last4
string
The last four characters of the API key.
modified_at
date-time
Date the API key was last modified.
name
string
Name of the API key.
remote_config_read_enabled
boolean
The remote config read enabled status.
id
string
ID of the API key.
relationships
object
Resources related to the API key.
created_by
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
modified_by
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
API Keys resource type. Allowed enum values: `api_keys`
default: `api_keys`
included
[ <oneOf>]
Array of objects related to the API key.
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
      "category": "string",
      "created_at": "2020-11-23T10:00:00.000Z",
      "date_last_used": "2020-11-27T10:00:00.000Z",
      "key": "string",
      "last4": "abcd",
      "modified_at": "2020-11-23T10:00:00.000Z",
      "name": "API Key for submitting metrics",
      "remote_config_read_enabled": false
    },
    "id": "string",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "users"
        }
      }
    },
    "type": "api_keys"
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get API key
Copy
```
                  # Path parameters  
export api_key_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys/${api_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get API key
```
"""
Get API key returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "api_key" in the system
API_KEY_DATA_ID = environ["API_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_api_key(
        api_key_id=API_KEY_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get API key
```
# Get API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "api_key" in the system
API_KEY_DATA_ID = ENV["API_KEY_DATA_ID"]
p api_instance.get_api_key(API_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get API key
```
// Get API key returns "OK" response

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
	// there is a valid "api_key" in the system
	APIKeyDataID := os.Getenv("API_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.GetAPIKey(ctx, APIKeyDataID, *datadogV2.NewGetAPIKeyOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.GetAPIKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.GetAPIKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get API key
```
// Get API key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.APIKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "api_key" in the system
    String API_KEY_DATA_ID = System.getenv("API_KEY_DATA_ID");

    try {
      APIKeyResponse result = apiInstance.getAPIKey(API_KEY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#getAPIKey");
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

#####  Get API key
```
// Get API key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::GetAPIKeyOptionalParams;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "api_key" in the system
    let api_key_data_id = std::env::var("API_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .get_api_key(api_key_data_id.clone(), GetAPIKeyOptionalParams::default())
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

#####  Get API key
```
/**
 * Get API key returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "api_key" in the system
const API_KEY_DATA_ID = process.env.API_KEY_DATA_ID as string;

const params: v2.KeyManagementApiGetAPIKeyRequest = {
  apiKeyId: API_KEY_DATA_ID,
};

apiInstance
  .getAPIKey(params)
  .then((data: v2.APIKeyResponse) => {
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
## [Get one application key owned by current user](https://docs.datadoghq.com/api/latest/key-management/#get-one-application-key-owned-by-current-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#get-one-application-key-owned-by-current-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/current_user/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/current_user/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}
### Overview
Get an application key owned by current user. The `key` field is not returned for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires the `user_app_keys` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the application key.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#GetCurrentUserApplicationKey-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#GetCurrentUserApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#GetCurrentUserApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#GetCurrentUserApplicationKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get one application key owned by current user
Copy
```
                  # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get one application key owned by current user
```
"""
Get one application key owned by current user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = environ["APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_current_user_application_key(
        app_key_id=APPLICATION_KEY_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get one application key owned by current user
```
# Get one application key owned by current user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
p api_instance.get_current_user_application_key(APPLICATION_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get one application key owned by current user
```
// Get one application key owned by current user returns "OK" response

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
	// there is a valid "application_key" in the system
	ApplicationKeyDataID := os.Getenv("APPLICATION_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.GetCurrentUserApplicationKey(ctx, ApplicationKeyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.GetCurrentUserApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.GetCurrentUserApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get one application key owned by current user
```
// Get one application key owned by current user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "application_key" in the system
    String APPLICATION_KEY_DATA_ID = System.getenv("APPLICATION_KEY_DATA_ID");

    try {
      ApplicationKeyResponse result =
          apiInstance.getCurrentUserApplicationKey(APPLICATION_KEY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#getCurrentUserApplicationKey");
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

#####  Get one application key owned by current user
```
// Get one application key owned by current user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "application_key" in the system
    let application_key_data_id = std::env::var("APPLICATION_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .get_current_user_application_key(application_key_data_id.clone())
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

#####  Get one application key owned by current user
```
/**
 * Get one application key owned by current user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "application_key" in the system
const APPLICATION_KEY_DATA_ID = process.env.APPLICATION_KEY_DATA_ID as string;

const params: v2.KeyManagementApiGetCurrentUserApplicationKeyRequest = {
  appKeyId: APPLICATION_KEY_DATA_ID,
};

apiInstance
  .getCurrentUserApplicationKey(params)
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
## [Create an application key for current user](https://docs.datadoghq.com/api/latest/key-management/#create-an-application-key-for-current-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#create-an-application-key-for-current-user-v2)


POST https://api.ap1.datadoghq.com/api/v2/current_user/application_keyshttps://api.ap2.datadoghq.com/api/v2/current_user/application_keyshttps://api.datadoghq.eu/api/v2/current_user/application_keyshttps://api.ddog-gov.com/api/v2/current_user/application_keyshttps://api.datadoghq.com/api/v2/current_user/application_keyshttps://api.us3.datadoghq.com/api/v2/current_user/application_keyshttps://api.us5.datadoghq.com/api/v2/current_user/application_keys
### Overview
Create an application key for current user This endpoint requires the `user_app_keys` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
#####  Create an Application key with scopes for current user returns "Created" response
```
{
  "data": {
    "type": "application_keys",
    "attributes": {
      "name": "Example-Key-Management",
      "scopes": [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share"
      ]
    }
  }
}
```

Copy
#####  Create an application key for current user returns "Created" response
```
{
  "data": {
    "type": "application_keys",
    "attributes": {
      "name": "Example-Key-Management"
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/key-management/#CreateCurrentUserApplicationKey-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#CreateCurrentUserApplicationKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#CreateCurrentUserApplicationKey-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#CreateCurrentUserApplicationKey-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Create an Application key with scopes for current user returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "application_keys",
    "attributes": {
      "name": "Example-Key-Management",
      "scopes": [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share"
      ]
    }
  }
}
EOF  

                        
```

#####  Create an application key for current user returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "application_keys",
    "attributes": {
      "name": "Example-Key-Management"
    }
  }
}
EOF  

                        
```

#####  Create an Application key with scopes for current user returns "Created" response 
```
// Create an Application key with scopes for current user returns "Created" response

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
	body := datadogV2.ApplicationKeyCreateRequest{
		Data: datadogV2.ApplicationKeyCreateData{
			Type: datadogV2.APPLICATIONKEYSTYPE_APPLICATION_KEYS,
			Attributes: datadogV2.ApplicationKeyCreateAttributes{
				Name: "Example-Key-Management",
				Scopes: *datadog.NewNullableList(&[]string{
					"dashboards_read",
					"dashboards_write",
					"dashboards_public_share",
				}),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.CreateCurrentUserApplicationKey(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.CreateCurrentUserApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.CreateCurrentUserApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#####  Create an application key for current user returns "Created" response 
```
// Create an application key for current user returns "Created" response

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
	body := datadogV2.ApplicationKeyCreateRequest{
		Data: datadogV2.ApplicationKeyCreateData{
			Type: datadogV2.APPLICATIONKEYSTYPE_APPLICATION_KEYS,
			Attributes: datadogV2.ApplicationKeyCreateAttributes{
				Name: "Example-Key-Management",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.CreateCurrentUserApplicationKey(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.CreateCurrentUserApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.CreateCurrentUserApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an Application key with scopes for current user returns "Created" response 
```
// Create an Application key with scopes for current user returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ApplicationKeyCreateAttributes;
import com.datadog.api.client.v2.model.ApplicationKeyCreateData;
import com.datadog.api.client.v2.model.ApplicationKeyCreateRequest;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;
import com.datadog.api.client.v2.model.ApplicationKeysType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    ApplicationKeyCreateRequest body =
        new ApplicationKeyCreateRequest()
            .data(
                new ApplicationKeyCreateData()
                    .type(ApplicationKeysType.APPLICATION_KEYS)
                    .attributes(
                        new ApplicationKeyCreateAttributes()
                            .name("Example-Key-Management")
                            .scopes(
                                Arrays.asList(
                                    "dashboards_read",
                                    "dashboards_write",
                                    "dashboards_public_share"))));

    try {
      ApplicationKeyResponse result = apiInstance.createCurrentUserApplicationKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#createCurrentUserApplicationKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create an application key for current user returns "Created" response 
```
// Create an application key for current user returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ApplicationKeyCreateAttributes;
import com.datadog.api.client.v2.model.ApplicationKeyCreateData;
import com.datadog.api.client.v2.model.ApplicationKeyCreateRequest;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;
import com.datadog.api.client.v2.model.ApplicationKeysType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    ApplicationKeyCreateRequest body =
        new ApplicationKeyCreateRequest()
            .data(
                new ApplicationKeyCreateData()
                    .type(ApplicationKeysType.APPLICATION_KEYS)
                    .attributes(
                        new ApplicationKeyCreateAttributes().name("Example-Key-Management")));

    try {
      ApplicationKeyResponse result = apiInstance.createCurrentUserApplicationKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#createCurrentUserApplicationKey");
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

#####  Create an Application key with scopes for current user returns "Created" response 
```
"""
Create an Application key with scopes for current user returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

body = ApplicationKeyCreateRequest(
    data=ApplicationKeyCreateData(
        type=ApplicationKeysType.APPLICATION_KEYS,
        attributes=ApplicationKeyCreateAttributes(
            name="Example-Key-Management",
            scopes=[
                "dashboards_read",
                "dashboards_write",
                "dashboards_public_share",
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_current_user_application_key(body=body)

    print(response)

```

Copy
#####  Create an application key for current user returns "Created" response 
```
"""
Create an application key for current user returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

body = ApplicationKeyCreateRequest(
    data=ApplicationKeyCreateData(
        type=ApplicationKeysType.APPLICATION_KEYS,
        attributes=ApplicationKeyCreateAttributes(
            name="Example-Key-Management",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_current_user_application_key(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an Application key with scopes for current user returns "Created" response 
```
# Create an Application key with scopes for current user returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

body = DatadogAPIClient::V2::ApplicationKeyCreateRequest.new({
  data: DatadogAPIClient::V2::ApplicationKeyCreateData.new({
    type: DatadogAPIClient::V2::ApplicationKeysType::APPLICATION_KEYS,
    attributes: DatadogAPIClient::V2::ApplicationKeyCreateAttributes.new({
      name: "Example-Key-Management",
      scopes: [
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share",
      ],
    }),
  }),
})
p api_instance.create_current_user_application_key(body)

```

Copy
#####  Create an application key for current user returns "Created" response 
```
# Create an application key for current user returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

body = DatadogAPIClient::V2::ApplicationKeyCreateRequest.new({
  data: DatadogAPIClient::V2::ApplicationKeyCreateData.new({
    type: DatadogAPIClient::V2::ApplicationKeysType::APPLICATION_KEYS,
    attributes: DatadogAPIClient::V2::ApplicationKeyCreateAttributes.new({
      name: "Example-Key-Management",
    }),
  }),
})
p api_instance.create_current_user_application_key(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an Application key with scopes for current user returns "Created" response 
```
// Create an Application key with scopes for current user returns "Created"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateAttributes;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateData;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateRequest;
use datadog_api_client::datadogV2::model::ApplicationKeysType;

#[tokio::main]
async fn main() {
    let body = ApplicationKeyCreateRequest::new(ApplicationKeyCreateData::new(
        ApplicationKeyCreateAttributes::new("Example-Key-Management".to_string()).scopes(Some(
            vec![
                "dashboards_read".to_string(),
                "dashboards_write".to_string(),
                "dashboards_public_share".to_string(),
            ],
        )),
        ApplicationKeysType::APPLICATION_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.create_current_user_application_key(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create an application key for current user returns "Created" response 
```
// Create an application key for current user returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateAttributes;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateData;
use datadog_api_client::datadogV2::model::ApplicationKeyCreateRequest;
use datadog_api_client::datadogV2::model::ApplicationKeysType;

#[tokio::main]
async fn main() {
    let body = ApplicationKeyCreateRequest::new(ApplicationKeyCreateData::new(
        ApplicationKeyCreateAttributes::new("Example-Key-Management".to_string()),
        ApplicationKeysType::APPLICATION_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.create_current_user_application_key(body).await;
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

#####  Create an Application key with scopes for current user returns "Created" response 
```
/**
 * Create an Application key with scopes for current user returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

const params: v2.KeyManagementApiCreateCurrentUserApplicationKeyRequest = {
  body: {
    data: {
      type: "application_keys",
      attributes: {
        name: "Example-Key-Management",
        scopes: [
          "dashboards_read",
          "dashboards_write",
          "dashboards_public_share",
        ],
      },
    },
  },
};

apiInstance
  .createCurrentUserApplicationKey(params)
  .then((data: v2.ApplicationKeyResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create an application key for current user returns "Created" response 
```
/**
 * Create an application key for current user returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

const params: v2.KeyManagementApiCreateCurrentUserApplicationKeyRequest = {
  body: {
    data: {
      type: "application_keys",
      attributes: {
        name: "Example-Key-Management",
      },
    },
  },
};

apiInstance
  .createCurrentUserApplicationKey(params)
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
## [Edit an API key](https://docs.datadoghq.com/api/latest/key-management/#edit-an-api-key)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#edit-an-api-key-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#edit-an-api-key-v2)


PUT https://api.ap1.datadoghq.com/api/v1/api_key/{key}https://api.ap2.datadoghq.com/api/v1/api_key/{key}https://api.datadoghq.eu/api/v1/api_key/{key}https://api.ddog-gov.com/api/v1/api_key/{key}https://api.datadoghq.com/api/v1/api_key/{key}https://api.us3.datadoghq.com/api/v1/api_key/{key}https://api.us5.datadoghq.com/api/v1/api_key/{key}
### Overview
Edit an API key name. This endpoint requires the `api_keys_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
key [_required_]
string
The specific API key you are working with.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Expand All
Field
Type
Description
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
```
{
  "name": "example user"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An API key with its associated metadata.
Field
Type
Description
api_key
object
Datadog API key.
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
```
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Edit an API key
Copy
```
                  # Path parameters  
export key="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key/${key}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Edit an API key
```
"""
Edit an API key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.api_key import ApiKey

body = ApiKey(
    name="example user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_api_key(key="key", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit an API key
```
# Edit an API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApiKey.new({
  name: "example user",
})
p api_instance.update_api_key("key", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit an API key
```
// Edit an API key returns "OK" response

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
	body := datadogV1.ApiKey{
		Name: datadog.PtrString("example user"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.UpdateAPIKey(ctx, "key", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.UpdateAPIKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.UpdateAPIKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit an API key
```
// Edit an API key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApiKey;
import com.datadog.api.client.v1.model.ApiKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    ApiKey body = new ApiKey().name("example user");

    try {
      ApiKeyResponse result = apiInstance.updateAPIKey("key", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#updateAPIKey");
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

#####  Edit an API key
```
// Edit an API key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV1::model::ApiKey;

#[tokio::main]
async fn main() {
    let body = ApiKey::new().name("example user".to_string());
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.update_api_key("key".to_string(), body).await;
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

#####  Edit an API key
```
/**
 * Edit an API key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiUpdateAPIKeyRequest = {
  body: {
    name: "example user",
  },
  key: "key",
};

apiInstance
  .updateAPIKey(params)
  .then((data: v1.ApiKeyResponse) => {
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

PATCH https://api.ap1.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.ap2.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.datadoghq.eu/api/v2/api_keys/{api_key_id}https://api.ddog-gov.com/api/v2/api_keys/{api_key_id}https://api.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.us3.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.us5.datadoghq.com/api/v2/api_keys/{api_key_id}
### Overview
Update an API key. This endpoint requires the `api_keys_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
api_key_id [_required_]
string
The ID of the API key.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Field
Type
Description
data [_required_]
object
Object used to update an API key.
attributes [_required_]
object
Attributes used to update an API Key.
category
string
The APIKeyUpdateAttributes category.
name [_required_]
string
Name of the API key.
remote_config_read_enabled
boolean
The APIKeyUpdateAttributes remote_config_read_enabled.
id [_required_]
string
ID of the API key.
type [_required_]
enum
API Keys resource type. Allowed enum values: `api_keys`
default: `api_keys`
```
{
  "data": {
    "type": "api_keys",
    "id": "string",
    "attributes": {
      "name": "Example-Key-Management"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#UpdateAPIKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Response for retrieving an API key.
Field
Type
Description
data
object
Datadog API key.
attributes
object
Attributes of a full API key.
category
string
The category of the API key.
created_at
date-time
Creation date of the API key.
date_last_used
date-time
Date the API Key was last used
key
string
The API key.
last4
string
The last four characters of the API key.
modified_at
date-time
Date the API key was last modified.
name
string
Name of the API key.
remote_config_read_enabled
boolean
The remote config read enabled status.
id
string
ID of the API key.
relationships
object
Resources related to the API key.
created_by
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
modified_by
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
API Keys resource type. Allowed enum values: `api_keys`
default: `api_keys`
included
[ <oneOf>]
Array of objects related to the API key.
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
      "category": "string",
      "created_at": "2020-11-23T10:00:00.000Z",
      "date_last_used": "2020-11-27T10:00:00.000Z",
      "key": "string",
      "last4": "abcd",
      "modified_at": "2020-11-23T10:00:00.000Z",
      "name": "API Key for submitting metrics",
      "remote_config_read_enabled": false
    },
    "id": "string",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "users"
        }
      }
    },
    "type": "api_keys"
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Edit an API key returns "OK" response
Copy
```
                          # Path parameters  
export api_key_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys/${api_key_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "api_keys",
    "id": "string",
    "attributes": {
      "name": "Example-Key-Management"
    }
  }
}
EOF  

                        
```

#####  Edit an API key returns "OK" response
```
// Edit an API key returns "OK" response

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
	// there is a valid "api_key" in the system
	APIKeyDataID := os.Getenv("API_KEY_DATA_ID")

	body := datadogV2.APIKeyUpdateRequest{
		Data: datadogV2.APIKeyUpdateData{
			Type: datadogV2.APIKEYSTYPE_API_KEYS,
			Id:   APIKeyDataID,
			Attributes: datadogV2.APIKeyUpdateAttributes{
				Name: "Example-Key-Management",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.UpdateAPIKey(ctx, APIKeyDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.UpdateAPIKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.UpdateAPIKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit an API key returns "OK" response
```
// Edit an API key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.APIKeyResponse;
import com.datadog.api.client.v2.model.APIKeyUpdateAttributes;
import com.datadog.api.client.v2.model.APIKeyUpdateData;
import com.datadog.api.client.v2.model.APIKeyUpdateRequest;
import com.datadog.api.client.v2.model.APIKeysType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "api_key" in the system
    String API_KEY_DATA_ID = System.getenv("API_KEY_DATA_ID");

    APIKeyUpdateRequest body =
        new APIKeyUpdateRequest()
            .data(
                new APIKeyUpdateData()
                    .type(APIKeysType.API_KEYS)
                    .id(API_KEY_DATA_ID)
                    .attributes(new APIKeyUpdateAttributes().name("Example-Key-Management")));

    try {
      APIKeyResponse result = apiInstance.updateAPIKey(API_KEY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#updateAPIKey");
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

#####  Edit an API key returns "OK" response
```
"""
Edit an API key returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.api_key_update_attributes import APIKeyUpdateAttributes
from datadog_api_client.v2.model.api_key_update_data import APIKeyUpdateData
from datadog_api_client.v2.model.api_key_update_request import APIKeyUpdateRequest
from datadog_api_client.v2.model.api_keys_type import APIKeysType

# there is a valid "api_key" in the system
API_KEY_DATA_ID = environ["API_KEY_DATA_ID"]

body = APIKeyUpdateRequest(
    data=APIKeyUpdateData(
        type=APIKeysType.API_KEYS,
        id=API_KEY_DATA_ID,
        attributes=APIKeyUpdateAttributes(
            name="Example-Key-Management",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_api_key(api_key_id=API_KEY_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit an API key returns "OK" response
```
# Edit an API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "api_key" in the system
API_KEY_DATA_ID = ENV["API_KEY_DATA_ID"]

body = DatadogAPIClient::V2::APIKeyUpdateRequest.new({
  data: DatadogAPIClient::V2::APIKeyUpdateData.new({
    type: DatadogAPIClient::V2::APIKeysType::API_KEYS,
    id: API_KEY_DATA_ID,
    attributes: DatadogAPIClient::V2::APIKeyUpdateAttributes.new({
      name: "Example-Key-Management",
    }),
  }),
})
p api_instance.update_api_key(API_KEY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit an API key returns "OK" response
```
// Edit an API key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::model::APIKeyUpdateAttributes;
use datadog_api_client::datadogV2::model::APIKeyUpdateData;
use datadog_api_client::datadogV2::model::APIKeyUpdateRequest;
use datadog_api_client::datadogV2::model::APIKeysType;

#[tokio::main]
async fn main() {
    // there is a valid "api_key" in the system
    let api_key_data_id = std::env::var("API_KEY_DATA_ID").unwrap();
    let body = APIKeyUpdateRequest::new(APIKeyUpdateData::new(
        APIKeyUpdateAttributes::new("Example-Key-Management".to_string()),
        api_key_data_id.clone(),
        APIKeysType::API_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.update_api_key(api_key_data_id.clone(), body).await;
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

#####  Edit an API key returns "OK" response
```
/**
 * Edit an API key returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "api_key" in the system
const API_KEY_DATA_ID = process.env.API_KEY_DATA_ID as string;

const params: v2.KeyManagementApiUpdateAPIKeyRequest = {
  body: {
    data: {
      type: "api_keys",
      id: API_KEY_DATA_ID,
      attributes: {
        name: "Example-Key-Management",
      },
    },
  },
  apiKeyId: API_KEY_DATA_ID,
};

apiInstance
  .updateAPIKey(params)
  .then((data: v2.APIKeyResponse) => {
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
## [Delete an API key](https://docs.datadoghq.com/api/latest/key-management/#delete-an-api-key)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#delete-an-api-key-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#delete-an-api-key-v2)


DELETE https://api.ap1.datadoghq.com/api/v1/api_key/{key}https://api.ap2.datadoghq.com/api/v1/api_key/{key}https://api.datadoghq.eu/api/v1/api_key/{key}https://api.ddog-gov.com/api/v1/api_key/{key}https://api.datadoghq.com/api/v1/api_key/{key}https://api.us3.datadoghq.com/api/v1/api_key/{key}https://api.us5.datadoghq.com/api/v1/api_key/{key}
### Overview
Delete a given API key. This endpoint requires the `api_keys_delete` permission.
### Arguments
#### Path Parameters
Name
Type
Description
key [_required_]
string
The specific API key you are working with.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An API key with its associated metadata.
Field
Type
Description
api_key
object
Datadog API key.
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
```
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Delete an API key
Copy
```
                  # Path parameters  
export key="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an API key
```
"""
Delete an API key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.delete_api_key(
        key="key",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an API key
```
# Delete an API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.delete_api_key("key")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an API key
```
// Delete an API key returns "OK" response

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
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.DeleteAPIKey(ctx, "key")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.DeleteAPIKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.DeleteAPIKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an API key
```
// Delete an API key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApiKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ApiKeyResponse result = apiInstance.deleteAPIKey("key");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#deleteAPIKey");
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

#####  Delete an API key
```
// Delete an API key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.delete_api_key("key".to_string()).await;
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

#####  Delete an API key
```
/**
 * Delete an API key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiDeleteAPIKeyRequest = {
  key: "key",
};

apiInstance
  .deleteAPIKey(params)
  .then((data: v1.ApiKeyResponse) => {
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

DELETE https://api.ap1.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.ap2.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.datadoghq.eu/api/v2/api_keys/{api_key_id}https://api.ddog-gov.com/api/v2/api_keys/{api_key_id}https://api.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.us3.datadoghq.com/api/v2/api_keys/{api_key_id}https://api.us5.datadoghq.com/api/v2/api_keys/{api_key_id}
### Overview
Delete an API key. This endpoint requires the `api_keys_delete` permission.
### Arguments
#### Path Parameters
Name
Type
Description
api_key_id [_required_]
string
The ID of the API key.
### Response
  * [204](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#DeleteAPIKey-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Delete an API key
Copy
```
                  # Path parameters  
export api_key_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys/${api_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an API key
```
"""
Delete an API key returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "api_key" in the system
API_KEY_DATA_ID = environ["API_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    api_instance.delete_api_key(
        api_key_id=API_KEY_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an API key
```
# Delete an API key returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "api_key" in the system
API_KEY_DATA_ID = ENV["API_KEY_DATA_ID"]
api_instance.delete_api_key(API_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an API key
```
// Delete an API key returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "api_key" in the system
	APIKeyDataID := os.Getenv("API_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	r, err := api.DeleteAPIKey(ctx, APIKeyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.DeleteAPIKey`: %v\n", err)
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

#####  Delete an API key
```
// Delete an API key returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "api_key" in the system
    String API_KEY_DATA_ID = System.getenv("API_KEY_DATA_ID");

    try {
      apiInstance.deleteAPIKey(API_KEY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#deleteAPIKey");
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

#####  Delete an API key
```
// Delete an API key returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "api_key" in the system
    let api_key_data_id = std::env::var("API_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.delete_api_key(api_key_data_id.clone()).await;
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

#####  Delete an API key
```
/**
 * Delete an API key returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "api_key" in the system
const API_KEY_DATA_ID = process.env.API_KEY_DATA_ID as string;

const params: v2.KeyManagementApiDeleteAPIKeyRequest = {
  apiKeyId: API_KEY_DATA_ID,
};

apiInstance
  .deleteAPIKey(params)
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
## [Get all application keys owned by current user](https://docs.datadoghq.com/api/latest/key-management/#get-all-application-keys-owned-by-current-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#get-all-application-keys-owned-by-current-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/current_user/application_keyshttps://api.ap2.datadoghq.com/api/v2/current_user/application_keyshttps://api.datadoghq.eu/api/v2/current_user/application_keyshttps://api.ddog-gov.com/api/v2/current_user/application_keyshttps://api.datadoghq.com/api/v2/current_user/application_keyshttps://api.us3.datadoghq.com/api/v2/current_user/application_keyshttps://api.us5.datadoghq.com/api/v2/current_user/application_keys
### Overview
List all application keys available for current user This endpoint requires the `user_app_keys` permission.
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
include
string
Resource path for related resources to include in the response. Only `owned_by` is supported.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#ListCurrentUserApplicationKeys-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#ListCurrentUserApplicationKeys-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#ListCurrentUserApplicationKeys-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#ListCurrentUserApplicationKeys-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#ListCurrentUserApplicationKeys-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get all application keys owned by current user
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all application keys owned by current user
```
"""
Get all application keys owned by current user returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_current_user_application_keys()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all application keys owned by current user
```
# Get all application keys owned by current user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new
p api_instance.list_current_user_application_keys()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all application keys owned by current user
```
// Get all application keys owned by current user returns "OK" response

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
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.ListCurrentUserApplicationKeys(ctx, *datadogV2.NewListCurrentUserApplicationKeysOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.ListCurrentUserApplicationKeys`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.ListCurrentUserApplicationKeys`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all application keys owned by current user
```
// Get all application keys owned by current user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ListApplicationKeysResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ListApplicationKeysResponse result = apiInstance.listCurrentUserApplicationKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#listCurrentUserApplicationKeys");
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

#####  Get all application keys owned by current user
```
// Get all application keys owned by current user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::api_key_management::ListCurrentUserApplicationKeysOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .list_current_user_application_keys(ListCurrentUserApplicationKeysOptionalParams::default())
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

#####  Get all application keys owned by current user
```
/**
 * Get all application keys owned by current user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

apiInstance
  .listCurrentUserApplicationKeys()
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
## [Get all application keys](https://docs.datadoghq.com/api/latest/key-management/#get-all-application-keys)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#get-all-application-keys-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#get-all-application-keys-v2)


GET https://api.ap1.datadoghq.com/api/v1/application_keyhttps://api.ap2.datadoghq.com/api/v1/application_keyhttps://api.datadoghq.eu/api/v1/application_keyhttps://api.ddog-gov.com/api/v1/application_keyhttps://api.datadoghq.com/api/v1/application_keyhttps://api.us3.datadoghq.com/api/v1/application_keyhttps://api.us5.datadoghq.com/api/v1/application_key
### Overview
Get all application keys available for your Datadog account. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
* `org_app_keys_read`
* `user_app_keys`
  

### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An application key response.
Field
Type
Description
application_keys
[object]
Array of application keys.
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
```
{
  "application_keys": [
    {
      "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
      "name": "app_key",
      "owner": "test_user"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get all application keys
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all application keys
```
"""
Get all application keys returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_application_keys()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all application keys
```
# Get all application keys returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.list_application_keys()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all application keys
```
// Get all application keys returns "OK" response

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
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.ListApplicationKeys(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.ListApplicationKeys`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.ListApplicationKeys`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all application keys
```
// Get all application keys returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApplicationKeyListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ApplicationKeyListResponse result = apiInstance.listApplicationKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#listApplicationKeys");
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

#####  Get all application keys
```
// Get all application keys returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.list_application_keys().await;
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

#####  Get all application keys
```
/**
 * Get all application keys returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

apiInstance
  .listApplicationKeys()
  .then((data: v1.ApplicationKeyListResponse) => {
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

GET https://api.ap1.datadoghq.com/api/v2/application_keyshttps://api.ap2.datadoghq.com/api/v2/application_keyshttps://api.datadoghq.eu/api/v2/application_keyshttps://api.ddog-gov.com/api/v2/application_keyshttps://api.datadoghq.com/api/v2/application_keyshttps://api.us3.datadoghq.com/api/v2/application_keyshttps://api.us5.datadoghq.com/api/v2/application_keys
### Overview
List all application keys available for your org This endpoint requires the `org_app_keys_read` permission.
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
include
string
Resource path for related resources to include in the response. Only `owned_by` is supported.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#ListApplicationKeys-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get all application keys
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all application keys
```
"""
Get all application keys returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_application_keys()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all application keys
```
# Get all application keys returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new
p api_instance.list_application_keys()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all application keys
```
// Get all application keys returns "OK" response

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
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.ListApplicationKeys(ctx, *datadogV2.NewListApplicationKeysOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.ListApplicationKeys`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.ListApplicationKeys`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all application keys
```
// Get all application keys returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ListApplicationKeysResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ListApplicationKeysResponse result = apiInstance.listApplicationKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#listApplicationKeys");
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

#####  Get all application keys
```
// Get all application keys returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::api_key_management::ListApplicationKeysOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .list_application_keys(ListApplicationKeysOptionalParams::default())
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

#####  Get all application keys
```
/**
 * Get all application keys returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

apiInstance
  .listApplicationKeys()
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
## [Create an application key](https://docs.datadoghq.com/api/latest/key-management/#create-an-application-key)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/key-management/#create-an-application-key-v1)


POST https://api.ap1.datadoghq.com/api/v1/application_keyhttps://api.ap2.datadoghq.com/api/v1/application_keyhttps://api.datadoghq.eu/api/v1/application_keyhttps://api.ddog-gov.com/api/v1/application_keyhttps://api.datadoghq.com/api/v1/application_keyhttps://api.us3.datadoghq.com/api/v1/application_keyhttps://api.us5.datadoghq.com/api/v1/application_key
### Overview
Create an application key with a given name. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires the `user_app_keys` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Expand All
Field
Type
Description
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
```
{
  "name": "example user"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#CreateApplicationKey-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#CreateApplicationKey-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#CreateApplicationKey-403-v1)
  * [409](https://docs.datadoghq.com/api/latest/key-management/#CreateApplicationKey-409-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#CreateApplicationKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An application key response.
Field
Type
Description
application_key
object
An application key with its associated metadata.
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
```
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Create an application key
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Create an application key
```
"""
Create an application key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.application_key import ApplicationKey

body = ApplicationKey(
    name="example user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_application_key(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an application key
```
# Create an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApplicationKey.new({
  name: "example user",
})
p api_instance.create_application_key(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an application key
```
// Create an application key returns "OK" response

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
	body := datadogV1.ApplicationKey{
		Name: datadog.PtrString("example user"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.CreateApplicationKey(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.CreateApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.CreateApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an application key
```
// Create an application key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApplicationKey;
import com.datadog.api.client.v1.model.ApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    ApplicationKey body = new ApplicationKey().name("example user");

    try {
      ApplicationKeyResponse result = apiInstance.createApplicationKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#createApplicationKey");
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

#####  Create an application key
```
// Create an application key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV1::model::ApplicationKey;

#[tokio::main]
async fn main() {
    let body = ApplicationKey::new().name("example user".to_string());
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.create_application_key(body).await;
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

#####  Create an application key
```
/**
 * Create an application key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiCreateApplicationKeyRequest = {
  body: {
    name: "example user",
  },
};

apiInstance
  .createApplicationKey(params)
  .then((data: v1.ApplicationKeyResponse) => {
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
## [Get an application key](https://docs.datadoghq.com/api/latest/key-management/#get-an-application-key)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#get-an-application-key-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#get-an-application-key-v2)


GET https://api.ap1.datadoghq.com/api/v1/application_key/{key}https://api.ap2.datadoghq.com/api/v1/application_key/{key}https://api.datadoghq.eu/api/v1/application_key/{key}https://api.ddog-gov.com/api/v1/application_key/{key}https://api.datadoghq.com/api/v1/application_key/{key}https://api.us3.datadoghq.com/api/v1/application_key/{key}https://api.us5.datadoghq.com/api/v1/application_key/{key}
### Overview
Get a given application key. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
* `org_app_keys_read`
* `user_app_keys`
  

### Arguments
#### Path Parameters
Name
Type
Description
key [_required_]
string
The specific APP key you are working with.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An application key response.
Field
Type
Description
application_key
object
An application key with its associated metadata.
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
```
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get an application key
Copy
```
                  # Path parameters  
export key="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an application key
```
"""
Get an application key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_application_key(
        key="key",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an application key
```
# Get an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.get_application_key("key")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an application key
```
// Get an application key returns "OK" response

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
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.GetApplicationKey(ctx, "key")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.GetApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.GetApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an application key
```
// Get an application key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ApplicationKeyResponse result = apiInstance.getApplicationKey("key");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#getApplicationKey");
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

#####  Get an application key
```
// Get an application key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.get_application_key("key".to_string()).await;
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

#####  Get an application key
```
/**
 * Get an application key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiGetApplicationKeyRequest = {
  key: "key",
};

apiInstance
  .getApplicationKey(params)
  .then((data: v1.ApplicationKeyResponse) => {
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

GET https://api.ap1.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/application_keys/{app_key_id}
### Overview
Get an application key for your org. This endpoint requires the `org_app_keys_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the application key.
#### Query Strings
Name
Type
Description
include
string
Resource path for related resources to include in the response. Only `owned_by` is supported.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#GetApplicationKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Get an application key
Copy
```
                  # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an application key
```
"""
Get an application key returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = environ["APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_application_key(
        app_key_id=APPLICATION_KEY_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an application key
```
# Get an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
p api_instance.get_application_key(APPLICATION_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an application key
```
// Get an application key returns "OK" response

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
	// there is a valid "application_key" in the system
	ApplicationKeyDataID := os.Getenv("APPLICATION_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.GetApplicationKey(ctx, ApplicationKeyDataID, *datadogV2.NewGetApplicationKeyOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.GetApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.GetApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an application key
```
// Get an application key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "application_key" in the system
    String APPLICATION_KEY_DATA_ID = System.getenv("APPLICATION_KEY_DATA_ID");

    try {
      ApplicationKeyResponse result = apiInstance.getApplicationKey(APPLICATION_KEY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#getApplicationKey");
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

#####  Get an application key
```
// Get an application key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::GetApplicationKeyOptionalParams;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "application_key" in the system
    let application_key_data_id = std::env::var("APPLICATION_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .get_application_key(
            application_key_data_id.clone(),
            GetApplicationKeyOptionalParams::default(),
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

#####  Get an application key
```
/**
 * Get an application key returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "application_key" in the system
const APPLICATION_KEY_DATA_ID = process.env.APPLICATION_KEY_DATA_ID as string;

const params: v2.KeyManagementApiGetApplicationKeyRequest = {
  appKeyId: APPLICATION_KEY_DATA_ID,
};

apiInstance
  .getApplicationKey(params)
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
## [Edit an application key](https://docs.datadoghq.com/api/latest/key-management/#edit-an-application-key)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#edit-an-application-key-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#edit-an-application-key-v2)


PUT https://api.ap1.datadoghq.com/api/v1/application_key/{key}https://api.ap2.datadoghq.com/api/v1/application_key/{key}https://api.datadoghq.eu/api/v1/application_key/{key}https://api.ddog-gov.com/api/v1/application_key/{key}https://api.datadoghq.com/api/v1/application_key/{key}https://api.us3.datadoghq.com/api/v1/application_key/{key}https://api.us5.datadoghq.com/api/v1/application_key/{key}
### Overview
Edit an application key name. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
* `org_app_keys_write`
* `user_app_keys`
  

### Arguments
#### Path Parameters
Name
Type
Description
key [_required_]
string
The specific APP key you are working with.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


Expand All
Field
Type
Description
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
```
{
  "name": "example user"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-404-v1)
  * [409](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-409-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An application key response.
Field
Type
Description
application_key
object
An application key with its associated metadata.
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
```
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Edit an application key
Copy
```
                  # Path parameters  
export key="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key/${key}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Edit an application key
```
"""
Edit an application key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.application_key import ApplicationKey

body = ApplicationKey(
    name="example user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_application_key(key="key", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit an application key
```
# Edit an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApplicationKey.new({
  name: "example user",
})
p api_instance.update_application_key("key", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit an application key
```
// Edit an application key returns "OK" response

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
	body := datadogV1.ApplicationKey{
		Name: datadog.PtrString("example user"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.UpdateApplicationKey(ctx, "key", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.UpdateApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.UpdateApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit an application key
```
// Edit an application key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApplicationKey;
import com.datadog.api.client.v1.model.ApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    ApplicationKey body = new ApplicationKey().name("example user");

    try {
      ApplicationKeyResponse result = apiInstance.updateApplicationKey("key", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#updateApplicationKey");
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

#####  Edit an application key
```
// Edit an application key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV1::model::ApplicationKey;

#[tokio::main]
async fn main() {
    let body = ApplicationKey::new().name("example user".to_string());
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.update_application_key("key".to_string(), body).await;
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

#####  Edit an application key
```
/**
 * Edit an application key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiUpdateApplicationKeyRequest = {
  body: {
    name: "example user",
  },
  key: "key",
};

apiInstance
  .updateApplicationKey(params)
  .then((data: v1.ApplicationKeyResponse) => {
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

PATCH https://api.ap1.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/application_keys/{app_key_id}
### Overview
Edit an application key This endpoint requires the `org_app_keys_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the application key.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
    "id": "string",
    "type": "application_keys",
    "attributes": {
      "name": "Application Key for managing dashboards-updated"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#UpdateApplicationKey-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Edit an application key returns "OK" response
Copy
```
                          # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "string",
    "type": "application_keys",
    "attributes": {
      "name": "Application Key for managing dashboards-updated"
    }
  }
}
EOF  

                        
```

#####  Edit an application key returns "OK" response
```
// Edit an application key returns "OK" response

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
	// there is a valid "application_key" in the system
	ApplicationKeyDataID := os.Getenv("APPLICATION_KEY_DATA_ID")

	body := datadogV2.ApplicationKeyUpdateRequest{
		Data: datadogV2.ApplicationKeyUpdateData{
			Id:   ApplicationKeyDataID,
			Type: datadogV2.APPLICATIONKEYSTYPE_APPLICATION_KEYS,
			Attributes: datadogV2.ApplicationKeyUpdateAttributes{
				Name: datadog.PtrString("Application Key for managing dashboards-updated"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	resp, r, err := api.UpdateApplicationKey(ctx, ApplicationKeyDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.UpdateApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.UpdateApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit an application key returns "OK" response
```
// Edit an application key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;
import com.datadog.api.client.v2.model.ApplicationKeyResponse;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateAttributes;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateData;
import com.datadog.api.client.v2.model.ApplicationKeyUpdateRequest;
import com.datadog.api.client.v2.model.ApplicationKeysType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "application_key" in the system
    String APPLICATION_KEY_DATA_ATTRIBUTES_NAME =
        System.getenv("APPLICATION_KEY_DATA_ATTRIBUTES_NAME");
    String APPLICATION_KEY_DATA_ID = System.getenv("APPLICATION_KEY_DATA_ID");

    ApplicationKeyUpdateRequest body =
        new ApplicationKeyUpdateRequest()
            .data(
                new ApplicationKeyUpdateData()
                    .id(APPLICATION_KEY_DATA_ID)
                    .type(ApplicationKeysType.APPLICATION_KEYS)
                    .attributes(
                        new ApplicationKeyUpdateAttributes()
                            .name("Application Key for managing dashboards-updated")));

    try {
      ApplicationKeyResponse result =
          apiInstance.updateApplicationKey(APPLICATION_KEY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#updateApplicationKey");
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

#####  Edit an application key returns "OK" response
```
"""
Edit an application key returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.application_key_update_attributes import ApplicationKeyUpdateAttributes
from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData
from datadog_api_client.v2.model.application_key_update_request import ApplicationKeyUpdateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ATTRIBUTES_NAME = environ["APPLICATION_KEY_DATA_ATTRIBUTES_NAME"]
APPLICATION_KEY_DATA_ID = environ["APPLICATION_KEY_DATA_ID"]

body = ApplicationKeyUpdateRequest(
    data=ApplicationKeyUpdateData(
        id=APPLICATION_KEY_DATA_ID,
        type=ApplicationKeysType.APPLICATION_KEYS,
        attributes=ApplicationKeyUpdateAttributes(
            name="Application Key for managing dashboards-updated",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_application_key(app_key_id=APPLICATION_KEY_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit an application key returns "OK" response
```
# Edit an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ATTRIBUTES_NAME = ENV["APPLICATION_KEY_DATA_ATTRIBUTES_NAME"]
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]

body = DatadogAPIClient::V2::ApplicationKeyUpdateRequest.new({
  data: DatadogAPIClient::V2::ApplicationKeyUpdateData.new({
    id: APPLICATION_KEY_DATA_ID,
    type: DatadogAPIClient::V2::ApplicationKeysType::APPLICATION_KEYS,
    attributes: DatadogAPIClient::V2::ApplicationKeyUpdateAttributes.new({
      name: "Application Key for managing dashboards-updated",
    }),
  }),
})
p api_instance.update_application_key(APPLICATION_KEY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit an application key returns "OK" response
```
// Edit an application key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateAttributes;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateData;
use datadog_api_client::datadogV2::model::ApplicationKeyUpdateRequest;
use datadog_api_client::datadogV2::model::ApplicationKeysType;

#[tokio::main]
async fn main() {
    // there is a valid "application_key" in the system
    let application_key_data_id = std::env::var("APPLICATION_KEY_DATA_ID").unwrap();
    let body = ApplicationKeyUpdateRequest::new(ApplicationKeyUpdateData::new(
        ApplicationKeyUpdateAttributes::new()
            .name("Application Key for managing dashboards-updated".to_string()),
        application_key_data_id.clone(),
        ApplicationKeysType::APPLICATION_KEYS,
    ));
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .update_application_key(application_key_data_id.clone(), body)
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

#####  Edit an application key returns "OK" response
```
/**
 * Edit an application key returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "application_key" in the system
const APPLICATION_KEY_DATA_ID = process.env.APPLICATION_KEY_DATA_ID as string;

const params: v2.KeyManagementApiUpdateApplicationKeyRequest = {
  body: {
    data: {
      id: APPLICATION_KEY_DATA_ID,
      type: "application_keys",
      attributes: {
        name: "Application Key for managing dashboards-updated",
      },
    },
  },
  appKeyId: APPLICATION_KEY_DATA_ID,
};

apiInstance
  .updateApplicationKey(params)
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
## [Delete an application key](https://docs.datadoghq.com/api/latest/key-management/#delete-an-application-key)
  * [v1](https://docs.datadoghq.com/api/latest/key-management/#delete-an-application-key-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/key-management/#delete-an-application-key-v2)


DELETE https://api.ap1.datadoghq.com/api/v1/application_key/{key}https://api.ap2.datadoghq.com/api/v1/application_key/{key}https://api.datadoghq.eu/api/v1/application_key/{key}https://api.ddog-gov.com/api/v1/application_key/{key}https://api.datadoghq.com/api/v1/application_key/{key}https://api.us3.datadoghq.com/api/v1/application_key/{key}https://api.us5.datadoghq.com/api/v1/application_key/{key}
### Overview
Delete a given application key. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
* `org_app_keys_write`
* `user_app_keys`
  

### Arguments
#### Path Parameters
Name
Type
Description
key [_required_]
string
The specific APP key you are working with.
### Response
  * [200](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


An application key response.
Field
Type
Description
application_key
object
An application key with its associated metadata.
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
```
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Delete an application key
Copy
```
                  # Path parameters  
export key="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an application key
```
"""
Delete an application key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.delete_application_key(
        key="key",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an application key
```
# Delete an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.delete_application_key("key")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an application key
```
// Delete an application key returns "OK" response

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
	api := datadogV1.NewKeyManagementApi(apiClient)
	resp, r, err := api.DeleteApplicationKey(ctx, "key")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.DeleteApplicationKey`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `KeyManagementApi.DeleteApplicationKey`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an application key
```
// Delete an application key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.KeyManagementApi;
import com.datadog.api.client.v1.model.ApplicationKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    try {
      ApplicationKeyResponse result = apiInstance.deleteApplicationKey("key");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#deleteApplicationKey");
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

#####  Delete an application key
```
// Delete an application key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api.delete_application_key("key".to_string()).await;
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

#####  Delete an application key
```
/**
 * Delete an application key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.KeyManagementApi(configuration);

const params: v1.KeyManagementApiDeleteApplicationKeyRequest = {
  key: "key",
};

apiInstance
  .deleteApplicationKey(params)
  .then((data: v1.ApplicationKeyResponse) => {
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

DELETE https://api.ap1.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.ap2.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.datadoghq.eu/api/v2/application_keys/{app_key_id}https://api.ddog-gov.com/api/v2/application_keys/{app_key_id}https://api.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.us3.datadoghq.com/api/v2/application_keys/{app_key_id}https://api.us5.datadoghq.com/api/v2/application_keys/{app_key_id}
### Overview
Delete an application key This endpoint requires the `org_app_keys_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the application key.
### Response
  * [204](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/key-management/#DeleteApplicationKey-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Model](https://docs.datadoghq.com/api/latest/key-management/)
  * [Example](https://docs.datadoghq.com/api/latest/key-management/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
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
  * [Curl](https://docs.datadoghq.com/api/latest/key-management/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/key-management/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/key-management/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/key-management/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/key-management/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/key-management/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/key-management/?code-lang=typescript)


#####  Delete an application key
Copy
```
                  # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an application key
```
"""
Delete an application key returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = environ["APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    api_instance.delete_application_key(
        app_key_id=APPLICATION_KEY_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an application key
```
# Delete an application key returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
api_instance.delete_application_key(APPLICATION_KEY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an application key
```
// Delete an application key returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "application_key" in the system
	ApplicationKeyDataID := os.Getenv("APPLICATION_KEY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewKeyManagementApi(apiClient)
	r, err := api.DeleteApplicationKey(ctx, ApplicationKeyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `KeyManagementApi.DeleteApplicationKey`: %v\n", err)
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

#####  Delete an application key
```
// Delete an application key returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);

    // there is a valid "application_key" in the system
    String APPLICATION_KEY_DATA_ID = System.getenv("APPLICATION_KEY_DATA_ID");

    try {
      apiInstance.deleteApplicationKey(APPLICATION_KEY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#deleteApplicationKey");
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

#####  Delete an application key
```
// Delete an application key returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_key_management::KeyManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "application_key" in the system
    let application_key_data_id = std::env::var("APPLICATION_KEY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = KeyManagementAPI::with_config(configuration);
    let resp = api
        .delete_application_key(application_key_data_id.clone())
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

#####  Delete an application key
```
/**
 * Delete an application key returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.KeyManagementApi(configuration);

// there is a valid "application_key" in the system
const APPLICATION_KEY_DATA_ID = process.env.APPLICATION_KEY_DATA_ID as string;

const params: v2.KeyManagementApiDeleteApplicationKeyRequest = {
  appKeyId: APPLICATION_KEY_DATA_ID,
};

apiInstance
  .deleteApplicationKey(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ca59bb50-6422-4256-ae9f-6f0afdc31ea6&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f1a49637-8b9d-4f98-a01a-4a47b32ad73f&pt=Key%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fkey-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ca59bb50-6422-4256-ae9f-6f0afdc31ea6&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f1a49637-8b9d-4f98-a01a-4a47b32ad73f&pt=Key%20Management&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fkey-management%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=aeacf556-316d-4de3-9a6a-2766ee3cf09d&bo=2&sid=b77a5fe0f0bf11f0bab0291dd4b5f9fd&vid=b77a7130f0bf11f0b69eb7008fe8e23b&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Key%20Management&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fkey-management%2F&r=&lt=3241&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=557113)
