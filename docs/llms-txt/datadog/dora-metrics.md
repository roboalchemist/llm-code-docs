# Source: https://docs.datadoghq.com/api/latest/dora-metrics.md

---
title: DORA Metrics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > DORA Metrics
---

# DORA Metrics

Search, send, or delete events for DORA Metrics to measure and improve your software delivery performance. See the [DORA Metrics page](https://docs.datadoghq.com/dora_metrics/) for more information.

**Note**: DORA Metrics are not available in the US1-FED site.

## Send a deployment event{% #send-a-deployment-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/dora/deployment |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/dora/deployment |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/dora/deployment      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/dora/deployment      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/dora/deployment     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/dora/deployment |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/dora/deployment |

### Overview

Use this API endpoint to provide deployment data.

This is necessary for:

- Deployment Frequency
- Change Lead Time
- Change Failure Rate

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                            | Type     | Description                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]           | object   | The JSON:API data.                                                                                                                                               |
| data         | attributes [*required*]     | object   | Attributes to create a DORA deployment event.                                                                                                                    |
| attributes   | custom_tags                      | [string] | A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.                                                     |
| attributes   | env                              | string   | Environment name to where the service was deployed.                                                                                                              |
| attributes   | finished_at [*required*]    | int64    | Unix timestamp when the deployment finished. It must be in nanoseconds, milliseconds, or seconds.                                                                |
| attributes   | git                              | object   | Git info for DORA Metrics events.                                                                                                                                |
| git          | commit_sha [*required*]     | string   | Git Commit SHA.                                                                                                                                                  |
| git          | repository_url [*required*] | string   | Git Repository URL                                                                                                                                               |
| attributes   | id                               | string   | Deployment ID. Must be 16-128 characters and contain only alphanumeric characters, hyphens, underscores, periods, and colons (a-z, A-Z, 0-9, -, _, ., :).        |
| attributes   | service [*required*]        | string   | Service name.                                                                                                                                                    |
| attributes   | started_at [*required*]     | int64    | Unix timestamp when the deployment started. It must be in nanoseconds, milliseconds, or seconds.                                                                 |
| attributes   | team                             | string   | Name of the team owning the deployed service. If not provided, this is automatically populated with the team associated with the service in the Service Catalog. |
| attributes   | version                          | string   | Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/).                                           |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response after receiving a DORA deployment event.

| Parent field | Field                  | Type   | Description                                                                      |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------------- |
|              | data [*required*] | object | The JSON:API data.                                                               |
| data         | id [*required*]   | string | The ID of the received DORA deployment event.                                    |
| data         | type                   | enum   | JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_deployment"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="202" %}
OK - but delayed due to incident
{% tab title="Model" %}
Response after receiving a DORA deployment event.

| Parent field | Field                  | Type   | Description                                                                      |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------------- |
|              | data [*required*] | object | The JSON:API data.                                                               |
| data         | id [*required*]   | string | The ID of the received DORA deployment event.                                    |
| data         | type                   | enum   | JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_deployment"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployment" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}

## Send a failure event{% #send-a-failure-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                           |
| ----------------- | ------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/dora/failure |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/dora/failure |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/dora/failure      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/dora/failure      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/dora/failure     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/dora/failure |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/dora/failure |

### Overview

Use this API endpoint to provide failure data.

This is necessary for:

- Change Failure Rate
- Time to Restore

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                            | Type     | Description                                                                                                                                            |
| ------------ | -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]           | object   | The JSON:API data.                                                                                                                                     |
| data         | attributes [*required*]     | object   | Attributes to create a DORA failure event.                                                                                                             |
| attributes   | custom_tags                      | [string] | A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.                                           |
| attributes   | env                              | string   | Environment name that was impacted by the failure.                                                                                                     |
| attributes   | finished_at                      | int64    | Unix timestamp when the failure finished. It must be in nanoseconds, milliseconds, or seconds.                                                         |
| attributes   | git                              | object   | Git info for DORA Metrics events.                                                                                                                      |
| git          | commit_sha [*required*]     | string   | Git Commit SHA.                                                                                                                                        |
| git          | repository_url [*required*] | string   | Git Repository URL                                                                                                                                     |
| attributes   | id                               | string   | Failure ID. Must be 16-128 characters and contain only alphanumeric characters, hyphens, underscores, periods, and colons (a-z, A-Z, 0-9, -, _, ., :). |
| attributes   | name                             | string   | Failure name.                                                                                                                                          |
| attributes   | services                         | [string] | Service names impacted by the failure. If possible, use names registered in the Service Catalog. Required when the team field is not provided.         |
| attributes   | severity                         | string   | Failure severity.                                                                                                                                      |
| attributes   | started_at [*required*]     | int64    | Unix timestamp when the failure started. It must be in nanoseconds, milliseconds, or seconds.                                                          |
| attributes   | team                             | string   | Name of the team owning the services impacted. If possible, use team handles registered in Datadog. Required when the services field is not provided.  |
| attributes   | version                          | string   | Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/).                                 |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response after receiving a DORA failure event.

| Parent field | Field                  | Type   | Description                                                                |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------- |
|              | data [*required*] | object | Response after receiving a DORA failure event.                             |
| data         | id [*required*]   | string | The ID of the received DORA failure event.                                 |
| data         | type                   | enum   | JSON:API type for DORA failure events. Allowed enum values: `dora_failure` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="202" %}
OK - but delayed due to incident
{% tab title="Model" %}
Response after receiving a DORA failure event.

| Parent field | Field                  | Type   | Description                                                                |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------- |
|              | data [*required*] | object | Response after receiving a DORA failure event.                             |
| data         | id [*required*]   | string | The ID of the received DORA failure event.                                 |
| data         | type                   | enum   | JSON:API type for DORA failure events. Allowed enum values: `dora_failure` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failure" \
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

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}

## Send an incident event{% #send-an-incident-event %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/dora/incident |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/dora/incident |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/dora/incident      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/dora/incident      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/dora/incident     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/dora/incident |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/dora/incident |

### Overview

**Note**: This endpoint is deprecated. Please use `/api/v2/dora/failure` instead.

Use this API endpoint to provide failure data.

This is necessary for:

- Change Failure Rate
- Time to Restore

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                            | Type     | Description                                                                                                                                            |
| ------------ | -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]           | object   | The JSON:API data.                                                                                                                                     |
| data         | attributes [*required*]     | object   | Attributes to create a DORA failure event.                                                                                                             |
| attributes   | custom_tags                      | [string] | A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event.                                           |
| attributes   | env                              | string   | Environment name that was impacted by the failure.                                                                                                     |
| attributes   | finished_at                      | int64    | Unix timestamp when the failure finished. It must be in nanoseconds, milliseconds, or seconds.                                                         |
| attributes   | git                              | object   | Git info for DORA Metrics events.                                                                                                                      |
| git          | commit_sha [*required*]     | string   | Git Commit SHA.                                                                                                                                        |
| git          | repository_url [*required*] | string   | Git Repository URL                                                                                                                                     |
| attributes   | id                               | string   | Failure ID. Must be 16-128 characters and contain only alphanumeric characters, hyphens, underscores, periods, and colons (a-z, A-Z, 0-9, -, _, ., :). |
| attributes   | name                             | string   | Failure name.                                                                                                                                          |
| attributes   | services                         | [string] | Service names impacted by the failure. If possible, use names registered in the Service Catalog. Required when the team field is not provided.         |
| attributes   | severity                         | string   | Failure severity.                                                                                                                                      |
| attributes   | started_at [*required*]     | int64    | Unix timestamp when the failure started. It must be in nanoseconds, milliseconds, or seconds.                                                          |
| attributes   | team                             | string   | Name of the team owning the services impacted. If possible, use team handles registered in Datadog. Required when the services field is not provided.  |
| attributes   | version                          | string   | Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/).                                 |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response after receiving a DORA failure event.

| Parent field | Field                  | Type   | Description                                                                |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------- |
|              | data [*required*] | object | Response after receiving a DORA failure event.                             |
| data         | id [*required*]   | string | The ID of the received DORA failure event.                                 |
| data         | type                   | enum   | JSON:API type for DORA failure events. Allowed enum values: `dora_failure` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="202" %}
OK - but delayed due to incident
{% tab title="Model" %}
Response after receiving a DORA failure event.

| Parent field | Field                  | Type   | Description                                                                |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------- |
|              | data [*required*] | object | Response after receiving a DORA failure event.                             |
| data         | id [*required*]   | string | The ID of the received DORA failure event.                                 |
| data         | type                   | enum   | JSON:API type for DORA failure events. Allowed enum values: `dora_failure` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "4242fcdd31586083",
    "type": "dora_failure"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/incident" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
## Get a list of deployment events{% #get-a-list-of-deployment-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/dora/deployments |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/dora/deployments |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/dora/deployments      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/dora/deployments      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/dora/deployments     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/dora/deployments |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/dora/deployments |

### Overview

Use this API endpoint to get a list of deployment events. This endpoint requires the `dora_metrics_read` permission.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type      | Description                                                                                                         |
| ------------ | ---------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object    | The JSON:API data.                                                                                                  |
| data         | attributes [*required*] | object    | Attributes to get a list of deployments.                                                                            |
| attributes   | from                         | date-time | Minimum timestamp for requested events.                                                                             |
| attributes   | limit                        | int32     | Maximum number of events in the response.                                                                           |
| attributes   | query                        | string    | Search query with event platform syntax.                                                                            |
| attributes   | sort                         | string    | Sort order (prefixed with `-` for descending).                                                                      |
| attributes   | to                           | date-time | Maximum timestamp for requested events.                                                                             |
| data         | type                         | enum      | The definition of `DORAListDeploymentsRequestDataType` object. Allowed enum values: `dora_deployments_list_request` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for the list deployments endpoint.

| Parent field | Field                            | Type     | Description                                                                                                  |
| ------------ | -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
|              | data                             | [object] | The list of DORA deployment events.                                                                          |
| data         | attributes                       | object   | The attributes of the deployment event.                                                                      |
| attributes   | custom_tags                      | [string] | A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event. |
| attributes   | env                              | string   | Environment name to where the service was deployed.                                                          |
| attributes   | finished_at [*required*]    | int64    | Unix timestamp when the deployment finished.                                                                 |
| attributes   | git                              | object   | Git info for DORA Metrics events.                                                                            |
| git          | commit_sha [*required*]     | string   | Git Commit SHA.                                                                                              |
| git          | repository_url [*required*] | string   | Git Repository URL                                                                                           |
| attributes   | service [*required*]        | string   | Service name.                                                                                                |
| attributes   | started_at [*required*]     | int64    | Unix timestamp when the deployment started.                                                                  |
| attributes   | team                             | string   | Name of the team owning the deployed service.                                                                |
| attributes   | version                          | string   | Version to correlate with APM Deployment Tracking.                                                           |
| data         | id                               | string   | The ID of the deployment event.                                                                              |
| data         | type                             | enum     | JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment`                             |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployments" \
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

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a list of deployment events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORADeploymentsListResponse;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequest;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequestAttributes;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequestData;
import com.datadog.api.client.v2.model.DORAListDeploymentsRequestDataType;
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
      DORADeploymentsListResponse result = apiInstance.listDORADeployments(body);
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
  .then((data: v2.DORADeploymentsListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a list of failure events{% #get-a-list-of-failure-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/dora/failures |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/dora/failures |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/dora/failures      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/dora/failures      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/dora/failures     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/dora/failures |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/dora/failures |

### Overview

Use this API endpoint to get a list of failure events. This endpoint requires the `dora_metrics_read` permission.

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type      | Description                                                                                                   |
| ------------ | ---------------------------- | --------- | ------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object    | The JSON:API data.                                                                                            |
| data         | attributes [*required*] | object    | Attributes to get a list of failures.                                                                         |
| attributes   | from                         | date-time | Minimum timestamp for requested events.                                                                       |
| attributes   | limit                        | int32     | Maximum number of events in the response.                                                                     |
| attributes   | query                        | string    | Search query with event platform syntax.                                                                      |
| attributes   | sort                         | string    | Sort order (prefixed with `-` for descending).                                                                |
| attributes   | to                           | date-time | Maximum timestamp for requested events.                                                                       |
| data         | type                         | enum      | The definition of `DORAListFailuresRequestDataType` object. Allowed enum values: `dora_failures_list_request` |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for the list failures endpoint.

| Parent field | Field                            | Type     | Description                                                                                                  |
| ------------ | -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
|              | data                             | [object] | The list of DORA incident events.                                                                            |
| data         | attributes                       | object   | The attributes of the incident event.                                                                        |
| attributes   | custom_tags                      | [string] | A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event. |
| attributes   | env                              | string   | Environment name that was impacted by the incident.                                                          |
| attributes   | finished_at                      | int64    | Unix timestamp when the incident finished.                                                                   |
| attributes   | git                              | object   | Git info for DORA Metrics events.                                                                            |
| git          | commit_sha [*required*]     | string   | Git Commit SHA.                                                                                              |
| git          | repository_url [*required*] | string   | Git Repository URL                                                                                           |
| attributes   | name                             | string   | Incident name.                                                                                               |
| attributes   | services                         | [string] | Service names impacted by the incident.                                                                      |
| attributes   | severity                         | string   | Incident severity.                                                                                           |
| attributes   | started_at [*required*]     | int64    | Unix timestamp when the incident started.                                                                    |
| attributes   | team                             | string   | Name of the team owning the services impacted.                                                               |
| attributes   | version                          | string   | Version to correlate with APM Deployment Tracking.                                                           |
| data         | id                               | string   | The ID of the incident event.                                                                                |
| data         | type                             | enum     | JSON:API type for DORA failure events. Allowed enum values: `dora_failure`                                   |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failures" \
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

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a list of failure events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAFailuresListResponse;
import com.datadog.api.client.v2.model.DORAListFailuresRequest;
import com.datadog.api.client.v2.model.DORAListFailuresRequestAttributes;
import com.datadog.api.client.v2.model.DORAListFailuresRequestData;
import com.datadog.api.client.v2.model.DORAListFailuresRequestDataType;
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
      DORAFailuresListResponse result = apiInstance.listDORAFailures(body);
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
  .then((data: v2.DORAFailuresListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a deployment event{% #get-a-deployment-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/dora/deployments/{deployment_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/dora/deployments/{deployment_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/dora/deployments/{deployment_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/dora/deployments/{deployment_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/dora/deployments/{deployment_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/dora/deployments/{deployment_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/dora/deployments/{deployment_id} |

### Overview

Use this API endpoint to get a deployment event. This endpoint requires the `dora_metrics_read` permission.

### Arguments

#### Path Parameters

| Name                            | Type   | Description                     |
| ------------------------------- | ------ | ------------------------------- |
| deployment_id [*required*] | string | The ID of the deployment event. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for fetching a single deployment event.

| Parent field | Field                            | Type     | Description                                                                                                  |
| ------------ | -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
|              | data                             | object   | A DORA deployment event.                                                                                     |
| data         | attributes                       | object   | The attributes of the deployment event.                                                                      |
| attributes   | custom_tags                      | [string] | A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event. |
| attributes   | env                              | string   | Environment name to where the service was deployed.                                                          |
| attributes   | finished_at [*required*]    | int64    | Unix timestamp when the deployment finished.                                                                 |
| attributes   | git                              | object   | Git info for DORA Metrics events.                                                                            |
| git          | commit_sha [*required*]     | string   | Git Commit SHA.                                                                                              |
| git          | repository_url [*required*] | string   | Git Repository URL                                                                                           |
| attributes   | service [*required*]        | string   | Service name.                                                                                                |
| attributes   | started_at [*required*]     | int64    | Unix timestamp when the deployment started.                                                                  |
| attributes   | team                             | string   | Name of the team owning the deployed service.                                                                |
| attributes   | version                          | string   | Version to correlate with APM Deployment Tracking.                                                           |
| data         | id                               | string   | The ID of the deployment event.                                                                              |
| data         | type                             | enum     | JSON:API type for DORA deployment events. Allowed enum values: `dora_deployment`                             |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport deployment_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployments/${deployment_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a deployment event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.get_dora_deployment("deployment_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a deployment event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORADeploymentFetchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    try {
      DORADeploymentFetchResponse result = apiInstance.getDORADeployment("deployment_id");
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
  .then((data: v2.DORADeploymentFetchResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a failure event{% #get-a-failure-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/dora/failures/{failure_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/dora/failures/{failure_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/dora/failures/{failure_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/dora/failures/{failure_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/dora/failures/{failure_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/dora/failures/{failure_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/dora/failures/{failure_id} |

### Overview

Use this API endpoint to get a failure event. This endpoint requires the `dora_metrics_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                  |
| ---------------------------- | ------ | ---------------------------- |
| failure_id [*required*] | string | The ID of the failure event. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for fetching a single failure event.

| Parent field | Field                            | Type     | Description                                                                                                  |
| ------------ | -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
|              | data                             | object   | A DORA incident event.                                                                                       |
| data         | attributes                       | object   | The attributes of the incident event.                                                                        |
| attributes   | custom_tags                      | [string] | A list of user-defined tags. The tags must follow the `key:value` pattern. Up to 100 may be added per event. |
| attributes   | env                              | string   | Environment name that was impacted by the incident.                                                          |
| attributes   | finished_at                      | int64    | Unix timestamp when the incident finished.                                                                   |
| attributes   | git                              | object   | Git info for DORA Metrics events.                                                                            |
| git          | commit_sha [*required*]     | string   | Git Commit SHA.                                                                                              |
| git          | repository_url [*required*] | string   | Git Repository URL                                                                                           |
| attributes   | name                             | string   | Incident name.                                                                                               |
| attributes   | services                         | [string] | Service names impacted by the incident.                                                                      |
| attributes   | severity                         | string   | Incident severity.                                                                                           |
| attributes   | started_at [*required*]     | int64    | Unix timestamp when the incident started.                                                                    |
| attributes   | team                             | string   | Name of the team owning the services impacted.                                                               |
| attributes   | version                          | string   | Version to correlate with APM Deployment Tracking.                                                           |
| data         | id                               | string   | The ID of the incident event.                                                                                |
| data         | type                             | enum     | JSON:API type for DORA failure events. Allowed enum values: `dora_failure`                                   |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport failure_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failures/${failure_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a failure event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.get_dora_failure("failure_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a failure event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORAFailureFetchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    try {
      DORAFailureFetchResponse result = apiInstance.getDORAFailure("failure_id");
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
  .then((data: v2.DORAFailureFetchResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete a failure event{% #delete-a-failure-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/dora/failure/{failure_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/dora/failure/{failure_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/dora/failure/{failure_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/dora/failure/{failure_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/dora/failure/{failure_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/dora/failure/{failure_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/dora/failure/{failure_id} |

### Overview

Use this API endpoint to delete a failure event. This endpoint requires the `dora_metrics_write` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                            |
| ---------------------------- | ------ | -------------------------------------- |
| failure_id [*required*] | string | The ID of the failure event to delete. |

### Response

{% tab title="202" %}
Accepted
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport failure_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/failure/${failure_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete a failure event returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.delete_dora_failure("NO_VALUE")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete a deployment event{% #delete-a-deployment-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/dora/deployment/{deployment_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/dora/deployment/{deployment_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/dora/deployment/{deployment_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/dora/deployment/{deployment_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/dora/deployment/{deployment_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/dora/deployment/{deployment_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/dora/deployment/{deployment_id} |

### Overview

Use this API endpoint to delete a deployment event. This endpoint requires the `dora_metrics_write` permission.

### Arguments

#### Path Parameters

| Name                            | Type   | Description                               |
| ------------------------------- | ------ | ----------------------------------------- |
| deployment_id [*required*] | string | The ID of the deployment event to delete. |

### Response

{% tab title="202" %}
Accepted
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport deployment_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployment/${deployment_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete a deployment event returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new
p api_instance.delete_dora_deployment("NO_VALUE")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Patch a deployment event{% #patch-a-deployment-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/dora/deployments/{deployment_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/dora/deployments/{deployment_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/dora/deployments/{deployment_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/dora/deployments/{deployment_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/dora/deployments/{deployment_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/dora/deployments/{deployment_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/dora/deployments/{deployment_id} |

### Overview

Use this API endpoint to patch a deployment event. This endpoint requires the `dora_metrics_write` permission.

### Arguments

#### Path Parameters

| Name                            | Type   | Description                     |
| ------------------------------- | ------ | ------------------------------- |
| deployment_id [*required*] | string | The ID of the deployment event. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                                           |
| ------------ | ---------------------------- | ------- | ----------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object  | The JSON:API data for patching a deployment.                                                          |
| data         | attributes [*required*] | object  | Attributes for patching a DORA deployment event.                                                      |
| attributes   | change_failure               | boolean | Indicates whether the deployment resulted in a change failure.                                        |
| attributes   | remediation                  | object  | Remediation details for the deployment.                                                               |
| remediation  | id [*required*]         | string  | The ID of the remediation action.                                                                     |
| remediation  | type [*required*]       | enum    | The type of remediation action taken. Allowed enum values: `rollback,rollforward`                     |
| data         | id [*required*]         | string  | The ID of the deployment to patch.                                                                    |
| data         | type [*required*]       | enum    | JSON:API type for DORA deployment patch request. Allowed enum values: `dora_deployment_patch_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "change_failure": true,
      "remediation": {
        "id": "eG42zNIkVjM",
        "type": "rollback"
      }
    },
    "id": "z_RwVLi7v4Y",
    "type": "dora_deployment_patch_request"
  }
}
```

{% /tab %}

### Response

{% tab title="202" %}
Accepted
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport deployment_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dora/deployments/${deployment_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "remediation": {
        "id": "eG42zNIkVjM",
        "type": "rollback"
      }
    },
    "id": "z_RwVLi7v4Y",
    "type": "dora_deployment_patch_request"
  }
}
EOF

#####

```python
"""
Patch a deployment event returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_deployment_patch_remediation import DORADeploymentPatchRemediation
from datadog_api_client.v2.model.dora_deployment_patch_remediation_type import DORADeploymentPatchRemediationType
from datadog_api_client.v2.model.dora_deployment_patch_request import DORADeploymentPatchRequest
from datadog_api_client.v2.model.dora_deployment_patch_request_attributes import DORADeploymentPatchRequestAttributes
from datadog_api_client.v2.model.dora_deployment_patch_request_data import DORADeploymentPatchRequestData
from datadog_api_client.v2.model.dora_deployment_patch_request_data_type import DORADeploymentPatchRequestDataType

body = DORADeploymentPatchRequest(
    data=DORADeploymentPatchRequestData(
        attributes=DORADeploymentPatchRequestAttributes(
            change_failure=True,
            remediation=DORADeploymentPatchRemediation(
                id="eG42zNIkVjM",
                type=DORADeploymentPatchRemediationType.ROLLBACK,
            ),
        ),
        id="z_RwVLi7v4Y",
        type=DORADeploymentPatchRequestDataType.DORA_DEPLOYMENT_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    api_instance.patch_dora_deployment(deployment_id="deployment_id", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Patch a deployment event returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DORAMetricsAPI.new

body = DatadogAPIClient::V2::DORADeploymentPatchRequest.new({
  data: DatadogAPIClient::V2::DORADeploymentPatchRequestData.new({
    attributes: DatadogAPIClient::V2::DORADeploymentPatchRequestAttributes.new({
      change_failure: true,
      remediation: DatadogAPIClient::V2::DORADeploymentPatchRemediation.new({
        id: "eG42zNIkVjM",
        type: DatadogAPIClient::V2::DORADeploymentPatchRemediationType::ROLLBACK,
      }),
    }),
    id: "z_RwVLi7v4Y",
    type: DatadogAPIClient::V2::DORADeploymentPatchRequestDataType::DORA_DEPLOYMENT_PATCH_REQUEST,
  }),
})
p api_instance.patch_dora_deployment("deployment_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Patch a deployment event returns "Accepted" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.DORADeploymentPatchRequest{
        Data: datadogV2.DORADeploymentPatchRequestData{
            Attributes: datadogV2.DORADeploymentPatchRequestAttributes{
                ChangeFailure: datadog.PtrBool(true),
                Remediation: &datadogV2.DORADeploymentPatchRemediation{
                    Id:   "eG42zNIkVjM",
                    Type: datadogV2.DORADEPLOYMENTPATCHREMEDIATIONTYPE_ROLLBACK,
                },
            },
            Id:   "z_RwVLi7v4Y",
            Type: datadogV2.DORADEPLOYMENTPATCHREQUESTDATATYPE_DORA_DEPLOYMENT_PATCH_REQUEST,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDORAMetricsApi(apiClient)
    r, err := api.PatchDORADeployment(ctx, "deployment_id", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DORAMetricsApi.PatchDORADeployment`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Patch a deployment event returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DoraMetricsApi;
import com.datadog.api.client.v2.model.DORADeploymentPatchRemediation;
import com.datadog.api.client.v2.model.DORADeploymentPatchRemediationType;
import com.datadog.api.client.v2.model.DORADeploymentPatchRequest;
import com.datadog.api.client.v2.model.DORADeploymentPatchRequestAttributes;
import com.datadog.api.client.v2.model.DORADeploymentPatchRequestData;
import com.datadog.api.client.v2.model.DORADeploymentPatchRequestDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DoraMetricsApi apiInstance = new DoraMetricsApi(defaultClient);

    DORADeploymentPatchRequest body =
        new DORADeploymentPatchRequest()
            .data(
                new DORADeploymentPatchRequestData()
                    .attributes(
                        new DORADeploymentPatchRequestAttributes()
                            .changeFailure(true)
                            .remediation(
                                new DORADeploymentPatchRemediation()
                                    .id("eG42zNIkVjM")
                                    .type(DORADeploymentPatchRemediationType.ROLLBACK)))
                    .id("z_RwVLi7v4Y")
                    .type(DORADeploymentPatchRequestDataType.DORA_DEPLOYMENT_PATCH_REQUEST));

    try {
      apiInstance.patchDORADeployment("deployment_id", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DoraMetricsApi#patchDORADeployment");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Patch a deployment event returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dora_metrics::DORAMetricsAPI;
use datadog_api_client::datadogV2::model::DORADeploymentPatchRemediation;
use datadog_api_client::datadogV2::model::DORADeploymentPatchRemediationType;
use datadog_api_client::datadogV2::model::DORADeploymentPatchRequest;
use datadog_api_client::datadogV2::model::DORADeploymentPatchRequestAttributes;
use datadog_api_client::datadogV2::model::DORADeploymentPatchRequestData;
use datadog_api_client::datadogV2::model::DORADeploymentPatchRequestDataType;

#[tokio::main]
async fn main() {
    let body = DORADeploymentPatchRequest::new(DORADeploymentPatchRequestData::new(
        DORADeploymentPatchRequestAttributes::new()
            .change_failure(true)
            .remediation(DORADeploymentPatchRemediation::new(
                "eG42zNIkVjM".to_string(),
                DORADeploymentPatchRemediationType::ROLLBACK,
            )),
        "z_RwVLi7v4Y".to_string(),
        DORADeploymentPatchRequestDataType::DORA_DEPLOYMENT_PATCH_REQUEST,
    ));
    let configuration = datadog::Configuration::new();
    let api = DORAMetricsAPI::with_config(configuration);
    let resp = api
        .patch_dora_deployment("deployment_id".to_string(), body)
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Patch a deployment event returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DORAMetricsApi(configuration);

const params: v2.DORAMetricsApiPatchDORADeploymentRequest = {
  body: {
    data: {
      attributes: {
        changeFailure: true,
        remediation: {
          id: "eG42zNIkVjM",
          type: "rollback",
        },
      },
      id: "z_RwVLi7v4Y",
      type: "dora_deployment_patch_request",
    },
  },
  deploymentId: "deployment_id",
};

apiInstance
  .patchDORADeployment(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
