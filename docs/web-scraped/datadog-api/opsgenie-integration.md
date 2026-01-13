# Source: https://docs.datadoghq.com/api/latest/opsgenie-integration/

# Opsgenie Integration
Configure your [Datadog Opsgenie integration](https://docs.datadoghq.com/integrations/opsgenie/) directly through the Datadog API.
## [Get all service objects](https://docs.datadoghq.com/api/latest/opsgenie-integration/#get-all-service-objects)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/opsgenie-integration/#get-all-service-objects-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.ap2.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.datadoghq.eu/api/v2/integration/opsgenie/serviceshttps://api.ddog-gov.com/api/v2/integration/opsgenie/serviceshttps://api.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.us3.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.us5.datadoghq.com/api/v2/integration/opsgenie/services
### Overview
Get a list of all services from the Datadog Opsgenie integration. This endpoint requires the `integrations_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/opsgenie-integration/#ListOpsgenieServices-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/opsgenie-integration/#ListOpsgenieServices-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/opsgenie-integration/#ListOpsgenieServices-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


Response with a list of Opsgenie services.
Field
Type
Description
data [_required_]
[object]
An array of Opsgenie services.
attributes [_required_]
object
The attributes from an Opsgenie service response.
custom_url
string
The custom URL for a custom region.
name
string
The name for the Opsgenie service.
region
enum
The region for the Opsgenie service. Allowed enum values: `us,eu,custom`
id [_required_]
string
The ID of the Opsgenie service.
type [_required_]
enum
Opsgenie service resource type. Allowed enum values: `opsgenie-service`
default: `opsgenie-service`
```
{
  "data": [
    {
      "attributes": {
        "custom_url": null,
        "name": "fake-opsgenie-service-name",
        "region": "us"
      },
      "id": "596da4af-0563-4097-90ff-07230c3f9db3",
      "type": "opsgenie-service"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=typescript)


#####  Get all service objects
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all service objects
```
"""
Get all service objects returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.list_opsgenie_services()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all service objects
```
# Get all service objects returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OpsgenieIntegrationAPI.new
p api_instance.list_opsgenie_services()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all service objects
```
// Get all service objects returns "OK" response

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
	api := datadogV2.NewOpsgenieIntegrationApi(apiClient)
	resp, r, err := api.ListOpsgenieServices(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OpsgenieIntegrationApi.ListOpsgenieServices`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OpsgenieIntegrationApi.ListOpsgenieServices`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all service objects
```
// Get all service objects returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OpsgenieIntegrationApi;
import com.datadog.api.client.v2.model.OpsgenieServicesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OpsgenieIntegrationApi apiInstance = new OpsgenieIntegrationApi(defaultClient);

    try {
      OpsgenieServicesResponse result = apiInstance.listOpsgenieServices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpsgenieIntegrationApi#listOpsgenieServices");
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

#####  Get all service objects
```
// Get all service objects returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_opsgenie_integration::OpsgenieIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OpsgenieIntegrationAPI::with_config(configuration);
    let resp = api.list_opsgenie_services().await;
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

#####  Get all service objects
```
/**
 * Get all service objects returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OpsgenieIntegrationApi(configuration);

apiInstance
  .listOpsgenieServices()
  .then((data: v2.OpsgenieServicesResponse) => {
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
## [Create a new service object](https://docs.datadoghq.com/api/latest/opsgenie-integration/#create-a-new-service-object)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/opsgenie-integration/#create-a-new-service-object-v2)


POST https://api.ap1.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.ap2.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.datadoghq.eu/api/v2/integration/opsgenie/serviceshttps://api.ddog-gov.com/api/v2/integration/opsgenie/serviceshttps://api.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.us3.datadoghq.com/api/v2/integration/opsgenie/serviceshttps://api.us5.datadoghq.com/api/v2/integration/opsgenie/services
### Overview
Create a new service object in the Opsgenie integration. This endpoint requires the `manage_integrations` permission.
### Request
#### Body Data (required)
Opsgenie service payload
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


Field
Type
Description
data [_required_]
object
Opsgenie service data for a create request.
attributes [_required_]
object
The Opsgenie service attributes for a create request.
custom_url
string
The custom URL for a custom region.
name [_required_]
string
The name for the Opsgenie service.
opsgenie_api_key [_required_]
string
The Opsgenie API key for your Opsgenie service.
region [_required_]
enum
The region for the Opsgenie service. Allowed enum values: `us,eu,custom`
type [_required_]
enum
Opsgenie service resource type. Allowed enum values: `opsgenie-service`
default: `opsgenie-service`
```
{
  "data": {
    "attributes": {
      "name": "Example-Opsgenie-Integration",
      "opsgenie_api_key": "00000000-0000-0000-0000-000000000000",
      "region": "us"
    },
    "type": "opsgenie-service"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/opsgenie-integration/#CreateOpsgenieService-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/opsgenie-integration/#CreateOpsgenieService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/opsgenie-integration/#CreateOpsgenieService-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/opsgenie-integration/#CreateOpsgenieService-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/opsgenie-integration/#CreateOpsgenieService-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


Response of an Opsgenie service.
Field
Type
Description
data [_required_]
object
Opsgenie service data from a response.
attributes [_required_]
object
The attributes from an Opsgenie service response.
custom_url
string
The custom URL for a custom region.
name
string
The name for the Opsgenie service.
region
enum
The region for the Opsgenie service. Allowed enum values: `us,eu,custom`
id [_required_]
string
The ID of the Opsgenie service.
type [_required_]
enum
Opsgenie service resource type. Allowed enum values: `opsgenie-service`
default: `opsgenie-service`
```
{
  "data": {
    "attributes": {
      "custom_url": null,
      "name": "fake-opsgenie-service-name",
      "region": "us"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "opsgenie-service"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=typescript)


#####  Create a new service object returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-Opsgenie-Integration",
      "opsgenie_api_key": "00000000-0000-0000-0000-000000000000",
      "region": "us"
    },
    "type": "opsgenie-service"
  }
}
EOF  

                        
```

#####  Create a new service object returns "CREATED" response
```
// Create a new service object returns "CREATED" response

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
	body := datadogV2.OpsgenieServiceCreateRequest{
		Data: datadogV2.OpsgenieServiceCreateData{
			Attributes: datadogV2.OpsgenieServiceCreateAttributes{
				Name:           "Example-Opsgenie-Integration",
				OpsgenieApiKey: "00000000-0000-0000-0000-000000000000",
				Region:         datadogV2.OPSGENIESERVICEREGIONTYPE_US,
			},
			Type: datadogV2.OPSGENIESERVICETYPE_OPSGENIE_SERVICE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOpsgenieIntegrationApi(apiClient)
	resp, r, err := api.CreateOpsgenieService(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OpsgenieIntegrationApi.CreateOpsgenieService`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OpsgenieIntegrationApi.CreateOpsgenieService`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a new service object returns "CREATED" response
```
// Create a new service object returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OpsgenieIntegrationApi;
import com.datadog.api.client.v2.model.OpsgenieServiceCreateAttributes;
import com.datadog.api.client.v2.model.OpsgenieServiceCreateData;
import com.datadog.api.client.v2.model.OpsgenieServiceCreateRequest;
import com.datadog.api.client.v2.model.OpsgenieServiceRegionType;
import com.datadog.api.client.v2.model.OpsgenieServiceResponse;
import com.datadog.api.client.v2.model.OpsgenieServiceType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OpsgenieIntegrationApi apiInstance = new OpsgenieIntegrationApi(defaultClient);

    OpsgenieServiceCreateRequest body =
        new OpsgenieServiceCreateRequest()
            .data(
                new OpsgenieServiceCreateData()
                    .attributes(
                        new OpsgenieServiceCreateAttributes()
                            .name("Example-Opsgenie-Integration")
                            .opsgenieApiKey("00000000-0000-0000-0000-000000000000")
                            .region(OpsgenieServiceRegionType.US))
                    .type(OpsgenieServiceType.OPSGENIE_SERVICE));

    try {
      OpsgenieServiceResponse result = apiInstance.createOpsgenieService(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpsgenieIntegrationApi#createOpsgenieService");
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

#####  Create a new service object returns "CREATED" response
```
"""
Create a new service object returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_service_create_attributes import OpsgenieServiceCreateAttributes
from datadog_api_client.v2.model.opsgenie_service_create_data import OpsgenieServiceCreateData
from datadog_api_client.v2.model.opsgenie_service_create_request import OpsgenieServiceCreateRequest
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType
from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType

body = OpsgenieServiceCreateRequest(
    data=OpsgenieServiceCreateData(
        attributes=OpsgenieServiceCreateAttributes(
            name="Example-Opsgenie-Integration",
            opsgenie_api_key="00000000-0000-0000-0000-000000000000",
            region=OpsgenieServiceRegionType.US,
        ),
        type=OpsgenieServiceType.OPSGENIE_SERVICE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.create_opsgenie_service(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a new service object returns "CREATED" response
```
# Create a new service object returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OpsgenieIntegrationAPI.new

body = DatadogAPIClient::V2::OpsgenieServiceCreateRequest.new({
  data: DatadogAPIClient::V2::OpsgenieServiceCreateData.new({
    attributes: DatadogAPIClient::V2::OpsgenieServiceCreateAttributes.new({
      name: "Example-Opsgenie-Integration",
      opsgenie_api_key: "00000000-0000-0000-0000-000000000000",
      region: DatadogAPIClient::V2::OpsgenieServiceRegionType::US,
    }),
    type: DatadogAPIClient::V2::OpsgenieServiceType::OPSGENIE_SERVICE,
  }),
})
p api_instance.create_opsgenie_service(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a new service object returns "CREATED" response
```
// Create a new service object returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_opsgenie_integration::OpsgenieIntegrationAPI;
use datadog_api_client::datadogV2::model::OpsgenieServiceCreateAttributes;
use datadog_api_client::datadogV2::model::OpsgenieServiceCreateData;
use datadog_api_client::datadogV2::model::OpsgenieServiceCreateRequest;
use datadog_api_client::datadogV2::model::OpsgenieServiceRegionType;
use datadog_api_client::datadogV2::model::OpsgenieServiceType;

#[tokio::main]
async fn main() {
    let body = OpsgenieServiceCreateRequest::new(OpsgenieServiceCreateData::new(
        OpsgenieServiceCreateAttributes::new(
            "Example-Opsgenie-Integration".to_string(),
            "00000000-0000-0000-0000-000000000000".to_string(),
            OpsgenieServiceRegionType::US,
        ),
        OpsgenieServiceType::OPSGENIE_SERVICE,
    ));
    let configuration = datadog::Configuration::new();
    let api = OpsgenieIntegrationAPI::with_config(configuration);
    let resp = api.create_opsgenie_service(body).await;
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

#####  Create a new service object returns "CREATED" response
```
/**
 * Create a new service object returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OpsgenieIntegrationApi(configuration);

const params: v2.OpsgenieIntegrationApiCreateOpsgenieServiceRequest = {
  body: {
    data: {
      attributes: {
        name: "Example-Opsgenie-Integration",
        opsgenieApiKey: "00000000-0000-0000-0000-000000000000",
        region: "us",
      },
      type: "opsgenie-service",
    },
  },
};

apiInstance
  .createOpsgenieService(params)
  .then((data: v2.OpsgenieServiceResponse) => {
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
## [Get a single service object](https://docs.datadoghq.com/api/latest/opsgenie-integration/#get-a-single-service-object)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/opsgenie-integration/#get-a-single-service-object-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.ap2.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.datadoghq.eu/api/v2/integration/opsgenie/services/{integration_service_id}https://api.ddog-gov.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.us3.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}
### Overview
Get a single service from the Datadog Opsgenie integration. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
integration_service_id [_required_]
string
The UUID of the service.
### Response
  * [200](https://docs.datadoghq.com/api/latest/opsgenie-integration/#GetOpsgenieService-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/opsgenie-integration/#GetOpsgenieService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/opsgenie-integration/#GetOpsgenieService-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/opsgenie-integration/#GetOpsgenieService-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/opsgenie-integration/#GetOpsgenieService-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/opsgenie-integration/#GetOpsgenieService-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


Response of an Opsgenie service.
Field
Type
Description
data [_required_]
object
Opsgenie service data from a response.
attributes [_required_]
object
The attributes from an Opsgenie service response.
custom_url
string
The custom URL for a custom region.
name
string
The name for the Opsgenie service.
region
enum
The region for the Opsgenie service. Allowed enum values: `us,eu,custom`
id [_required_]
string
The ID of the Opsgenie service.
type [_required_]
enum
Opsgenie service resource type. Allowed enum values: `opsgenie-service`
default: `opsgenie-service`
```
{
  "data": {
    "attributes": {
      "custom_url": null,
      "name": "fake-opsgenie-service-name",
      "region": "us"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "opsgenie-service"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=typescript)


#####  Get a single service object
Copy
```
                  # Path parameters  
export integration_service_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services/${integration_service_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a single service object
```
"""
Get a single service object returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ID = environ["OPSGENIE_SERVICE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.get_opsgenie_service(
        integration_service_id=OPSGENIE_SERVICE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a single service object
```
# Get a single service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OpsgenieIntegrationAPI.new

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ID = ENV["OPSGENIE_SERVICE_DATA_ID"]
p api_instance.get_opsgenie_service(OPSGENIE_SERVICE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a single service object
```
// Get a single service object returns "OK" response

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
	// there is a valid "opsgenie_service" in the system
	OpsgenieServiceDataID := os.Getenv("OPSGENIE_SERVICE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOpsgenieIntegrationApi(apiClient)
	resp, r, err := api.GetOpsgenieService(ctx, OpsgenieServiceDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OpsgenieIntegrationApi.GetOpsgenieService`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OpsgenieIntegrationApi.GetOpsgenieService`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a single service object
```
// Get a single service object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OpsgenieIntegrationApi;
import com.datadog.api.client.v2.model.OpsgenieServiceResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OpsgenieIntegrationApi apiInstance = new OpsgenieIntegrationApi(defaultClient);

    // there is a valid "opsgenie_service" in the system
    String OPSGENIE_SERVICE_DATA_ID = System.getenv("OPSGENIE_SERVICE_DATA_ID");

    try {
      OpsgenieServiceResponse result = apiInstance.getOpsgenieService(OPSGENIE_SERVICE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpsgenieIntegrationApi#getOpsgenieService");
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

#####  Get a single service object
```
// Get a single service object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_opsgenie_integration::OpsgenieIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "opsgenie_service" in the system
    let opsgenie_service_data_id = std::env::var("OPSGENIE_SERVICE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OpsgenieIntegrationAPI::with_config(configuration);
    let resp = api
        .get_opsgenie_service(opsgenie_service_data_id.clone())
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

#####  Get a single service object
```
/**
 * Get a single service object returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OpsgenieIntegrationApi(configuration);

// there is a valid "opsgenie_service" in the system
const OPSGENIE_SERVICE_DATA_ID = process.env.OPSGENIE_SERVICE_DATA_ID as string;

const params: v2.OpsgenieIntegrationApiGetOpsgenieServiceRequest = {
  integrationServiceId: OPSGENIE_SERVICE_DATA_ID,
};

apiInstance
  .getOpsgenieService(params)
  .then((data: v2.OpsgenieServiceResponse) => {
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
## [Update a single service object](https://docs.datadoghq.com/api/latest/opsgenie-integration/#update-a-single-service-object)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/opsgenie-integration/#update-a-single-service-object-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.ap2.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.datadoghq.eu/api/v2/integration/opsgenie/services/{integration_service_id}https://api.ddog-gov.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.us3.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}
### Overview
Update a single service object in the Datadog Opsgenie integration. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
integration_service_id [_required_]
string
The UUID of the service.
### Request
#### Body Data (required)
Opsgenie service payload.
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


Field
Type
Description
data [_required_]
object
Opsgenie service for an update request.
attributes [_required_]
object
The Opsgenie service attributes for an update request.
custom_url
string
The custom URL for a custom region.
name
string
The name for the Opsgenie service.
opsgenie_api_key
string
The Opsgenie API key for your Opsgenie service.
region
enum
The region for the Opsgenie service. Allowed enum values: `us,eu,custom`
id [_required_]
string
The ID of the Opsgenie service.
type [_required_]
enum
Opsgenie service resource type. Allowed enum values: `opsgenie-service`
default: `opsgenie-service`
```
{
  "data": {
    "attributes": {
      "name": "fake-opsgenie-service-name--updated",
      "opsgenie_api_key": "00000000-0000-0000-0000-000000000000",
      "region": "eu"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "opsgenie-service"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/opsgenie-integration/#UpdateOpsgenieService-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/opsgenie-integration/#UpdateOpsgenieService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/opsgenie-integration/#UpdateOpsgenieService-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/opsgenie-integration/#UpdateOpsgenieService-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/opsgenie-integration/#UpdateOpsgenieService-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/opsgenie-integration/#UpdateOpsgenieService-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


Response of an Opsgenie service.
Field
Type
Description
data [_required_]
object
Opsgenie service data from a response.
attributes [_required_]
object
The attributes from an Opsgenie service response.
custom_url
string
The custom URL for a custom region.
name
string
The name for the Opsgenie service.
region
enum
The region for the Opsgenie service. Allowed enum values: `us,eu,custom`
id [_required_]
string
The ID of the Opsgenie service.
type [_required_]
enum
Opsgenie service resource type. Allowed enum values: `opsgenie-service`
default: `opsgenie-service`
```
{
  "data": {
    "attributes": {
      "custom_url": null,
      "name": "fake-opsgenie-service-name",
      "region": "us"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "opsgenie-service"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=typescript)


#####  Update a single service object returns "OK" response
Copy
```
                          # Path parameters  
export integration_service_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services/${integration_service_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "fake-opsgenie-service-name--updated",
      "opsgenie_api_key": "00000000-0000-0000-0000-000000000000",
      "region": "eu"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "opsgenie-service"
  }
}
EOF  

                        
```

#####  Update a single service object returns "OK" response
```
// Update a single service object returns "OK" response

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
	// there is a valid "opsgenie_service" in the system
	OpsgenieServiceDataID := os.Getenv("OPSGENIE_SERVICE_DATA_ID")

	body := datadogV2.OpsgenieServiceUpdateRequest{
		Data: datadogV2.OpsgenieServiceUpdateData{
			Attributes: datadogV2.OpsgenieServiceUpdateAttributes{
				Name:           datadog.PtrString("fake-opsgenie-service-name--updated"),
				OpsgenieApiKey: datadog.PtrString("00000000-0000-0000-0000-000000000000"),
				Region:         datadogV2.OPSGENIESERVICEREGIONTYPE_EU.Ptr(),
			},
			Id:   OpsgenieServiceDataID,
			Type: datadogV2.OPSGENIESERVICETYPE_OPSGENIE_SERVICE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOpsgenieIntegrationApi(apiClient)
	resp, r, err := api.UpdateOpsgenieService(ctx, OpsgenieServiceDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OpsgenieIntegrationApi.UpdateOpsgenieService`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OpsgenieIntegrationApi.UpdateOpsgenieService`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a single service object returns "OK" response
```
// Update a single service object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OpsgenieIntegrationApi;
import com.datadog.api.client.v2.model.OpsgenieServiceRegionType;
import com.datadog.api.client.v2.model.OpsgenieServiceResponse;
import com.datadog.api.client.v2.model.OpsgenieServiceType;
import com.datadog.api.client.v2.model.OpsgenieServiceUpdateAttributes;
import com.datadog.api.client.v2.model.OpsgenieServiceUpdateData;
import com.datadog.api.client.v2.model.OpsgenieServiceUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OpsgenieIntegrationApi apiInstance = new OpsgenieIntegrationApi(defaultClient);

    // there is a valid "opsgenie_service" in the system
    String OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME =
        System.getenv("OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME");
    String OPSGENIE_SERVICE_DATA_ID = System.getenv("OPSGENIE_SERVICE_DATA_ID");

    OpsgenieServiceUpdateRequest body =
        new OpsgenieServiceUpdateRequest()
            .data(
                new OpsgenieServiceUpdateData()
                    .attributes(
                        new OpsgenieServiceUpdateAttributes()
                            .name("fake-opsgenie-service-name--updated")
                            .opsgenieApiKey("00000000-0000-0000-0000-000000000000")
                            .region(OpsgenieServiceRegionType.EU))
                    .id(OPSGENIE_SERVICE_DATA_ID)
                    .type(OpsgenieServiceType.OPSGENIE_SERVICE));

    try {
      OpsgenieServiceResponse result =
          apiInstance.updateOpsgenieService(OPSGENIE_SERVICE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpsgenieIntegrationApi#updateOpsgenieService");
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

#####  Update a single service object returns "OK" response
```
"""
Update a single service object returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType
from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType
from datadog_api_client.v2.model.opsgenie_service_update_attributes import OpsgenieServiceUpdateAttributes
from datadog_api_client.v2.model.opsgenie_service_update_data import OpsgenieServiceUpdateData
from datadog_api_client.v2.model.opsgenie_service_update_request import OpsgenieServiceUpdateRequest

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME = environ["OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME"]
OPSGENIE_SERVICE_DATA_ID = environ["OPSGENIE_SERVICE_DATA_ID"]

body = OpsgenieServiceUpdateRequest(
    data=OpsgenieServiceUpdateData(
        attributes=OpsgenieServiceUpdateAttributes(
            name="fake-opsgenie-service-name--updated",
            opsgenie_api_key="00000000-0000-0000-0000-000000000000",
            region=OpsgenieServiceRegionType.EU,
        ),
        id=OPSGENIE_SERVICE_DATA_ID,
        type=OpsgenieServiceType.OPSGENIE_SERVICE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.update_opsgenie_service(integration_service_id=OPSGENIE_SERVICE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a single service object returns "OK" response
```
# Update a single service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OpsgenieIntegrationAPI.new

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME = ENV["OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME"]
OPSGENIE_SERVICE_DATA_ID = ENV["OPSGENIE_SERVICE_DATA_ID"]

body = DatadogAPIClient::V2::OpsgenieServiceUpdateRequest.new({
  data: DatadogAPIClient::V2::OpsgenieServiceUpdateData.new({
    attributes: DatadogAPIClient::V2::OpsgenieServiceUpdateAttributes.new({
      name: "fake-opsgenie-service-name--updated",
      opsgenie_api_key: "00000000-0000-0000-0000-000000000000",
      region: DatadogAPIClient::V2::OpsgenieServiceRegionType::EU,
    }),
    id: OPSGENIE_SERVICE_DATA_ID,
    type: DatadogAPIClient::V2::OpsgenieServiceType::OPSGENIE_SERVICE,
  }),
})
p api_instance.update_opsgenie_service(OPSGENIE_SERVICE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a single service object returns "OK" response
```
// Update a single service object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_opsgenie_integration::OpsgenieIntegrationAPI;
use datadog_api_client::datadogV2::model::OpsgenieServiceRegionType;
use datadog_api_client::datadogV2::model::OpsgenieServiceType;
use datadog_api_client::datadogV2::model::OpsgenieServiceUpdateAttributes;
use datadog_api_client::datadogV2::model::OpsgenieServiceUpdateData;
use datadog_api_client::datadogV2::model::OpsgenieServiceUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "opsgenie_service" in the system
    let opsgenie_service_data_id = std::env::var("OPSGENIE_SERVICE_DATA_ID").unwrap();
    let body = OpsgenieServiceUpdateRequest::new(OpsgenieServiceUpdateData::new(
        OpsgenieServiceUpdateAttributes::new()
            .name("fake-opsgenie-service-name--updated".to_string())
            .opsgenie_api_key("00000000-0000-0000-0000-000000000000".to_string())
            .region(OpsgenieServiceRegionType::EU),
        opsgenie_service_data_id.clone(),
        OpsgenieServiceType::OPSGENIE_SERVICE,
    ));
    let configuration = datadog::Configuration::new();
    let api = OpsgenieIntegrationAPI::with_config(configuration);
    let resp = api
        .update_opsgenie_service(opsgenie_service_data_id.clone(), body)
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

#####  Update a single service object returns "OK" response
```
/**
 * Update a single service object returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OpsgenieIntegrationApi(configuration);

// there is a valid "opsgenie_service" in the system
const OPSGENIE_SERVICE_DATA_ID = process.env.OPSGENIE_SERVICE_DATA_ID as string;

const params: v2.OpsgenieIntegrationApiUpdateOpsgenieServiceRequest = {
  body: {
    data: {
      attributes: {
        name: "fake-opsgenie-service-name--updated",
        opsgenieApiKey: "00000000-0000-0000-0000-000000000000",
        region: "eu",
      },
      id: OPSGENIE_SERVICE_DATA_ID,
      type: "opsgenie-service",
    },
  },
  integrationServiceId: OPSGENIE_SERVICE_DATA_ID,
};

apiInstance
  .updateOpsgenieService(params)
  .then((data: v2.OpsgenieServiceResponse) => {
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
## [Delete a single service object](https://docs.datadoghq.com/api/latest/opsgenie-integration/#delete-a-single-service-object)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/opsgenie-integration/#delete-a-single-service-object-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.ap2.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.datadoghq.eu/api/v2/integration/opsgenie/services/{integration_service_id}https://api.ddog-gov.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.us3.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services/{integration_service_id}
### Overview
Delete a single service object in the Datadog Opsgenie integration. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
integration_service_id [_required_]
string
The UUID of the service.
### Response
  * [204](https://docs.datadoghq.com/api/latest/opsgenie-integration/#DeleteOpsgenieService-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/opsgenie-integration/#DeleteOpsgenieService-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/opsgenie-integration/#DeleteOpsgenieService-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/opsgenie-integration/#DeleteOpsgenieService-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/opsgenie-integration/#DeleteOpsgenieService-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/opsgenie-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/opsgenie-integration/?code-lang=typescript)


#####  Delete a single service object
Copy
```
                  # Path parameters  
export integration_service_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/opsgenie/services/${integration_service_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a single service object
```
"""
Delete a single service object returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ID = environ["OPSGENIE_SERVICE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    api_instance.delete_opsgenie_service(
        integration_service_id=OPSGENIE_SERVICE_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a single service object
```
# Delete a single service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OpsgenieIntegrationAPI.new

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ID = ENV["OPSGENIE_SERVICE_DATA_ID"]
api_instance.delete_opsgenie_service(OPSGENIE_SERVICE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a single service object
```
// Delete a single service object returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "opsgenie_service" in the system
	OpsgenieServiceDataID := os.Getenv("OPSGENIE_SERVICE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOpsgenieIntegrationApi(apiClient)
	r, err := api.DeleteOpsgenieService(ctx, OpsgenieServiceDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OpsgenieIntegrationApi.DeleteOpsgenieService`: %v\n", err)
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

#####  Delete a single service object
```
// Delete a single service object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OpsgenieIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OpsgenieIntegrationApi apiInstance = new OpsgenieIntegrationApi(defaultClient);

    // there is a valid "opsgenie_service" in the system
    String OPSGENIE_SERVICE_DATA_ID = System.getenv("OPSGENIE_SERVICE_DATA_ID");

    try {
      apiInstance.deleteOpsgenieService(OPSGENIE_SERVICE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpsgenieIntegrationApi#deleteOpsgenieService");
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

#####  Delete a single service object
```
// Delete a single service object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_opsgenie_integration::OpsgenieIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "opsgenie_service" in the system
    let opsgenie_service_data_id = std::env::var("OPSGENIE_SERVICE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = OpsgenieIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_opsgenie_service(opsgenie_service_data_id.clone())
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

#####  Delete a single service object
```
/**
 * Delete a single service object returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OpsgenieIntegrationApi(configuration);

// there is a valid "opsgenie_service" in the system
const OPSGENIE_SERVICE_DATA_ID = process.env.OPSGENIE_SERVICE_DATA_ID as string;

const params: v2.OpsgenieIntegrationApiDeleteOpsgenieServiceRequest = {
  integrationServiceId: OPSGENIE_SERVICE_DATA_ID,
};

apiInstance
  .deleteOpsgenieService(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=5b95167d-bab5-46e8-b6e0-b82a7ff67125&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d674958b-f4d8-449f-af09-8b4a37a44e4d&pt=Opsgenie%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fopsgenie-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=5b95167d-bab5-46e8-b6e0-b82a7ff67125&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d674958b-f4d8-449f-af09-8b4a37a44e4d&pt=Opsgenie%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fopsgenie-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=24be1a87-b4d3-436c-be85-83ad998bf962&bo=2&sid=4afb3340f0c011f0a70bcf3adf5a320c&vid=4afb72d0f0c011f0a0b97926bab7a539&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Opsgenie%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fopsgenie-integration%2F&r=&lt=1333&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=127594)
