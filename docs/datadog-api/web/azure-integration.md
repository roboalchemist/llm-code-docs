# Source: https://docs.datadoghq.com/api/latest/azure-integration/

# Azure Integration
Configure your Datadog-Azure integration directly through the Datadog API. For more information, see the [Datadog-Azure integration page](https://docs.datadoghq.com/integrations/azure).
## [List all Azure integrations](https://docs.datadoghq.com/api/latest/azure-integration/#list-all-azure-integrations)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/azure-integration/#list-all-azure-integrations-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/azurehttps://api.ap2.datadoghq.com/api/v1/integration/azurehttps://api.datadoghq.eu/api/v1/integration/azurehttps://api.ddog-gov.com/api/v1/integration/azurehttps://api.datadoghq.com/api/v1/integration/azurehttps://api.us3.datadoghq.com/api/v1/integration/azurehttps://api.us5.datadoghq.com/api/v1/integration/azure
### Overview
List all Datadog-Azure integrations configured in your Datadog account. This endpoint requires the `azure_configuration_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/azure-integration/#ListAzureIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/azure-integration/#ListAzureIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/azure-integration/#ListAzureIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/azure-integration/#ListAzureIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Accounts configured for your organization.
Field
Type
Description
app_service_plan_filters
string
Limit the Azure app service plans that are pulled into Datadog using tags. Only app service plans that match one of the defined tags are imported into Datadog.
automute
boolean
Silence monitors for expected Azure VM shutdowns.
client_id
string
Your Azure web application ID.
client_secret
string
Your Azure web application secret key.
container_app_filters
string
Limit the Azure container apps that are pulled into Datadog using tags. Only container apps that match one of the defined tags are imported into Datadog.
cspm_enabled
boolean
When enabled, Datadog’s Cloud Security Management product scans resource configurations monitored by this app registration. Note: This requires resource_collection_enabled to be set to true.
custom_metrics_enabled
boolean
Enable custom metrics for your organization.
errors
[string]
Errors in your configuration.
host_filters
string
Limit the Azure instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.
metrics_enabled
boolean
Enable Azure metrics for your organization.
metrics_enabled_default
boolean
Enable Azure metrics for your organization for resource providers where no resource provider config is specified.
new_client_id
string
Your New Azure web application ID.
new_tenant_name
string
Your New Azure Active Directory ID.
resource_collection_enabled
boolean
When enabled, Datadog collects metadata and configuration info from cloud resources (compute instances, databases, load balancers, etc.) monitored by this app registration.
resource_provider_configs
[object]
Configuration settings applied to resources from the specified Azure resource providers.
metrics_enabled
boolean
Collect metrics for resources from this provider.
namespace
string
The provider namespace to apply this configuration to.
tenant_name
string
Your Azure Active Directory ID.
usage_metrics_enabled
boolean
Enable azure.usage metrics for your organization.
```
{
  "app_service_plan_filters": "key:value,filter:example",
  "automute": true,
  "client_id": "testc7f6-1234-5678-9101-3fcbf464test",
  "client_secret": "TestingRh2nx664kUy5dIApvM54T4AtO",
  "container_app_filters": "key:value,filter:example",
  "cspm_enabled": true,
  "custom_metrics_enabled": true,
  "errors": [
    "*"
  ],
  "host_filters": "key:value,filter:example",
  "metrics_enabled": true,
  "metrics_enabled_default": true,
  "new_client_id": "new1c7f6-1234-5678-9101-3fcbf464test",
  "new_tenant_name": "new1c44-1234-5678-9101-cc00736ftest",
  "resource_collection_enabled": true,
  "resource_provider_configs": [
    {
      "metrics_enabled": true,
      "namespace": "Microsoft.Compute"
    }
  ],
  "tenant_name": "testc44-1234-5678-9101-cc00736ftest",
  "usage_metrics_enabled": true
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python-legacy)


#####  List all Azure integrations
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/azure" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all Azure integrations
```
"""
List all Azure integrations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.list_azure_integration()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List all Azure integrations
```
# List all Azure integrations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AzureIntegrationAPI.new
p api_instance.list_azure_integration()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all Azure integrations
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.azure_integration_list

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all Azure integrations
```
// List all Azure integrations returns "OK" response

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
	api := datadogV1.NewAzureIntegrationApi(apiClient)
	resp, r, err := api.ListAzureIntegration(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AzureIntegrationApi.ListAzureIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AzureIntegrationApi.ListAzureIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List all Azure integrations
```
// List all Azure integrations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AzureIntegrationApi;
import com.datadog.api.client.v1.model.AzureAccount;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AzureIntegrationApi apiInstance = new AzureIntegrationApi(defaultClient);

    try {
      List<AzureAccount> result = apiInstance.listAzureIntegration();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AzureIntegrationApi#listAzureIntegration");
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

#####  List all Azure integrations
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AzureIntegration.list()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  List all Azure integrations
```
// List all Azure integrations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_azure_integration::AzureIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AzureIntegrationAPI::with_config(configuration);
    let resp = api.list_azure_integration().await;
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

#####  List all Azure integrations
```
/**
 * List all Azure integrations returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AzureIntegrationApi(configuration);

apiInstance
  .listAzureIntegration()
  .then((data: v1.AzureAccount[]) => {
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
## [Create an Azure integration](https://docs.datadoghq.com/api/latest/azure-integration/#create-an-azure-integration)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/azure-integration/#create-an-azure-integration-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/azurehttps://api.ap2.datadoghq.com/api/v1/integration/azurehttps://api.datadoghq.eu/api/v1/integration/azurehttps://api.ddog-gov.com/api/v1/integration/azurehttps://api.datadoghq.com/api/v1/integration/azurehttps://api.us3.datadoghq.com/api/v1/integration/azurehttps://api.us5.datadoghq.com/api/v1/integration/azure
### Overview
Create a Datadog-Azure integration.
Using the `POST` method updates your integration configuration by adding your new configuration to the existing one in your Datadog organization.
Using the `PUT` method updates your integration configuration by replacing your current configuration with the new one sent to your Datadog organization.
This endpoint requires the `azure_configurations_manage` permission.
### Request
#### Body Data (required)
Create a Datadog-Azure integration for your Datadog account request body.
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Field
Type
Description
app_service_plan_filters
string
Limit the Azure app service plans that are pulled into Datadog using tags. Only app service plans that match one of the defined tags are imported into Datadog.
automute
boolean
Silence monitors for expected Azure VM shutdowns.
client_id
string
Your Azure web application ID.
client_secret
string
Your Azure web application secret key.
container_app_filters
string
Limit the Azure container apps that are pulled into Datadog using tags. Only container apps that match one of the defined tags are imported into Datadog.
cspm_enabled
boolean
When enabled, Datadog’s Cloud Security Management product scans resource configurations monitored by this app registration. Note: This requires resource_collection_enabled to be set to true.
custom_metrics_enabled
boolean
Enable custom metrics for your organization.
errors
[string]
Errors in your configuration.
host_filters
string
Limit the Azure instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.
metrics_enabled
boolean
Enable Azure metrics for your organization.
metrics_enabled_default
boolean
Enable Azure metrics for your organization for resource providers where no resource provider config is specified.
new_client_id
string
Your New Azure web application ID.
new_tenant_name
string
Your New Azure Active Directory ID.
resource_collection_enabled
boolean
When enabled, Datadog collects metadata and configuration info from cloud resources (compute instances, databases, load balancers, etc.) monitored by this app registration.
resource_provider_configs
[object]
Configuration settings applied to resources from the specified Azure resource providers.
metrics_enabled
boolean
Collect metrics for resources from this provider.
namespace
string
The provider namespace to apply this configuration to.
tenant_name
string
Your Azure Active Directory ID.
usage_metrics_enabled
boolean
Enable azure.usage metrics for your organization.
```
{
  "app_service_plan_filters": "key:value,filter:example",
  "automute": true,
  "client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "client_secret": "TestingRh2nx664kUy5dIApvM54T4AtO",
  "container_app_filters": "key:value,filter:example",
  "cspm_enabled": true,
  "custom_metrics_enabled": true,
  "errors": [
    "*"
  ],
  "host_filters": "key:value,filter:example",
  "new_client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "new_tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "resource_collection_enabled": true,
  "tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/azure-integration/#CreateAzureIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/azure-integration/#CreateAzureIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/azure-integration/#CreateAzureIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/azure-integration/#CreateAzureIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby-legacy)


#####  Create an Azure integration returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/azure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "app_service_plan_filters": "key:value,filter:example",
  "automute": true,
  "client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "client_secret": "TestingRh2nx664kUy5dIApvM54T4AtO",
  "container_app_filters": "key:value,filter:example",
  "cspm_enabled": true,
  "custom_metrics_enabled": true,
  "errors": [
    "*"
  ],
  "host_filters": "key:value,filter:example",
  "new_client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "new_tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "resource_collection_enabled": true,
  "tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
}
EOF  

                        
```

#####  Create an Azure integration returns "OK" response
```
// Create an Azure integration returns "OK" response

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
	body := datadogV1.AzureAccount{
		AppServicePlanFilters: datadog.PtrString("key:value,filter:example"),
		Automute:              datadog.PtrBool(true),
		ClientId:              datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
		ClientSecret:          datadog.PtrString("TestingRh2nx664kUy5dIApvM54T4AtO"),
		ContainerAppFilters:   datadog.PtrString("key:value,filter:example"),
		CspmEnabled:           datadog.PtrBool(true),
		CustomMetricsEnabled:  datadog.PtrBool(true),
		Errors: []string{
			"*",
		},
		HostFilters:               datadog.PtrString("key:value,filter:example"),
		NewClientId:               datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
		NewTenantName:             datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
		ResourceCollectionEnabled: datadog.PtrBool(true),
		TenantName:                datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAzureIntegrationApi(apiClient)
	resp, r, err := api.CreateAzureIntegration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AzureIntegrationApi.CreateAzureIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AzureIntegrationApi.CreateAzureIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create an Azure integration returns "OK" response
```
// Create an Azure integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AzureIntegrationApi;
import com.datadog.api.client.v1.model.AzureAccount;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AzureIntegrationApi apiInstance = new AzureIntegrationApi(defaultClient);

    AzureAccount body =
        new AzureAccount()
            .appServicePlanFilters("key:value,filter:example")
            .automute(true)
            .clientId("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
            .clientSecret("TestingRh2nx664kUy5dIApvM54T4AtO")
            .containerAppFilters("key:value,filter:example")
            .cspmEnabled(true)
            .customMetricsEnabled(true)
            .errors(Collections.singletonList("*"))
            .hostFilters("key:value,filter:example")
            .newClientId("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
            .newTenantName("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
            .resourceCollectionEnabled(true)
            .tenantName("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d");

    try {
      apiInstance.createAzureIntegration(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AzureIntegrationApi#createAzureIntegration");
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

#####  Create an Azure integration returns "OK" response
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AzureIntegration.create(
    tenant_name="<AZURE_TENANT_NAME>",
    host_filters="<KEY_1>:<VALUE_1>,<KEY_2>:<VALUE_2>",
    client_id="<AZURE_CLIENT_ID>",
    client_secret="<AZURE_CLIENT_SECRET>"
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Create an Azure integration returns "OK" response
```
"""
Create an Azure integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount

body = AzureAccount(
    app_service_plan_filters="key:value,filter:example",
    automute=True,
    client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    client_secret="TestingRh2nx664kUy5dIApvM54T4AtO",
    container_app_filters="key:value,filter:example",
    cspm_enabled=True,
    custom_metrics_enabled=True,
    errors=[
        "*",
    ],
    host_filters="key:value,filter:example",
    new_client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    new_tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    resource_collection_enabled=True,
    tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.create_azure_integration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create an Azure integration returns "OK" response
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

config= {
    "tenant_name": "<AZURE_TENANT_NAME>",
    "client_id": "<AZURE_CLIENT_ID>",
    "client_secret": "<AZURE_CLIENT_SECRET>",
    "host_filters": "<KEY_1>:<VALUE_1>,<KEY_2>:<VALUE_2>"
  }

dog = Dogapi::Client.new(api_key, app_key)

dog.azure_integration_create(config)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an Azure integration returns "OK" response
```
# Create an Azure integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AzureIntegrationAPI.new

body = DatadogAPIClient::V1::AzureAccount.new({
  app_service_plan_filters: "key:value,filter:example",
  automute: true,
  client_id: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  client_secret: "TestingRh2nx664kUy5dIApvM54T4AtO",
  container_app_filters: "key:value,filter:example",
  cspm_enabled: true,
  custom_metrics_enabled: true,
  errors: [
    "*",
  ],
  host_filters: "key:value,filter:example",
  new_client_id: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  new_tenant_name: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  resource_collection_enabled: true,
  tenant_name: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
})
p api_instance.create_azure_integration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create an Azure integration returns "OK" response
```
// Create an Azure integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_azure_integration::AzureIntegrationAPI;
use datadog_api_client::datadogV1::model::AzureAccount;

#[tokio::main]
async fn main() {
    let body = AzureAccount::new()
        .app_service_plan_filters("key:value,filter:example".to_string())
        .automute(true)
        .client_id("".to_string())
        .client_secret("TestingRh2nx664kUy5dIApvM54T4AtO".to_string())
        .container_app_filters("key:value,filter:example".to_string())
        .cspm_enabled(true)
        .custom_metrics_enabled(true)
        .errors(vec!["*".to_string()])
        .host_filters("key:value,filter:example".to_string())
        .new_client_id("".to_string())
        .new_tenant_name("".to_string())
        .resource_collection_enabled(true)
        .tenant_name("".to_string());
    let configuration = datadog::Configuration::new();
    let api = AzureIntegrationAPI::with_config(configuration);
    let resp = api.create_azure_integration(body).await;
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

#####  Create an Azure integration returns "OK" response
```
/**
 * Create an Azure integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AzureIntegrationApi(configuration);

const params: v1.AzureIntegrationApiCreateAzureIntegrationRequest = {
  body: {
    appServicePlanFilters: "key:value,filter:example",
    automute: true,
    clientId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    clientSecret: "TestingRh2nx664kUy5dIApvM54T4AtO",
    containerAppFilters: "key:value,filter:example",
    cspmEnabled: true,
    customMetricsEnabled: true,
    errors: ["*"],
    hostFilters: "key:value,filter:example",
    newClientId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    newTenantName: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    resourceCollectionEnabled: true,
    tenantName: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  },
};

apiInstance
  .createAzureIntegration(params)
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
## [Delete an Azure integration](https://docs.datadoghq.com/api/latest/azure-integration/#delete-an-azure-integration)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/azure-integration/#delete-an-azure-integration-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/azurehttps://api.ap2.datadoghq.com/api/v1/integration/azurehttps://api.datadoghq.eu/api/v1/integration/azurehttps://api.ddog-gov.com/api/v1/integration/azurehttps://api.datadoghq.com/api/v1/integration/azurehttps://api.us3.datadoghq.com/api/v1/integration/azurehttps://api.us5.datadoghq.com/api/v1/integration/azure
### Overview
Delete a given Datadog-Azure integration from your Datadog account. This endpoint requires the `azure_configurations_manage` permission.
### Request
#### Body Data (required)
Delete a given Datadog-Azure integration request body.
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Field
Type
Description
app_service_plan_filters
string
Limit the Azure app service plans that are pulled into Datadog using tags. Only app service plans that match one of the defined tags are imported into Datadog.
automute
boolean
Silence monitors for expected Azure VM shutdowns.
client_id
string
Your Azure web application ID.
client_secret
string
Your Azure web application secret key.
container_app_filters
string
Limit the Azure container apps that are pulled into Datadog using tags. Only container apps that match one of the defined tags are imported into Datadog.
cspm_enabled
boolean
When enabled, Datadog’s Cloud Security Management product scans resource configurations monitored by this app registration. Note: This requires resource_collection_enabled to be set to true.
custom_metrics_enabled
boolean
Enable custom metrics for your organization.
errors
[string]
Errors in your configuration.
host_filters
string
Limit the Azure instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.
metrics_enabled
boolean
Enable Azure metrics for your organization.
metrics_enabled_default
boolean
Enable Azure metrics for your organization for resource providers where no resource provider config is specified.
new_client_id
string
Your New Azure web application ID.
new_tenant_name
string
Your New Azure Active Directory ID.
resource_collection_enabled
boolean
When enabled, Datadog collects metadata and configuration info from cloud resources (compute instances, databases, load balancers, etc.) monitored by this app registration.
resource_provider_configs
[object]
Configuration settings applied to resources from the specified Azure resource providers.
metrics_enabled
boolean
Collect metrics for resources from this provider.
namespace
string
The provider namespace to apply this configuration to.
tenant_name
string
Your Azure Active Directory ID.
usage_metrics_enabled
boolean
Enable azure.usage metrics for your organization.
```
{
  "client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/azure-integration/#DeleteAzureIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/azure-integration/#DeleteAzureIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/azure-integration/#DeleteAzureIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/azure-integration/#DeleteAzureIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby-legacy)


#####  Delete an Azure integration returns "OK" response
Copy
```
                          # Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/azure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
}
EOF  

                        
```

#####  Delete an Azure integration returns "OK" response
```
// Delete an Azure integration returns "OK" response

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
	body := datadogV1.AzureAccount{
		ClientId:   datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
		TenantName: datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAzureIntegrationApi(apiClient)
	resp, r, err := api.DeleteAzureIntegration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AzureIntegrationApi.DeleteAzureIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AzureIntegrationApi.DeleteAzureIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an Azure integration returns "OK" response
```
// Delete an Azure integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AzureIntegrationApi;
import com.datadog.api.client.v1.model.AzureAccount;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AzureIntegrationApi apiInstance = new AzureIntegrationApi(defaultClient);

    AzureAccount body =
        new AzureAccount()
            .clientId("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
            .tenantName("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d");

    try {
      apiInstance.deleteAzureIntegration(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AzureIntegrationApi#deleteAzureIntegration");
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

#####  Delete an Azure integration returns "OK" response
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AzureIntegration.delete(
    tenant_name="<AZURE_TENANT_NAME>",
    client_id="<AZURE_CLIENT_ID>"
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Delete an Azure integration returns "OK" response
```
"""
Delete an Azure integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount

body = AzureAccount(
    client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.delete_azure_integration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an Azure integration returns "OK" response
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
    "tenant_name": '<AZURE_TENANT_NAME>',
    "client_id": '<AZURE_CLIENT_ID>'
  }

dog.azure_integration_delete(config)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an Azure integration returns "OK" response
```
# Delete an Azure integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AzureIntegrationAPI.new

body = DatadogAPIClient::V1::AzureAccount.new({
  client_id: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  tenant_name: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
})
p api_instance.delete_azure_integration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an Azure integration returns "OK" response
```
// Delete an Azure integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_azure_integration::AzureIntegrationAPI;
use datadog_api_client::datadogV1::model::AzureAccount;

#[tokio::main]
async fn main() {
    let body = AzureAccount::new()
        .client_id("".to_string())
        .tenant_name("".to_string());
    let configuration = datadog::Configuration::new();
    let api = AzureIntegrationAPI::with_config(configuration);
    let resp = api.delete_azure_integration(body).await;
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

#####  Delete an Azure integration returns "OK" response
```
/**
 * Delete an Azure integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AzureIntegrationApi(configuration);

const params: v1.AzureIntegrationApiDeleteAzureIntegrationRequest = {
  body: {
    clientId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    tenantName: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  },
};

apiInstance
  .deleteAzureIntegration(params)
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
## [Update an Azure integration](https://docs.datadoghq.com/api/latest/azure-integration/#update-an-azure-integration)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/azure-integration/#update-an-azure-integration-v1)


PUT https://api.ap1.datadoghq.com/api/v1/integration/azurehttps://api.ap2.datadoghq.com/api/v1/integration/azurehttps://api.datadoghq.eu/api/v1/integration/azurehttps://api.ddog-gov.com/api/v1/integration/azurehttps://api.datadoghq.com/api/v1/integration/azurehttps://api.us3.datadoghq.com/api/v1/integration/azurehttps://api.us5.datadoghq.com/api/v1/integration/azure
### Overview
Update a Datadog-Azure integration. Requires an existing `tenant_name` and `client_id`. Any other fields supplied will overwrite existing values. To overwrite `tenant_name` or `client_id`, use `new_tenant_name` and `new_client_id`. To leave a field unchanged, do not supply that field in the payload. This endpoint requires the `azure_configuration_edit` permission.
### Request
#### Body Data (required)
Update a Datadog-Azure integration request body.
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Field
Type
Description
app_service_plan_filters
string
Limit the Azure app service plans that are pulled into Datadog using tags. Only app service plans that match one of the defined tags are imported into Datadog.
automute
boolean
Silence monitors for expected Azure VM shutdowns.
client_id
string
Your Azure web application ID.
client_secret
string
Your Azure web application secret key.
container_app_filters
string
Limit the Azure container apps that are pulled into Datadog using tags. Only container apps that match one of the defined tags are imported into Datadog.
cspm_enabled
boolean
When enabled, Datadog’s Cloud Security Management product scans resource configurations monitored by this app registration. Note: This requires resource_collection_enabled to be set to true.
custom_metrics_enabled
boolean
Enable custom metrics for your organization.
errors
[string]
Errors in your configuration.
host_filters
string
Limit the Azure instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.
metrics_enabled
boolean
Enable Azure metrics for your organization.
metrics_enabled_default
boolean
Enable Azure metrics for your organization for resource providers where no resource provider config is specified.
new_client_id
string
Your New Azure web application ID.
new_tenant_name
string
Your New Azure Active Directory ID.
resource_collection_enabled
boolean
When enabled, Datadog collects metadata and configuration info from cloud resources (compute instances, databases, load balancers, etc.) monitored by this app registration.
resource_provider_configs
[object]
Configuration settings applied to resources from the specified Azure resource providers.
metrics_enabled
boolean
Collect metrics for resources from this provider.
namespace
string
The provider namespace to apply this configuration to.
tenant_name
string
Your Azure Active Directory ID.
usage_metrics_enabled
boolean
Enable azure.usage metrics for your organization.
```
{
  "app_service_plan_filters": "key:value,filter:example",
  "automute": true,
  "client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "client_secret": "TestingRh2nx664kUy5dIApvM54T4AtO",
  "container_app_filters": "key:value,filter:example",
  "cspm_enabled": true,
  "custom_metrics_enabled": true,
  "errors": [
    "*"
  ],
  "host_filters": "key:value,filter:example",
  "new_client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "new_tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "resource_collection_enabled": true,
  "tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=typescript)


#####  Update an Azure integration returns "OK" response
Copy
```
                          # Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/azure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "app_service_plan_filters": "key:value,filter:example",
  "automute": true,
  "client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "client_secret": "TestingRh2nx664kUy5dIApvM54T4AtO",
  "container_app_filters": "key:value,filter:example",
  "cspm_enabled": true,
  "custom_metrics_enabled": true,
  "errors": [
    "*"
  ],
  "host_filters": "key:value,filter:example",
  "new_client_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "new_tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "resource_collection_enabled": true,
  "tenant_name": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
}
EOF  

                        
```

#####  Update an Azure integration returns "OK" response
```
// Update an Azure integration returns "OK" response

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
	body := datadogV1.AzureAccount{
		AppServicePlanFilters: datadog.PtrString("key:value,filter:example"),
		Automute:              datadog.PtrBool(true),
		ClientId:              datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
		ClientSecret:          datadog.PtrString("TestingRh2nx664kUy5dIApvM54T4AtO"),
		ContainerAppFilters:   datadog.PtrString("key:value,filter:example"),
		CspmEnabled:           datadog.PtrBool(true),
		CustomMetricsEnabled:  datadog.PtrBool(true),
		Errors: []string{
			"*",
		},
		HostFilters:               datadog.PtrString("key:value,filter:example"),
		NewClientId:               datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
		NewTenantName:             datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
		ResourceCollectionEnabled: datadog.PtrBool(true),
		TenantName:                datadog.PtrString("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAzureIntegrationApi(apiClient)
	resp, r, err := api.UpdateAzureIntegration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AzureIntegrationApi.UpdateAzureIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AzureIntegrationApi.UpdateAzureIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update an Azure integration returns "OK" response
```
// Update an Azure integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AzureIntegrationApi;
import com.datadog.api.client.v1.model.AzureAccount;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AzureIntegrationApi apiInstance = new AzureIntegrationApi(defaultClient);

    AzureAccount body =
        new AzureAccount()
            .appServicePlanFilters("key:value,filter:example")
            .automute(true)
            .clientId("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
            .clientSecret("TestingRh2nx664kUy5dIApvM54T4AtO")
            .containerAppFilters("key:value,filter:example")
            .cspmEnabled(true)
            .customMetricsEnabled(true)
            .errors(Collections.singletonList("*"))
            .hostFilters("key:value,filter:example")
            .newClientId("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
            .newTenantName("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
            .resourceCollectionEnabled(true)
            .tenantName("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d");

    try {
      apiInstance.updateAzureIntegration(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AzureIntegrationApi#updateAzureIntegration");
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

#####  Update an Azure integration returns "OK" response
```
"""
Update an Azure integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount

body = AzureAccount(
    app_service_plan_filters="key:value,filter:example",
    automute=True,
    client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    client_secret="TestingRh2nx664kUy5dIApvM54T4AtO",
    container_app_filters="key:value,filter:example",
    cspm_enabled=True,
    custom_metrics_enabled=True,
    errors=[
        "*",
    ],
    host_filters="key:value,filter:example",
    new_client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    new_tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    resource_collection_enabled=True,
    tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.update_azure_integration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update an Azure integration returns "OK" response
```
# Update an Azure integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AzureIntegrationAPI.new

body = DatadogAPIClient::V1::AzureAccount.new({
  app_service_plan_filters: "key:value,filter:example",
  automute: true,
  client_id: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  client_secret: "TestingRh2nx664kUy5dIApvM54T4AtO",
  container_app_filters: "key:value,filter:example",
  cspm_enabled: true,
  custom_metrics_enabled: true,
  errors: [
    "*",
  ],
  host_filters: "key:value,filter:example",
  new_client_id: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  new_tenant_name: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  resource_collection_enabled: true,
  tenant_name: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
})
p api_instance.update_azure_integration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update an Azure integration returns "OK" response
```
// Update an Azure integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_azure_integration::AzureIntegrationAPI;
use datadog_api_client::datadogV1::model::AzureAccount;

#[tokio::main]
async fn main() {
    let body = AzureAccount::new()
        .app_service_plan_filters("key:value,filter:example".to_string())
        .automute(true)
        .client_id("".to_string())
        .client_secret("TestingRh2nx664kUy5dIApvM54T4AtO".to_string())
        .container_app_filters("key:value,filter:example".to_string())
        .cspm_enabled(true)
        .custom_metrics_enabled(true)
        .errors(vec!["*".to_string()])
        .host_filters("key:value,filter:example".to_string())
        .new_client_id("".to_string())
        .new_tenant_name("".to_string())
        .resource_collection_enabled(true)
        .tenant_name("".to_string());
    let configuration = datadog::Configuration::new();
    let api = AzureIntegrationAPI::with_config(configuration);
    let resp = api.update_azure_integration(body).await;
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

#####  Update an Azure integration returns "OK" response
```
/**
 * Update an Azure integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AzureIntegrationApi(configuration);

const params: v1.AzureIntegrationApiUpdateAzureIntegrationRequest = {
  body: {
    appServicePlanFilters: "key:value,filter:example",
    automute: true,
    clientId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    clientSecret: "TestingRh2nx664kUy5dIApvM54T4AtO",
    containerAppFilters: "key:value,filter:example",
    cspmEnabled: true,
    customMetricsEnabled: true,
    errors: ["*"],
    hostFilters: "key:value,filter:example",
    newClientId: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    newTenantName: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    resourceCollectionEnabled: true,
    tenantName: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  },
};

apiInstance
  .updateAzureIntegration(params)
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
## [Update Azure integration host filters](https://docs.datadoghq.com/api/latest/azure-integration/#update-azure-integration-host-filters)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/azure-integration/#update-azure-integration-host-filters-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/azure/host_filtershttps://api.ap2.datadoghq.com/api/v1/integration/azure/host_filtershttps://api.datadoghq.eu/api/v1/integration/azure/host_filtershttps://api.ddog-gov.com/api/v1/integration/azure/host_filtershttps://api.datadoghq.com/api/v1/integration/azure/host_filtershttps://api.us3.datadoghq.com/api/v1/integration/azure/host_filtershttps://api.us5.datadoghq.com/api/v1/integration/azure/host_filters
### Overview
Update the defined list of host filters for a given Datadog-Azure integration. This endpoint requires the `azure_configuration_edit` permission.
### Request
#### Body Data (required)
Update a Datadog-Azure integration’s host filters request body.
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Field
Type
Description
app_service_plan_filters
string
Limit the Azure app service plans that are pulled into Datadog using tags. Only app service plans that match one of the defined tags are imported into Datadog.
automute
boolean
Silence monitors for expected Azure VM shutdowns.
client_id
string
Your Azure web application ID.
client_secret
string
Your Azure web application secret key.
container_app_filters
string
Limit the Azure container apps that are pulled into Datadog using tags. Only container apps that match one of the defined tags are imported into Datadog.
cspm_enabled
boolean
When enabled, Datadog’s Cloud Security Management product scans resource configurations monitored by this app registration. Note: This requires resource_collection_enabled to be set to true.
custom_metrics_enabled
boolean
Enable custom metrics for your organization.
errors
[string]
Errors in your configuration.
host_filters
string
Limit the Azure instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.
metrics_enabled
boolean
Enable Azure metrics for your organization.
metrics_enabled_default
boolean
Enable Azure metrics for your organization for resource providers where no resource provider config is specified.
new_client_id
string
Your New Azure web application ID.
new_tenant_name
string
Your New Azure Active Directory ID.
resource_collection_enabled
boolean
When enabled, Datadog collects metadata and configuration info from cloud resources (compute instances, databases, load balancers, etc.) monitored by this app registration.
resource_provider_configs
[object]
Configuration settings applied to resources from the specified Azure resource providers.
metrics_enabled
boolean
Collect metrics for resources from this provider.
namespace
string
The provider namespace to apply this configuration to.
tenant_name
string
Your Azure Active Directory ID.
usage_metrics_enabled
boolean
Enable azure.usage metrics for your organization.
```
{
  "app_service_plan_filters": "key:value,filter:example",
  "automute": true,
  "client_id": "testc7f6-1234-5678-9101-3fcbf464test",
  "client_secret": "TestingRh2nx664kUy5dIApvM54T4AtO",
  "container_app_filters": "key:value,filter:example",
  "cspm_enabled": true,
  "custom_metrics_enabled": true,
  "errors": [
    "*"
  ],
  "host_filters": "key:value,filter:example",
  "metrics_enabled": true,
  "metrics_enabled_default": true,
  "new_client_id": "new1c7f6-1234-5678-9101-3fcbf464test",
  "new_tenant_name": "new1c44-1234-5678-9101-cc00736ftest",
  "resource_collection_enabled": true,
  "resource_provider_configs": [
    {
      "metrics_enabled": true,
      "namespace": "Microsoft.Compute"
    }
  ],
  "tenant_name": "testc44-1234-5678-9101-cc00736ftest",
  "usage_metrics_enabled": true
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureHostFilters-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureHostFilters-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureHostFilters-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/azure-integration/#UpdateAzureHostFilters-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/azure-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/azure-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/azure-integration/?code-lang=python-legacy)


#####  Update Azure integration host filters
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/azure/host_filters" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Update Azure integration host filters
```
"""
Update Azure integration host filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount
from datadog_api_client.v1.model.resource_provider_config import ResourceProviderConfig

body = AzureAccount(
    app_service_plan_filters="key:value,filter:example",
    automute=True,
    client_id="testc7f6-1234-5678-9101-3fcbf464test",
    client_secret="TestingRh2nx664kUy5dIApvM54T4AtO",
    container_app_filters="key:value,filter:example",
    cspm_enabled=True,
    custom_metrics_enabled=True,
    errors=[
        "*",
    ],
    host_filters="key:value,filter:example",
    metrics_enabled=True,
    metrics_enabled_default=True,
    new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
    new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
    resource_collection_enabled=True,
    resource_provider_configs=[
        ResourceProviderConfig(
            metrics_enabled=True,
            namespace="Microsoft.Compute",
        ),
    ],
    tenant_name="testc44-1234-5678-9101-cc00736ftest",
    usage_metrics_enabled=True,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.update_azure_host_filters(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update Azure integration host filters
```
# Update Azure integration host filters returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AzureIntegrationAPI.new

body = DatadogAPIClient::V1::AzureAccount.new({
  app_service_plan_filters: "key:value,filter:example",
  automute: true,
  client_id: "testc7f6-1234-5678-9101-3fcbf464test",
  client_secret: "TestingRh2nx664kUy5dIApvM54T4AtO",
  container_app_filters: "key:value,filter:example",
  cspm_enabled: true,
  custom_metrics_enabled: true,
  errors: [
    "*",
  ],
  host_filters: "key:value,filter:example",
  metrics_enabled: true,
  metrics_enabled_default: true,
  new_client_id: "new1c7f6-1234-5678-9101-3fcbf464test",
  new_tenant_name: "new1c44-1234-5678-9101-cc00736ftest",
  resource_collection_enabled: true,
  resource_provider_configs: [
    DatadogAPIClient::V1::ResourceProviderConfig.new({
      metrics_enabled: true,
      namespace: "Microsoft.Compute",
    }),
  ],
  tenant_name: "testc44-1234-5678-9101-cc00736ftest",
  usage_metrics_enabled: true,
})
p api_instance.update_azure_host_filters(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update Azure integration host filters
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

config= {
    "tenant_name": "<AZURE_TENANT_NAME>",
    "client_id": "<AZURE_CLIENT_ID>",
    "host_filters": "<NEW_KEY>:<NEW_VALUE>"
  }

dog = Dogapi::Client.new(api_key, app_key)

dog.azure_integration_update_host_filters(config)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update Azure integration host filters
```
// Update Azure integration host filters returns "OK" response

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
	body := datadogV1.AzureAccount{
		AppServicePlanFilters: datadog.PtrString("key:value,filter:example"),
		Automute:              datadog.PtrBool(true),
		ClientId:              datadog.PtrString("testc7f6-1234-5678-9101-3fcbf464test"),
		ClientSecret:          datadog.PtrString("TestingRh2nx664kUy5dIApvM54T4AtO"),
		ContainerAppFilters:   datadog.PtrString("key:value,filter:example"),
		CspmEnabled:           datadog.PtrBool(true),
		CustomMetricsEnabled:  datadog.PtrBool(true),
		Errors: []string{
			"*",
		},
		HostFilters:               datadog.PtrString("key:value,filter:example"),
		MetricsEnabled:            datadog.PtrBool(true),
		MetricsEnabledDefault:     datadog.PtrBool(true),
		NewClientId:               datadog.PtrString("new1c7f6-1234-5678-9101-3fcbf464test"),
		NewTenantName:             datadog.PtrString("new1c44-1234-5678-9101-cc00736ftest"),
		ResourceCollectionEnabled: datadog.PtrBool(true),
		ResourceProviderConfigs: []datadogV1.ResourceProviderConfig{
			{
				MetricsEnabled: datadog.PtrBool(true),
				Namespace:      datadog.PtrString("Microsoft.Compute"),
			},
		},
		TenantName:          datadog.PtrString("testc44-1234-5678-9101-cc00736ftest"),
		UsageMetricsEnabled: datadog.PtrBool(true),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAzureIntegrationApi(apiClient)
	resp, r, err := api.UpdateAzureHostFilters(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AzureIntegrationApi.UpdateAzureHostFilters`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AzureIntegrationApi.UpdateAzureHostFilters`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update Azure integration host filters
```
// Update Azure integration host filters returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AzureIntegrationApi;
import com.datadog.api.client.v1.model.AzureAccount;
import com.datadog.api.client.v1.model.ResourceProviderConfig;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AzureIntegrationApi apiInstance = new AzureIntegrationApi(defaultClient);

    AzureAccount body =
        new AzureAccount()
            .appServicePlanFilters("key:value,filter:example")
            .automute(true)
            .clientId("testc7f6-1234-5678-9101-3fcbf464test")
            .clientSecret("TestingRh2nx664kUy5dIApvM54T4AtO")
            .containerAppFilters("key:value,filter:example")
            .cspmEnabled(true)
            .customMetricsEnabled(true)
            .errors(Collections.singletonList("*"))
            .hostFilters("key:value,filter:example")
            .metricsEnabled(true)
            .metricsEnabledDefault(true)
            .newClientId("new1c7f6-1234-5678-9101-3fcbf464test")
            .newTenantName("new1c44-1234-5678-9101-cc00736ftest")
            .resourceCollectionEnabled(true)
            .resourceProviderConfigs(
                Collections.singletonList(
                    new ResourceProviderConfig()
                        .metricsEnabled(true)
                        .namespace("Microsoft.Compute")))
            .tenantName("testc44-1234-5678-9101-cc00736ftest")
            .usageMetricsEnabled(true);

    try {
      apiInstance.updateAzureHostFilters(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AzureIntegrationApi#updateAzureHostFilters");
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

#####  Update Azure integration host filters
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AzureIntegration.update_host_filters(
    tenant_name="<AZURE_TENANT_NAME>",
    host_filters="new:filters",
    client_id="<AZURE_CLIENT_ID>"
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Update Azure integration host filters
```
// Update Azure integration host filters returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_azure_integration::AzureIntegrationAPI;
use datadog_api_client::datadogV1::model::AzureAccount;
use datadog_api_client::datadogV1::model::ResourceProviderConfig;

#[tokio::main]
async fn main() {
    let body = AzureAccount::new()
        .app_service_plan_filters("key:value,filter:example".to_string())
        .automute(true)
        .client_id("testc7f6-1234-5678-9101-3fcbf464test".to_string())
        .client_secret("TestingRh2nx664kUy5dIApvM54T4AtO".to_string())
        .container_app_filters("key:value,filter:example".to_string())
        .cspm_enabled(true)
        .custom_metrics_enabled(true)
        .errors(vec!["*".to_string()])
        .host_filters("key:value,filter:example".to_string())
        .metrics_enabled(true)
        .metrics_enabled_default(true)
        .new_client_id("new1c7f6-1234-5678-9101-3fcbf464test".to_string())
        .new_tenant_name("new1c44-1234-5678-9101-cc00736ftest".to_string())
        .resource_collection_enabled(true)
        .resource_provider_configs(vec![ResourceProviderConfig::new()
            .metrics_enabled(true)
            .namespace("Microsoft.Compute".to_string())])
        .tenant_name("testc44-1234-5678-9101-cc00736ftest".to_string())
        .usage_metrics_enabled(true);
    let configuration = datadog::Configuration::new();
    let api = AzureIntegrationAPI::with_config(configuration);
    let resp = api.update_azure_host_filters(body).await;
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

#####  Update Azure integration host filters
```
/**
 * Update Azure integration host filters returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AzureIntegrationApi(configuration);

const params: v1.AzureIntegrationApiUpdateAzureHostFiltersRequest = {
  body: {
    appServicePlanFilters: "key:value,filter:example",
    automute: true,
    clientId: "testc7f6-1234-5678-9101-3fcbf464test",
    clientSecret: "TestingRh2nx664kUy5dIApvM54T4AtO",
    containerAppFilters: "key:value,filter:example",
    cspmEnabled: true,
    customMetricsEnabled: true,
    errors: ["*"],
    hostFilters: "key:value,filter:example",
    metricsEnabled: true,
    metricsEnabledDefault: true,
    newClientId: "new1c7f6-1234-5678-9101-3fcbf464test",
    newTenantName: "new1c44-1234-5678-9101-cc00736ftest",
    resourceCollectionEnabled: true,
    resourceProviderConfigs: [
      {
        metricsEnabled: true,
        namespace: "Microsoft.Compute",
      },
    ],
    tenantName: "testc44-1234-5678-9101-cc00736ftest",
    usageMetricsEnabled: true,
  },
};

apiInstance
  .updateAzureHostFilters(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e60261d0-a2ca-498b-8dc4-58f4f0392a3d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d39c3104-3d49-4c22-b0bf-39a455fdcacc&pt=Azure%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fazure-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e60261d0-a2ca-498b-8dc4-58f4f0392a3d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d39c3104-3d49-4c22-b0bf-39a455fdcacc&pt=Azure%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fazure-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=4448af69-a3cf-4f18-a4b0-e2164dc231b9&bo=2&sid=2b97e1f0f0bf11f0a95ed35e5ee0944a&vid=2b983270f0bf11f0b99eb30165f83ff9&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Azure%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fazure-integration%2F&r=&lt=1518&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=465664)
