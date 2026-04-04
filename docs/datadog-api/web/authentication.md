# Source: https://docs.datadoghq.com/api/latest/authentication/

# Authentication
All requests to Datadog’s API must be authenticated. Requests that write data require reporting access and require an `API key`. Requests that read data require full access and also require an `application key`.
**Note:** All Datadog API clients are configured by default to consume Datadog US site APIs. If you are on the Datadog EU site, set the environment variable `DATADOG_HOST` to `https://api.datadoghq.eu` or override this value directly when creating your client.
[Manage your account’s API and application keys](https://app.datadoghq.com/organization-settings/) in Datadog, and see the [API and Application Keys page](https://docs.datadoghq.com/account_management/api-app-keys/) in the documentation.
## [Validate API key](https://docs.datadoghq.com/api/latest/authentication/#validate-api-key)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/authentication/#validate-api-key-v1)


GET https://api.ap1.datadoghq.com/api/v1/validatehttps://api.ap2.datadoghq.com/api/v1/validatehttps://api.datadoghq.eu/api/v1/validatehttps://api.ddog-gov.com/api/v1/validatehttps://api.datadoghq.com/api/v1/validatehttps://api.us3.datadoghq.com/api/v1/validatehttps://api.us5.datadoghq.com/api/v1/validate
### Overview
Check if the API key (not the APP key) is valid. If invalid, a 403 is returned.
### Response
  * [200](https://docs.datadoghq.com/api/latest/authentication/#Validate-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/authentication/#Validate-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/authentication/#Validate-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/authentication/)
  * [Example](https://docs.datadoghq.com/api/latest/authentication/)


Represent validation endpoint responses.
Expand All
Field
Type
Description
valid
boolean
Return `true` if the authentication response is valid.
```
{
  "valid": true
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/authentication/)
  * [Example](https://docs.datadoghq.com/api/latest/authentication/)


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
  * [Model](https://docs.datadoghq.com/api/latest/authentication/)
  * [Example](https://docs.datadoghq.com/api/latest/authentication/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/authentication/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/authentication/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/authentication/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/authentication/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/authentication/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/authentication/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/authentication/?code-lang=typescript)


#####  Validate API key
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/validate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}"  

                
```

#####  Validate API key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"


```

#####  Validate API key
```
# Validate API key returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AuthenticationAPI.new
p api_instance.validate()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Validate API key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"


```

#####  Validate API key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"


```

#####  Validate API key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run


```

#####  Validate API key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=76592dc0-8f68-4f6f-bb88-deaea1f8857a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=bd7b4083-acf3-4486-9141-73bb34aed41a&pt=Authentication&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fauthentication%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=76592dc0-8f68-4f6f-bb88-deaea1f8857a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=bd7b4083-acf3-4486-9141-73bb34aed41a&pt=Authentication&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fauthentication%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=b7fb8d81-b6ba-4547-a82a-aacd1c89087a&bo=2&sid=d872ad90f0be11f08643b917bdf1bf9a&vid=d8733b60f0be11f081df2b1decc9a94d&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Authentication&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fauthentication%2F&r=&lt=1132&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=667086)
