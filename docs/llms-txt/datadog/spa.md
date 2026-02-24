# Source: https://docs.datadoghq.com/api/latest/spa.md

---
title: Spa
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Spa
---

# Spa

SPA (Spark Pod Autosizing) API. Provides resource recommendations and cost insights to help optimize Spark job configurations.

## Get SPA Recommendations with a shard parameter{% #get-spa-recommendations-with-a-shard-parameter %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may change in the future. It is not yet recommended for production use.
| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/spa/recommendations/{service}/{shard} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/spa/recommendations/{service}/{shard} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/spa/recommendations/{service}/{shard}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/spa/recommendations/{service}/{shard}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/spa/recommendations/{service}/{shard}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/spa/recommendations/{service}/{shard} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/spa/recommendations/{service}/{shard} |

### Overview

This endpoint is currently experimental and restricted to Datadog internal use only. Retrieve resource recommendations for a Spark job. The caller (Spark Gateway or DJM UI) provides a service name and shard identifier, and SPA returns structured recommendations for driver and executor resources.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                                                                                                         |
| ------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------- |
| shard [*required*]   | string | The shard tag for a spark job, which differentiates jobs within the same service that have different resource needs |
| service [*required*] | string | The service name for a spark job                                                                                    |

#### Query Strings

| Name         | Type   | Description                                                  |
| ------------ | ------ | ------------------------------------------------------------ |
| bypass_cache | string | The recommendation service should not use its metrics cache. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                                                         |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.                               |
| data         | attributes [*required*] | object | Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.                                                    |
| attributes   | confidence_level             | double |
| attributes   | driver [*required*]     | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| driver       | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| attributes   | executor [*required*]   | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| executor     | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| data         | id                           | string | Resource identifier for the recommendation. Optional in responses.                                                                                                  |
| data         | type [*required*]       | enum   | JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "confidence_level": "number",
      "driver": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      },
      "executor": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      }
    },
    "id": "string",
    "type": "recommendation"
  }
}
```

{% /tab %}

{% tab title="Model" %}
JSON:API document containing a single Recommendation resource. Returned by SPA when the Spark Gateway requests recommendations.

| Parent field | Field                        | Type   | Description                                                                                                                                                         |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.                               |
| data         | attributes [*required*] | object | Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.                                                    |
| attributes   | confidence_level             | double |
| attributes   | driver [*required*]     | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| driver       | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| attributes   | executor [*required*]   | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| executor     | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| data         | id                           | string | Resource identifier for the recommendation. Optional in responses.                                                                                                  |
| data         | type [*required*]       | enum   | JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "confidence_level": "number",
      "driver": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      },
      "executor": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      }
    },
    "id": "string",
    "type": "recommendation"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
                  \# Path parametersexport shard="CHANGE_ME"export service="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spa/recommendations/${service}/${shard}" \
-H "Accept: application/json"
                
##### 

```python
"""
Get SPA Recommendations with a shard parameter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spa_api import SpaApi

configuration = Configuration()
configuration.unstable_operations["get_spa_recommendations_with_shard"] = True
with ApiClient(configuration) as api_client:
    api_instance = SpaApi(api_client)
    response = api_instance.get_spa_recommendations_with_shard(
        shard="shard",
        service="service",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" python3 "example.py"
##### 

```ruby
# Get SPA Recommendations with a shard parameter returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_spa_recommendations_with_shard".to_sym] = true
end
api_instance = DatadogAPIClient::V2::SpaAPI.new
p api_instance.get_spa_recommendations_with_shard("shard", "service")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" rb "example.rb"
##### 

```go
// Get SPA Recommendations with a shard parameter returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.GetSPARecommendationsWithShard", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSpaApi(apiClient)
	resp, r, err := api.GetSPARecommendationsWithShard(ctx, "shard", "service", *datadogV2.NewGetSPARecommendationsWithShardOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpaApi.GetSPARecommendationsWithShard`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SpaApi.GetSPARecommendationsWithShard`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" go run "main.go"
##### 

```java
// Get SPA Recommendations with a shard parameter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpaApi;
import com.datadog.api.client.v2.model.RecommendationDocument;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getSPARecommendationsWithShard", true);
    SpaApi apiInstance = new SpaApi(defaultClient);

    try {
      RecommendationDocument result =
          apiInstance.getSPARecommendationsWithShard("shard", "service");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpaApi#getSPARecommendationsWithShard");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" java "Example.java"
##### 

```rust
// Get SPA Recommendations with a shard parameter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spa::GetSPARecommendationsWithShardOptionalParams;
use datadog_api_client::datadogV2::api_spa::SpaAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetSPARecommendationsWithShard", true);
    let api = SpaAPI::with_config(configuration);
    let resp = api
        .get_spa_recommendations_with_shard(
            "shard".to_string(),
            "service".to_string(),
            GetSPARecommendationsWithShardOptionalParams::default(),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" cargo run
##### 

```typescript
/**
 * Get SPA Recommendations with a shard parameter returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getSPARecommendationsWithShard"] = true;
const apiInstance = new v2.SpaApi(configuration);

const params: v2.SpaApiGetSPARecommendationsWithShardRequest = {
  shard: "shard",
  service: "service",
};

apiInstance
  .getSPARecommendationsWithShard(params)
  .then((data: v2.RecommendationDocument) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" tsc "example.ts"
{% /tab %}

## Get SPA Recommendations{% #get-spa-recommendations %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may change in the future. It is not yet recommended for production use.
| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/spa/recommendations/{service} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/spa/recommendations/{service} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/spa/recommendations/{service}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/spa/recommendations/{service}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/spa/recommendations/{service}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/spa/recommendations/{service} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/spa/recommendations/{service} |

### Overview

This endpoint is currently experimental and restricted to Datadog internal use only. Retrieve resource recommendations for a Spark job. The caller (Spark Gateway or DJM UI) provides a service name and SPA returns structured recommendations for driver and executor resources. The version with a shard should be preferred, where possible, as it gives more accurate results.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                       |
| ------------------------- | ------ | --------------------------------- |
| service [*required*] | string | The service name for a spark job. |

#### Query Strings

| Name         | Type   | Description                                                  |
| ------------ | ------ | ------------------------------------------------------------ |
| bypass_cache | string | The recommendation service should not use its metrics cache. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                                                         |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.                               |
| data         | attributes [*required*] | object | Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.                                                    |
| attributes   | confidence_level             | double |
| attributes   | driver [*required*]     | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| driver       | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| attributes   | executor [*required*]   | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| executor     | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| data         | id                           | string | Resource identifier for the recommendation. Optional in responses.                                                                                                  |
| data         | type [*required*]       | enum   | JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "confidence_level": "number",
      "driver": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      },
      "executor": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      }
    },
    "id": "string",
    "type": "recommendation"
  }
}
```

{% /tab %}

{% tab title="Model" %}
JSON:API document containing a single Recommendation resource. Returned by SPA when the Spark Gateway requests recommendations.

| Parent field | Field                        | Type   | Description                                                                                                                                                         |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.                               |
| data         | attributes [*required*] | object | Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.                                                    |
| attributes   | confidence_level             | double |
| attributes   | driver [*required*]     | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| driver       | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| attributes   | executor [*required*]   | object | Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.                                  |
| executor     | estimation [*required*] | object | Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.               |
| estimation   | cpu                          | object | CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles. |
| cpu          | max                          | int64  | Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.                                                          |
| cpu          | p75                          | int64  | 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.                                                    |
| cpu          | p95                          | int64  | 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.                                                        |
| estimation   | ephemeral_storage            | int64  | Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.                                                                     |
| estimation   | heap                         | int64  | Recommended JVM heap size (in MiB).                                                                                                                                 |
| estimation   | memory                       | int64  | Recommended total memory allocation (in MiB). Includes both heap and overhead.                                                                                      |
| estimation   | overhead                     | int64  | Recommended JVM overhead (in MiB). Computed as total memory - heap.                                                                                                 |
| data         | id                           | string | Resource identifier for the recommendation. Optional in responses.                                                                                                  |
| data         | type [*required*]       | enum   | JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "confidence_level": "number",
      "driver": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      },
      "executor": {
        "estimation": {
          "cpu": {
            "max": "integer",
            "p75": "integer",
            "p95": "integer"
          },
          "ephemeral_storage": "integer",
          "heap": "integer",
          "memory": "integer",
          "overhead": "integer"
        }
      }
    },
    "id": "string",
    "type": "recommendation"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
                  \# Path parametersexport service="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spa/recommendations/${service}" \
-H "Accept: application/json"
                
##### 

```python
"""
Get SPA Recommendations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spa_api import SpaApi

configuration = Configuration()
configuration.unstable_operations["get_spa_recommendations"] = True
with ApiClient(configuration) as api_client:
    api_instance = SpaApi(api_client)
    response = api_instance.get_spa_recommendations(
        service="service",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" python3 "example.py"
##### 

```ruby
# Get SPA Recommendations returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_spa_recommendations".to_sym] = true
end
api_instance = DatadogAPIClient::V2::SpaAPI.new
p api_instance.get_spa_recommendations("service")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" rb "example.rb"
##### 

```go
// Get SPA Recommendations returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.GetSPARecommendations", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSpaApi(apiClient)
	resp, r, err := api.GetSPARecommendations(ctx, "service", *datadogV2.NewGetSPARecommendationsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpaApi.GetSPARecommendations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SpaApi.GetSPARecommendations`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" go run "main.go"
##### 

```java
// Get SPA Recommendations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpaApi;
import com.datadog.api.client.v2.model.RecommendationDocument;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getSPARecommendations", true);
    SpaApi apiInstance = new SpaApi(defaultClient);

    try {
      RecommendationDocument result = apiInstance.getSPARecommendations("service");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpaApi#getSPARecommendations");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" java "Example.java"
##### 

```rust
// Get SPA Recommendations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spa::GetSPARecommendationsOptionalParams;
use datadog_api_client::datadogV2::api_spa::SpaAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetSPARecommendations", true);
    let api = SpaAPI::with_config(configuration);
    let resp = api
        .get_spa_recommendations(
            "service".to_string(),
            GetSPARecommendationsOptionalParams::default(),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" cargo run
##### 

```typescript
/**
 * Get SPA Recommendations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getSPARecommendations"] = true;
const apiInstance = new v2.SpaApi(configuration);

const params: v2.SpaApiGetSPARecommendationsRequest = {
  service: "service",
};

apiInstance
  .getSPARecommendations(params)
  .then((data: v2.RecommendationDocument) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" tsc "example.ts"
{% /tab %}
