# Source: https://docs.datadoghq.com/api/latest/csm-coverage-analysis.md

---
title: CSM Coverage Analysis
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > CSM Coverage Analysis
---

# CSM Coverage Analysis

Datadog Cloud Security Management (CSM) delivers real-time threat detection and continuous configuration audits across your entire cloud infrastructure, all in a unified view for seamless collaboration and faster remediation. Go to [https://docs.datadoghq.com/security/cloud_security_management](https://docs.datadoghq.com/security/cloud_security_management) to learn more.

## Get the CSM Cloud Accounts Coverage Analysis{% #get-the-csm-cloud-accounts-coverage-analysis %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/csm/onboarding/coverage_analysis/cloud_accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts |

### Overview

Get the CSM Coverage Analysis of your Cloud Accounts. This is calculated based on the number of your Cloud Accounts that are scanned for security issues.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
CSM Cloud Accounts Coverage Analysis response.

| Parent field   | Field                                | Type   | Description                                                                                                     |
| -------------- | ------------------------------------ | ------ | --------------------------------------------------------------------------------------------------------------- |
|                | data                                 | object | CSM Cloud Accounts Coverage Analysis data.                                                                      |
| data           | attributes                           | object | CSM Cloud Accounts Coverage Analysis attributes.                                                                |
| attributes     | aws_coverage                         | object | CSM Coverage Analysis.                                                                                          |
| aws_coverage   | configured_resources_count           | int64  | The number of fully configured resources.                                                                       |
| aws_coverage   | coverage                             | double | The coverage percentage.                                                                                        |
| aws_coverage   | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                   |
| aws_coverage   | total_resources_count                | int64  | The total number of resources.                                                                                  |
| attributes     | azure_coverage                       | object | CSM Coverage Analysis.                                                                                          |
| azure_coverage | configured_resources_count           | int64  | The number of fully configured resources.                                                                       |
| azure_coverage | coverage                             | double | The coverage percentage.                                                                                        |
| azure_coverage | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                   |
| azure_coverage | total_resources_count                | int64  | The total number of resources.                                                                                  |
| attributes     | gcp_coverage                         | object | CSM Coverage Analysis.                                                                                          |
| gcp_coverage   | configured_resources_count           | int64  | The number of fully configured resources.                                                                       |
| gcp_coverage   | coverage                             | double | The coverage percentage.                                                                                        |
| gcp_coverage   | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                   |
| gcp_coverage   | total_resources_count                | int64  | The total number of resources.                                                                                  |
| attributes     | org_id                               | int64  | The ID of your organization.                                                                                    |
| attributes     | total_coverage                       | object | CSM Coverage Analysis.                                                                                          |
| total_coverage | configured_resources_count           | int64  | The number of fully configured resources.                                                                       |
| total_coverage | coverage                             | double | The coverage percentage.                                                                                        |
| total_coverage | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                   |
| total_coverage | total_resources_count                | int64  | The total number of resources.                                                                                  |
| data           | id                                   | string | The ID of your organization.                                                                                    |
| data           | type                                 | string | The type of the resource. The value should always be `get_cloud_accounts_coverage_analysis_response_public_v0`. |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/cloud_accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get the CSM Cloud Accounts Coverage Analysis returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMCoverageAnalysisAPI.new
p api_instance.get_csm_cloud_accounts_coverage_analysis()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get the CSM Hosts and Containers Coverage Analysis{% #get-the-csm-hosts-and-containers-coverage-analysis %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers |

### Overview

Get the CSM Coverage Analysis of your Hosts and Containers. This is calculated based on the number of agents running on your Hosts and Containers with CSM feature(s) enabled.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
CSM Hosts and Containers Coverage Analysis response.

| Parent field   | Field                                | Type   | Description                                                                                                           |
| -------------- | ------------------------------------ | ------ | --------------------------------------------------------------------------------------------------------------------- |
|                | data                                 | object | CSM Hosts and Containers Coverage Analysis data.                                                                      |
| data           | attributes                           | object | CSM Hosts and Containers Coverage Analysis attributes.                                                                |
| attributes     | cspm_coverage                        | object | CSM Coverage Analysis.                                                                                                |
| cspm_coverage  | configured_resources_count           | int64  | The number of fully configured resources.                                                                             |
| cspm_coverage  | coverage                             | double | The coverage percentage.                                                                                              |
| cspm_coverage  | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                         |
| cspm_coverage  | total_resources_count                | int64  | The total number of resources.                                                                                        |
| attributes     | cws_coverage                         | object | CSM Coverage Analysis.                                                                                                |
| cws_coverage   | configured_resources_count           | int64  | The number of fully configured resources.                                                                             |
| cws_coverage   | coverage                             | double | The coverage percentage.                                                                                              |
| cws_coverage   | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                         |
| cws_coverage   | total_resources_count                | int64  | The total number of resources.                                                                                        |
| attributes     | org_id                               | int64  | The ID of your organization.                                                                                          |
| attributes     | total_coverage                       | object | CSM Coverage Analysis.                                                                                                |
| total_coverage | configured_resources_count           | int64  | The number of fully configured resources.                                                                             |
| total_coverage | coverage                             | double | The coverage percentage.                                                                                              |
| total_coverage | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                         |
| total_coverage | total_resources_count                | int64  | The total number of resources.                                                                                        |
| attributes     | vm_coverage                          | object | CSM Coverage Analysis.                                                                                                |
| vm_coverage    | configured_resources_count           | int64  | The number of fully configured resources.                                                                             |
| vm_coverage    | coverage                             | double | The coverage percentage.                                                                                              |
| vm_coverage    | partially_configured_resources_count | int64  | The number of partially configured resources.                                                                         |
| vm_coverage    | total_resources_count                | int64  | The total number of resources.                                                                                        |
| data           | id                                   | string | The ID of your organization.                                                                                          |
| data           | type                                 | string | The type of the resource. The value should always be `get_hosts_and_containers_coverage_analysis_response_public_v0`. |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get the CSM Hosts and Containers Coverage Analysis returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMCoverageAnalysisAPI.new
p api_instance.get_csm_hosts_and_containers_coverage_analysis()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get the CSM Serverless Coverage Analysis{% #get-the-csm-serverless-coverage-analysis %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/csm/onboarding/coverage_analysis/serverless      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/csm/onboarding/coverage_analysis/serverless      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless |

### Overview

Get the CSM Coverage Analysis of your Serverless Resources. This is calculated based on the number of agents running on your Serverless Resources with CSM feature(s) enabled.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
CSM Serverless Resources Coverage Analysis response.

| Parent field   | Field                                | Type   | Description                                                                                                 |
| -------------- | ------------------------------------ | ------ | ----------------------------------------------------------------------------------------------------------- |
|                | data                                 | object | CSM Serverless Resources Coverage Analysis data.                                                            |
| data           | attributes                           | object | CSM Serverless Resources Coverage Analysis attributes.                                                      |
| attributes     | cws_coverage                         | object | CSM Coverage Analysis.                                                                                      |
| cws_coverage   | configured_resources_count           | int64  | The number of fully configured resources.                                                                   |
| cws_coverage   | coverage                             | double | The coverage percentage.                                                                                    |
| cws_coverage   | partially_configured_resources_count | int64  | The number of partially configured resources.                                                               |
| cws_coverage   | total_resources_count                | int64  | The total number of resources.                                                                              |
| attributes     | org_id                               | int64  | The ID of your organization.                                                                                |
| attributes     | total_coverage                       | object | CSM Coverage Analysis.                                                                                      |
| total_coverage | configured_resources_count           | int64  | The number of fully configured resources.                                                                   |
| total_coverage | coverage                             | double | The coverage percentage.                                                                                    |
| total_coverage | partially_configured_resources_count | int64  | The number of partially configured resources.                                                               |
| total_coverage | total_resources_count                | int64  | The total number of resources.                                                                              |
| data           | id                                   | string | The ID of your organization.                                                                                |
| data           | type                                 | string | The type of the resource. The value should always be `get_serverless_coverage_analysis_response_public_v0`. |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
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

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/csm/onboarding/coverage_analysis/serverless" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get the CSM Serverless Coverage Analysis returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CSMCoverageAnalysisAPI.new
p api_instance.get_csm_serverless_coverage_analysis()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
