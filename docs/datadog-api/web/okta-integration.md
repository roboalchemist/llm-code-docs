# Source: https://docs.datadoghq.com/api/latest/okta-integration/

# Okta Integration
Configure your [Datadog Okta integration](https://docs.datadoghq.com/integrations/okta/) directly through the Datadog API.
## [List Okta accounts](https://docs.datadoghq.com/api/latest/okta-integration/#list-okta-accounts)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/okta-integration/#list-okta-accounts-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/okta/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/okta/accountshttps://api.datadoghq.eu/api/v2/integrations/okta/accountshttps://api.ddog-gov.com/api/v2/integrations/okta/accountshttps://api.datadoghq.com/api/v2/integrations/okta/accountshttps://api.us3.datadoghq.com/api/v2/integrations/okta/accountshttps://api.us5.datadoghq.com/api/v2/integrations/okta/accounts
### Overview
List Okta accounts. This endpoint requires the `integrations_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/okta-integration/#ListOktaAccounts-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/okta-integration/#ListOktaAccounts-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/okta-integration/#ListOktaAccounts-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/okta-integration/#ListOktaAccounts-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/okta-integration/#ListOktaAccounts-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


The expected response schema when getting Okta accounts.
Field
Type
Description
data
[object]
List of Okta accounts.
attributes [_required_]
object
Attributes object for an Okta account.
api_key
string
The API key of the Okta account.
auth_method [_required_]
string
The authorization method for an Okta account.
client_id
string
The Client ID of an Okta app integration.
client_secret
string
The client secret of an Okta app integration.
domain [_required_]
string
The domain of the Okta account.
name [_required_]
string
The name of the Okta account.
id [_required_]
string
The ID of the Okta account, a UUID hash of the account name.
type [_required_]
enum
Account type for an Okta account. Allowed enum values: `okta-accounts`
default: `okta-accounts`
```
{
  "data": [
    {
      "attributes": {
        "api_key": "string",
        "auth_method": "oauth",
        "client_id": "string",
        "client_secret": "string",
        "domain": "https://example.okta.com/",
        "name": "Okta-Prod"
      },
      "id": "f749daaf-682e-4208-a38d-c9b43162c609",
      "type": "okta-accounts"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=typescript)


#####  List Okta accounts
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Okta accounts
```
"""
List Okta accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.list_okta_accounts()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Okta accounts
```
# List Okta accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new
p api_instance.list_okta_accounts()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Okta accounts
```
// List Okta accounts returns "OK" response

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
	api := datadogV2.NewOktaIntegrationApi(apiClient)
	resp, r, err := api.ListOktaAccounts(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OktaIntegrationApi.ListOktaAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OktaIntegrationApi.ListOktaAccounts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Okta accounts
```
// List Okta accounts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OktaIntegrationApi;
import com.datadog.api.client.v2.model.OktaAccountsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OktaIntegrationApi apiInstance = new OktaIntegrationApi(defaultClient);

    try {
      OktaAccountsResponse result = apiInstance.listOktaAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OktaIntegrationApi#listOktaAccounts");
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

#####  List Okta accounts
```
// List Okta accounts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_okta_integration::OktaIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OktaIntegrationAPI::with_config(configuration);
    let resp = api.list_okta_accounts().await;
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

#####  List Okta accounts
```
/**
 * List Okta accounts returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OktaIntegrationApi(configuration);

apiInstance
  .listOktaAccounts()
  .then((data: v2.OktaAccountsResponse) => {
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
## [Add Okta account](https://docs.datadoghq.com/api/latest/okta-integration/#add-okta-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/okta-integration/#add-okta-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/integrations/okta/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/okta/accountshttps://api.datadoghq.eu/api/v2/integrations/okta/accountshttps://api.ddog-gov.com/api/v2/integrations/okta/accountshttps://api.datadoghq.com/api/v2/integrations/okta/accountshttps://api.us3.datadoghq.com/api/v2/integrations/okta/accountshttps://api.us5.datadoghq.com/api/v2/integrations/okta/accounts
### Overview
Create an Okta account. This endpoint requires the `manage_integrations` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


Field
Type
Description
data [_required_]
object
Schema for an Okta account.
attributes [_required_]
object
Attributes object for an Okta account.
api_key
string
The API key of the Okta account.
auth_method [_required_]
string
The authorization method for an Okta account.
client_id
string
The Client ID of an Okta app integration.
client_secret
string
The client secret of an Okta app integration.
domain [_required_]
string
The domain of the Okta account.
name [_required_]
string
The name of the Okta account.
id
string
The ID of the Okta account, a UUID hash of the account name.
type [_required_]
enum
Account type for an Okta account. Allowed enum values: `okta-accounts`
default: `okta-accounts`
```
{
  "data": {
    "attributes": {
      "auth_method": "oauth",
      "domain": "https://example.okta.com/",
      "name": "exampleoktaintegration",
      "client_id": "client_id",
      "client_secret": "client_secret"
    },
    "id": "f749daaf-682e-4208-a38d-c9b43162c609",
    "type": "okta-accounts"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/okta-integration/#CreateOktaAccount-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/okta-integration/#CreateOktaAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/okta-integration/#CreateOktaAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/okta-integration/#CreateOktaAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/okta-integration/#CreateOktaAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


Response object for an Okta account.
Field
Type
Description
data
object
Schema for an Okta account.
attributes [_required_]
object
Attributes object for an Okta account.
api_key
string
The API key of the Okta account.
auth_method [_required_]
string
The authorization method for an Okta account.
client_id
string
The Client ID of an Okta app integration.
client_secret
string
The client secret of an Okta app integration.
domain [_required_]
string
The domain of the Okta account.
name [_required_]
string
The name of the Okta account.
id
string
The ID of the Okta account, a UUID hash of the account name.
type [_required_]
enum
Account type for an Okta account. Allowed enum values: `okta-accounts`
default: `okta-accounts`
```
{
  "data": {
    "attributes": {
      "api_key": "string",
      "auth_method": "oauth",
      "client_id": "string",
      "client_secret": "string",
      "domain": "https://example.okta.com/",
      "name": "Okta-Prod"
    },
    "id": "f749daaf-682e-4208-a38d-c9b43162c609",
    "type": "okta-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=typescript)


#####  Add Okta account returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "auth_method": "oauth",
      "domain": "https://example.okta.com/",
      "name": "exampleoktaintegration",
      "client_id": "client_id",
      "client_secret": "client_secret"
    },
    "id": "f749daaf-682e-4208-a38d-c9b43162c609",
    "type": "okta-accounts"
  }
}
EOF  

                        
```

#####  Add Okta account returns "OK" response
```
// Add Okta account returns "OK" response

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
	body := datadogV2.OktaAccountRequest{
		Data: datadogV2.OktaAccount{
			Attributes: datadogV2.OktaAccountAttributes{
				AuthMethod:   "oauth",
				Domain:       "https://example.okta.com/",
				Name:         "exampleoktaintegration",
				ClientId:     datadog.PtrString("client_id"),
				ClientSecret: datadog.PtrString("client_secret"),
			},
			Id:   datadog.PtrString("f749daaf-682e-4208-a38d-c9b43162c609"),
			Type: datadogV2.OKTAACCOUNTTYPE_OKTA_ACCOUNTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOktaIntegrationApi(apiClient)
	resp, r, err := api.CreateOktaAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OktaIntegrationApi.CreateOktaAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OktaIntegrationApi.CreateOktaAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add Okta account returns "OK" response
```
// Add Okta account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OktaIntegrationApi;
import com.datadog.api.client.v2.model.OktaAccount;
import com.datadog.api.client.v2.model.OktaAccountAttributes;
import com.datadog.api.client.v2.model.OktaAccountRequest;
import com.datadog.api.client.v2.model.OktaAccountResponse;
import com.datadog.api.client.v2.model.OktaAccountType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OktaIntegrationApi apiInstance = new OktaIntegrationApi(defaultClient);

    OktaAccountRequest body =
        new OktaAccountRequest()
            .data(
                new OktaAccount()
                    .attributes(
                        new OktaAccountAttributes()
                            .authMethod("oauth")
                            .domain("https://example.okta.com/")
                            .name("exampleoktaintegration")
                            .clientId("client_id")
                            .clientSecret("client_secret"))
                    .id("f749daaf-682e-4208-a38d-c9b43162c609")
                    .type(OktaAccountType.OKTA_ACCOUNTS));

    try {
      OktaAccountResponse result = apiInstance.createOktaAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OktaIntegrationApi#createOktaAccount");
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

#####  Add Okta account returns "OK" response
```
"""
Add Okta account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi
from datadog_api_client.v2.model.okta_account import OktaAccount
from datadog_api_client.v2.model.okta_account_attributes import OktaAccountAttributes
from datadog_api_client.v2.model.okta_account_request import OktaAccountRequest
from datadog_api_client.v2.model.okta_account_type import OktaAccountType

body = OktaAccountRequest(
    data=OktaAccount(
        attributes=OktaAccountAttributes(
            auth_method="oauth",
            domain="https://example.okta.com/",
            name="exampleoktaintegration",
            client_id="client_id",
            client_secret="client_secret",
        ),
        id="f749daaf-682e-4208-a38d-c9b43162c609",
        type=OktaAccountType.OKTA_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.create_okta_account(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add Okta account returns "OK" response
```
# Add Okta account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new

body = DatadogAPIClient::V2::OktaAccountRequest.new({
  data: DatadogAPIClient::V2::OktaAccount.new({
    attributes: DatadogAPIClient::V2::OktaAccountAttributes.new({
      auth_method: "oauth",
      domain: "https://example.okta.com/",
      name: "exampleoktaintegration",
      client_id: "client_id",
      client_secret: "client_secret",
    }),
    id: "f749daaf-682e-4208-a38d-c9b43162c609",
    type: DatadogAPIClient::V2::OktaAccountType::OKTA_ACCOUNTS,
  }),
})
p api_instance.create_okta_account(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add Okta account returns "OK" response
```
// Add Okta account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_okta_integration::OktaIntegrationAPI;
use datadog_api_client::datadogV2::model::OktaAccount;
use datadog_api_client::datadogV2::model::OktaAccountAttributes;
use datadog_api_client::datadogV2::model::OktaAccountRequest;
use datadog_api_client::datadogV2::model::OktaAccountType;

#[tokio::main]
async fn main() {
    let body = OktaAccountRequest::new(
        OktaAccount::new(
            OktaAccountAttributes::new(
                "oauth".to_string(),
                "https://example.okta.com/".to_string(),
                "exampleoktaintegration".to_string(),
            )
            .client_id("client_id".to_string())
            .client_secret("client_secret".to_string()),
            OktaAccountType::OKTA_ACCOUNTS,
        )
        .id("f749daaf-682e-4208-a38d-c9b43162c609".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = OktaIntegrationAPI::with_config(configuration);
    let resp = api.create_okta_account(body).await;
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

#####  Add Okta account returns "OK" response
```
/**
 * Add Okta account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OktaIntegrationApi(configuration);

const params: v2.OktaIntegrationApiCreateOktaAccountRequest = {
  body: {
    data: {
      attributes: {
        authMethod: "oauth",
        domain: "https://example.okta.com/",
        name: "exampleoktaintegration",
        clientId: "client_id",
        clientSecret: "client_secret",
      },
      id: "f749daaf-682e-4208-a38d-c9b43162c609",
      type: "okta-accounts",
    },
  },
};

apiInstance
  .createOktaAccount(params)
  .then((data: v2.OktaAccountResponse) => {
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
## [Get Okta account](https://docs.datadoghq.com/api/latest/okta-integration/#get-okta-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/okta-integration/#get-okta-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/okta/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/okta/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}
### Overview
Get an Okta account. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/okta-integration/#GetOktaAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/okta-integration/#GetOktaAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/okta-integration/#GetOktaAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/okta-integration/#GetOktaAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/okta-integration/#GetOktaAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


Response object for an Okta account.
Field
Type
Description
data
object
Schema for an Okta account.
attributes [_required_]
object
Attributes object for an Okta account.
api_key
string
The API key of the Okta account.
auth_method [_required_]
string
The authorization method for an Okta account.
client_id
string
The Client ID of an Okta app integration.
client_secret
string
The client secret of an Okta app integration.
domain [_required_]
string
The domain of the Okta account.
name [_required_]
string
The name of the Okta account.
id
string
The ID of the Okta account, a UUID hash of the account name.
type [_required_]
enum
Account type for an Okta account. Allowed enum values: `okta-accounts`
default: `okta-accounts`
```
{
  "data": {
    "attributes": {
      "api_key": "string",
      "auth_method": "oauth",
      "client_id": "string",
      "client_secret": "string",
      "domain": "https://example.okta.com/",
      "name": "Okta-Prod"
    },
    "id": "f749daaf-682e-4208-a38d-c9b43162c609",
    "type": "okta-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=typescript)


#####  Get Okta account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Okta account
```
"""
Get Okta account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi

# there is a valid "okta_account" in the system
OKTA_ACCOUNT_DATA_ID = environ["OKTA_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.get_okta_account(
        account_id=OKTA_ACCOUNT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get Okta account
```
# Get Okta account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new

# there is a valid "okta_account" in the system
OKTA_ACCOUNT_DATA_ID = ENV["OKTA_ACCOUNT_DATA_ID"]
p api_instance.get_okta_account(OKTA_ACCOUNT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get Okta account
```
// Get Okta account returns "OK" response

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
	// there is a valid "okta_account" in the system
	OktaAccountDataID := os.Getenv("OKTA_ACCOUNT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOktaIntegrationApi(apiClient)
	resp, r, err := api.GetOktaAccount(ctx, OktaAccountDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OktaIntegrationApi.GetOktaAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OktaIntegrationApi.GetOktaAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get Okta account
```
// Get Okta account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OktaIntegrationApi;
import com.datadog.api.client.v2.model.OktaAccountResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OktaIntegrationApi apiInstance = new OktaIntegrationApi(defaultClient);

    // there is a valid "okta_account" in the system
    String OKTA_ACCOUNT_DATA_ID = System.getenv("OKTA_ACCOUNT_DATA_ID");

    try {
      OktaAccountResponse result = apiInstance.getOktaAccount(OKTA_ACCOUNT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OktaIntegrationApi#getOktaAccount");
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

#####  Get Okta account
```
// Get Okta account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_okta_integration::OktaIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "okta_account" in the system
    let okta_account_data_id = std::env::var("OKTA_ACCOUNT_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OktaIntegrationAPI::with_config(configuration);
    let resp = api.get_okta_account(okta_account_data_id.clone()).await;
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

#####  Get Okta account
```
/**
 * Get Okta account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OktaIntegrationApi(configuration);

// there is a valid "okta_account" in the system
const OKTA_ACCOUNT_DATA_ID = process.env.OKTA_ACCOUNT_DATA_ID as string;

const params: v2.OktaIntegrationApiGetOktaAccountRequest = {
  accountId: OKTA_ACCOUNT_DATA_ID,
};

apiInstance
  .getOktaAccount(params)
  .then((data: v2.OktaAccountResponse) => {
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
## [Update Okta account](https://docs.datadoghq.com/api/latest/okta-integration/#update-okta-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/okta-integration/#update-okta-account-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/okta/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/okta/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}
### Overview
Update an Okta account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


Field
Type
Description
data [_required_]
object
Data object for updating an Okta account.
attributes
object
Attributes object for updating an Okta account.
api_key
string
The API key of the Okta account.
auth_method [_required_]
string
The authorization method for an Okta account.
client_id
string
The Client ID of an Okta app integration.
client_secret
string
The client secret of an Okta app integration.
domain [_required_]
string
The domain associated with an Okta account.
type
enum
Account type for an Okta account. Allowed enum values: `okta-accounts`
default: `okta-accounts`
```
{
  "data": {
    "attributes": {
      "auth_method": "oauth",
      "domain": "https://example.okta.com/",
      "client_id": "client_id",
      "client_secret": "client_secret"
    },
    "type": "okta-accounts"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/okta-integration/#UpdateOktaAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/okta-integration/#UpdateOktaAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/okta-integration/#UpdateOktaAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/okta-integration/#UpdateOktaAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/okta-integration/#UpdateOktaAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


Response object for an Okta account.
Field
Type
Description
data
object
Schema for an Okta account.
attributes [_required_]
object
Attributes object for an Okta account.
api_key
string
The API key of the Okta account.
auth_method [_required_]
string
The authorization method for an Okta account.
client_id
string
The Client ID of an Okta app integration.
client_secret
string
The client secret of an Okta app integration.
domain [_required_]
string
The domain of the Okta account.
name [_required_]
string
The name of the Okta account.
id
string
The ID of the Okta account, a UUID hash of the account name.
type [_required_]
enum
Account type for an Okta account. Allowed enum values: `okta-accounts`
default: `okta-accounts`
```
{
  "data": {
    "attributes": {
      "api_key": "string",
      "auth_method": "oauth",
      "client_id": "string",
      "client_secret": "string",
      "domain": "https://example.okta.com/",
      "name": "Okta-Prod"
    },
    "id": "f749daaf-682e-4208-a38d-c9b43162c609",
    "type": "okta-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=typescript)


#####  Update Okta account returns "OK" response
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/${account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "auth_method": "oauth",
      "domain": "https://example.okta.com/",
      "client_id": "client_id",
      "client_secret": "client_secret"
    },
    "type": "okta-accounts"
  }
}
EOF  

                        
```

#####  Update Okta account returns "OK" response
```
// Update Okta account returns "OK" response

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
	// there is a valid "okta_account" in the system
	OktaAccountDataID := os.Getenv("OKTA_ACCOUNT_DATA_ID")

	body := datadogV2.OktaAccountUpdateRequest{
		Data: datadogV2.OktaAccountUpdateRequestData{
			Attributes: &datadogV2.OktaAccountUpdateRequestAttributes{
				AuthMethod:   "oauth",
				Domain:       "https://example.okta.com/",
				ClientId:     datadog.PtrString("client_id"),
				ClientSecret: datadog.PtrString("client_secret"),
			},
			Type: datadogV2.OKTAACCOUNTTYPE_OKTA_ACCOUNTS.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOktaIntegrationApi(apiClient)
	resp, r, err := api.UpdateOktaAccount(ctx, OktaAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OktaIntegrationApi.UpdateOktaAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OktaIntegrationApi.UpdateOktaAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update Okta account returns "OK" response
```
// Update Okta account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OktaIntegrationApi;
import com.datadog.api.client.v2.model.OktaAccountResponse;
import com.datadog.api.client.v2.model.OktaAccountType;
import com.datadog.api.client.v2.model.OktaAccountUpdateRequest;
import com.datadog.api.client.v2.model.OktaAccountUpdateRequestAttributes;
import com.datadog.api.client.v2.model.OktaAccountUpdateRequestData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OktaIntegrationApi apiInstance = new OktaIntegrationApi(defaultClient);

    // there is a valid "okta_account" in the system
    String OKTA_ACCOUNT_DATA_ID = System.getenv("OKTA_ACCOUNT_DATA_ID");

    OktaAccountUpdateRequest body =
        new OktaAccountUpdateRequest()
            .data(
                new OktaAccountUpdateRequestData()
                    .attributes(
                        new OktaAccountUpdateRequestAttributes()
                            .authMethod("oauth")
                            .domain("https://example.okta.com/")
                            .clientId("client_id")
                            .clientSecret("client_secret"))
                    .type(OktaAccountType.OKTA_ACCOUNTS));

    try {
      OktaAccountResponse result = apiInstance.updateOktaAccount(OKTA_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OktaIntegrationApi#updateOktaAccount");
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

#####  Update Okta account returns "OK" response
```
"""
Update Okta account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi
from datadog_api_client.v2.model.okta_account_type import OktaAccountType
from datadog_api_client.v2.model.okta_account_update_request import OktaAccountUpdateRequest
from datadog_api_client.v2.model.okta_account_update_request_attributes import OktaAccountUpdateRequestAttributes
from datadog_api_client.v2.model.okta_account_update_request_data import OktaAccountUpdateRequestData

# there is a valid "okta_account" in the system
OKTA_ACCOUNT_DATA_ID = environ["OKTA_ACCOUNT_DATA_ID"]

body = OktaAccountUpdateRequest(
    data=OktaAccountUpdateRequestData(
        attributes=OktaAccountUpdateRequestAttributes(
            auth_method="oauth",
            domain="https://example.okta.com/",
            client_id="client_id",
            client_secret="client_secret",
        ),
        type=OktaAccountType.OKTA_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.update_okta_account(account_id=OKTA_ACCOUNT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update Okta account returns "OK" response
```
# Update Okta account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new

# there is a valid "okta_account" in the system
OKTA_ACCOUNT_DATA_ID = ENV["OKTA_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::OktaAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::OktaAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::OktaAccountUpdateRequestAttributes.new({
      auth_method: "oauth",
      domain: "https://example.okta.com/",
      client_id: "client_id",
      client_secret: "client_secret",
    }),
    type: DatadogAPIClient::V2::OktaAccountType::OKTA_ACCOUNTS,
  }),
})
p api_instance.update_okta_account(OKTA_ACCOUNT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update Okta account returns "OK" response
```
// Update Okta account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_okta_integration::OktaIntegrationAPI;
use datadog_api_client::datadogV2::model::OktaAccountType;
use datadog_api_client::datadogV2::model::OktaAccountUpdateRequest;
use datadog_api_client::datadogV2::model::OktaAccountUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::OktaAccountUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "okta_account" in the system
    let okta_account_data_id = std::env::var("OKTA_ACCOUNT_DATA_ID").unwrap();
    let body = OktaAccountUpdateRequest::new(
        OktaAccountUpdateRequestData::new()
            .attributes(
                OktaAccountUpdateRequestAttributes::new(
                    "oauth".to_string(),
                    "https://example.okta.com/".to_string(),
                )
                .client_id("client_id".to_string())
                .client_secret("client_secret".to_string()),
            )
            .type_(OktaAccountType::OKTA_ACCOUNTS),
    );
    let configuration = datadog::Configuration::new();
    let api = OktaIntegrationAPI::with_config(configuration);
    let resp = api
        .update_okta_account(okta_account_data_id.clone(), body)
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

#####  Update Okta account returns "OK" response
```
/**
 * Update Okta account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OktaIntegrationApi(configuration);

// there is a valid "okta_account" in the system
const OKTA_ACCOUNT_DATA_ID = process.env.OKTA_ACCOUNT_DATA_ID as string;

const params: v2.OktaIntegrationApiUpdateOktaAccountRequest = {
  body: {
    data: {
      attributes: {
        authMethod: "oauth",
        domain: "https://example.okta.com/",
        clientId: "client_id",
        clientSecret: "client_secret",
      },
      type: "okta-accounts",
    },
  },
  accountId: OKTA_ACCOUNT_DATA_ID,
};

apiInstance
  .updateOktaAccount(params)
  .then((data: v2.OktaAccountResponse) => {
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
## [Delete Okta account](https://docs.datadoghq.com/api/latest/okta-integration/#delete-okta-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/okta-integration/#delete-okta-account-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/okta/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/okta/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}
### Overview
Delete an Okta account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/okta-integration/#DeleteOktaAccount-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/okta-integration/#DeleteOktaAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/okta-integration/#DeleteOktaAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/okta-integration/#DeleteOktaAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/okta-integration/#DeleteOktaAccount-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/okta-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/okta-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/okta-integration/?code-lang=typescript)


#####  Delete Okta account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete Okta account
```
"""
Delete Okta account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    api_instance.delete_okta_account(
        account_id="account_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete Okta account
```
# Delete Okta account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new
api_instance.delete_okta_account("account_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete Okta account
```
// Delete Okta account returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOktaIntegrationApi(apiClient)
	r, err := api.DeleteOktaAccount(ctx, "account_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OktaIntegrationApi.DeleteOktaAccount`: %v\n", err)
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

#####  Delete Okta account
```
// Delete Okta account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OktaIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OktaIntegrationApi apiInstance = new OktaIntegrationApi(defaultClient);

    try {
      apiInstance.deleteOktaAccount("account_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling OktaIntegrationApi#deleteOktaAccount");
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

#####  Delete Okta account
```
// Delete Okta account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_okta_integration::OktaIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OktaIntegrationAPI::with_config(configuration);
    let resp = api.delete_okta_account("account_id".to_string()).await;
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

#####  Delete Okta account
```
/**
 * Delete Okta account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OktaIntegrationApi(configuration);

const params: v2.OktaIntegrationApiDeleteOktaAccountRequest = {
  accountId: "account_id",
};

apiInstance
  .deleteOktaAccount(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b3a691cb-da21-4dd7-80fe-912a5e780a3d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=caf6489a-3627-4cda-88a6-bc374ed8d81d&pt=Okta%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fokta-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b3a691cb-da21-4dd7-80fe-912a5e780a3d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=caf6489a-3627-4cda-88a6-bc374ed8d81d&pt=Okta%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fokta-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=d61d8f36-d8a3-4d42-88b2-57f86ddce2e4&bo=2&sid=3d8da700f0c011f0b447d932ca871b75&vid=3d8dcb40f0c011f095171bdc3f922644&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Okta%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fokta-integration%2F&r=&lt=1174&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=80503)
