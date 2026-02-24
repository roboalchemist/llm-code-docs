# Source: https://docs.datadoghq.com/api/latest/key-management.md

---
title: Key Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Key Management
---

# Key Management

Manage your Datadog API and application keys. You need an API key and an application key for a user with the required permissions to interact with these endpoints.

Consult the following pages to view and manage your keys:

- [API Keys](https://app.datadoghq.com/organization-settings/api-keys)
- [Application Keys](https://app.datadoghq.com/personal-settings/application-keys)

## Delete an application key owned by current user{% #delete-an-application-key-owned-by-current-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                           |
| ----------------- | -------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/current_user/application_keys/{app_key_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/current_user/application_keys/{app_key_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |

### Overview

Delete an application key owned by current user This endpoint requires the `user_app_keys` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                    |
| ---------------------------- | ------ | ------------------------------ |
| app_key_id [*required*] | string | The ID of the application key. |

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
                  \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an application key owned by current user returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
api_instance.delete_current_user_application_key(APPLICATION_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get all API keys{% #get-all-api-keys %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                     |
| ----------------- | ------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/api_key |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/api_key |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/api_key      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/api_key      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/api_key     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/api_key |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/api_key |

### Overview

Get all API keys available for your account. This endpoint requires the `api_keys_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of API and application keys available for a given organization.

| Parent field | Field      | Type     | Description                                   |
| ------------ | ---------- | -------- | --------------------------------------------- |
|              | api_keys   | [object] | Array of API keys.                            |
| api_keys     | created    | string   | Date of creation of the API key.              |
| api_keys     | created_by | string   | Datadog user handle that created the API key. |
| api_keys     | key        | string   | API key.                                      |
| api_keys     | name       | string   | Name of your API key.                         |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all API keys returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.list_api_keys()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                      |
| ----------------- | ------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/api_keys |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/api_keys |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/api_keys      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/api_keys      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/api_keys     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/api_keys |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/api_keys |

### Overview

List all API keys available for your account. This endpoint requires the `api_keys_read` permission.

### Arguments

#### Query Strings

| Name                               | Type    | Description                                                                                                                                                                                                                                                     |
| ---------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]                         | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                                                                        |
| page[number]                       | integer | Specific page number to return.                                                                                                                                                                                                                                 |
| sort                               | enum    | API key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign.Allowed enum values: `created_at, -created_at, last4, -last4, modified_at, -modified_at, name, -name` |
| filter                             | string  | Filter API keys by the specified string.                                                                                                                                                                                                                        |
| filter[created_at][start]          | string  | Only include API keys created on or after the specified date.                                                                                                                                                                                                   |
| filter[created_at][end]            | string  | Only include API keys created on or before the specified date.                                                                                                                                                                                                  |
| filter[modified_at][start]         | string  | Only include API keys modified on or after the specified date.                                                                                                                                                                                                  |
| filter[modified_at][end]           | string  | Only include API keys modified on or before the specified date.                                                                                                                                                                                                 |
| include                            | string  | Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`.                                                                                                           |
| filter[remote_config_read_enabled] | boolean | Filter API keys by remote config read enabled status.                                                                                                                                                                                                           |
| filter[category]                   | string  | Filter API keys by category.                                                                                                                                                                                                                                    |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a list of API keys.

| Parent field  | Field                        | Type            | Description                                                                |
| ------------- | ---------------------------- | --------------- | -------------------------------------------------------------------------- |
|               | data                         | [object]        | Array of API keys.                                                         |
| data          | attributes                   | object          | Attributes of a partial API key.                                           |
| attributes    | category                     | string          | The category of the API key.                                               |
| attributes    | created_at                   | string          | Creation date of the API key.                                              |
| attributes    | date_last_used               | date-time       | Date the API Key was last used.                                            |
| attributes    | last4                        | string          | The last four characters of the API key.                                   |
| attributes    | modified_at                  | string          | Date the API key was last modified.                                        |
| attributes    | name                         | string          | Name of the API key.                                                       |
| attributes    | remote_config_read_enabled   | boolean         | The remote config read enabled status.                                     |
| data          | id                           | string          | ID of the API key.                                                         |
| data          | relationships                | object          | Resources related to the API key.                                          |
| relationships | created_by                   | object          | Relationship to user.                                                      |
| created_by    | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | modified_by                  | object          | Relationship to user.                                                      |
| modified_by   | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| data          | type                         | enum            | API Keys resource type. Allowed enum values: `api_keys`                    |
|               | included                     | [ <oneOf>] | Array of objects related to the API key.                                   |
| included      | Option 1                     | object          | User object returned by the API.                                           |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                             |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                 |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                              |
| attributes    | email                        | string          | Email of the user.                                                         |
| attributes    | handle                       | string          | Handle of the user.                                                        |
| attributes    | icon                         | string          | URL of the user's icon.                                                    |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                          |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                   |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                      |
| attributes    | name                         | string          | Name of the user.                                                          |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                     |
| attributes    | status                       | string          | Status of the user.                                                        |
| attributes    | title                        | string          | Title of the user.                                                         |
| attributes    | verified                     | boolean         | Whether the user is verified.                                              |
| Option 1      | id                           | string          | ID of the user.                                                            |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                      |
| relationships | org                          | object          | Relationship to an organization.                                           |
| org           | data [*required*]       | object          | Relationship to organization object.                                       |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_orgs                   | object          | Relationship to organizations.                                             |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                     |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_users                  | object          | Relationship to users.                                                     |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                             |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | roles                        | object          | Relationship to roles.                                                     |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.              |
| data          | id                           | string          | The unique identifier of the role.                                         |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                   |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                          |
| included      | Option 2                     | object          | The definition of LeakedKey object.                                        |
| Option 2      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                              |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                              |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                       |
| Option 2      | id [*required*]         | string          | The LeakedKey id.                                                          |
| Option 2      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys` |
|               | meta                         | object          | Additional information related to api keys response.                       |
| meta          | max_allowed                  | int64           | Max allowed number of API keys.                                            |
| meta          | page                         | object          | Additional information related to the API keys response.                   |
| page          | total_filtered_count         | int64           | Total filtered application key count.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create an API key{% #create-an-api-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                      |
| ----------------- | ------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/api_key |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/api_key |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/api_key      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/api_key      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/api_key     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/api_key |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/api_key |

### Overview

Creates an API key with a given name. This endpoint requires the `api_keys_write` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Field      | Type   | Description                                   |
| ---------- | ------ | --------------------------------------------- |
| created    | string | Date of creation of the API key.              |
| created_by | string | Datadog user handle that created the API key. |
| key        | string | API key.                                      |
| name       | string | Name of your API key.                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "name": "example user"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An API key with its associated metadata.

| Parent field | Field      | Type   | Description                                   |
| ------------ | ---------- | ------ | --------------------------------------------- |
|              | api_key    | object | Datadog API key.                              |
| api_key      | created    | string | Date of creation of the API key.              |
| api_key      | created_by | string | Datadog user handle that created the API key. |
| api_key      | key        | string | API key.                                      |
| api_key      | name       | string | Name of your API key.                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
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
Forbidden
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key" \
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create an API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApiKey.new({
  name: "example user",
})
p api_instance.create_api_key(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                       |
| ----------------- | -------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/api_keys |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/api_keys |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/api_keys      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/api_keys      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/api_keys     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/api_keys |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/api_keys |

### Overview

Create an API key. This endpoint requires the `api_keys_write` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                             |
| ------------ | ---------------------------- | ------- | ------------------------------------------------------- |
|              | data [*required*]       | object  | Object used to create an API key.                       |
| data         | attributes [*required*] | object  | Attributes used to create an API Key.                   |
| attributes   | category                     | string  | The APIKeyCreateAttributes category.                    |
| attributes   | name [*required*]       | string  | Name of the API key.                                    |
| attributes   | remote_config_read_enabled   | boolean | The APIKeyCreateAttributes remote_config_read_enabled.  |
| data         | type [*required*]       | enum    | API Keys resource type. Allowed enum values: `api_keys` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "api_keys",
    "attributes": {
      "name": "Example-Key-Management"
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response for retrieving an API key.

| Parent field  | Field                        | Type            | Description                                                                |
| ------------- | ---------------------------- | --------------- | -------------------------------------------------------------------------- |
|               | data                         | object          | Datadog API key.                                                           |
| data          | attributes                   | object          | Attributes of a full API key.                                              |
| attributes    | category                     | string          | The category of the API key.                                               |
| attributes    | created_at                   | date-time       | Creation date of the API key.                                              |
| attributes    | date_last_used               | date-time       | Date the API Key was last used                                             |
| attributes    | key                          | string          | The API key.                                                               |
| attributes    | last4                        | string          | The last four characters of the API key.                                   |
| attributes    | modified_at                  | date-time       | Date the API key was last modified.                                        |
| attributes    | name                         | string          | Name of the API key.                                                       |
| attributes    | remote_config_read_enabled   | boolean         | The remote config read enabled status.                                     |
| data          | id                           | string          | ID of the API key.                                                         |
| data          | relationships                | object          | Resources related to the API key.                                          |
| relationships | created_by                   | object          | Relationship to user.                                                      |
| created_by    | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | modified_by                  | object          | Relationship to user.                                                      |
| modified_by   | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| data          | type                         | enum            | API Keys resource type. Allowed enum values: `api_keys`                    |
|               | included                     | [ <oneOf>] | Array of objects related to the API key.                                   |
| included      | Option 1                     | object          | User object returned by the API.                                           |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                             |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                 |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                              |
| attributes    | email                        | string          | Email of the user.                                                         |
| attributes    | handle                       | string          | Handle of the user.                                                        |
| attributes    | icon                         | string          | URL of the user's icon.                                                    |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                          |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                   |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                      |
| attributes    | name                         | string          | Name of the user.                                                          |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                     |
| attributes    | status                       | string          | Status of the user.                                                        |
| attributes    | title                        | string          | Title of the user.                                                         |
| attributes    | verified                     | boolean         | Whether the user is verified.                                              |
| Option 1      | id                           | string          | ID of the user.                                                            |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                      |
| relationships | org                          | object          | Relationship to an organization.                                           |
| org           | data [*required*]       | object          | Relationship to organization object.                                       |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_orgs                   | object          | Relationship to organizations.                                             |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                     |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_users                  | object          | Relationship to users.                                                     |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                             |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | roles                        | object          | Relationship to roles.                                                     |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.              |
| data          | id                           | string          | The unique identifier of the role.                                         |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                   |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                          |
| included      | Option 2                     | object          | The definition of LeakedKey object.                                        |
| Option 2      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                              |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                              |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                       |
| Option 2      | id [*required*]         | string          | The LeakedKey id.                                                          |
| Option 2      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Edit an application key owned by current user{% #edit-an-application-key-owned-by-current-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/current_user/application_keys/{app_key_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/current_user/application_keys/{app_key_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |

### Overview

Edit an application key owned by current user. The `key` field is not returned for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires the `user_app_keys` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                    |
| ---------------------------- | ------ | ------------------------------ |
| app_key_id [*required*] | string | The ID of the application key. |

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
    "id": "string",
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
                          \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys/${app_key_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get API key{% #get-api-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                           |
| ----------------- | ------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/api_key/{key} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/api_key/{key} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/api_key/{key}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/api_key/{key}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/api_key/{key}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/api_key/{key} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/api_key/{key} |

### Overview

Get a given API key. This endpoint requires the `api_keys_read` permission.

### Arguments

#### Path Parameters

| Name                  | Type   | Description                                |
| --------------------- | ------ | ------------------------------------------ |
| key [*required*] | string | The specific API key you are working with. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An API key with its associated metadata.

| Parent field | Field      | Type   | Description                                   |
| ------------ | ---------- | ------ | --------------------------------------------- |
|              | api_key    | object | Datadog API key.                              |
| api_key      | created    | string | Date of creation of the API key.              |
| api_key      | created_by | string | Datadog user handle that created the API key. |
| api_key      | key        | string | API key.                                      |
| api_key      | name       | string | Name of your API key.                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Path parametersexport key="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.get_api_key("key")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/api_keys/{api_key_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/api_keys/{api_key_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/api_keys/{api_key_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/api_keys/{api_key_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/api_keys/{api_key_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/api_keys/{api_key_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/api_keys/{api_key_id} |

### Overview

Get an API key. This endpoint requires the `api_keys_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| api_key_id [*required*] | string | The ID of the API key. |

#### Query Strings

| Name    | Type   | Description                                                                                                                                           |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for retrieving an API key.

| Parent field  | Field                        | Type            | Description                                                                |
| ------------- | ---------------------------- | --------------- | -------------------------------------------------------------------------- |
|               | data                         | object          | Datadog API key.                                                           |
| data          | attributes                   | object          | Attributes of a full API key.                                              |
| attributes    | category                     | string          | The category of the API key.                                               |
| attributes    | created_at                   | date-time       | Creation date of the API key.                                              |
| attributes    | date_last_used               | date-time       | Date the API Key was last used                                             |
| attributes    | key                          | string          | The API key.                                                               |
| attributes    | last4                        | string          | The last four characters of the API key.                                   |
| attributes    | modified_at                  | date-time       | Date the API key was last modified.                                        |
| attributes    | name                         | string          | Name of the API key.                                                       |
| attributes    | remote_config_read_enabled   | boolean         | The remote config read enabled status.                                     |
| data          | id                           | string          | ID of the API key.                                                         |
| data          | relationships                | object          | Resources related to the API key.                                          |
| relationships | created_by                   | object          | Relationship to user.                                                      |
| created_by    | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | modified_by                  | object          | Relationship to user.                                                      |
| modified_by   | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| data          | type                         | enum            | API Keys resource type. Allowed enum values: `api_keys`                    |
|               | included                     | [ <oneOf>] | Array of objects related to the API key.                                   |
| included      | Option 1                     | object          | User object returned by the API.                                           |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                             |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                 |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                              |
| attributes    | email                        | string          | Email of the user.                                                         |
| attributes    | handle                       | string          | Handle of the user.                                                        |
| attributes    | icon                         | string          | URL of the user's icon.                                                    |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                          |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                   |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                      |
| attributes    | name                         | string          | Name of the user.                                                          |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                     |
| attributes    | status                       | string          | Status of the user.                                                        |
| attributes    | title                        | string          | Title of the user.                                                         |
| attributes    | verified                     | boolean         | Whether the user is verified.                                              |
| Option 1      | id                           | string          | ID of the user.                                                            |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                      |
| relationships | org                          | object          | Relationship to an organization.                                           |
| org           | data [*required*]       | object          | Relationship to organization object.                                       |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_orgs                   | object          | Relationship to organizations.                                             |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                     |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_users                  | object          | Relationship to users.                                                     |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                             |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | roles                        | object          | Relationship to roles.                                                     |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.              |
| data          | id                           | string          | The unique identifier of the role.                                         |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                   |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                          |
| included      | Option 2                     | object          | The definition of LeakedKey object.                                        |
| Option 2      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                              |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                              |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                       |
| Option 2      | id [*required*]         | string          | The LeakedKey id.                                                          |
| Option 2      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport api_key_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys/${api_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "api_key" in the system
API_KEY_DATA_ID = ENV["API_KEY_DATA_ID"]
p api_instance.get_api_key(API_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get one application key owned by current user{% #get-one-application-key-owned-by-current-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/current_user/application_keys/{app_key_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/current_user/application_keys/{app_key_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/current_user/application_keys/{app_key_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/current_user/application_keys/{app_key_id} |

### Overview

Get an application key owned by current user. The `key` field is not returned for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires the `user_app_keys` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                    |
| ---------------------------- | ------ | ------------------------------ |
| app_key_id [*required*] | string | The ID of the application key. |

### Response

{% tab title="200" %}
OK
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
                  \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get one application key owned by current user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
p api_instance.get_current_user_application_key(APPLICATION_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create an application key for current user{% #create-an-application-key-for-current-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/current_user/application_keys |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/current_user/application_keys |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/current_user/application_keys      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/current_user/application_keys      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/current_user/application_keys     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/current_user/application_keys |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/current_user/application_keys |

### Overview

Create an application key for current user This endpoint requires the `user_app_keys` permission.

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

##### 

```json
{
  "data": {
    "type": "application_keys",
    "attributes": {
      "name": "Example-Key-Management"
    }
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys" \
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
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys" \
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
                        
##### 

```go
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

##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Edit an API key{% #edit-an-api-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                           |
| ----------------- | ------------------------------------------------------ |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/api_key/{key} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/api_key/{key} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/api_key/{key}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/api_key/{key}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/api_key/{key}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/api_key/{key} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/api_key/{key} |

### Overview

Edit an API key name. This endpoint requires the `api_keys_write` permission.

### Arguments

#### Path Parameters

| Name                  | Type   | Description                                |
| --------------------- | ------ | ------------------------------------------ |
| key [*required*] | string | The specific API key you are working with. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Field      | Type   | Description                                   |
| ---------- | ------ | --------------------------------------------- |
| created    | string | Date of creation of the API key.              |
| created_by | string | Datadog user handle that created the API key. |
| key        | string | API key.                                      |
| name       | string | Name of your API key.                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "name": "example user"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An API key with its associated metadata.

| Parent field | Field      | Type   | Description                                   |
| ------------ | ---------- | ------ | --------------------------------------------- |
|              | api_key    | object | Datadog API key.                              |
| api_key      | created    | string | Date of creation of the API key.              |
| api_key      | created_by | string | Datadog user handle that created the API key. |
| api_key      | key        | string | API key.                                      |
| api_key      | name       | string | Name of your API key.                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
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
Forbidden
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
                  \# Path parametersexport key="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key/${key}" \
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Edit an API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApiKey.new({
  name: "example user",
})
p api_instance.update_api_key("key", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/api_keys/{api_key_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/api_keys/{api_key_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/api_keys/{api_key_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/api_keys/{api_key_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/api_keys/{api_key_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/api_keys/{api_key_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/api_keys/{api_key_id} |

### Overview

Update an API key. This endpoint requires the `api_keys_write` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| api_key_id [*required*] | string | The ID of the API key. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                             |
| ------------ | ---------------------------- | ------- | ------------------------------------------------------- |
|              | data [*required*]       | object  | Object used to update an API key.                       |
| data         | attributes [*required*] | object  | Attributes used to update an API Key.                   |
| attributes   | category                     | string  | The APIKeyUpdateAttributes category.                    |
| attributes   | name [*required*]       | string  | Name of the API key.                                    |
| attributes   | remote_config_read_enabled   | boolean | The APIKeyUpdateAttributes remote_config_read_enabled.  |
| data         | id [*required*]         | string  | ID of the API key.                                      |
| data         | type [*required*]       | enum    | API Keys resource type. Allowed enum values: `api_keys` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for retrieving an API key.

| Parent field  | Field                        | Type            | Description                                                                |
| ------------- | ---------------------------- | --------------- | -------------------------------------------------------------------------- |
|               | data                         | object          | Datadog API key.                                                           |
| data          | attributes                   | object          | Attributes of a full API key.                                              |
| attributes    | category                     | string          | The category of the API key.                                               |
| attributes    | created_at                   | date-time       | Creation date of the API key.                                              |
| attributes    | date_last_used               | date-time       | Date the API Key was last used                                             |
| attributes    | key                          | string          | The API key.                                                               |
| attributes    | last4                        | string          | The last four characters of the API key.                                   |
| attributes    | modified_at                  | date-time       | Date the API key was last modified.                                        |
| attributes    | name                         | string          | Name of the API key.                                                       |
| attributes    | remote_config_read_enabled   | boolean         | The remote config read enabled status.                                     |
| data          | id                           | string          | ID of the API key.                                                         |
| data          | relationships                | object          | Resources related to the API key.                                          |
| relationships | created_by                   | object          | Relationship to user.                                                      |
| created_by    | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | modified_by                  | object          | Relationship to user.                                                      |
| modified_by   | data [*required*]       | object          | Relationship to user object.                                               |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| data          | type                         | enum            | API Keys resource type. Allowed enum values: `api_keys`                    |
|               | included                     | [ <oneOf>] | Array of objects related to the API key.                                   |
| included      | Option 1                     | object          | User object returned by the API.                                           |
| Option 1      | attributes                   | object          | Attributes of user object returned by the API.                             |
| attributes    | created_at                   | date-time       | Creation time of the user.                                                 |
| attributes    | disabled                     | boolean         | Whether the user is disabled.                                              |
| attributes    | email                        | string          | Email of the user.                                                         |
| attributes    | handle                       | string          | Handle of the user.                                                        |
| attributes    | icon                         | string          | URL of the user's icon.                                                    |
| attributes    | last_login_time              | date-time       | The last time the user logged in.                                          |
| attributes    | mfa_enabled                  | boolean         | If user has MFA enabled.                                                   |
| attributes    | modified_at                  | date-time       | Time that the user was last modified.                                      |
| attributes    | name                         | string          | Name of the user.                                                          |
| attributes    | service_account              | boolean         | Whether the user is a service account.                                     |
| attributes    | status                       | string          | Status of the user.                                                        |
| attributes    | title                        | string          | Title of the user.                                                         |
| attributes    | verified                     | boolean         | Whether the user is verified.                                              |
| Option 1      | id                           | string          | ID of the user.                                                            |
| Option 1      | relationships                | object          | Relationships of the user object returned by the API.                      |
| relationships | org                          | object          | Relationship to an organization.                                           |
| org           | data [*required*]       | object          | Relationship to organization object.                                       |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_orgs                   | object          | Relationship to organizations.                                             |
| other_orgs    | data [*required*]       | [object]        | Relationships to organization objects.                                     |
| data          | id [*required*]         | string          | ID of the organization.                                                    |
| data          | type [*required*]       | enum            | Organizations resource type. Allowed enum values: `orgs`                   |
| relationships | other_users                  | object          | Relationship to users.                                                     |
| other_users   | data [*required*]       | [object]        | Relationships to user objects.                                             |
| data          | id [*required*]         | string          | A unique identifier that represents the user.                              |
| data          | type [*required*]       | enum            | Users resource type. Allowed enum values: `users`                          |
| relationships | roles                        | object          | Relationship to roles.                                                     |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.              |
| data          | id                           | string          | The unique identifier of the role.                                         |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                   |
| Option 1      | type                         | enum            | Users resource type. Allowed enum values: `users`                          |
| included      | Option 2                     | object          | The definition of LeakedKey object.                                        |
| Option 2      | attributes [*required*] | object          | The definition of LeakedKeyAttributes object.                              |
| attributes    | date [*required*]       | date-time       | The LeakedKeyAttributes date.                                              |
| attributes    | leak_source                  | string          | The LeakedKeyAttributes leak_source.                                       |
| Option 2      | id [*required*]         | string          | The LeakedKey id.                                                          |
| Option 2      | type [*required*]       | enum            | The definition of LeakedKeyType object. Allowed enum values: `leaked_keys` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport api_key_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys/${api_key_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete an API key{% #delete-an-api-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/api_key/{key} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/api_key/{key} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/api_key/{key}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/api_key/{key}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/api_key/{key}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/api_key/{key} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/api_key/{key} |

### Overview

Delete a given API key. This endpoint requires the `api_keys_delete` permission.

### Arguments

#### Path Parameters

| Name                  | Type   | Description                                |
| --------------------- | ------ | ------------------------------------------ |
| key [*required*] | string | The specific API key you are working with. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An API key with its associated metadata.

| Parent field | Field      | Type   | Description                                   |
| ------------ | ---------- | ------ | --------------------------------------------- |
|              | api_key    | object | Datadog API key.                              |
| api_key      | created    | string | Date of creation of the API key.              |
| api_key      | created_by | string | Datadog user handle that created the API key. |
| api_key      | key        | string | API key.                                      |
| api_key      | name       | string | Name of your API key.                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "api_key": {
    "created_by": "test_user",
    "key": "1234512345123456abcabc912349abcd",
    "name": "app_key"
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
Forbidden
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
                  \# Path parametersexport key="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/api_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.delete_api_key("key")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/api_keys/{api_key_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/api_keys/{api_key_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/api_keys/{api_key_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/api_keys/{api_key_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/api_keys/{api_key_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/api_keys/{api_key_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/api_keys/{api_key_id} |

### Overview

Delete an API key. This endpoint requires the `api_keys_delete` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description            |
| ---------------------------- | ------ | ---------------------- |
| api_key_id [*required*] | string | The ID of the API key. |

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
                  \# Path parametersexport api_key_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/api_keys/${api_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an API key returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "api_key" in the system
API_KEY_DATA_ID = ENV["API_KEY_DATA_ID"]
api_instance.delete_api_key(API_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get all application keys owned by current user{% #get-all-application-keys-owned-by-current-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/current_user/application_keys |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/current_user/application_keys |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/current_user/application_keys      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/current_user/application_keys      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/current_user/application_keys     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/current_user/application_keys |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/current_user/application_keys |

### Overview

List all application keys available for current user This endpoint requires the `user_app_keys` permission.

### Arguments

#### Query Strings

| Name                      | Type    | Description                                                                                                                                                                                                                                  |
| ------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]                | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                                                     |
| page[number]              | integer | Specific page number to return.                                                                                                                                                                                                              |
| sort                      | enum    | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign.Allowed enum values: `created_at, -created_at, last4, -last4, name, -name` |
| filter                    | string  | Filter application keys by the specified string.                                                                                                                                                                                             |
| filter[created_at][start] | string  | Only include application keys created on or after the specified date.                                                                                                                                                                        |
| filter[created_at][end]   | string  | Only include application keys created on or before the specified date.                                                                                                                                                                       |
| include                   | string  | Resource path for related resources to include in the response. Only `owned_by` is supported.                                                                                                                                                |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/current_user/application_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all application keys owned by current user returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new
p api_instance.list_current_user_application_keys()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get all application keys{% #get-all-application-keys %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/application_key |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/application_key |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/application_key      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/application_key      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/application_key     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/application_key |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/application_key |

### Overview

Get all application keys available for your Datadog account. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
`org_app_keys_read``user_app_keys`


### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An application key response.

| Parent field     | Field            | Type     | Description                  |
| ---------------- | ---------------- | -------- | ---------------------------- |
|                  | application_keys | [object] | Array of application keys.   |
| application_keys | hash             | string   | Hash of an application key.  |
| application_keys | name             | string   | Name of an application key.  |
| application_keys | owner            | string   | Owner of an application key. |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all application keys returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.list_application_keys()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/application_keys |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/application_keys |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/application_keys      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/application_keys      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/application_keys     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/application_keys |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/application_keys |

### Overview

List all application keys available for your org This endpoint requires the `org_app_keys_read` permission.

### Arguments

#### Query Strings

| Name                      | Type    | Description                                                                                                                                                                                                                                  |
| ------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[size]                | integer | Size for a given page. The maximum allowed value is 100.                                                                                                                                                                                     |
| page[number]              | integer | Specific page number to return.                                                                                                                                                                                                              |
| sort                      | enum    | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign.Allowed enum values: `created_at, -created_at, last4, -last4, name, -name` |
| filter                    | string  | Filter application keys by the specified string.                                                                                                                                                                                             |
| filter[created_at][start] | string  | Only include application keys created on or after the specified date.                                                                                                                                                                        |
| filter[created_at][end]   | string  | Only include application keys created on or before the specified date.                                                                                                                                                                       |
| include                   | string  | Resource path for related resources to include in the response. Only `owned_by` is supported.                                                                                                                                                |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all application keys returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new
p api_instance.list_application_keys()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create an application key{% #create-an-application-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/application_key |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/application_key |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/application_key      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/application_key      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/application_key     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/application_key |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/application_key |

### Overview

Create an application key with a given name. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires the `user_app_keys` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Field | Type   | Description                  |
| ----- | ------ | ---------------------------- |
| hash  | string | Hash of an application key.  |
| name  | string | Name of an application key.  |
| owner | string | Owner of an application key. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "name": "example user"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An application key response.

| Parent field    | Field           | Type   | Description                                      |
| --------------- | --------------- | ------ | ------------------------------------------------ |
|                 | application_key | object | An application key with its associated metadata. |
| application_key | hash            | string | Hash of an application key.                      |
| application_key | name            | string | Name of an application key.                      |
| application_key | owner           | string | Owner of an application key.                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
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
Forbidden
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key" \
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApplicationKey.new({
  name: "example user",
})
p api_instance.create_application_key(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get an application key{% #get-an-application-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/application_key/{key} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/application_key/{key} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/application_key/{key}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/application_key/{key}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/application_key/{key}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/application_key/{key} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/application_key/{key} |

### Overview

Get a given application key. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
`org_app_keys_read``user_app_keys`


### Arguments

#### Path Parameters

| Name                  | Type   | Description                                |
| --------------------- | ------ | ------------------------------------------ |
| key [*required*] | string | The specific APP key you are working with. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An application key response.

| Parent field    | Field           | Type   | Description                                      |
| --------------- | --------------- | ------ | ------------------------------------------------ |
|                 | application_key | object | An application key with its associated metadata. |
| application_key | hash            | string | Hash of an application key.                      |
| application_key | name            | string | Name of an application key.                      |
| application_key | owner           | string | Owner of an application key.                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Path parametersexport key="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.get_application_key("key")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/application_keys/{app_key_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/application_keys/{app_key_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/application_keys/{app_key_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/application_keys/{app_key_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/application_keys/{app_key_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/application_keys/{app_key_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/application_keys/{app_key_id} |

### Overview

Get an application key for your org. This endpoint requires the `org_app_keys_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                    |
| ---------------------------- | ------ | ------------------------------ |
| app_key_id [*required*] | string | The ID of the application key. |

#### Query Strings

| Name    | Type   | Description                                                                                   |
| ------- | ------ | --------------------------------------------------------------------------------------------- |
| include | string | Resource path for related resources to include in the response. Only `owned_by` is supported. |

### Response

{% tab title="200" %}
OK
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
                  \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
p api_instance.get_application_key(APPLICATION_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Edit an application key{% #edit-an-application-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/application_key/{key} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/application_key/{key} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/application_key/{key}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/application_key/{key}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/application_key/{key}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/application_key/{key} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/application_key/{key} |

### Overview

Edit an application key name. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
`org_app_keys_write``user_app_keys`


### Arguments

#### Path Parameters

| Name                  | Type   | Description                                |
| --------------------- | ------ | ------------------------------------------ |
| key [*required*] | string | The specific APP key you are working with. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Field | Type   | Description                  |
| ----- | ------ | ---------------------------- |
| hash  | string | Hash of an application key.  |
| name  | string | Name of an application key.  |
| owner | string | Owner of an application key. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "name": "example user"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An application key response.

| Parent field    | Field           | Type   | Description                                      |
| --------------- | --------------- | ------ | ------------------------------------------------ |
|                 | application_key | object | An application key with its associated metadata. |
| application_key | hash            | string | Hash of an application key.                      |
| application_key | name            | string | Name of an application key.                      |
| application_key | owner           | string | Owner of an application key.                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
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
Forbidden
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
                  \# Path parametersexport key="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key/${key}" \
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Edit an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new

body = DatadogAPIClient::V1::ApplicationKey.new({
  name: "example user",
})
p api_instance.update_application_key("key", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/application_keys/{app_key_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/application_keys/{app_key_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/application_keys/{app_key_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/application_keys/{app_key_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/application_keys/{app_key_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/application_keys/{app_key_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/application_keys/{app_key_id} |

### Overview

Edit an application key This endpoint requires the `org_app_keys_write` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                    |
| ---------------------------- | ------ | ------------------------------ |
| app_key_id [*required*] | string | The ID of the application key. |

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
    "id": "string",
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
                          \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys/${app_key_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete an application key{% #delete-an-application-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/application_key/{key} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/application_key/{key} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/application_key/{key}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/application_key/{key}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/application_key/{key}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/application_key/{key} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/application_key/{key} |

### Overview

Delete a given application key. This endpoint is disabled for organizations in [One-Time Read mode](https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode). This endpoint requires any of the following permissions:
`org_app_keys_write``user_app_keys`


### Arguments

#### Path Parameters

| Name                  | Type   | Description                                |
| --------------------- | ------ | ------------------------------------------ |
| key [*required*] | string | The specific APP key you are working with. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An application key response.

| Parent field    | Field           | Type   | Description                                      |
| --------------- | --------------- | ------ | ------------------------------------------------ |
|                 | application_key | object | An application key with its associated metadata. |
| application_key | hash            | string | Hash of an application key.                      |
| application_key | name            | string | Name of an application key.                      |
| application_key | owner           | string | Owner of an application key.                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "app_key",
    "owner": "test_user"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Path parametersexport key="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/application_key/${key}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an application key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::KeyManagementAPI.new
p api_instance.delete_application_key("key")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/application_keys/{app_key_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/application_keys/{app_key_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/application_keys/{app_key_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/application_keys/{app_key_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/application_keys/{app_key_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/application_keys/{app_key_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/application_keys/{app_key_id} |

### Overview

Delete an application key This endpoint requires the `org_app_keys_write` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                    |
| ---------------------------- | ------ | ------------------------------ |
| app_key_id [*required*] | string | The ID of the application key. |

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
                  \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/application_keys/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an application key returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::KeyManagementAPI.new

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = ENV["APPLICATION_KEY_DATA_ID"]
api_instance.delete_application_key(APPLICATION_KEY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
