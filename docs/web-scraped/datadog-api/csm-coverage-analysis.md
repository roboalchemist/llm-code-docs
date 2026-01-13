# Source: https://docs.datadoghq.com/api/latest/csm-coverage-analysis/

# CSM Coverage Analysis
Datadog Cloud Security Management (CSM) delivers real-time threat detection and continuous configuration audits across your entire cloud infrastructure, all in a unified view for seamless collaboration and faster remediation. Go to <https://docs.datadoghq.com/security/cloud_security_management> to learn more.
## [Get the CSM Cloud Accounts Coverage Analysis](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#get-the-csm-cloud-accounts-coverage-analysis)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#get-the-csm-cloud-accounts-coverage-analysis-v2)


GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accountshttps://api.ap2.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accountshttps://api.datadoghq.eu/api/v2/csm/onboarding/coverage_analysis/cloud_accountshttps://api.ddog-gov.com/api/v2/csm/onboarding/coverage_analysis/cloud_accountshttps://api.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accountshttps://api.us3.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accountshttps://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts
### Overview
Get the CSM Coverage Analysis of your Cloud Accounts. This is calculated based on the number of your Cloud Accounts that are scanned for security issues.
### Response
  * [200](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMCloudAccountsCoverageAnalysis-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMCloudAccountsCoverageAnalysis-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMCloudAccountsCoverageAnalysis-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


CSM Cloud Accounts Coverage Analysis response.
Field
Type
Description
data
object
CSM Cloud Accounts Coverage Analysis data.
attributes
object
CSM Cloud Accounts Coverage Analysis attributes.
aws_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
azure_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
gcp_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
org_id
int64
The ID of your organization.
total_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
id
string
The ID of your organization.
type
string
The type of the resource. The value should always be `get_cloud_accounts_coverage_analysis_response_public_v0`.
default: `get_cloud_accounts_coverage_analysis_response_public_v0`
```
{
  "data": {
    "attributes": {
      "aws_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      },
      "azure_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      },
      "gcp_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      },
      "org_id": 123456,
      "total_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      }
    },
    "id": "66b3c6b5-5c9a-457e-b1c3-f247ca23afa3",
    "type": "get_cloud_accounts_coverage_analysis_response_public_v0"
  }
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


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
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=typescript)


#####  Get the CSM Cloud Accounts Coverage Analysis
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the CSM Cloud Accounts Coverage Analysis
```
"""
Get the CSM Cloud Accounts Coverage Analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_coverage_analysis_api import CSMCoverageAnalysisApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMCoverageAnalysisApi(api_client)
    response = api_instance.get_csm_cloud_accounts_coverage_analysis()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the CSM Cloud Accounts Coverage Analysis
```
# Get the CSM Cloud Accounts Coverage Analysis returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMCoverageAnalysisAPI.new
p api_instance.get_csm_cloud_accounts_coverage_analysis()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the CSM Cloud Accounts Coverage Analysis
```
// Get the CSM Cloud Accounts Coverage Analysis returns "OK" response

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
	api := datadogV2.NewCSMCoverageAnalysisApi(apiClient)
	resp, r, err := api.GetCSMCloudAccountsCoverageAnalysis(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMCoverageAnalysisApi.GetCSMCloudAccountsCoverageAnalysis`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMCoverageAnalysisApi.GetCSMCloudAccountsCoverageAnalysis`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the CSM Cloud Accounts Coverage Analysis
```
// Get the CSM Cloud Accounts Coverage Analysis returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmCoverageAnalysisApi;
import com.datadog.api.client.v2.model.CsmCloudAccountsCoverageAnalysisResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmCoverageAnalysisApi apiInstance = new CsmCoverageAnalysisApi(defaultClient);

    try {
      CsmCloudAccountsCoverageAnalysisResponse result =
          apiInstance.getCSMCloudAccountsCoverageAnalysis();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CsmCoverageAnalysisApi#getCSMCloudAccountsCoverageAnalysis");
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

#####  Get the CSM Cloud Accounts Coverage Analysis
```
// Get the CSM Cloud Accounts Coverage Analysis returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_coverage_analysis::CSMCoverageAnalysisAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMCoverageAnalysisAPI::with_config(configuration);
    let resp = api.get_csm_cloud_accounts_coverage_analysis().await;
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

#####  Get the CSM Cloud Accounts Coverage Analysis
```
/**
 * Get the CSM Cloud Accounts Coverage Analysis returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMCoverageAnalysisApi(configuration);

apiInstance
  .getCSMCloudAccountsCoverageAnalysis()
  .then((data: v2.CsmCloudAccountsCoverageAnalysisResponse) => {
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
## [Get the CSM Hosts and Containers Coverage Analysis](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#get-the-csm-hosts-and-containers-coverage-analysis)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#get-the-csm-hosts-and-containers-coverage-analysis-v2)


GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containershttps://api.ap2.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containershttps://api.datadoghq.eu/api/v2/csm/onboarding/coverage_analysis/hosts_and_containershttps://api.ddog-gov.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containershttps://api.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containershttps://api.us3.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containershttps://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers
### Overview
Get the CSM Coverage Analysis of your Hosts and Containers. This is calculated based on the number of agents running on your Hosts and Containers with CSM feature(s) enabled.
### Response
  * [200](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMHostsAndContainersCoverageAnalysis-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMHostsAndContainersCoverageAnalysis-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMHostsAndContainersCoverageAnalysis-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


CSM Hosts and Containers Coverage Analysis response.
Field
Type
Description
data
object
CSM Hosts and Containers Coverage Analysis data.
attributes
object
CSM Hosts and Containers Coverage Analysis attributes.
cspm_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
cws_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
org_id
int64
The ID of your organization.
total_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
vm_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
id
string
The ID of your organization.
type
string
The type of the resource. The value should always be `get_hosts_and_containers_coverage_analysis_response_public_v0`.
default: `get_hosts_and_containers_coverage_analysis_response_public_v0`
```
{
  "data": {
    "attributes": {
      "cspm_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      },
      "cws_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      },
      "org_id": 123456,
      "total_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      },
      "vm_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      }
    },
    "id": "66b3c6b5-5c9a-457e-b1c3-f247ca23afa3",
    "type": "get_hosts_and_containers_coverage_analysis_response_public_v0"
  }
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


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
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=typescript)


#####  Get the CSM Hosts and Containers Coverage Analysis
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the CSM Hosts and Containers Coverage Analysis
```
"""
Get the CSM Hosts and Containers Coverage Analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_coverage_analysis_api import CSMCoverageAnalysisApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMCoverageAnalysisApi(api_client)
    response = api_instance.get_csm_hosts_and_containers_coverage_analysis()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the CSM Hosts and Containers Coverage Analysis
```
# Get the CSM Hosts and Containers Coverage Analysis returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMCoverageAnalysisAPI.new
p api_instance.get_csm_hosts_and_containers_coverage_analysis()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the CSM Hosts and Containers Coverage Analysis
```
// Get the CSM Hosts and Containers Coverage Analysis returns "OK" response

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
	api := datadogV2.NewCSMCoverageAnalysisApi(apiClient)
	resp, r, err := api.GetCSMHostsAndContainersCoverageAnalysis(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMCoverageAnalysisApi.GetCSMHostsAndContainersCoverageAnalysis`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMCoverageAnalysisApi.GetCSMHostsAndContainersCoverageAnalysis`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the CSM Hosts and Containers Coverage Analysis
```
// Get the CSM Hosts and Containers Coverage Analysis returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmCoverageAnalysisApi;
import com.datadog.api.client.v2.model.CsmHostsAndContainersCoverageAnalysisResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmCoverageAnalysisApi apiInstance = new CsmCoverageAnalysisApi(defaultClient);

    try {
      CsmHostsAndContainersCoverageAnalysisResponse result =
          apiInstance.getCSMHostsAndContainersCoverageAnalysis();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CsmCoverageAnalysisApi#getCSMHostsAndContainersCoverageAnalysis");
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

#####  Get the CSM Hosts and Containers Coverage Analysis
```
// Get the CSM Hosts and Containers Coverage Analysis returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_coverage_analysis::CSMCoverageAnalysisAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMCoverageAnalysisAPI::with_config(configuration);
    let resp = api.get_csm_hosts_and_containers_coverage_analysis().await;
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

#####  Get the CSM Hosts and Containers Coverage Analysis
```
/**
 * Get the CSM Hosts and Containers Coverage Analysis returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMCoverageAnalysisApi(configuration);

apiInstance
  .getCSMHostsAndContainersCoverageAnalysis()
  .then((data: v2.CsmHostsAndContainersCoverageAnalysisResponse) => {
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
## [Get the CSM Serverless Coverage Analysis](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#get-the-csm-serverless-coverage-analysis)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#get-the-csm-serverless-coverage-analysis-v2)


GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverlesshttps://api.ap2.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverlesshttps://api.datadoghq.eu/api/v2/csm/onboarding/coverage_analysis/serverlesshttps://api.ddog-gov.com/api/v2/csm/onboarding/coverage_analysis/serverlesshttps://api.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverlesshttps://api.us3.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverlesshttps://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless
### Overview
Get the CSM Coverage Analysis of your Serverless Resources. This is calculated based on the number of agents running on your Serverless Resources with CSM feature(s) enabled.
### Response
  * [200](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMServerlessCoverageAnalysis-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMServerlessCoverageAnalysis-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/#GetCSMServerlessCoverageAnalysis-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


CSM Serverless Resources Coverage Analysis response.
Field
Type
Description
data
object
CSM Serverless Resources Coverage Analysis data.
attributes
object
CSM Serverless Resources Coverage Analysis attributes.
cws_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
org_id
int64
The ID of your organization.
total_coverage
object
CSM Coverage Analysis.
configured_resources_count
int64
The number of fully configured resources.
coverage
double
The coverage percentage.
partially_configured_resources_count
int64
The number of partially configured resources.
total_resources_count
int64
The total number of resources.
id
string
The ID of your organization.
type
string
The type of the resource. The value should always be `get_serverless_coverage_analysis_response_public_v0`.
default: `get_serverless_coverage_analysis_response_public_v0`
```
{
  "data": {
    "attributes": {
      "cws_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      },
      "org_id": 123456,
      "total_coverage": {
        "configured_resources_count": 8,
        "coverage": 0.8,
        "partially_configured_resources_count": 0,
        "total_resources_count": 10
      }
    },
    "id": "66b3c6b5-5c9a-457e-b1c3-f247ca23afa3",
    "type": "get_serverless_coverage_analysis_response_public_v0"
  }
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


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
  * [Model](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)
  * [Example](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/csm-coverage-analysis/?code-lang=typescript)


#####  Get the CSM Serverless Coverage Analysis
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the CSM Serverless Coverage Analysis
```
"""
Get the CSM Serverless Coverage Analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_coverage_analysis_api import CSMCoverageAnalysisApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMCoverageAnalysisApi(api_client)
    response = api_instance.get_csm_serverless_coverage_analysis()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the CSM Serverless Coverage Analysis
```
# Get the CSM Serverless Coverage Analysis returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMCoverageAnalysisAPI.new
p api_instance.get_csm_serverless_coverage_analysis()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the CSM Serverless Coverage Analysis
```
// Get the CSM Serverless Coverage Analysis returns "OK" response

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
	api := datadogV2.NewCSMCoverageAnalysisApi(apiClient)
	resp, r, err := api.GetCSMServerlessCoverageAnalysis(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CSMCoverageAnalysisApi.GetCSMServerlessCoverageAnalysis`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CSMCoverageAnalysisApi.GetCSMServerlessCoverageAnalysis`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the CSM Serverless Coverage Analysis
```
// Get the CSM Serverless Coverage Analysis returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CsmCoverageAnalysisApi;
import com.datadog.api.client.v2.model.CsmServerlessCoverageAnalysisResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CsmCoverageAnalysisApi apiInstance = new CsmCoverageAnalysisApi(defaultClient);

    try {
      CsmServerlessCoverageAnalysisResponse result = apiInstance.getCSMServerlessCoverageAnalysis();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CsmCoverageAnalysisApi#getCSMServerlessCoverageAnalysis");
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

#####  Get the CSM Serverless Coverage Analysis
```
// Get the CSM Serverless Coverage Analysis returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_csm_coverage_analysis::CSMCoverageAnalysisAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CSMCoverageAnalysisAPI::with_config(configuration);
    let resp = api.get_csm_serverless_coverage_analysis().await;
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

#####  Get the CSM Serverless Coverage Analysis
```
/**
 * Get the CSM Serverless Coverage Analysis returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CSMCoverageAnalysisApi(configuration);

apiInstance
  .getCSMServerlessCoverageAnalysis()
  .then((data: v2.CsmServerlessCoverageAnalysisResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b28a1bb4-2b3d-4439-a283-21505def6896&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b514547b-f614-46c8-bbfb-45b7c5411aa7&pt=CSM%20Coverage%20Analysis&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcsm-coverage-analysis%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b28a1bb4-2b3d-4439-a283-21505def6896&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b514547b-f614-46c8-bbfb-45b7c5411aa7&pt=CSM%20Coverage%20Analysis&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcsm-coverage-analysis%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=c100eba4-35a2-441d-b42c-eab9e5877b8f&bo=2&sid=53eb54b0f0bf11f08bc051f3bb0a0149&vid=53ebab10f0bf11f08df6bf78b3295379&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=CSM%20Coverage%20Analysis&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcsm-coverage-analysis%2F&r=&lt=1190&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=573874)
