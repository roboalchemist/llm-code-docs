# Source: https://docs.datadoghq.com/api/latest/webhooks-integration

# Webhooks Integration
Configure your Datadog-Webhooks integration directly through the Datadog API. See the [Webhooks integration page](https://docs.datadoghq.com/integrations/webhooks) for more information.
## [Create a webhooks integration](https://docs.datadoghq.com/api/latest/webhooks-integration/#create-a-webhooks-integration)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#create-a-webhooks-integration-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhookshttps://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhookshttps://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhookshttps://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhookshttps://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhookshttps://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhookshttps://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks
### Overview
Creates an endpoint with the name `<WEBHOOK_NAME>`. This endpoint requires the `create_webhooks` permission.
OAuth apps require the `create_webhooks` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#webhooks-integration) to access this endpoint.
### Request
#### Body Data (required)
Create a webhooks integration request body.
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Expand All
Field
Type
Description
custom_headers
string
If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.
encode_as
enum
Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`
default: `json`
name [_required_]
string
The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).
payload
string
If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage).
url [_required_]
string
URL of the webhook.
```
{
  "name": "Example-Webhooks-Integration",
  "url": "https://example.com/webhook"
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegration-201-v1)
  * [400](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Datadog-Webhooks integration.
Expand All
Field
Type
Description
custom_headers
string
If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.
encode_as
enum
Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`
default: `json`
name [_required_]
string
The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).
payload
string
If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage).
url [_required_]
string
URL of the webhook.
```
{
  "custom_headers": "string",
  "encode_as": "string",
  "name": "WEBHOOK_NAME",
  "payload": "string",
  "url": "https://example.com/webhook"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Create a webhooks integration returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks" \
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

                        
```

#####  Create a webhooks integration returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a webhooks integration returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create a webhooks integration returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a webhooks integration returns "OK" response
```
# Create a webhooks integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

body = DatadogAPIClient::V1::WebhooksIntegration.new({
  name: "Example-Webhooks-Integration",
  url: "https://example.com/webhook",
})
p api_instance.create_webhooks_integration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a webhooks integration returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create a webhooks integration returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a webhook integration](https://docs.datadoghq.com/api/latest/webhooks-integration/#get-a-webhook-integration)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#get-a-webhook-integration-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}
### Overview
Gets the content of the webhook with the name `<WEBHOOK_NAME>`. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
webhook_name [_required_]
string
The name of the webhook.
### Response
  * [200](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegration-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegration-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Datadog-Webhooks integration.
Expand All
Field
Type
Description
custom_headers
string
If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.
encode_as
enum
Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`
default: `json`
name [_required_]
string
The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).
payload
string
If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage).
url [_required_]
string
URL of the webhook.
```
{
  "custom_headers": "string",
  "encode_as": "string",
  "name": "WEBHOOK_NAME",
  "payload": "string",
  "url": "https://example.com/webhook"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Get a webhook integration
Copy
```
                  # Path parameters  
export webhook_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/${webhook_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a webhook integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a webhook integration
```
# Get a webhook integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook" in the system
WEBHOOK_NAME = ENV["WEBHOOK_NAME"]
p api_instance.get_webhooks_integration(WEBHOOK_NAME)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a webhook integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a webhook integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a webhook integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a webhook integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a webhook](https://docs.datadoghq.com/api/latest/webhooks-integration/#update-a-webhook)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#update-a-webhook-v1)


PUT https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}
### Overview
Updates the endpoint with the name `<WEBHOOK_NAME>`. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
webhook_name [_required_]
string
The name of the webhook.
### Request
#### Body Data (required)
Update an existing Datadog-Webhooks integration.
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Expand All
Field
Type
Description
custom_headers
string
If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.
encode_as
enum
Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`
default: `json`
name
string
The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).
payload
string
If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage).
url
string
URL of the webhook.
```
{
  "url": "https://example.com/webhook-updated"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegration-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegration-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Datadog-Webhooks integration.
Expand All
Field
Type
Description
custom_headers
string
If `null`, uses no header. If given a JSON payload, these will be headers attached to your webhook.
encode_as
enum
Encoding type. Can be given either `json` or `form`. Allowed enum values: `json,form`
default: `json`
name [_required_]
string
The name of the webhook. It corresponds with `<WEBHOOK_NAME>`. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).
payload
string
If `null`, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage).
url [_required_]
string
URL of the webhook.
```
{
  "custom_headers": "string",
  "encode_as": "string",
  "name": "WEBHOOK_NAME",
  "payload": "string",
  "url": "https://example.com/webhook"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Update a webhook returns "OK" response
Copy
```
                          # Path parameters  
export webhook_name="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/${webhook_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "url": "https://example.com/webhook-updated"
}
EOF  

                        
```

#####  Update a webhook returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a webhook returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a webhook returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a webhook returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a webhook returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a webhook returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete a webhook](https://docs.datadoghq.com/api/latest/webhooks-integration/#delete-a-webhook)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#delete-a-webhook-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}
### Overview
Deletes the endpoint with the name `<WEBHOOK NAME>`. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
webhook_name [_required_]
string
The name of the webhook.
### Response
  * [200](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegration-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegration-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegration-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegration-429-v1)


OK
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Delete a webhook
Copy
```
                  # Path parameters  
export webhook_name="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks/${webhook_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a webhook
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a webhook
```
# Delete a webhook returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook" in the system
WEBHOOK_NAME = ENV["WEBHOOK_NAME"]
p api_instance.delete_webhooks_integration(WEBHOOK_NAME)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a webhook
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a webhook
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete a webhook
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete a webhook
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a custom variable](https://docs.datadoghq.com/api/latest/webhooks-integration/#create-a-custom-variable)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#create-a-custom-variable-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variableshttps://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variableshttps://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variableshttps://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variableshttps://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variableshttps://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variableshttps://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables
### Overview
Creates an endpoint with the name `<CUSTOM_VARIABLE_NAME>`. This endpoint requires the `manage_integrations` permission.
### Request
#### Body Data (required)
Define a custom variable request body.
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Expand All
Field
Type
Description
is_secret [_required_]
boolean
Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.
name [_required_]
string
The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`.
value [_required_]
string
Value of the custom variable.
```
{
  "is_secret": true,
  "name": "EXAMPLEWEBHOOKSINTEGRATION",
  "value": "CUSTOM_VARIABLE_VALUE"
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegrationCustomVariable-201-v1)
  * [400](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegrationCustomVariable-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegrationCustomVariable-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#CreateWebhooksIntegrationCustomVariable-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Custom variable for Webhook integration.
Expand All
Field
Type
Description
is_secret [_required_]
boolean
Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.
name [_required_]
string
The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores.
value
string
Value of the custom variable. It won't be returned if the variable is secret.
```
{
  "is_secret": true,
  "name": "CUSTOM_VARIABLE_NAME",
  "value": "CUSTOM_VARIABLE_VALUE"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Create a custom variable returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables" \
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

                        
```

#####  Create a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a custom variable](https://docs.datadoghq.com/api/latest/webhooks-integration/#get-a-custom-variable)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#get-a-custom-variable-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}
### Overview
Shows the content of the custom variable with the name `<CUSTOM_VARIABLE_NAME>`.
If the custom variable is secret, the value does not return in the response payload.
This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
custom_variable_name [_required_]
string
The name of the custom variable.
### Response
  * [200](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegrationCustomVariable-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegrationCustomVariable-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegrationCustomVariable-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegrationCustomVariable-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#GetWebhooksIntegrationCustomVariable-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Custom variable for Webhook integration.
Expand All
Field
Type
Description
is_secret [_required_]
boolean
Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.
name [_required_]
string
The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores.
value
string
Value of the custom variable. It won't be returned if the variable is secret.
```
{
  "is_secret": true,
  "name": "CUSTOM_VARIABLE_NAME",
  "value": "CUSTOM_VARIABLE_VALUE"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Get a custom variable
Copy
```
                  # Path parameters  
export custom_variable_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/${custom_variable_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a custom variable
```
# Get a custom variable returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new
p api_instance.get_webhooks_integration_custom_variable("custom_variable_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a custom variable](https://docs.datadoghq.com/api/latest/webhooks-integration/#update-a-custom-variable)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#update-a-custom-variable-v1)


PUT https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}
### Overview
Updates the endpoint with the name `<CUSTOM_VARIABLE_NAME>`. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
custom_variable_name [_required_]
string
The name of the custom variable.
### Request
#### Body Data (required)
Update an existing custom variable request body.
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Expand All
Field
Type
Description
is_secret
boolean
Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.
name
string
The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores.
value
string
Value of the custom variable.
```
{
  "value": "variable-updated"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegrationCustomVariable-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegrationCustomVariable-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegrationCustomVariable-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegrationCustomVariable-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#UpdateWebhooksIntegrationCustomVariable-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


Custom variable for Webhook integration.
Expand All
Field
Type
Description
is_secret [_required_]
boolean
Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.
name [_required_]
string
The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores.
value
string
Value of the custom variable. It won't be returned if the variable is secret.
```
{
  "is_secret": true,
  "name": "CUSTOM_VARIABLE_NAME",
  "value": "CUSTOM_VARIABLE_VALUE"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Update a custom variable returns "OK" response
Copy
```
                          # Path parameters  
export custom_variable_name="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/${custom_variable_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "value": "variable-updated"
}
EOF  

                        
```

#####  Update a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a custom variable returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete a custom variable](https://docs.datadoghq.com/api/latest/webhooks-integration/#delete-a-custom-variable)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/webhooks-integration/#delete-a-custom-variable-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.ap2.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.datadoghq.eu/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.ddog-gov.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.us3.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}
### Overview
Deletes the endpoint with the name `<CUSTOM_VARIABLE_NAME>`. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
custom_variable_name [_required_]
string
The name of the custom variable.
### Response
  * [200](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegrationCustomVariable-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegrationCustomVariable-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegrationCustomVariable-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/webhooks-integration/#DeleteWebhooksIntegrationCustomVariable-429-v1)


OK
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/webhooks-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/webhooks-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/webhooks-integration/?code-lang=typescript)


#####  Delete a custom variable
Copy
```
                  # Path parameters  
export custom_variable_name="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/webhooks/configuration/custom-variables/${custom_variable_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a custom variable
```
# Delete a custom variable returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::WebhooksIntegrationAPI.new

# there is a valid "webhook_custom_variable" in the system
WEBHOOK_CUSTOM_VARIABLE_NAME = ENV["WEBHOOK_CUSTOM_VARIABLE_NAME"]
p api_instance.delete_webhooks_integration_custom_variable(WEBHOOK_CUSTOM_VARIABLE_NAME)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete a custom variable
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=8d868fcf-e199-47ad-ae4e-d7c54d0bc1b7&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=bb61568f-0fc7-4acf-b4b8-6665c7401b04&pt=Webhooks%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fwebhooks-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=8d868fcf-e199-47ad-ae4e-d7c54d0bc1b7&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=bb61568f-0fc7-4acf-b4b8-6665c7401b04&pt=Webhooks%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fwebhooks-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=e6e99fed-6316-4003-8263-b022f4471efa&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Webhooks%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fwebhooks-integration%2F&r=&lt=5089&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=65839)
