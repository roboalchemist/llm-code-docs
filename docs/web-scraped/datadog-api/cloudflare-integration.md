# Source: https://docs.datadoghq.com/api/latest/cloudflare-integration/

# Cloudflare Integration
Manage your Datadog Cloudflare integration directly through the Datadog API. See the [Cloudflare integration page](https://docs.datadoghq.com/integrations/cloudflare/) for more information.
## [List Cloudflare accounts](https://docs.datadoghq.com/api/latest/cloudflare-integration/#list-cloudflare-accounts)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/cloudflare-integration/#list-cloudflare-accounts-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.datadoghq.eu/api/v2/integrations/cloudflare/accountshttps://api.ddog-gov.com/api/v2/integrations/cloudflare/accountshttps://api.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts
### Overview
List Cloudflare accounts. This endpoint requires the `integrations_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/cloudflare-integration/#ListCloudflareAccounts-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/cloudflare-integration/#ListCloudflareAccounts-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/cloudflare-integration/#ListCloudflareAccounts-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/cloudflare-integration/#ListCloudflareAccounts-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/cloudflare-integration/#ListCloudflareAccounts-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


The expected response schema when getting Cloudflare accounts.
Field
Type
Description
data
[object]
The JSON:API data schema.
attributes [_required_]
object
Attributes object of a Cloudflare account.
email
string
The email associated with the Cloudflare account.
name [_required_]
string
The name of the Cloudflare account.
resources
[string]
An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources.
zones
[string]
An allowlist of zones to restrict pulling metrics for.
id [_required_]
string
The ID of the Cloudflare account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`
default: `cloudflare-accounts`
```
{
  "data": [
    {
      "attributes": {
        "email": "test-email@example.com",
        "name": "test-name",
        "resources": [
          "web",
          "dns",
          "lb",
          "worker"
        ],
        "zones": [
          "zone_id_1",
          "zone_id_2"
        ]
      },
      "id": "c1a8e059bfd1e911cf10b626340c9a54",
      "type": "cloudflare-accounts"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=typescript)


#####  List Cloudflare accounts
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Cloudflare accounts
```
"""
List Cloudflare accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.list_cloudflare_accounts()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Cloudflare accounts
```
# List Cloudflare accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new
p api_instance.list_cloudflare_accounts()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Cloudflare accounts
```
// List Cloudflare accounts returns "OK" response

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
	api := datadogV2.NewCloudflareIntegrationApi(apiClient)
	resp, r, err := api.ListCloudflareAccounts(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudflareIntegrationApi.ListCloudflareAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudflareIntegrationApi.ListCloudflareAccounts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Cloudflare accounts
```
// List Cloudflare accounts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudflareIntegrationApi;
import com.datadog.api.client.v2.model.CloudflareAccountsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudflareIntegrationApi apiInstance = new CloudflareIntegrationApi(defaultClient);

    try {
      CloudflareAccountsResponse result = apiInstance.listCloudflareAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudflareIntegrationApi#listCloudflareAccounts");
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

#####  List Cloudflare accounts
```
// List Cloudflare accounts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloudflare_integration::CloudflareIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudflareIntegrationAPI::with_config(configuration);
    let resp = api.list_cloudflare_accounts().await;
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

#####  List Cloudflare accounts
```
/**
 * List Cloudflare accounts returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudflareIntegrationApi(configuration);

apiInstance
  .listCloudflareAccounts()
  .then((data: v2.CloudflareAccountsResponse) => {
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
## [Add Cloudflare account](https://docs.datadoghq.com/api/latest/cloudflare-integration/#add-cloudflare-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/cloudflare-integration/#add-cloudflare-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.datadoghq.eu/api/v2/integrations/cloudflare/accountshttps://api.ddog-gov.com/api/v2/integrations/cloudflare/accountshttps://api.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accountshttps://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts
### Overview
Create a Cloudflare account. This endpoint requires the `manage_integrations` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


Field
Type
Description
data [_required_]
object
Data object for creating a Cloudflare account.
attributes [_required_]
object
Attributes object for creating a Cloudflare account.
api_key [_required_]
string
The API key (or token) for the Cloudflare account.
email
string
The email associated with the Cloudflare account. If an API key is provided (and not a token), this field is also required.
name [_required_]
string
The name of the Cloudflare account.
resources
[string]
An allowlist of resources to restrict pulling metrics for including `'web', 'dns', 'lb' (load balancer), 'worker'`.
zones
[string]
An allowlist of zones to restrict pulling metrics for.
type [_required_]
enum
The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`
default: `cloudflare-accounts`
```
{
  "data": {
    "attributes": {
      "api_key": "fakekey",
      "email": "dev@datadoghq.com",
      "name": "examplecloudflareintegration"
    },
    "type": "cloudflare-accounts"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/cloudflare-integration/#CreateCloudflareAccount-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/cloudflare-integration/#CreateCloudflareAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/cloudflare-integration/#CreateCloudflareAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/cloudflare-integration/#CreateCloudflareAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/cloudflare-integration/#CreateCloudflareAccount-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


The expected response schema when getting a Cloudflare account.
Field
Type
Description
data
object
Data object of a Cloudflare account.
attributes [_required_]
object
Attributes object of a Cloudflare account.
email
string
The email associated with the Cloudflare account.
name [_required_]
string
The name of the Cloudflare account.
resources
[string]
An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources.
zones
[string]
An allowlist of zones to restrict pulling metrics for.
id [_required_]
string
The ID of the Cloudflare account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`
default: `cloudflare-accounts`
```
{
  "data": {
    "attributes": {
      "email": "test-email@example.com",
      "name": "test-name",
      "resources": [
        "web",
        "dns",
        "lb",
        "worker"
      ],
      "zones": [
        "zone_id_1",
        "zone_id_2"
      ]
    },
    "id": "c1a8e059bfd1e911cf10b626340c9a54",
    "type": "cloudflare-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=typescript)


#####  Add Cloudflare account returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "api_key": "fakekey",
      "email": "dev@datadoghq.com",
      "name": "examplecloudflareintegration"
    },
    "type": "cloudflare-accounts"
  }
}
EOF  

                        
```

#####  Add Cloudflare account returns "CREATED" response
```
// Add Cloudflare account returns "CREATED" response

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
	body := datadogV2.CloudflareAccountCreateRequest{
		Data: datadogV2.CloudflareAccountCreateRequestData{
			Attributes: datadogV2.CloudflareAccountCreateRequestAttributes{
				ApiKey: "fakekey",
				Email:  datadog.PtrString("dev@datadoghq.com"),
				Name:   "examplecloudflareintegration",
			},
			Type: datadogV2.CLOUDFLAREACCOUNTTYPE_CLOUDFLARE_ACCOUNTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudflareIntegrationApi(apiClient)
	resp, r, err := api.CreateCloudflareAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudflareIntegrationApi.CreateCloudflareAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudflareIntegrationApi.CreateCloudflareAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add Cloudflare account returns "CREATED" response
```
// Add Cloudflare account returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudflareIntegrationApi;
import com.datadog.api.client.v2.model.CloudflareAccountCreateRequest;
import com.datadog.api.client.v2.model.CloudflareAccountCreateRequestAttributes;
import com.datadog.api.client.v2.model.CloudflareAccountCreateRequestData;
import com.datadog.api.client.v2.model.CloudflareAccountResponse;
import com.datadog.api.client.v2.model.CloudflareAccountType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudflareIntegrationApi apiInstance = new CloudflareIntegrationApi(defaultClient);

    CloudflareAccountCreateRequest body =
        new CloudflareAccountCreateRequest()
            .data(
                new CloudflareAccountCreateRequestData()
                    .attributes(
                        new CloudflareAccountCreateRequestAttributes()
                            .apiKey("fakekey")
                            .email("dev@datadoghq.com")
                            .name("examplecloudflareintegration"))
                    .type(CloudflareAccountType.CLOUDFLARE_ACCOUNTS));

    try {
      CloudflareAccountResponse result = apiInstance.createCloudflareAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudflareIntegrationApi#createCloudflareAccount");
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

#####  Add Cloudflare account returns "CREATED" response
```
"""
Add Cloudflare account returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi
from datadog_api_client.v2.model.cloudflare_account_create_request import CloudflareAccountCreateRequest
from datadog_api_client.v2.model.cloudflare_account_create_request_attributes import (
    CloudflareAccountCreateRequestAttributes,
)
from datadog_api_client.v2.model.cloudflare_account_create_request_data import CloudflareAccountCreateRequestData
from datadog_api_client.v2.model.cloudflare_account_type import CloudflareAccountType

body = CloudflareAccountCreateRequest(
    data=CloudflareAccountCreateRequestData(
        attributes=CloudflareAccountCreateRequestAttributes(
            api_key="fakekey",
            email="dev@datadoghq.com",
            name="examplecloudflareintegration",
        ),
        type=CloudflareAccountType.CLOUDFLARE_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.create_cloudflare_account(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add Cloudflare account returns "CREATED" response
```
# Add Cloudflare account returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new

body = DatadogAPIClient::V2::CloudflareAccountCreateRequest.new({
  data: DatadogAPIClient::V2::CloudflareAccountCreateRequestData.new({
    attributes: DatadogAPIClient::V2::CloudflareAccountCreateRequestAttributes.new({
      api_key: "fakekey",
      email: "dev@datadoghq.com",
      name: "examplecloudflareintegration",
    }),
    type: DatadogAPIClient::V2::CloudflareAccountType::CLOUDFLARE_ACCOUNTS,
  }),
})
p api_instance.create_cloudflare_account(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add Cloudflare account returns "CREATED" response
```
// Add Cloudflare account returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloudflare_integration::CloudflareIntegrationAPI;
use datadog_api_client::datadogV2::model::CloudflareAccountCreateRequest;
use datadog_api_client::datadogV2::model::CloudflareAccountCreateRequestAttributes;
use datadog_api_client::datadogV2::model::CloudflareAccountCreateRequestData;
use datadog_api_client::datadogV2::model::CloudflareAccountType;

#[tokio::main]
async fn main() {
    let body = CloudflareAccountCreateRequest::new(CloudflareAccountCreateRequestData::new(
        CloudflareAccountCreateRequestAttributes::new(
            "fakekey".to_string(),
            "examplecloudflareintegration".to_string(),
        )
        .email("dev@datadoghq.com".to_string()),
        CloudflareAccountType::CLOUDFLARE_ACCOUNTS,
    ));
    let configuration = datadog::Configuration::new();
    let api = CloudflareIntegrationAPI::with_config(configuration);
    let resp = api.create_cloudflare_account(body).await;
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

#####  Add Cloudflare account returns "CREATED" response
```
/**
 * Add Cloudflare account returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudflareIntegrationApi(configuration);

const params: v2.CloudflareIntegrationApiCreateCloudflareAccountRequest = {
  body: {
    data: {
      attributes: {
        apiKey: "fakekey",
        email: "dev@datadoghq.com",
        name: "examplecloudflareintegration",
      },
      type: "cloudflare-accounts",
    },
  },
};

apiInstance
  .createCloudflareAccount(params)
  .then((data: v2.CloudflareAccountResponse) => {
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
## [Get Cloudflare account](https://docs.datadoghq.com/api/latest/cloudflare-integration/#get-cloudflare-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/cloudflare-integration/#get-cloudflare-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}
### Overview
Get a Cloudflare account. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/cloudflare-integration/#GetCloudflareAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/cloudflare-integration/#GetCloudflareAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/cloudflare-integration/#GetCloudflareAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/cloudflare-integration/#GetCloudflareAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/cloudflare-integration/#GetCloudflareAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


The expected response schema when getting a Cloudflare account.
Field
Type
Description
data
object
Data object of a Cloudflare account.
attributes [_required_]
object
Attributes object of a Cloudflare account.
email
string
The email associated with the Cloudflare account.
name [_required_]
string
The name of the Cloudflare account.
resources
[string]
An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources.
zones
[string]
An allowlist of zones to restrict pulling metrics for.
id [_required_]
string
The ID of the Cloudflare account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`
default: `cloudflare-accounts`
```
{
  "data": {
    "attributes": {
      "email": "test-email@example.com",
      "name": "test-name",
      "resources": [
        "web",
        "dns",
        "lb",
        "worker"
      ],
      "zones": [
        "zone_id_1",
        "zone_id_2"
      ]
    },
    "id": "c1a8e059bfd1e911cf10b626340c9a54",
    "type": "cloudflare-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=typescript)


#####  Get Cloudflare account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Cloudflare account
```
"""
Get Cloudflare account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi

# there is a valid "cloudflare_account" in the system
CLOUDFLARE_ACCOUNT_DATA_ID = environ["CLOUDFLARE_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.get_cloudflare_account(
        account_id=CLOUDFLARE_ACCOUNT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get Cloudflare account
```
# Get Cloudflare account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new

# there is a valid "cloudflare_account" in the system
CLOUDFLARE_ACCOUNT_DATA_ID = ENV["CLOUDFLARE_ACCOUNT_DATA_ID"]
p api_instance.get_cloudflare_account(CLOUDFLARE_ACCOUNT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get Cloudflare account
```
// Get Cloudflare account returns "OK" response

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
	// there is a valid "cloudflare_account" in the system
	CloudflareAccountDataID := os.Getenv("CLOUDFLARE_ACCOUNT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudflareIntegrationApi(apiClient)
	resp, r, err := api.GetCloudflareAccount(ctx, CloudflareAccountDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudflareIntegrationApi.GetCloudflareAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudflareIntegrationApi.GetCloudflareAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get Cloudflare account
```
// Get Cloudflare account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudflareIntegrationApi;
import com.datadog.api.client.v2.model.CloudflareAccountResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudflareIntegrationApi apiInstance = new CloudflareIntegrationApi(defaultClient);

    // there is a valid "cloudflare_account" in the system
    String CLOUDFLARE_ACCOUNT_DATA_ID = System.getenv("CLOUDFLARE_ACCOUNT_DATA_ID");

    try {
      CloudflareAccountResponse result =
          apiInstance.getCloudflareAccount(CLOUDFLARE_ACCOUNT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudflareIntegrationApi#getCloudflareAccount");
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

#####  Get Cloudflare account
```
// Get Cloudflare account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloudflare_integration::CloudflareIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "cloudflare_account" in the system
    let cloudflare_account_data_id = std::env::var("CLOUDFLARE_ACCOUNT_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CloudflareIntegrationAPI::with_config(configuration);
    let resp = api
        .get_cloudflare_account(cloudflare_account_data_id.clone())
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

#####  Get Cloudflare account
```
/**
 * Get Cloudflare account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudflareIntegrationApi(configuration);

// there is a valid "cloudflare_account" in the system
const CLOUDFLARE_ACCOUNT_DATA_ID = process.env
  .CLOUDFLARE_ACCOUNT_DATA_ID as string;

const params: v2.CloudflareIntegrationApiGetCloudflareAccountRequest = {
  accountId: CLOUDFLARE_ACCOUNT_DATA_ID,
};

apiInstance
  .getCloudflareAccount(params)
  .then((data: v2.CloudflareAccountResponse) => {
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
## [Update Cloudflare account](https://docs.datadoghq.com/api/latest/cloudflare-integration/#update-cloudflare-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/cloudflare-integration/#update-cloudflare-account-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}
### Overview
Update a Cloudflare account. This endpoint requires the `manage_integrations` permission.
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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


Field
Type
Description
data [_required_]
object
Data object for updating a Cloudflare account.
attributes
object
Attributes object for updating a Cloudflare account.
api_key [_required_]
string
The API key of the Cloudflare account.
email
string
The email associated with the Cloudflare account. If an API key is provided (and not a token), this field is also required.
name
string
The name of the Cloudflare account.
resources
[string]
An allowlist of resources to restrict pulling metrics for including `'web', 'dns', 'lb' (load balancer), 'worker'`.
zones
[string]
An allowlist of zones to restrict pulling metrics for.
type
enum
The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`
default: `cloudflare-accounts`
```
{
  "data": {
    "attributes": {
      "api_key": "fakekey",
      "email": "dev@datadoghq.com",
      "zones": [
        "zone-id-3"
      ]
    },
    "type": "cloudflare-accounts"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/cloudflare-integration/#UpdateCloudflareAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/cloudflare-integration/#UpdateCloudflareAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/cloudflare-integration/#UpdateCloudflareAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/cloudflare-integration/#UpdateCloudflareAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/cloudflare-integration/#UpdateCloudflareAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


The expected response schema when getting a Cloudflare account.
Field
Type
Description
data
object
Data object of a Cloudflare account.
attributes [_required_]
object
Attributes object of a Cloudflare account.
email
string
The email associated with the Cloudflare account.
name [_required_]
string
The name of the Cloudflare account.
resources
[string]
An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources.
zones
[string]
An allowlist of zones to restrict pulling metrics for.
id [_required_]
string
The ID of the Cloudflare account, a hash of the account name.
type [_required_]
enum
The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`
default: `cloudflare-accounts`
```
{
  "data": {
    "attributes": {
      "email": "test-email@example.com",
      "name": "test-name",
      "resources": [
        "web",
        "dns",
        "lb",
        "worker"
      ],
      "zones": [
        "zone_id_1",
        "zone_id_2"
      ]
    },
    "id": "c1a8e059bfd1e911cf10b626340c9a54",
    "type": "cloudflare-accounts"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=typescript)


#####  Update Cloudflare account returns "OK" response
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/${account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "api_key": "fakekey",
      "email": "dev@datadoghq.com",
      "zones": [
        "zone-id-3"
      ]
    },
    "type": "cloudflare-accounts"
  }
}
EOF  

                        
```

#####  Update Cloudflare account returns "OK" response
```
// Update Cloudflare account returns "OK" response

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
	// there is a valid "cloudflare_account" in the system
	CloudflareAccountDataID := os.Getenv("CLOUDFLARE_ACCOUNT_DATA_ID")

	body := datadogV2.CloudflareAccountUpdateRequest{
		Data: datadogV2.CloudflareAccountUpdateRequestData{
			Attributes: &datadogV2.CloudflareAccountUpdateRequestAttributes{
				ApiKey: "fakekey",
				Email:  datadog.PtrString("dev@datadoghq.com"),
				Zones: []string{
					"zone-id-3",
				},
			},
			Type: datadogV2.CLOUDFLAREACCOUNTTYPE_CLOUDFLARE_ACCOUNTS.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudflareIntegrationApi(apiClient)
	resp, r, err := api.UpdateCloudflareAccount(ctx, CloudflareAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudflareIntegrationApi.UpdateCloudflareAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudflareIntegrationApi.UpdateCloudflareAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update Cloudflare account returns "OK" response
```
// Update Cloudflare account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudflareIntegrationApi;
import com.datadog.api.client.v2.model.CloudflareAccountResponse;
import com.datadog.api.client.v2.model.CloudflareAccountType;
import com.datadog.api.client.v2.model.CloudflareAccountUpdateRequest;
import com.datadog.api.client.v2.model.CloudflareAccountUpdateRequestAttributes;
import com.datadog.api.client.v2.model.CloudflareAccountUpdateRequestData;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudflareIntegrationApi apiInstance = new CloudflareIntegrationApi(defaultClient);

    // there is a valid "cloudflare_account" in the system
    String CLOUDFLARE_ACCOUNT_DATA_ID = System.getenv("CLOUDFLARE_ACCOUNT_DATA_ID");

    CloudflareAccountUpdateRequest body =
        new CloudflareAccountUpdateRequest()
            .data(
                new CloudflareAccountUpdateRequestData()
                    .attributes(
                        new CloudflareAccountUpdateRequestAttributes()
                            .apiKey("fakekey")
                            .email("dev@datadoghq.com")
                            .zones(Collections.singletonList("zone-id-3")))
                    .type(CloudflareAccountType.CLOUDFLARE_ACCOUNTS));

    try {
      CloudflareAccountResponse result =
          apiInstance.updateCloudflareAccount(CLOUDFLARE_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudflareIntegrationApi#updateCloudflareAccount");
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

#####  Update Cloudflare account returns "OK" response
```
"""
Update Cloudflare account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi
from datadog_api_client.v2.model.cloudflare_account_type import CloudflareAccountType
from datadog_api_client.v2.model.cloudflare_account_update_request import CloudflareAccountUpdateRequest
from datadog_api_client.v2.model.cloudflare_account_update_request_attributes import (
    CloudflareAccountUpdateRequestAttributes,
)
from datadog_api_client.v2.model.cloudflare_account_update_request_data import CloudflareAccountUpdateRequestData

# there is a valid "cloudflare_account" in the system
CLOUDFLARE_ACCOUNT_DATA_ID = environ["CLOUDFLARE_ACCOUNT_DATA_ID"]

body = CloudflareAccountUpdateRequest(
    data=CloudflareAccountUpdateRequestData(
        attributes=CloudflareAccountUpdateRequestAttributes(
            api_key="fakekey",
            email="dev@datadoghq.com",
            zones=[
                "zone-id-3",
            ],
        ),
        type=CloudflareAccountType.CLOUDFLARE_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.update_cloudflare_account(account_id=CLOUDFLARE_ACCOUNT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update Cloudflare account returns "OK" response
```
# Update Cloudflare account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new

# there is a valid "cloudflare_account" in the system
CLOUDFLARE_ACCOUNT_DATA_ID = ENV["CLOUDFLARE_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::CloudflareAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::CloudflareAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::CloudflareAccountUpdateRequestAttributes.new({
      api_key: "fakekey",
      email: "dev@datadoghq.com",
      zones: [
        "zone-id-3",
      ],
    }),
    type: DatadogAPIClient::V2::CloudflareAccountType::CLOUDFLARE_ACCOUNTS,
  }),
})
p api_instance.update_cloudflare_account(CLOUDFLARE_ACCOUNT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update Cloudflare account returns "OK" response
```
// Update Cloudflare account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloudflare_integration::CloudflareIntegrationAPI;
use datadog_api_client::datadogV2::model::CloudflareAccountType;
use datadog_api_client::datadogV2::model::CloudflareAccountUpdateRequest;
use datadog_api_client::datadogV2::model::CloudflareAccountUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::CloudflareAccountUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "cloudflare_account" in the system
    let cloudflare_account_data_id = std::env::var("CLOUDFLARE_ACCOUNT_DATA_ID").unwrap();
    let body = CloudflareAccountUpdateRequest::new(
        CloudflareAccountUpdateRequestData::new()
            .attributes(
                CloudflareAccountUpdateRequestAttributes::new("fakekey".to_string())
                    .email("dev@datadoghq.com".to_string())
                    .zones(vec!["zone-id-3".to_string()]),
            )
            .type_(CloudflareAccountType::CLOUDFLARE_ACCOUNTS),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudflareIntegrationAPI::with_config(configuration);
    let resp = api
        .update_cloudflare_account(cloudflare_account_data_id.clone(), body)
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

#####  Update Cloudflare account returns "OK" response
```
/**
 * Update Cloudflare account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudflareIntegrationApi(configuration);

// there is a valid "cloudflare_account" in the system
const CLOUDFLARE_ACCOUNT_DATA_ID = process.env
  .CLOUDFLARE_ACCOUNT_DATA_ID as string;

const params: v2.CloudflareIntegrationApiUpdateCloudflareAccountRequest = {
  body: {
    data: {
      attributes: {
        apiKey: "fakekey",
        email: "dev@datadoghq.com",
        zones: ["zone-id-3"],
      },
      type: "cloudflare-accounts",
    },
  },
  accountId: CLOUDFLARE_ACCOUNT_DATA_ID,
};

apiInstance
  .updateCloudflareAccount(params)
  .then((data: v2.CloudflareAccountResponse) => {
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
## [Delete Cloudflare account](https://docs.datadoghq.com/api/latest/cloudflare-integration/#delete-cloudflare-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/cloudflare-integration/#delete-cloudflare-account-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}
### Overview
Delete a Cloudflare account. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/cloudflare-integration/#DeleteCloudflareAccount-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/cloudflare-integration/#DeleteCloudflareAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/cloudflare-integration/#DeleteCloudflareAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/cloudflare-integration/#DeleteCloudflareAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/cloudflare-integration/#DeleteCloudflareAccount-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/cloudflare-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/cloudflare-integration/?code-lang=typescript)


#####  Delete Cloudflare account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete Cloudflare account
```
"""
Delete Cloudflare account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    api_instance.delete_cloudflare_account(
        account_id="account_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete Cloudflare account
```
# Delete Cloudflare account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new
api_instance.delete_cloudflare_account("account_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete Cloudflare account
```
// Delete Cloudflare account returns "OK" response

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
	api := datadogV2.NewCloudflareIntegrationApi(apiClient)
	r, err := api.DeleteCloudflareAccount(ctx, "account_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudflareIntegrationApi.DeleteCloudflareAccount`: %v\n", err)
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

#####  Delete Cloudflare account
```
// Delete Cloudflare account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudflareIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudflareIntegrationApi apiInstance = new CloudflareIntegrationApi(defaultClient);

    try {
      apiInstance.deleteCloudflareAccount("account_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudflareIntegrationApi#deleteCloudflareAccount");
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

#####  Delete Cloudflare account
```
// Delete Cloudflare account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloudflare_integration::CloudflareIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudflareIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_cloudflare_account("account_id".to_string())
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

#####  Delete Cloudflare account
```
/**
 * Delete Cloudflare account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudflareIntegrationApi(configuration);

const params: v2.CloudflareIntegrationApiDeleteCloudflareAccountRequest = {
  accountId: "account_id",
};

apiInstance
  .deleteCloudflareAccount(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=dceef51d-cccd-4f70-a4a0-7cf2258adb66&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b6214877-75d3-4c26-b080-075f5abc4279&pt=Cloudflare%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcloudflare-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=dceef51d-cccd-4f70-a4a0-7cf2258adb66&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b6214877-75d3-4c26-b080-075f5abc4279&pt=Cloudflare%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcloudflare-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=62193122-e17f-4bab-a847-d529f040019b&bo=2&sid=3dcb5360f0bf11f0b770d1a90854b039&vid=3dcb8270f0bf11f0b05aab124df80fee&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Cloudflare%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcloudflare-integration%2F&r=&lt=1272&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=472858)
