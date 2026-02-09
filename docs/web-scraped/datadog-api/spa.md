# Source: https://docs.datadoghq.com/api/latest/spa/

# Spa
SPA (Spark Pod Autosizing) API. Provides resource recommendations and cost insights to help optimize Spark job configurations.
## [Get SPA Recommendations with a shard parameter](https://docs.datadoghq.com/api/latest/spa/#get-spa-recommendations-with-a-shard-parameter)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/spa/#get-spa-recommendations-with-a-shard-parameter-v2)


**Note** : This endpoint is in preview and may change in the future. It is not yet recommended for production use.
GET https://api.ap1.datadoghq.com/api/v2/spa/recommendations/{service}/{shard}https://api.ap2.datadoghq.com/api/v2/spa/recommendations/{service}/{shard}https://api.datadoghq.eu/api/v2/spa/recommendations/{service}/{shard}https://api.ddog-gov.com/api/v2/spa/recommendations/{service}/{shard}https://api.datadoghq.com/api/v2/spa/recommendations/{service}/{shard}https://api.us3.datadoghq.com/api/v2/spa/recommendations/{service}/{shard}https://api.us5.datadoghq.com/api/v2/spa/recommendations/{service}/{shard}
### Overview
This endpoint is currently experimental and restricted to Datadog internal use only. Retrieve resource recommendations for a Spark job. The caller (Spark Gateway or DJM UI) provides a service name and shard identifier, and SPA returns structured recommendations for driver and executor resources.
### Arguments
#### Path Parameters
Name
Type
Description
shard [_required_]
string
The shard tag for a spark job, which differentiates jobs within the same service that have different resource needs
service [_required_]
string
The service name for a spark job
#### Query Strings
Name
Type
Description
bypass_cache
string
The recommendation service should not use its metrics cache.
### Response
  * [200](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendationsWithShard-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendationsWithShard-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendationsWithShard-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendationsWithShard-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


Field
Type
Description
data [_required_]
object
JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.
attributes [_required_]
object
Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.
confidence_level
double
driver [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
executor [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
id
string
Resource identifier for the recommendation. Optional in responses.
type [_required_]
enum
JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`
default: `recommendation`
```
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

Copy
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


JSON:API document containing a single Recommendation resource. Returned by SPA when the Spark Gateway requests recommendations.
Field
Type
Description
data [_required_]
object
JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.
attributes [_required_]
object
Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.
confidence_level
double
driver [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
executor [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
id
string
Resource identifier for the recommendation. Optional in responses.
type [_required_]
enum
JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`
default: `recommendation`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


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
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


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
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/spa/?code-lang=curl)


#####  Get SPA Recommendations with a shard parameter
Copy
```
                  # Path parameters  
export shard="CHANGE_ME"  
export service="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spa/recommendations/${service}/${shard}" \
-H "Accept: application/json"  

                
```

* * *
## [Get SPA Recommendations](https://docs.datadoghq.com/api/latest/spa/#get-spa-recommendations)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/spa/#get-spa-recommendations-v2)


**Note** : This endpoint is in preview and may change in the future. It is not yet recommended for production use.
GET https://api.ap1.datadoghq.com/api/v2/spa/recommendations/{service}https://api.ap2.datadoghq.com/api/v2/spa/recommendations/{service}https://api.datadoghq.eu/api/v2/spa/recommendations/{service}https://api.ddog-gov.com/api/v2/spa/recommendations/{service}https://api.datadoghq.com/api/v2/spa/recommendations/{service}https://api.us3.datadoghq.com/api/v2/spa/recommendations/{service}https://api.us5.datadoghq.com/api/v2/spa/recommendations/{service}
### Overview
This endpoint is currently experimental and restricted to Datadog internal use only. Retrieve resource recommendations for a Spark job. The caller (Spark Gateway or DJM UI) provides a service name and SPA returns structured recommendations for driver and executor resources. The version with a shard should be preferred, where possible, as it gives more accurate results.
### Arguments
#### Path Parameters
Name
Type
Description
service [_required_]
string
The service name for a spark job.
#### Query Strings
Name
Type
Description
bypass_cache
string
The recommendation service should not use its metrics cache.
### Response
  * [200](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendations-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendations-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendations-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/spa/#GetSPARecommendations-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


Field
Type
Description
data [_required_]
object
JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.
attributes [_required_]
object
Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.
confidence_level
double
driver [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
executor [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
id
string
Resource identifier for the recommendation. Optional in responses.
type [_required_]
enum
JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`
default: `recommendation`
```
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

Copy
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


JSON:API document containing a single Recommendation resource. Returned by SPA when the Spark Gateway requests recommendations.
Field
Type
Description
data [_required_]
object
JSON:API resource object for SPA Recommendation. Includes type, optional ID, and resource attributes with structured recommendations.
attributes [_required_]
object
Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.
confidence_level
double
driver [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
executor [_required_]
object
Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
estimation [_required_]
object
Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
cpu
object
CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
max
int64
Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
p75
int64
75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
p95
int64
95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
ephemeral_storage
int64
Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
heap
int64
Recommended JVM heap size (in MiB).
memory
int64
Recommended total memory allocation (in MiB). Includes both heap and overhead.
overhead
int64
Recommended JVM overhead (in MiB). Computed as total memory - heap.
id
string
Resource identifier for the recommendation. Optional in responses.
type [_required_]
enum
JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA. Allowed enum values: `recommendation`
default: `recommendation`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


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
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


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
  * [Model](https://docs.datadoghq.com/api/latest/spa/)
  * [Example](https://docs.datadoghq.com/api/latest/spa/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/spa/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/spa/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/spa/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/spa/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/spa/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/spa/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/spa/?code-lang=typescript)


#####  Get SPA Recommendations
Copy
```
                  # Path parameters  
export service="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/spa/recommendations/${service}" \
-H "Accept: application/json"  

                
```

#####  Get SPA Recommendations
```
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
        shard="shard",
        service="service",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" python3 "example.py"


```

#####  Get SPA Recommendations
```
# Get SPA Recommendations returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_spa_recommendations".to_sym] = true
end
api_instance = DatadogAPIClient::V2::SpaAPI.new
p api_instance.get_spa_recommendations("shard", "service")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" rb "example.rb"


```

#####  Get SPA Recommendations
```
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
	resp, r, err := api.GetSPARecommendations(ctx, "shard", "service")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpaApi.GetSPARecommendations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SpaApi.GetSPARecommendations`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" go run "main.go"


```

#####  Get SPA Recommendations
```
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
      RecommendationDocument result = apiInstance.getSPARecommendations("shard", "service");
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" java "Example.java"


```

#####  Get SPA Recommendations
```
// Get SPA Recommendations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spa::SpaAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetSPARecommendations", true);
    let api = SpaAPI::with_config(configuration);
    let resp = api
        .get_spa_recommendations("shard".to_string(), "service".to_string())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" cargo run


```

#####  Get SPA Recommendations
```
/**
 * Get SPA Recommendations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getSPARecommendations"] = true;
const apiInstance = new v2.SpaApi(configuration);

const params: v2.SpaApiGetSPARecommendationsRequest = {
  shard: "shard",
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=f720dfad-c11f-418f-98d4-2c0a0edfee52&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8118000d-b769-4213-8994-2534835ccffb&pt=Spa&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fspa%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=f720dfad-c11f-418f-98d4-2c0a0edfee52&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8118000d-b769-4213-8994-2534835ccffb&pt=Spa&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fspa%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=0c8ada2f-83c9-4be0-88e1-fc57b3f97189&bo=2&sid=ca97aff0f0bf11f0b225ebe7018368cd&vid=ca980060f0bf11f09385b797b877861f&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Spa&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fspa%2F&r=&lt=1047&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=959197)
