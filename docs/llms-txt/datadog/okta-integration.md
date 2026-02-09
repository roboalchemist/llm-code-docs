# Source: https://docs.datadoghq.com/api/latest/okta-integration.md

---
title: Okta Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Okta Integration
---

# Okta Integration

Configure your [Datadog Okta integration](https://docs.datadoghq.com/integrations/okta/) directly through the Datadog API.

## List Okta accounts{% #list-okta-accounts %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/okta/accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/okta/accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/okta/accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts |

### Overview

List Okta accounts. This endpoint requires the `integrations_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting Okta accounts.

| Parent field | Field                         | Type     | Description                                                            |
| ------------ | ----------------------------- | -------- | ---------------------------------------------------------------------- |
|              | data                          | [object] | List of Okta accounts.                                                 |
| data         | attributes [*required*]  | object   | Attributes object for an Okta account.                                 |
| attributes   | api_key                       | string   | The API key of the Okta account.                                       |
| attributes   | auth_method [*required*] | string   | The authorization method for an Okta account.                          |
| attributes   | client_id                     | string   | The Client ID of an Okta app integration.                              |
| attributes   | client_secret                 | string   | The client secret of an Okta app integration.                          |
| attributes   | domain [*required*]      | string   | The domain of the Okta account.                                        |
| attributes   | name [*required*]        | string   | The name of the Okta account.                                          |
| data         | id [*required*]          | string   | The ID of the Okta account, a UUID hash of the account name.           |
| data         | type [*required*]        | enum     | Account type for an Okta account. Allowed enum values: `okta-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Okta accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new
p api_instance.list_okta_accounts()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Add Okta account{% #add-okta-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integrations/okta/accounts      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integrations/okta/accounts      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integrations/okta/accounts     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts |

### Overview

Create an Okta account. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                         | Type   | Description                                                            |
| ------------ | ----------------------------- | ------ | ---------------------------------------------------------------------- |
|              | data [*required*]        | object | Schema for an Okta account.                                            |
| data         | attributes [*required*]  | object | Attributes object for an Okta account.                                 |
| attributes   | api_key                       | string | The API key of the Okta account.                                       |
| attributes   | auth_method [*required*] | string | The authorization method for an Okta account.                          |
| attributes   | client_id                     | string | The Client ID of an Okta app integration.                              |
| attributes   | client_secret                 | string | The client secret of an Okta app integration.                          |
| attributes   | domain [*required*]      | string | The domain of the Okta account.                                        |
| attributes   | name [*required*]        | string | The name of the Okta account.                                          |
| data         | id                            | string | The ID of the Okta account, a UUID hash of the account name.           |
| data         | type [*required*]        | enum   | Account type for an Okta account. Allowed enum values: `okta-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Response object for an Okta account.

| Parent field | Field                         | Type   | Description                                                            |
| ------------ | ----------------------------- | ------ | ---------------------------------------------------------------------- |
|              | data                          | object | Schema for an Okta account.                                            |
| data         | attributes [*required*]  | object | Attributes object for an Okta account.                                 |
| attributes   | api_key                       | string | The API key of the Okta account.                                       |
| attributes   | auth_method [*required*] | string | The authorization method for an Okta account.                          |
| attributes   | client_id                     | string | The Client ID of an Okta app integration.                              |
| attributes   | client_secret                 | string | The client secret of an Okta app integration.                          |
| attributes   | domain [*required*]      | string | The domain of the Okta account.                                        |
| attributes   | name [*required*]        | string | The name of the Okta account.                                          |
| data         | id                            | string | The ID of the Okta account, a UUID hash of the account name.           |
| data         | type [*required*]        | enum   | Account type for an Okta account. Allowed enum values: `okta-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get Okta account{% #get-okta-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/okta/accounts/{account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/okta/accounts/{account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |

### Overview

Get an Okta account. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description |
| ---------------------------- | ------ | ----------- |
| account_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for an Okta account.

| Parent field | Field                         | Type   | Description                                                            |
| ------------ | ----------------------------- | ------ | ---------------------------------------------------------------------- |
|              | data                          | object | Schema for an Okta account.                                            |
| data         | attributes [*required*]  | object | Attributes object for an Okta account.                                 |
| attributes   | api_key                       | string | The API key of the Okta account.                                       |
| attributes   | auth_method [*required*] | string | The authorization method for an Okta account.                          |
| attributes   | client_id                     | string | The Client ID of an Okta app integration.                              |
| attributes   | client_secret                 | string | The client secret of an Okta app integration.                          |
| attributes   | domain [*required*]      | string | The domain of the Okta account.                                        |
| attributes   | name [*required*]        | string | The name of the Okta account.                                          |
| data         | id                            | string | The ID of the Okta account, a UUID hash of the account name.           |
| data         | type [*required*]        | enum   | Account type for an Okta account. Allowed enum values: `okta-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get Okta account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new

# there is a valid "okta_account" in the system
OKTA_ACCOUNT_DATA_ID = ENV["OKTA_ACCOUNT_DATA_ID"]
p api_instance.get_okta_account(OKTA_ACCOUNT_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update Okta account{% #update-okta-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integrations/okta/accounts/{account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integrations/okta/accounts/{account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |

### Overview

Update an Okta account. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description |
| ---------------------------- | ------ | ----------- |
| account_id [*required*] | string | None        |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                         | Type   | Description                                                            |
| ------------ | ----------------------------- | ------ | ---------------------------------------------------------------------- |
|              | data [*required*]        | object | Data object for updating an Okta account.                              |
| data         | attributes                    | object | Attributes object for updating an Okta account.                        |
| attributes   | api_key                       | string | The API key of the Okta account.                                       |
| attributes   | auth_method [*required*] | string | The authorization method for an Okta account.                          |
| attributes   | client_id                     | string | The Client ID of an Okta app integration.                              |
| attributes   | client_secret                 | string | The client secret of an Okta app integration.                          |
| attributes   | domain [*required*]      | string | The domain associated with an Okta account.                            |
| data         | type                          | enum   | Account type for an Okta account. Allowed enum values: `okta-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for an Okta account.

| Parent field | Field                         | Type   | Description                                                            |
| ------------ | ----------------------------- | ------ | ---------------------------------------------------------------------- |
|              | data                          | object | Schema for an Okta account.                                            |
| data         | attributes [*required*]  | object | Attributes object for an Okta account.                                 |
| attributes   | api_key                       | string | The API key of the Okta account.                                       |
| attributes   | auth_method [*required*] | string | The authorization method for an Okta account.                          |
| attributes   | client_id                     | string | The Client ID of an Okta app integration.                              |
| attributes   | client_secret                 | string | The client secret of an Okta app integration.                          |
| attributes   | domain [*required*]      | string | The domain of the Okta account.                                        |
| attributes   | name [*required*]        | string | The name of the Okta account.                                          |
| data         | id                            | string | The ID of the Okta account, a UUID hash of the account name.           |
| data         | type [*required*]        | enum   | Account type for an Okta account. Allowed enum values: `okta-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/${account_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete Okta account{% #delete-okta-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integrations/okta/accounts/{account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integrations/okta/accounts/{account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integrations/okta/accounts/{account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/{account_id} |

### Overview

Delete an Okta account. This endpoint requires the `manage_integrations` permission.

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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/okta/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Okta account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OktaIntegrationAPI.new
api_instance.delete_okta_account("account_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
