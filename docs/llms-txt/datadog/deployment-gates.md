# Source: https://docs.datadoghq.com/api/latest/deployment-gates.md

---
title: Deployment Gates
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Deployment Gates
---

# Deployment Gates

Manage Deployment Gates using this API to reduce the likelihood and impact of incidents caused by deployments. See the [Deployment Gates documentation](https://docs.datadoghq.com/deployment_gates/) for more information.

## Create deployment gate{% #create-deployment-gate %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/deployment_gates |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/deployment_gates |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/deployment_gates      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/deployment_gates      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/deployment_gates     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/deployment_gates |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/deployment_gates |

### Overview

Endpoint to create a deployment gate. This endpoint requires the `deployment_gates_write` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                           |
| ------------ | ---------------------------- | ------- | --------------------------------------------------------------------- |
|              | data [*required*]       | object  | Parameters for creating a deployment gate.                            |
| data         | attributes [*required*] | object  | Parameters for creating a deployment gate.                            |
| attributes   | dry_run                      | boolean | Whether this gate is run in dry-run mode.                             |
| attributes   | env [*required*]        | string  | The environment of the deployment gate.                               |
| attributes   | identifier                   | string  | The identifier of the deployment gate.                                |
| attributes   | service [*required*]    | string  | The service of the deployment gate.                                   |
| data         | type [*required*]       | enum    | Deployment gate resource type. Allowed enum values: `deployment_gate` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "dry_run": false,
      "env": "production",
      "identifier": "my-gate-1",
      "service": "my-service"
    },
    "type": "deployment_gate"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a deployment gate.

| Parent field | Field                        | Type      | Description                                                           |
| ------------ | ---------------------------- | --------- | --------------------------------------------------------------------- |
|              | data                         | object    | Data for a deployment gate.                                           |
| data         | attributes [*required*] | object    | Basic information about a deployment gate.                            |
| attributes   | created_at [*required*] | date-time | The timestamp when the deployment gate was created.                   |
| attributes   | created_by [*required*] | object    | Information about the user who created the deployment gate.           |
| created_by   | handle                       | string    | The handle of the user who created the deployment rule.               |
| created_by   | id [*required*]         | string    | The ID of the user who created the deployment rule.                   |
| created_by   | name                         | string    | The name of the user who created the deployment rule.                 |
| attributes   | dry_run [*required*]    | boolean   | Whether this gate is run in dry-run mode.                             |
| attributes   | env [*required*]        | string    | The environment of the deployment gate.                               |
| attributes   | identifier [*required*] | string    | The identifier of the deployment gate.                                |
| attributes   | service [*required*]    | string    | The service of the deployment gate.                                   |
| attributes   | updated_at                   | date-time | The timestamp when the deployment gate was last updated.              |
| attributes   | updated_by                   | object    | Information about the user who updated the deployment gate.           |
| updated_by   | handle                       | string    | The handle of the user who updated the deployment rule.               |
| updated_by   | id [*required*]         | string    | The ID of the user who updated the deployment rule.                   |
| updated_by   | name                         | string    | The name of the user who updated the deployment rule.                 |
| data         | id [*required*]         | string    | Unique identifier of the deployment gate.                             |
| data         | type [*required*]       | enum      | Deployment gate resource type. Allowed enum values: `deployment_gate` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2021-01-01T00:00:00Z",
      "created_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      },
      "dry_run": false,
      "env": "production",
      "identifier": "pre",
      "service": "my-service",
      "updated_at": "2021-01-01T00:00:00Z",
      "updated_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      }
    },
    "id": "1111-2222-3333-4444-555566667777",
    "type": "deployment_gate"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "dry_run": false,
      "env": "production",
      "identifier": "my-gate-1",
      "service": "my-service"
    },
    "type": "deployment_gate"
  }
}
EOF

#####

```go
// Create deployment gate returns "OK" response

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
    body := datadogV2.CreateDeploymentGateParams{
        Data: datadogV2.CreateDeploymentGateParamsData{
            Attributes: datadogV2.CreateDeploymentGateParamsDataAttributes{
                DryRun:     datadog.PtrBool(false),
                Env:        "production",
                Identifier: datadog.PtrString("my-gate-1"),
                Service:    "my-service",
            },
            Type: datadogV2.DEPLOYMENTGATEDATATYPE_DEPLOYMENT_GATE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateDeploymentGate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    resp, r, err := api.CreateDeploymentGate(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.CreateDeploymentGate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DeploymentGatesApi.CreateDeploymentGate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create deployment gate returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;
import com.datadog.api.client.v2.model.CreateDeploymentGateParams;
import com.datadog.api.client.v2.model.CreateDeploymentGateParamsData;
import com.datadog.api.client.v2.model.CreateDeploymentGateParamsDataAttributes;
import com.datadog.api.client.v2.model.DeploymentGateDataType;
import com.datadog.api.client.v2.model.DeploymentGateResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createDeploymentGate", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    CreateDeploymentGateParams body =
        new CreateDeploymentGateParams()
            .data(
                new CreateDeploymentGateParamsData()
                    .attributes(
                        new CreateDeploymentGateParamsDataAttributes()
                            .dryRun(false)
                            .env("production")
                            .identifier("my-gate-1")
                            .service("my-service"))
                    .type(DeploymentGateDataType.DEPLOYMENT_GATE));

    try {
      DeploymentGateResponse result = apiInstance.createDeploymentGate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#createDeploymentGate");
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
Create deployment gate returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.create_deployment_gate_params import CreateDeploymentGateParams
from datadog_api_client.v2.model.create_deployment_gate_params_data import CreateDeploymentGateParamsData
from datadog_api_client.v2.model.create_deployment_gate_params_data_attributes import (
    CreateDeploymentGateParamsDataAttributes,
)
from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType

body = CreateDeploymentGateParams(
    data=CreateDeploymentGateParamsData(
        attributes=CreateDeploymentGateParamsDataAttributes(
            dry_run=False,
            env="production",
            identifier="my-gate-1",
            service="my-service",
        ),
        type=DeploymentGateDataType.DEPLOYMENT_GATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_deployment_gate"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.create_deployment_gate(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create deployment gate returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_deployment_gate".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

body = DatadogAPIClient::V2::CreateDeploymentGateParams.new({
  data: DatadogAPIClient::V2::CreateDeploymentGateParamsData.new({
    attributes: DatadogAPIClient::V2::CreateDeploymentGateParamsDataAttributes.new({
      dry_run: false,
      env: "production",
      identifier: "my-gate-1",
      service: "my-service",
    }),
    type: DatadogAPIClient::V2::DeploymentGateDataType::DEPLOYMENT_GATE,
  }),
})
p api_instance.create_deployment_gate(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create deployment gate returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;
use datadog_api_client::datadogV2::model::CreateDeploymentGateParams;
use datadog_api_client::datadogV2::model::CreateDeploymentGateParamsData;
use datadog_api_client::datadogV2::model::CreateDeploymentGateParamsDataAttributes;
use datadog_api_client::datadogV2::model::DeploymentGateDataType;

#[tokio::main]
async fn main() {
    let body = CreateDeploymentGateParams::new(CreateDeploymentGateParamsData::new(
        CreateDeploymentGateParamsDataAttributes::new(
            "production".to_string(),
            "my-service".to_string(),
        )
        .dry_run(false)
        .identifier("my-gate-1".to_string()),
        DeploymentGateDataType::DEPLOYMENT_GATE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateDeploymentGate", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api.create_deployment_gate(body).await;
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
 * Create deployment gate returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createDeploymentGate"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

const params: v2.DeploymentGatesApiCreateDeploymentGateRequest = {
  body: {
    data: {
      attributes: {
        dryRun: false,
        env: "production",
        identifier: "my-gate-1",
        service: "my-service",
      },
      type: "deployment_gate",
    },
  },
};

apiInstance
  .createDeploymentGate(params)
  .then((data: v2.DeploymentGateResponse) => {
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

## Get deployment gate{% #get-deployment-gate %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/deployment_gates/{id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/deployment_gates/{id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/deployment_gates/{id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/deployment_gates/{id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/deployment_gates/{id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/deployment_gates/{id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/deployment_gates/{id} |

### Overview

Endpoint to get a deployment gate. This endpoint requires the `deployment_gates_read` permission.

### Arguments

#### Path Parameters

| Name                 | Type   | Description                    |
| -------------------- | ------ | ------------------------------ |
| id [*required*] | string | The ID of the deployment gate. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a deployment gate.

| Parent field | Field                        | Type      | Description                                                           |
| ------------ | ---------------------------- | --------- | --------------------------------------------------------------------- |
|              | data                         | object    | Data for a deployment gate.                                           |
| data         | attributes [*required*] | object    | Basic information about a deployment gate.                            |
| attributes   | created_at [*required*] | date-time | The timestamp when the deployment gate was created.                   |
| attributes   | created_by [*required*] | object    | Information about the user who created the deployment gate.           |
| created_by   | handle                       | string    | The handle of the user who created the deployment rule.               |
| created_by   | id [*required*]         | string    | The ID of the user who created the deployment rule.                   |
| created_by   | name                         | string    | The name of the user who created the deployment rule.                 |
| attributes   | dry_run [*required*]    | boolean   | Whether this gate is run in dry-run mode.                             |
| attributes   | env [*required*]        | string    | The environment of the deployment gate.                               |
| attributes   | identifier [*required*] | string    | The identifier of the deployment gate.                                |
| attributes   | service [*required*]    | string    | The service of the deployment gate.                                   |
| attributes   | updated_at                   | date-time | The timestamp when the deployment gate was last updated.              |
| attributes   | updated_by                   | object    | Information about the user who updated the deployment gate.           |
| updated_by   | handle                       | string    | The handle of the user who updated the deployment rule.               |
| updated_by   | id [*required*]         | string    | The ID of the user who updated the deployment rule.                   |
| updated_by   | name                         | string    | The name of the user who updated the deployment rule.                 |
| data         | id [*required*]         | string    | Unique identifier of the deployment gate.                             |
| data         | type [*required*]       | enum      | Deployment gate resource type. Allowed enum values: `deployment_gate` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2021-01-01T00:00:00Z",
      "created_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      },
      "dry_run": false,
      "env": "production",
      "identifier": "pre",
      "service": "my-service",
      "updated_at": "2021-01-01T00:00:00Z",
      "updated_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      }
    },
    "id": "1111-2222-3333-4444-555566667777",
    "type": "deployment_gate"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
Deployment gate not found.
{% tab title="Model" %}
Deployment gate not found.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get deployment gate returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_deployment_gate"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.get_deployment_gate(
        id=DEPLOYMENT_GATE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get deployment gate returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_deployment_gate".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]
p api_instance.get_deployment_gate(DEPLOYMENT_GATE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get deployment gate returns "OK" response

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
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetDeploymentGate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    resp, r, err := api.GetDeploymentGate(ctx, DeploymentGateDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.GetDeploymentGate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DeploymentGatesApi.GetDeploymentGate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get deployment gate returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;
import com.datadog.api.client.v2.model.DeploymentGateResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getDeploymentGate", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    try {
      DeploymentGateResponse result = apiInstance.getDeploymentGate(DEPLOYMENT_GATE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#getDeploymentGate");
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

```rust
// Get deployment gate returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetDeploymentGate", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .get_deployment_gate(deployment_gate_data_id.clone())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get deployment gate returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getDeploymentGate"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

const params: v2.DeploymentGatesApiGetDeploymentGateRequest = {
  id: DEPLOYMENT_GATE_DATA_ID,
};

apiInstance
  .getDeploymentGate(params)
  .then((data: v2.DeploymentGateResponse) => {
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

## Update deployment gate{% #update-deployment-gate %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/deployment_gates/{id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/deployment_gates/{id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/deployment_gates/{id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/deployment_gates/{id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/deployment_gates/{id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/deployment_gates/{id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/deployment_gates/{id} |

### Overview

Endpoint to update a deployment gate. This endpoint requires the `deployment_gates_write` permission.

### Arguments

#### Path Parameters

| Name                 | Type   | Description                    |
| -------------------- | ------ | ------------------------------ |
| id [*required*] | string | The ID of the deployment gate. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                           |
| ------------ | ---------------------------- | ------- | --------------------------------------------------------------------- |
|              | data [*required*]       | object  | Parameters for updating a deployment gate.                            |
| data         | attributes [*required*] | object  | Attributes for updating a deployment gate.                            |
| attributes   | dry_run [*required*]    | boolean | Whether to run in dry-run mode.                                       |
| data         | id [*required*]         | string  | Unique identifier of the deployment gate.                             |
| data         | type [*required*]       | enum    | Deployment gate resource type. Allowed enum values: `deployment_gate` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "dry_run": false
    },
    "id": "12345678-1234-1234-1234-123456789012",
    "type": "deployment_gate"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a deployment gate.

| Parent field | Field                        | Type      | Description                                                           |
| ------------ | ---------------------------- | --------- | --------------------------------------------------------------------- |
|              | data                         | object    | Data for a deployment gate.                                           |
| data         | attributes [*required*] | object    | Basic information about a deployment gate.                            |
| attributes   | created_at [*required*] | date-time | The timestamp when the deployment gate was created.                   |
| attributes   | created_by [*required*] | object    | Information about the user who created the deployment gate.           |
| created_by   | handle                       | string    | The handle of the user who created the deployment rule.               |
| created_by   | id [*required*]         | string    | The ID of the user who created the deployment rule.                   |
| created_by   | name                         | string    | The name of the user who created the deployment rule.                 |
| attributes   | dry_run [*required*]    | boolean   | Whether this gate is run in dry-run mode.                             |
| attributes   | env [*required*]        | string    | The environment of the deployment gate.                               |
| attributes   | identifier [*required*] | string    | The identifier of the deployment gate.                                |
| attributes   | service [*required*]    | string    | The service of the deployment gate.                                   |
| attributes   | updated_at                   | date-time | The timestamp when the deployment gate was last updated.              |
| attributes   | updated_by                   | object    | Information about the user who updated the deployment gate.           |
| updated_by   | handle                       | string    | The handle of the user who updated the deployment rule.               |
| updated_by   | id [*required*]         | string    | The ID of the user who updated the deployment rule.                   |
| updated_by   | name                         | string    | The name of the user who updated the deployment rule.                 |
| data         | id [*required*]         | string    | Unique identifier of the deployment gate.                             |
| data         | type [*required*]       | enum      | Deployment gate resource type. Allowed enum values: `deployment_gate` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2021-01-01T00:00:00Z",
      "created_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      },
      "dry_run": false,
      "env": "production",
      "identifier": "pre",
      "service": "my-service",
      "updated_at": "2021-01-01T00:00:00Z",
      "updated_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      }
    },
    "id": "1111-2222-3333-4444-555566667777",
    "type": "deployment_gate"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
Deployment gate not found.
{% tab title="Model" %}
Deployment gate not found.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "dry_run": false
    },
    "id": "12345678-1234-1234-1234-123456789012",
    "type": "deployment_gate"
  }
}
EOF

#####

```go
// Update deployment gate returns "OK" response

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
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    body := datadogV2.UpdateDeploymentGateParams{
        Data: datadogV2.UpdateDeploymentGateParamsData{
            Attributes: datadogV2.UpdateDeploymentGateParamsDataAttributes{
                DryRun: false,
            },
            Id:   "12345678-1234-1234-1234-123456789012",
            Type: datadogV2.DEPLOYMENTGATEDATATYPE_DEPLOYMENT_GATE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.UpdateDeploymentGate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    resp, r, err := api.UpdateDeploymentGate(ctx, DeploymentGateDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.UpdateDeploymentGate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DeploymentGatesApi.UpdateDeploymentGate`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update deployment gate returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;
import com.datadog.api.client.v2.model.DeploymentGateDataType;
import com.datadog.api.client.v2.model.DeploymentGateResponse;
import com.datadog.api.client.v2.model.UpdateDeploymentGateParams;
import com.datadog.api.client.v2.model.UpdateDeploymentGateParamsData;
import com.datadog.api.client.v2.model.UpdateDeploymentGateParamsDataAttributes;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateDeploymentGate", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    UpdateDeploymentGateParams body =
        new UpdateDeploymentGateParams()
            .data(
                new UpdateDeploymentGateParamsData()
                    .attributes(new UpdateDeploymentGateParamsDataAttributes().dryRun(false))
                    .id("12345678-1234-1234-1234-123456789012")
                    .type(DeploymentGateDataType.DEPLOYMENT_GATE));

    try {
      DeploymentGateResponse result =
          apiInstance.updateDeploymentGate(DEPLOYMENT_GATE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#updateDeploymentGate");
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
Update deployment gate returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType
from datadog_api_client.v2.model.update_deployment_gate_params import UpdateDeploymentGateParams
from datadog_api_client.v2.model.update_deployment_gate_params_data import UpdateDeploymentGateParamsData
from datadog_api_client.v2.model.update_deployment_gate_params_data_attributes import (
    UpdateDeploymentGateParamsDataAttributes,
)

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

body = UpdateDeploymentGateParams(
    data=UpdateDeploymentGateParamsData(
        attributes=UpdateDeploymentGateParamsDataAttributes(
            dry_run=False,
        ),
        id="12345678-1234-1234-1234-123456789012",
        type=DeploymentGateDataType.DEPLOYMENT_GATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_deployment_gate"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.update_deployment_gate(id=DEPLOYMENT_GATE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update deployment gate returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_deployment_gate".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]

body = DatadogAPIClient::V2::UpdateDeploymentGateParams.new({
  data: DatadogAPIClient::V2::UpdateDeploymentGateParamsData.new({
    attributes: DatadogAPIClient::V2::UpdateDeploymentGateParamsDataAttributes.new({
      dry_run: false,
    }),
    id: "12345678-1234-1234-1234-123456789012",
    type: DatadogAPIClient::V2::DeploymentGateDataType::DEPLOYMENT_GATE,
  }),
})
p api_instance.update_deployment_gate(DEPLOYMENT_GATE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update deployment gate returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;
use datadog_api_client::datadogV2::model::DeploymentGateDataType;
use datadog_api_client::datadogV2::model::UpdateDeploymentGateParams;
use datadog_api_client::datadogV2::model::UpdateDeploymentGateParamsData;
use datadog_api_client::datadogV2::model::UpdateDeploymentGateParamsDataAttributes;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();
    let body = UpdateDeploymentGateParams::new(UpdateDeploymentGateParamsData::new(
        UpdateDeploymentGateParamsDataAttributes::new(false),
        "12345678-1234-1234-1234-123456789012".to_string(),
        DeploymentGateDataType::DEPLOYMENT_GATE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateDeploymentGate", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .update_deployment_gate(deployment_gate_data_id.clone(), body)
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Update deployment gate returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateDeploymentGate"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

const params: v2.DeploymentGatesApiUpdateDeploymentGateRequest = {
  body: {
    data: {
      attributes: {
        dryRun: false,
      },
      id: "12345678-1234-1234-1234-123456789012",
      type: "deployment_gate",
    },
  },
  id: DEPLOYMENT_GATE_DATA_ID,
};

apiInstance
  .updateDeploymentGate(params)
  .then((data: v2.DeploymentGateResponse) => {
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

## Delete deployment gate{% #delete-deployment-gate %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/deployment_gates/{id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/deployment_gates/{id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/deployment_gates/{id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/deployment_gates/{id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/deployment_gates/{id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/deployment_gates/{id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/deployment_gates/{id} |

### Overview

Endpoint to delete a deployment gate. Rules associated with the gate are also deleted. This endpoint requires the `deployment_gates_write` permission.

### Arguments

#### Path Parameters

| Name                 | Type   | Description                    |
| -------------------- | ------ | ------------------------------ |
| id [*required*] | string | The ID of the deployment gate. |

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
Deployment gate not found.
{% tab title="Model" %}
Deployment gate not found.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete deployment gate returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_deployment_gate"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    api_instance.delete_deployment_gate(
        id=DEPLOYMENT_GATE_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete deployment gate returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_deployment_gate".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]
api_instance.delete_deployment_gate(DEPLOYMENT_GATE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete deployment gate returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.DeleteDeploymentGate", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    r, err := api.DeleteDeploymentGate(ctx, DeploymentGateDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.DeleteDeploymentGate`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete deployment gate returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteDeploymentGate", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    try {
      apiInstance.deleteDeploymentGate(DEPLOYMENT_GATE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#deleteDeploymentGate");
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

```rust
// Delete deployment gate returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteDeploymentGate", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .delete_deployment_gate(deployment_gate_data_id.clone())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Delete deployment gate returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteDeploymentGate"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

const params: v2.DeploymentGatesApiDeleteDeploymentGateRequest = {
  id: DEPLOYMENT_GATE_DATA_ID,
};

apiInstance
  .deleteDeploymentGate(params)
  .then((data: any) => {
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

## Create deployment rule{% #create-deployment-rule %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |

### Overview

Endpoint to create a deployment rule. A gate for the rule must already exist. This endpoint requires the `deployment_gates_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                    |
| ------------------------- | ------ | ------------------------------ |
| gate_id [*required*] | string | The ID of the deployment gate. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type          | Description                                                                                              |
| ------------ | ---------------------------- | ------------- | -------------------------------------------------------------------------------------------------------- |
|              | data                         | object        | Parameters for creating a deployment rule.                                                               |
| data         | attributes [*required*] | object        | Parameters for creating a deployment rule.                                                               |
| attributes   | dry_run                      | boolean       | Whether this rule is run in dry-run mode.                                                                |
| attributes   | name [*required*]       | string        | The name of the deployment rule.                                                                         |
| attributes   | options [*required*]    |  <oneOf> | Options for deployment rule response representing either faulty deployment detection or monitor options. |
| options      | Option 1                     | object        | Faulty deployment detection options for deployment rules.                                                |
| Option 1     | duration                     | int64         | The duration for faulty deployment detection.                                                            |
| Option 1     | excluded_resources           | [string]      | Resources to exclude from faulty deployment detection.                                                   |
| options      | Option 2                     | object        | Monitor options for deployment rules.                                                                    |
| Option 2     | duration                     | int64         | Seconds the monitor needs to stay in OK status for the rule to pass.                                     |
| Option 2     | query [*required*]      | string        | Monitors that match this query are evaluated.                                                            |
| attributes   | type [*required*]       | string        | The type of the deployment rule (faulty_deployment_detection or monitor).                                |
| data         | type [*required*]       | enum          | Deployment rule resource type. Allowed enum values: `deployment_rule`                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "dry_run": false,
      "name": "My deployment rule",
      "options": {
        "excluded_resources": []
      },
      "type": "faulty_deployment_detection"
    },
    "type": "deployment_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a deployment rule.

| Parent field | Field                        | Type          | Description                                                                                              |
| ------------ | ---------------------------- | ------------- | -------------------------------------------------------------------------------------------------------- |
|              | data                         | object        | Data for a deployment rule.                                                                              |
| data         | attributes [*required*] | object        | Basic information about a deployment rule.                                                               |
| attributes   | created_at [*required*] | date-time     | The timestamp when the deployment rule was created.                                                      |
| attributes   | created_by [*required*] | object        | Information about the user who created the deployment rule.                                              |
| created_by   | handle                       | string        | The handle of the user who created the deployment rule.                                                  |
| created_by   | id [*required*]         | string        | The ID of the user who created the deployment rule.                                                      |
| created_by   | name                         | string        | The name of the user who created the deployment rule.                                                    |
| attributes   | dry_run [*required*]    | boolean       | Whether this rule is run in dry-run mode.                                                                |
| attributes   | gate_id [*required*]    | string        | The ID of the deployment gate.                                                                           |
| attributes   | name [*required*]       | string        | The name of the deployment rule.                                                                         |
| attributes   | options [*required*]    |  <oneOf> | Options for deployment rule response representing either faulty deployment detection or monitor options. |
| options      | Option 1                     | object        | Faulty deployment detection options for deployment rules.                                                |
| Option 1     | duration                     | int64         | The duration for faulty deployment detection.                                                            |
| Option 1     | excluded_resources           | [string]      | Resources to exclude from faulty deployment detection.                                                   |
| options      | Option 2                     | object        | Monitor options for deployment rules.                                                                    |
| Option 2     | duration                     | int64         | Seconds the monitor needs to stay in OK status for the rule to pass.                                     |
| Option 2     | query [*required*]      | string        | Monitors that match this query are evaluated.                                                            |
| attributes   | type [*required*]       | enum          | The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`              |
| attributes   | updated_at                   | date-time     | The timestamp when the deployment rule was last updated.                                                 |
| attributes   | updated_by                   | object        | Information about the user who updated the deployment rule.                                              |
| updated_by   | handle                       | string        | The handle of the user who updated the deployment rule.                                                  |
| updated_by   | id [*required*]         | string        | The ID of the user who updated the deployment rule.                                                      |
| updated_by   | name                         | string        | The name of the user who updated the deployment rule.                                                    |
| data         | id [*required*]         | string        | Unique identifier of the deployment rule.                                                                |
| data         | type [*required*]       | enum          | Deployment rule resource type. Allowed enum values: `deployment_rule`                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2021-01-01T00:00:00Z",
      "created_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      },
      "dry_run": false,
      "gate_id": "1111-2222-3333-4444-555566667777",
      "name": "My deployment rule",
      "options": {
        "duration": 3600,
        "excluded_resources": [
          "resource1",
          "resource2"
        ]
      },
      "type": "faulty_deployment_detection",
      "updated_at": "2019-09-19T10:00:00.000Z",
      "updated_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      }
    },
    "id": "1111-2222-3333-4444-555566667777",
    "type": "deployment_rule"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Path parametersexport gate_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "dry_run": false,
      "name": "My deployment rule",
      "options": {
        "excluded_resources": []
      },
      "type": "faulty_deployment_detection"
    },
    "type": "deployment_rule"
  }
}
EOF

#####

```go
// Create deployment rule returns "OK" response

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
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    body := datadogV2.CreateDeploymentRuleParams{
        Data: &datadogV2.CreateDeploymentRuleParamsData{
            Attributes: datadogV2.CreateDeploymentRuleParamsDataAttributes{
                DryRun: datadog.PtrBool(false),
                Name:   "My deployment rule",
                Options: datadogV2.DeploymentRulesOptions{
                    DeploymentRuleOptionsFaultyDeploymentDetection: &datadogV2.DeploymentRuleOptionsFaultyDeploymentDetection{
                        ExcludedResources: []string{},
                    }},
                Type: "faulty_deployment_detection",
            },
            Type: datadogV2.DEPLOYMENTRULEDATATYPE_DEPLOYMENT_RULE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateDeploymentRule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    resp, r, err := api.CreateDeploymentRule(ctx, DeploymentGateDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.CreateDeploymentRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DeploymentGatesApi.CreateDeploymentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create deployment rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;
import com.datadog.api.client.v2.model.CreateDeploymentRuleParams;
import com.datadog.api.client.v2.model.CreateDeploymentRuleParamsData;
import com.datadog.api.client.v2.model.CreateDeploymentRuleParamsDataAttributes;
import com.datadog.api.client.v2.model.DeploymentRuleDataType;
import com.datadog.api.client.v2.model.DeploymentRuleOptionsFaultyDeploymentDetection;
import com.datadog.api.client.v2.model.DeploymentRuleResponse;
import com.datadog.api.client.v2.model.DeploymentRulesOptions;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createDeploymentRule", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    CreateDeploymentRuleParams body =
        new CreateDeploymentRuleParams()
            .data(
                new CreateDeploymentRuleParamsData()
                    .attributes(
                        new CreateDeploymentRuleParamsDataAttributes()
                            .dryRun(false)
                            .name("My deployment rule")
                            .options(
                                new DeploymentRulesOptions(
                                    new DeploymentRuleOptionsFaultyDeploymentDetection()))
                            .type("faulty_deployment_detection"))
                    .type(DeploymentRuleDataType.DEPLOYMENT_RULE));

    try {
      DeploymentRuleResponse result =
          apiInstance.createDeploymentRule(DEPLOYMENT_GATE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#createDeploymentRule");
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
Create deployment rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.create_deployment_rule_params import CreateDeploymentRuleParams
from datadog_api_client.v2.model.create_deployment_rule_params_data import CreateDeploymentRuleParamsData
from datadog_api_client.v2.model.create_deployment_rule_params_data_attributes import (
    CreateDeploymentRuleParamsDataAttributes,
)
from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType
from datadog_api_client.v2.model.deployment_rule_options_faulty_deployment_detection import (
    DeploymentRuleOptionsFaultyDeploymentDetection,
)

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

body = CreateDeploymentRuleParams(
    data=CreateDeploymentRuleParamsData(
        attributes=CreateDeploymentRuleParamsDataAttributes(
            dry_run=False,
            name="My deployment rule",
            options=DeploymentRuleOptionsFaultyDeploymentDetection(
                excluded_resources=[],
            ),
            type="faulty_deployment_detection",
        ),
        type=DeploymentRuleDataType.DEPLOYMENT_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_deployment_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.create_deployment_rule(gate_id=DEPLOYMENT_GATE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create deployment rule returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_deployment_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]

body = DatadogAPIClient::V2::CreateDeploymentRuleParams.new({
  data: DatadogAPIClient::V2::CreateDeploymentRuleParamsData.new({
    attributes: DatadogAPIClient::V2::CreateDeploymentRuleParamsDataAttributes.new({
      dry_run: false,
      name: "My deployment rule",
      options: DatadogAPIClient::V2::DeploymentRuleOptionsFaultyDeploymentDetection.new({
        excluded_resources: [],
      }),
      type: "faulty_deployment_detection",
    }),
    type: DatadogAPIClient::V2::DeploymentRuleDataType::DEPLOYMENT_RULE,
  }),
})
p api_instance.create_deployment_rule(DEPLOYMENT_GATE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create deployment rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;
use datadog_api_client::datadogV2::model::CreateDeploymentRuleParams;
use datadog_api_client::datadogV2::model::CreateDeploymentRuleParamsData;
use datadog_api_client::datadogV2::model::CreateDeploymentRuleParamsDataAttributes;
use datadog_api_client::datadogV2::model::DeploymentRuleDataType;
use datadog_api_client::datadogV2::model::DeploymentRuleOptionsFaultyDeploymentDetection;
use datadog_api_client::datadogV2::model::DeploymentRulesOptions;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();
    let body = CreateDeploymentRuleParams::new().data(CreateDeploymentRuleParamsData::new(
        CreateDeploymentRuleParamsDataAttributes::new(
            "My deployment rule".to_string(),
            DeploymentRulesOptions::DeploymentRuleOptionsFaultyDeploymentDetection(Box::new(
                DeploymentRuleOptionsFaultyDeploymentDetection::new().excluded_resources(vec![]),
            )),
            "faulty_deployment_detection".to_string(),
        )
        .dry_run(false),
        DeploymentRuleDataType::DEPLOYMENT_RULE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateDeploymentRule", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .create_deployment_rule(deployment_gate_data_id.clone(), body)
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create deployment rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createDeploymentRule"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

const params: v2.DeploymentGatesApiCreateDeploymentRuleRequest = {
  body: {
    data: {
      attributes: {
        dryRun: false,
        name: "My deployment rule",
        options: {
          excludedResources: [],
        },
        type: "faulty_deployment_detection",
      },
      type: "deployment_rule",
    },
  },
  gateId: DEPLOYMENT_GATE_DATA_ID,
};

apiInstance
  .createDeploymentRule(params)
  .then((data: v2.DeploymentRuleResponse) => {
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

## Get deployment rule{% #get-deployment-rule %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules/{id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules/{id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |

### Overview

Endpoint to get a deployment rule. This endpoint requires the `deployment_gates_read` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                    |
| ------------------------- | ------ | ------------------------------ |
| gate_id [*required*] | string | The ID of the deployment gate. |
| id [*required*]      | string | The ID of the deployment rule. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a deployment rule.

| Parent field | Field                        | Type          | Description                                                                                              |
| ------------ | ---------------------------- | ------------- | -------------------------------------------------------------------------------------------------------- |
|              | data                         | object        | Data for a deployment rule.                                                                              |
| data         | attributes [*required*] | object        | Basic information about a deployment rule.                                                               |
| attributes   | created_at [*required*] | date-time     | The timestamp when the deployment rule was created.                                                      |
| attributes   | created_by [*required*] | object        | Information about the user who created the deployment rule.                                              |
| created_by   | handle                       | string        | The handle of the user who created the deployment rule.                                                  |
| created_by   | id [*required*]         | string        | The ID of the user who created the deployment rule.                                                      |
| created_by   | name                         | string        | The name of the user who created the deployment rule.                                                    |
| attributes   | dry_run [*required*]    | boolean       | Whether this rule is run in dry-run mode.                                                                |
| attributes   | gate_id [*required*]    | string        | The ID of the deployment gate.                                                                           |
| attributes   | name [*required*]       | string        | The name of the deployment rule.                                                                         |
| attributes   | options [*required*]    |  <oneOf> | Options for deployment rule response representing either faulty deployment detection or monitor options. |
| options      | Option 1                     | object        | Faulty deployment detection options for deployment rules.                                                |
| Option 1     | duration                     | int64         | The duration for faulty deployment detection.                                                            |
| Option 1     | excluded_resources           | [string]      | Resources to exclude from faulty deployment detection.                                                   |
| options      | Option 2                     | object        | Monitor options for deployment rules.                                                                    |
| Option 2     | duration                     | int64         | Seconds the monitor needs to stay in OK status for the rule to pass.                                     |
| Option 2     | query [*required*]      | string        | Monitors that match this query are evaluated.                                                            |
| attributes   | type [*required*]       | enum          | The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`              |
| attributes   | updated_at                   | date-time     | The timestamp when the deployment rule was last updated.                                                 |
| attributes   | updated_by                   | object        | Information about the user who updated the deployment rule.                                              |
| updated_by   | handle                       | string        | The handle of the user who updated the deployment rule.                                                  |
| updated_by   | id [*required*]         | string        | The ID of the user who updated the deployment rule.                                                      |
| updated_by   | name                         | string        | The name of the user who updated the deployment rule.                                                    |
| data         | id [*required*]         | string        | Unique identifier of the deployment rule.                                                                |
| data         | type [*required*]       | enum          | Deployment rule resource type. Allowed enum values: `deployment_rule`                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2021-01-01T00:00:00Z",
      "created_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      },
      "dry_run": false,
      "gate_id": "1111-2222-3333-4444-555566667777",
      "name": "My deployment rule",
      "options": {
        "duration": 3600,
        "excluded_resources": [
          "resource1",
          "resource2"
        ]
      },
      "type": "faulty_deployment_detection",
      "updated_at": "2019-09-19T10:00:00.000Z",
      "updated_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      }
    },
    "id": "1111-2222-3333-4444-555566667777",
    "type": "deployment_rule"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
Deployment rule not found.
{% tab title="Model" %}
Deployment rule not found.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport gate_id="CHANGE_ME"export id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get deployment rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

# there is a valid "deployment_rule" in the system
DEPLOYMENT_RULE_DATA_ID = environ["DEPLOYMENT_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_deployment_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.get_deployment_rule(
        gate_id=DEPLOYMENT_GATE_DATA_ID,
        id=DEPLOYMENT_RULE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get deployment rule returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_deployment_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]

# there is a valid "deployment_rule" in the system
DEPLOYMENT_RULE_DATA_ID = ENV["DEPLOYMENT_RULE_DATA_ID"]
p api_instance.get_deployment_rule(DEPLOYMENT_GATE_DATA_ID, DEPLOYMENT_RULE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get deployment rule returns "OK" response

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
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    // there is a valid "deployment_rule" in the system
    DeploymentRuleDataID := os.Getenv("DEPLOYMENT_RULE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetDeploymentRule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    resp, r, err := api.GetDeploymentRule(ctx, DeploymentGateDataID, DeploymentRuleDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.GetDeploymentRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DeploymentGatesApi.GetDeploymentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get deployment rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;
import com.datadog.api.client.v2.model.DeploymentRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getDeploymentRule", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    // there is a valid "deployment_rule" in the system
    String DEPLOYMENT_RULE_DATA_ID = System.getenv("DEPLOYMENT_RULE_DATA_ID");

    try {
      DeploymentRuleResponse result =
          apiInstance.getDeploymentRule(DEPLOYMENT_GATE_DATA_ID, DEPLOYMENT_RULE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#getDeploymentRule");
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

```rust
// Get deployment rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();

    // there is a valid "deployment_rule" in the system
    let deployment_rule_data_id = std::env::var("DEPLOYMENT_RULE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetDeploymentRule", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .get_deployment_rule(
            deployment_gate_data_id.clone(),
            deployment_rule_data_id.clone(),
        )
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get deployment rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getDeploymentRule"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

// there is a valid "deployment_rule" in the system
const DEPLOYMENT_RULE_DATA_ID = process.env.DEPLOYMENT_RULE_DATA_ID as string;

const params: v2.DeploymentGatesApiGetDeploymentRuleRequest = {
  gateId: DEPLOYMENT_GATE_DATA_ID,
  id: DEPLOYMENT_RULE_DATA_ID,
};

apiInstance
  .getDeploymentRule(params)
  .then((data: v2.DeploymentRuleResponse) => {
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

## Update deployment rule{% #update-deployment-rule %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules/{id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules/{id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |

### Overview

Endpoint to update a deployment rule. This endpoint requires the `deployment_gates_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                    |
| ------------------------- | ------ | ------------------------------ |
| gate_id [*required*] | string | The ID of the deployment gate. |
| id [*required*]      | string | The ID of the deployment rule. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type          | Description                                                                                              |
| ------------ | ---------------------------- | ------------- | -------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object        | Parameters for updating a deployment rule.                                                               |
| data         | attributes [*required*] | object        | Parameters for updating a deployment rule.                                                               |
| attributes   | dry_run [*required*]    | boolean       | Whether to run this rule in dry-run mode.                                                                |
| attributes   | name [*required*]       | string        | The name of the deployment rule.                                                                         |
| attributes   | options [*required*]    |  <oneOf> | Options for deployment rule response representing either faulty deployment detection or monitor options. |
| options      | Option 1                     | object        | Faulty deployment detection options for deployment rules.                                                |
| Option 1     | duration                     | int64         | The duration for faulty deployment detection.                                                            |
| Option 1     | excluded_resources           | [string]      | Resources to exclude from faulty deployment detection.                                                   |
| options      | Option 2                     | object        | Monitor options for deployment rules.                                                                    |
| Option 2     | duration                     | int64         | Seconds the monitor needs to stay in OK status for the rule to pass.                                     |
| Option 2     | query [*required*]      | string        | Monitors that match this query are evaluated.                                                            |
| data         | type [*required*]       | enum          | Deployment rule resource type. Allowed enum values: `deployment_rule`                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "dry_run": false,
      "name": "Updated deployment rule",
      "options": {
        "excluded_resources": []
      }
    },
    "type": "deployment_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a deployment rule.

| Parent field | Field                        | Type          | Description                                                                                              |
| ------------ | ---------------------------- | ------------- | -------------------------------------------------------------------------------------------------------- |
|              | data                         | object        | Data for a deployment rule.                                                                              |
| data         | attributes [*required*] | object        | Basic information about a deployment rule.                                                               |
| attributes   | created_at [*required*] | date-time     | The timestamp when the deployment rule was created.                                                      |
| attributes   | created_by [*required*] | object        | Information about the user who created the deployment rule.                                              |
| created_by   | handle                       | string        | The handle of the user who created the deployment rule.                                                  |
| created_by   | id [*required*]         | string        | The ID of the user who created the deployment rule.                                                      |
| created_by   | name                         | string        | The name of the user who created the deployment rule.                                                    |
| attributes   | dry_run [*required*]    | boolean       | Whether this rule is run in dry-run mode.                                                                |
| attributes   | gate_id [*required*]    | string        | The ID of the deployment gate.                                                                           |
| attributes   | name [*required*]       | string        | The name of the deployment rule.                                                                         |
| attributes   | options [*required*]    |  <oneOf> | Options for deployment rule response representing either faulty deployment detection or monitor options. |
| options      | Option 1                     | object        | Faulty deployment detection options for deployment rules.                                                |
| Option 1     | duration                     | int64         | The duration for faulty deployment detection.                                                            |
| Option 1     | excluded_resources           | [string]      | Resources to exclude from faulty deployment detection.                                                   |
| options      | Option 2                     | object        | Monitor options for deployment rules.                                                                    |
| Option 2     | duration                     | int64         | Seconds the monitor needs to stay in OK status for the rule to pass.                                     |
| Option 2     | query [*required*]      | string        | Monitors that match this query are evaluated.                                                            |
| attributes   | type [*required*]       | enum          | The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`              |
| attributes   | updated_at                   | date-time     | The timestamp when the deployment rule was last updated.                                                 |
| attributes   | updated_by                   | object        | Information about the user who updated the deployment rule.                                              |
| updated_by   | handle                       | string        | The handle of the user who updated the deployment rule.                                                  |
| updated_by   | id [*required*]         | string        | The ID of the user who updated the deployment rule.                                                      |
| updated_by   | name                         | string        | The name of the user who updated the deployment rule.                                                    |
| data         | id [*required*]         | string        | Unique identifier of the deployment rule.                                                                |
| data         | type [*required*]       | enum          | Deployment rule resource type. Allowed enum values: `deployment_rule`                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2021-01-01T00:00:00Z",
      "created_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      },
      "dry_run": false,
      "gate_id": "1111-2222-3333-4444-555566667777",
      "name": "My deployment rule",
      "options": {
        "duration": 3600,
        "excluded_resources": [
          "resource1",
          "resource2"
        ]
      },
      "type": "faulty_deployment_detection",
      "updated_at": "2019-09-19T10:00:00.000Z",
      "updated_by": {
        "handle": "test-user",
        "id": "1111-2222-3333-4444-555566667777",
        "name": "Test User"
      }
    },
    "id": "1111-2222-3333-4444-555566667777",
    "type": "deployment_rule"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
Deployment rule not found.
{% tab title="Model" %}
Deployment rule not found.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Path parametersexport gate_id="CHANGE_ME"export id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules/${id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "dry_run": false,
      "name": "Updated deployment rule",
      "options": {
        "excluded_resources": []
      }
    },
    "type": "deployment_rule"
  }
}
EOF

#####

```go
// Update deployment rule returns "OK" response

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
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    // there is a valid "deployment_rule" in the system
    DeploymentRuleDataID := os.Getenv("DEPLOYMENT_RULE_DATA_ID")

    body := datadogV2.UpdateDeploymentRuleParams{
        Data: datadogV2.UpdateDeploymentRuleParamsData{
            Attributes: datadogV2.UpdateDeploymentRuleParamsDataAttributes{
                DryRun: false,
                Name:   "Updated deployment rule",
                Options: datadogV2.DeploymentRulesOptions{
                    DeploymentRuleOptionsFaultyDeploymentDetection: &datadogV2.DeploymentRuleOptionsFaultyDeploymentDetection{
                        ExcludedResources: []string{},
                    }},
            },
            Type: datadogV2.DEPLOYMENTRULEDATATYPE_DEPLOYMENT_RULE,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.UpdateDeploymentRule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    resp, r, err := api.UpdateDeploymentRule(ctx, DeploymentGateDataID, DeploymentRuleDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.UpdateDeploymentRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DeploymentGatesApi.UpdateDeploymentRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update deployment rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;
import com.datadog.api.client.v2.model.DeploymentRuleDataType;
import com.datadog.api.client.v2.model.DeploymentRuleOptionsFaultyDeploymentDetection;
import com.datadog.api.client.v2.model.DeploymentRuleResponse;
import com.datadog.api.client.v2.model.DeploymentRulesOptions;
import com.datadog.api.client.v2.model.UpdateDeploymentRuleParams;
import com.datadog.api.client.v2.model.UpdateDeploymentRuleParamsData;
import com.datadog.api.client.v2.model.UpdateDeploymentRuleParamsDataAttributes;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateDeploymentRule", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    // there is a valid "deployment_rule" in the system
    String DEPLOYMENT_RULE_DATA_ID = System.getenv("DEPLOYMENT_RULE_DATA_ID");

    UpdateDeploymentRuleParams body =
        new UpdateDeploymentRuleParams()
            .data(
                new UpdateDeploymentRuleParamsData()
                    .attributes(
                        new UpdateDeploymentRuleParamsDataAttributes()
                            .dryRun(false)
                            .name("Updated deployment rule")
                            .options(
                                new DeploymentRulesOptions(
                                    new DeploymentRuleOptionsFaultyDeploymentDetection())))
                    .type(DeploymentRuleDataType.DEPLOYMENT_RULE));

    try {
      DeploymentRuleResponse result =
          apiInstance.updateDeploymentRule(DEPLOYMENT_GATE_DATA_ID, DEPLOYMENT_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#updateDeploymentRule");
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
Update deployment rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType
from datadog_api_client.v2.model.deployment_rule_options_faulty_deployment_detection import (
    DeploymentRuleOptionsFaultyDeploymentDetection,
)
from datadog_api_client.v2.model.update_deployment_rule_params import UpdateDeploymentRuleParams
from datadog_api_client.v2.model.update_deployment_rule_params_data import UpdateDeploymentRuleParamsData
from datadog_api_client.v2.model.update_deployment_rule_params_data_attributes import (
    UpdateDeploymentRuleParamsDataAttributes,
)

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

# there is a valid "deployment_rule" in the system
DEPLOYMENT_RULE_DATA_ID = environ["DEPLOYMENT_RULE_DATA_ID"]

body = UpdateDeploymentRuleParams(
    data=UpdateDeploymentRuleParamsData(
        attributes=UpdateDeploymentRuleParamsDataAttributes(
            dry_run=False,
            name="Updated deployment rule",
            options=DeploymentRuleOptionsFaultyDeploymentDetection(
                excluded_resources=[],
            ),
        ),
        type=DeploymentRuleDataType.DEPLOYMENT_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_deployment_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.update_deployment_rule(
        gate_id=DEPLOYMENT_GATE_DATA_ID, id=DEPLOYMENT_RULE_DATA_ID, body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update deployment rule returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_deployment_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]

# there is a valid "deployment_rule" in the system
DEPLOYMENT_RULE_DATA_ID = ENV["DEPLOYMENT_RULE_DATA_ID"]

body = DatadogAPIClient::V2::UpdateDeploymentRuleParams.new({
  data: DatadogAPIClient::V2::UpdateDeploymentRuleParamsData.new({
    attributes: DatadogAPIClient::V2::UpdateDeploymentRuleParamsDataAttributes.new({
      dry_run: false,
      name: "Updated deployment rule",
      options: DatadogAPIClient::V2::DeploymentRuleOptionsFaultyDeploymentDetection.new({
        excluded_resources: [],
      }),
    }),
    type: DatadogAPIClient::V2::DeploymentRuleDataType::DEPLOYMENT_RULE,
  }),
})
p api_instance.update_deployment_rule(DEPLOYMENT_GATE_DATA_ID, DEPLOYMENT_RULE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update deployment rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;
use datadog_api_client::datadogV2::model::DeploymentRuleDataType;
use datadog_api_client::datadogV2::model::DeploymentRuleOptionsFaultyDeploymentDetection;
use datadog_api_client::datadogV2::model::DeploymentRulesOptions;
use datadog_api_client::datadogV2::model::UpdateDeploymentRuleParams;
use datadog_api_client::datadogV2::model::UpdateDeploymentRuleParamsData;
use datadog_api_client::datadogV2::model::UpdateDeploymentRuleParamsDataAttributes;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();

    // there is a valid "deployment_rule" in the system
    let deployment_rule_data_id = std::env::var("DEPLOYMENT_RULE_DATA_ID").unwrap();
    let body = UpdateDeploymentRuleParams::new(UpdateDeploymentRuleParamsData::new(
        UpdateDeploymentRuleParamsDataAttributes::new(
            false,
            "Updated deployment rule".to_string(),
            DeploymentRulesOptions::DeploymentRuleOptionsFaultyDeploymentDetection(Box::new(
                DeploymentRuleOptionsFaultyDeploymentDetection::new().excluded_resources(vec![]),
            )),
        ),
        DeploymentRuleDataType::DEPLOYMENT_RULE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateDeploymentRule", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .update_deployment_rule(
            deployment_gate_data_id.clone(),
            deployment_rule_data_id.clone(),
            body,
        )
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Update deployment rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateDeploymentRule"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

// there is a valid "deployment_rule" in the system
const DEPLOYMENT_RULE_DATA_ID = process.env.DEPLOYMENT_RULE_DATA_ID as string;

const params: v2.DeploymentGatesApiUpdateDeploymentRuleRequest = {
  body: {
    data: {
      attributes: {
        dryRun: false,
        name: "Updated deployment rule",
        options: {
          excludedResources: [],
        },
      },
      type: "deployment_rule",
    },
  },
  gateId: DEPLOYMENT_GATE_DATA_ID,
  id: DEPLOYMENT_RULE_DATA_ID,
};

apiInstance
  .updateDeploymentRule(params)
  .then((data: v2.DeploymentRuleResponse) => {
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

## Delete deployment rule{% #delete-deployment-rule %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules/{id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules/{id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id} |

### Overview

Endpoint to delete a deployment rule. This endpoint requires the `deployment_gates_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                    |
| ------------------------- | ------ | ------------------------------ |
| gate_id [*required*] | string | The ID of the deployment gate. |
| id [*required*]      | string | The ID of the deployment rule. |

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
Deployment gate not found.
{% tab title="Model" %}
Deployment gate not found.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport gate_id="CHANGE_ME"export id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete deployment rule returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

# there is a valid "deployment_rule" in the system
DEPLOYMENT_RULE_DATA_ID = environ["DEPLOYMENT_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_deployment_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    api_instance.delete_deployment_rule(
        gate_id=DEPLOYMENT_GATE_DATA_ID,
        id=DEPLOYMENT_RULE_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete deployment rule returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_deployment_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]

# there is a valid "deployment_rule" in the system
DEPLOYMENT_RULE_DATA_ID = ENV["DEPLOYMENT_RULE_DATA_ID"]
api_instance.delete_deployment_rule(DEPLOYMENT_GATE_DATA_ID, DEPLOYMENT_RULE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete deployment rule returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    // there is a valid "deployment_rule" in the system
    DeploymentRuleDataID := os.Getenv("DEPLOYMENT_RULE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.DeleteDeploymentRule", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    r, err := api.DeleteDeploymentRule(ctx, DeploymentGateDataID, DeploymentRuleDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.DeleteDeploymentRule`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete deployment rule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteDeploymentRule", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    // there is a valid "deployment_rule" in the system
    String DEPLOYMENT_RULE_DATA_ID = System.getenv("DEPLOYMENT_RULE_DATA_ID");

    try {
      apiInstance.deleteDeploymentRule(DEPLOYMENT_GATE_DATA_ID, DEPLOYMENT_RULE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#deleteDeploymentRule");
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

```rust
// Delete deployment rule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();

    // there is a valid "deployment_rule" in the system
    let deployment_rule_data_id = std::env::var("DEPLOYMENT_RULE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteDeploymentRule", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .delete_deployment_rule(
            deployment_gate_data_id.clone(),
            deployment_rule_data_id.clone(),
        )
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Delete deployment rule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteDeploymentRule"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

// there is a valid "deployment_rule" in the system
const DEPLOYMENT_RULE_DATA_ID = process.env.DEPLOYMENT_RULE_DATA_ID as string;

const params: v2.DeploymentGatesApiDeleteDeploymentRuleRequest = {
  gateId: DEPLOYMENT_GATE_DATA_ID,
  id: DEPLOYMENT_RULE_DATA_ID,
};

apiInstance
  .deleteDeploymentRule(params)
  .then((data: any) => {
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

## Get rules for a deployment gate{% #get-rules-for-a-deployment-gate %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules |

### Overview

Endpoint to get rules for a deployment gate. This endpoint requires the `deployment_gates_read` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                    |
| ------------------------- | ------ | ------------------------------ |
| gate_id [*required*] | string | The ID of the deployment gate. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for a deployment gate rules.

| Parent field | Field                        | Type          | Description                                                                                              |
| ------------ | ---------------------------- | ------------- | -------------------------------------------------------------------------------------------------------- |
|              | data                         | object        | Data for a list of deployment rules.                                                                     |
| data         | attributes [*required*] | object        |
| attributes   | rules                        | [object]      |
| rules        | created_at [*required*] | date-time     | The timestamp when the deployment rule was created.                                                      |
| rules        | created_by [*required*] | object        | Information about the user who created the deployment rule.                                              |
| created_by   | handle                       | string        | The handle of the user who created the deployment rule.                                                  |
| created_by   | id [*required*]         | string        | The ID of the user who created the deployment rule.                                                      |
| created_by   | name                         | string        | The name of the user who created the deployment rule.                                                    |
| rules        | dry_run [*required*]    | boolean       | Whether this rule is run in dry-run mode.                                                                |
| rules        | gate_id [*required*]    | string        | The ID of the deployment gate.                                                                           |
| rules        | name [*required*]       | string        | The name of the deployment rule.                                                                         |
| rules        | options [*required*]    |  <oneOf> | Options for deployment rule response representing either faulty deployment detection or monitor options. |
| options      | Option 1                     | object        | Faulty deployment detection options for deployment rules.                                                |
| Option 1     | duration                     | int64         | The duration for faulty deployment detection.                                                            |
| Option 1     | excluded_resources           | [string]      | Resources to exclude from faulty deployment detection.                                                   |
| options      | Option 2                     | object        | Monitor options for deployment rules.                                                                    |
| Option 2     | duration                     | int64         | Seconds the monitor needs to stay in OK status for the rule to pass.                                     |
| Option 2     | query [*required*]      | string        | Monitors that match this query are evaluated.                                                            |
| rules        | type [*required*]       | enum          | The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`              |
| rules        | updated_at                   | date-time     | The timestamp when the deployment rule was last updated.                                                 |
| rules        | updated_by                   | object        | Information about the user who updated the deployment rule.                                              |
| updated_by   | handle                       | string        | The handle of the user who updated the deployment rule.                                                  |
| updated_by   | id [*required*]         | string        | The ID of the user who updated the deployment rule.                                                      |
| updated_by   | name                         | string        | The name of the user who updated the deployment rule.                                                    |
| data         | id [*required*]         | string        | Unique identifier of the deployment rule.                                                                |
| data         | type [*required*]       | enum          | List deployment rule resource type. Allowed enum values: `list_deployment_rules`                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "rules": [
        {
          "created_at": "2021-01-01T00:00:00Z",
          "created_by": {
            "handle": "test-user",
            "id": "1111-2222-3333-4444-555566667777",
            "name": "Test User"
          },
          "dry_run": false,
          "gate_id": "1111-2222-3333-4444-555566667777",
          "name": "My deployment rule",
          "options": {
            "duration": 3600,
            "excluded_resources": [
              "resource1",
              "resource2"
            ]
          },
          "type": "faulty_deployment_detection",
          "updated_at": "2019-09-19T10:00:00.000Z",
          "updated_by": {
            "handle": "test-user",
            "id": "1111-2222-3333-4444-555566667777",
            "name": "Test User"
          }
        }
      ]
    },
    "id": "1111-2222-3333-4444-555566667777",
    "type": "list_deployment_rules"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request.
{% tab title="Model" %}
Bad request.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport gate_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get rules for a deployment gate returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_deployment_gate_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.get_deployment_gate_rules(
        gate_id=DEPLOYMENT_GATE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get rules for a deployment gate returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_deployment_gate_rules".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DeploymentGatesAPI.new

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = ENV["DEPLOYMENT_GATE_DATA_ID"]
p api_instance.get_deployment_gate_rules(DEPLOYMENT_GATE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get rules for a deployment gate returns "OK" response

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
    // there is a valid "deployment_gate" in the system
    DeploymentGateDataID := os.Getenv("DEPLOYMENT_GATE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetDeploymentGateRules", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDeploymentGatesApi(apiClient)
    resp, r, err := api.GetDeploymentGateRules(ctx, DeploymentGateDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DeploymentGatesApi.GetDeploymentGateRules`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DeploymentGatesApi.GetDeploymentGateRules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get rules for a deployment gate returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DeploymentGatesApi;
import com.datadog.api.client.v2.model.DeploymentGateRulesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getDeploymentGateRules", true);
    DeploymentGatesApi apiInstance = new DeploymentGatesApi(defaultClient);

    // there is a valid "deployment_gate" in the system
    String DEPLOYMENT_GATE_DATA_ID = System.getenv("DEPLOYMENT_GATE_DATA_ID");

    try {
      DeploymentGateRulesResponse result =
          apiInstance.getDeploymentGateRules(DEPLOYMENT_GATE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentGatesApi#getDeploymentGateRules");
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

```rust
// Get rules for a deployment gate returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_deployment_gates::DeploymentGatesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "deployment_gate" in the system
    let deployment_gate_data_id = std::env::var("DEPLOYMENT_GATE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetDeploymentGateRules", true);
    let api = DeploymentGatesAPI::with_config(configuration);
    let resp = api
        .get_deployment_gate_rules(deployment_gate_data_id.clone())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get rules for a deployment gate returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getDeploymentGateRules"] = true;
const apiInstance = new v2.DeploymentGatesApi(configuration);

// there is a valid "deployment_gate" in the system
const DEPLOYMENT_GATE_DATA_ID = process.env.DEPLOYMENT_GATE_DATA_ID as string;

const params: v2.DeploymentGatesApiGetDeploymentGateRulesRequest = {
  gateId: DEPLOYMENT_GATE_DATA_ID,
};

apiInstance
  .getDeploymentGateRules(params)
  .then((data: v2.DeploymentGateRulesResponse) => {
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
