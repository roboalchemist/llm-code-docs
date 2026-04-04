# Source: https://docs.datadoghq.com/api/latest/pagerduty-integration/

# PagerDuty Integration
Configure your [Datadog-PagerDuty integration](https://docs.datadoghq.com/integrations/pagerduty/) directly through the Datadog API.
## [Create a new service object](https://docs.datadoghq.com/api/latest/pagerduty-integration/#create-a-new-service-object)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/pagerduty-integration/#create-a-new-service-object-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/serviceshttps://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/serviceshttps://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/serviceshttps://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/serviceshttps://api.datadoghq.com/api/v1/integration/pagerduty/configuration/serviceshttps://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/serviceshttps://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services
### Overview
Create a new service object in the PagerDuty integration. This endpoint requires the `manage_integrations` permission.
### Request
#### Body Data (required)
Create a new service object request body.
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


Expand All
Field
Type
Description
service_key [_required_]
string
Your service key in PagerDuty.
service_name [_required_]
string
Your service name associated with a service key in PagerDuty.
```
{
  "service_key": "",
  "service_name": ""
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/pagerduty-integration/#CreatePagerDutyIntegrationService-201-v1)
  * [400](https://docs.datadoghq.com/api/latest/pagerduty-integration/#CreatePagerDutyIntegrationService-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/pagerduty-integration/#CreatePagerDutyIntegrationService-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/pagerduty-integration/#CreatePagerDutyIntegrationService-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


PagerDuty service object name.
Expand All
Field
Type
Description
service_name [_required_]
string
Your service name associated service key in PagerDuty.
```
{
  "service_name": ""
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=typescript)


#####  Create a new service object
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services" \
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

                
```

#####  Create a new service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a new service object
```
# Create a new service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new

body = DatadogAPIClient::V1::PagerDutyService.new({
  service_key: "",
  service_name: "",
})
p api_instance.create_pager_duty_integration_service(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a new service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a new service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a new service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a new service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a single service object](https://docs.datadoghq.com/api/latest/pagerduty-integration/#get-a-single-service-object)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/pagerduty-integration/#get-a-single-service-object-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}
### Overview
Get service name in the Datadog-PagerDuty integration. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_name [_required_]
string
The service name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/pagerduty-integration/#GetPagerDutyIntegrationService-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/pagerduty-integration/#GetPagerDutyIntegrationService-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/pagerduty-integration/#GetPagerDutyIntegrationService-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/pagerduty-integration/#GetPagerDutyIntegrationService-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


PagerDuty service object name.
Expand All
Field
Type
Description
service_name [_required_]
string
Your service name associated service key in PagerDuty.
```
{
  "service_name": ""
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=typescript)


#####  Get a single service object
Copy
```
                  # Path parameters  
export service_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/${service_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a single service object
```
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
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new
p api_instance.get_pager_duty_integration_service("service_name")

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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a single service object](https://docs.datadoghq.com/api/latest/pagerduty-integration/#update-a-single-service-object)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/pagerduty-integration/#update-a-single-service-object-v1)


PUT https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}
### Overview
Update a single service object in the Datadog-PagerDuty integration. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_name [_required_]
string
The service name
### Request
#### Body Data (required)
Update an existing service object request body.
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


Expand All
Field
Type
Description
service_key [_required_]
string
Your service key in PagerDuty.
```
{
  "service_key": ""
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/pagerduty-integration/#UpdatePagerDutyIntegrationService-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/pagerduty-integration/#UpdatePagerDutyIntegrationService-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/pagerduty-integration/#UpdatePagerDutyIntegrationService-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/pagerduty-integration/#UpdatePagerDutyIntegrationService-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/pagerduty-integration/#UpdatePagerDutyIntegrationService-429-v1)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=typescript)


#####  Update a single service object
Copy
```
                  # Path parameters  
export service_name="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/${service_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "service_key": ""
}
EOF  

                
```

#####  Update a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a single service object
```
# Update a single service object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new

body = DatadogAPIClient::V1::PagerDutyServiceKey.new({
  service_key: "",
})
p api_instance.update_pager_duty_integration_service("service_name", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete a single service object](https://docs.datadoghq.com/api/latest/pagerduty-integration/#delete-a-single-service-object)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/pagerduty-integration/#delete-a-single-service-object-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.ap2.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.datadoghq.eu/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.ddog-gov.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.us3.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/{service_name}
### Overview
Delete a single service object in the Datadog-PagerDuty integration. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
service_name [_required_]
string
The service name
### Response
  * [204](https://docs.datadoghq.com/api/latest/pagerduty-integration/#DeletePagerDutyIntegrationService-204-v1)
  * [403](https://docs.datadoghq.com/api/latest/pagerduty-integration/#DeletePagerDutyIntegrationService-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/pagerduty-integration/#DeletePagerDutyIntegrationService-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/pagerduty-integration/#DeletePagerDutyIntegrationService-429-v1)


No Content
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/pagerduty-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/pagerduty-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/pagerduty-integration/?code-lang=typescript)


#####  Delete a single service object
Copy
```
                  # Path parameters  
export service_name="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/pagerduty/configuration/services/${service_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a single service object
```
# Delete a single service object returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::PagerDutyIntegrationAPI.new
api_instance.delete_pager_duty_integration_service("service_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete a single service object
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a9b1d464-2840-45fd-a6ec-38b7b41d636b&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=eab1f73b-1214-49a9-a651-0951a6e5cef6&pt=PagerDuty%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fpagerduty-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a9b1d464-2840-45fd-a6ec-38b7b41d636b&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=eab1f73b-1214-49a9-a651-0951a6e5cef6&pt=PagerDuty%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fpagerduty-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=2963a30f-94ea-4d10-a5f8-435cf350e671&bo=2&sid=545458e0f0c011f0a1a8c3a4f135763b&vid=54545f80f0c011f0909d2faa02b2847c&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=PagerDuty%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fpagerduty-integration%2F&r=&lt=1518&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=145823)
