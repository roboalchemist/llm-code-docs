# Source: https://docs.datadoghq.com/api/latest/deployment-gates/

# Deployment Gates
Manage Deployment Gates using this API to reduce the likelihood and impact of incidents caused by deployments. See the [Deployment Gates documentation](https://docs.datadoghq.com/deployment_gates/) for more information.
## [Create deployment gate](https://docs.datadoghq.com/api/latest/deployment-gates/#create-deployment-gate)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#create-deployment-gate-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/deployment_gateshttps://api.ap2.datadoghq.com/api/v2/deployment_gateshttps://api.datadoghq.eu/api/v2/deployment_gateshttps://api.ddog-gov.com/api/v2/deployment_gateshttps://api.datadoghq.com/api/v2/deployment_gateshttps://api.us3.datadoghq.com/api/v2/deployment_gateshttps://api.us5.datadoghq.com/api/v2/deployment_gates
### Overview
Endpoint to create a deployment gate. This endpoint requires the `deployment_gates_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Field
Type
Description
data [_required_]
object
Parameters for creating a deployment gate.
attributes [_required_]
object
Parameters for creating a deployment gate.
dry_run
boolean
Whether this gate is run in dry-run mode.
env [_required_]
string
The environment of the deployment gate.
identifier
string
The identifier of the deployment gate.
default: `default`
service [_required_]
string
The service of the deployment gate.
type [_required_]
enum
Deployment gate resource type. Allowed enum values: `deployment_gate`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentGate-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentGate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentGate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentGate-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentGate-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentGate-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Response for a deployment gate.
Field
Type
Description
data
object
Data for a deployment gate.
attributes [_required_]
object
Basic information about a deployment gate.
created_at [_required_]
date-time
The timestamp when the deployment gate was created.
created_by [_required_]
object
Information about the user who created the deployment gate.
handle
string
The handle of the user who created the deployment rule.
id [_required_]
string
The ID of the user who created the deployment rule.
name
string
The name of the user who created the deployment rule.
dry_run [_required_]
boolean
Whether this gate is run in dry-run mode.
env [_required_]
string
The environment of the deployment gate.
identifier [_required_]
string
The identifier of the deployment gate.
service [_required_]
string
The service of the deployment gate.
updated_at
date-time
The timestamp when the deployment gate was last updated.
updated_by
object
Information about the user who updated the deployment gate.
handle
string
The handle of the user who updated the deployment rule.
id [_required_]
string
The ID of the user who updated the deployment rule.
name
string
The name of the user who updated the deployment rule.
id [_required_]
string
Unique identifier of the deployment gate.
type [_required_]
enum
Deployment gate resource type. Allowed enum values: `deployment_gate`
```
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

Copy
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Create deployment gate returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates" \
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

                        
```

#####  Create deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get deployment gate](https://docs.datadoghq.com/api/latest/deployment-gates/#get-deployment-gate)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#get-deployment-gate-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/deployment_gates/{id}https://api.ap2.datadoghq.com/api/v2/deployment_gates/{id}https://api.datadoghq.eu/api/v2/deployment_gates/{id}https://api.ddog-gov.com/api/v2/deployment_gates/{id}https://api.datadoghq.com/api/v2/deployment_gates/{id}https://api.us3.datadoghq.com/api/v2/deployment_gates/{id}https://api.us5.datadoghq.com/api/v2/deployment_gates/{id}
### Overview
Endpoint to get a deployment gate. This endpoint requires the `deployment_gates_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the deployment gate.
### Response
  * [200](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGate-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGate-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGate-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGate-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Response for a deployment gate.
Field
Type
Description
data
object
Data for a deployment gate.
attributes [_required_]
object
Basic information about a deployment gate.
created_at [_required_]
date-time
The timestamp when the deployment gate was created.
created_by [_required_]
object
Information about the user who created the deployment gate.
handle
string
The handle of the user who created the deployment rule.
id [_required_]
string
The ID of the user who created the deployment rule.
name
string
The name of the user who created the deployment rule.
dry_run [_required_]
boolean
Whether this gate is run in dry-run mode.
env [_required_]
string
The environment of the deployment gate.
identifier [_required_]
string
The identifier of the deployment gate.
service [_required_]
string
The service of the deployment gate.
updated_at
date-time
The timestamp when the deployment gate was last updated.
updated_by
object
Information about the user who updated the deployment gate.
handle
string
The handle of the user who updated the deployment rule.
id [_required_]
string
The ID of the user who updated the deployment rule.
name
string
The name of the user who updated the deployment rule.
id [_required_]
string
Unique identifier of the deployment gate.
type [_required_]
enum
Deployment gate resource type. Allowed enum values: `deployment_gate`
```
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

Copy
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Deployment gate not found.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Deployment gate not found.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Get deployment gate
Copy
```
                  # Path parameters  
export id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update deployment gate](https://docs.datadoghq.com/api/latest/deployment-gates/#update-deployment-gate)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#update-deployment-gate-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PUT https://api.ap1.datadoghq.com/api/v2/deployment_gates/{id}https://api.ap2.datadoghq.com/api/v2/deployment_gates/{id}https://api.datadoghq.eu/api/v2/deployment_gates/{id}https://api.ddog-gov.com/api/v2/deployment_gates/{id}https://api.datadoghq.com/api/v2/deployment_gates/{id}https://api.us3.datadoghq.com/api/v2/deployment_gates/{id}https://api.us5.datadoghq.com/api/v2/deployment_gates/{id}
### Overview
Endpoint to update a deployment gate. This endpoint requires the `deployment_gates_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the deployment gate.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Field
Type
Description
data [_required_]
object
Parameters for updating a deployment gate.
attributes [_required_]
object
Attributes for updating a deployment gate.
dry_run [_required_]
boolean
Whether to run in dry-run mode.
id [_required_]
string
Unique identifier of the deployment gate.
type [_required_]
enum
Deployment gate resource type. Allowed enum values: `deployment_gate`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentGate-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentGate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentGate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentGate-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentGate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentGate-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentGate-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Response for a deployment gate.
Field
Type
Description
data
object
Data for a deployment gate.
attributes [_required_]
object
Basic information about a deployment gate.
created_at [_required_]
date-time
The timestamp when the deployment gate was created.
created_by [_required_]
object
Information about the user who created the deployment gate.
handle
string
The handle of the user who created the deployment rule.
id [_required_]
string
The ID of the user who created the deployment rule.
name
string
The name of the user who created the deployment rule.
dry_run [_required_]
boolean
Whether this gate is run in dry-run mode.
env [_required_]
string
The environment of the deployment gate.
identifier [_required_]
string
The identifier of the deployment gate.
service [_required_]
string
The service of the deployment gate.
updated_at
date-time
The timestamp when the deployment gate was last updated.
updated_by
object
Information about the user who updated the deployment gate.
handle
string
The handle of the user who updated the deployment rule.
id [_required_]
string
The ID of the user who updated the deployment rule.
name
string
The name of the user who updated the deployment rule.
id [_required_]
string
Unique identifier of the deployment gate.
type [_required_]
enum
Deployment gate resource type. Allowed enum values: `deployment_gate`
```
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

Copy
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Deployment gate not found.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Deployment gate not found.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Update deployment gate returns "OK" response
Copy
```
                          # Path parameters  
export id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${id}" \
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

                        
```

#####  Update deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update deployment gate returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete deployment gate](https://docs.datadoghq.com/api/latest/deployment-gates/#delete-deployment-gate)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#delete-deployment-gate-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/deployment_gates/{id}https://api.ap2.datadoghq.com/api/v2/deployment_gates/{id}https://api.datadoghq.eu/api/v2/deployment_gates/{id}https://api.ddog-gov.com/api/v2/deployment_gates/{id}https://api.datadoghq.com/api/v2/deployment_gates/{id}https://api.us3.datadoghq.com/api/v2/deployment_gates/{id}https://api.us5.datadoghq.com/api/v2/deployment_gates/{id}
### Overview
Endpoint to delete a deployment gate. Rules associated with the gate are also deleted. This endpoint requires the `deployment_gates_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
id [_required_]
string
The ID of the deployment gate.
### Response
  * [204](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentGate-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentGate-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentGate-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentGate-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentGate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentGate-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentGate-500-v2)


No Content
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Deployment gate not found.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Deployment gate not found.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Delete deployment gate
Copy
```
                  # Path parameters  
export id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create deployment rule](https://docs.datadoghq.com/api/latest/deployment-gates/#create-deployment-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#create-deployment-rule-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/ruleshttps://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules
### Overview
Endpoint to create a deployment rule. A gate for the rule must already exist. This endpoint requires the `deployment_gates_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
gate_id [_required_]
string
The ID of the deployment gate.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Field
Type
Description
data
object
Parameters for creating a deployment rule.
attributes [_required_]
object
Parameters for creating a deployment rule.
dry_run
boolean
Whether this rule is run in dry-run mode.
name [_required_]
string
The name of the deployment rule.
options [_required_]
<oneOf>
Options for deployment rule response representing either faulty deployment detection or monitor options.
Option 1
object
Faulty deployment detection options for deployment rules.
duration
int64
The duration for faulty deployment detection.
excluded_resources
[string]
Resources to exclude from faulty deployment detection.
Option 2
object
Monitor options for deployment rules.
duration
int64
Seconds the monitor needs to stay in OK status for the rule to pass.
query [_required_]
string
Monitors that match this query are evaluated.
type [_required_]
string
The type of the deployment rule (faulty_deployment_detection or monitor).
type [_required_]
enum
Deployment rule resource type. Allowed enum values: `deployment_rule`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentRule-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentRule-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#CreateDeploymentRule-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Response for a deployment rule.
Field
Type
Description
data
object
Data for a deployment rule.
attributes [_required_]
object
Basic information about a deployment rule.
created_at [_required_]
date-time
The timestamp when the deployment rule was created.
created_by [_required_]
object
Information about the user who created the deployment rule.
handle
string
The handle of the user who created the deployment rule.
id [_required_]
string
The ID of the user who created the deployment rule.
name
string
The name of the user who created the deployment rule.
dry_run [_required_]
boolean
Whether this rule is run in dry-run mode.
gate_id [_required_]
string
The ID of the deployment gate.
name [_required_]
string
The name of the deployment rule.
options [_required_]
<oneOf>
Options for deployment rule response representing either faulty deployment detection or monitor options.
Option 1
object
Faulty deployment detection options for deployment rules.
duration
int64
The duration for faulty deployment detection.
excluded_resources
[string]
Resources to exclude from faulty deployment detection.
Option 2
object
Monitor options for deployment rules.
duration
int64
Seconds the monitor needs to stay in OK status for the rule to pass.
query [_required_]
string
Monitors that match this query are evaluated.
type [_required_]
enum
The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`
updated_at
date-time
The timestamp when the deployment rule was last updated.
updated_by
object
Information about the user who updated the deployment rule.
handle
string
The handle of the user who updated the deployment rule.
id [_required_]
string
The ID of the user who updated the deployment rule.
name
string
The name of the user who updated the deployment rule.
id [_required_]
string
Unique identifier of the deployment rule.
type [_required_]
enum
Deployment rule resource type. Allowed enum values: `deployment_rule`
```
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

Copy
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Create deployment rule returns "OK" response
Copy
```
                          # Path parameters  
export gate_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules" \
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

                        
```

#####  Create deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get deployment rule](https://docs.datadoghq.com/api/latest/deployment-gates/#get-deployment-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#get-deployment-rule-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}
### Overview
Endpoint to get a deployment rule. This endpoint requires the `deployment_gates_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
gate_id [_required_]
string
The ID of the deployment gate.
id [_required_]
string
The ID of the deployment rule.
### Response
  * [200](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentRule-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentRule-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Response for a deployment rule.
Field
Type
Description
data
object
Data for a deployment rule.
attributes [_required_]
object
Basic information about a deployment rule.
created_at [_required_]
date-time
The timestamp when the deployment rule was created.
created_by [_required_]
object
Information about the user who created the deployment rule.
handle
string
The handle of the user who created the deployment rule.
id [_required_]
string
The ID of the user who created the deployment rule.
name
string
The name of the user who created the deployment rule.
dry_run [_required_]
boolean
Whether this rule is run in dry-run mode.
gate_id [_required_]
string
The ID of the deployment gate.
name [_required_]
string
The name of the deployment rule.
options [_required_]
<oneOf>
Options for deployment rule response representing either faulty deployment detection or monitor options.
Option 1
object
Faulty deployment detection options for deployment rules.
duration
int64
The duration for faulty deployment detection.
excluded_resources
[string]
Resources to exclude from faulty deployment detection.
Option 2
object
Monitor options for deployment rules.
duration
int64
Seconds the monitor needs to stay in OK status for the rule to pass.
query [_required_]
string
Monitors that match this query are evaluated.
type [_required_]
enum
The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`
updated_at
date-time
The timestamp when the deployment rule was last updated.
updated_by
object
Information about the user who updated the deployment rule.
handle
string
The handle of the user who updated the deployment rule.
id [_required_]
string
The ID of the user who updated the deployment rule.
name
string
The name of the user who updated the deployment rule.
id [_required_]
string
Unique identifier of the deployment rule.
type [_required_]
enum
Deployment rule resource type. Allowed enum values: `deployment_rule`
```
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

Copy
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Deployment rule not found.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Deployment rule not found.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Get deployment rule
Copy
```
                  # Path parameters  
export gate_id="CHANGE_ME"  
export id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update deployment rule](https://docs.datadoghq.com/api/latest/deployment-gates/#update-deployment-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#update-deployment-rule-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PUT https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}
### Overview
Endpoint to update a deployment rule. This endpoint requires the `deployment_gates_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
gate_id [_required_]
string
The ID of the deployment gate.
id [_required_]
string
The ID of the deployment rule.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Field
Type
Description
data [_required_]
object
Parameters for updating a deployment rule.
attributes [_required_]
object
Parameters for updating a deployment rule.
dry_run [_required_]
boolean
Whether to run this rule in dry-run mode.
name [_required_]
string
The name of the deployment rule.
options [_required_]
<oneOf>
Options for deployment rule response representing either faulty deployment detection or monitor options.
Option 1
object
Faulty deployment detection options for deployment rules.
duration
int64
The duration for faulty deployment detection.
excluded_resources
[string]
Resources to exclude from faulty deployment detection.
Option 2
object
Monitor options for deployment rules.
duration
int64
Seconds the monitor needs to stay in OK status for the rule to pass.
query [_required_]
string
Monitors that match this query are evaluated.
type [_required_]
enum
Deployment rule resource type. Allowed enum values: `deployment_rule`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentRule-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#UpdateDeploymentRule-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Response for a deployment rule.
Field
Type
Description
data
object
Data for a deployment rule.
attributes [_required_]
object
Basic information about a deployment rule.
created_at [_required_]
date-time
The timestamp when the deployment rule was created.
created_by [_required_]
object
Information about the user who created the deployment rule.
handle
string
The handle of the user who created the deployment rule.
id [_required_]
string
The ID of the user who created the deployment rule.
name
string
The name of the user who created the deployment rule.
dry_run [_required_]
boolean
Whether this rule is run in dry-run mode.
gate_id [_required_]
string
The ID of the deployment gate.
name [_required_]
string
The name of the deployment rule.
options [_required_]
<oneOf>
Options for deployment rule response representing either faulty deployment detection or monitor options.
Option 1
object
Faulty deployment detection options for deployment rules.
duration
int64
The duration for faulty deployment detection.
excluded_resources
[string]
Resources to exclude from faulty deployment detection.
Option 2
object
Monitor options for deployment rules.
duration
int64
Seconds the monitor needs to stay in OK status for the rule to pass.
query [_required_]
string
Monitors that match this query are evaluated.
type [_required_]
enum
The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`
updated_at
date-time
The timestamp when the deployment rule was last updated.
updated_by
object
Information about the user who updated the deployment rule.
handle
string
The handle of the user who updated the deployment rule.
id [_required_]
string
The ID of the user who updated the deployment rule.
name
string
The name of the user who updated the deployment rule.
id [_required_]
string
Unique identifier of the deployment rule.
type [_required_]
enum
Deployment rule resource type. Allowed enum values: `deployment_rule`
```
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

Copy
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Deployment rule not found.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Deployment rule not found.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Update deployment rule returns "OK" response
Copy
```
                          # Path parameters  
export gate_id="CHANGE_ME"  
export id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules/${id}" \
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

                        
```

#####  Update deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update deployment rule returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete deployment rule](https://docs.datadoghq.com/api/latest/deployment-gates/#delete-deployment-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#delete-deployment-rule-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}https://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules/{id}
### Overview
Endpoint to delete a deployment rule. This endpoint requires the `deployment_gates_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
gate_id [_required_]
string
The ID of the deployment gate.
id [_required_]
string
The ID of the deployment rule.
### Response
  * [204](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentRule-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentRule-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentRule-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentRule-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#DeleteDeploymentRule-500-v2)


No Content
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Deployment gate not found.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Deployment gate not found.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Delete deployment rule
Copy
```
                  # Path parameters  
export gate_id="CHANGE_ME"  
export id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete deployment rule
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get rules for a deployment gate](https://docs.datadoghq.com/api/latest/deployment-gates/#get-rules-for-a-deployment-gate)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/deployment-gates/#get-rules-for-a-deployment-gate-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.ap2.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.datadoghq.eu/api/v2/deployment_gates/{gate_id}/ruleshttps://api.ddog-gov.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.us3.datadoghq.com/api/v2/deployment_gates/{gate_id}/ruleshttps://api.us5.datadoghq.com/api/v2/deployment_gates/{gate_id}/rules
### Overview
Endpoint to get rules for a deployment gate. This endpoint requires the `deployment_gates_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
gate_id [_required_]
string
The ID of the deployment gate.
### Response
  * [200](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGateRules-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGateRules-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGateRules-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGateRules-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGateRules-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/deployment-gates/#GetDeploymentGateRules-500-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Response for a deployment gate rules.
Field
Type
Description
data
object
Data for a list of deployment rules.
attributes [_required_]
object
rules
[object]
created_at [_required_]
date-time
The timestamp when the deployment rule was created.
created_by [_required_]
object
Information about the user who created the deployment rule.
handle
string
The handle of the user who created the deployment rule.
id [_required_]
string
The ID of the user who created the deployment rule.
name
string
The name of the user who created the deployment rule.
dry_run [_required_]
boolean
Whether this rule is run in dry-run mode.
gate_id [_required_]
string
The ID of the deployment gate.
name [_required_]
string
The name of the deployment rule.
options [_required_]
<oneOf>
Options for deployment rule response representing either faulty deployment detection or monitor options.
Option 1
object
Faulty deployment detection options for deployment rules.
duration
int64
The duration for faulty deployment detection.
excluded_resources
[string]
Resources to exclude from faulty deployment detection.
Option 2
object
Monitor options for deployment rules.
duration
int64
Seconds the monitor needs to stay in OK status for the rule to pass.
query [_required_]
string
Monitors that match this query are evaluated.
type [_required_]
enum
The type of the deployment rule. Allowed enum values: `faulty_deployment_detection,monitor`
updated_at
date-time
The timestamp when the deployment rule was last updated.
updated_by
object
Information about the user who updated the deployment rule.
handle
string
The handle of the user who updated the deployment rule.
id [_required_]
string
The ID of the user who updated the deployment rule.
name
string
The name of the user who updated the deployment rule.
id [_required_]
string
Unique identifier of the deployment rule.
type [_required_]
enum
List deployment rule resource type. Allowed enum values: `list_deployment_rules`
```
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

Copy
Bad request.
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Bad request.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


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
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/deployment-gates/)
  * [Example](https://docs.datadoghq.com/api/latest/deployment-gates/)


Errors occurred.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/deployment-gates/?code-lang=typescript)


#####  Get rules for a deployment gate
Copy
```
                  # Path parameters  
export gate_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/deployment_gates/${gate_id}/rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get rules for a deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get rules for a deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get rules for a deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get rules for a deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get rules for a deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get rules for a deployment gate
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=9b098a60-1ddc-4a8b-97ad-00564304212f&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c26a2ad5-007a-4427-8572-4dcaa693e022&pt=Deployment%20Gates&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdeployment-gates%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=9b098a60-1ddc-4a8b-97ad-00564304212f&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c26a2ad5-007a-4427-8572-4dcaa693e022&pt=Deployment%20Gates&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdeployment-gates%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=d0643678-bfda-4c6e-8080-d76964a9158d&bo=2&sid=a0b8b460f0bf11f0adcf65ee3e3f7e81&vid=a0b8f840f0bf11f090614bb702f21557&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Deployment%20Gates&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdeployment-gates%2F&r=&lt=2602&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=777830)
