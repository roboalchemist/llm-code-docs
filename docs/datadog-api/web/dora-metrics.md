# Source: https://docs.datadoghq.com/api/latest/dora-metrics/

# DORA Metrics
Search, send, or delete events for DORA Metrics to measure and improve your software delivery performance. See the [DORA Metrics page](https://docs.datadoghq.com/dora_metrics/) for more information.
**Note** : DORA Metrics are not available in the US1-FED site.
## [Send a deployment event](https://docs.datadoghq.com/api/latest/dora-metrics/#send-a-deployment-event)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#send-a-deployment-event-v2)


POST https://api.ap1.datadoghq.com/api/v2/dora/deploymenthttps://api.ap2.datadoghq.com/api/v2/dora/deploymenthttps://api.datadoghq.eu/api/v2/dora/deploymenthttps://api.ddog-gov.com/api/v2/dora/deploymenthttps://api.datadoghq.com/api/v2/dora/deploymenthttps://api.us3.datadoghq.com/api/v2/dora/deploymenthttps://api.us5.datadoghq.com/api/v2/dora/deployment
### Overview
Use this API endpoint to provide deployment data.
This is necessary for:
  * Deployment Frequency
  * Change Lead Time
  * Change Failure Rate


### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Field
Type
Description
data [_required_]
object
The JSON:API data.
attributes [_required_]
object
Attributes to create a DORA deployment event.
custom_tags
[string]
A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.
env
string
Environment name to where the service was deployed.
finished_at [_required_]
int64
Unix timestamp when the deployment finished. It must be in nanoseconds, milliseconds, or seconds.
git
object
Git info for DORA Metrics events.
commit_sha [_required_]
string
Git Commit SHA.
repository_url [_required_]
string
Git Repository URL
id
string
Deployment ID. Must be 16-128 characters and contain only alphanumeric characters, hyphens, underscores, periods, and colons (a-z, A-Z, 0-9, -, _, ., :).
service [_required_]
string
Service name.
started_at [_required_]
int64
Unix timestamp when the deployment started. It must be in nanoseconds, milliseconds, or seconds.
team
string
Name of the team owning the deployed service. If not provided, this is automatically populated with the team associated with the service in the Service Catalog.
version
string
Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/).
```
{
  "data": {
    "attributes": {
      "finished_at": 1693491984000000000,
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "service": "shopist",
      "started_at": 1693491974000000000,
      "version": "v1.12.07"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORADeployment-200-v2)
  * [202](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORADeployment-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORADeployment-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORADeployment-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORADeployment-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response after receiving a DORA deployment event.
Field
Type
Description
data [_required_]
object
The JSON:API data.
id [_required_]
string
The ID of the received DORA deployment event.
type
enum
JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment`
default: `dora_deployment`
```
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_deployment"
  }
}
```

Copy
OK - but delayed due to incident
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response after receiving a DORA deployment event.
Field
Type
Description
data [_required_]
object
The JSON:API data.
id [_required_]
string
The ID of the received DORA deployment event.
type
enum
JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment`
default: `dora_deployment`
```
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_deployment"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Send a deployment event returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployment" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "finished_at": 1693491984000000000,
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "service": "shopist",
      "started_at": 1693491974000000000,
      "version": "v1.12.07"
    }
  }
}
EOF  

                        
```

#####  Send a deployment event returns "OK" response
```
// Send a deployment event returns "OK" response

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
	body := datadogV2.DORADeploymentRequest{
		Data: datadogV2.DORADeploymentRequestData{
			Attributes: datadogV2.DORADeploymentRequestAttributes{
				FinishedAt: 1693491984000000000,
				Git: &datadogV2.DORAGitInfo{
					CommitSha:     "66adc9350f2cc9b250b69abddab733dd55e1a588",
					RepositoryUrl: "https://github.com/organization/example-repository",
				},
				Service:   "shopist",
				StartedAt: 1693491974000000000,
				Version:   datadog.PtrString("v1.12.07"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDORAMetricsApi(apiClient)
	resp, r, err := api.CreateDORADeployment(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.CreateDORADeployment`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DORAMetricsApi.CreateDORADeployment`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"


```

#####  Send a deployment event returns "OK" response
```
// Send a deployment event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORADeploymentRequest;
import com.datadog.api.client.v2.model.DORADeploymentRequestAttributes;
import com.datadog.api.client.v2.model.DORADeploymentRequestData;
import com.datadog.api.client.v2.model.DORADeploymentResponse;
import com.datadog.api.client.v2.model.DORAGitInfo;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    DORADeploymentRequest body =
        new DORADeploymentRequest()
            .data(
                new DORADeploymentRequestData()
                    .attributes(
                        new DORADeploymentRequestAttributes()
                            .finishedAt(1693491984000000000L)
                            .git(
                                new DORAGitInfo()
                                    .commitSha("66adc9350f2cc9b250b69abddab733dd55e1a588")
                                    .repositoryUrl(
                                        "https://github.com/organization/example-repository"))
                            .service("shopist")
                            .startedAt(1693491974000000000L)
                            .version("v1.12.07")));

    try {
      DORADeploymentResponse result = apiInstance.createDORADeployment(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#createDORADeployment");
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"


```

#####  Send a deployment event returns "OK" response
```
"""
Send a deployment event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_deployment_request import DORADeploymentRequest
from datadog_api_client.v2.model.dora_deployment_request_attributes import DORADeploymentRequestAttributes
from datadog_api_client.v2.model.dora_deployment_request_data import DORADeploymentRequestData
from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

body = DORADeploymentRequest(
    data=DORADeploymentRequestData(
        attributes=DORADeploymentRequestAttributes(
            finished_at=1693491984000000000,
            git=DORAGitInfo(
                commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
                repository_url="https://github.com/organization/example-repository",
            ),
            service="shopist",
            started_at=1693491974000000000,
            version="v1.12.07",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.create_dora_deployment(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"


```

#####  Send a deployment event returns "OK" response
```
# Send a deployment event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new

body = DatadogAPIClient::V2::DORADeploymentRequest.new({
  data: DatadogAPIClient::V2::DORADeploymentRequestData.new({
    attributes: DatadogAPIClient::V2::DORADeploymentRequestAttributes.new({
      finished_at: 1693491984000000000,
      git: DatadogAPIClient::V2::DORAGitInfo.new({
        commit_sha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
        repository_url: "https://github.com/organization/example-repository",
      }),
      service: "shopist",
      started_at: 1693491974000000000,
      version: "v1.12.07",
    }),
  }),
})
p api_instance.create_dora_deployment(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Send a deployment event returns "OK" response
```
// Send a deployment event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;
use datadog_api_client::datadogV2::model::DORADeploymentRequest;
use datadog_api_client::datadogV2::model::DORADeploymentRequestAttributes;
use datadog_api_client::datadogV2::model::DORADeploymentRequestData;
use datadog_api_client::datadogV2::model::DORAGitInfo;

#[tokio::main]
async fn main() {
    let body = DORADeploymentRequest::new(DORADeploymentRequestData::new(
        DORADeploymentRequestAttributes::new(
            1693491984000000000,
            "shopist".to_string(),
            1693491974000000000,
        )
        .git(DORAGitInfo::new(
            "66adc9350f2cc9b250b69abddab733dd55e1a588".to_string(),
            "https://github.com/organization/example-repository".to_string(),
        ))
        .version("v1.12.07".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.create_dora_deployment(body).await;
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run


```

#####  Send a deployment event returns "OK" response
```
/**
 * Send a deployment event returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiCreateDORADeploymentRequest = {
  body: {
    data: {
      attributes: {
        finishedAt: 1693491984000000000,
        git: {
          commitSha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
          repositoryUrl: "https://github.com/organization/example-repository",
        },
        service: "shopist",
        startedAt: 1693491974000000000,
        version: "v1.12.07",
      },
    },
  },
};

apiInstance
  .createDORADeployment(params)
  .then((data: v2.DORADeploymentResponse) => {
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"


```

* * *
## [Send a failure event](https://docs.datadoghq.com/api/latest/dora-metrics/#send-a-failure-event)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#send-a-failure-event-v2)


POST https://api.ap1.datadoghq.com/api/v2/dora/failurehttps://api.ap2.datadoghq.com/api/v2/dora/failurehttps://api.datadoghq.eu/api/v2/dora/failurehttps://api.ddog-gov.com/api/v2/dora/failurehttps://api.datadoghq.com/api/v2/dora/failurehttps://api.us3.datadoghq.com/api/v2/dora/failurehttps://api.us5.datadoghq.com/api/v2/dora/failure
### Overview
Use this API endpoint to provide failure data.
This is necessary for:
  * Change Failure Rate
  * Time to Restore


### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Field
Type
Description
data [_required_]
object
The JSON:API data.
attributes [_required_]
object
Attributes to create a DORA failure event.
custom_tags
[string]
A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.
env
string
Environment name that was impacted by the failure.
finished_at
int64
Unix timestamp when the failure finished. It must be in nanoseconds, milliseconds, or seconds.
git
object
Git info for DORA Metrics events.
commit_sha [_required_]
string
Git Commit SHA.
repository_url [_required_]
string
Git Repository URL
id
string
Failure ID. Must be 16-128 characters and contain only alphanumeric characters, hyphens, underscores, periods, and colons (a-z, A-Z, 0-9, -, _, ., :).
name
string
Failure name.
services
[string]
Service names impacted by the failure. If possible, use names registered in the Service Catalog. Required when the team field is not provided.
severity
string
Failure severity.
started_at [_required_]
int64
Unix timestamp when the failure started. It must be in nanoseconds, milliseconds, or seconds.
team
string
Name of the team owning the services impacted. If possible, use team handles registered in Datadog. Required when the services field is not provided.
version
string
Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/).
```
{
  "data": {
    "attributes": {
      "custom_tags": [
        "language:java",
        "department:engineering"
      ],
      "env": "staging",
      "finished_at": 1693491984000000000,
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "id": "string",
      "name": "Webserver is down failing all requests.",
      "services": [
        "shopist"
      ],
      "severity": "High",
      "started_at": 1693491974000000000,
      "team": "backend",
      "version": "v1.12.07"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAFailure-200-v2)
  * [202](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAFailure-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAFailure-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAFailure-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAFailure-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response after receiving a DORA failure event.
Field
Type
Description
data [_required_]
object
Response after receiving a DORA failure event.
id [_required_]
string
The ID of the received DORA failure event.
type
enum
JSON:API type for DORA failure events. Allowed enum values: `dora_failure`
default: `dora_failure`
```
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

Copy
OK - but delayed due to incident
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response after receiving a DORA failure event.
Field
Type
Description
data [_required_]
object
Response after receiving a DORA failure event.
id [_required_]
string
The ID of the received DORA failure event.
type
enum
JSON:API type for DORA failure events. Allowed enum values: `dora_failure`
default: `dora_failure`
```
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Send a failure event
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failure" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "started_at": 1693491974000000000
    }
  }
}
EOF  

                
```

#####  Send a failure event
```
"""
Send a failure event returns "OK - but delayed due to incident" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_failure_request import DORAFailureRequest
from datadog_api_client.v2.model.dora_failure_request_attributes import DORAFailureRequestAttributes
from datadog_api_client.v2.model.dora_failure_request_data import DORAFailureRequestData
from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

body = DORAFailureRequest(
    data=DORAFailureRequestData(
        attributes=DORAFailureRequestAttributes(
            custom_tags=[
                "language:java",
                "department:engineering",
            ],
            env="staging",
            finished_at=1693491984000000000,
            git=DORAGitInfo(
                commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
                repository_url="https://github.com/organization/example-repository",
            ),
            name="Webserver is down failing all requests.",
            services=[
                "shopist",
            ],
            severity="High",
            started_at=1693491974000000000,
            team="backend",
            version="v1.12.07",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.create_dora_failure(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"


```

#####  Send a failure event
```
# Send a failure event returns "OK - but delayed due to incident" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new

body = DatadogAPIClient::V2::DORAFailureRequest.new({
  data: DatadogAPIClient::V2::DORAFailureRequestData.new({
    attributes: DatadogAPIClient::V2::DORAFailureRequestAttributes.new({
      custom_tags: [
        "language:java",
        "department:engineering",
      ],
      env: "staging",
      finished_at: 1693491984000000000,
      git: DatadogAPIClient::V2::DORAGitInfo.new({
        commit_sha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
        repository_url: "https://github.com/organization/example-repository",
      }),
      name: "Webserver is down failing all requests.",
      services: [
        "shopist",
      ],
      severity: "High",
      started_at: 1693491974000000000,
      team: "backend",
      version: "v1.12.07",
    }),
  }),
})
p api_instance.create_dora_failure(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Send a failure event
```
// Send a failure event returns "OK - but delayed due to incident" response

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
	body := datadogV2.DORAFailureRequest{
		Data: datadogV2.DORAFailureRequestData{
			Attributes: datadogV2.DORAFailureRequestAttributes{
				CustomTags: *datadog.NewNullableList(&[]string{
					"language:java",
					"department:engineering",
				}),
				Env:        datadog.PtrString("staging"),
				FinishedAt: datadog.PtrInt64(1693491984000000000),
				Git: &datadogV2.DORAGitInfo{
					CommitSha:     "66adc9350f2cc9b250b69abddab733dd55e1a588",
					RepositoryUrl: "https://github.com/organization/example-repository",
				},
				Name: datadog.PtrString("Webserver is down failing all requests."),
				Services: []string{
					"shopist",
				},
				Severity:  datadog.PtrString("High"),
				StartedAt: 1693491974000000000,
				Team:      datadog.PtrString("backend"),
				Version:   datadog.PtrString("v1.12.07"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDORAMetricsApi(apiClient)
	resp, r, err := api.CreateDORAFailure(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.CreateDORAFailure`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DORAMetricsApi.CreateDORAFailure`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"


```

#####  Send a failure event
```
// Send a failure event returns "OK - but delayed due to incident" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAFailureRequest;
import com.datadog.api.client.v2.model.DORAFailureRequestAttributes;
import com.datadog.api.client.v2.model.DORAFailureRequestData;
import com.datadog.api.client.v2.model.DORAFailureResponse;
import com.datadog.api.client.v2.model.DORAGitInfo;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    DORAFailureRequest body =
        new DORAFailureRequest()
            .data(
                new DORAFailureRequestData()
                    .attributes(
                        new DORAFailureRequestAttributes()
                            .customTags(Arrays.asList("language:java", "department:engineering"))
                            .env("staging")
                            .finishedAt(1693491984000000000L)
                            .git(
                                new DORAGitInfo()
                                    .commitSha("66adc9350f2cc9b250b69abddab733dd55e1a588")
                                    .repositoryUrl(
                                        "https://github.com/organization/example-repository"))
                            .name("Webserver is down failing all requests.")
                            .services(Collections.singletonList("shopist"))
                            .severity("High")
                            .startedAt(1693491974000000000L)
                            .team("backend")
                            .version("v1.12.07")));

    try {
      DORAFailureResponse result = apiInstance.createDORAFailure(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#createDORAFailure");
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"


```

#####  Send a failure event
```
// Send a failure event returns "OK - but delayed due to incident" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;
use datadog_api_client::datadogV2::model::DORAFailureRequest;
use datadog_api_client::datadogV2::model::DORAFailureRequestAttributes;
use datadog_api_client::datadogV2::model::DORAFailureRequestData;
use datadog_api_client::datadogV2::model::DORAGitInfo;

#[tokio::main]
async fn main() {
    let body = DORAFailureRequest::new(DORAFailureRequestData::new(
        DORAFailureRequestAttributes::new(1693491974000000000)
            .custom_tags(Some(vec![
                "language:java".to_string(),
                "department:engineering".to_string(),
            ]))
            .env("staging".to_string())
            .finished_at(1693491984000000000)
            .git(DORAGitInfo::new(
                "66adc9350f2cc9b250b69abddab733dd55e1a588".to_string(),
                "https://github.com/organization/example-repository".to_string(),
            ))
            .name("Webserver is down failing all requests.".to_string())
            .services(vec!["shopist".to_string()])
            .severity("High".to_string())
            .team("backend".to_string())
            .version("v1.12.07".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.create_dora_failure(body).await;
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run


```

#####  Send a failure event
```
/**
 * Send a failure event returns "OK - but delayed due to incident" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiCreateDORAFailureRequest = {
  body: {
    data: {
      attributes: {
        customTags: ["language:java", "department:engineering"],
        env: "staging",
        finishedAt: 1693491984000000000,
        git: {
          commitSha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
          repositoryUrl: "https://github.com/organization/example-repository",
        },
        name: "Webserver is down failing all requests.",
        services: ["shopist"],
        severity: "High",
        startedAt: 1693491974000000000,
        team: "backend",
        version: "v1.12.07",
      },
    },
  },
};

apiInstance
  .createDORAFailure(params)
  .then((data: v2.DORAFailureResponse) => {
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"


```

* * *
## [Send an incident event](https://docs.datadoghq.com/api/latest/dora-metrics/#send-an-incident-event)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/dora-metrics/#send-an-incident-event-v2)


POST https://api.ap1.datadoghq.com/api/v2/dora/incidenthttps://api.ap2.datadoghq.com/api/v2/dora/incidenthttps://api.datadoghq.eu/api/v2/dora/incidenthttps://api.ddog-gov.com/api/v2/dora/incidenthttps://api.datadoghq.com/api/v2/dora/incidenthttps://api.us3.datadoghq.com/api/v2/dora/incidenthttps://api.us5.datadoghq.com/api/v2/dora/incident
### Overview
**Note** : This endpoint is deprecated. Please use `/api/v2/dora/failure` instead.
Use this API endpoint to provide failure data.
This is necessary for:
  * Change Failure Rate
  * Time to Restore


### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Field
Type
Description
data [_required_]
object
The JSON:API data.
attributes [_required_]
object
Attributes to create a DORA failure event.
custom_tags
[string]
A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.
env
string
Environment name that was impacted by the failure.
finished_at
int64
Unix timestamp when the failure finished. It must be in nanoseconds, milliseconds, or seconds.
git
object
Git info for DORA Metrics events.
commit_sha [_required_]
string
Git Commit SHA.
repository_url [_required_]
string
Git Repository URL
id
string
Failure ID. Must be 16-128 characters and contain only alphanumeric characters, hyphens, underscores, periods, and colons (a-z, A-Z, 0-9, -, _, ., :).
name
string
Failure name.
services
[string]
Service names impacted by the failure. If possible, use names registered in the Service Catalog. Required when the team field is not provided.
severity
string
Failure severity.
started_at [_required_]
int64
Unix timestamp when the failure started. It must be in nanoseconds, milliseconds, or seconds.
team
string
Name of the team owning the services impacted. If possible, use team handles registered in Datadog. Required when the services field is not provided.
version
string
Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/).
```
{
  "data": {
    "attributes": {
      "finished_at": 1707842944600000000,
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "name": "Webserver is down failing all requests",
      "services": [
        "shopist"
      ],
      "severity": "High",
      "started_at": 1707842944500000000,
      "team": "backend",
      "version": "v1.12.07"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAIncident-200-v2)
  * [202](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAIncident-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAIncident-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAIncident-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#CreateDORAIncident-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response after receiving a DORA failure event.
Field
Type
Description
data [_required_]
object
Response after receiving a DORA failure event.
id [_required_]
string
The ID of the received DORA failure event.
type
enum
JSON:API type for DORA failure events. Allowed enum values: `dora_failure`
default: `dora_failure`
```
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

Copy
OK - but delayed due to incident
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response after receiving a DORA failure event.
Field
Type
Description
data [_required_]
object
Response after receiving a DORA failure event.
id [_required_]
string
The ID of the received DORA failure event.
type
enum
JSON:API type for DORA failure events. Allowed enum values: `dora_failure`
default: `dora_failure`
```
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Send a failure event returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/incident" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "finished_at": 1707842944600000000,
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "name": "Webserver is down failing all requests",
      "services": [
        "shopist"
      ],
      "severity": "High",
      "started_at": 1707842944500000000,
      "team": "backend",
      "version": "v1.12.07"
    }
  }
}
EOF  

                        
```

#####  Send a failure event returns "OK" response
```
// Send a failure event returns "OK" response

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
	body := datadogV2.DORAFailureRequest{
		Data: datadogV2.DORAFailureRequestData{
			Attributes: datadogV2.DORAFailureRequestAttributes{
				FinishedAt: datadog.PtrInt64(1707842944600000000),
				Git: &datadogV2.DORAGitInfo{
					CommitSha:     "66adc9350f2cc9b250b69abddab733dd55e1a588",
					RepositoryUrl: "https://github.com/organization/example-repository",
				},
				Name: datadog.PtrString("Webserver is down failing all requests"),
				Services: []string{
					"shopist",
				},
				Severity:  datadog.PtrString("High"),
				StartedAt: 1707842944500000000,
				Team:      datadog.PtrString("backend"),
				Version:   datadog.PtrString("v1.12.07"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDORAMetricsApi(apiClient)
	resp, r, err := api.CreateDORAIncident(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.CreateDORAIncident`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DORAMetricsApi.CreateDORAIncident`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"


```

#####  Send a failure event returns "OK" response
```
// Send a failure event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAFailureRequest;
import com.datadog.api.client.v2.model.DORAFailureRequestAttributes;
import com.datadog.api.client.v2.model.DORAFailureRequestData;
import com.datadog.api.client.v2.model.DORAFailureResponse;
import com.datadog.api.client.v2.model.DORAGitInfo;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    DORAFailureRequest body =
        new DORAFailureRequest()
            .data(
                new DORAFailureRequestData()
                    .attributes(
                        new DORAFailureRequestAttributes()
                            .finishedAt(1707842944600000000L)
                            .git(
                                new DORAGitInfo()
                                    .commitSha("66adc9350f2cc9b250b69abddab733dd55e1a588")
                                    .repositoryUrl(
                                        "https://github.com/organization/example-repository"))
                            .name("Webserver is down failing all requests")
                            .services(Collections.singletonList("shopist"))
                            .severity("High")
                            .startedAt(1707842944500000000L)
                            .team("backend")
                            .version("v1.12.07")));

    try {
      DORAFailureResponse result = apiInstance.createDORAIncident(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#createDORAIncident");
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"


```

#####  Send a failure event returns "OK" response
```
"""
Send a failure event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_failure_request import DORAFailureRequest
from datadog_api_client.v2.model.dora_failure_request_attributes import DORAFailureRequestAttributes
from datadog_api_client.v2.model.dora_failure_request_data import DORAFailureRequestData
from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

body = DORAFailureRequest(
    data=DORAFailureRequestData(
        attributes=DORAFailureRequestAttributes(
            finished_at=1707842944600000000,
            git=DORAGitInfo(
                commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
                repository_url="https://github.com/organization/example-repository",
            ),
            name="Webserver is down failing all requests",
            services=[
                "shopist",
            ],
            severity="High",
            started_at=1707842944500000000,
            team="backend",
            version="v1.12.07",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.create_dora_incident(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"


```

#####  Send a failure event returns "OK" response
```
# Send a failure event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new

body = DatadogAPIClient::V2::DORAFailureRequest.new({
  data: DatadogAPIClient::V2::DORAFailureRequestData.new({
    attributes: DatadogAPIClient::V2::DORAFailureRequestAttributes.new({
      finished_at: 1707842944600000000,
      git: DatadogAPIClient::V2::DORAGitInfo.new({
        commit_sha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
        repository_url: "https://github.com/organization/example-repository",
      }),
      name: "Webserver is down failing all requests",
      services: [
        "shopist",
      ],
      severity: "High",
      started_at: 1707842944500000000,
      team: "backend",
      version: "v1.12.07",
    }),
  }),
})
p api_instance.create_dora_incident(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Send a failure event returns "OK" response
```
// Send a failure event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;
use datadog_api_client::datadogV2::model::DORAFailureRequest;
use datadog_api_client::datadogV2::model::DORAFailureRequestAttributes;
use datadog_api_client::datadogV2::model::DORAFailureRequestData;
use datadog_api_client::datadogV2::model::DORAGitInfo;

#[tokio::main]
async fn main() {
    let body = DORAFailureRequest::new(DORAFailureRequestData::new(
        DORAFailureRequestAttributes::new(1707842944500000000)
            .finished_at(1707842944600000000)
            .git(DORAGitInfo::new(
                "66adc9350f2cc9b250b69abddab733dd55e1a588".to_string(),
                "https://github.com/organization/example-repository".to_string(),
            ))
            .name("Webserver is down failing all requests".to_string())
            .services(vec!["shopist".to_string()])
            .severity("High".to_string())
            .team("backend".to_string())
            .version("v1.12.07".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.create_dora_incident(body).await;
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run


```

#####  Send a failure event returns "OK" response
```
/**
 * Send a failure event returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiCreateDORAIncidentRequest = {
  body: {
    data: {
      attributes: {
        finishedAt: 1707842944600000000,
        git: {
          commitSha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
          repositoryUrl: "https://github.com/organization/example-repository",
        },
        name: "Webserver is down failing all requests",
        services: ["shopist"],
        severity: "High",
        startedAt: 1707842944500000000,
        team: "backend",
        version: "v1.12.07",
      },
    },
  },
};

apiInstance
  .createDORAIncident(params)
  .then((data: v2.DORAFailureResponse) => {
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"


```

* * *
## [Get a list of deployment events](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-list-of-deployment-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-list-of-deployment-events-v2)


POST https://api.ap1.datadoghq.com/api/v2/dora/deploymentshttps://api.ap2.datadoghq.com/api/v2/dora/deploymentshttps://api.datadoghq.eu/api/v2/dora/deploymentshttps://api.ddog-gov.com/api/v2/dora/deploymentshttps://api.datadoghq.com/api/v2/dora/deploymentshttps://api.us3.datadoghq.com/api/v2/dora/deploymentshttps://api.us5.datadoghq.com/api/v2/dora/deployments
### Overview
Use this API endpoint to get a list of deployment events. This endpoint requires the `dora_metrics_read` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Field
Type
Description
data [_required_]
object
The JSON:API data.
attributes [_required_]
object
Attributes to get a list of deployments.
from
date-time
Minimum timestamp for requested events.
limit
int32
Maximum number of events in the response.
default: `10`
query
string
Search query with event platform syntax.
sort
string
Sort order (prefixed with `-` for descending).
to
date-time
Maximum timestamp for requested events.
type
enum
The definition of `DORAListDeploymentsRequestDataType` object. Allowed enum values: `dora_deployments_list_request`
default: `dora_deployments_list_request`
```
{
  "data": {
    "attributes": {
      "from": "2025-01-01T00:00:00Z",
      "limit": 500,
      "query": "service:(shopist OR api-service OR payment-service) env:(production OR staging) team:(backend OR platform)",
      "sort": "-started_at",
      "to": "2025-01-31T23:59:59Z"
    },
    "type": "dora_deployments_list_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORADeployments-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORADeployments-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORADeployments-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORADeployments-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response for the list deployments endpoint.
Field
Type
Description
data
[object]
The list of DORA deployment events.
attributes
object
The attributes of the deployment event.
custom_tags
[string]
A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.
env
string
Environment name to where the service was deployed.
finished_at [_required_]
int64
Unix timestamp when the deployment finished.
git
object
Git info for DORA Metrics events.
commit_sha [_required_]
string
Git Commit SHA.
repository_url [_required_]
string
Git Repository URL
service [_required_]
string
Service name.
started_at [_required_]
int64
Unix timestamp when the deployment started.
team
string
Name of the team owning the deployed service.
version
string
Version to correlate with APM Deployment Tracking.
id
string
The ID of the deployment event.
type
enum
JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment`
default: `dora_deployment`
```
{
  "data": [
    {
      "attributes": {
        "custom_tags": [
          "language:java",
          "department:engineering",
          "region:us-east-1"
        ],
        "env": "production",
        "finished_at": 1693491984000000000,
        "git": {
          "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
          "repository_url": "https://github.com/organization/example-repository"
        },
        "service": "shopist",
        "started_at": 1693491974000000000,
        "team": "backend",
        "version": "v1.12.07"
      },
      "id": "4242fcdd31586083",
      "type": "dora_deployment"
    },
    {
      "attributes": {
        "custom_tags": [
          "language:go",
          "department:platform"
        ],
        "env": "production",
        "finished_at": 1693492084000000000,
        "git": {
          "commit_sha": "77bdc9350f2cc9b250b69abddab733dd55e1a599",
          "repository_url": "https://github.com/organization/api-service"
        },
        "service": "api-service",
        "started_at": 1693492074000000000,
        "team": "backend",
        "version": "v2.1.0"
      },
      "id": "4242fcdd31586084",
      "type": "dora_deployment"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Get a list of deployment events
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployments" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {}
  }
}
EOF  

                
```

#####  Get a list of deployment events
```
"""
Get a list of deployment events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_list_deployments_request import DORAListDeploymentsRequest
from datadog_api_client.v2.model.dora_list_deployments_request_attributes import DORAListDeploymentsRequestAttributes
from datadog_api_client.v2.model.dora_list_deployments_request_data import DORAListDeploymentsRequestData
from datadog_api_client.v2.model.dora_list_deployments_request_data_type import DORAListDeploymentsRequestDataType
from datetime import datetime
from dateutil.tz import tzutc

body = DORAListDeploymentsRequest(
    data=DORAListDeploymentsRequestData(
        attributes=DORAListDeploymentsRequestAttributes(
            _from=datetime(2025, 3, 23, 0, 0, tzinfo=tzutc()),
            limit=1,
            to=datetime(2025, 3, 24, 0, 0, tzinfo=tzutc()),
        ),
        type=DORAListDeploymentsRequestDataType.DORA_DEPLOYMENTS_LIST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.list_dora_deployments(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of deployment events
```
# Get a list of deployment events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new

body = DatadogAPIClient::V2::DORAListDeploymentsRequest.new({
  data: DatadogAPIClient::V2::DORAListDeploymentsRequestData.new({
    attributes: DatadogAPIClient::V2::DORAListDeploymentsRequestAttributes.new({
      from: "2025-03-23T00:00:00Z",
      limit: 1,
      to: "2025-03-24T00:00:00Z",
    }),
    type: DatadogAPIClient::V2::DORAListDeploymentsRequestDataType::DORA_DEPLOYMENTS_LIST_REQUEST,
  }),
})
p api_instance.list_dora_deployments(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of deployment events
```
// Get a list of deployment events returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.DORAListDeploymentsRequest{
		Data: datadogV2.DORAListDeploymentsRequestData{
			Attributes: datadogV2.DORAListDeploymentsRequestAttributes{
				From:  datadog.PtrTime(time.Date(2025, 3, 23, 0, 0, 0, 0, time.UTC)),
				Limit: datadog.PtrInt32(1),
				To:    datadog.PtrTime(time.Date(2025, 3, 24, 0, 0, 0, 0, time.UTC)),
			},
			Type: datadogV2.DORALISTDEPLOYMENTSREQUESTDATATYPE_DORA_DEPLOYMENTS_LIST_REQUEST.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDORAMetricsApi(apiClient)
	resp, r, err := api.ListDORADeployments(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.ListDORADeployments`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DORAMetricsApi.ListDORADeployments`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of deployment events
```
// Get a list of deployment events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequest;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequestAttributes;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequestData;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequestDataType;
import com.datadog.api.client.v2.model.DORAListResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    DORAListDeploymentsRequest body =
        new DORAListDeploymentsRequest()
            .data(
                new DORAListDeploymentsRequestData()
                    .attributes(
                        new DORAListDeploymentsRequestAttributes()
                            .from(OffsetDateTime.parse("2025-03-23T00:00:00Z"))
                            .limit(1)
                            .to(OffsetDateTime.parse("2025-03-24T00:00:00Z")))
                    .type(DORAListDeploymentsRequestDataType.DORA_DEPLOYMENTS_LIST_REQUEST));

    try {
      DORAListResponse result = apiInstance.listDORADeployments(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#listDORADeployments");
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

#####  Get a list of deployment events
```
// Get a list of deployment events returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;
use datadog_api_client::datadogV2::model::DORAListDeploymentsRequest;
use datadog_api_client::datadogV2::model::DORAListDeploymentsRequestAttributes;
use datadog_api_client::datadogV2::model::DORAListDeploymentsRequestData;
use datadog_api_client::datadogV2::model::DORAListDeploymentsRequestDataType;

#[tokio::main]
async fn main() {
    let body = DORAListDeploymentsRequest::new(
        DORAListDeploymentsRequestData::new(
            DORAListDeploymentsRequestAttributes::new()
                .from(
                    DateTime::parse_from_rfc3339("2025-03-23T00:00:00+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .limit(1)
                .to(DateTime::parse_from_rfc3339("2025-03-24T00:00:00+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc)),
        )
        .type_(DORAListDeploymentsRequestDataType::DORA_DEPLOYMENTS_LIST_REQUEST),
    );
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.list_dora_deployments(body).await;
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

#####  Get a list of deployment events
```
/**
 * Get a list of deployment events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiListDORADeploymentsRequest = {
  body: {
    data: {
      attributes: {
        from: new Date(2025, 3, 23, 0, 0, 0, 0),
        limit: 1,
        to: new Date(2025, 3, 24, 0, 0, 0, 0),
      },
      type: "dora_deployments_list_request",
    },
  },
};

apiInstance
  .listDORADeployments(params)
  .then((data: v2.DORAListResponse) => {
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
## [Get a list of failure events](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-list-of-failure-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-list-of-failure-events-v2)


POST https://api.ap1.datadoghq.com/api/v2/dora/failureshttps://api.ap2.datadoghq.com/api/v2/dora/failureshttps://api.datadoghq.eu/api/v2/dora/failureshttps://api.ddog-gov.com/api/v2/dora/failureshttps://api.datadoghq.com/api/v2/dora/failureshttps://api.us3.datadoghq.com/api/v2/dora/failureshttps://api.us5.datadoghq.com/api/v2/dora/failures
### Overview
Use this API endpoint to get a list of failure events. This endpoint requires the `dora_metrics_read` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Field
Type
Description
data [_required_]
object
The JSON:API data.
attributes [_required_]
object
Attributes to get a list of failures.
from
date-time
Minimum timestamp for requested events.
limit
int32
Maximum number of events in the response.
default: `10`
query
string
Search query with event platform syntax.
sort
string
Sort order (prefixed with `-` for descending).
to
date-time
Maximum timestamp for requested events.
type
enum
The definition of `DORAListFailuresRequestDataType` object. Allowed enum values: `dora_failures_list_request`
default: `dora_failures_list_request`
```
{
  "data": {
    "attributes": {
      "from": "2025-01-01T00:00:00Z",
      "limit": 500,
      "query": "severity:(SEV-1 OR SEV-2) env:(production OR staging) service:(shopist OR api-service OR payment-service) team:(backend OR platform OR payments)",
      "sort": "-started_at",
      "to": "2025-01-31T23:59:59Z"
    },
    "type": "dora_failures_list_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORAFailures-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORAFailures-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORAFailures-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#ListDORAFailures-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response for the list failures endpoint.
Field
Type
Description
data
[object]
The list of DORA incident events.
attributes
object
The attributes of the incident event.
custom_tags
[string]
A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.
env
string
Environment name that was impacted by the incident.
finished_at
int64
Unix timestamp when the incident finished.
git
object
Git info for DORA Metrics events.
commit_sha [_required_]
string
Git Commit SHA.
repository_url [_required_]
string
Git Repository URL
name
string
Incident name.
services
[string]
Service names impacted by the incident.
severity
string
Incident severity.
started_at [_required_]
int64
Unix timestamp when the incident started.
team
string
Name of the team owning the services impacted.
version
string
Version to correlate with APM Deployment Tracking.
id
string
The ID of the incident event.
type
enum
JSON:API type for DORA failure events. Allowed enum values: `dora_failure`
default: `dora_failure`
```
{
  "data": [
    {
      "attributes": {
        "custom_tags": [
          "incident_type:database",
          "department:engineering"
        ],
        "env": "production",
        "finished_at": 1693492274000000000,
        "name": "Database outage",
        "services": [
          "shopist"
        ],
        "severity": "SEV-1",
        "started_at": 1693492174000000000,
        "team": "backend"
      },
      "id": "4242fcdd31586085",
      "type": "dora_incident"
    },
    {
      "attributes": {
        "custom_tags": [
          "incident_type:service_down",
          "department:platform"
        ],
        "env": "production",
        "finished_at": 1693492474000000000,
        "name": "API service outage",
        "services": [
          "api-service",
          "payment-service"
        ],
        "severity": "SEV-2",
        "started_at": 1693492374000000000,
        "team": "backend"
      },
      "id": "4242fcdd31586086",
      "type": "dora_incident"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Get a list of failure events
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failures" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {}
  }
}
EOF  

                
```

#####  Get a list of failure events
```
"""
Get a list of failure events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_list_failures_request import DORAListFailuresRequest
from datadog_api_client.v2.model.dora_list_failures_request_attributes import DORAListFailuresRequestAttributes
from datadog_api_client.v2.model.dora_list_failures_request_data import DORAListFailuresRequestData
from datadog_api_client.v2.model.dora_list_failures_request_data_type import DORAListFailuresRequestDataType
from datetime import datetime
from dateutil.tz import tzutc

body = DORAListFailuresRequest(
    data=DORAListFailuresRequestData(
        attributes=DORAListFailuresRequestAttributes(
            _from=datetime(2025, 3, 23, 0, 0, tzinfo=tzutc()),
            limit=1,
            to=datetime(2025, 3, 24, 0, 0, tzinfo=tzutc()),
        ),
        type=DORAListFailuresRequestDataType.DORA_FAILURES_LIST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.list_dora_failures(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of failure events
```
# Get a list of failure events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new

body = DatadogAPIClient::V2::DORAListFailuresRequest.new({
  data: DatadogAPIClient::V2::DORAListFailuresRequestData.new({
    attributes: DatadogAPIClient::V2::DORAListFailuresRequestAttributes.new({
      from: "2025-03-23T00:00:00Z",
      limit: 1,
      to: "2025-03-24T00:00:00Z",
    }),
    type: DatadogAPIClient::V2::DORAListFailuresRequestDataType::DORA_FAILURES_LIST_REQUEST,
  }),
})
p api_instance.list_dora_failures(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of failure events
```
// Get a list of failure events returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.DORAListFailuresRequest{
		Data: datadogV2.DORAListFailuresRequestData{
			Attributes: datadogV2.DORAListFailuresRequestAttributes{
				From:  datadog.PtrTime(time.Date(2025, 3, 23, 0, 0, 0, 0, time.UTC)),
				Limit: datadog.PtrInt32(1),
				To:    datadog.PtrTime(time.Date(2025, 3, 24, 0, 0, 0, 0, time.UTC)),
			},
			Type: datadogV2.DORALISTFAILURESREQUESTDATATYPE_DORA_FAILURES_LIST_REQUEST.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDORAMetricsApi(apiClient)
	resp, r, err := api.ListDORAFailures(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.ListDORAFailures`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DORAMetricsApi.ListDORAFailures`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of failure events
```
// Get a list of failure events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAListFailuresRequest;
import com.datadog.api.client.v2.model.DORAListFailuresRequestAttributes;
import com.datadog.api.client.v2.model.DORAListFailuresRequestData;
import com.datadog.api.client.v2.model.DORAListFailuresRequestDataType;
import com.datadog.api.client.v2.model.DORAListResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    DORAListFailuresRequest body =
        new DORAListFailuresRequest()
            .data(
                new DORAListFailuresRequestData()
                    .attributes(
                        new DORAListFailuresRequestAttributes()
                            .from(OffsetDateTime.parse("2025-03-23T00:00:00Z"))
                            .limit(1)
                            .to(OffsetDateTime.parse("2025-03-24T00:00:00Z")))
                    .type(DORAListFailuresRequestDataType.DORA_FAILURES_LIST_REQUEST));

    try {
      DORAListResponse result = apiInstance.listDORAFailures(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#listDORAFailures");
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

#####  Get a list of failure events
```
// Get a list of failure events returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;
use datadog_api_client::datadogV2::model::DORAListFailuresRequest;
use datadog_api_client::datadogV2::model::DORAListFailuresRequestAttributes;
use datadog_api_client::datadogV2::model::DORAListFailuresRequestData;
use datadog_api_client::datadogV2::model::DORAListFailuresRequestDataType;

#[tokio::main]
async fn main() {
    let body = DORAListFailuresRequest::new(
        DORAListFailuresRequestData::new(
            DORAListFailuresRequestAttributes::new()
                .from(
                    DateTime::parse_from_rfc3339("2025-03-23T00:00:00+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .limit(1)
                .to(DateTime::parse_from_rfc3339("2025-03-24T00:00:00+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc)),
        )
        .type_(DORAListFailuresRequestDataType::DORA_FAILURES_LIST_REQUEST),
    );
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.list_dora_failures(body).await;
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

#####  Get a list of failure events
```
/**
 * Get a list of failure events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiListDORAFailuresRequest = {
  body: {
    data: {
      attributes: {
        from: new Date(2025, 3, 23, 0, 0, 0, 0),
        limit: 1,
        to: new Date(2025, 3, 24, 0, 0, 0, 0),
      },
      type: "dora_failures_list_request",
    },
  },
};

apiInstance
  .listDORAFailures(params)
  .then((data: v2.DORAListResponse) => {
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
## [Get a deployment event](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-deployment-event)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-deployment-event-v2)


GET https://api.ap1.datadoghq.com/api/v2/dora/deployments/{deployment_id}https://api.ap2.datadoghq.com/api/v2/dora/deployments/{deployment_id}https://api.datadoghq.eu/api/v2/dora/deployments/{deployment_id}https://api.ddog-gov.com/api/v2/dora/deployments/{deployment_id}https://api.datadoghq.com/api/v2/dora/deployments/{deployment_id}https://api.us3.datadoghq.com/api/v2/dora/deployments/{deployment_id}https://api.us5.datadoghq.com/api/v2/dora/deployments/{deployment_id}
### Overview
Use this API endpoint to get a deployment event. This endpoint requires the `dora_metrics_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
deployment_id [_required_]
string
The ID of the deployment event.
### Response
  * [200](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORADeployment-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORADeployment-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORADeployment-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORADeployment-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response for fetching a single deployment event.
Field
Type
Description
data
object
A DORA deployment event.
attributes
object
The attributes of the deployment event.
custom_tags
[string]
A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.
env
string
Environment name to where the service was deployed.
finished_at [_required_]
int64
Unix timestamp when the deployment finished.
git
object
Git info for DORA Metrics events.
commit_sha [_required_]
string
Git Commit SHA.
repository_url [_required_]
string
Git Repository URL
service [_required_]
string
Service name.
started_at [_required_]
int64
Unix timestamp when the deployment started.
team
string
Name of the team owning the deployed service.
version
string
Version to correlate with APM Deployment Tracking.
id
string
The ID of the deployment event.
type
enum
JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment`
default: `dora_deployment`
```
{
  "data": {
    "attributes": {
      "custom_tags": [
        "language:java",
        "department:engineering"
      ],
      "env": "production",
      "finished_at": 1693491984000000000,
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "service": "shopist",
      "started_at": 1693491974000000000,
      "team": "backend",
      "version": "v1.12.07"
    },
    "id": "string",
    "type": "dora_deployment"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Get a deployment event
Copy
```
                  # Path parameters  
export deployment_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployments/${deployment_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a deployment event
```
"""
Get a deployment event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.get_dora_deployment(
        deployment_id="deployment_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a deployment event
```
# Get a deployment event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.get_dora_deployment("deployment_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a deployment event
```
// Get a deployment event returns "OK" response

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
	api := datadogV2.NewDORAMetricsApi(apiClient)
	resp, r, err := api.GetDORADeployment(ctx, "deployment_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.GetDORADeployment`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DORAMetricsApi.GetDORADeployment`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a deployment event
```
// Get a deployment event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAFetchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    try {
      DORAFetchResponse result = apiInstance.getDORADeployment("deployment_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#getDORADeployment");
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

#####  Get a deployment event
```
// Get a deployment event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.get_dora_deployment("deployment_id".to_string()).await;
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

#####  Get a deployment event
```
/**
 * Get a deployment event returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiGetDORADeploymentRequest = {
  deploymentId: "deployment_id",
};

apiInstance
  .getDORADeployment(params)
  .then((data: v2.DORAFetchResponse) => {
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
## [Get a failure event](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-failure-event)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#get-a-failure-event-v2)


GET https://api.ap1.datadoghq.com/api/v2/dora/failures/{failure_id}https://api.ap2.datadoghq.com/api/v2/dora/failures/{failure_id}https://api.datadoghq.eu/api/v2/dora/failures/{failure_id}https://api.ddog-gov.com/api/v2/dora/failures/{failure_id}https://api.datadoghq.com/api/v2/dora/failures/{failure_id}https://api.us3.datadoghq.com/api/v2/dora/failures/{failure_id}https://api.us5.datadoghq.com/api/v2/dora/failures/{failure_id}
### Overview
Use this API endpoint to get a failure event. This endpoint requires the `dora_metrics_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
failure_id [_required_]
string
The ID of the failure event.
### Response
  * [200](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORAFailure-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORAFailure-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORAFailure-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#GetDORAFailure-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


Response for fetching a single failure event.
Field
Type
Description
data
object
A DORA incident event.
attributes
object
The attributes of the incident event.
custom_tags
[string]
A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.
env
string
Environment name that was impacted by the incident.
finished_at
int64
Unix timestamp when the incident finished.
git
object
Git info for DORA Metrics events.
commit_sha [_required_]
string
Git Commit SHA.
repository_url [_required_]
string
Git Repository URL
name
string
Incident name.
services
[string]
Service names impacted by the incident.
severity
string
Incident severity.
started_at [_required_]
int64
Unix timestamp when the incident started.
team
string
Name of the team owning the services impacted.
version
string
Version to correlate with APM Deployment Tracking.
id
string
The ID of the incident event.
type
enum
JSON:API type for DORA failure events. Allowed enum values: `dora_failure`
default: `dora_failure`
```
{
  "data": {
    "attributes": {
      "custom_tags": [
        "language:java",
        "department:engineering"
      ],
      "env": "production",
      "finished_at": 1693491984000000000,
      "git": {
        "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
        "repository_url": "https://github.com/organization/example-repository"
      },
      "name": "Database outage",
      "services": [
        "shopist"
      ],
      "severity": "SEV-1",
      "started_at": 1693491974000000000,
      "team": "backend",
      "version": "v1.12.07"
    },
    "id": "string",
    "type": "dora_failure"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Get a failure event
Copy
```
                  # Path parameters  
export failure_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failures/${failure_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a failure event
```
"""
Get a failure event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.get_dora_failure(
        failure_id="failure_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a failure event
```
# Get a failure event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.get_dora_failure("failure_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a failure event
```
// Get a failure event returns "OK" response

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
	api := datadogV2.NewDORAMetricsApi(apiClient)
	resp, r, err := api.GetDORAFailure(ctx, "failure_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.GetDORAFailure`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DORAMetricsApi.GetDORAFailure`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a failure event
```
// Get a failure event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAFetchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    try {
      DORAFetchResponse result = apiInstance.getDORAFailure("failure_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#getDORAFailure");
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

#####  Get a failure event
```
// Get a failure event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.get_dora_failure("failure_id".to_string()).await;
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

#####  Get a failure event
```
/**
 * Get a failure event returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiGetDORAFailureRequest = {
  failureId: "failure_id",
};

apiInstance
  .getDORAFailure(params)
  .then((data: v2.DORAFetchResponse) => {
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
## [Delete a failure event](https://docs.datadoghq.com/api/latest/dora-metrics/#delete-a-failure-event)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#delete-a-failure-event-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/dora/failure/{failure_id}https://api.ap2.datadoghq.com/api/v2/dora/failure/{failure_id}https://api.datadoghq.eu/api/v2/dora/failure/{failure_id}https://api.ddog-gov.com/api/v2/dora/failure/{failure_id}https://api.datadoghq.com/api/v2/dora/failure/{failure_id}https://api.us3.datadoghq.com/api/v2/dora/failure/{failure_id}https://api.us5.datadoghq.com/api/v2/dora/failure/{failure_id}
### Overview
Use this API endpoint to delete a failure event. This endpoint requires the `dora_metrics_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
failure_id [_required_]
string
The ID of the failure event to delete.
### Response
  * [202](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORAFailure-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORAFailure-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORAFailure-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORAFailure-429-v2)


Accepted
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Delete a failure event
Copy
```
                  # Path parameters  
export failure_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failure/${failure_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a failure event
```
"""
Delete a failure event returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    api_instance.delete_dora_failure(
        failure_id="NO_VALUE",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a failure event
```
# Delete a failure event returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.delete_dora_failure("NO_VALUE")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a failure event
```
// Delete a failure event returns "Accepted" response

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
	api := datadogV2.NewDORAMetricsApi(apiClient)
	r, err := api.DeleteDORAFailure(ctx, "NO_VALUE")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.DeleteDORAFailure`: %v\n", err)
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

#####  Delete a failure event
```
// Delete a failure event returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    try {
      apiInstance.deleteDORAFailure("NO_VALUE");
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#deleteDORAFailure");
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

#####  Delete a failure event
```
// Delete a failure event returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.delete_dora_failure("NO_VALUE".to_string()).await;
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

#####  Delete a failure event
```
/**
 * Delete a failure event returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiDeleteDORAFailureRequest = {
  failureId: "NO_VALUE",
};

apiInstance
  .deleteDORAFailure(params)
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
## [Delete a deployment event](https://docs.datadoghq.com/api/latest/dora-metrics/#delete-a-deployment-event)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dora-metrics/#delete-a-deployment-event-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/dora/deployment/{deployment_id}https://api.ap2.datadoghq.com/api/v2/dora/deployment/{deployment_id}https://api.datadoghq.eu/api/v2/dora/deployment/{deployment_id}https://api.ddog-gov.com/api/v2/dora/deployment/{deployment_id}https://api.datadoghq.com/api/v2/dora/deployment/{deployment_id}https://api.us3.datadoghq.com/api/v2/dora/deployment/{deployment_id}https://api.us5.datadoghq.com/api/v2/dora/deployment/{deployment_id}
### Overview
Use this API endpoint to delete a deployment event. This endpoint requires the `dora_metrics_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
deployment_id [_required_]
string
The ID of the deployment event to delete.
### Response
  * [202](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORADeployment-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORADeployment-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORADeployment-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/dora-metrics/#DeleteDORADeployment-429-v2)


Accepted
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/dora-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/dora-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dora-metrics/?code-lang=typescript)


#####  Delete a deployment event
Copy
```
                  # Path parameters  
export deployment_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployment/${deployment_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a deployment event
```
"""
Delete a deployment event returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    api_instance.delete_dora_deployment(
        deployment_id="NO_VALUE",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a deployment event
```
# Delete a deployment event returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.delete_dora_deployment("NO_VALUE")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a deployment event
```
// Delete a deployment event returns "Accepted" response

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
	api := datadogV2.NewDORAMetricsApi(apiClient)
	r, err := api.DeleteDORADeployment(ctx, "NO_VALUE")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.DeleteDORADeployment`: %v\n", err)
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

#####  Delete a deployment event
```
// Delete a deployment event returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    try {
      apiInstance.deleteDORADeployment("NO_VALUE");
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#deleteDORADeployment");
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

#####  Delete a deployment event
```
// Delete a deployment event returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api.delete_dora_deployment("NO_VALUE".to_string()).await;
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

#####  Delete a deployment event
```
/**
 * Delete a deployment event returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiDeleteDORADeploymentRequest = {
  deploymentId: "NO_VALUE",
};

apiInstance
  .deleteDORADeployment(params)
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=07b74464-a1f6-465c-891d-728892261d90&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=1a019bde-1452-4d90-8b07-4b24923cc14f&pt=DORA%20Metrics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdora-metrics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=07b74464-a1f6-465c-891d-728892261d90&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=1a019bde-1452-4d90-8b07-4b24923cc14f&pt=DORA%20Metrics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdora-metrics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=e399b277-ad13-4b52-a5a3-2066b702457d&bo=2&sid=a619e810f0bf11f09cfddf8eecd6685c&vid=a61a4b10f0bf11f0bf527f4b7489ac07&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=DORA%20Metrics&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdora-metrics%2F&r=&lt=2206&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=86032)
