# Source: https://docs.datadoghq.com/api/latest/fastly-integration.md

---
title: Fastly Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Fastly Integration
---

# Fastly Integration

Manage your Datadog Fastly integration accounts and services directly through the Datadog API. See the [Fastly integration page](https://docs.datadoghq.com/integrations/fastly/) for more information.

## List Fastly accounts{% #list-fastly-accounts %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/fastly/accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/fastly/accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/fastly/accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts |

### Overview

List Fastly accounts. This endpoint requires the `integrations_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting Fastly accounts.

| Parent field | Field                        | Type     | Description                                                                                                |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                         | [object] | The JSON:API data schema.                                                                                  |
| data         | attributes [*required*] | object   | Attributes object of a Fastly account.                                                                     |
| attributes   | name [*required*]       | string   | The name of the Fastly account.                                                                            |
| attributes   | services                     | [object] | A list of services belonging to the parent account.                                                        |
| services     | id [*required*]         | string   | The ID of the Fastly service                                                                               |
| services     | tags                         | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]         | string   | The ID of the Fastly account, a hash of the account name.                                                  |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Fastly accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
p api_instance.list_fastly_accounts()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Add Fastly account{% #add-fastly-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integrations/fastly/accounts      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integrations/fastly/accounts      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integrations/fastly/accounts     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts |

### Overview

Create a Fastly account. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Data object for creating a Fastly account.                                                                 |
| data         | attributes [*required*] | object   | Attributes object for creating a Fastly account.                                                           |
| attributes   | api_key [*required*]    | string   | The API key for the Fastly account.                                                                        |
| attributes   | name [*required*]       | string   | The name of the Fastly account.                                                                            |
| attributes   | services                     | [object] | A list of services belonging to the parent account.                                                        |
| services     | id [*required*]         | string   | The ID of the Fastly service                                                                               |
| services     | tags                         | [string] | A list of tags for the Fastly service.                                                                     |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
The expected response schema when getting a Fastly account.

| Parent field | Field                        | Type     | Description                                                                                                |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Data object of a Fastly account.                                                                           |
| data         | attributes [*required*] | object   | Attributes object of a Fastly account.                                                                     |
| attributes   | name [*required*]       | string   | The name of the Fastly account.                                                                            |
| attributes   | services                     | [object] | A list of services belonging to the parent account.                                                        |
| services     | id [*required*]         | string   | The ID of the Fastly service                                                                               |
| services     | tags                         | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]         | string   | The ID of the Fastly account, a hash of the account name.                                                  |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get Fastly account{% #get-fastly-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |

### Overview

Get a Fastly account. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Fastly account.

| Parent field | Field                        | Type     | Description                                                                                                |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Data object of a Fastly account.                                                                           |
| data         | attributes [*required*] | object   | Attributes object of a Fastly account.                                                                     |
| attributes   | name [*required*]       | string   | The name of the Fastly account.                                                                            |
| attributes   | services                     | [object] | A list of services belonging to the parent account.                                                        |
| services     | id [*required*]         | string   | The ID of the Fastly service                                                                               |
| services     | tags                         | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]         | string   | The ID of the Fastly account, a hash of the account name.                                                  |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get Fastly account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new

# there is a valid "fastly_account" in the system
FASTLY_ACCOUNT_DATA_ID = ENV["FASTLY_ACCOUNT_DATA_ID"]
p api_instance.get_fastly_account(FASTLY_ACCOUNT_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update Fastly account{% #update-fastly-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |

### Overview

Update a Fastly account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                                                                |
| ------------ | ---------------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Data object for updating a Fastly account.                                                                 |
| data         | attributes             | object | Attributes object for updating a Fastly account.                                                           |
| attributes   | api_key                | string | The API key of the Fastly account.                                                                         |
| attributes   | name                   | string | The name of the Fastly account.                                                                            |
| data         | type                   | enum   | The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key": "update-secret"
    },
    "type": "fastly-accounts"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Fastly account.

| Parent field | Field                        | Type     | Description                                                                                                |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Data object of a Fastly account.                                                                           |
| data         | attributes [*required*] | object   | Attributes object of a Fastly account.                                                                     |
| attributes   | name [*required*]       | string   | The name of the Fastly account.                                                                            |
| attributes   | services                     | [object] | A list of services belonging to the parent account.                                                        |
| services     | id [*required*]         | string   | The ID of the Fastly service                                                                               |
| services     | tags                         | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]         | string   | The ID of the Fastly account, a hash of the account name.                                                  |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `fastly-accounts`. Allowed enum values: `fastly-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete Fastly account{% #delete-fastly-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id} |

### Overview

Delete a Fastly account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |

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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Fastly account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
api_instance.delete_fastly_account("account_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## List Fastly services{% #list-fastly-services %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |

### Overview

List Fastly services for an account. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting Fastly services.

| Parent field | Field                  | Type     | Description                                                                                                |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                   | [object] | The JSON:API data schema.                                                                                  |
| data         | attributes             | object   | Attributes object for Fastly service requests.                                                             |
| attributes   | tags                   | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]   | string   | The ID of the Fastly service.                                                                              |
| data         | type [*required*] | enum     | The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Fastly services returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
p api_instance.list_fastly_services("account_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Add Fastly service{% #add-fastly-service %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services |

### Overview

Create a Fastly service for an account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object   | Data object for Fastly service requests.                                                                   |
| data         | attributes             | object   | Attributes object for Fastly service requests.                                                             |
| attributes   | tags                   | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]   | string   | The ID of the Fastly service.                                                                              |
| data         | type [*required*] | enum     | The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
The expected response schema when getting a Fastly service.

| Parent field | Field                  | Type     | Description                                                                                                |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                   | object   | Data object for Fastly service requests.                                                                   |
| data         | attributes             | object   | Attributes object for Fastly service requests.                                                             |
| attributes   | tags                   | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]   | string   | The ID of the Fastly service.                                                                              |
| data         | type [*required*] | enum     | The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services" \
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
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get Fastly service{% #get-fastly-service %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |

### Overview

Get a Fastly service for an account. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |
| service_id [*required*] | string | Fastly Service ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Fastly service.

| Parent field | Field                  | Type     | Description                                                                                                |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                   | object   | Data object for Fastly service requests.                                                                   |
| data         | attributes             | object   | Attributes object for Fastly service requests.                                                             |
| attributes   | tags                   | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]   | string   | The ID of the Fastly service.                                                                              |
| data         | type [*required*] | enum     | The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport account_id="CHANGE_ME"export service_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services/${service_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get Fastly service returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
p api_instance.get_fastly_service("account_id", "service_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update Fastly service{% #update-fastly-service %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |

### Overview

Update a Fastly service for an account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |
| service_id [*required*] | string | Fastly Service ID. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object   | Data object for Fastly service requests.                                                                   |
| data         | attributes             | object   | Attributes object for Fastly service requests.                                                             |
| attributes   | tags                   | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]   | string   | The ID of the Fastly service.                                                                              |
| data         | type [*required*] | enum     | The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Fastly service.

| Parent field | Field                  | Type     | Description                                                                                                |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
|              | data                   | object   | Data object for Fastly service requests.                                                                   |
| data         | attributes             | object   | Attributes object for Fastly service requests.                                                             |
| attributes   | tags                   | [string] | A list of tags for the Fastly service.                                                                     |
| data         | id [*required*]   | string   | The ID of the Fastly service.                                                                              |
| data         | type [*required*] | enum     | The JSON:API type for this API. Should always be `fastly-services`. Allowed enum values: `fastly-services` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport account_id="CHANGE_ME"export service_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services/${service_id}" \
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
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete Fastly service{% #delete-fastly-service %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/{account_id}/services/{service_id} |

### Overview

Delete a Fastly service for an account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description        |
| ---------------------------- | ------ | ------------------ |
| account_id [*required*] | string | Fastly Account id. |
| service_id [*required*] | string | Fastly Service ID. |

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
                  \# Path parametersexport account_id="CHANGE_ME"export service_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/fastly/accounts/${account_id}/services/${service_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Fastly service returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::FastlyIntegrationAPI.new
api_instance.delete_fastly_service("account_id", "service_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
