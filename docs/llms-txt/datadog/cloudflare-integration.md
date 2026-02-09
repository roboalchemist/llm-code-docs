# Source: https://docs.datadoghq.com/api/latest/cloudflare-integration.md

---
title: Cloudflare Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Cloudflare Integration
---

# Cloudflare Integration

Manage your Datadog Cloudflare integration directly through the Datadog API. See the [Cloudflare integration page](https://docs.datadoghq.com/integrations/cloudflare/) for more information.

## List Cloudflare accounts{% #list-cloudflare-accounts %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts |

### Overview

List Cloudflare accounts. This endpoint requires the `integrations_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting Cloudflare accounts.

| Parent field | Field                        | Type     | Description                                                                                                                           |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | [object] | The JSON:API data schema.                                                                                                             |
| data         | attributes [*required*] | object   | Attributes object of a Cloudflare account.                                                                                            |
| attributes   | email                        | string   | The email associated with the Cloudflare account.                                                                                     |
| attributes   | name [*required*]       | string   | The name of the Cloudflare account.                                                                                                   |
| attributes   | resources                    | [string] | An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources. |
| attributes   | zones                        | [string] | An allowlist of zones to restrict pulling metrics for.                                                                                |
| data         | id [*required*]         | string   | The ID of the Cloudflare account, a hash of the account name.                                                                         |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`                    |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Cloudflare accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new
p api_instance.list_cloudflare_accounts()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Add Cloudflare account{% #add-cloudflare-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts |

### Overview

Create a Cloudflare account. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                 |
| ------------ | ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Data object for creating a Cloudflare account.                                                                              |
| data         | attributes [*required*] | object   | Attributes object for creating a Cloudflare account.                                                                        |
| attributes   | api_key [*required*]    | string   | The API key (or token) for the Cloudflare account.                                                                          |
| attributes   | email                        | string   | The email associated with the Cloudflare account. If an API key is provided (and not a token), this field is also required. |
| attributes   | name [*required*]       | string   | The name of the Cloudflare account.                                                                                         |
| attributes   | resources                    | [string] | An allowlist of resources to restrict pulling metrics for including `'web', 'dns', 'lb' (load balancer), 'worker'`.         |
| attributes   | zones                        | [string] | An allowlist of zones to restrict pulling metrics for.                                                                      |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`          |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
The expected response schema when getting a Cloudflare account.

| Parent field | Field                        | Type     | Description                                                                                                                           |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Data object of a Cloudflare account.                                                                                                  |
| data         | attributes [*required*] | object   | Attributes object of a Cloudflare account.                                                                                            |
| attributes   | email                        | string   | The email associated with the Cloudflare account.                                                                                     |
| attributes   | name [*required*]       | string   | The name of the Cloudflare account.                                                                                                   |
| attributes   | resources                    | [string] | An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources. |
| attributes   | zones                        | [string] | An allowlist of zones to restrict pulling metrics for.                                                                                |
| data         | id [*required*]         | string   | The ID of the Cloudflare account, a hash of the account name.                                                                         |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`                    |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get Cloudflare account{% #get-cloudflare-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                           |
| ----------------- | -------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts/{account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts/{account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |

### Overview

Get a Cloudflare account. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description |
| ---------------------------- | ------ | ----------- |
| account_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Cloudflare account.

| Parent field | Field                        | Type     | Description                                                                                                                           |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Data object of a Cloudflare account.                                                                                                  |
| data         | attributes [*required*] | object   | Attributes object of a Cloudflare account.                                                                                            |
| attributes   | email                        | string   | The email associated with the Cloudflare account.                                                                                     |
| attributes   | name [*required*]       | string   | The name of the Cloudflare account.                                                                                                   |
| attributes   | resources                    | [string] | An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources. |
| attributes   | zones                        | [string] | An allowlist of zones to restrict pulling metrics for.                                                                                |
| data         | id [*required*]         | string   | The ID of the Cloudflare account, a hash of the account name.                                                                         |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`                    |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get Cloudflare account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new

# there is a valid "cloudflare_account" in the system
CLOUDFLARE_ACCOUNT_DATA_ID = ENV["CLOUDFLARE_ACCOUNT_DATA_ID"]
p api_instance.get_cloudflare_account(CLOUDFLARE_ACCOUNT_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update Cloudflare account{% #update-cloudflare-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts/{account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts/{account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |

### Overview

Update a Cloudflare account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description |
| ---------------------------- | ------ | ----------- |
| account_id [*required*] | string | None        |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                     | Type     | Description                                                                                                                 |
| ------------ | ------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]    | object   | Data object for updating a Cloudflare account.                                                                              |
| data         | attributes                | object   | Attributes object for updating a Cloudflare account.                                                                        |
| attributes   | api_key [*required*] | string   | The API key of the Cloudflare account.                                                                                      |
| attributes   | email                     | string   | The email associated with the Cloudflare account. If an API key is provided (and not a token), this field is also required. |
| attributes   | name                      | string   | The name of the Cloudflare account.                                                                                         |
| attributes   | resources                 | [string] | An allowlist of resources to restrict pulling metrics for including `'web', 'dns', 'lb' (load balancer), 'worker'`.         |
| attributes   | zones                     | [string] | An allowlist of zones to restrict pulling metrics for.                                                                      |
| data         | type                      | enum     | The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`          |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Cloudflare account.

| Parent field | Field                        | Type     | Description                                                                                                                           |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Data object of a Cloudflare account.                                                                                                  |
| data         | attributes [*required*] | object   | Attributes object of a Cloudflare account.                                                                                            |
| attributes   | email                        | string   | The email associated with the Cloudflare account.                                                                                     |
| attributes   | name [*required*]       | string   | The name of the Cloudflare account.                                                                                                   |
| attributes   | resources                    | [string] | An allowlist of resources, such as `web`, `dns`, `lb` (load balancer), `worker`, that restricts pulling metrics from those resources. |
| attributes   | zones                        | [string] | An allowlist of zones to restrict pulling metrics for.                                                                                |
| data         | id [*required*]         | string   | The ID of the Cloudflare account, a hash of the account name.                                                                         |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `cloudflare-accounts`. Allowed enum values: `cloudflare-accounts`                    |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/${account_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete Cloudflare account{% #delete-cloudflare-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integrations/cloudflare/accounts/{account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integrations/cloudflare/accounts/{account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/{account_id} |

### Overview

Delete a Cloudflare account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description |
| ---------------------------- | ------ | ----------- |
| account_id [*required*] | string | None        |

### Response

{% tab title="204" %}
OK
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/cloudflare/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Cloudflare account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudflareIntegrationAPI.new
api_instance.delete_cloudflare_account("account_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
