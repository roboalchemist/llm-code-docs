# Source: https://docs.datadoghq.com/api/latest/pagerduty-integration.md

---
title: PagerDuty Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > PagerDuty Integration
---

# PagerDuty Integration

Configure your [Datadog-PagerDuty integration](https://docs.datadoghq.com/integrations/pagerduty/) directly through the Datadog API.

## Create a new service object{% #create-a-new-service-object %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                           |
| ----------------- | -------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/services |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/services |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/services      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/services      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/pagerduty/configuration/services     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/services |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services |

### Overview

Create a new service object in the PagerDuty integration. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)

Create a new service object request body.

{% tab title="Model" %}

| Field                          | Type   | Description                                                   |
| ------------------------------ | ------ | ------------------------------------------------------------- |
| service_key [*required*]  | string | Your service key in PagerDuty.                                |
| service_name [*required*] | string | Your service name associated with a service key in PagerDuty. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "service_key": "",
  "service_name": ""
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
PagerDuty service object name.

| Field                          | Type   | Description                                            |
| ------------------------------ | ------ | ------------------------------------------------------ |
| service_name [*required*] | string | Your service name associated service key in PagerDuty. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "service_name": ""
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "service_key": "",
  "service_name": ""
}
EOF

#####

```python
"""
Create a new service object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi
from datadog_api_client.v1.model.pager_duty_service import PagerDutyService

body = PagerDutyService(
    service_key="",
    service_name="",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PagerDutyIntegrationApi(api_client)
    response = api_instance.create_pager_duty_integration_service(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a new service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new

body = DatadogAPIClient::V1::PagerDutyService.new({
  service_key: "",
  service_name: "",
})
p api_instance.create_pager_duty_integration_service(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Create a new service object returns "OK" response

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
    body := datadogV1.PagerDutyService{
        ServiceKey:  "",
        ServiceName: "",
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewPagerDutyIntegrationApi(apiClient)
    resp, r, err := api.CreatePagerDutyIntegrationService(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PagerDutyIntegrationApi.CreatePagerDutyIntegrationService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `PagerDutyIntegrationApi.CreatePagerDutyIntegrationService`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a new service object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.PagerDutyIntegrationApi;
import com.datadog.api.client.v1.model.PagerDutyService;
import com.datadog.api.client.v1.model.PagerDutyServiceName;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PagerDutyIntegrationApi apiInstance = new PagerDutyIntegrationApi(defaultClient);

    PagerDutyService body = new PagerDutyService().serviceKey("").serviceName("");

    try {
      PagerDutyServiceName result = apiInstance.createPagerDutyIntegrationService(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling PagerDutyIntegrationApi#createPagerDutyIntegrationService");
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
// Create a new service object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_pager_duty_integration::PagerDutyIntegrationAPI;
use datadog_api_client::datadogV1::model::PagerDutyService;

#[tokio::main]
async fn main() {
    let body = PagerDutyService::new("".to_string(), "".to_string());
    let configuration = datadog::Configuration::new();
    let api = PagerDutyIntegrationAPI::with_config(configuration);
    let resp = api.create_pager_duty_integration_service(body).await;
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
 * Create a new service object returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.PagerDutyIntegrationApi(configuration);

const params: v1.PagerDutyIntegrationApiCreatePagerDutyIntegrationServiceRequest =
  {
    body: {
      serviceKey: "",
      serviceName: "",
    },
  };

apiInstance
  .createPagerDutyIntegrationService(params)
  .then((data: v1.PagerDutyServiceName) => {
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

## Get a single service object{% #get-a-single-service-object %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/services/{service_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/services/{service_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |

### Overview

Get service name in the Datadog-PagerDuty integration. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description       |
| ------------------------------ | ------ | ----------------- |
| service_name [*required*] | string | The service name. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
PagerDuty service object name.

| Field                          | Type   | Description                                            |
| ------------------------------ | ------ | ------------------------------------------------------ |
| service_name [*required*] | string | Your service name associated service key in PagerDuty. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "service_name": ""
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
                  \# Path parametersexport service_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/${service_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a single service object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PagerDutyIntegrationApi(api_client)
    response = api_instance.get_pager_duty_integration_service(
        service_name="service_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a single service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new
p api_instance.get_pager_duty_integration_service("service_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a single service object returns "OK" response

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
    api := datadogV1.NewPagerDutyIntegrationApi(apiClient)
    resp, r, err := api.GetPagerDutyIntegrationService(ctx, "service_name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PagerDutyIntegrationApi.GetPagerDutyIntegrationService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `PagerDutyIntegrationApi.GetPagerDutyIntegrationService`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a single service object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.PagerDutyIntegrationApi;
import com.datadog.api.client.v1.model.PagerDutyServiceName;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PagerDutyIntegrationApi apiInstance = new PagerDutyIntegrationApi(defaultClient);

    try {
      PagerDutyServiceName result = apiInstance.getPagerDutyIntegrationService("service_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling PagerDutyIntegrationApi#getPagerDutyIntegrationService");
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
// Get a single service object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_pager_duty_integration::PagerDutyIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = PagerDutyIntegrationAPI::with_config(configuration);
    let resp = api
        .get_pager_duty_integration_service("service_name".to_string())
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
 * Get a single service object returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.PagerDutyIntegrationApi(configuration);

const params: v1.PagerDutyIntegrationApiGetPagerDutyIntegrationServiceRequest =
  {
    serviceName: "service_name",
  };

apiInstance
  .getPagerDutyIntegrationService(params)
  .then((data: v1.PagerDutyServiceName) => {
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

## Update a single service object{% #update-a-single-service-object %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/services/{service_name}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/services/{service_name}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |

### Overview

Update a single service object in the Datadog-PagerDuty integration. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| service_name [*required*] | string | The service name |

### Request

#### Body Data (required)

Update an existing service object request body.

{% tab title="Model" %}

| Field                         | Type   | Description                    |
| ----------------------------- | ------ | ------------------------------ |
| service_key [*required*] | string | Your service key in PagerDuty. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "service_key": ""
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
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
                  \# Path parametersexport service_name="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/${service_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "service_key": ""
}
EOF

#####

```python
"""
Update a single service object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi
from datadog_api_client.v1.model.pager_duty_service_key import PagerDutyServiceKey

body = PagerDutyServiceKey(
    service_key="",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PagerDutyIntegrationApi(api_client)
    api_instance.update_pager_duty_integration_service(service_name="service_name", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a single service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new

body = DatadogAPIClient::V1::PagerDutyServiceKey.new({
  service_key: "",
})
p api_instance.update_pager_duty_integration_service("service_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update a single service object returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.PagerDutyServiceKey{
        ServiceKey: "",
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewPagerDutyIntegrationApi(apiClient)
    r, err := api.UpdatePagerDutyIntegrationService(ctx, "service_name", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PagerDutyIntegrationApi.UpdatePagerDutyIntegrationService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a single service object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.PagerDutyIntegrationApi;
import com.datadog.api.client.v1.model.PagerDutyServiceKey;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PagerDutyIntegrationApi apiInstance = new PagerDutyIntegrationApi(defaultClient);

    PagerDutyServiceKey body = new PagerDutyServiceKey().serviceKey("");

    try {
      apiInstance.updatePagerDutyIntegrationService("service_name", body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling PagerDutyIntegrationApi#updatePagerDutyIntegrationService");
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
// Update a single service object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_pager_duty_integration::PagerDutyIntegrationAPI;
use datadog_api_client::datadogV1::model::PagerDutyServiceKey;

#[tokio::main]
async fn main() {
    let body = PagerDutyServiceKey::new("".to_string());
    let configuration = datadog::Configuration::new();
    let api = PagerDutyIntegrationAPI::with_config(configuration);
    let resp = api
        .update_pager_duty_integration_service("service_name".to_string(), body)
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
 * Update a single service object returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.PagerDutyIntegrationApi(configuration);

const params: v1.PagerDutyIntegrationApiUpdatePagerDutyIntegrationServiceRequest =
  {
    body: {
      serviceKey: "",
    },
    serviceName: "service_name",
  };

apiInstance
  .updatePagerDutyIntegrationService(params)
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

## Delete a single service object{% #delete-a-single-service-object %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/services/{service_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/services/{service_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name} |

### Overview

Delete a single service object in the Datadog-PagerDuty integration. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| service_name [*required*] | string | The service name |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport service_name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/${service_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a single service object returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PagerDutyIntegrationApi(api_client)
    api_instance.delete_pager_duty_integration_service(
        service_name="service_name",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a single service object returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new
api_instance.delete_pager_duty_integration_service("service_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a single service object returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewPagerDutyIntegrationApi(apiClient)
    r, err := api.DeletePagerDutyIntegrationService(ctx, "service_name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PagerDutyIntegrationApi.DeletePagerDutyIntegrationService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a single service object returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.PagerDutyIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PagerDutyIntegrationApi apiInstance = new PagerDutyIntegrationApi(defaultClient);

    try {
      apiInstance.deletePagerDutyIntegrationService("service_name");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling PagerDutyIntegrationApi#deletePagerDutyIntegrationService");
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
// Delete a single service object returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_pager_duty_integration::PagerDutyIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = PagerDutyIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_pager_duty_integration_service("service_name".to_string())
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
 * Delete a single service object returns "No Content" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.PagerDutyIntegrationApi(configuration);

const params: v1.PagerDutyIntegrationApiDeletePagerDutyIntegrationServiceRequest =
  {
    serviceName: "service_name",
  };

apiInstance
  .deletePagerDutyIntegrationService(params)
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
