# Source: https://docs.datadoghq.com/api/latest/authentication.md

---
title: Authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Authentication
---

# Authentication

All requests to Datadog's API must be authenticated. Requests that write data require reporting access and require an `API key`. Requests that read data require full access and also require an `application key`.

**Note:** All Datadog API clients are configured by default to consume Datadog US site APIs. If you are on the Datadog EU site, set the environment variable `DATADOG_HOST` to `https://api.datadoghq.eu` or override this value directly when creating your client.

[Manage your account's API and application keys](https://app.datadoghq.com/organization-settings/) in Datadog, and see the [API and Application Keys page](https://docs.datadoghq.com/account_management/api-app-keys/) in the documentation.

## Validate API key{% #validate-api-key %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                      |
| ----------------- | ------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/validate |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/validate |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/validate      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/validate      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/validate     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/validate |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/validate |

### Overview

Check if the API key (not the APP key) is valid. If invalid, a 403 is returned.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Represent validation endpoint responses.

| Field | Type    | Description                                            |
| ----- | ------- | ------------------------------------------------------ |
| valid | boolean | Return `true` if the authentication response is valid. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "valid": true
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/validate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}"
                
##### 

```python
"""
Validate API key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.authentication_api import AuthenticationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthenticationApi(api_client)
    response = api_instance.validate()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
##### 

```ruby
# Validate API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AuthenticationAPI.new
p api_instance.validate()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```go
// Validate API key returns "OK" response

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
	api := datadogV1.NewAuthenticationApi(apiClient)
	resp, r, err := api.Validate(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationApi.Validate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationApi.Validate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
##### 

```java
// Validate API key returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AuthenticationApi;
import com.datadog.api.client.v1.model.AuthenticationValidationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);

    try {
      AuthenticationValidationResponse result = apiInstance.validate();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#validate");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
##### 

```rust
// Validate API key returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_authentication::AuthenticationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AuthenticationAPI::with_config(configuration);
    let resp = api.validate().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
##### 

```typescript
/**
 * Validate API key returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AuthenticationApi(configuration);

apiInstance
  .validate()
  .then((data: v1.AuthenticationValidationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}
