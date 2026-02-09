# Source: https://docs.datadoghq.com/api/latest/gcp-integration/

# GCP Integration
Configure your Datadog-Google Cloud Platform (GCP) integration directly through the Datadog API. Read more about the [Datadog-Google Cloud Platform integration](https://docs.datadoghq.com/integrations/google_cloud_platform).
## [List all GCP integrations](https://docs.datadoghq.com/api/latest/gcp-integration/#list-all-gcp-integrations)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/gcp-integration/#list-all-gcp-integrations-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/gcphttps://api.ap2.datadoghq.com/api/v1/integration/gcphttps://api.datadoghq.eu/api/v1/integration/gcphttps://api.ddog-gov.com/api/v1/integration/gcphttps://api.datadoghq.com/api/v1/integration/gcphttps://api.us3.datadoghq.com/api/v1/integration/gcphttps://api.us5.datadoghq.com/api/v1/integration/gcp
### Overview
This endpoint is deprecated – use the V2 endpoints instead. List all Datadog-GCP integrations configured in your Datadog account. This endpoint requires the `gcp_configuration_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Array of GCP account responses.
Field
Type
Description
auth_provider_x509_cert_url
string
Should be `https://www.googleapis.com/oauth2/v1/certs`.
auth_uri
string
Should be `https://accounts.google.com/o/oauth2/auth`.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your email found in your JSON service account key.
client_id
string
Your ID found in your JSON service account key.
client_x509_cert_url
string
Should be `https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL` where `$CLIENT_EMAIL` is the email found in your JSON service account key.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
errors
[string]
An array of errors.
host_filters
string
**DEPRECATED** : A comma-separated list of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
private_key
string
Your private key name found in your JSON service account key.
private_key_id
string
Your private key ID found in your JSON service account key.
project_id
string
Your Google Cloud project ID found in your JSON service account key.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
token_uri
string
Should be `https://accounts.google.com/o/oauth2/token`.
type
string
The value for service_account found in your JSON service account key.
```
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "automute": false,
  "client_email": "api-dev@datadog-sandbox.iam.gserviceaccount.com",
  "client_id": "123456712345671234567",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  "cloud_run_revision_filters": [
    "$KEY:$VALUE"
  ],
  "errors": [
    "*"
  ],
  "host_filters": "$KEY1:$VALUE1,$KEY2:$VALUE2",
  "is_cspm_enabled": true,
  "is_resource_change_collection_enabled": true,
  "is_security_command_center_enabled": true,
  "monitored_resource_configs": [
    {
      "filters": [
        "$KEY:$VALUE"
      ],
      "type": "gce_instance"
    }
  ],
  "private_key": "private_key",
  "private_key_id": "123456789abcdefghi123456789abcdefghijklm",
  "project_id": "datadog-apitest",
  "resource_collection_enabled": true,
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "type": "service_account"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python-legacy)


#####  List all GCP integrations
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/gcp" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all GCP integrations
```
"""
List all GCP integrations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.list_gcp_integration()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List all GCP integrations
```
# List all GCP integrations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::GCPIntegrationAPI.new
p api_instance.list_gcp_integration()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all GCP integrations
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.gcp_integration_list

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all GCP integrations
```
// List all GCP integrations returns "OK" response

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
	api := datadogV1.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.ListGCPIntegration(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.ListGCPIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.ListGCPIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List all GCP integrations
```
// List all GCP integrations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.GcpIntegrationApi;
import com.datadog.api.client.v1.model.GCPAccount;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    try {
      List<GCPAccount> result = apiInstance.listGCPIntegration();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#listGCPIntegration");
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

#####  List all GCP integrations
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.GcpIntegration.list()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  List all GCP integrations
```
// List all GCP integrations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_gcp_integration::GCPIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.list_gcp_integration().await;
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

#####  List all GCP integrations
```
/**
 * List all GCP integrations returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.GCPIntegrationApi(configuration);

apiInstance
  .listGCPIntegration()
  .then((data: v1.GCPAccount[]) => {
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
## [List all GCP STS-enabled service accounts](https://docs.datadoghq.com/api/latest/gcp-integration/#list-all-gcp-sts-enabled-service-accounts)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/gcp-integration/#list-all-gcp-sts-enabled-service-accounts-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/gcp/accountshttps://api.ap2.datadoghq.com/api/v2/integration/gcp/accountshttps://api.datadoghq.eu/api/v2/integration/gcp/accountshttps://api.ddog-gov.com/api/v2/integration/gcp/accountshttps://api.datadoghq.com/api/v2/integration/gcp/accountshttps://api.us3.datadoghq.com/api/v2/integration/gcp/accountshttps://api.us5.datadoghq.com/api/v2/integration/gcp/accounts
### Overview
List all GCP STS-enabled service accounts configured in your Datadog account. This endpoint requires the `gcp_configuration_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPSTSAccounts-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPSTSAccounts-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPSTSAccounts-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#ListGCPSTSAccounts-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Object containing all your STS enabled accounts.
Field
Type
Description
data
[object]
Array of GCP STS enabled service accounts.
attributes
object
Attributes associated with your service account.
account_tags
[string]
Tags to be associated with GCP metrics and service checks from your account.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your service account email address.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
host_filters
[string]
**DEPRECATED** : List of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_global_location_enabled
boolean
When enabled, Datadog collects metrics where location is explicitly stated as "global" or where location information cannot be deduced from GCP labels.
default: `true`
is_per_project_quota_enabled
boolean
When enabled, Datadog applies the `X-Goog-User-Project` header, attributing Google Cloud billing and quota usage to the project being monitored rather than the default service account project.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
metric_namespace_configs
[object]
Configurations for GCP metric namespaces.
disabled
boolean
When disabled, Datadog does not collect metrics that are related to this GCP metric namespace.
filters
[string]
When enabled, Datadog applies these additional filters to limit metric collection. A metric is collected only if it does not match all exclusion filters and matches at least one allow filter.
id
string
The id of the GCP metric namespace.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
region_filter_configs
[string]
Configurations for GCP location filtering, such as region, multi-region, or zone. Only monitored resources that match the specified regions are imported into Datadog. By default, Datadog collects from all locations.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
id
string
Your service account's unique ID.
meta
object
Additional information related to your service account.
accessible_projects
[string]
The current list of projects accessible from your service account.
type
enum
The type of account. Allowed enum values: `gcp_service_account`
default: `gcp_service_account`
```
{
  "data": [
    {
      "attributes": {
        "account_tags": [],
        "automute": false,
        "client_email": "datadog-service-account@test-project.iam.gserviceaccount.com",
        "cloud_run_revision_filters": [
          "$KEY:$VALUE"
        ],
        "host_filters": [
          "$KEY:$VALUE"
        ],
        "is_cspm_enabled": false,
        "is_global_location_enabled": true,
        "is_per_project_quota_enabled": true,
        "is_resource_change_collection_enabled": true,
        "is_security_command_center_enabled": true,
        "metric_namespace_configs": [
          {
            "disabled": true,
            "filters": [
              "snapshot.*",
              "!*_by_region"
            ],
            "id": "pubsub"
          }
        ],
        "monitored_resource_configs": [
          {
            "filters": [
              "$KEY:$VALUE"
            ],
            "type": "gce_instance"
          }
        ],
        "region_filter_configs": [
          "nam4",
          "europe-north1"
        ],
        "resource_collection_enabled": false
      },
      "id": "d291291f-12c2-22g4-j290-123456678897",
      "meta": {
        "accessible_projects": []
      },
      "type": "gcp_service_account"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)


#####  List all GCP STS-enabled service accounts
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all GCP STS-enabled service accounts
```
"""
List all GCP STS-enabled service accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.list_gcpsts_accounts()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List all GCP STS-enabled service accounts
```
# List all GCP STS-enabled service accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new
p api_instance.list_gcpsts_accounts()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List all GCP STS-enabled service accounts
```
// List all GCP STS-enabled service accounts returns "OK" response

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
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.ListGCPSTSAccounts(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.ListGCPSTSAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.ListGCPSTSAccounts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List all GCP STS-enabled service accounts
```
// List all GCP STS-enabled service accounts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    try {
      GCPSTSServiceAccountsResponse result = apiInstance.listGCPSTSAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#listGCPSTSAccounts");
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

#####  List all GCP STS-enabled service accounts
```
// List all GCP STS-enabled service accounts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.list_gcpsts_accounts().await;
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

#####  List all GCP STS-enabled service accounts
```
/**
 * List all GCP STS-enabled service accounts returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

apiInstance
  .listGCPSTSAccounts()
  .then((data: v2.GCPSTSServiceAccountsResponse) => {
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
## [Create a GCP integration](https://docs.datadoghq.com/api/latest/gcp-integration/#create-a-gcp-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/gcp-integration/#create-a-gcp-integration-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/gcphttps://api.ap2.datadoghq.com/api/v1/integration/gcphttps://api.datadoghq.eu/api/v1/integration/gcphttps://api.ddog-gov.com/api/v1/integration/gcphttps://api.datadoghq.com/api/v1/integration/gcphttps://api.us3.datadoghq.com/api/v1/integration/gcphttps://api.us5.datadoghq.com/api/v1/integration/gcp
### Overview
This endpoint is deprecated – use the V2 endpoints instead. Create a Datadog-GCP integration. This endpoint requires the `gcp_configurations_manage` permission.
### Request
#### Body Data (required)
Create a Datadog-GCP integration.
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Field
Type
Description
auth_provider_x509_cert_url
string
Should be `https://www.googleapis.com/oauth2/v1/certs`.
auth_uri
string
Should be `https://accounts.google.com/o/oauth2/auth`.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your email found in your JSON service account key.
client_id
string
Your ID found in your JSON service account key.
client_x509_cert_url
string
Should be `https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL` where `$CLIENT_EMAIL` is the email found in your JSON service account key.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
errors
[string]
An array of errors.
host_filters
string
**DEPRECATED** : A comma-separated list of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
private_key
string
Your private key name found in your JSON service account key.
private_key_id
string
Your private key ID found in your JSON service account key.
project_id
string
Your Google Cloud project ID found in your JSON service account key.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
token_uri
string
Should be `https://accounts.google.com/o/oauth2/token`.
type
string
The value for service_account found in your JSON service account key.
```
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  "host_filters": "key:value,filter:example",
  "cloud_run_revision_filters": [
    "dr:dre"
  ],
  "is_cspm_enabled": true,
  "is_security_command_center_enabled": true,
  "is_resource_change_collection_enabled": true,
  "private_key": "private_key",
  "private_key_id": "123456789abcdefghi123456789abcdefghijklm",
  "project_id": "datadog-apitest",
  "resource_collection_enabled": true,
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "type": "service_account"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby-legacy)


#####  Create a GCP integration returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/gcp" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  "host_filters": "key:value,filter:example",
  "cloud_run_revision_filters": [
    "dr:dre"
  ],
  "is_cspm_enabled": true,
  "is_security_command_center_enabled": true,
  "is_resource_change_collection_enabled": true,
  "private_key": "private_key",
  "private_key_id": "123456789abcdefghi123456789abcdefghijklm",
  "project_id": "datadog-apitest",
  "resource_collection_enabled": true,
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "type": "service_account"
}
EOF  

                        
```

#####  Create a GCP integration returns "OK" response
```
// Create a GCP integration returns "OK" response

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
	body := datadogV1.GCPAccount{
		AuthProviderX509CertUrl: datadog.PtrString("https://www.googleapis.com/oauth2/v1/certs"),
		AuthUri:                 datadog.PtrString("https://accounts.google.com/o/oauth2/auth"),
		ClientEmail:             datadog.PtrString("252bf553ef04b351@example.com"),
		ClientId:                datadog.PtrString("163662907116366290710"),
		ClientX509CertUrl:       datadog.PtrString("https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL"),
		HostFilters:             datadog.PtrString("key:value,filter:example"),
		CloudRunRevisionFilters: []string{
			"dr:dre",
		},
		IsCspmEnabled:                     datadog.PtrBool(true),
		IsSecurityCommandCenterEnabled:    datadog.PtrBool(true),
		IsResourceChangeCollectionEnabled: datadog.PtrBool(true),
		PrivateKey:                        datadog.PtrString("private_key"),
		PrivateKeyId:                      datadog.PtrString("123456789abcdefghi123456789abcdefghijklm"),
		ProjectId:                         datadog.PtrString("datadog-apitest"),
		ResourceCollectionEnabled:         datadog.PtrBool(true),
		TokenUri:                          datadog.PtrString("https://accounts.google.com/o/oauth2/token"),
		Type:                              datadog.PtrString("service_account"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.CreateGCPIntegration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.CreateGCPIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.CreateGCPIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a GCP integration returns "OK" response
```
// Create a GCP integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.GcpIntegrationApi;
import com.datadog.api.client.v1.model.GCPAccount;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    GCPAccount body =
        new GCPAccount()
            .authProviderX509CertUrl("https://www.googleapis.com/oauth2/v1/certs")
            .authUri("https://accounts.google.com/o/oauth2/auth")
            .clientEmail("252bf553ef04b351@example.com")
            .clientId("163662907116366290710")
            .clientX509CertUrl("https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL")
            .hostFilters("key:value,filter:example")
            .cloudRunRevisionFilters(Collections.singletonList("dr:dre"))
            .isCspmEnabled(true)
            .isSecurityCommandCenterEnabled(true)
            .isResourceChangeCollectionEnabled(true)
            .privateKey("private_key")
            .privateKeyId("123456789abcdefghi123456789abcdefghijklm")
            .projectId("datadog-apitest")
            .resourceCollectionEnabled(true)
            .tokenUri("https://accounts.google.com/o/oauth2/token")
            .type("service_account");

    try {
      apiInstance.createGCPIntegration(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#createGCPIntegration");
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

#####  Create a GCP integration returns "OK" response
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.GcpIntegration.create(
    type="service_account",
    project_id="<GCP_PROJECT_ID>",
    private_key_id="<GCP_PRIVATE_KEY_ID>",
    private_key="<GCP_PRIVATE_KEY>",
    client_email="<GCP_CLIENT_EMAIL>",
    client_id="<GCP_CLIENT_ID>",
    auth_uri="<GCP_AUTH_URI>",
    token_uri="<GCP_TOKEN_URI>",
    auth_provider_x509_cert_url="<GCP_AUTH_PROVIDER_X509_CERT_URL>",
    client_x509_cert_url="<GCP_CLIENT_X509_CERT_URL>",
    host_filters="<KEY>:<VALUE>,<KEY>:<VALUE>"
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Create a GCP integration returns "OK" response
```
"""
Create a GCP integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v1.model.gcp_account import GCPAccount

body = GCPAccount(
    auth_provider_x509_cert_url="https://www.googleapis.com/oauth2/v1/certs",
    auth_uri="https://accounts.google.com/o/oauth2/auth",
    client_email="252bf553ef04b351@example.com",
    client_id="163662907116366290710",
    client_x509_cert_url="https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
    host_filters="key:value,filter:example",
    cloud_run_revision_filters=[
        "dr:dre",
    ],
    is_cspm_enabled=True,
    is_security_command_center_enabled=True,
    is_resource_change_collection_enabled=True,
    private_key="private_key",
    private_key_id="123456789abcdefghi123456789abcdefghijklm",
    project_id="datadog-apitest",
    resource_collection_enabled=True,
    token_uri="https://accounts.google.com/o/oauth2/token",
    type="service_account",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcp_integration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a GCP integration returns "OK" response
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

config= {
    "type": "service_account",
    "project_id": "<GCP_PROJECT_ID>",
    "private_key_id": "<PRIVATE_KEY_ID>",
    "private_key": "<PRIVATE_KEY>",
    "client_email": "<CLIENT_EMAIL>",
    "client_id": "<CLIENT_ID>",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/<CLIENT_EMAIL>",
    "host_filters": "<KEY_1>:<VALUE_1>,<KEY_2>:<VALUE_2>"
  }

dog = Dogapi::Client.new(api_key, app_key)

dog.gcp_integration_create(config)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a GCP integration returns "OK" response
```
# Create a GCP integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::GCPIntegrationAPI.new

body = DatadogAPIClient::V1::GCPAccount.new({
  auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
  auth_uri: "https://accounts.google.com/o/oauth2/auth",
  client_email: "252bf553ef04b351@example.com",
  client_id: "163662907116366290710",
  client_x509_cert_url: "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  host_filters: "key:value,filter:example",
  cloud_run_revision_filters: [
    "dr:dre",
  ],
  is_cspm_enabled: true,
  is_security_command_center_enabled: true,
  is_resource_change_collection_enabled: true,
  private_key: "private_key",
  private_key_id: "123456789abcdefghi123456789abcdefghijklm",
  project_id: "datadog-apitest",
  resource_collection_enabled: true,
  token_uri: "https://accounts.google.com/o/oauth2/token",
  type: "service_account",
})
p api_instance.create_gcp_integration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a GCP integration returns "OK" response
```
// Create a GCP integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV1::model::GCPAccount;

#[tokio::main]
async fn main() {
    let body = GCPAccount::new()
        .auth_provider_x509_cert_url("https://www.googleapis.com/oauth2/v1/certs".to_string())
        .auth_uri("https://accounts.google.com/o/oauth2/auth".to_string())
        .client_email("252bf553ef04b351@example.com".to_string())
        .client_id("163662907116366290710".to_string())
        .client_x509_cert_url(
            "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL".to_string(),
        )
        .cloud_run_revision_filters(vec!["dr:dre".to_string()])
        .host_filters("key:value,filter:example".to_string())
        .is_cspm_enabled(true)
        .is_resource_change_collection_enabled(true)
        .is_security_command_center_enabled(true)
        .private_key("private_key".to_string())
        .private_key_id("123456789abcdefghi123456789abcdefghijklm".to_string())
        .project_id("datadog-apitest".to_string())
        .resource_collection_enabled(true)
        .token_uri("https://accounts.google.com/o/oauth2/token".to_string())
        .type_("service_account".to_string());
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.create_gcp_integration(body).await;
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

#####  Create a GCP integration returns "OK" response
```
/**
 * Create a GCP integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.GCPIntegrationApi(configuration);

const params: v1.GCPIntegrationApiCreateGCPIntegrationRequest = {
  body: {
    authProviderX509CertUrl: "https://www.googleapis.com/oauth2/v1/certs",
    authUri: "https://accounts.google.com/o/oauth2/auth",
    clientEmail: "252bf553ef04b351@example.com",
    clientId: "163662907116366290710",
    clientX509CertUrl:
      "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
    hostFilters: "key:value,filter:example",
    cloudRunRevisionFilters: ["dr:dre"],
    isCspmEnabled: true,
    isSecurityCommandCenterEnabled: true,
    isResourceChangeCollectionEnabled: true,
    privateKey: "private_key",
    privateKeyId: "123456789abcdefghi123456789abcdefghijklm",
    projectId: "datadog-apitest",
    resourceCollectionEnabled: true,
    tokenUri: "https://accounts.google.com/o/oauth2/token",
    type: "service_account",
  },
};

apiInstance
  .createGCPIntegration(params)
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
## [Create a new entry for your service account](https://docs.datadoghq.com/api/latest/gcp-integration/#create-a-new-entry-for-your-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/gcp-integration/#create-a-new-entry-for-your-service-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/integration/gcp/accountshttps://api.ap2.datadoghq.com/api/v2/integration/gcp/accountshttps://api.datadoghq.eu/api/v2/integration/gcp/accountshttps://api.ddog-gov.com/api/v2/integration/gcp/accountshttps://api.datadoghq.com/api/v2/integration/gcp/accountshttps://api.us3.datadoghq.com/api/v2/integration/gcp/accountshttps://api.us5.datadoghq.com/api/v2/integration/gcp/accounts
### Overview
Create a new entry within Datadog for your STS enabled service account. This endpoint requires the `gcp_configurations_manage` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Field
Type
Description
data
object
Additional metadata on your generated service account.
attributes
object
Attributes associated with your service account.
account_tags
[string]
Tags to be associated with GCP metrics and service checks from your account.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your service account email address.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
host_filters
[string]
**DEPRECATED** : List of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_global_location_enabled
boolean
When enabled, Datadog collects metrics where location is explicitly stated as "global" or where location information cannot be deduced from GCP labels.
default: `true`
is_per_project_quota_enabled
boolean
When enabled, Datadog applies the `X-Goog-User-Project` header, attributing Google Cloud billing and quota usage to the project being monitored rather than the default service account project.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
metric_namespace_configs
[object]
Configurations for GCP metric namespaces.
disabled
boolean
When disabled, Datadog does not collect metrics that are related to this GCP metric namespace.
filters
[string]
When enabled, Datadog applies these additional filters to limit metric collection. A metric is collected only if it does not match all exclusion filters and matches at least one allow filter.
id
string
The id of the GCP metric namespace.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
region_filter_configs
[string]
Configurations for GCP location filtering, such as region, multi-region, or zone. Only monitored resources that match the specified regions are imported into Datadog. By default, Datadog collects from all locations.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
type
enum
The type of account. Allowed enum values: `gcp_service_account`
default: `gcp_service_account`
#####  Create a new entry for your service account returns "OK" response
```
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      "host_filters": []
    },
    "type": "gcp_service_account"
  }
}
```

Copy
#####  Create a new entry for your service account with account_tags returns "OK" response
```
{
  "data": {
    "attributes": {
      "account_tags": [
        "lorem",
        "ipsum"
      ],
      "client_email": "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      "host_filters": []
    },
    "type": "gcp_service_account"
  }
}
```

Copy
#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response
```
{
  "data": {
    "attributes": {
      "cloud_run_revision_filters": [
        "meh:bleh"
      ],
      "client_email": "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      "host_filters": []
    },
    "type": "gcp_service_account"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPSTSAccount-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPSTSAccount-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPSTSAccount-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPSTSAccount-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPSTSAccount-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#CreateGCPSTSAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


The account creation response.
Field
Type
Description
data
object
Info on your service account.
attributes
object
Attributes associated with your service account.
account_tags
[string]
Tags to be associated with GCP metrics and service checks from your account.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your service account email address.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
host_filters
[string]
**DEPRECATED** : List of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_global_location_enabled
boolean
When enabled, Datadog collects metrics where location is explicitly stated as "global" or where location information cannot be deduced from GCP labels.
default: `true`
is_per_project_quota_enabled
boolean
When enabled, Datadog applies the `X-Goog-User-Project` header, attributing Google Cloud billing and quota usage to the project being monitored rather than the default service account project.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
metric_namespace_configs
[object]
Configurations for GCP metric namespaces.
disabled
boolean
When disabled, Datadog does not collect metrics that are related to this GCP metric namespace.
filters
[string]
When enabled, Datadog applies these additional filters to limit metric collection. A metric is collected only if it does not match all exclusion filters and matches at least one allow filter.
id
string
The id of the GCP metric namespace.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
region_filter_configs
[string]
Configurations for GCP location filtering, such as region, multi-region, or zone. Only monitored resources that match the specified regions are imported into Datadog. By default, Datadog collects from all locations.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
id
string
Your service account's unique ID.
meta
object
Additional information related to your service account.
accessible_projects
[string]
The current list of projects accessible from your service account.
type
enum
The type of account. Allowed enum values: `gcp_service_account`
default: `gcp_service_account`
```
{
  "data": {
    "attributes": {
      "account_tags": [],
      "automute": false,
      "client_email": "datadog-service-account@test-project.iam.gserviceaccount.com",
      "cloud_run_revision_filters": [
        "$KEY:$VALUE"
      ],
      "host_filters": [
        "$KEY:$VALUE"
      ],
      "is_cspm_enabled": false,
      "is_global_location_enabled": true,
      "is_per_project_quota_enabled": true,
      "is_resource_change_collection_enabled": true,
      "is_security_command_center_enabled": true,
      "metric_namespace_configs": [
        {
          "disabled": true,
          "filters": [
            "snapshot.*",
            "!*_by_region"
          ],
          "id": "pubsub"
        }
      ],
      "monitored_resource_configs": [
        {
          "filters": [
            "$KEY:$VALUE"
          ],
          "type": "gce_instance"
        }
      ],
      "region_filter_configs": [
        "nam4",
        "europe-north1"
      ],
      "resource_collection_enabled": false
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "meta": {
      "accessible_projects": []
    },
    "type": "gcp_service_account"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)


#####  Create a new entry for your service account returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      "host_filters": []
    },
    "type": "gcp_service_account"
  }
}
EOF  

                        
```

#####  Create a new entry for your service account with account_tags returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_tags": [
        "lorem",
        "ipsum"
      ],
      "client_email": "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      "host_filters": []
    },
    "type": "gcp_service_account"
  }
}
EOF  

                        
```

#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "cloud_run_revision_filters": [
        "meh:bleh"
      ],
      "client_email": "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      "host_filters": []
    },
    "type": "gcp_service_account"
  }
}
EOF  

                        
```

#####  Create a new entry for your service account returns "OK" response 
```
// Create a new entry for your service account returns "OK" response

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
	body := datadogV2.GCPSTSServiceAccountCreateRequest{
		Data: &datadogV2.GCPSTSServiceAccountData{
			Attributes: &datadogV2.GCPSTSServiceAccountAttributes{
				ClientEmail: datadog.PtrString("Test-252bf553ef04b351@test-project.iam.gserviceaccount.com"),
				HostFilters: []string{},
			},
			Type: datadogV2.GCPSERVICEACCOUNTTYPE_GCP_SERVICE_ACCOUNT.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.CreateGCPSTSAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.CreateGCPSTSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.CreateGCPSTSAccount`:\n%s\n", responseContent)
}

```

Copy
#####  Create a new entry for your service account with account_tags returns "OK" response 
```
// Create a new entry for your service account with account_tags returns "OK" response

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
	body := datadogV2.GCPSTSServiceAccountCreateRequest{
		Data: &datadogV2.GCPSTSServiceAccountData{
			Attributes: &datadogV2.GCPSTSServiceAccountAttributes{
				AccountTags: []string{
					"lorem",
					"ipsum",
				},
				ClientEmail: datadog.PtrString("Test-252bf553ef04b351@test-project.iam.gserviceaccount.com"),
				HostFilters: []string{},
			},
			Type: datadogV2.GCPSERVICEACCOUNTTYPE_GCP_SERVICE_ACCOUNT.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.CreateGCPSTSAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.CreateGCPSTSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.CreateGCPSTSAccount`:\n%s\n", responseContent)
}

```

Copy
#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response 
```
// Create a new entry for your service account with cloud run revision filters enabled returns "OK" response

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
	body := datadogV2.GCPSTSServiceAccountCreateRequest{
		Data: &datadogV2.GCPSTSServiceAccountData{
			Attributes: &datadogV2.GCPSTSServiceAccountAttributes{
				CloudRunRevisionFilters: []string{
					"meh:bleh",
				},
				ClientEmail: datadog.PtrString("Test-252bf553ef04b351@test-project.iam.gserviceaccount.com"),
				HostFilters: []string{},
			},
			Type: datadogV2.GCPSERVICEACCOUNTTYPE_GCP_SERVICE_ACCOUNT.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.CreateGCPSTSAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.CreateGCPSTSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.CreateGCPSTSAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a new entry for your service account returns "OK" response 
```
// Create a new entry for your service account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountAttributes;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountCreateRequest;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountData;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountResponse;
import com.datadog.api.client.v2.model.GCPServiceAccountType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    GCPSTSServiceAccountCreateRequest body =
        new GCPSTSServiceAccountCreateRequest()
            .data(
                new GCPSTSServiceAccountData()
                    .attributes(
                        new GCPSTSServiceAccountAttributes()
                            .clientEmail(
                                "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com"))
                    .type(GCPServiceAccountType.GCP_SERVICE_ACCOUNT));

    try {
      GCPSTSServiceAccountResponse result = apiInstance.createGCPSTSAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#createGCPSTSAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a new entry for your service account with account_tags returns "OK" response 
```
// Create a new entry for your service account with account_tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountAttributes;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountCreateRequest;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountData;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountResponse;
import com.datadog.api.client.v2.model.GCPServiceAccountType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    GCPSTSServiceAccountCreateRequest body =
        new GCPSTSServiceAccountCreateRequest()
            .data(
                new GCPSTSServiceAccountData()
                    .attributes(
                        new GCPSTSServiceAccountAttributes()
                            .accountTags(Arrays.asList("lorem", "ipsum"))
                            .clientEmail(
                                "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com"))
                    .type(GCPServiceAccountType.GCP_SERVICE_ACCOUNT));

    try {
      GCPSTSServiceAccountResponse result = apiInstance.createGCPSTSAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#createGCPSTSAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response 
```
// Create a new entry for your service account with cloud run revision filters enabled returns "OK"
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountAttributes;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountCreateRequest;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountData;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountResponse;
import com.datadog.api.client.v2.model.GCPServiceAccountType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    GCPSTSServiceAccountCreateRequest body =
        new GCPSTSServiceAccountCreateRequest()
            .data(
                new GCPSTSServiceAccountData()
                    .attributes(
                        new GCPSTSServiceAccountAttributes()
                            .cloudRunRevisionFilters(Collections.singletonList("meh:bleh"))
                            .clientEmail(
                                "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com"))
                    .type(GCPServiceAccountType.GCP_SERVICE_ACCOUNT));

    try {
      GCPSTSServiceAccountResponse result = apiInstance.createGCPSTSAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#createGCPSTSAccount");
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

#####  Create a new entry for your service account returns "OK" response 
```
"""
Create a new entry for your service account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_create_request import GCPSTSServiceAccountCreateRequest
from datadog_api_client.v2.model.gcpsts_service_account_data import GCPSTSServiceAccountData

body = GCPSTSServiceAccountCreateRequest(
    data=GCPSTSServiceAccountData(
        attributes=GCPSTSServiceAccountAttributes(
            client_email="Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
            host_filters=[],
        ),
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcpsts_account(body=body)

    print(response)

```

Copy
#####  Create a new entry for your service account with account_tags returns "OK" response 
```
"""
Create a new entry for your service account with account_tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_create_request import GCPSTSServiceAccountCreateRequest
from datadog_api_client.v2.model.gcpsts_service_account_data import GCPSTSServiceAccountData

body = GCPSTSServiceAccountCreateRequest(
    data=GCPSTSServiceAccountData(
        attributes=GCPSTSServiceAccountAttributes(
            account_tags=[
                "lorem",
                "ipsum",
            ],
            client_email="Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
            host_filters=[],
        ),
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcpsts_account(body=body)

    print(response)

```

Copy
#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response 
```
"""
Create a new entry for your service account with cloud run revision filters enabled returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_create_request import GCPSTSServiceAccountCreateRequest
from datadog_api_client.v2.model.gcpsts_service_account_data import GCPSTSServiceAccountData

body = GCPSTSServiceAccountCreateRequest(
    data=GCPSTSServiceAccountData(
        attributes=GCPSTSServiceAccountAttributes(
            cloud_run_revision_filters=[
                "meh:bleh",
            ],
            client_email="Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
            host_filters=[],
        ),
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcpsts_account(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a new entry for your service account returns "OK" response 
```
# Create a new entry for your service account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new

body = DatadogAPIClient::V2::GCPSTSServiceAccountCreateRequest.new({
  data: DatadogAPIClient::V2::GCPSTSServiceAccountData.new({
    attributes: DatadogAPIClient::V2::GCPSTSServiceAccountAttributes.new({
      client_email: "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      host_filters: [],
    }),
    type: DatadogAPIClient::V2::GCPServiceAccountType::GCP_SERVICE_ACCOUNT,
  }),
})
p api_instance.create_gcpsts_account(body)

```

Copy
#####  Create a new entry for your service account with account_tags returns "OK" response 
```
# Create a new entry for your service account with account_tags returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new

body = DatadogAPIClient::V2::GCPSTSServiceAccountCreateRequest.new({
  data: DatadogAPIClient::V2::GCPSTSServiceAccountData.new({
    attributes: DatadogAPIClient::V2::GCPSTSServiceAccountAttributes.new({
      account_tags: [
        "lorem",
        "ipsum",
      ],
      client_email: "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      host_filters: [],
    }),
    type: DatadogAPIClient::V2::GCPServiceAccountType::GCP_SERVICE_ACCOUNT,
  }),
})
p api_instance.create_gcpsts_account(body)

```

Copy
#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response 
```
# Create a new entry for your service account with cloud run revision filters enabled returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new

body = DatadogAPIClient::V2::GCPSTSServiceAccountCreateRequest.new({
  data: DatadogAPIClient::V2::GCPSTSServiceAccountData.new({
    attributes: DatadogAPIClient::V2::GCPSTSServiceAccountAttributes.new({
      cloud_run_revision_filters: [
        "meh:bleh",
      ],
      client_email: "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
      host_filters: [],
    }),
    type: DatadogAPIClient::V2::GCPServiceAccountType::GCP_SERVICE_ACCOUNT,
  }),
})
p api_instance.create_gcpsts_account(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a new entry for your service account returns "OK" response 
```
// Create a new entry for your service account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountAttributes;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountCreateRequest;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountData;
use datadog_api_client::datadogV2::model::GCPServiceAccountType;

#[tokio::main]
async fn main() {
    let body = GCPSTSServiceAccountCreateRequest::new().data(
        GCPSTSServiceAccountData::new()
            .attributes(
                GCPSTSServiceAccountAttributes::new()
                    .client_email(
                        "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com".to_string(),
                    )
                    .host_filters(vec![]),
            )
            .type_(GCPServiceAccountType::GCP_SERVICE_ACCOUNT),
    );
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.create_gcpsts_account(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a new entry for your service account with account_tags returns "OK" response 
```
// Create a new entry for your service account with account_tags returns "OK"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountAttributes;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountCreateRequest;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountData;
use datadog_api_client::datadogV2::model::GCPServiceAccountType;

#[tokio::main]
async fn main() {
    let body = GCPSTSServiceAccountCreateRequest::new().data(
        GCPSTSServiceAccountData::new()
            .attributes(
                GCPSTSServiceAccountAttributes::new()
                    .account_tags(vec!["lorem".to_string(), "ipsum".to_string()])
                    .client_email(
                        "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com".to_string(),
                    )
                    .host_filters(vec![]),
            )
            .type_(GCPServiceAccountType::GCP_SERVICE_ACCOUNT),
    );
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.create_gcpsts_account(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response 
```
// Create a new entry for your service account with cloud run revision filters
// enabled returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountAttributes;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountCreateRequest;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountData;
use datadog_api_client::datadogV2::model::GCPServiceAccountType;

#[tokio::main]
async fn main() {
    let body = GCPSTSServiceAccountCreateRequest::new().data(
        GCPSTSServiceAccountData::new()
            .attributes(
                GCPSTSServiceAccountAttributes::new()
                    .client_email(
                        "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com".to_string(),
                    )
                    .cloud_run_revision_filters(vec!["meh:bleh".to_string()])
                    .host_filters(vec![]),
            )
            .type_(GCPServiceAccountType::GCP_SERVICE_ACCOUNT),
    );
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.create_gcpsts_account(body).await;
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

#####  Create a new entry for your service account returns "OK" response 
```
/**
 * Create a new entry for your service account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

const params: v2.GCPIntegrationApiCreateGCPSTSAccountRequest = {
  body: {
    data: {
      attributes: {
        clientEmail:
          "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
        hostFilters: [],
      },
      type: "gcp_service_account",
    },
  },
};

apiInstance
  .createGCPSTSAccount(params)
  .then((data: v2.GCPSTSServiceAccountResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a new entry for your service account with account_tags returns "OK" response 
```
/**
 * Create a new entry for your service account with account_tags returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

const params: v2.GCPIntegrationApiCreateGCPSTSAccountRequest = {
  body: {
    data: {
      attributes: {
        accountTags: ["lorem", "ipsum"],
        clientEmail:
          "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
        hostFilters: [],
      },
      type: "gcp_service_account",
    },
  },
};

apiInstance
  .createGCPSTSAccount(params)
  .then((data: v2.GCPSTSServiceAccountResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a new entry for your service account with cloud run revision filters enabled returns "OK" response 
```
/**
 * Create a new entry for your service account with cloud run revision filters enabled returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

const params: v2.GCPIntegrationApiCreateGCPSTSAccountRequest = {
  body: {
    data: {
      attributes: {
        cloudRunRevisionFilters: ["meh:bleh"],
        clientEmail:
          "Test-252bf553ef04b351@test-project.iam.gserviceaccount.com",
        hostFilters: [],
      },
      type: "gcp_service_account",
    },
  },
};

apiInstance
  .createGCPSTSAccount(params)
  .then((data: v2.GCPSTSServiceAccountResponse) => {
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
## [Delete a GCP integration](https://docs.datadoghq.com/api/latest/gcp-integration/#delete-a-gcp-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/gcp-integration/#delete-a-gcp-integration-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/gcphttps://api.ap2.datadoghq.com/api/v1/integration/gcphttps://api.datadoghq.eu/api/v1/integration/gcphttps://api.ddog-gov.com/api/v1/integration/gcphttps://api.datadoghq.com/api/v1/integration/gcphttps://api.us3.datadoghq.com/api/v1/integration/gcphttps://api.us5.datadoghq.com/api/v1/integration/gcp
### Overview
This endpoint is deprecated – use the V2 endpoints instead. Delete a given Datadog-GCP integration. This endpoint requires the `gcp_configurations_manage` permission.
### Request
#### Body Data (required)
Delete a given Datadog-GCP integration.
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Field
Type
Description
auth_provider_x509_cert_url
string
Should be `https://www.googleapis.com/oauth2/v1/certs`.
auth_uri
string
Should be `https://accounts.google.com/o/oauth2/auth`.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your email found in your JSON service account key.
client_id
string
Your ID found in your JSON service account key.
client_x509_cert_url
string
Should be `https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL` where `$CLIENT_EMAIL` is the email found in your JSON service account key.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
errors
[string]
An array of errors.
host_filters
string
**DEPRECATED** : A comma-separated list of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
private_key
string
Your private key name found in your JSON service account key.
private_key_id
string
Your private key ID found in your JSON service account key.
project_id
string
Your Google Cloud project ID found in your JSON service account key.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
token_uri
string
Should be `https://accounts.google.com/o/oauth2/token`.
type
string
The value for service_account found in your JSON service account key.
```
{
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "project_id": "datadog-apitest"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby-legacy)


#####  Delete a GCP integration returns "OK" response
Copy
```
                          # Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/gcp" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "project_id": "datadog-apitest"
}
EOF  

                        
```

#####  Delete a GCP integration returns "OK" response
```
// Delete a GCP integration returns "OK" response

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
	body := datadogV1.GCPAccount{
		ClientEmail: datadog.PtrString("252bf553ef04b351@example.com"),
		ClientId:    datadog.PtrString("163662907116366290710"),
		ProjectId:   datadog.PtrString("datadog-apitest"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.DeleteGCPIntegration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.DeleteGCPIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.DeleteGCPIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a GCP integration returns "OK" response
```
// Delete a GCP integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.GcpIntegrationApi;
import com.datadog.api.client.v1.model.GCPAccount;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    GCPAccount body =
        new GCPAccount()
            .clientEmail("252bf553ef04b351@example.com")
            .clientId("163662907116366290710")
            .projectId("datadog-apitest");

    try {
      apiInstance.deleteGCPIntegration(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#deleteGCPIntegration");
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

#####  Delete a GCP integration returns "OK" response
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.GcpIntegration.delete(
    project_id="<GCP_PROJECT_ID>",
    client_email="<GCP_CLIENT_EMAIL>"
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"


```

#####  Delete a GCP integration returns "OK" response
```
"""
Delete a GCP integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v1.model.gcp_account import GCPAccount

body = GCPAccount(
    client_email="252bf553ef04b351@example.com",
    client_id="163662907116366290710",
    project_id="datadog-apitest",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.delete_gcp_integration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a GCP integration returns "OK" response
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
    "project_id": "<GCP_PROJECT_ID>",
    "client_email": "<GCP_CLIENT_EMAIL>"
  }

dog.gcp_integration_delete(config)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a GCP integration returns "OK" response
```
# Delete a GCP integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::GCPIntegrationAPI.new

body = DatadogAPIClient::V1::GCPAccount.new({
  client_email: "252bf553ef04b351@example.com",
  client_id: "163662907116366290710",
  project_id: "datadog-apitest",
})
p api_instance.delete_gcp_integration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a GCP integration returns "OK" response
```
// Delete a GCP integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV1::model::GCPAccount;

#[tokio::main]
async fn main() {
    let body = GCPAccount::new()
        .client_email("252bf553ef04b351@example.com".to_string())
        .client_id("163662907116366290710".to_string())
        .project_id("datadog-apitest".to_string());
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.delete_gcp_integration(body).await;
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

#####  Delete a GCP integration returns "OK" response
```
/**
 * Delete a GCP integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.GCPIntegrationApi(configuration);

const params: v1.GCPIntegrationApiDeleteGCPIntegrationRequest = {
  body: {
    clientEmail: "252bf553ef04b351@example.com",
    clientId: "163662907116366290710",
    projectId: "datadog-apitest",
  },
};

apiInstance
  .deleteGCPIntegration(params)
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
## [Delete an STS enabled GCP Account](https://docs.datadoghq.com/api/latest/gcp-integration/#delete-an-sts-enabled-gcp-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/gcp-integration/#delete-an-sts-enabled-gcp-account-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.datadoghq.eu/api/v2/integration/gcp/accounts/{account_id}https://api.ddog-gov.com/api/v2/integration/gcp/accounts/{account_id}https://api.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}
### Overview
Delete an STS enabled GCP account from within Datadog. This endpoint requires the `gcp_configurations_manage` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Your GCP STS enabled service account’s unique ID.
### Response
  * [204](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPSTSAccount-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPSTSAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPSTSAccount-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#DeleteGCPSTSAccount-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)


#####  Delete an STS enabled GCP Account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an STS enabled GCP Account
```
"""
Delete an STS enabled GCP Account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    api_instance.delete_gcpsts_account(
        account_id="account_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an STS enabled GCP Account
```
# Delete an STS enabled GCP Account returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new
api_instance.delete_gcpsts_account("account_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an STS enabled GCP Account
```
// Delete an STS enabled GCP Account returns "No Content" response

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
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	r, err := api.DeleteGCPSTSAccount(ctx, "account_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.DeleteGCPSTSAccount`: %v\n", err)
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

#####  Delete an STS enabled GCP Account
```
// Delete an STS enabled GCP Account returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    try {
      apiInstance.deleteGCPSTSAccount("account_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#deleteGCPSTSAccount");
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

#####  Delete an STS enabled GCP Account
```
// Delete an STS enabled GCP Account returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.delete_gcpsts_account("account_id".to_string()).await;
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

#####  Delete an STS enabled GCP Account
```
/**
 * Delete an STS enabled GCP Account returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

const params: v2.GCPIntegrationApiDeleteGCPSTSAccountRequest = {
  accountId: "account_id",
};

apiInstance
  .deleteGCPSTSAccount(params)
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
## [Update a GCP integration](https://docs.datadoghq.com/api/latest/gcp-integration/#update-a-gcp-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/gcp-integration/#update-a-gcp-integration-v1)


PUT https://api.ap1.datadoghq.com/api/v1/integration/gcphttps://api.ap2.datadoghq.com/api/v1/integration/gcphttps://api.datadoghq.eu/api/v1/integration/gcphttps://api.ddog-gov.com/api/v1/integration/gcphttps://api.datadoghq.com/api/v1/integration/gcphttps://api.us3.datadoghq.com/api/v1/integration/gcphttps://api.us5.datadoghq.com/api/v1/integration/gcp
### Overview
This endpoint is deprecated – use the V2 endpoints instead. Update a Datadog-GCP integrations host_filters and/or auto-mute. Requires a `project_id` and `client_email`, however these fields cannot be updated. If you need to update these fields, delete and use the create (`POST`) endpoint. The unspecified fields will keep their original values. This endpoint requires the `gcp_configuration_edit` permission.
### Request
#### Body Data (required)
Update a Datadog-GCP integration.
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Field
Type
Description
auth_provider_x509_cert_url
string
Should be `https://www.googleapis.com/oauth2/v1/certs`.
auth_uri
string
Should be `https://accounts.google.com/o/oauth2/auth`.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your email found in your JSON service account key.
client_id
string
Your ID found in your JSON service account key.
client_x509_cert_url
string
Should be `https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL` where `$CLIENT_EMAIL` is the email found in your JSON service account key.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
errors
[string]
An array of errors.
host_filters
string
**DEPRECATED** : A comma-separated list of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
private_key
string
Your private key name found in your JSON service account key.
private_key_id
string
Your private key ID found in your JSON service account key.
project_id
string
Your Google Cloud project ID found in your JSON service account key.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
token_uri
string
Should be `https://accounts.google.com/o/oauth2/token`.
type
string
The value for service_account found in your JSON service account key.
#####  Update a GCP integration cloud run revision filters returns "OK" response
```
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  "host_filters": "key:value,filter:example",
  "cloud_run_revision_filters": [
    "merp:derp"
  ],
  "is_cspm_enabled": true,
  "is_security_command_center_enabled": true,
  "is_resource_change_collection_enabled": true,
  "private_key": "private_key",
  "private_key_id": "123456789abcdefghi123456789abcdefghijklm",
  "project_id": "datadog-apitest",
  "resource_collection_enabled": true,
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "type": "service_account"
}
```

Copy
#####  Update a GCP integration returns "OK" response
```
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  "host_filters": "key:value,filter:example",
  "is_cspm_enabled": true,
  "is_security_command_center_enabled": true,
  "is_resource_change_collection_enabled": true,
  "private_key": "private_key",
  "private_key_id": "123456789abcdefghi123456789abcdefghijklm",
  "project_id": "datadog-apitest",
  "resource_collection_enabled": true,
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "type": "service_account"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)


#####  Update a GCP integration cloud run revision filters returns "OK" response
Copy
```
                          # Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/gcp" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  "host_filters": "key:value,filter:example",
  "cloud_run_revision_filters": [
    "merp:derp"
  ],
  "is_cspm_enabled": true,
  "is_security_command_center_enabled": true,
  "is_resource_change_collection_enabled": true,
  "private_key": "private_key",
  "private_key_id": "123456789abcdefghi123456789abcdefghijklm",
  "project_id": "datadog-apitest",
  "resource_collection_enabled": true,
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "type": "service_account"
}
EOF  

                        
```

#####  Update a GCP integration returns "OK" response
Copy
```
                          # Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/gcp" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "252bf553ef04b351@example.com",
  "client_id": "163662907116366290710",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  "host_filters": "key:value,filter:example",
  "is_cspm_enabled": true,
  "is_security_command_center_enabled": true,
  "is_resource_change_collection_enabled": true,
  "private_key": "private_key",
  "private_key_id": "123456789abcdefghi123456789abcdefghijklm",
  "project_id": "datadog-apitest",
  "resource_collection_enabled": true,
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "type": "service_account"
}
EOF  

                        
```

#####  Update a GCP integration cloud run revision filters returns "OK" response 
```
// Update a GCP integration cloud run revision filters returns "OK" response

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
	body := datadogV1.GCPAccount{
		AuthProviderX509CertUrl: datadog.PtrString("https://www.googleapis.com/oauth2/v1/certs"),
		AuthUri:                 datadog.PtrString("https://accounts.google.com/o/oauth2/auth"),
		ClientEmail:             datadog.PtrString("252bf553ef04b351@example.com"),
		ClientId:                datadog.PtrString("163662907116366290710"),
		ClientX509CertUrl:       datadog.PtrString("https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL"),
		HostFilters:             datadog.PtrString("key:value,filter:example"),
		CloudRunRevisionFilters: []string{
			"merp:derp",
		},
		IsCspmEnabled:                     datadog.PtrBool(true),
		IsSecurityCommandCenterEnabled:    datadog.PtrBool(true),
		IsResourceChangeCollectionEnabled: datadog.PtrBool(true),
		PrivateKey:                        datadog.PtrString("private_key"),
		PrivateKeyId:                      datadog.PtrString("123456789abcdefghi123456789abcdefghijklm"),
		ProjectId:                         datadog.PtrString("datadog-apitest"),
		ResourceCollectionEnabled:         datadog.PtrBool(true),
		TokenUri:                          datadog.PtrString("https://accounts.google.com/o/oauth2/token"),
		Type:                              datadog.PtrString("service_account"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.UpdateGCPIntegration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.UpdateGCPIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.UpdateGCPIntegration`:\n%s\n", responseContent)
}

```

Copy
#####  Update a GCP integration returns "OK" response 
```
// Update a GCP integration returns "OK" response

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
	body := datadogV1.GCPAccount{
		AuthProviderX509CertUrl:           datadog.PtrString("https://www.googleapis.com/oauth2/v1/certs"),
		AuthUri:                           datadog.PtrString("https://accounts.google.com/o/oauth2/auth"),
		ClientEmail:                       datadog.PtrString("252bf553ef04b351@example.com"),
		ClientId:                          datadog.PtrString("163662907116366290710"),
		ClientX509CertUrl:                 datadog.PtrString("https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL"),
		HostFilters:                       datadog.PtrString("key:value,filter:example"),
		IsCspmEnabled:                     datadog.PtrBool(true),
		IsSecurityCommandCenterEnabled:    datadog.PtrBool(true),
		IsResourceChangeCollectionEnabled: datadog.PtrBool(true),
		PrivateKey:                        datadog.PtrString("private_key"),
		PrivateKeyId:                      datadog.PtrString("123456789abcdefghi123456789abcdefghijklm"),
		ProjectId:                         datadog.PtrString("datadog-apitest"),
		ResourceCollectionEnabled:         datadog.PtrBool(true),
		TokenUri:                          datadog.PtrString("https://accounts.google.com/o/oauth2/token"),
		Type:                              datadog.PtrString("service_account"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.UpdateGCPIntegration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.UpdateGCPIntegration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.UpdateGCPIntegration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a GCP integration cloud run revision filters returns "OK" response 
```
// Update a GCP integration cloud run revision filters returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.GcpIntegrationApi;
import com.datadog.api.client.v1.model.GCPAccount;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    GCPAccount body =
        new GCPAccount()
            .authProviderX509CertUrl("https://www.googleapis.com/oauth2/v1/certs")
            .authUri("https://accounts.google.com/o/oauth2/auth")
            .clientEmail("252bf553ef04b351@example.com")
            .clientId("163662907116366290710")
            .clientX509CertUrl("https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL")
            .hostFilters("key:value,filter:example")
            .cloudRunRevisionFilters(Collections.singletonList("merp:derp"))
            .isCspmEnabled(true)
            .isSecurityCommandCenterEnabled(true)
            .isResourceChangeCollectionEnabled(true)
            .privateKey("private_key")
            .privateKeyId("123456789abcdefghi123456789abcdefghijklm")
            .projectId("datadog-apitest")
            .resourceCollectionEnabled(true)
            .tokenUri("https://accounts.google.com/o/oauth2/token")
            .type("service_account");

    try {
      apiInstance.updateGCPIntegration(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#updateGCPIntegration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Update a GCP integration returns "OK" response 
```
// Update a GCP integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.GcpIntegrationApi;
import com.datadog.api.client.v1.model.GCPAccount;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    GCPAccount body =
        new GCPAccount()
            .authProviderX509CertUrl("https://www.googleapis.com/oauth2/v1/certs")
            .authUri("https://accounts.google.com/o/oauth2/auth")
            .clientEmail("252bf553ef04b351@example.com")
            .clientId("163662907116366290710")
            .clientX509CertUrl("https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL")
            .hostFilters("key:value,filter:example")
            .isCspmEnabled(true)
            .isSecurityCommandCenterEnabled(true)
            .isResourceChangeCollectionEnabled(true)
            .privateKey("private_key")
            .privateKeyId("123456789abcdefghi123456789abcdefghijklm")
            .projectId("datadog-apitest")
            .resourceCollectionEnabled(true)
            .tokenUri("https://accounts.google.com/o/oauth2/token")
            .type("service_account");

    try {
      apiInstance.updateGCPIntegration(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#updateGCPIntegration");
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

#####  Update a GCP integration cloud run revision filters returns "OK" response 
```
"""
Update a GCP integration cloud run revision filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v1.model.gcp_account import GCPAccount

body = GCPAccount(
    auth_provider_x509_cert_url="https://www.googleapis.com/oauth2/v1/certs",
    auth_uri="https://accounts.google.com/o/oauth2/auth",
    client_email="252bf553ef04b351@example.com",
    client_id="163662907116366290710",
    client_x509_cert_url="https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
    host_filters="key:value,filter:example",
    cloud_run_revision_filters=[
        "merp:derp",
    ],
    is_cspm_enabled=True,
    is_security_command_center_enabled=True,
    is_resource_change_collection_enabled=True,
    private_key="private_key",
    private_key_id="123456789abcdefghi123456789abcdefghijklm",
    project_id="datadog-apitest",
    resource_collection_enabled=True,
    token_uri="https://accounts.google.com/o/oauth2/token",
    type="service_account",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcp_integration(body=body)

    print(response)

```

Copy
#####  Update a GCP integration returns "OK" response 
```
"""
Update a GCP integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v1.model.gcp_account import GCPAccount

body = GCPAccount(
    auth_provider_x509_cert_url="https://www.googleapis.com/oauth2/v1/certs",
    auth_uri="https://accounts.google.com/o/oauth2/auth",
    client_email="252bf553ef04b351@example.com",
    client_id="163662907116366290710",
    client_x509_cert_url="https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
    host_filters="key:value,filter:example",
    is_cspm_enabled=True,
    is_security_command_center_enabled=True,
    is_resource_change_collection_enabled=True,
    private_key="private_key",
    private_key_id="123456789abcdefghi123456789abcdefghijklm",
    project_id="datadog-apitest",
    resource_collection_enabled=True,
    token_uri="https://accounts.google.com/o/oauth2/token",
    type="service_account",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcp_integration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a GCP integration cloud run revision filters returns "OK" response 
```
# Update a GCP integration cloud run revision filters returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::GCPIntegrationAPI.new

body = DatadogAPIClient::V1::GCPAccount.new({
  auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
  auth_uri: "https://accounts.google.com/o/oauth2/auth",
  client_email: "252bf553ef04b351@example.com",
  client_id: "163662907116366290710",
  client_x509_cert_url: "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  host_filters: "key:value,filter:example",
  cloud_run_revision_filters: [
    "merp:derp",
  ],
  is_cspm_enabled: true,
  is_security_command_center_enabled: true,
  is_resource_change_collection_enabled: true,
  private_key: "private_key",
  private_key_id: "123456789abcdefghi123456789abcdefghijklm",
  project_id: "datadog-apitest",
  resource_collection_enabled: true,
  token_uri: "https://accounts.google.com/o/oauth2/token",
  type: "service_account",
})
p api_instance.update_gcp_integration(body)

```

Copy
#####  Update a GCP integration returns "OK" response 
```
# Update a GCP integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::GCPIntegrationAPI.new

body = DatadogAPIClient::V1::GCPAccount.new({
  auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
  auth_uri: "https://accounts.google.com/o/oauth2/auth",
  client_email: "252bf553ef04b351@example.com",
  client_id: "163662907116366290710",
  client_x509_cert_url: "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
  host_filters: "key:value,filter:example",
  is_cspm_enabled: true,
  is_security_command_center_enabled: true,
  is_resource_change_collection_enabled: true,
  private_key: "private_key",
  private_key_id: "123456789abcdefghi123456789abcdefghijklm",
  project_id: "datadog-apitest",
  resource_collection_enabled: true,
  token_uri: "https://accounts.google.com/o/oauth2/token",
  type: "service_account",
})
p api_instance.update_gcp_integration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a GCP integration cloud run revision filters returns "OK" response 
```
// Update a GCP integration cloud run revision filters returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV1::model::GCPAccount;

#[tokio::main]
async fn main() {
    let body = GCPAccount::new()
        .auth_provider_x509_cert_url("https://www.googleapis.com/oauth2/v1/certs".to_string())
        .auth_uri("https://accounts.google.com/o/oauth2/auth".to_string())
        .client_email("252bf553ef04b351@example.com".to_string())
        .client_id("163662907116366290710".to_string())
        .client_x509_cert_url(
            "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL".to_string(),
        )
        .cloud_run_revision_filters(vec!["merp:derp".to_string()])
        .host_filters("key:value,filter:example".to_string())
        .is_cspm_enabled(true)
        .is_resource_change_collection_enabled(true)
        .is_security_command_center_enabled(true)
        .private_key("private_key".to_string())
        .private_key_id("123456789abcdefghi123456789abcdefghijklm".to_string())
        .project_id("datadog-apitest".to_string())
        .resource_collection_enabled(true)
        .token_uri("https://accounts.google.com/o/oauth2/token".to_string())
        .type_("service_account".to_string());
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.update_gcp_integration(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Update a GCP integration returns "OK" response 
```
// Update a GCP integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV1::model::GCPAccount;

#[tokio::main]
async fn main() {
    let body = GCPAccount::new()
        .auth_provider_x509_cert_url("https://www.googleapis.com/oauth2/v1/certs".to_string())
        .auth_uri("https://accounts.google.com/o/oauth2/auth".to_string())
        .client_email("252bf553ef04b351@example.com".to_string())
        .client_id("163662907116366290710".to_string())
        .client_x509_cert_url(
            "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL".to_string(),
        )
        .host_filters("key:value,filter:example".to_string())
        .is_cspm_enabled(true)
        .is_resource_change_collection_enabled(true)
        .is_security_command_center_enabled(true)
        .private_key("private_key".to_string())
        .private_key_id("123456789abcdefghi123456789abcdefghijklm".to_string())
        .project_id("datadog-apitest".to_string())
        .resource_collection_enabled(true)
        .token_uri("https://accounts.google.com/o/oauth2/token".to_string())
        .type_("service_account".to_string());
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.update_gcp_integration(body).await;
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

#####  Update a GCP integration cloud run revision filters returns "OK" response 
```
/**
 * Update a GCP integration cloud run revision filters returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.GCPIntegrationApi(configuration);

const params: v1.GCPIntegrationApiUpdateGCPIntegrationRequest = {
  body: {
    authProviderX509CertUrl: "https://www.googleapis.com/oauth2/v1/certs",
    authUri: "https://accounts.google.com/o/oauth2/auth",
    clientEmail: "252bf553ef04b351@example.com",
    clientId: "163662907116366290710",
    clientX509CertUrl:
      "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
    hostFilters: "key:value,filter:example",
    cloudRunRevisionFilters: ["merp:derp"],
    isCspmEnabled: true,
    isSecurityCommandCenterEnabled: true,
    isResourceChangeCollectionEnabled: true,
    privateKey: "private_key",
    privateKeyId: "123456789abcdefghi123456789abcdefghijklm",
    projectId: "datadog-apitest",
    resourceCollectionEnabled: true,
    tokenUri: "https://accounts.google.com/o/oauth2/token",
    type: "service_account",
  },
};

apiInstance
  .updateGCPIntegration(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Update a GCP integration returns "OK" response 
```
/**
 * Update a GCP integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.GCPIntegrationApi(configuration);

const params: v1.GCPIntegrationApiUpdateGCPIntegrationRequest = {
  body: {
    authProviderX509CertUrl: "https://www.googleapis.com/oauth2/v1/certs",
    authUri: "https://accounts.google.com/o/oauth2/auth",
    clientEmail: "252bf553ef04b351@example.com",
    clientId: "163662907116366290710",
    clientX509CertUrl:
      "https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
    hostFilters: "key:value,filter:example",
    isCspmEnabled: true,
    isSecurityCommandCenterEnabled: true,
    isResourceChangeCollectionEnabled: true,
    privateKey: "private_key",
    privateKeyId: "123456789abcdefghi123456789abcdefghijklm",
    projectId: "datadog-apitest",
    resourceCollectionEnabled: true,
    tokenUri: "https://accounts.google.com/o/oauth2/token",
    type: "service_account",
  },
};

apiInstance
  .updateGCPIntegration(params)
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
## [Update STS Service Account](https://docs.datadoghq.com/api/latest/gcp-integration/#update-sts-service-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/gcp-integration/#update-sts-service-account-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.datadoghq.eu/api/v2/integration/gcp/accounts/{account_id}https://api.ddog-gov.com/api/v2/integration/gcp/accounts/{account_id}https://api.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts/{account_id}
### Overview
Update an STS enabled service account. This endpoint requires the `gcp_configuration_edit` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Your GCP STS enabled service account’s unique ID.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Field
Type
Description
data
object
Data on your service account.
attributes
object
Attributes associated with your service account.
account_tags
[string]
Tags to be associated with GCP metrics and service checks from your account.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your service account email address.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
host_filters
[string]
**DEPRECATED** : List of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_global_location_enabled
boolean
When enabled, Datadog collects metrics where location is explicitly stated as "global" or where location information cannot be deduced from GCP labels.
default: `true`
is_per_project_quota_enabled
boolean
When enabled, Datadog applies the `X-Goog-User-Project` header, attributing Google Cloud billing and quota usage to the project being monitored rather than the default service account project.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
metric_namespace_configs
[object]
Configurations for GCP metric namespaces.
disabled
boolean
When disabled, Datadog does not collect metrics that are related to this GCP metric namespace.
filters
[string]
When enabled, Datadog applies these additional filters to limit metric collection. A metric is collected only if it does not match all exclusion filters and matches at least one allow filter.
id
string
The id of the GCP metric namespace.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
region_filter_configs
[string]
Configurations for GCP location filtering, such as region, multi-region, or zone. Only monitored resources that match the specified regions are imported into Datadog. By default, Datadog collects from all locations.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
id
string
Your service account's unique ID.
type
enum
The type of account. Allowed enum values: `gcp_service_account`
default: `gcp_service_account`
#####  Update STS Service Account returns "OK" response
```
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@example.com",
      "host_filters": [
        "foo:bar"
      ]
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "type": "gcp_service_account"
  }
}
```

Copy
#####  Update STS Service Account returns "OK" response with cloud run revision filters
```
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@example.com",
      "cloud_run_revision_filters": [
        "merp:derp"
      ]
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "type": "gcp_service_account"
  }
}
```

Copy
#####  Update STS Service Account returns "OK" response with enable resource collection turned on
```
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@example.com",
      "resource_collection_enabled": true
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "type": "gcp_service_account"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPSTSAccount-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPSTSAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPSTSAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPSTSAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#UpdateGCPSTSAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


The account creation response.
Field
Type
Description
data
object
Info on your service account.
attributes
object
Attributes associated with your service account.
account_tags
[string]
Tags to be associated with GCP metrics and service checks from your account.
automute
boolean
Silence monitors for expected GCE instance shutdowns.
client_email
string
Your service account email address.
cloud_run_revision_filters
[string]
**DEPRECATED** : List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. Only Cloud Run revision resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=cloud_run_revision`
host_filters
[string]
**DEPRECATED** : List of filters to limit the VM instances that are pulled into Datadog by using tags. Only VM instance resources that apply to specified filters are imported into Datadog. **Note:** This field is deprecated. Instead, use `monitored_resource_configs` with `type=gce_instance`
is_cspm_enabled
boolean
When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
is_global_location_enabled
boolean
When enabled, Datadog collects metrics where location is explicitly stated as "global" or where location information cannot be deduced from GCP labels.
default: `true`
is_per_project_quota_enabled
boolean
When enabled, Datadog applies the `X-Goog-User-Project` header, attributing Google Cloud billing and quota usage to the project being monitored rather than the default service account project.
is_resource_change_collection_enabled
boolean
When enabled, Datadog scans for all resource change data in your Google Cloud environment.
is_security_command_center_enabled
boolean
When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
metric_namespace_configs
[object]
Configurations for GCP metric namespaces.
disabled
boolean
When disabled, Datadog does not collect metrics that are related to this GCP metric namespace.
filters
[string]
When enabled, Datadog applies these additional filters to limit metric collection. A metric is collected only if it does not match all exclusion filters and matches at least one allow filter.
id
string
The id of the GCP metric namespace.
monitored_resource_configs
[object]
Configurations for GCP monitored resources.
filters
[string]
List of filters to limit the monitored resources that are pulled into Datadog by using tags. Only monitored resources that apply to specified filters are imported into Datadog.
type
enum
The GCP monitored resource type. Only a subset of resource types are supported. Allowed enum values: `cloud_function,cloud_run_revision,gce_instance`
region_filter_configs
[string]
Configurations for GCP location filtering, such as region, multi-region, or zone. Only monitored resources that match the specified regions are imported into Datadog. By default, Datadog collects from all locations.
resource_collection_enabled
boolean
When enabled, Datadog scans for all resources in your GCP environment.
id
string
Your service account's unique ID.
meta
object
Additional information related to your service account.
accessible_projects
[string]
The current list of projects accessible from your service account.
type
enum
The type of account. Allowed enum values: `gcp_service_account`
default: `gcp_service_account`
```
{
  "data": {
    "attributes": {
      "account_tags": [],
      "automute": false,
      "client_email": "datadog-service-account@test-project.iam.gserviceaccount.com",
      "cloud_run_revision_filters": [
        "$KEY:$VALUE"
      ],
      "host_filters": [
        "$KEY:$VALUE"
      ],
      "is_cspm_enabled": false,
      "is_global_location_enabled": true,
      "is_per_project_quota_enabled": true,
      "is_resource_change_collection_enabled": true,
      "is_security_command_center_enabled": true,
      "metric_namespace_configs": [
        {
          "disabled": true,
          "filters": [
            "snapshot.*",
            "!*_by_region"
          ],
          "id": "pubsub"
        }
      ],
      "monitored_resource_configs": [
        {
          "filters": [
            "$KEY:$VALUE"
          ],
          "type": "gce_instance"
        }
      ],
      "region_filter_configs": [
        "nam4",
        "europe-north1"
      ],
      "resource_collection_enabled": false
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "meta": {
      "accessible_projects": []
    },
    "type": "gcp_service_account"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)


#####  Update STS Service Account returns "OK" response
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts/${account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@example.com",
      "host_filters": [
        "foo:bar"
      ]
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "type": "gcp_service_account"
  }
}
EOF  

                        
```

#####  Update STS Service Account returns "OK" response with cloud run revision filters
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts/${account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@example.com",
      "cloud_run_revision_filters": [
        "merp:derp"
      ]
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "type": "gcp_service_account"
  }
}
EOF  

                        
```

#####  Update STS Service Account returns "OK" response with enable resource collection turned on
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/accounts/${account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "client_email": "Test-252bf553ef04b351@example.com",
      "resource_collection_enabled": true
    },
    "id": "d291291f-12c2-22g4-j290-123456678897",
    "type": "gcp_service_account"
  }
}
EOF  

                        
```

#####  Update STS Service Account returns "OK" response 
```
// Update STS Service Account returns "OK" response

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
	// there is a valid "gcp_sts_account" in the system
	GcpStsAccountDataID := os.Getenv("GCP_STS_ACCOUNT_DATA_ID")

	body := datadogV2.GCPSTSServiceAccountUpdateRequest{
		Data: &datadogV2.GCPSTSServiceAccountUpdateRequestData{
			Attributes: &datadogV2.GCPSTSServiceAccountAttributes{
				ClientEmail: datadog.PtrString("Test-252bf553ef04b351@example.com"),
				HostFilters: []string{
					"foo:bar",
				},
			},
			Id:   datadog.PtrString(GcpStsAccountDataID),
			Type: datadogV2.GCPSERVICEACCOUNTTYPE_GCP_SERVICE_ACCOUNT.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.UpdateGCPSTSAccount(ctx, GcpStsAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.UpdateGCPSTSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.UpdateGCPSTSAccount`:\n%s\n", responseContent)
}

```

Copy
#####  Update STS Service Account returns "OK" response with cloud run revision filters 
```
// Update STS Service Account returns "OK" response with cloud run revision filters

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
	// there is a valid "gcp_sts_account" in the system
	GcpStsAccountDataID := os.Getenv("GCP_STS_ACCOUNT_DATA_ID")

	body := datadogV2.GCPSTSServiceAccountUpdateRequest{
		Data: &datadogV2.GCPSTSServiceAccountUpdateRequestData{
			Attributes: &datadogV2.GCPSTSServiceAccountAttributes{
				ClientEmail: datadog.PtrString("Test-252bf553ef04b351@example.com"),
				CloudRunRevisionFilters: []string{
					"merp:derp",
				},
			},
			Id:   datadog.PtrString(GcpStsAccountDataID),
			Type: datadogV2.GCPSERVICEACCOUNTTYPE_GCP_SERVICE_ACCOUNT.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.UpdateGCPSTSAccount(ctx, GcpStsAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.UpdateGCPSTSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.UpdateGCPSTSAccount`:\n%s\n", responseContent)
}

```

Copy
#####  Update STS Service Account returns "OK" response with enable resource collection turned on 
```
// Update STS Service Account returns "OK" response with enable resource collection turned on

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
	// there is a valid "gcp_sts_account" in the system
	GcpStsAccountDataID := os.Getenv("GCP_STS_ACCOUNT_DATA_ID")

	body := datadogV2.GCPSTSServiceAccountUpdateRequest{
		Data: &datadogV2.GCPSTSServiceAccountUpdateRequestData{
			Attributes: &datadogV2.GCPSTSServiceAccountAttributes{
				ClientEmail:               datadog.PtrString("Test-252bf553ef04b351@example.com"),
				ResourceCollectionEnabled: datadog.PtrBool(true),
			},
			Id:   datadog.PtrString(GcpStsAccountDataID),
			Type: datadogV2.GCPSERVICEACCOUNTTYPE_GCP_SERVICE_ACCOUNT.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.UpdateGCPSTSAccount(ctx, GcpStsAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.UpdateGCPSTSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.UpdateGCPSTSAccount`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update STS Service Account returns "OK" response 
```
// Update STS Service Account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountAttributes;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountResponse;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountUpdateRequest;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountUpdateRequestData;
import com.datadog.api.client.v2.model.GCPServiceAccountType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    // there is a valid "gcp_sts_account" in the system
    String GCP_STS_ACCOUNT_DATA_ID = System.getenv("GCP_STS_ACCOUNT_DATA_ID");

    GCPSTSServiceAccountUpdateRequest body =
        new GCPSTSServiceAccountUpdateRequest()
            .data(
                new GCPSTSServiceAccountUpdateRequestData()
                    .attributes(
                        new GCPSTSServiceAccountAttributes()
                            .clientEmail("Test-252bf553ef04b351@example.com")
                            .hostFilters(Collections.singletonList("foo:bar")))
                    .id(GCP_STS_ACCOUNT_DATA_ID)
                    .type(GCPServiceAccountType.GCP_SERVICE_ACCOUNT));

    try {
      GCPSTSServiceAccountResponse result =
          apiInstance.updateGCPSTSAccount(GCP_STS_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#updateGCPSTSAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Update STS Service Account returns "OK" response with cloud run revision filters 
```
// Update STS Service Account returns "OK" response with cloud run revision filters

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountAttributes;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountResponse;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountUpdateRequest;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountUpdateRequestData;
import com.datadog.api.client.v2.model.GCPServiceAccountType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    // there is a valid "gcp_sts_account" in the system
    String GCP_STS_ACCOUNT_DATA_ID = System.getenv("GCP_STS_ACCOUNT_DATA_ID");

    GCPSTSServiceAccountUpdateRequest body =
        new GCPSTSServiceAccountUpdateRequest()
            .data(
                new GCPSTSServiceAccountUpdateRequestData()
                    .attributes(
                        new GCPSTSServiceAccountAttributes()
                            .clientEmail("Test-252bf553ef04b351@example.com")
                            .cloudRunRevisionFilters(Collections.singletonList("merp:derp")))
                    .id(GCP_STS_ACCOUNT_DATA_ID)
                    .type(GCPServiceAccountType.GCP_SERVICE_ACCOUNT));

    try {
      GCPSTSServiceAccountResponse result =
          apiInstance.updateGCPSTSAccount(GCP_STS_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#updateGCPSTSAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Update STS Service Account returns "OK" response with enable resource collection turned on 
```
// Update STS Service Account returns "OK" response with enable resource collection turned on

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountAttributes;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountResponse;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountUpdateRequest;
import com.datadog.api.client.v2.model.GCPSTSServiceAccountUpdateRequestData;
import com.datadog.api.client.v2.model.GCPServiceAccountType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    // there is a valid "gcp_sts_account" in the system
    String GCP_STS_ACCOUNT_DATA_ID = System.getenv("GCP_STS_ACCOUNT_DATA_ID");

    GCPSTSServiceAccountUpdateRequest body =
        new GCPSTSServiceAccountUpdateRequest()
            .data(
                new GCPSTSServiceAccountUpdateRequestData()
                    .attributes(
                        new GCPSTSServiceAccountAttributes()
                            .clientEmail("Test-252bf553ef04b351@example.com")
                            .resourceCollectionEnabled(true))
                    .id(GCP_STS_ACCOUNT_DATA_ID)
                    .type(GCPServiceAccountType.GCP_SERVICE_ACCOUNT));

    try {
      GCPSTSServiceAccountResponse result =
          apiInstance.updateGCPSTSAccount(GCP_STS_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#updateGCPSTSAccount");
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

#####  Update STS Service Account returns "OK" response 
```
"""
Update STS Service Account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_update_request import GCPSTSServiceAccountUpdateRequest
from datadog_api_client.v2.model.gcpsts_service_account_update_request_data import GCPSTSServiceAccountUpdateRequestData

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = environ["GCP_STS_ACCOUNT_DATA_ID"]

body = GCPSTSServiceAccountUpdateRequest(
    data=GCPSTSServiceAccountUpdateRequestData(
        attributes=GCPSTSServiceAccountAttributes(
            client_email="Test-252bf553ef04b351@example.com",
            host_filters=[
                "foo:bar",
            ],
        ),
        id=GCP_STS_ACCOUNT_DATA_ID,
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcpsts_account(account_id=GCP_STS_ACCOUNT_DATA_ID, body=body)

    print(response)

```

Copy
#####  Update STS Service Account returns "OK" response with cloud run revision filters 
```
"""
Update STS Service Account returns "OK" response with cloud run revision filters
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_update_request import GCPSTSServiceAccountUpdateRequest
from datadog_api_client.v2.model.gcpsts_service_account_update_request_data import GCPSTSServiceAccountUpdateRequestData

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = environ["GCP_STS_ACCOUNT_DATA_ID"]

body = GCPSTSServiceAccountUpdateRequest(
    data=GCPSTSServiceAccountUpdateRequestData(
        attributes=GCPSTSServiceAccountAttributes(
            client_email="Test-252bf553ef04b351@example.com",
            cloud_run_revision_filters=[
                "merp:derp",
            ],
        ),
        id=GCP_STS_ACCOUNT_DATA_ID,
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcpsts_account(account_id=GCP_STS_ACCOUNT_DATA_ID, body=body)

    print(response)

```

Copy
#####  Update STS Service Account returns "OK" response with enable resource collection turned on 
```
"""
Update STS Service Account returns "OK" response with enable resource collection turned on
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_update_request import GCPSTSServiceAccountUpdateRequest
from datadog_api_client.v2.model.gcpsts_service_account_update_request_data import GCPSTSServiceAccountUpdateRequestData

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = environ["GCP_STS_ACCOUNT_DATA_ID"]

body = GCPSTSServiceAccountUpdateRequest(
    data=GCPSTSServiceAccountUpdateRequestData(
        attributes=GCPSTSServiceAccountAttributes(
            client_email="Test-252bf553ef04b351@example.com",
            resource_collection_enabled=True,
        ),
        id=GCP_STS_ACCOUNT_DATA_ID,
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcpsts_account(account_id=GCP_STS_ACCOUNT_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update STS Service Account returns "OK" response 
```
# Update STS Service Account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = ENV["GCP_STS_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::GCPSTSServiceAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::GCPSTSServiceAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::GCPSTSServiceAccountAttributes.new({
      client_email: "Test-252bf553ef04b351@example.com",
      host_filters: [
        "foo:bar",
      ],
    }),
    id: GCP_STS_ACCOUNT_DATA_ID,
    type: DatadogAPIClient::V2::GCPServiceAccountType::GCP_SERVICE_ACCOUNT,
  }),
})
p api_instance.update_gcpsts_account(GCP_STS_ACCOUNT_DATA_ID, body)

```

Copy
#####  Update STS Service Account returns "OK" response with cloud run revision filters 
```
# Update STS Service Account returns "OK" response with cloud run revision filters

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = ENV["GCP_STS_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::GCPSTSServiceAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::GCPSTSServiceAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::GCPSTSServiceAccountAttributes.new({
      client_email: "Test-252bf553ef04b351@example.com",
      cloud_run_revision_filters: [
        "merp:derp",
      ],
    }),
    id: GCP_STS_ACCOUNT_DATA_ID,
    type: DatadogAPIClient::V2::GCPServiceAccountType::GCP_SERVICE_ACCOUNT,
  }),
})
p api_instance.update_gcpsts_account(GCP_STS_ACCOUNT_DATA_ID, body)

```

Copy
#####  Update STS Service Account returns "OK" response with enable resource collection turned on 
```
# Update STS Service Account returns "OK" response with enable resource collection turned on

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = ENV["GCP_STS_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::GCPSTSServiceAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::GCPSTSServiceAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::GCPSTSServiceAccountAttributes.new({
      client_email: "Test-252bf553ef04b351@example.com",
      resource_collection_enabled: true,
    }),
    id: GCP_STS_ACCOUNT_DATA_ID,
    type: DatadogAPIClient::V2::GCPServiceAccountType::GCP_SERVICE_ACCOUNT,
  }),
})
p api_instance.update_gcpsts_account(GCP_STS_ACCOUNT_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update STS Service Account returns "OK" response 
```
// Update STS Service Account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountAttributes;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountUpdateRequest;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountUpdateRequestData;
use datadog_api_client::datadogV2::model::GCPServiceAccountType;

#[tokio::main]
async fn main() {
    // there is a valid "gcp_sts_account" in the system
    let gcp_sts_account_data_id = std::env::var("GCP_STS_ACCOUNT_DATA_ID").unwrap();
    let body = GCPSTSServiceAccountUpdateRequest::new().data(
        GCPSTSServiceAccountUpdateRequestData::new()
            .attributes(
                GCPSTSServiceAccountAttributes::new()
                    .client_email("Test-252bf553ef04b351@example.com".to_string())
                    .host_filters(vec!["foo:bar".to_string()]),
            )
            .id(gcp_sts_account_data_id.clone())
            .type_(GCPServiceAccountType::GCP_SERVICE_ACCOUNT),
    );
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api
        .update_gcpsts_account(gcp_sts_account_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Update STS Service Account returns "OK" response with cloud run revision filters 
```
// Update STS Service Account returns "OK" response with cloud run revision filters
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountAttributes;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountUpdateRequest;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountUpdateRequestData;
use datadog_api_client::datadogV2::model::GCPServiceAccountType;

#[tokio::main]
async fn main() {
    // there is a valid "gcp_sts_account" in the system
    let gcp_sts_account_data_id = std::env::var("GCP_STS_ACCOUNT_DATA_ID").unwrap();
    let body = GCPSTSServiceAccountUpdateRequest::new().data(
        GCPSTSServiceAccountUpdateRequestData::new()
            .attributes(
                GCPSTSServiceAccountAttributes::new()
                    .client_email("Test-252bf553ef04b351@example.com".to_string())
                    .cloud_run_revision_filters(vec!["merp:derp".to_string()]),
            )
            .id(gcp_sts_account_data_id.clone())
            .type_(GCPServiceAccountType::GCP_SERVICE_ACCOUNT),
    );
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api
        .update_gcpsts_account(gcp_sts_account_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Update STS Service Account returns "OK" response with enable resource collection turned on 
```
// Update STS Service Account returns "OK" response with enable resource
// collection turned on
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountAttributes;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountUpdateRequest;
use datadog_api_client::datadogV2::model::GCPSTSServiceAccountUpdateRequestData;
use datadog_api_client::datadogV2::model::GCPServiceAccountType;

#[tokio::main]
async fn main() {
    // there is a valid "gcp_sts_account" in the system
    let gcp_sts_account_data_id = std::env::var("GCP_STS_ACCOUNT_DATA_ID").unwrap();
    let body = GCPSTSServiceAccountUpdateRequest::new().data(
        GCPSTSServiceAccountUpdateRequestData::new()
            .attributes(
                GCPSTSServiceAccountAttributes::new()
                    .client_email("Test-252bf553ef04b351@example.com".to_string())
                    .resource_collection_enabled(true),
            )
            .id(gcp_sts_account_data_id.clone())
            .type_(GCPServiceAccountType::GCP_SERVICE_ACCOUNT),
    );
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api
        .update_gcpsts_account(gcp_sts_account_data_id.clone(), body)
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

#####  Update STS Service Account returns "OK" response 
```
/**
 * Update STS Service Account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

// there is a valid "gcp_sts_account" in the system
const GCP_STS_ACCOUNT_DATA_ID = process.env.GCP_STS_ACCOUNT_DATA_ID as string;

const params: v2.GCPIntegrationApiUpdateGCPSTSAccountRequest = {
  body: {
    data: {
      attributes: {
        clientEmail: "Test-252bf553ef04b351@example.com",
        hostFilters: ["foo:bar"],
      },
      id: GCP_STS_ACCOUNT_DATA_ID,
      type: "gcp_service_account",
    },
  },
  accountId: GCP_STS_ACCOUNT_DATA_ID,
};

apiInstance
  .updateGCPSTSAccount(params)
  .then((data: v2.GCPSTSServiceAccountResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Update STS Service Account returns "OK" response with cloud run revision filters 
```
/**
 * Update STS Service Account returns "OK" response with cloud run revision filters
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

// there is a valid "gcp_sts_account" in the system
const GCP_STS_ACCOUNT_DATA_ID = process.env.GCP_STS_ACCOUNT_DATA_ID as string;

const params: v2.GCPIntegrationApiUpdateGCPSTSAccountRequest = {
  body: {
    data: {
      attributes: {
        clientEmail: "Test-252bf553ef04b351@example.com",
        cloudRunRevisionFilters: ["merp:derp"],
      },
      id: GCP_STS_ACCOUNT_DATA_ID,
      type: "gcp_service_account",
    },
  },
  accountId: GCP_STS_ACCOUNT_DATA_ID,
};

apiInstance
  .updateGCPSTSAccount(params)
  .then((data: v2.GCPSTSServiceAccountResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Update STS Service Account returns "OK" response with enable resource collection turned on 
```
/**
 * Update STS Service Account returns "OK" response with enable resource collection turned on
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

// there is a valid "gcp_sts_account" in the system
const GCP_STS_ACCOUNT_DATA_ID = process.env.GCP_STS_ACCOUNT_DATA_ID as string;

const params: v2.GCPIntegrationApiUpdateGCPSTSAccountRequest = {
  body: {
    data: {
      attributes: {
        clientEmail: "Test-252bf553ef04b351@example.com",
        resourceCollectionEnabled: true,
      },
      id: GCP_STS_ACCOUNT_DATA_ID,
      type: "gcp_service_account",
    },
  },
  accountId: GCP_STS_ACCOUNT_DATA_ID,
};

apiInstance
  .updateGCPSTSAccount(params)
  .then((data: v2.GCPSTSServiceAccountResponse) => {
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
## [Create a Datadog GCP principal](https://docs.datadoghq.com/api/latest/gcp-integration/#create-a-datadog-gcp-principal)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/gcp-integration/#create-a-datadog-gcp-principal-v2)


POST https://api.ap1.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.ap2.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.datadoghq.eu/api/v2/integration/gcp/sts_delegatehttps://api.ddog-gov.com/api/v2/integration/gcp/sts_delegatehttps://api.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.us3.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.us5.datadoghq.com/api/v2/integration/gcp/sts_delegate
### Overview
Create a Datadog GCP principal. This endpoint requires the `gcp_configuration_edit` permission.
### Request
#### Body Data 
Create a delegate service account within Datadog.
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Expand All
Field
Type
Description
No request body
```
{}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/gcp-integration/#MakeGCPSTSDelegate-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#MakeGCPSTSDelegate-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/gcp-integration/#MakeGCPSTSDelegate-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#MakeGCPSTSDelegate-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Your delegate service account response data.
Field
Type
Description
data
object
Datadog principal service account info.
attributes
object
Your delegate account attributes.
delegate_account_email
string
Your organization's Datadog principal email address.
id
string
The ID of the delegate service account.
type
enum
The type of account. Allowed enum values: `gcp_sts_delegate`
default: `gcp_sts_delegate`
```
{
  "data": {
    "attributes": {
      "delegate_account_email": "ddgci-1a19n28hb1a812221893@datadog-gci-sts-us5-prod.iam.gserviceaccount.com"
    },
    "id": "ddgci-1a19n28hb1a812221893@datadog-gci-sts-us5-prod.iam.gserviceaccount.com",
    "type": "gcp_sts_delegate"
  }
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)


#####  Create a Datadog GCP principal with empty body returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/sts_delegate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                        
```

#####  Create a Datadog GCP principal with empty body returns "OK" response
```
// Create a Datadog GCP principal with empty body returns "OK" response

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
	body := new(interface{})
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.MakeGCPSTSDelegate(ctx, *datadogV2.NewMakeGCPSTSDelegateOptionalParameters().WithBody(body))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.MakeGCPSTSDelegate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.MakeGCPSTSDelegate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a Datadog GCP principal with empty body returns "OK" response
```
// Create a Datadog GCP principal with empty body returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.api.GcpIntegrationApi.MakeGCPSTSDelegateOptionalParameters;
import com.datadog.api.client.v2.model.GCPSTSDelegateAccountResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    Object body = new Object();

    try {
      GCPSTSDelegateAccountResponse result =
          apiInstance.makeGCPSTSDelegate(new MakeGCPSTSDelegateOptionalParameters().body(body));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#makeGCPSTSDelegate");
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

#####  Create a Datadog GCP principal with empty body returns "OK" response
```
"""
Create a Datadog GCP principal with empty body returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi

body = dict()

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.make_gcpsts_delegate(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a Datadog GCP principal with empty body returns "OK" response
```
# Create a Datadog GCP principal with empty body returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new

body = {}
opts = {
  body: body,
}
p api_instance.make_gcpsts_delegate(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a Datadog GCP principal with empty body returns "OK" response
```
// Create a Datadog GCP principal with empty body returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;
use datadog_api_client::datadogV2::api_gcp_integration::MakeGCPSTSDelegateOptionalParams;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = BTreeMap::new();
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api
        .make_gcpsts_delegate(MakeGCPSTSDelegateOptionalParams::default().body(body))
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

#####  Create a Datadog GCP principal with empty body returns "OK" response
```
/**
 * Create a Datadog GCP principal with empty body returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

const params: v2.GCPIntegrationApiMakeGCPSTSDelegateRequest = {
  body: {},
};

apiInstance
  .makeGCPSTSDelegate(params)
  .then((data: v2.GCPSTSDelegateAccountResponse) => {
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
## [List delegate account](https://docs.datadoghq.com/api/latest/gcp-integration/#list-delegate-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/gcp-integration/#list-delegate-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.ap2.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.datadoghq.eu/api/v2/integration/gcp/sts_delegatehttps://api.ddog-gov.com/api/v2/integration/gcp/sts_delegatehttps://api.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.us3.datadoghq.com/api/v2/integration/gcp/sts_delegatehttps://api.us5.datadoghq.com/api/v2/integration/gcp/sts_delegate
### Overview
List your Datadog-GCP STS delegate account configured in your Datadog account. This endpoint requires the `gcp_configuration_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/gcp-integration/#GetGCPSTSDelegate-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/gcp-integration/#GetGCPSTSDelegate-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/gcp-integration/#GetGCPSTSDelegate-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


Your delegate service account response data.
Field
Type
Description
data
object
Datadog principal service account info.
attributes
object
Your delegate account attributes.
delegate_account_email
string
Your organization's Datadog principal email address.
id
string
The ID of the delegate service account.
type
enum
The type of account. Allowed enum values: `gcp_sts_delegate`
default: `gcp_sts_delegate`
```
{
  "data": {
    "attributes": {
      "delegate_account_email": "ddgci-1a19n28hb1a812221893@datadog-gci-sts-us5-prod.iam.gserviceaccount.com"
    },
    "id": "ddgci-1a19n28hb1a812221893@datadog-gci-sts-us5-prod.iam.gserviceaccount.com",
    "type": "gcp_sts_delegate"
  }
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Model](https://docs.datadoghq.com/api/latest/gcp-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/gcp-integration/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/gcp-integration/?code-lang=typescript)


#####  List delegate account
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/gcp/sts_delegate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List delegate account
```
"""
List delegate account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.get_gcpsts_delegate()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List delegate account
```
# List delegate account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::GCPIntegrationAPI.new
p api_instance.get_gcpsts_delegate()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List delegate account
```
// List delegate account returns "OK" response

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
	api := datadogV2.NewGCPIntegrationApi(apiClient)
	resp, r, err := api.GetGCPSTSDelegate(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GCPIntegrationApi.GetGCPSTSDelegate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `GCPIntegrationApi.GetGCPSTSDelegate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List delegate account
```
// List delegate account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.GcpIntegrationApi;
import com.datadog.api.client.v2.model.GCPSTSDelegateAccountResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    GcpIntegrationApi apiInstance = new GcpIntegrationApi(defaultClient);

    try {
      GCPSTSDelegateAccountResponse result = apiInstance.getGCPSTSDelegate();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcpIntegrationApi#getGCPSTSDelegate");
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

#####  List delegate account
```
// List delegate account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_gcp_integration::GCPIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = GCPIntegrationAPI::with_config(configuration);
    let resp = api.get_gcpsts_delegate().await;
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

#####  List delegate account
```
/**
 * List delegate account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.GCPIntegrationApi(configuration);

apiInstance
  .getGCPSTSDelegate()
  .then((data: v2.GCPSTSDelegateAccountResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=badfaab2-ff12-4dd0-91e8-24898e3e64e5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=ddd7bc7d-531f-40a1-a03f-bcc567f6462b&pt=GCP%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fgcp-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=badfaab2-ff12-4dd0-91e8-24898e3e64e5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=ddd7bc7d-531f-40a1-a03f-bcc567f6462b&pt=GCP%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fgcp-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=e0cc25ea-5c1f-4896-9231-d6936e2237d1&bo=2&sid=b77a5fe0f0bf11f0bab0291dd4b5f9fd&vid=b77a7130f0bf11f0b69eb7008fe8e23b&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=GCP%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fgcp-integration%2F&r=&lt=2515&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=547360)
Feedback
## Was this page helpful?
Yes 🎉
No 👎
Next
![](https://survey-images.hotjar.com/surveys/logo/90f40352a7464c849f5ce82ccd0e758d)
