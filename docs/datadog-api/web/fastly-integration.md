# Source: https://docs.datadoghq.com/api/latest/fastly-integration/

# Fastly Integration
Manage your Datadog Fastly integration accounts and services directly through the Datadog API. See the [Fastly integration page](https://docs.datadoghq.com/integrations/fastly/) for more information.
## [List Fastly accounts](https://docs.datadoghq.com/api/latest/fastly-integration/#list-fastly-accounts)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#list-fastly-accounts-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.datadoghq.eu/api/v2/integrations/fastly/accountshttps://api.ddog-gov.com/api/v2/integrations/fastly/accountshttps://api.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.us3.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts
### Overview
List Fastly accounts. This endpoint requires the `integrations_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyAccounts-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyAccounts-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyAccounts-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyAccounts-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyAccounts-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting Fastly accounts.
Field
Type
Description
data
[object]
The JSON:API data schema.
attributes [_required_]
object
Attributes object of a Fastly account.
name [_required_]
string
The name of the Fastly account.
services
[object]
A list of services belonging to the parent account.
id [_required_]
string
The ID of the Fastly service
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts`
default: `fastly-accounts`
```
{
  "data": [
    {
      "attributes": {
        "name": "test-name",
        "services": [
          {
            "id": "6abc7de6893AbcDe9fghIj",
            "tags": [
              "myTag",
              "myTag2:myValue"
            ]
          }
        ]
      },
      "id": "abc123",
      "type": "fastly-accounts"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  List Fastly accounts
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Fastly accounts
```
"""
List Fastly accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.list_fastly_accounts()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Fastly accounts
```
# List Fastly accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
p api_instance.list_fastly_accounts()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Fastly accounts
```
// List Fastly accounts returns "OK" response

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
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.ListFastlyAccounts(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.ListFastlyAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.ListFastlyAccounts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Fastly accounts
```
// List Fastly accounts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyAccountsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    try {
      FastlyAccountsResponse result = apiInstance.listFastlyAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#listFastlyAccounts");
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

#####  List Fastly accounts
```
// List Fastly accounts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api.list_fastly_accounts().await;
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

#####  List Fastly accounts
```
/**
 * List Fastly accounts returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

apiInstance
  .listFastlyAccounts()
  .then((data: v2.FastlyAccountsResponse) => {
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
## [Add Fastly account](https://docs.datadoghq.com/api/latest/fastly-integration/#add-fastly-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#add-fastly-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.datadoghq.eu/api/v2/integrations/fastly/accountshttps://api.ddog-gov.com/api/v2/integrations/fastly/accountshttps://api.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.us3.datadoghq.com/api/v2/integrations/fastly/accountshttps://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts
### Overview
Create a Fastly account. This endpoint requires the `manage_integrations` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


Field
Type
Description
data [_required_]
object
Data object for creating a Fastly account.
attributes [_required_]
object
Attributes object for creating a Fastly account.
api_key [_required_]
string
The API key for the Fastly account.
name [_required_]
string
The name of the Fastly account.
services
[object]
A list of services belonging to the parent account.
id [_required_]
string
The ID of the Fastly service
tags
[string]
A list of tags for the Fastly service.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts`
default: `fastly-accounts`
```
{
  "data": {
    "attributes": {
      "api_key": "ExampleFastlyIntegration",
      "name": "Example-Fastly-Integration",
      "services": []
    },
    "type": "fastly-accounts"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyAccount-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyAccount-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting a Fastly account.
Field
Type
Description
data
object
Data object of a Fastly account.
attributes [_required_]
object
Attributes object of a Fastly account.
name [_required_]
string
The name of the Fastly account.
services
[object]
A list of services belonging to the parent account.
id [_required_]
string
The ID of the Fastly service
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts`
default: `fastly-accounts`
```
{
  "data": {
    "attributes": {
      "name": "test-name",
      "services": [
        {
          "id": "6abc7de6893AbcDe9fghIj",
          "tags": [
            "myTag",
            "myTag2:myValue"
          ]
        }
      ]
    },
    "id": "abc123",
    "type": "fastly-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Add Fastly account returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "api_key": "ExampleFastlyIntegration",
      "name": "Example-Fastly-Integration",
      "services": []
    },
    "type": "fastly-accounts"
  }
}
EOF  

                        
```

#####  Add Fastly account returns "CREATED" response
```
// Add Fastly account returns "CREATED" response

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
	body := datadogV2.FastlyAccountCreateRequest{
		Data: datadogV2.FastlyAccountCreateRequestData{
			Attributes: datadogV2.FastlyAccountCreateRequestAttributes{
				ApiKey:   "ExampleFastlyIntegration",
				Name:     "Example-Fastly-Integration",
				Services: []datadogV2.FastlyService{},
			},
			Type: datadogV2.FASTLYACCOUNTTYPE_FASTLY_ACCOUNTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.CreateFastlyAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.CreateFastlyAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.CreateFastlyAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add Fastly account returns "CREATED" response
```
// Add Fastly account returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyAccountCreateRequest;
import com.datadog.api.client.v2.model.FastlyAccountCreateRequestAttributes;
import com.datadog.api.client.v2.model.FastlyAccountCreateRequestData;
import com.datadog.api.client.v2.model.FastlyAccountResponse;
import com.datadog.api.client.v2.model.FastlyAccountType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    FastlyAccountCreateRequest body =
        new FastlyAccountCreateRequest()
            .data(
                new FastlyAccountCreateRequestData()
                    .attributes(
                        new FastlyAccountCreateRequestAttributes()
                            .apiKey("ExampleFastlyIntegration")
                            .name("Example-Fastly-Integration"))
                    .type(FastlyAccountType.FASTLY_ACCOUNTS));

    try {
      FastlyAccountResponse result = apiInstance.createFastlyAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#createFastlyAccount");
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

#####  Add Fastly account returns "CREATED" response
```
"""
Add Fastly account returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_account_create_request import FastlyAccountCreateRequest
from datadog_api_client.v2.model.fastly_account_create_request_attributes import FastlyAccountCreateRequestAttributes
from datadog_api_client.v2.model.fastly_account_create_request_data import FastlyAccountCreateRequestData
from datadog_api_client.v2.model.fastly_account_type import FastlyAccountType

body = FastlyAccountCreateRequest(
    data=FastlyAccountCreateRequestData(
        attributes=FastlyAccountCreateRequestAttributes(
            api_key="ExampleFastlyIntegration",
            name="Example-Fastly-Integration",
            services=[],
        ),
        type=FastlyAccountType.FASTLY_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.create_fastly_account(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add Fastly account returns "CREATED" response
```
# Add Fastly account returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new

body = DatadogAPIClient::V2::FastlyAccountCreateRequest.new({
  data: DatadogAPIClient::V2::FastlyAccountCreateRequestData.new({
    attributes: DatadogAPIClient::V2::FastlyAccountCreateRequestAttributes.new({
      api_key: "ExampleFastlyIntegration",
      name: "Example-Fastly-Integration",
      services: [],
    }),
    type: DatadogAPIClient::V2::FastlyAccountType::FASTLY_ACCOUNTS,
  }),
})
p api_instance.create_fastly_account(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add Fastly account returns "CREATED" response
```
// Add Fastly account returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;
use datadog_api_client::datadogV2::model::FastlyAccountCreateRequest;
use datadog_api_client::datadogV2::model::FastlyAccountCreateRequestAttributes;
use datadog_api_client::datadogV2::model::FastlyAccountCreateRequestData;
use datadog_api_client::datadogV2::model::FastlyAccountType;

#[tokio::main]
async fn main() {
    let body = FastlyAccountCreateRequest::new(FastlyAccountCreateRequestData::new(
        FastlyAccountCreateRequestAttributes::new(
            "ExampleFastlyIntegration".to_string(),
            "Example-Fastly-Integration".to_string(),
        )
        .services(vec![]),
        FastlyAccountType::FASTLY_ACCOUNTS,
    ));
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api.create_fastly_account(body).await;
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

#####  Add Fastly account returns "CREATED" response
```
/**
 * Add Fastly account returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

const params: v2.FastlyIntegrationApiCreateFastlyAccountRequest = {
  body: {
    data: {
      attributes: {
        apiKey: "ExampleFastlyIntegration",
        name: "Example-Fastly-Integration",
        services: [],
      },
      type: "fastly-accounts",
    },
  },
};

apiInstance
  .createFastlyAccount(params)
  .then((data: v2.FastlyAccountResponse) => {
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
## [Get Fastly account](https://docs.datadoghq.com/api/latest/fastly-integration/#get-fastly-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#get-fastly-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}
### Overview
Get a Fastly account. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
### Response
  * [200](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting a Fastly account.
Field
Type
Description
data
object
Data object of a Fastly account.
attributes [_required_]
object
Attributes object of a Fastly account.
name [_required_]
string
The name of the Fastly account.
services
[object]
A list of services belonging to the parent account.
id [_required_]
string
The ID of the Fastly service
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts`
default: `fastly-accounts`
```
{
  "data": {
    "attributes": {
      "name": "test-name",
      "services": [
        {
          "id": "6abc7de6893AbcDe9fghIj",
          "tags": [
            "myTag",
            "myTag2:myValue"
          ]
        }
      ]
    },
    "id": "abc123",
    "type": "fastly-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Get Fastly account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Fastly account
```
"""
Get Fastly account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

# there is a valid "fastly_account" in the system
FASTLY_ACCOUNT_DATA_ID = environ["FASTLY_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.get_fastly_account(
        account_id=FASTLY_ACCOUNT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get Fastly account
```
# Get Fastly account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new

# there is a valid "fastly_account" in the system
FASTLY_ACCOUNT_DATA_ID = ENV["FASTLY_ACCOUNT_DATA_ID"]
p api_instance.get_fastly_account(FASTLY_ACCOUNT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get Fastly account
```
// Get Fastly account returns "OK" response

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
	// there is a valid "fastly_account" in the system
	FastlyAccountDataID := os.Getenv("FASTLY_ACCOUNT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.GetFastlyAccount(ctx, FastlyAccountDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.GetFastlyAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.GetFastlyAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get Fastly account
```
// Get Fastly account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyAccountResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    // there is a valid "fastly_account" in the system
    String FASTLY_ACCOUNT_DATA_ID = System.getenv("FASTLY_ACCOUNT_DATA_ID");

    try {
      FastlyAccountResponse result = apiInstance.getFastlyAccount(FASTLY_ACCOUNT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#getFastlyAccount");
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

#####  Get Fastly account
```
// Get Fastly account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "fastly_account" in the system
    let fastly_account_data_id = std::env::var("FASTLY_ACCOUNT_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api.get_fastly_account(fastly_account_data_id.clone()).await;
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

#####  Get Fastly account
```
/**
 * Get Fastly account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

// there is a valid "fastly_account" in the system
const FASTLY_ACCOUNT_DATA_ID = process.env.FASTLY_ACCOUNT_DATA_ID as string;

const params: v2.FastlyIntegrationApiGetFastlyAccountRequest = {
  accountId: FASTLY_ACCOUNT_DATA_ID,
};

apiInstance
  .getFastlyAccount(params)
  .then((data: v2.FastlyAccountResponse) => {
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
## [Update Fastly account](https://docs.datadoghq.com/api/latest/fastly-integration/#update-fastly-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#update-fastly-account-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}
### Overview
Update a Fastly account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


Field
Type
Description
data [_required_]
object
Data object for updating a Fastly account.
attributes
object
Attributes object for updating a Fastly account.
api_key
string
The API key of the Fastly account.
name
string
The name of the Fastly account.
type
enum
The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts`
default: `fastly-accounts`
```
{
  "data": {
    "attributes": {
      "api_key": "update-secret"
    },
    "type": "fastly-accounts"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting a Fastly account.
Field
Type
Description
data
object
Data object of a Fastly account.
attributes [_required_]
object
Attributes object of a Fastly account.
name [_required_]
string
The name of the Fastly account.
services
[object]
A list of services belonging to the parent account.
id [_required_]
string
The ID of the Fastly service
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts`
default: `fastly-accounts`
```
{
  "data": {
    "attributes": {
      "name": "test-name",
      "services": [
        {
          "id": "6abc7de6893AbcDe9fghIj",
          "tags": [
            "myTag",
            "myTag2:myValue"
          ]
        }
      ]
    },
    "id": "abc123",
    "type": "fastly-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Update Fastly account returns "OK" response
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "api_key": "update-secret"
    },
    "type": "fastly-accounts"
  }
}
EOF  

                        
```

#####  Update Fastly account returns "OK" response
```
// Update Fastly account returns "OK" response

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
	// there is a valid "fastly_account" in the system
	FastlyAccountDataID := os.Getenv("FASTLY_ACCOUNT_DATA_ID")

	body := datadogV2.FastlyAccountUpdateRequest{
		Data: datadogV2.FastlyAccountUpdateRequestData{
			Attributes: &datadogV2.FastlyAccountUpdateRequestAttributes{
				ApiKey: datadog.PtrString("update-secret"),
			},
			Type: datadogV2.FASTLYACCOUNTTYPE_FASTLY_ACCOUNTS.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.UpdateFastlyAccount(ctx, FastlyAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.UpdateFastlyAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.UpdateFastlyAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update Fastly account returns "OK" response
```
// Update Fastly account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyAccountResponse;
import com.datadog.api.client.v2.model.FastlyAccountType;
import com.datadog.api.client.v2.model.FastlyAccountUpdateRequest;
import com.datadog.api.client.v2.model.FastlyAccountUpdateRequestAttributes;
import com.datadog.api.client.v2.model.FastlyAccountUpdateRequestData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    // there is a valid "fastly_account" in the system
    String FASTLY_ACCOUNT_DATA_ID = System.getenv("FASTLY_ACCOUNT_DATA_ID");

    FastlyAccountUpdateRequest body =
        new FastlyAccountUpdateRequest()
            .data(
                new FastlyAccountUpdateRequestData()
                    .attributes(new FastlyAccountUpdateRequestAttributes().apiKey("update-secret"))
                    .type(FastlyAccountType.FASTLY_ACCOUNTS));

    try {
      FastlyAccountResponse result = apiInstance.updateFastlyAccount(FASTLY_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#updateFastlyAccount");
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

#####  Update Fastly account returns "OK" response
```
"""
Update Fastly account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_account_type import FastlyAccountType
from datadog_api_client.v2.model.fastly_account_update_request import FastlyAccountUpdateRequest
from datadog_api_client.v2.model.fastly_account_update_request_attributes import FastlyAccountUpdateRequestAttributes
from datadog_api_client.v2.model.fastly_account_update_request_data import FastlyAccountUpdateRequestData

# there is a valid "fastly_account" in the system
FASTLY_ACCOUNT_DATA_ID = environ["FASTLY_ACCOUNT_DATA_ID"]

body = FastlyAccountUpdateRequest(
    data=FastlyAccountUpdateRequestData(
        attributes=FastlyAccountUpdateRequestAttributes(
            api_key="update-secret",
        ),
        type=FastlyAccountType.FASTLY_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.update_fastly_account(account_id=FASTLY_ACCOUNT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update Fastly account returns "OK" response
```
# Update Fastly account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new

# there is a valid "fastly_account" in the system
FASTLY_ACCOUNT_DATA_ID = ENV["FASTLY_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::FastlyAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::FastlyAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::FastlyAccountUpdateRequestAttributes.new({
      api_key: "update-secret",
    }),
    type: DatadogAPIClient::V2::FastlyAccountType::FASTLY_ACCOUNTS,
  }),
})
p api_instance.update_fastly_account(FASTLY_ACCOUNT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update Fastly account returns "OK" response
```
// Update Fastly account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;
use datadog_api_client::datadogV2::model::FastlyAccountType;
use datadog_api_client::datadogV2::model::FastlyAccountUpdateRequest;
use datadog_api_client::datadogV2::model::FastlyAccountUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::FastlyAccountUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "fastly_account" in the system
    let fastly_account_data_id = std::env::var("FASTLY_ACCOUNT_DATA_ID").unwrap();
    let body = FastlyAccountUpdateRequest::new(
        FastlyAccountUpdateRequestData::new()
            .attributes(
                FastlyAccountUpdateRequestAttributes::new().api_key("update-secret".to_string()),
            )
            .type_(FastlyAccountType::FASTLY_ACCOUNTS),
    );
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api
        .update_fastly_account(fastly_account_data_id.clone(), body)
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

#####  Update Fastly account returns "OK" response
```
/**
 * Update Fastly account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

// there is a valid "fastly_account" in the system
const FASTLY_ACCOUNT_DATA_ID = process.env.FASTLY_ACCOUNT_DATA_ID as string;

const params: v2.FastlyIntegrationApiUpdateFastlyAccountRequest = {
  body: {
    data: {
      attributes: {
        apiKey: "update-secret",
      },
      type: "fastly-accounts",
    },
  },
  accountId: FASTLY_ACCOUNT_DATA_ID,
};

apiInstance
  .updateFastlyAccount(params)
  .then((data: v2.FastlyAccountResponse) => {
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
## [Delete Fastly account](https://docs.datadoghq.com/api/latest/fastly-integration/#delete-fastly-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#delete-fastly-account-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}
### Overview
Delete a Fastly account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
### Response
  * [204](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyAccount-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyAccount-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Delete Fastly account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete Fastly account
```
"""
Delete Fastly account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    api_instance.delete_fastly_account(
        account_id="account_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete Fastly account
```
# Delete Fastly account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
api_instance.delete_fastly_account("account_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete Fastly account
```
// Delete Fastly account returns "OK" response

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
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	r, err := api.DeleteFastlyAccount(ctx, "account_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.DeleteFastlyAccount`: %v\n", err)
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

#####  Delete Fastly account
```
// Delete Fastly account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    try {
      apiInstance.deleteFastlyAccount("account_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#deleteFastlyAccount");
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

#####  Delete Fastly account
```
// Delete Fastly account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api.delete_fastly_account("account_id".to_string()).await;
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

#####  Delete Fastly account
```
/**
 * Delete Fastly account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

const params: v2.FastlyIntegrationApiDeleteFastlyAccountRequest = {
  accountId: "account_id",
};

apiInstance
  .deleteFastlyAccount(params)
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
## [List Fastly services](https://docs.datadoghq.com/api/latest/fastly-integration/#list-fastly-services)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#list-fastly-services-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services
### Overview
List Fastly services for an account. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
### Response
  * [200](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyServices-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyServices-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyServices-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyServices-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#ListFastlyServices-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting Fastly services.
Field
Type
Description
data
[object]
The JSON:API data schema.
attributes
object
Attributes object for Fastly service requests.
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly service.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services`
default: `fastly-services`
```
{
  "data": [
    {
      "attributes": {
        "tags": [
          "myTag",
          "myTag2:myValue"
        ]
      },
      "id": "abc123",
      "type": "fastly-services"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  List Fastly services
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Fastly services
```
"""
List Fastly services returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.list_fastly_services(
        account_id="account_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Fastly services
```
# List Fastly services returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
p api_instance.list_fastly_services("account_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Fastly services
```
// List Fastly services returns "OK" response

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
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.ListFastlyServices(ctx, "account_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.ListFastlyServices`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.ListFastlyServices`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Fastly services
```
// List Fastly services returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyServicesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    try {
      FastlyServicesResponse result = apiInstance.listFastlyServices("account_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#listFastlyServices");
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

#####  List Fastly services
```
// List Fastly services returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api.list_fastly_services("account_id".to_string()).await;
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

#####  List Fastly services
```
/**
 * List Fastly services returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

const params: v2.FastlyIntegrationApiListFastlyServicesRequest = {
  accountId: "account_id",
};

apiInstance
  .listFastlyServices(params)
  .then((data: v2.FastlyServicesResponse) => {
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
## [Add Fastly service](https://docs.datadoghq.com/api/latest/fastly-integration/#add-fastly-service)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#add-fastly-service-v2)


POST https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/serviceshttps://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services
### Overview
Create a Fastly service for an account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


Field
Type
Description
data [_required_]
object
Data object for Fastly service requests.
attributes
object
Attributes object for Fastly service requests.
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly service.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services`
default: `fastly-services`
```
{
  "data": {
    "attributes": {
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "abc123",
    "type": "fastly-services"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyService-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyService-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyService-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#CreateFastlyService-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting a Fastly service.
Field
Type
Description
data
object
Data object for Fastly service requests.
attributes
object
Attributes object for Fastly service requests.
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly service.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services`
default: `fastly-services`
```
{
  "data": {
    "attributes": {
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "abc123",
    "type": "fastly-services"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Add Fastly service
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "abc123",
    "type": "fastly-services"
  }
}
EOF  

                
```

#####  Add Fastly service
```
"""
Add Fastly service returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_service_attributes import FastlyServiceAttributes
from datadog_api_client.v2.model.fastly_service_data import FastlyServiceData
from datadog_api_client.v2.model.fastly_service_request import FastlyServiceRequest
from datadog_api_client.v2.model.fastly_service_type import FastlyServiceType

body = FastlyServiceRequest(
    data=FastlyServiceData(
        attributes=FastlyServiceAttributes(
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
        id="abc123",
        type=FastlyServiceType.FASTLY_SERVICES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.create_fastly_service(account_id="account_id", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add Fastly service
```
# Add Fastly service returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new

body = DatadogAPIClient::V2::FastlyServiceRequest.new({
  data: DatadogAPIClient::V2::FastlyServiceData.new({
    attributes: DatadogAPIClient::V2::FastlyServiceAttributes.new({
      tags: [
        "myTag",
        "myTag2:myValue",
      ],
    }),
    id: "abc123",
    type: DatadogAPIClient::V2::FastlyServiceType::FASTLY_SERVICES,
  }),
})
p api_instance.create_fastly_service("account_id", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add Fastly service
```
// Add Fastly service returns "CREATED" response

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
	body := datadogV2.FastlyServiceRequest{
		Data: datadogV2.FastlyServiceData{
			Attributes: &datadogV2.FastlyServiceAttributes{
				Tags: []string{
					"myTag",
					"myTag2:myValue",
				},
			},
			Id:   "abc123",
			Type: datadogV2.FASTLYSERVICETYPE_FASTLY_SERVICES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.CreateFastlyService(ctx, "account_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.CreateFastlyService`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.CreateFastlyService`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add Fastly service
```
// Add Fastly service returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyServiceAttributes;
import com.datadog.api.client.v2.model.FastlyServiceData;
import com.datadog.api.client.v2.model.FastlyServiceRequest;
import com.datadog.api.client.v2.model.FastlyServiceResponse;
import com.datadog.api.client.v2.model.FastlyServiceType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    FastlyServiceRequest body =
        new FastlyServiceRequest()
            .data(
                new FastlyServiceData()
                    .attributes(
                        new FastlyServiceAttributes()
                            .tags(Arrays.asList("myTag", "myTag2:myValue")))
                    .id("abc123")
                    .type(FastlyServiceType.FASTLY_SERVICES));

    try {
      FastlyServiceResponse result = apiInstance.createFastlyService("account_id", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#createFastlyService");
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

#####  Add Fastly service
```
// Add Fastly service returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;
use datadog_api_client::datadogV2::model::FastlyServiceAttributes;
use datadog_api_client::datadogV2::model::FastlyServiceData;
use datadog_api_client::datadogV2::model::FastlyServiceRequest;
use datadog_api_client::datadogV2::model::FastlyServiceType;

#[tokio::main]
async fn main() {
    let body = FastlyServiceRequest::new(
        FastlyServiceData::new("abc123".to_string(), FastlyServiceType::FASTLY_SERVICES)
            .attributes(
                FastlyServiceAttributes::new()
                    .tags(vec!["myTag".to_string(), "myTag2:myValue".to_string()]),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api
        .create_fastly_service("account_id".to_string(), body)
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

#####  Add Fastly service
```
/**
 * Add Fastly service returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

const params: v2.FastlyIntegrationApiCreateFastlyServiceRequest = {
  body: {
    data: {
      attributes: {
        tags: ["myTag", "myTag2:myValue"],
      },
      id: "abc123",
      type: "fastly-services",
    },
  },
  accountId: "account_id",
};

apiInstance
  .createFastlyService(params)
  .then((data: v2.FastlyServiceResponse) => {
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
## [Get Fastly service](https://docs.datadoghq.com/api/latest/fastly-integration/#get-fastly-service)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#get-fastly-service-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}
### Overview
Get a Fastly service for an account. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
service_id [_required_]
string
Fastly Service ID.
### Response
  * [200](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyService-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyService-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyService-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#GetFastlyService-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting a Fastly service.
Field
Type
Description
data
object
Data object for Fastly service requests.
attributes
object
Attributes object for Fastly service requests.
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly service.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services`
default: `fastly-services`
```
{
  "data": {
    "attributes": {
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "abc123",
    "type": "fastly-services"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Get Fastly service
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
export service_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services/${service_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Fastly service
```
"""
Get Fastly service returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.get_fastly_service(
        account_id="account_id",
        service_id="service_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get Fastly service
```
# Get Fastly service returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
p api_instance.get_fastly_service("account_id", "service_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get Fastly service
```
// Get Fastly service returns "OK" response

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
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.GetFastlyService(ctx, "account_id", "service_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.GetFastlyService`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.GetFastlyService`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get Fastly service
```
// Get Fastly service returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyServiceResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    try {
      FastlyServiceResponse result = apiInstance.getFastlyService("account_id", "service_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#getFastlyService");
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

#####  Get Fastly service
```
// Get Fastly service returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api
        .get_fastly_service("account_id".to_string(), "service_id".to_string())
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

#####  Get Fastly service
```
/**
 * Get Fastly service returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

const params: v2.FastlyIntegrationApiGetFastlyServiceRequest = {
  accountId: "account_id",
  serviceId: "service_id",
};

apiInstance
  .getFastlyService(params)
  .then((data: v2.FastlyServiceResponse) => {
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
## [Update Fastly service](https://docs.datadoghq.com/api/latest/fastly-integration/#update-fastly-service)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#update-fastly-service-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}
### Overview
Update a Fastly service for an account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
service_id [_required_]
string
Fastly Service ID.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


Field
Type
Description
data [_required_]
object
Data object for Fastly service requests.
attributes
object
Attributes object for Fastly service requests.
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly service.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services`
default: `fastly-services`
```
{
  "data": {
    "attributes": {
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "abc123",
    "type": "fastly-services"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyService-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyService-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyService-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#UpdateFastlyService-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


The expected response schema when getting a Fastly service.
Field
Type
Description
data
object
Data object for Fastly service requests.
attributes
object
Attributes object for Fastly service requests.
tags
[string]
A list of tags for the Fastly service.
id [_required_]
string
The ID of the Fastly service.
type [_required_]
enum
The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services`
default: `fastly-services`
```
{
  "data": {
    "attributes": {
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "abc123",
    "type": "fastly-services"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Update Fastly service
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
export service_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services/${service_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "abc123",
    "type": "fastly-services"
  }
}
EOF  

                
```

#####  Update Fastly service
```
"""
Update Fastly service returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_service_attributes import FastlyServiceAttributes
from datadog_api_client.v2.model.fastly_service_data import FastlyServiceData
from datadog_api_client.v2.model.fastly_service_request import FastlyServiceRequest
from datadog_api_client.v2.model.fastly_service_type import FastlyServiceType

body = FastlyServiceRequest(
    data=FastlyServiceData(
        attributes=FastlyServiceAttributes(
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
        id="abc123",
        type=FastlyServiceType.FASTLY_SERVICES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.update_fastly_service(account_id="account_id", service_id="service_id", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update Fastly service
```
# Update Fastly service returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new

body = DatadogAPIClient::V2::FastlyServiceRequest.new({
  data: DatadogAPIClient::V2::FastlyServiceData.new({
    attributes: DatadogAPIClient::V2::FastlyServiceAttributes.new({
      tags: [
        "myTag",
        "myTag2:myValue",
      ],
    }),
    id: "abc123",
    type: DatadogAPIClient::V2::FastlyServiceType::FASTLY_SERVICES,
  }),
})
p api_instance.update_fastly_service("account_id", "service_id", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update Fastly service
```
// Update Fastly service returns "OK" response

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
	body := datadogV2.FastlyServiceRequest{
		Data: datadogV2.FastlyServiceData{
			Attributes: &datadogV2.FastlyServiceAttributes{
				Tags: []string{
					"myTag",
					"myTag2:myValue",
				},
			},
			Id:   "abc123",
			Type: datadogV2.FASTLYSERVICETYPE_FASTLY_SERVICES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	resp, r, err := api.UpdateFastlyService(ctx, "account_id", "service_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.UpdateFastlyService`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `FastlyIntegrationApi.UpdateFastlyService`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update Fastly service
```
// Update Fastly service returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;
import com.datadog.api.client.v2.model.FastlyServiceAttributes;
import com.datadog.api.client.v2.model.FastlyServiceData;
import com.datadog.api.client.v2.model.FastlyServiceRequest;
import com.datadog.api.client.v2.model.FastlyServiceResponse;
import com.datadog.api.client.v2.model.FastlyServiceType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    FastlyServiceRequest body =
        new FastlyServiceRequest()
            .data(
                new FastlyServiceData()
                    .attributes(
                        new FastlyServiceAttributes()
                            .tags(Arrays.asList("myTag", "myTag2:myValue")))
                    .id("abc123")
                    .type(FastlyServiceType.FASTLY_SERVICES));

    try {
      FastlyServiceResponse result =
          apiInstance.updateFastlyService("account_id", "service_id", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#updateFastlyService");
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

#####  Update Fastly service
```
// Update Fastly service returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;
use datadog_api_client::datadogV2::model::FastlyServiceAttributes;
use datadog_api_client::datadogV2::model::FastlyServiceData;
use datadog_api_client::datadogV2::model::FastlyServiceRequest;
use datadog_api_client::datadogV2::model::FastlyServiceType;

#[tokio::main]
async fn main() {
    let body = FastlyServiceRequest::new(
        FastlyServiceData::new("abc123".to_string(), FastlyServiceType::FASTLY_SERVICES)
            .attributes(
                FastlyServiceAttributes::new()
                    .tags(vec!["myTag".to_string(), "myTag2:myValue".to_string()]),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api
        .update_fastly_service("account_id".to_string(), "service_id".to_string(), body)
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

#####  Update Fastly service
```
/**
 * Update Fastly service returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

const params: v2.FastlyIntegrationApiUpdateFastlyServiceRequest = {
  body: {
    data: {
      attributes: {
        tags: ["myTag", "myTag2:myValue"],
      },
      id: "abc123",
      type: "fastly-services",
    },
  },
  accountId: "account_id",
  serviceId: "service_id",
};

apiInstance
  .updateFastlyService(params)
  .then((data: v2.FastlyServiceResponse) => {
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
## [Delete Fastly service](https://docs.datadoghq.com/api/latest/fastly-integration/#delete-fastly-service)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/fastly-integration/#delete-fastly-service-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}
### Overview
Delete a Fastly service for an account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Fastly Account id.
service_id [_required_]
string
Fastly Service ID.
### Response
  * [204](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyService-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyService-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyService-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/fastly-integration/#DeleteFastlyService-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/fastly-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/fastly-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/fastly-integration/?code-lang=typescript)


#####  Delete Fastly service
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
export service_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services/${service_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete Fastly service
```
"""
Delete Fastly service returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    api_instance.delete_fastly_service(
        account_id="account_id",
        service_id="service_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete Fastly service
```
# Delete Fastly service returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
api_instance.delete_fastly_service("account_id", "service_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete Fastly service
```
// Delete Fastly service returns "OK" response

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
	api := datadogV2.NewFastlyIntegrationApi(apiClient)
	r, err := api.DeleteFastlyService(ctx, "account_id", "service_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FastlyIntegrationApi.DeleteFastlyService`: %v\n", err)
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

#####  Delete Fastly service
```
// Delete Fastly service returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.FastlyIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    FastlyIntegrationApi apiInstance = new FastlyIntegrationApi(defaultClient);

    try {
      apiInstance.deleteFastlyService("account_id", "service_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling FastlyIntegrationApi#deleteFastlyService");
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

#####  Delete Fastly service
```
// Delete Fastly service returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_fastly_integration::FastlyIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = FastlyIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_fastly_service("account_id".to_string(), "service_id".to_string())
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

#####  Delete Fastly service
```
/**
 * Delete Fastly service returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.FastlyIntegrationApi(configuration);

const params: v2.FastlyIntegrationApiDeleteFastlyServiceRequest = {
  accountId: "account_id",
  serviceId: "service_id",
};

apiInstance
  .deleteFastlyService(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=33a58cbf-7740-4118-8bbf-5abfa26bba28&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=56d7ce7d-34ea-41f6-a644-5bfeaf37e94c&pt=Fastly%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ffastly-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=33a58cbf-7740-4118-8bbf-5abfa26bba28&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=56d7ce7d-34ea-41f6-a644-5bfeaf37e94c&pt=Fastly%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ffastly-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
Feedback
## Was this page helpful?
Yes 🎉
No 👎
Next
![](https://survey-images.hotjar.com/surveys/logo/90f40352a7464c849f5ce82ccd0e758d)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=505e5784-5e3d-4029-9e0b-cc42c7cdd0f0&bo=2&sid=ae838290f0bf11f082a211cb2590164a&vid=ae83a1b0f0bf11f0ac21fb24fefcc951&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Fastly%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ffastly-integration%2F&r=&lt=1516&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=281323)
