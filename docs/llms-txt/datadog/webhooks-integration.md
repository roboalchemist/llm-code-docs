# Source: https://docs.datadoghq.com/api/latest/webhooks-integration.md

---
title: Webhooks Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Webhooks Integration
---

# Webhooks Integration

Configure your Datadog-Webhooks integration directly through the Datadog API. See the [Webhooks integration page](https://docs.datadoghq.com/integrations/webhooks) for more information.

## Create a webhooks integration{% #create-a-webhooks-integration %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhooks      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhooks      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks |

### Overview

Creates an endpoint with the name `<WEBHOOK_NAME>`. This endpoint requires the `create_webhooks` permission.

OAuth apps require the `create_webhooks` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#webhooks-integration) to access this endpoint.



### Request

#### Body Data (required)

Create a webhooks integration request body.

{% tab title="Model" %}

| Field                  | Type   | Description                                                                                                                                                                                                       |
| ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| custom_headers         | string | If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.                                                                                                               |
| encode_as              | enum   | Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`                                                                                                                             |
| name [*required*] | string | The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).                                                |
| payload                | string | If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage). |
| url [*required*]  | string | URL of the webhook.                                                                                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "name": "Example-Webhooks-Integration",
  "url": "https://example.com/webhook"
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Datadog-Webhooks integration.

| Field                  | Type   | Description                                                                                                                                                                                                       |
| ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| custom_headers         | string | If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.                                                                                                               |
| encode_as              | enum   | Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`                                                                                                                             |
| name [*required*] | string | The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).                                                |
| payload                | string | If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage). |
| url [*required*]  | string | URL of the webhook.                                                                                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "custom_headers": "string",
  "encode_as": "string",
  "name": "WEBHOOK_NAME",
  "payload": "string",
  "url": "https://example.com/webhook"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "Example-Webhooks-Integration",
  "url": "https://example.com/webhook"
}
EOF

#####

```go
// Create a webhooks integration returns "OK" response

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
    body := datadogV1.WebhooksIntegration{
        Name: "Example-Webhooks-Integration",
        Url:  "https://example.com/webhook",
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    resp, r, err := api.CreateWebhooksIntegration(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.CreateWebhooksIntegration`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `WebhooksIntegrationApi.CreateWebhooksIntegration`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a webhooks integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;
import com.datadog.api.client.v1.model.WebhooksIntegration;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    WebhooksIntegration body =
        new WebhooksIntegration()
            .name("Example-Webhooks-Integration")
            .url("https://example.com/webhook");

    try {
      WebhooksIntegration result = apiInstance.createWebhooksIntegration(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksIntegrationApi#createWebhooksIntegration");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
"""
Create a webhooks integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration import WebhooksIntegration

body = WebhooksIntegration(
    name="Example-Webhooks-Integration",
    url="https://example.com/webhook",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.create_webhooks_integration(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a webhooks integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

body = DatadogAPIClient::V1::WebhooksIntegration.new({
  name: "Example-Webhooks-Integration",
  url: "https://example.com/webhook",
})
p api_instance.create_webhooks_integration(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create a webhooks integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;
use datadog_api_client::datadogV1::model::WebhooksIntegration;

#[tokio::main]
async fn main() {
    let body = WebhooksIntegration::new(
        "Example-Webhooks-Integration".to_string(),
        "https://example.com/webhook".to_string(),
    );
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api.create_webhooks_integration(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create a webhooks integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

const params: v1.WebhooksIntegrationApiCreateWebhooksIntegrationRequest = {
  body: {
    name: "Example-Webhooks-Integration",
    url: "https://example.com/webhook",
  },
};

apiInstance
  .createWebhooksIntegration(params)
  .then((data: v1.WebhooksIntegration) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a webhook integration{% #get-a-webhook-integration %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |

### Overview

Gets the content of the webhook with the name `<WEBHOOK_NAME>`. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| webhook_name [*required*] | string | The name of the webhook. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Datadog-Webhooks integration.

| Field                  | Type   | Description                                                                                                                                                                                                       |
| ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| custom_headers         | string | If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.                                                                                                               |
| encode_as              | enum   | Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`                                                                                                                             |
| name [*required*] | string | The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).                                                |
| payload                | string | If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage). |
| url [*required*]  | string | URL of the webhook.                                                                                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "custom_headers": "string",
  "encode_as": "string",
  "name": "WEBHOOK_NAME",
  "payload": "string",
  "url": "https://example.com/webhook"
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

{% tab title="404" %}
Item Not Found
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
                  \# Path parametersexport webhook_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/${webhook_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a webhook integration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi

# there is a valid "webhook" in the system
WEBHOOK_NAME = environ["WEBHOOK_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.get_webhooks_integration(
        webhook_name=WEBHOOK_NAME,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a webhook integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook" in the system
WEBHOOK_NAME = ENV["WEBHOOK_NAME"]
p api_instance.get_webhooks_integration(WEBHOOK_NAME)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a webhook integration returns "OK" response

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
    // there is a valid "webhook" in the system
    WebhookName := os.Getenv("WEBHOOK_NAME")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    resp, r, err := api.GetWebhooksIntegration(ctx, WebhookName)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.GetWebhooksIntegration`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `WebhooksIntegrationApi.GetWebhooksIntegration`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a webhook integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;
import com.datadog.api.client.v1.model.WebhooksIntegration;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    // there is a valid "webhook" in the system
    String WEBHOOK_NAME = System.getenv("WEBHOOK_NAME");

    try {
      WebhooksIntegration result = apiInstance.getWebhooksIntegration(WEBHOOK_NAME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksIntegrationApi#getWebhooksIntegration");
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
// Get a webhook integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "webhook" in the system
    let webhook_name = std::env::var("WEBHOOK_NAME").unwrap();
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api.get_webhooks_integration(webhook_name.clone()).await;
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
 * Get a webhook integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

// there is a valid "webhook" in the system
const WEBHOOK_NAME = process.env.WEBHOOK_NAME as string;

const params: v1.WebhooksIntegrationApiGetWebhooksIntegrationRequest = {
  webhookName: WEBHOOK_NAME,
};

apiInstance
  .getWebhooksIntegration(params)
  .then((data: v1.WebhooksIntegration) => {
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

## Update a webhook{% #update-a-webhook %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |

### Overview

Updates the endpoint with the name `<WEBHOOK_NAME>`. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| webhook_name [*required*] | string | The name of the webhook. |

### Request

#### Body Data (required)

Update an existing Datadog-Webhooks integration.

{% tab title="Model" %}

| Field          | Type   | Description                                                                                                                                                                                                       |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| custom_headers | string | If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.                                                                                                               |
| encode_as      | enum   | Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`                                                                                                                             |
| name           | string | The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).                                                |
| payload        | string | If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage). |
| url            | string | URL of the webhook.                                                                                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "url": "https://example.com/webhook-updated"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Datadog-Webhooks integration.

| Field                  | Type   | Description                                                                                                                                                                                                       |
| ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| custom_headers         | string | If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.                                                                                                               |
| encode_as              | enum   | Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`                                                                                                                             |
| name [*required*] | string | The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).                                                |
| payload                | string | If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage). |
| url [*required*]  | string | URL of the webhook.                                                                                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "custom_headers": "string",
  "encode_as": "string",
  "name": "WEBHOOK_NAME",
  "payload": "string",
  "url": "https://example.com/webhook"
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

{% tab title="404" %}
Item Not Found
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
                          \# Path parametersexport webhook_name="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/${webhook_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "url": "https://example.com/webhook-updated"
}
EOF

#####

```go
// Update a webhook returns "OK" response

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
    // there is a valid "webhook" in the system
    WebhookName := os.Getenv("WEBHOOK_NAME")

    body := datadogV1.WebhooksIntegrationUpdateRequest{
        Url: datadog.PtrString("https://example.com/webhook-updated"),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    resp, r, err := api.UpdateWebhooksIntegration(ctx, WebhookName, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.UpdateWebhooksIntegration`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `WebhooksIntegrationApi.UpdateWebhooksIntegration`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a webhook returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;
import com.datadog.api.client.v1.model.WebhooksIntegration;
import com.datadog.api.client.v1.model.WebhooksIntegrationUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    // there is a valid "webhook" in the system
    String WEBHOOK_NAME = System.getenv("WEBHOOK_NAME");

    WebhooksIntegrationUpdateRequest body =
        new WebhooksIntegrationUpdateRequest().url("https://example.com/webhook-updated");

    try {
      WebhooksIntegration result = apiInstance.updateWebhooksIntegration(WEBHOOK_NAME, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksIntegrationApi#updateWebhooksIntegration");
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
Update a webhook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration_update_request import WebhooksIntegrationUpdateRequest

# there is a valid "webhook" in the system
WEBHOOK_NAME = environ["WEBHOOK_NAME"]

body = WebhooksIntegrationUpdateRequest(
    url="https://example.com/webhook-updated",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.update_webhooks_integration(webhook_name=WEBHOOK_NAME, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a webhook returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook" in the system
WEBHOOK_NAME = ENV["WEBHOOK_NAME"]

body = DatadogAPIClient::V1::WebhooksIntegrationUpdateRequest.new({
  url: "https://example.com/webhook-updated",
})
p api_instance.update_webhooks_integration(WEBHOOK_NAME, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update a webhook returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;
use datadog_api_client::datadogV1::model::WebhooksIntegrationUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "webhook" in the system
    let webhook_name = std::env::var("WEBHOOK_NAME").unwrap();
    let body = WebhooksIntegrationUpdateRequest::new()
        .url("https://example.com/webhook-updated".to_string());
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api
        .update_webhooks_integration(webhook_name.clone(), body)
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
 * Update a webhook returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

// there is a valid "webhook" in the system
const WEBHOOK_NAME = process.env.WEBHOOK_NAME as string;

const params: v1.WebhooksIntegrationApiUpdateWebhooksIntegrationRequest = {
  body: {
    url: "https://example.com/webhook-updated",
  },
  webhookName: WEBHOOK_NAME,
};

apiInstance
  .updateWebhooksIntegration(params)
  .then((data: v1.WebhooksIntegration) => {
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

## Delete a webhook{% #delete-a-webhook %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name} |

### Overview

Deletes the endpoint with the name `<WEBHOOK NAME>`. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| webhook_name [*required*] | string | The name of the webhook. |

### Response

{% tab title="200" %}
OK
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

{% tab title="404" %}
Item Not Found
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
                  \# Path parametersexport webhook_name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/${webhook_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a webhook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi

# there is a valid "webhook" in the system
WEBHOOK_NAME = environ["WEBHOOK_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    api_instance.delete_webhooks_integration(
        webhook_name=WEBHOOK_NAME,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a webhook returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook" in the system
WEBHOOK_NAME = ENV["WEBHOOK_NAME"]
p api_instance.delete_webhooks_integration(WEBHOOK_NAME)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a webhook returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    // there is a valid "webhook" in the system
    WebhookName := os.Getenv("WEBHOOK_NAME")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    r, err := api.DeleteWebhooksIntegration(ctx, WebhookName)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.DeleteWebhooksIntegration`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a webhook returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    // there is a valid "webhook" in the system
    String WEBHOOK_NAME = System.getenv("WEBHOOK_NAME");

    try {
      apiInstance.deleteWebhooksIntegration(WEBHOOK_NAME);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksIntegrationApi#deleteWebhooksIntegration");
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
// Delete a webhook returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "webhook" in the system
    let webhook_name = std::env::var("WEBHOOK_NAME").unwrap();
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api.delete_webhooks_integration(webhook_name.clone()).await;
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
 * Delete a webhook returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

// there is a valid "webhook" in the system
const WEBHOOK_NAME = process.env.WEBHOOK_NAME as string;

const params: v1.WebhooksIntegrationApiDeleteWebhooksIntegrationRequest = {
  webhookName: WEBHOOK_NAME,
};

apiInstance
  .deleteWebhooksIntegration(params)
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

## Create a custom variable{% #create-a-custom-variable %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variables      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variables      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables |

### Overview

Creates an endpoint with the name `<CUSTOM_VARIABLE_NAME>`. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)

Define a custom variable request body.

{% tab title="Model" %}

| Field                       | Type    | Description                                                                                                                 |
| --------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| is_secret [*required*] | boolean | Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload. |
| name [*required*]      | string  | The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`.                                                     |
| value [*required*]     | string  | Value of the custom variable.                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "is_secret": true,
  "name": "EXAMPLEWEBHOOKSINTEGRATION",
  "value": "CUSTOM_VARIABLE_VALUE"
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Custom variable for Webhook integration.

| Field                       | Type    | Description                                                                                                                                   |
| --------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| is_secret [*required*] | boolean | Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.                   |
| name [*required*]      | string  | The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores. |
| value                       | string  | Value of the custom variable. It won't be returned if the variable is secret.                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "is_secret": true,
  "name": "CUSTOM_VARIABLE_NAME",
  "value": "CUSTOM_VARIABLE_VALUE"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "is_secret": true,
  "name": "EXAMPLEWEBHOOKSINTEGRATION",
  "value": "CUSTOM_VARIABLE_VALUE"
}
EOF

#####

```go
// Create a custom variable returns "OK" response

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
    body := datadogV1.WebhooksIntegrationCustomVariable{
        IsSecret: true,
        Name:     "EXAMPLEWEBHOOKSINTEGRATION",
        Value:    "CUSTOM_VARIABLE_VALUE",
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    resp, r, err := api.CreateWebhooksIntegrationCustomVariable(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.CreateWebhooksIntegrationCustomVariable`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `WebhooksIntegrationApi.CreateWebhooksIntegrationCustomVariable`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a custom variable returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;
import com.datadog.api.client.v1.model.WebhooksIntegrationCustomVariable;
import com.datadog.api.client.v1.model.WebhooksIntegrationCustomVariableResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    WebhooksIntegrationCustomVariable body =
        new WebhooksIntegrationCustomVariable()
            .isSecret(true)
            .name("EXAMPLEWEBHOOKSINTEGRATION")
            .value("CUSTOM_VARIABLE_VALUE");

    try {
      WebhooksIntegrationCustomVariableResponse result =
          apiInstance.createWebhooksIntegrationCustomVariable(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling WebhooksIntegrationApi#createWebhooksIntegrationCustomVariable");
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
Create a custom variable returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration_custom_variable import WebhooksIntegrationCustomVariable

body = WebhooksIntegrationCustomVariable(
    is_secret=True,
    name="EXAMPLEWEBHOOKSINTEGRATION",
    value="CUSTOM_VARIABLE_VALUE",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.create_webhooks_integration_custom_variable(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a custom variable returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

body = DatadogAPIClient::V1::WebhooksIntegrationCustomVariable.new({
  is_secret: true,
  name: "EXAMPLEWEBHOOKSINTEGRATION",
  value: "CUSTOM_VARIABLE_VALUE",
})
p api_instance.create_webhooks_integration_custom_variable(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a custom variable returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;
use datadog_api_client::datadogV1::model::WebhooksIntegrationCustomVariable;

#[tokio::main]
async fn main() {
    let body = WebhooksIntegrationCustomVariable::new(
        true,
        "EXAMPLEWEBHOOKSINTEGRATION".to_string(),
        "CUSTOM_VARIABLE_VALUE".to_string(),
    );
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api.create_webhooks_integration_custom_variable(body).await;
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
 * Create a custom variable returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

const params: v1.WebhooksIntegrationApiCreateWebhooksIntegrationCustomVariableRequest =
  {
    body: {
      isSecret: true,
      name: "EXAMPLEWEBHOOKSINTEGRATION",
      value: "CUSTOM_VARIABLE_VALUE",
    },
  };

apiInstance
  .createWebhooksIntegrationCustomVariable(params)
  .then((data: v1.WebhooksIntegrationCustomVariableResponse) => {
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

## Get a custom variable{% #get-a-custom-variable %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |

### Overview



Shows the content of the custom variable with the name `<CUSTOM_VARIABLE_NAME>`.

If the custom variable is secret, the value does not return in the response payload.
This endpoint requires the `integrations_read` permission.


### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| custom_variable_name [*required*] | string | The name of the custom variable. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Custom variable for Webhook integration.

| Field                       | Type    | Description                                                                                                                                   |
| --------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| is_secret [*required*] | boolean | Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.                   |
| name [*required*]      | string  | The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores. |
| value                       | string  | Value of the custom variable. It won't be returned if the variable is secret.                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "is_secret": true,
  "name": "CUSTOM_VARIABLE_NAME",
  "value": "CUSTOM_VARIABLE_VALUE"
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

{% tab title="404" %}
Item Not Found
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
                  \# Path parametersexport custom_variable_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/${custom_variable_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a custom variable returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.get_webhooks_integration_custom_variable(
        custom_variable_name="custom_variable_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a custom variable returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new
p api_instance.get_webhooks_integration_custom_variable("custom_variable_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a custom variable returns "OK" response

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
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    resp, r, err := api.GetWebhooksIntegrationCustomVariable(ctx, "custom_variable_name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.GetWebhooksIntegrationCustomVariable`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `WebhooksIntegrationApi.GetWebhooksIntegrationCustomVariable`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a custom variable returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;
import com.datadog.api.client.v1.model.WebhooksIntegrationCustomVariableResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    try {
      WebhooksIntegrationCustomVariableResponse result =
          apiInstance.getWebhooksIntegrationCustomVariable("custom_variable_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling WebhooksIntegrationApi#getWebhooksIntegrationCustomVariable");
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
// Get a custom variable returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api
        .get_webhooks_integration_custom_variable("custom_variable_name".to_string())
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
 * Get a custom variable returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

const params: v1.WebhooksIntegrationApiGetWebhooksIntegrationCustomVariableRequest =
  {
    customVariableName: "custom_variable_name",
  };

apiInstance
  .getWebhooksIntegrationCustomVariable(params)
  .then((data: v1.WebhooksIntegrationCustomVariableResponse) => {
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

## Update a custom variable{% #update-a-custom-variable %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |

### Overview

Updates the endpoint with the name `<CUSTOM_VARIABLE_NAME>`. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| custom_variable_name [*required*] | string | The name of the custom variable. |

### Request

#### Body Data (required)

Update an existing custom variable request body.

{% tab title="Model" %}

| Field     | Type    | Description                                                                                                                                   |
| --------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| is_secret | boolean | Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.                   |
| name      | string  | The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores. |
| value     | string  | Value of the custom variable.                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "value": "variable-updated"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Custom variable for Webhook integration.

| Field                       | Type    | Description                                                                                                                                   |
| --------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| is_secret [*required*] | boolean | Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.                   |
| name [*required*]      | string  | The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores. |
| value                       | string  | Value of the custom variable. It won't be returned if the variable is secret.                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "is_secret": true,
  "name": "CUSTOM_VARIABLE_NAME",
  "value": "CUSTOM_VARIABLE_VALUE"
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

{% tab title="404" %}
Item Not Found
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
                          \# Path parametersexport custom_variable_name="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/${custom_variable_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "value": "variable-updated"
}
EOF

#####

```go
// Update a custom variable returns "OK" response

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
    // there is a valid "webhook_custom_variable" in the system
    WebhookCustomVariableName := os.Getenv("WEBHOOK_CUSTOM_VARIABLE_NAME")

    body := datadogV1.WebhooksIntegrationCustomVariableUpdateRequest{
        Value: datadog.PtrString("variable-updated"),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    resp, r, err := api.UpdateWebhooksIntegrationCustomVariable(ctx, WebhookCustomVariableName, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.UpdateWebhooksIntegrationCustomVariable`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `WebhooksIntegrationApi.UpdateWebhooksIntegrationCustomVariable`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a custom variable returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;
import com.datadog.api.client.v1.model.WebhooksIntegrationCustomVariableResponse;
import com.datadog.api.client.v1.model.WebhooksIntegrationCustomVariableUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    // there is a valid "webhook_custom_variable" in the system
    String WEBHOOK_CUSTOM_VARIABLE_NAME = System.getenv("WEBHOOK_CUSTOM_VARIABLE_NAME");

    WebhooksIntegrationCustomVariableUpdateRequest body =
        new WebhooksIntegrationCustomVariableUpdateRequest().value("variable-updated");

    try {
      WebhooksIntegrationCustomVariableResponse result =
          apiInstance.updateWebhooksIntegrationCustomVariable(WEBHOOK_CUSTOM_VARIABLE_NAME, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling WebhooksIntegrationApi#updateWebhooksIntegrationCustomVariable");
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
Update a custom variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration_custom_variable_update_request import (
    WebhooksIntegrationCustomVariableUpdateRequest,
)

# there is a valid "webhook_custom_variable" in the system
WEBHOOK_CUSTOM_VARIABLE_NAME = environ["WEBHOOK_CUSTOM_VARIABLE_NAME"]

body = WebhooksIntegrationCustomVariableUpdateRequest(
    value="variable-updated",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.update_webhooks_integration_custom_variable(
        custom_variable_name=WEBHOOK_CUSTOM_VARIABLE_NAME, body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a custom variable returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook_custom_variable" in the system
WEBHOOK_CUSTOM_VARIABLE_NAME = ENV["WEBHOOK_CUSTOM_VARIABLE_NAME"]

body = DatadogAPIClient::V1::WebhooksIntegrationCustomVariableUpdateRequest.new({
  value: "variable-updated",
})
p api_instance.update_webhooks_integration_custom_variable(WEBHOOK_CUSTOM_VARIABLE_NAME, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update a custom variable returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;
use datadog_api_client::datadogV1::model::WebhooksIntegrationCustomVariableUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "webhook_custom_variable" in the system
    let webhook_custom_variable_name = std::env::var("WEBHOOK_CUSTOM_VARIABLE_NAME").unwrap();
    let body =
        WebhooksIntegrationCustomVariableUpdateRequest::new().value("variable-updated".to_string());
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api
        .update_webhooks_integration_custom_variable(webhook_custom_variable_name.clone(), body)
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
 * Update a custom variable returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

// there is a valid "webhook_custom_variable" in the system
const WEBHOOK_CUSTOM_VARIABLE_NAME = process.env
  .WEBHOOK_CUSTOM_VARIABLE_NAME as string;

const params: v1.WebhooksIntegrationApiUpdateWebhooksIntegrationCustomVariableRequest =
  {
    body: {
      value: "variable-updated",
    },
    customVariableName: WEBHOOK_CUSTOM_VARIABLE_NAME,
  };

apiInstance
  .updateWebhooksIntegrationCustomVariable(params)
  .then((data: v1.WebhooksIntegrationCustomVariableResponse) => {
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

## Delete a custom variable{% #delete-a-custom-variable %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} |

### Overview

Deletes the endpoint with the name `<CUSTOM_VARIABLE_NAME>`. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| custom_variable_name [*required*] | string | The name of the custom variable. |

### Response

{% tab title="200" %}
OK
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

{% tab title="404" %}
Item Not Found
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
                  \# Path parametersexport custom_variable_name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/${custom_variable_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a custom variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi

# there is a valid "webhook_custom_variable" in the system
WEBHOOK_CUSTOM_VARIABLE_NAME = environ["WEBHOOK_CUSTOM_VARIABLE_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    api_instance.delete_webhooks_integration_custom_variable(
        custom_variable_name=WEBHOOK_CUSTOM_VARIABLE_NAME,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a custom variable returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook_custom_variable" in the system
WEBHOOK_CUSTOM_VARIABLE_NAME = ENV["WEBHOOK_CUSTOM_VARIABLE_NAME"]
p api_instance.delete_webhooks_integration_custom_variable(WEBHOOK_CUSTOM_VARIABLE_NAME)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a custom variable returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    // there is a valid "webhook_custom_variable" in the system
    WebhookCustomVariableName := os.Getenv("WEBHOOK_CUSTOM_VARIABLE_NAME")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewWebhooksIntegrationApi(apiClient)
    r, err := api.DeleteWebhooksIntegrationCustomVariable(ctx, WebhookCustomVariableName)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `WebhooksIntegrationApi.DeleteWebhooksIntegrationCustomVariable`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a custom variable returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.WebhooksIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WebhooksIntegrationApi apiInstance = new WebhooksIntegrationApi(defaultClient);

    // there is a valid "webhook_custom_variable" in the system
    String WEBHOOK_CUSTOM_VARIABLE_NAME = System.getenv("WEBHOOK_CUSTOM_VARIABLE_NAME");

    try {
      apiInstance.deleteWebhooksIntegrationCustomVariable(WEBHOOK_CUSTOM_VARIABLE_NAME);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling WebhooksIntegrationApi#deleteWebhooksIntegrationCustomVariable");
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
// Delete a custom variable returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_webhooks_integration::WebhooksIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "webhook_custom_variable" in the system
    let webhook_custom_variable_name = std::env::var("WEBHOOK_CUSTOM_VARIABLE_NAME").unwrap();
    let configuration = datadog::Configuration::new();
    let api = WebhooksIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_webhooks_integration_custom_variable(webhook_custom_variable_name.clone())
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
 * Delete a custom variable returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.WebhooksIntegrationApi(configuration);

// there is a valid "webhook_custom_variable" in the system
const WEBHOOK_CUSTOM_VARIABLE_NAME = process.env
  .WEBHOOK_CUSTOM_VARIABLE_NAME as string;

const params: v1.WebhooksIntegrationApiDeleteWebhooksIntegrationCustomVariableRequest =
  {
    customVariableName: WEBHOOK_CUSTOM_VARIABLE_NAME,
  };

apiInstance
  .deleteWebhooksIntegrationCustomVariable(params)
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
