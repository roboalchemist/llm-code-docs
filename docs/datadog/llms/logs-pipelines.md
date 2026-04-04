# Source: https://docs.datadoghq.com/api/latest/logs-pipelines.md

---
title: Logs Pipelines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Logs Pipelines
---

# Logs Pipelines

Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.

- See the [pipelines configuration page](https://app.datadoghq.com/logs/pipelines) for a list of the pipelines and processors currently configured in web UI.

- Additional API-related information about processors can be found in the [processors documentation](https://docs.datadoghq.com/logs/log_configuration/processors/?tab=api#lookup-processor).

- For more information about Pipelines, see the [pipeline documentation](https://docs.datadoghq.com/logs/log_configuration/pipelines).

**Notes:**

**Grok parsing rules may effect JSON output and require returned data to be configured before using in a request.** For example, if you are using the data returned from a request for another request body, and have a parsing rule that uses a regex pattern like `\s` for spaces, you will need to configure all escaped spaces as `%{space}` to use in the body data.

## Get pipeline order{% #get-pipeline-order %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/logs/config/pipeline-order |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/logs/config/pipeline-order |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/logs/config/pipeline-order      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/logs/config/pipeline-order      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/logs/config/pipeline-order     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/logs/config/pipeline-order |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order |

### Overview

Get the current order of your pipelines. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object containing the ordered list of pipeline IDs.

| Field                          | Type     | Description                                                                                                                      |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| pipeline_ids [*required*] | [string] | Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get pipeline order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.get_logs_pipeline_order()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get pipeline order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.get_logs_pipeline_order()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get pipeline order returns "OK" response

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
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.GetLogsPipelineOrder(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.GetLogsPipelineOrder`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.GetLogsPipelineOrder`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get pipeline order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipelinesOrder;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      LogsPipelinesOrder result = apiInstance.getLogsPipelineOrder();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#getLogsPipelineOrder");
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
// Get pipeline order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.get_logs_pipeline_order().await;
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
 * Get pipeline order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

apiInstance
  .getLogsPipelineOrder()
  .then((data: v1.LogsPipelinesOrder) => {
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

## Update pipeline order{% #update-pipeline-order %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/logs/config/pipeline-order |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/logs/config/pipeline-order |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/logs/config/pipeline-order      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/logs/config/pipeline-order      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/logs/config/pipeline-order     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/logs/config/pipeline-order |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order |

### Overview



Update the order of your pipelines. Since logs are processed sequentially, reordering a pipeline may change the structure and content of the data processed by other pipelines and their processors.

**Note**: Using the `PUT` method updates your pipeline order by replacing your current order with the new one sent to your Datadog organization.
This endpoint requires the `logs_write_pipelines` permission.


### Request

#### Body Data (required)

Object containing the new ordered list of pipeline IDs.

{% tab title="Model" %}

| Field                          | Type     | Description                                                                                                                      |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| pipeline_ids [*required*] | [string] | Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object containing the ordered list of pipeline IDs.

| Field                          | Type     | Description                                                                                                                      |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| pipeline_ids [*required*] | [string] | Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="422" %}
Unprocessable Entity
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipeline-order" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "pipeline_ids": [
    "tags",
    "org_ids",
    "products"
  ]
}
EOF

#####

```python
"""
Update pipeline order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_pipelines_order import LogsPipelinesOrder

body = LogsPipelinesOrder(
    pipeline_ids=[
        "tags",
        "org_ids",
        "products",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.update_logs_pipeline_order(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update pipeline order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipelinesOrder.new({
  pipeline_ids: [
    "tags",
    "org_ids",
    "products",
  ],
})
p api_instance.update_logs_pipeline_order(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update pipeline order returns "OK" response

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
    body := datadogV1.LogsPipelinesOrder{
        PipelineIds: []string{
            "tags",
            "org_ids",
            "products",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.UpdateLogsPipelineOrder(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.UpdateLogsPipelineOrder`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.UpdateLogsPipelineOrder`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update pipeline order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipelinesOrder;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipelinesOrder body =
        new LogsPipelinesOrder().pipelineIds(Arrays.asList("tags", "org_ids", "products"));

    try {
      LogsPipelinesOrder result = apiInstance.updateLogsPipelineOrder(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#updateLogsPipelineOrder");
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
// Update pipeline order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsPipelinesOrder;

#[tokio::main]
async fn main() {
    let body = LogsPipelinesOrder::new(vec![
        "tags".to_string(),
        "org_ids".to_string(),
        "products".to_string(),
    ]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.update_logs_pipeline_order(body).await;
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
 * Update pipeline order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiUpdateLogsPipelineOrderRequest = {
  body: {
    pipelineIds: ["tags", "org_ids", "products"],
  },
};

apiInstance
  .updateLogsPipelineOrder(params)
  .then((data: v1.LogsPipelinesOrder) => {
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

## Get all pipelines{% #get-all-pipelines %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/logs/config/pipelines      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/logs/config/pipelines      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/logs/config/pipelines     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/logs/config/pipelines |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/logs/config/pipelines |

### Overview

Get all pipelines from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Array of all log pipeline objects configured for the organization.

| Parent field         | Field                                     | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | description                               | string          | A description of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | id                                        | string          | ID of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | is_enabled                                | boolean         | Whether or not the pipeline is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                      | is_read_only                              | boolean         | Whether or not the pipeline can be edited.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | name                                      | string          | Name of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | processors                                | [ <oneOf>] | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 1                                  | object          | Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).                                                                                                                                                                         |
| Option 1             | grok [*required*]                    | object          | Set of rules for the grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | match_rules [*required*]             | string          | List of match rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | support_rules                             | string          | List of support rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 1             | samples                                   | [string]        | List of sample logs to test this grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | source [*required*]                  | string          | Name of the log attribute to parse.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | type [*required*]                    | enum            | Type of logs grok parser. Allowed enum values: `grok-parser`                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 2                                  | object          | As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.                                                                                                                                                                                                                                                                                                                                                             | `timestamp`                                                                                                                                                                                                            | `date`                                                                                                                                                                                                                                                                                                                   | `_timestamp` | `Timestamp` | `eventTime` | `published_date` | If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164. | **Note:** If your logs don't contain any of the default attributes and you haven't defined your own date attribute, Datadog timestamps the logs with the date it received them. | If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account. |
| Option 2             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 2             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs date remapper. Allowed enum values: `date-remapper`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 3                                  | object          | Use this Processor if you want to assign some attributes as the official status.                                                                                                                                                                                                                                                                                                                                                                                  | Each incoming status value is mapped as follows.                                                                                                                                                                       | **Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.                                                                                                                                                         |
| Option 3             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 3             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 3             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | type [*required*]                    | enum            | Type of logs status remapper. Allowed enum values: `status-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 4                                  | object          | Use this processor if you want to assign one or more attributes as the official service.                                                                                                                                                                                                                                                                                                                                                                          | **Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                           |
| Option 4             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 4             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 4             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 4             | type [*required*]                    | enum            | Type of logs service remapper. Allowed enum values: `service-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 5                                  | object          | The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.                                                                                                                                                                                                                                    | **Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                       |
| Option 5             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 5             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 5             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 5             | type [*required*]                    | enum            | Type of logs message remapper. Allowed enum values: `message-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 6                                  | object          | The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.                                                                                           |
| Option 6             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 6             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 6             | override_on_conflict                      | boolean         | Override or not the target element if already set,                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 6             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 6             | source_type                               | string          | Defines if the sources are from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 6             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 6             | target [*required*]                  | string          | Final attribute or tag name to remap the sources to.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 6             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 6             | target_type                               | string          | Defines if the final attribute or tag name is from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 6             | type [*required*]                    | enum            | Type of logs attribute remapper. Allowed enum values: `attribute-remapper`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 7                                  | object          | This processor extracts query parameters and other important parameters from a URL.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 7             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 7             | normalize_ending_slashes                  | boolean         | Normalize the ending slashes or not.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 7             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 7             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | type [*required*]                    | enum            | Type of logs URL parser. Allowed enum values: `url-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 8                                  | object          | The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.                                                                                                                                                                                                                                                                                |
| Option 8             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | is_encoded                                | boolean         | Define if the source attribute is URL encoded or not.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Option 8             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 8             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 8             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | type [*required*]                    | enum            | Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 9                                  | object          | Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.                                                                                                                                                           | **Notes**:                                                                                                                                                                                                             |
| Option 9             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | name                                      | string          | Value to assign to the target attribute.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 9             | target [*required*]                  | string          | Name of the target attribute which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 9             | type [*required*]                    | enum            | Type of logs category processor. Allowed enum values: `category-processor`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 10                                 | object          | Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.                                                                                                                              | The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.                                                                                                                                 | By default, the calculation is skipped if an attribute is missing. Select "Replace missing attribute by 0" to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number. | *Notes*:     |
| Option 10            | expression [*required*]              | string          | Arithmetic operation between one or more log attributes.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_replace_missing                        | boolean         | If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.                                                                                                                                                                                                                                                                                                                                        |
| Option 10            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 10            | target [*required*]                  | string          | Name of the attribute that contains the result of the arithmetic operation.                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 10            | type [*required*]                    | enum            | Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`                                                                                                                                                                                                                                                                                                                                                                                    |
| processors           | Option 11                                 | object          | Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.                                                                                                                                                                                                                        | The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.                                                                                                                               | **Notes**:                                                                                                                                                                                                                                                                                                               |
| Option 11            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 11            | is_replace_missing                        | boolean         | If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.                                                                                                                                                                                                                                                                                                                   |
| Option 11            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 11            | target [*required*]                  | string          | The name of the attribute that contains the result of the template.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | template [*required*]                | string          | A formula with one or more attributes and raw text.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | type [*required*]                    | enum            | Type of logs string builder processor. Allowed enum values: `string-builder-processor`                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 12                                 | object          | Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.                                                                                                                                                                                  | A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.                                                                                                          |
| Option 12            | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 12            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 12            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 12            | processors                                | [object]        | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 12            | type [*required*]                    | enum            | Type of logs pipeline processor. Allowed enum values: `pipeline`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 13                                 | object          | The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.                                                                                                                                                                                                                                                                                                  |
| Option 13            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 13            | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 13            | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | type [*required*]                    | enum            | Type of GeoIP parser. Allowed enum values: `geo-ip-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 14                                 | object          | Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.                                     |
| Option 14            | default_lookup                            | string          | Value to set the target attribute if the source value is not found in the list.                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 14            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 14            | lookup_table [*required*]            | [string]        | Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`                                                                                                                                                                                                                                                                                          |
| Option 14            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 14            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 14            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.                                                                                                                                                                                                                                                                                                                         |
| Option 14            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 15                                 | object          | **Note**: Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines. |
| Option 15            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 15            | lookup_enrichment_table [*required*] | string          | Name of the Reference Table for the source attribute and their associated target attribute values.                                                                                                                                                                                                                                                                                                                                                                |
| Option 15            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 15            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 15            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list.                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 15            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 16                                 | object          | There are two ways to improve correlation between application traces and logs.                                                                                                                                                                                                                                                                                                                                                                                    | Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.     | Use the Trace remapper processor to define a log attribute as its associated trace ID.                                                                                                                                                                                                                                   |
| Option 16            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 16            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 16            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 16            | type [*required*]                    | enum            | Type of logs trace remapper. Allowed enum values: `trace-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                             |
| processors           | Option 17                                 | object          | There are two ways to define correlation between application spans and logs:                                                                                                                                                                                                                                                                                                                                                                                      | Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default. | Use the span remapper processor to define a log attribute as its associated span ID.                                                                                                                                                                                                                                     |
| Option 17            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 17            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 17            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 17            | type [*required*]                    | enum            | Type of logs span remapper. Allowed enum values: `span-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                               |
| processors           | Option 18                                 | object          | A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:                                                                                                                                                                                                                                                                                                                                      |
| Option 18            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 18            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | operation [*required*]               |  <oneOf>   | Configuration of the array processor operation to perform.                                                                                                                                                                                                                                                                                                                                                                                                        |
| operation            | Option 1                                  | object          | Operation that appends a value to a target array attribute.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | source [*required*]                  | string          | Attribute path containing the value to append.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Option 1             | target [*required*]                  | string          | Attribute path of the array to append to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Operation type. Allowed enum values: `append`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 2                                  | object          | Operation that computes the length of a `source` array and stores the result in the `target` attribute.                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | source [*required*]                  | string          | Attribute path of the array to measure.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | target [*required*]                  | string          | Attribute that receives the computed length.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 2             | type [*required*]                    | enum            | Operation type. Allowed enum values: `length`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 3                                  | object          | Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.                                                                                                                                                                                                                                                                                                                              |
| Option 3             | filter [*required*]                  | string          | Filter condition expressed as `key:value` used to find the matching element.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | source [*required*]                  | string          | Attribute path of the array to search into.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | target [*required*]                  | string          | Attribute that receives the extracted value.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | type [*required*]                    | enum            | Operation type. Allowed enum values: `select`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 3             | value_to_extract [*required*]        | string          | Key of the value to extract from the matching element.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | type [*required*]                    | enum            | Type of logs array processor. Allowed enum values: `array-processor`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 19                                 | object          | The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.                                                                                                                                                                                                                                                                                    |
| Option 19            | binary_to_text_encoding [*required*] | enum            | The encoding used to represent the binary data. Allowed enum values: `base64,base16`                                                                                                                                                                                                                                                                                                                                                                              |
| Option 19            | input_representation [*required*]    | enum            | The original representation of input string. Allowed enum values: `utf_8,integer`                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | is_enabled                                | boolean         | Whether the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 19            | source [*required*]                  | string          | Name of the log attribute with the encoded data.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 19            | target [*required*]                  | string          | Name of the log attribute that contains the decoded data.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 19            | type [*required*]                    | enum            | Type of logs decoder processor. Allowed enum values: `decoder-processor`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 20                                 | object          | A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.                                                                                                                                                                                                                                                                                                                                         |
| Option 20            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 20            | mappers [*required*]                 | [ <oneOf>] | The `LogsSchemaProcessor` `mappers`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 1                                  | object          | The schema remapper maps source log fields to their correct fields.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                    | string          | Name of the logs schema remapper.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1             | override_on_conflict                      | boolean         | Override or not the target element if already set.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | target [*required*]                  | string          | Target field to map log source field to.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Type of logs schema remapper. Allowed enum values: `schema-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 2                                  | object          | Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.                                                                                                                                                                                                                                                                                      | **Notes**:                                                                                                                                                                                                             |
| Option 2             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter [*required*]                  | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | id [*required*]                      | int64           | ID to inject into the category.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| categories           | name [*required*]                    | string          | Value to assign to target schema field.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | fallback                                  | object          | Used to override hardcoded category values with a value pulled from a source attribute on the log.                                                                                                                                                                                                                                                                                                                                                                |
| fallback             | sources                                   | object          | Fallback sources used to populate value of field.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| additionalProperties | <any-key>                                 | [string]        |
| fallback             | values                                    | object          | Values that define when the fallback is used.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties | <any-key>                                 | string          |
| Option 2             | name [*required*]                    | string          | Name of the logs schema category mapper.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | targets [*required*]                 | object          | Name of the target attributes which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                    |
| targets              | id                                        | string          | ID of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| targets              | name                                      | string          | Name of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`                                                                                                                                                                                                                                                                                                                                                                                |
| Option 20            | name [*required*]                    | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 20            | schema [*required*]                  | object          | Configuration of the schema data to use.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| schema               | class_name [*required*]              | string          | Class name of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| schema               | class_uid [*required*]               | int64           | Class UID of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | profiles                                  | [string]        | Optional list of profiles to modify the schema.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | schema_type [*required*]             | string          | Type of schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| schema               | version [*required*]                 | string          | Version of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 20            | type [*required*]                    | enum            | Type of logs schema processor. Allowed enum values: `schema-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | tags                                      | [string]        | A list of tags associated with the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                      | type                                      | string          | Type of pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all pipelines returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.list_logs_pipelines()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all pipelines returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.list_logs_pipelines()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all pipelines returns "OK" response

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
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.ListLogsPipelines(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.ListLogsPipelines`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.ListLogsPipelines`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all pipelines returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipeline;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      List<LogsPipeline> result = apiInstance.listLogsPipelines();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#listLogsPipelines");
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
// Get all pipelines returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.list_logs_pipelines().await;
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
 * Get all pipelines returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

apiInstance
  .listLogsPipelines()
  .then((data: v1.LogsPipeline[]) => {
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

## Create a pipeline{% #create-a-pipeline %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/logs/config/pipelines      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/logs/config/pipelines      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/logs/config/pipelines     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/logs/config/pipelines |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/logs/config/pipelines |

### Overview

Create a pipeline in your organization. This endpoint requires the `logs_write_pipelines` permission.

### Request

#### Body Data (required)

Definition of the new pipeline.

{% tab title="Model" %}

| Parent field         | Field                                     | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | description                               | string          | A description of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | id                                        | string          | ID of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | is_enabled                                | boolean         | Whether or not the pipeline is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                      | is_read_only                              | boolean         | Whether or not the pipeline can be edited.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | name [*required*]                    | string          | Name of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | processors                                | [ <oneOf>] | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 1                                  | object          | Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).                                                                                                                                                                         |
| Option 1             | grok [*required*]                    | object          | Set of rules for the grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | match_rules [*required*]             | string          | List of match rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | support_rules                             | string          | List of support rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 1             | samples                                   | [string]        | List of sample logs to test this grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | source [*required*]                  | string          | Name of the log attribute to parse.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | type [*required*]                    | enum            | Type of logs grok parser. Allowed enum values: `grok-parser`                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 2                                  | object          | As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.                                                                                                                                                                                                                                                                                                                                                             | `timestamp`                                                                                                                                                                                                            | `date`                                                                                                                                                                                                                                                                                                                   | `_timestamp` | `Timestamp` | `eventTime` | `published_date` | If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164. | **Note:** If your logs don't contain any of the default attributes and you haven't defined your own date attribute, Datadog timestamps the logs with the date it received them. | If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account. |
| Option 2             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 2             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs date remapper. Allowed enum values: `date-remapper`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 3                                  | object          | Use this Processor if you want to assign some attributes as the official status.                                                                                                                                                                                                                                                                                                                                                                                  | Each incoming status value is mapped as follows.                                                                                                                                                                       | **Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.                                                                                                                                                         |
| Option 3             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 3             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 3             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | type [*required*]                    | enum            | Type of logs status remapper. Allowed enum values: `status-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 4                                  | object          | Use this processor if you want to assign one or more attributes as the official service.                                                                                                                                                                                                                                                                                                                                                                          | **Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                           |
| Option 4             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 4             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 4             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 4             | type [*required*]                    | enum            | Type of logs service remapper. Allowed enum values: `service-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 5                                  | object          | The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.                                                                                                                                                                                                                                    | **Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                       |
| Option 5             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 5             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 5             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 5             | type [*required*]                    | enum            | Type of logs message remapper. Allowed enum values: `message-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 6                                  | object          | The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.                                                                                           |
| Option 6             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 6             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 6             | override_on_conflict                      | boolean         | Override or not the target element if already set,                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 6             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 6             | source_type                               | string          | Defines if the sources are from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 6             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 6             | target [*required*]                  | string          | Final attribute or tag name to remap the sources to.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 6             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 6             | target_type                               | string          | Defines if the final attribute or tag name is from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 6             | type [*required*]                    | enum            | Type of logs attribute remapper. Allowed enum values: `attribute-remapper`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 7                                  | object          | This processor extracts query parameters and other important parameters from a URL.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 7             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 7             | normalize_ending_slashes                  | boolean         | Normalize the ending slashes or not.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 7             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 7             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | type [*required*]                    | enum            | Type of logs URL parser. Allowed enum values: `url-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 8                                  | object          | The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.                                                                                                                                                                                                                                                                                |
| Option 8             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | is_encoded                                | boolean         | Define if the source attribute is URL encoded or not.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Option 8             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 8             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 8             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | type [*required*]                    | enum            | Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 9                                  | object          | Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.                                                                                                                                                           | **Notes**:                                                                                                                                                                                                             |
| Option 9             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | name                                      | string          | Value to assign to the target attribute.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 9             | target [*required*]                  | string          | Name of the target attribute which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 9             | type [*required*]                    | enum            | Type of logs category processor. Allowed enum values: `category-processor`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 10                                 | object          | Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.                                                                                                                              | The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.                                                                                                                                 | By default, the calculation is skipped if an attribute is missing. Select "Replace missing attribute by 0" to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number. | *Notes*:     |
| Option 10            | expression [*required*]              | string          | Arithmetic operation between one or more log attributes.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_replace_missing                        | boolean         | If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.                                                                                                                                                                                                                                                                                                                                        |
| Option 10            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 10            | target [*required*]                  | string          | Name of the attribute that contains the result of the arithmetic operation.                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 10            | type [*required*]                    | enum            | Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`                                                                                                                                                                                                                                                                                                                                                                                    |
| processors           | Option 11                                 | object          | Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.                                                                                                                                                                                                                        | The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.                                                                                                                               | **Notes**:                                                                                                                                                                                                                                                                                                               |
| Option 11            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 11            | is_replace_missing                        | boolean         | If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.                                                                                                                                                                                                                                                                                                                   |
| Option 11            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 11            | target [*required*]                  | string          | The name of the attribute that contains the result of the template.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | template [*required*]                | string          | A formula with one or more attributes and raw text.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | type [*required*]                    | enum            | Type of logs string builder processor. Allowed enum values: `string-builder-processor`                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 12                                 | object          | Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.                                                                                                                                                                                  | A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.                                                                                                          |
| Option 12            | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 12            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 12            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 12            | processors                                | [object]        | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 12            | type [*required*]                    | enum            | Type of logs pipeline processor. Allowed enum values: `pipeline`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 13                                 | object          | The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.                                                                                                                                                                                                                                                                                                  |
| Option 13            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 13            | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 13            | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | type [*required*]                    | enum            | Type of GeoIP parser. Allowed enum values: `geo-ip-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 14                                 | object          | Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.                                     |
| Option 14            | default_lookup                            | string          | Value to set the target attribute if the source value is not found in the list.                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 14            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 14            | lookup_table [*required*]            | [string]        | Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`                                                                                                                                                                                                                                                                                          |
| Option 14            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 14            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 14            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.                                                                                                                                                                                                                                                                                                                         |
| Option 14            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 15                                 | object          | **Note**: Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines. |
| Option 15            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 15            | lookup_enrichment_table [*required*] | string          | Name of the Reference Table for the source attribute and their associated target attribute values.                                                                                                                                                                                                                                                                                                                                                                |
| Option 15            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 15            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 15            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list.                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 15            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 16                                 | object          | There are two ways to improve correlation between application traces and logs.                                                                                                                                                                                                                                                                                                                                                                                    | Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.     | Use the Trace remapper processor to define a log attribute as its associated trace ID.                                                                                                                                                                                                                                   |
| Option 16            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 16            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 16            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 16            | type [*required*]                    | enum            | Type of logs trace remapper. Allowed enum values: `trace-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                             |
| processors           | Option 17                                 | object          | There are two ways to define correlation between application spans and logs:                                                                                                                                                                                                                                                                                                                                                                                      | Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default. | Use the span remapper processor to define a log attribute as its associated span ID.                                                                                                                                                                                                                                     |
| Option 17            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 17            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 17            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 17            | type [*required*]                    | enum            | Type of logs span remapper. Allowed enum values: `span-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                               |
| processors           | Option 18                                 | object          | A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:                                                                                                                                                                                                                                                                                                                                      |
| Option 18            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 18            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | operation [*required*]               |  <oneOf>   | Configuration of the array processor operation to perform.                                                                                                                                                                                                                                                                                                                                                                                                        |
| operation            | Option 1                                  | object          | Operation that appends a value to a target array attribute.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | source [*required*]                  | string          | Attribute path containing the value to append.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Option 1             | target [*required*]                  | string          | Attribute path of the array to append to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Operation type. Allowed enum values: `append`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 2                                  | object          | Operation that computes the length of a `source` array and stores the result in the `target` attribute.                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | source [*required*]                  | string          | Attribute path of the array to measure.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | target [*required*]                  | string          | Attribute that receives the computed length.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 2             | type [*required*]                    | enum            | Operation type. Allowed enum values: `length`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 3                                  | object          | Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.                                                                                                                                                                                                                                                                                                                              |
| Option 3             | filter [*required*]                  | string          | Filter condition expressed as `key:value` used to find the matching element.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | source [*required*]                  | string          | Attribute path of the array to search into.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | target [*required*]                  | string          | Attribute that receives the extracted value.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | type [*required*]                    | enum            | Operation type. Allowed enum values: `select`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 3             | value_to_extract [*required*]        | string          | Key of the value to extract from the matching element.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | type [*required*]                    | enum            | Type of logs array processor. Allowed enum values: `array-processor`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 19                                 | object          | The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.                                                                                                                                                                                                                                                                                    |
| Option 19            | binary_to_text_encoding [*required*] | enum            | The encoding used to represent the binary data. Allowed enum values: `base64,base16`                                                                                                                                                                                                                                                                                                                                                                              |
| Option 19            | input_representation [*required*]    | enum            | The original representation of input string. Allowed enum values: `utf_8,integer`                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | is_enabled                                | boolean         | Whether the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 19            | source [*required*]                  | string          | Name of the log attribute with the encoded data.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 19            | target [*required*]                  | string          | Name of the log attribute that contains the decoded data.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 19            | type [*required*]                    | enum            | Type of logs decoder processor. Allowed enum values: `decoder-processor`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 20                                 | object          | A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.                                                                                                                                                                                                                                                                                                                                         |
| Option 20            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 20            | mappers [*required*]                 | [ <oneOf>] | The `LogsSchemaProcessor` `mappers`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 1                                  | object          | The schema remapper maps source log fields to their correct fields.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                    | string          | Name of the logs schema remapper.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1             | override_on_conflict                      | boolean         | Override or not the target element if already set.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | target [*required*]                  | string          | Target field to map log source field to.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Type of logs schema remapper. Allowed enum values: `schema-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 2                                  | object          | Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.                                                                                                                                                                                                                                                                                      | **Notes**:                                                                                                                                                                                                             |
| Option 2             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter [*required*]                  | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | id [*required*]                      | int64           | ID to inject into the category.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| categories           | name [*required*]                    | string          | Value to assign to target schema field.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | fallback                                  | object          | Used to override hardcoded category values with a value pulled from a source attribute on the log.                                                                                                                                                                                                                                                                                                                                                                |
| fallback             | sources                                   | object          | Fallback sources used to populate value of field.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| additionalProperties | <any-key>                                 | [string]        |
| fallback             | values                                    | object          | Values that define when the fallback is used.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties | <any-key>                                 | string          |
| Option 2             | name [*required*]                    | string          | Name of the logs schema category mapper.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | targets [*required*]                 | object          | Name of the target attributes which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                    |
| targets              | id                                        | string          | ID of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| targets              | name                                      | string          | Name of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`                                                                                                                                                                                                                                                                                                                                                                                |
| Option 20            | name [*required*]                    | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 20            | schema [*required*]                  | object          | Configuration of the schema data to use.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| schema               | class_name [*required*]              | string          | Class name of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| schema               | class_uid [*required*]               | int64           | Class UID of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | profiles                                  | [string]        | Optional list of profiles to modify the schema.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | schema_type [*required*]             | string          | Type of schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| schema               | version [*required*]                 | string          | Version of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 20            | type [*required*]                    | enum            | Type of logs schema processor. Allowed enum values: `schema-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | tags                                      | [string]        | A list of tags associated with the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                      | type                                      | string          | Type of pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppend",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_to_array",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps"
      }
    }
  ],
  "tags": []
}
```

#####

```json
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendNoPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_remove_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": false
      }
    }
  ],
  "tags": []
}
```

#####

```json
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_keep_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": true
      }
    }
  ],
  "tags": []
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}


Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.

**Note**: These endpoints are only available for admin users. Make sure to use an application key created by an admin.



| Parent field         | Field                                     | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | description                               | string          | A description of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | id                                        | string          | ID of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | is_enabled                                | boolean         | Whether or not the pipeline is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                      | is_read_only                              | boolean         | Whether or not the pipeline can be edited.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | name [*required*]                    | string          | Name of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | processors                                | [ <oneOf>] | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 1                                  | object          | Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).                                                                                                                                                                         |
| Option 1             | grok [*required*]                    | object          | Set of rules for the grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | match_rules [*required*]             | string          | List of match rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | support_rules                             | string          | List of support rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 1             | samples                                   | [string]        | List of sample logs to test this grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | source [*required*]                  | string          | Name of the log attribute to parse.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | type [*required*]                    | enum            | Type of logs grok parser. Allowed enum values: `grok-parser`                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 2                                  | object          | As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.                                                                                                                                                                                                                                                                                                                                                             | `timestamp`                                                                                                                                                                                                            | `date`                                                                                                                                                                                                                                                                                                                   | `_timestamp` | `Timestamp` | `eventTime` | `published_date` | If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164. | **Note:** If your logs don't contain any of the default attributes and you haven't defined your own date attribute, Datadog timestamps the logs with the date it received them. | If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account. |
| Option 2             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 2             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs date remapper. Allowed enum values: `date-remapper`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 3                                  | object          | Use this Processor if you want to assign some attributes as the official status.                                                                                                                                                                                                                                                                                                                                                                                  | Each incoming status value is mapped as follows.                                                                                                                                                                       | **Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.                                                                                                                                                         |
| Option 3             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 3             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 3             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | type [*required*]                    | enum            | Type of logs status remapper. Allowed enum values: `status-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 4                                  | object          | Use this processor if you want to assign one or more attributes as the official service.                                                                                                                                                                                                                                                                                                                                                                          | **Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                           |
| Option 4             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 4             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 4             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 4             | type [*required*]                    | enum            | Type of logs service remapper. Allowed enum values: `service-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 5                                  | object          | The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.                                                                                                                                                                                                                                    | **Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                       |
| Option 5             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 5             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 5             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 5             | type [*required*]                    | enum            | Type of logs message remapper. Allowed enum values: `message-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 6                                  | object          | The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.                                                                                           |
| Option 6             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 6             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 6             | override_on_conflict                      | boolean         | Override or not the target element if already set,                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 6             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 6             | source_type                               | string          | Defines if the sources are from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 6             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 6             | target [*required*]                  | string          | Final attribute or tag name to remap the sources to.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 6             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 6             | target_type                               | string          | Defines if the final attribute or tag name is from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 6             | type [*required*]                    | enum            | Type of logs attribute remapper. Allowed enum values: `attribute-remapper`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 7                                  | object          | This processor extracts query parameters and other important parameters from a URL.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 7             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 7             | normalize_ending_slashes                  | boolean         | Normalize the ending slashes or not.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 7             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 7             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | type [*required*]                    | enum            | Type of logs URL parser. Allowed enum values: `url-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 8                                  | object          | The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.                                                                                                                                                                                                                                                                                |
| Option 8             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | is_encoded                                | boolean         | Define if the source attribute is URL encoded or not.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Option 8             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 8             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 8             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | type [*required*]                    | enum            | Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 9                                  | object          | Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.                                                                                                                                                           | **Notes**:                                                                                                                                                                                                             |
| Option 9             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | name                                      | string          | Value to assign to the target attribute.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 9             | target [*required*]                  | string          | Name of the target attribute which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 9             | type [*required*]                    | enum            | Type of logs category processor. Allowed enum values: `category-processor`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 10                                 | object          | Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.                                                                                                                              | The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.                                                                                                                                 | By default, the calculation is skipped if an attribute is missing. Select "Replace missing attribute by 0" to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number. | *Notes*:     |
| Option 10            | expression [*required*]              | string          | Arithmetic operation between one or more log attributes.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_replace_missing                        | boolean         | If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.                                                                                                                                                                                                                                                                                                                                        |
| Option 10            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 10            | target [*required*]                  | string          | Name of the attribute that contains the result of the arithmetic operation.                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 10            | type [*required*]                    | enum            | Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`                                                                                                                                                                                                                                                                                                                                                                                    |
| processors           | Option 11                                 | object          | Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.                                                                                                                                                                                                                        | The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.                                                                                                                               | **Notes**:                                                                                                                                                                                                                                                                                                               |
| Option 11            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 11            | is_replace_missing                        | boolean         | If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.                                                                                                                                                                                                                                                                                                                   |
| Option 11            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 11            | target [*required*]                  | string          | The name of the attribute that contains the result of the template.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | template [*required*]                | string          | A formula with one or more attributes and raw text.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | type [*required*]                    | enum            | Type of logs string builder processor. Allowed enum values: `string-builder-processor`                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 12                                 | object          | Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.                                                                                                                                                                                  | A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.                                                                                                          |
| Option 12            | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 12            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 12            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 12            | processors                                | [object]        | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 12            | type [*required*]                    | enum            | Type of logs pipeline processor. Allowed enum values: `pipeline`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 13                                 | object          | The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.                                                                                                                                                                                                                                                                                                  |
| Option 13            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 13            | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 13            | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | type [*required*]                    | enum            | Type of GeoIP parser. Allowed enum values: `geo-ip-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 14                                 | object          | Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.                                     |
| Option 14            | default_lookup                            | string          | Value to set the target attribute if the source value is not found in the list.                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 14            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 14            | lookup_table [*required*]            | [string]        | Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`                                                                                                                                                                                                                                                                                          |
| Option 14            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 14            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 14            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.                                                                                                                                                                                                                                                                                                                         |
| Option 14            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 15                                 | object          | **Note**: Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines. |
| Option 15            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 15            | lookup_enrichment_table [*required*] | string          | Name of the Reference Table for the source attribute and their associated target attribute values.                                                                                                                                                                                                                                                                                                                                                                |
| Option 15            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 15            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 15            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list.                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 15            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 16                                 | object          | There are two ways to improve correlation between application traces and logs.                                                                                                                                                                                                                                                                                                                                                                                    | Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.     | Use the Trace remapper processor to define a log attribute as its associated trace ID.                                                                                                                                                                                                                                   |
| Option 16            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 16            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 16            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 16            | type [*required*]                    | enum            | Type of logs trace remapper. Allowed enum values: `trace-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                             |
| processors           | Option 17                                 | object          | There are two ways to define correlation between application spans and logs:                                                                                                                                                                                                                                                                                                                                                                                      | Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default. | Use the span remapper processor to define a log attribute as its associated span ID.                                                                                                                                                                                                                                     |
| Option 17            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 17            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 17            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 17            | type [*required*]                    | enum            | Type of logs span remapper. Allowed enum values: `span-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                               |
| processors           | Option 18                                 | object          | A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:                                                                                                                                                                                                                                                                                                                                      |
| Option 18            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 18            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | operation [*required*]               |  <oneOf>   | Configuration of the array processor operation to perform.                                                                                                                                                                                                                                                                                                                                                                                                        |
| operation            | Option 1                                  | object          | Operation that appends a value to a target array attribute.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | source [*required*]                  | string          | Attribute path containing the value to append.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Option 1             | target [*required*]                  | string          | Attribute path of the array to append to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Operation type. Allowed enum values: `append`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 2                                  | object          | Operation that computes the length of a `source` array and stores the result in the `target` attribute.                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | source [*required*]                  | string          | Attribute path of the array to measure.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | target [*required*]                  | string          | Attribute that receives the computed length.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 2             | type [*required*]                    | enum            | Operation type. Allowed enum values: `length`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 3                                  | object          | Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.                                                                                                                                                                                                                                                                                                                              |
| Option 3             | filter [*required*]                  | string          | Filter condition expressed as `key:value` used to find the matching element.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | source [*required*]                  | string          | Attribute path of the array to search into.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | target [*required*]                  | string          | Attribute that receives the extracted value.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | type [*required*]                    | enum            | Operation type. Allowed enum values: `select`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 3             | value_to_extract [*required*]        | string          | Key of the value to extract from the matching element.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | type [*required*]                    | enum            | Type of logs array processor. Allowed enum values: `array-processor`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 19                                 | object          | The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.                                                                                                                                                                                                                                                                                    |
| Option 19            | binary_to_text_encoding [*required*] | enum            | The encoding used to represent the binary data. Allowed enum values: `base64,base16`                                                                                                                                                                                                                                                                                                                                                                              |
| Option 19            | input_representation [*required*]    | enum            | The original representation of input string. Allowed enum values: `utf_8,integer`                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | is_enabled                                | boolean         | Whether the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 19            | source [*required*]                  | string          | Name of the log attribute with the encoded data.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 19            | target [*required*]                  | string          | Name of the log attribute that contains the decoded data.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 19            | type [*required*]                    | enum            | Type of logs decoder processor. Allowed enum values: `decoder-processor`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 20                                 | object          | A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.                                                                                                                                                                                                                                                                                                                                         |
| Option 20            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 20            | mappers [*required*]                 | [ <oneOf>] | The `LogsSchemaProcessor` `mappers`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 1                                  | object          | The schema remapper maps source log fields to their correct fields.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                    | string          | Name of the logs schema remapper.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1             | override_on_conflict                      | boolean         | Override or not the target element if already set.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | target [*required*]                  | string          | Target field to map log source field to.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Type of logs schema remapper. Allowed enum values: `schema-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 2                                  | object          | Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.                                                                                                                                                                                                                                                                                      | **Notes**:                                                                                                                                                                                                             |
| Option 2             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter [*required*]                  | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | id [*required*]                      | int64           | ID to inject into the category.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| categories           | name [*required*]                    | string          | Value to assign to target schema field.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | fallback                                  | object          | Used to override hardcoded category values with a value pulled from a source attribute on the log.                                                                                                                                                                                                                                                                                                                                                                |
| fallback             | sources                                   | object          | Fallback sources used to populate value of field.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| additionalProperties | <any-key>                                 | [string]        |
| fallback             | values                                    | object          | Values that define when the fallback is used.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties | <any-key>                                 | string          |
| Option 2             | name [*required*]                    | string          | Name of the logs schema category mapper.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | targets [*required*]                 | object          | Name of the target attributes which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                    |
| targets              | id                                        | string          | ID of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| targets              | name                                      | string          | Name of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`                                                                                                                                                                                                                                                                                                                                                                                |
| Option 20            | name [*required*]                    | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 20            | schema [*required*]                  | object          | Configuration of the schema data to use.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| schema               | class_name [*required*]              | string          | Class name of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| schema               | class_uid [*required*]               | int64           | Class UID of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | profiles                                  | [string]        | Optional list of profiles to modify the schema.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | schema_type [*required*]             | string          | Type of schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| schema               | version [*required*]                 | string          | Version of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 20            | type [*required*]                    | enum            | Type of logs schema processor. Allowed enum values: `schema-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | tags                                      | [string]        | A list of tags associated with the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                      | type                                      | string          | Type of pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppend",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_to_array",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps"
      }
    }
  ],
  "tags": []
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendNoPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_remove_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": false
      }
    }
  ],
  "tags": []
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "source:python"
  },
  "name": "testPipelineArrayAppendPreserve",
  "processors": [
    {
      "type": "array-processor",
      "is_enabled": true,
      "name": "append_ip_and_keep_source",
      "operation": {
        "type": "append",
        "source": "network.client.ip",
        "target": "sourceIps",
        "preserve_source": true
      }
    }
  ],
  "tags": []
}
EOF

#####

```go
// Create a pipeline with Array Processor Append Operation returns "OK" response

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
    body := datadogV1.LogsPipeline{
        Filter: &datadogV1.LogsFilter{
            Query: datadog.PtrString("source:python"),
        },
        Name: "testPipelineArrayAppend",
        Processors: []datadogV1.LogsProcessor{
            datadogV1.LogsProcessor{
                LogsArrayProcessor: &datadogV1.LogsArrayProcessor{
                    Type:      datadogV1.LOGSARRAYPROCESSORTYPE_ARRAY_PROCESSOR,
                    IsEnabled: datadog.PtrBool(true),
                    Name:      datadog.PtrString("append_ip_to_array"),
                    Operation: datadogV1.LogsArrayProcessorOperation{
                        LogsArrayProcessorOperationAppend: &datadogV1.LogsArrayProcessorOperationAppend{
                            Type:   datadogV1.LOGSARRAYPROCESSOROPERATIONAPPENDTYPE_APPEND,
                            Source: "network.client.ip",
                            Target: "sourceIps",
                        }},
                }},
        },
        Tags: []string{},
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.CreateLogsPipeline(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.CreateLogsPipeline`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.CreateLogsPipeline`:\n%s\n", responseContent)
}
```

#####

```go
// Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response

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
    body := datadogV1.LogsPipeline{
        Filter: &datadogV1.LogsFilter{
            Query: datadog.PtrString("source:python"),
        },
        Name: "testPipelineArrayAppendNoPreserve",
        Processors: []datadogV1.LogsProcessor{
            datadogV1.LogsProcessor{
                LogsArrayProcessor: &datadogV1.LogsArrayProcessor{
                    Type:      datadogV1.LOGSARRAYPROCESSORTYPE_ARRAY_PROCESSOR,
                    IsEnabled: datadog.PtrBool(true),
                    Name:      datadog.PtrString("append_ip_and_remove_source"),
                    Operation: datadogV1.LogsArrayProcessorOperation{
                        LogsArrayProcessorOperationAppend: &datadogV1.LogsArrayProcessorOperationAppend{
                            Type:           datadogV1.LOGSARRAYPROCESSOROPERATIONAPPENDTYPE_APPEND,
                            Source:         "network.client.ip",
                            Target:         "sourceIps",
                            PreserveSource: datadog.PtrBool(false),
                        }},
                }},
        },
        Tags: []string{},
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.CreateLogsPipeline(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.CreateLogsPipeline`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.CreateLogsPipeline`:\n%s\n", responseContent)
}
```

#####

```go
// Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response

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
    body := datadogV1.LogsPipeline{
        Filter: &datadogV1.LogsFilter{
            Query: datadog.PtrString("source:python"),
        },
        Name: "testPipelineArrayAppendPreserve",
        Processors: []datadogV1.LogsProcessor{
            datadogV1.LogsProcessor{
                LogsArrayProcessor: &datadogV1.LogsArrayProcessor{
                    Type:      datadogV1.LOGSARRAYPROCESSORTYPE_ARRAY_PROCESSOR,
                    IsEnabled: datadog.PtrBool(true),
                    Name:      datadog.PtrString("append_ip_and_keep_source"),
                    Operation: datadogV1.LogsArrayProcessorOperation{
                        LogsArrayProcessorOperationAppend: &datadogV1.LogsArrayProcessorOperationAppend{
                            Type:           datadogV1.LOGSARRAYPROCESSOROPERATIONAPPENDTYPE_APPEND,
                            Source:         "network.client.ip",
                            Target:         "sourceIps",
                            PreserveSource: datadog.PtrBool(true),
                        }},
                }},
        },
        Tags: []string{},
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.CreateLogsPipeline(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.CreateLogsPipeline`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.CreateLogsPipeline`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a pipeline with Array Processor Append Operation returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsArrayProcessor;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperation;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppend;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppendType;
import com.datadog.api.client.v1.model.LogsArrayProcessorType;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("testPipelineArrayAppend")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsArrayProcessor()
                            .type(LogsArrayProcessorType.ARRAY_PROCESSOR)
                            .isEnabled(true)
                            .name("append_ip_to_array")
                            .operation(
                                new LogsArrayProcessorOperation(
                                    new LogsArrayProcessorOperationAppend()
                                        .type(LogsArrayProcessorOperationAppendType.APPEND)
                                        .source("network.client.ip")
                                        .target("sourceIps"))))));

    try {
      LogsPipeline result = apiInstance.createLogsPipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#createLogsPipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#####

```java
// Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK"
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsArrayProcessor;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperation;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppend;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppendType;
import com.datadog.api.client.v1.model.LogsArrayProcessorType;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("testPipelineArrayAppendNoPreserve")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsArrayProcessor()
                            .type(LogsArrayProcessorType.ARRAY_PROCESSOR)
                            .isEnabled(true)
                            .name("append_ip_and_remove_source")
                            .operation(
                                new LogsArrayProcessorOperation(
                                    new LogsArrayProcessorOperationAppend()
                                        .type(LogsArrayProcessorOperationAppendType.APPEND)
                                        .source("network.client.ip")
                                        .target("sourceIps")
                                        .preserveSource(false))))));

    try {
      LogsPipeline result = apiInstance.createLogsPipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#createLogsPipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#####

```java
// Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK"
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsArrayProcessor;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperation;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppend;
import com.datadog.api.client.v1.model.LogsArrayProcessorOperationAppendType;
import com.datadog.api.client.v1.model.LogsArrayProcessorType;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("testPipelineArrayAppendPreserve")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsArrayProcessor()
                            .type(LogsArrayProcessorType.ARRAY_PROCESSOR)
                            .isEnabled(true)
                            .name("append_ip_and_keep_source")
                            .operation(
                                new LogsArrayProcessorOperation(
                                    new LogsArrayProcessorOperationAppend()
                                        .type(LogsArrayProcessorOperationAppendType.APPEND)
                                        .source("network.client.ip")
                                        .target("sourceIps")
                                        .preserveSource(true))))));

    try {
      LogsPipeline result = apiInstance.createLogsPipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#createLogsPipeline");
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

```python
"""
Create a pipeline with Array Processor Append Operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
from datadog_api_client.v1.model.logs_array_processor_operation_append_type import LogsArrayProcessorOperationAppendType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayAppend",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="append_ip_to_array",
            operation=LogsArrayProcessorOperationAppend(
                type=LogsArrayProcessorOperationAppendType.APPEND,
                source="network.client.ip",
                target="sourceIps",
            ),
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
```

#####

```python
"""
Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
from datadog_api_client.v1.model.logs_array_processor_operation_append_type import LogsArrayProcessorOperationAppendType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayAppendNoPreserve",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="append_ip_and_remove_source",
            operation=LogsArrayProcessorOperationAppend(
                type=LogsArrayProcessorOperationAppendType.APPEND,
                source="network.client.ip",
                target="sourceIps",
                preserve_source=False,
            ),
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
```

#####

```python
"""
Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
from datadog_api_client.v1.model.logs_array_processor_operation_append_type import LogsArrayProcessorOperationAppendType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayAppendPreserve",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="append_ip_and_keep_source",
            operation=LogsArrayProcessorOperationAppend(
                type=LogsArrayProcessorOperationAppendType.APPEND,
                source="network.client.ip",
                target="sourceIps",
                preserve_source=True,
            ),
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a pipeline with Array Processor Append Operation returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "testPipelineArrayAppend",
  processors: [
    DatadogAPIClient::V1::LogsArrayProcessor.new({
      type: DatadogAPIClient::V1::LogsArrayProcessorType::ARRAY_PROCESSOR,
      is_enabled: true,
      name: "append_ip_to_array",
      operation: DatadogAPIClient::V1::LogsArrayProcessorOperationAppend.new({
        type: DatadogAPIClient::V1::LogsArrayProcessorOperationAppendType::APPEND,
        source: "network.client.ip",
        target: "sourceIps",
      }),
    }),
  ],
  tags: [],
})
p api_instance.create_logs_pipeline(body)
```

#####

```ruby
# Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "testPipelineArrayAppendNoPreserve",
  processors: [
    DatadogAPIClient::V1::LogsArrayProcessor.new({
      type: DatadogAPIClient::V1::LogsArrayProcessorType::ARRAY_PROCESSOR,
      is_enabled: true,
      name: "append_ip_and_remove_source",
      operation: DatadogAPIClient::V1::LogsArrayProcessorOperationAppend.new({
        type: DatadogAPIClient::V1::LogsArrayProcessorOperationAppendType::APPEND,
        source: "network.client.ip",
        target: "sourceIps",
        preserve_source: false,
      }),
    }),
  ],
  tags: [],
})
p api_instance.create_logs_pipeline(body)
```

#####

```ruby
# Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "testPipelineArrayAppendPreserve",
  processors: [
    DatadogAPIClient::V1::LogsArrayProcessor.new({
      type: DatadogAPIClient::V1::LogsArrayProcessorType::ARRAY_PROCESSOR,
      is_enabled: true,
      name: "append_ip_and_keep_source",
      operation: DatadogAPIClient::V1::LogsArrayProcessorOperationAppend.new({
        type: DatadogAPIClient::V1::LogsArrayProcessorOperationAppendType::APPEND,
        source: "network.client.ip",
        target: "sourceIps",
        preserve_source: true,
      }),
    }),
  ],
  tags: [],
})
p api_instance.create_logs_pipeline(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a pipeline with Array Processor Append Operation returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsArrayProcessor;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperation;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppend;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppendType;
use datadog_api_client::datadogV1::model::LogsArrayProcessorType;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("testPipelineArrayAppend".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsArrayProcessor(Box::new(
            LogsArrayProcessor::new(
                LogsArrayProcessorOperation::LogsArrayProcessorOperationAppend(Box::new(
                    LogsArrayProcessorOperationAppend::new(
                        "network.client.ip".to_string(),
                        "sourceIps".to_string(),
                        LogsArrayProcessorOperationAppendType::APPEND,
                    ),
                )),
                LogsArrayProcessorType::ARRAY_PROCESSOR,
            )
            .is_enabled(true)
            .name("append_ip_to_array".to_string()),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.create_logs_pipeline(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create a pipeline with Array Processor Append Operation with preserve_source
// false returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsArrayProcessor;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperation;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppend;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppendType;
use datadog_api_client::datadogV1::model::LogsArrayProcessorType;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("testPipelineArrayAppendNoPreserve".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsArrayProcessor(Box::new(
            LogsArrayProcessor::new(
                LogsArrayProcessorOperation::LogsArrayProcessorOperationAppend(Box::new(
                    LogsArrayProcessorOperationAppend::new(
                        "network.client.ip".to_string(),
                        "sourceIps".to_string(),
                        LogsArrayProcessorOperationAppendType::APPEND,
                    )
                    .preserve_source(false),
                )),
                LogsArrayProcessorType::ARRAY_PROCESSOR,
            )
            .is_enabled(true)
            .name("append_ip_and_remove_source".to_string()),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.create_logs_pipeline(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create a pipeline with Array Processor Append Operation with preserve_source
// true returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsArrayProcessor;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperation;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppend;
use datadog_api_client::datadogV1::model::LogsArrayProcessorOperationAppendType;
use datadog_api_client::datadogV1::model::LogsArrayProcessorType;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("testPipelineArrayAppendPreserve".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsArrayProcessor(Box::new(
            LogsArrayProcessor::new(
                LogsArrayProcessorOperation::LogsArrayProcessorOperationAppend(Box::new(
                    LogsArrayProcessorOperationAppend::new(
                        "network.client.ip".to_string(),
                        "sourceIps".to_string(),
                        LogsArrayProcessorOperationAppendType::APPEND,
                    )
                    .preserve_source(true),
                )),
                LogsArrayProcessorType::ARRAY_PROCESSOR,
            )
            .is_enabled(true)
            .name("append_ip_and_keep_source".to_string()),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.create_logs_pipeline(body).await;
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
 * Create a pipeline with Array Processor Append Operation returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiCreateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "testPipelineArrayAppend",
    processors: [
      {
        type: "array-processor",
        isEnabled: true,
        name: "append_ip_to_array",
        operation: {
          type: "append",
          source: "network.client.ip",
          target: "sourceIps",
        },
      },
    ],
    tags: [],
  },
};

apiInstance
  .createLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiCreateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "testPipelineArrayAppendNoPreserve",
    processors: [
      {
        type: "array-processor",
        isEnabled: true,
        name: "append_ip_and_remove_source",
        operation: {
          type: "append",
          source: "network.client.ip",
          target: "sourceIps",
          preserveSource: false,
        },
      },
    ],
    tags: [],
  },
};

apiInstance
  .createLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiCreateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "testPipelineArrayAppendPreserve",
    processors: [
      {
        type: "array-processor",
        isEnabled: true,
        name: "append_ip_and_keep_source",
        operation: {
          type: "append",
          source: "network.client.ip",
          target: "sourceIps",
          preserveSource: true,
        },
      },
    ],
    tags: [],
  },
};

apiInstance
  .createLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
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

## Get a pipeline{% #get-a-pipeline %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/logs/config/pipelines/{pipeline_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/logs/config/pipelines/{pipeline_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |

### Overview

Get a specific pipeline from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                |
| ----------------------------- | ------ | -------------------------- |
| pipeline_id [*required*] | string | ID of the pipeline to get. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}


Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.

**Note**: These endpoints are only available for admin users. Make sure to use an application key created by an admin.



| Parent field         | Field                                     | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | description                               | string          | A description of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | id                                        | string          | ID of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | is_enabled                                | boolean         | Whether or not the pipeline is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                      | is_read_only                              | boolean         | Whether or not the pipeline can be edited.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | name [*required*]                    | string          | Name of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | processors                                | [ <oneOf>] | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 1                                  | object          | Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).                                                                                                                                                                         |
| Option 1             | grok [*required*]                    | object          | Set of rules for the grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | match_rules [*required*]             | string          | List of match rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | support_rules                             | string          | List of support rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 1             | samples                                   | [string]        | List of sample logs to test this grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | source [*required*]                  | string          | Name of the log attribute to parse.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | type [*required*]                    | enum            | Type of logs grok parser. Allowed enum values: `grok-parser`                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 2                                  | object          | As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.                                                                                                                                                                                                                                                                                                                                                             | `timestamp`                                                                                                                                                                                                            | `date`                                                                                                                                                                                                                                                                                                                   | `_timestamp` | `Timestamp` | `eventTime` | `published_date` | If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164. | **Note:** If your logs don't contain any of the default attributes and you haven't defined your own date attribute, Datadog timestamps the logs with the date it received them. | If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account. |
| Option 2             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 2             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs date remapper. Allowed enum values: `date-remapper`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 3                                  | object          | Use this Processor if you want to assign some attributes as the official status.                                                                                                                                                                                                                                                                                                                                                                                  | Each incoming status value is mapped as follows.                                                                                                                                                                       | **Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.                                                                                                                                                         |
| Option 3             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 3             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 3             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | type [*required*]                    | enum            | Type of logs status remapper. Allowed enum values: `status-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 4                                  | object          | Use this processor if you want to assign one or more attributes as the official service.                                                                                                                                                                                                                                                                                                                                                                          | **Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                           |
| Option 4             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 4             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 4             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 4             | type [*required*]                    | enum            | Type of logs service remapper. Allowed enum values: `service-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 5                                  | object          | The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.                                                                                                                                                                                                                                    | **Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                       |
| Option 5             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 5             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 5             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 5             | type [*required*]                    | enum            | Type of logs message remapper. Allowed enum values: `message-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 6                                  | object          | The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.                                                                                           |
| Option 6             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 6             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 6             | override_on_conflict                      | boolean         | Override or not the target element if already set,                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 6             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 6             | source_type                               | string          | Defines if the sources are from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 6             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 6             | target [*required*]                  | string          | Final attribute or tag name to remap the sources to.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 6             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 6             | target_type                               | string          | Defines if the final attribute or tag name is from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 6             | type [*required*]                    | enum            | Type of logs attribute remapper. Allowed enum values: `attribute-remapper`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 7                                  | object          | This processor extracts query parameters and other important parameters from a URL.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 7             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 7             | normalize_ending_slashes                  | boolean         | Normalize the ending slashes or not.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 7             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 7             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | type [*required*]                    | enum            | Type of logs URL parser. Allowed enum values: `url-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 8                                  | object          | The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.                                                                                                                                                                                                                                                                                |
| Option 8             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | is_encoded                                | boolean         | Define if the source attribute is URL encoded or not.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Option 8             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 8             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 8             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | type [*required*]                    | enum            | Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 9                                  | object          | Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.                                                                                                                                                           | **Notes**:                                                                                                                                                                                                             |
| Option 9             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | name                                      | string          | Value to assign to the target attribute.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 9             | target [*required*]                  | string          | Name of the target attribute which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 9             | type [*required*]                    | enum            | Type of logs category processor. Allowed enum values: `category-processor`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 10                                 | object          | Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.                                                                                                                              | The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.                                                                                                                                 | By default, the calculation is skipped if an attribute is missing. Select "Replace missing attribute by 0" to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number. | *Notes*:     |
| Option 10            | expression [*required*]              | string          | Arithmetic operation between one or more log attributes.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_replace_missing                        | boolean         | If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.                                                                                                                                                                                                                                                                                                                                        |
| Option 10            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 10            | target [*required*]                  | string          | Name of the attribute that contains the result of the arithmetic operation.                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 10            | type [*required*]                    | enum            | Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`                                                                                                                                                                                                                                                                                                                                                                                    |
| processors           | Option 11                                 | object          | Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.                                                                                                                                                                                                                        | The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.                                                                                                                               | **Notes**:                                                                                                                                                                                                                                                                                                               |
| Option 11            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 11            | is_replace_missing                        | boolean         | If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.                                                                                                                                                                                                                                                                                                                   |
| Option 11            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 11            | target [*required*]                  | string          | The name of the attribute that contains the result of the template.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | template [*required*]                | string          | A formula with one or more attributes and raw text.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | type [*required*]                    | enum            | Type of logs string builder processor. Allowed enum values: `string-builder-processor`                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 12                                 | object          | Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.                                                                                                                                                                                  | A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.                                                                                                          |
| Option 12            | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 12            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 12            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 12            | processors                                | [object]        | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 12            | type [*required*]                    | enum            | Type of logs pipeline processor. Allowed enum values: `pipeline`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 13                                 | object          | The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.                                                                                                                                                                                                                                                                                                  |
| Option 13            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 13            | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 13            | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | type [*required*]                    | enum            | Type of GeoIP parser. Allowed enum values: `geo-ip-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 14                                 | object          | Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.                                     |
| Option 14            | default_lookup                            | string          | Value to set the target attribute if the source value is not found in the list.                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 14            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 14            | lookup_table [*required*]            | [string]        | Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`                                                                                                                                                                                                                                                                                          |
| Option 14            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 14            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 14            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.                                                                                                                                                                                                                                                                                                                         |
| Option 14            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 15                                 | object          | **Note**: Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines. |
| Option 15            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 15            | lookup_enrichment_table [*required*] | string          | Name of the Reference Table for the source attribute and their associated target attribute values.                                                                                                                                                                                                                                                                                                                                                                |
| Option 15            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 15            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 15            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list.                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 15            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 16                                 | object          | There are two ways to improve correlation between application traces and logs.                                                                                                                                                                                                                                                                                                                                                                                    | Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.     | Use the Trace remapper processor to define a log attribute as its associated trace ID.                                                                                                                                                                                                                                   |
| Option 16            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 16            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 16            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 16            | type [*required*]                    | enum            | Type of logs trace remapper. Allowed enum values: `trace-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                             |
| processors           | Option 17                                 | object          | There are two ways to define correlation between application spans and logs:                                                                                                                                                                                                                                                                                                                                                                                      | Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default. | Use the span remapper processor to define a log attribute as its associated span ID.                                                                                                                                                                                                                                     |
| Option 17            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 17            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 17            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 17            | type [*required*]                    | enum            | Type of logs span remapper. Allowed enum values: `span-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                               |
| processors           | Option 18                                 | object          | A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:                                                                                                                                                                                                                                                                                                                                      |
| Option 18            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 18            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | operation [*required*]               |  <oneOf>   | Configuration of the array processor operation to perform.                                                                                                                                                                                                                                                                                                                                                                                                        |
| operation            | Option 1                                  | object          | Operation that appends a value to a target array attribute.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | source [*required*]                  | string          | Attribute path containing the value to append.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Option 1             | target [*required*]                  | string          | Attribute path of the array to append to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Operation type. Allowed enum values: `append`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 2                                  | object          | Operation that computes the length of a `source` array and stores the result in the `target` attribute.                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | source [*required*]                  | string          | Attribute path of the array to measure.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | target [*required*]                  | string          | Attribute that receives the computed length.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 2             | type [*required*]                    | enum            | Operation type. Allowed enum values: `length`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 3                                  | object          | Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.                                                                                                                                                                                                                                                                                                                              |
| Option 3             | filter [*required*]                  | string          | Filter condition expressed as `key:value` used to find the matching element.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | source [*required*]                  | string          | Attribute path of the array to search into.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | target [*required*]                  | string          | Attribute that receives the extracted value.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | type [*required*]                    | enum            | Operation type. Allowed enum values: `select`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 3             | value_to_extract [*required*]        | string          | Key of the value to extract from the matching element.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | type [*required*]                    | enum            | Type of logs array processor. Allowed enum values: `array-processor`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 19                                 | object          | The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.                                                                                                                                                                                                                                                                                    |
| Option 19            | binary_to_text_encoding [*required*] | enum            | The encoding used to represent the binary data. Allowed enum values: `base64,base16`                                                                                                                                                                                                                                                                                                                                                                              |
| Option 19            | input_representation [*required*]    | enum            | The original representation of input string. Allowed enum values: `utf_8,integer`                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | is_enabled                                | boolean         | Whether the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 19            | source [*required*]                  | string          | Name of the log attribute with the encoded data.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 19            | target [*required*]                  | string          | Name of the log attribute that contains the decoded data.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 19            | type [*required*]                    | enum            | Type of logs decoder processor. Allowed enum values: `decoder-processor`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 20                                 | object          | A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.                                                                                                                                                                                                                                                                                                                                         |
| Option 20            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 20            | mappers [*required*]                 | [ <oneOf>] | The `LogsSchemaProcessor` `mappers`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 1                                  | object          | The schema remapper maps source log fields to their correct fields.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                    | string          | Name of the logs schema remapper.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1             | override_on_conflict                      | boolean         | Override or not the target element if already set.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | target [*required*]                  | string          | Target field to map log source field to.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Type of logs schema remapper. Allowed enum values: `schema-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 2                                  | object          | Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.                                                                                                                                                                                                                                                                                      | **Notes**:                                                                                                                                                                                                             |
| Option 2             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter [*required*]                  | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | id [*required*]                      | int64           | ID to inject into the category.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| categories           | name [*required*]                    | string          | Value to assign to target schema field.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | fallback                                  | object          | Used to override hardcoded category values with a value pulled from a source attribute on the log.                                                                                                                                                                                                                                                                                                                                                                |
| fallback             | sources                                   | object          | Fallback sources used to populate value of field.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| additionalProperties | <any-key>                                 | [string]        |
| fallback             | values                                    | object          | Values that define when the fallback is used.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties | <any-key>                                 | string          |
| Option 2             | name [*required*]                    | string          | Name of the logs schema category mapper.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | targets [*required*]                 | object          | Name of the target attributes which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                    |
| targets              | id                                        | string          | ID of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| targets              | name                                      | string          | Name of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`                                                                                                                                                                                                                                                                                                                                                                                |
| Option 20            | name [*required*]                    | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 20            | schema [*required*]                  | object          | Configuration of the schema data to use.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| schema               | class_name [*required*]              | string          | Class name of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| schema               | class_uid [*required*]               | int64           | Class UID of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | profiles                                  | [string]        | Optional list of profiles to modify the schema.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | schema_type [*required*]             | string          | Type of schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| schema               | version [*required*]                 | string          | Version of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 20            | type [*required*]                    | enum            | Type of logs schema processor. Allowed enum values: `schema-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | tags                                      | [string]        | A list of tags associated with the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                      | type                                      | string          | Type of pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport pipeline_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.get_logs_pipeline(
        pipeline_id="pipeline_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a pipeline returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.get_logs_pipeline("pipeline_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a pipeline returns "OK" response

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
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.GetLogsPipeline(ctx, "pipeline_id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.GetLogsPipeline`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.GetLogsPipeline`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsPipeline;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      LogsPipeline result = apiInstance.getLogsPipeline("pipeline_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#getLogsPipeline");
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
// Get a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.get_logs_pipeline("pipeline_id".to_string()).await;
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
 * Get a pipeline returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiGetLogsPipelineRequest = {
  pipelineId: "pipeline_id",
};

apiInstance
  .getLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
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

## Delete a pipeline{% #delete-a-pipeline %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/logs/config/pipelines/{pipeline_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/logs/config/pipelines/{pipeline_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |

### Overview

Delete a given pipeline from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_write_pipelines` permission.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                   |
| ----------------------------- | ------ | ----------------------------- |
| pipeline_id [*required*] | string | ID of the pipeline to delete. |

### Response

{% tab title="200" %}
OK
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport pipeline_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    api_instance.delete_logs_pipeline(
        pipeline_id="pipeline_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a pipeline returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new
p api_instance.delete_logs_pipeline("pipeline_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a pipeline returns "OK" response

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
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    r, err := api.DeleteLogsPipeline(ctx, "pipeline_id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.DeleteLogsPipeline`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    try {
      apiInstance.deleteLogsPipeline("pipeline_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#deleteLogsPipeline");
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
// Delete a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api.delete_logs_pipeline("pipeline_id".to_string()).await;
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
 * Delete a pipeline returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiDeleteLogsPipelineRequest = {
  pipelineId: "pipeline_id",
};

apiInstance
  .deleteLogsPipeline(params)
  .then((data: any) => {
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

## Update a pipeline{% #update-a-pipeline %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/logs/config/pipelines/{pipeline_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/logs/config/pipelines/{pipeline_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/{pipeline_id} |

### Overview



Update a given pipeline configuration to change it's processors or their order.

**Note**: Using this method updates your pipeline configuration by **replacing** your current configuration with the new one sent to your Datadog organization.
This endpoint requires the `logs_write_pipelines` permission.


### Arguments

#### Path Parameters

| Name                          | Type   | Description                   |
| ----------------------------- | ------ | ----------------------------- |
| pipeline_id [*required*] | string | ID of the pipeline to delete. |

### Request

#### Body Data (required)

New definition of the pipeline.

{% tab title="Model" %}

| Parent field         | Field                                     | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | description                               | string          | A description of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | id                                        | string          | ID of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | is_enabled                                | boolean         | Whether or not the pipeline is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                      | is_read_only                              | boolean         | Whether or not the pipeline can be edited.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | name [*required*]                    | string          | Name of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | processors                                | [ <oneOf>] | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 1                                  | object          | Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).                                                                                                                                                                         |
| Option 1             | grok [*required*]                    | object          | Set of rules for the grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | match_rules [*required*]             | string          | List of match rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | support_rules                             | string          | List of support rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 1             | samples                                   | [string]        | List of sample logs to test this grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | source [*required*]                  | string          | Name of the log attribute to parse.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | type [*required*]                    | enum            | Type of logs grok parser. Allowed enum values: `grok-parser`                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 2                                  | object          | As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.                                                                                                                                                                                                                                                                                                                                                             | `timestamp`                                                                                                                                                                                                            | `date`                                                                                                                                                                                                                                                                                                                   | `_timestamp` | `Timestamp` | `eventTime` | `published_date` | If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164. | **Note:** If your logs don't contain any of the default attributes and you haven't defined your own date attribute, Datadog timestamps the logs with the date it received them. | If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account. |
| Option 2             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 2             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs date remapper. Allowed enum values: `date-remapper`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 3                                  | object          | Use this Processor if you want to assign some attributes as the official status.                                                                                                                                                                                                                                                                                                                                                                                  | Each incoming status value is mapped as follows.                                                                                                                                                                       | **Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.                                                                                                                                                         |
| Option 3             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 3             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 3             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | type [*required*]                    | enum            | Type of logs status remapper. Allowed enum values: `status-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 4                                  | object          | Use this processor if you want to assign one or more attributes as the official service.                                                                                                                                                                                                                                                                                                                                                                          | **Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                           |
| Option 4             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 4             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 4             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 4             | type [*required*]                    | enum            | Type of logs service remapper. Allowed enum values: `service-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 5                                  | object          | The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.                                                                                                                                                                                                                                    | **Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                       |
| Option 5             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 5             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 5             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 5             | type [*required*]                    | enum            | Type of logs message remapper. Allowed enum values: `message-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 6                                  | object          | The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.                                                                                           |
| Option 6             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 6             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 6             | override_on_conflict                      | boolean         | Override or not the target element if already set,                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 6             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 6             | source_type                               | string          | Defines if the sources are from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 6             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 6             | target [*required*]                  | string          | Final attribute or tag name to remap the sources to.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 6             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 6             | target_type                               | string          | Defines if the final attribute or tag name is from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 6             | type [*required*]                    | enum            | Type of logs attribute remapper. Allowed enum values: `attribute-remapper`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 7                                  | object          | This processor extracts query parameters and other important parameters from a URL.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 7             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 7             | normalize_ending_slashes                  | boolean         | Normalize the ending slashes or not.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 7             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 7             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | type [*required*]                    | enum            | Type of logs URL parser. Allowed enum values: `url-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 8                                  | object          | The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.                                                                                                                                                                                                                                                                                |
| Option 8             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | is_encoded                                | boolean         | Define if the source attribute is URL encoded or not.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Option 8             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 8             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 8             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | type [*required*]                    | enum            | Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 9                                  | object          | Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.                                                                                                                                                           | **Notes**:                                                                                                                                                                                                             |
| Option 9             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | name                                      | string          | Value to assign to the target attribute.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 9             | target [*required*]                  | string          | Name of the target attribute which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 9             | type [*required*]                    | enum            | Type of logs category processor. Allowed enum values: `category-processor`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 10                                 | object          | Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.                                                                                                                              | The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.                                                                                                                                 | By default, the calculation is skipped if an attribute is missing. Select "Replace missing attribute by 0" to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number. | *Notes*:     |
| Option 10            | expression [*required*]              | string          | Arithmetic operation between one or more log attributes.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_replace_missing                        | boolean         | If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.                                                                                                                                                                                                                                                                                                                                        |
| Option 10            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 10            | target [*required*]                  | string          | Name of the attribute that contains the result of the arithmetic operation.                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 10            | type [*required*]                    | enum            | Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`                                                                                                                                                                                                                                                                                                                                                                                    |
| processors           | Option 11                                 | object          | Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.                                                                                                                                                                                                                        | The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.                                                                                                                               | **Notes**:                                                                                                                                                                                                                                                                                                               |
| Option 11            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 11            | is_replace_missing                        | boolean         | If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.                                                                                                                                                                                                                                                                                                                   |
| Option 11            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 11            | target [*required*]                  | string          | The name of the attribute that contains the result of the template.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | template [*required*]                | string          | A formula with one or more attributes and raw text.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | type [*required*]                    | enum            | Type of logs string builder processor. Allowed enum values: `string-builder-processor`                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 12                                 | object          | Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.                                                                                                                                                                                  | A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.                                                                                                          |
| Option 12            | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 12            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 12            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 12            | processors                                | [object]        | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 12            | type [*required*]                    | enum            | Type of logs pipeline processor. Allowed enum values: `pipeline`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 13                                 | object          | The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.                                                                                                                                                                                                                                                                                                  |
| Option 13            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 13            | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 13            | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | type [*required*]                    | enum            | Type of GeoIP parser. Allowed enum values: `geo-ip-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 14                                 | object          | Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.                                     |
| Option 14            | default_lookup                            | string          | Value to set the target attribute if the source value is not found in the list.                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 14            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 14            | lookup_table [*required*]            | [string]        | Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`                                                                                                                                                                                                                                                                                          |
| Option 14            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 14            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 14            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.                                                                                                                                                                                                                                                                                                                         |
| Option 14            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 15                                 | object          | **Note**: Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines. |
| Option 15            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 15            | lookup_enrichment_table [*required*] | string          | Name of the Reference Table for the source attribute and their associated target attribute values.                                                                                                                                                                                                                                                                                                                                                                |
| Option 15            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 15            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 15            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list.                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 15            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 16                                 | object          | There are two ways to improve correlation between application traces and logs.                                                                                                                                                                                                                                                                                                                                                                                    | Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.     | Use the Trace remapper processor to define a log attribute as its associated trace ID.                                                                                                                                                                                                                                   |
| Option 16            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 16            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 16            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 16            | type [*required*]                    | enum            | Type of logs trace remapper. Allowed enum values: `trace-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                             |
| processors           | Option 17                                 | object          | There are two ways to define correlation between application spans and logs:                                                                                                                                                                                                                                                                                                                                                                                      | Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default. | Use the span remapper processor to define a log attribute as its associated span ID.                                                                                                                                                                                                                                     |
| Option 17            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 17            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 17            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 17            | type [*required*]                    | enum            | Type of logs span remapper. Allowed enum values: `span-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                               |
| processors           | Option 18                                 | object          | A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:                                                                                                                                                                                                                                                                                                                                      |
| Option 18            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 18            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | operation [*required*]               |  <oneOf>   | Configuration of the array processor operation to perform.                                                                                                                                                                                                                                                                                                                                                                                                        |
| operation            | Option 1                                  | object          | Operation that appends a value to a target array attribute.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | source [*required*]                  | string          | Attribute path containing the value to append.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Option 1             | target [*required*]                  | string          | Attribute path of the array to append to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Operation type. Allowed enum values: `append`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 2                                  | object          | Operation that computes the length of a `source` array and stores the result in the `target` attribute.                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | source [*required*]                  | string          | Attribute path of the array to measure.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | target [*required*]                  | string          | Attribute that receives the computed length.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 2             | type [*required*]                    | enum            | Operation type. Allowed enum values: `length`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 3                                  | object          | Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.                                                                                                                                                                                                                                                                                                                              |
| Option 3             | filter [*required*]                  | string          | Filter condition expressed as `key:value` used to find the matching element.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | source [*required*]                  | string          | Attribute path of the array to search into.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | target [*required*]                  | string          | Attribute that receives the extracted value.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | type [*required*]                    | enum            | Operation type. Allowed enum values: `select`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 3             | value_to_extract [*required*]        | string          | Key of the value to extract from the matching element.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | type [*required*]                    | enum            | Type of logs array processor. Allowed enum values: `array-processor`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 19                                 | object          | The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.                                                                                                                                                                                                                                                                                    |
| Option 19            | binary_to_text_encoding [*required*] | enum            | The encoding used to represent the binary data. Allowed enum values: `base64,base16`                                                                                                                                                                                                                                                                                                                                                                              |
| Option 19            | input_representation [*required*]    | enum            | The original representation of input string. Allowed enum values: `utf_8,integer`                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | is_enabled                                | boolean         | Whether the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 19            | source [*required*]                  | string          | Name of the log attribute with the encoded data.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 19            | target [*required*]                  | string          | Name of the log attribute that contains the decoded data.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 19            | type [*required*]                    | enum            | Type of logs decoder processor. Allowed enum values: `decoder-processor`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 20                                 | object          | A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.                                                                                                                                                                                                                                                                                                                                         |
| Option 20            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 20            | mappers [*required*]                 | [ <oneOf>] | The `LogsSchemaProcessor` `mappers`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 1                                  | object          | The schema remapper maps source log fields to their correct fields.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                    | string          | Name of the logs schema remapper.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1             | override_on_conflict                      | boolean         | Override or not the target element if already set.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | target [*required*]                  | string          | Target field to map log source field to.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Type of logs schema remapper. Allowed enum values: `schema-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 2                                  | object          | Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.                                                                                                                                                                                                                                                                                      | **Notes**:                                                                                                                                                                                                             |
| Option 2             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter [*required*]                  | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | id [*required*]                      | int64           | ID to inject into the category.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| categories           | name [*required*]                    | string          | Value to assign to target schema field.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | fallback                                  | object          | Used to override hardcoded category values with a value pulled from a source attribute on the log.                                                                                                                                                                                                                                                                                                                                                                |
| fallback             | sources                                   | object          | Fallback sources used to populate value of field.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| additionalProperties | <any-key>                                 | [string]        |
| fallback             | values                                    | object          | Values that define when the fallback is used.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties | <any-key>                                 | string          |
| Option 2             | name [*required*]                    | string          | Name of the logs schema category mapper.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | targets [*required*]                 | object          | Name of the target attributes which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                    |
| targets              | id                                        | string          | ID of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| targets              | name                                      | string          | Name of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`                                                                                                                                                                                                                                                                                                                                                                                |
| Option 20            | name [*required*]                    | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 20            | schema [*required*]                  | object          | Configuration of the schema data to use.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| schema               | class_name [*required*]              | string          | Class name of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| schema               | class_uid [*required*]               | int64           | Class UID of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | profiles                                  | [string]        | Optional list of profiles to modify the schema.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | schema_type [*required*]             | string          | Type of schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| schema               | version [*required*]                 | string          | Version of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 20            | type [*required*]                    | enum            | Type of logs schema processor. Allowed enum values: `schema-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | tags                                      | [string]        | A list of tags associated with the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                      | type                                      | string          | Type of pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "is_enabled": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": []
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}


Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.

**Note**: These endpoints are only available for admin users. Make sure to use an application key created by an admin.



| Parent field         | Field                                     | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | description                               | string          | A description of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | id                                        | string          | ID of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | is_enabled                                | boolean         | Whether or not the pipeline is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                      | is_read_only                              | boolean         | Whether or not the pipeline can be edited.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | name [*required*]                    | string          | Name of the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | processors                                | [ <oneOf>] | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 1                                  | object          | Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/log_configuration/parsing).                                                                                                                                                                         |
| Option 1             | grok [*required*]                    | object          | Set of rules for the grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | match_rules [*required*]             | string          | List of match rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                                 |
| grok                 | support_rules                             | string          | List of support rules for the grok parser, separated by a new line.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 1             | samples                                   | [string]        | List of sample logs to test this grok parser.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | source [*required*]                  | string          | Name of the log attribute to parse.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | type [*required*]                    | enum            | Type of logs grok parser. Allowed enum values: `grok-parser`                                                                                                                                                                                                                                                                                                                                                                                                      |
| processors           | Option 2                                  | object          | As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.                                                                                                                                                                                                                                                                                                                                                             | `timestamp`                                                                                                                                                                                                            | `date`                                                                                                                                                                                                                                                                                                                   | `_timestamp` | `Timestamp` | `eventTime` | `published_date` | If your logs put their dates in an attribute not in this list, use the log date Remapper Processor to define their date attribute as the official log timestamp. The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164. | **Note:** If your logs don't contain any of the default attributes and you haven't defined your own date attribute, Datadog timestamps the logs with the date it received them. | If multiple log date remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account. |
| Option 2             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 2             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs date remapper. Allowed enum values: `date-remapper`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 3                                  | object          | Use this Processor if you want to assign some attributes as the official status.                                                                                                                                                                                                                                                                                                                                                                                  | Each incoming status value is mapped as follows.                                                                                                                                                                       | **Note:** If multiple log status remapper processors can be applied to a given log, only the first one (according to the pipelines order) is taken into account.                                                                                                                                                         |
| Option 3             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 3             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 3             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | type [*required*]                    | enum            | Type of logs status remapper. Allowed enum values: `status-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 4                                  | object          | Use this processor if you want to assign one or more attributes as the official service.                                                                                                                                                                                                                                                                                                                                                                          | **Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                           |
| Option 4             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 4             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 4             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 4             | type [*required*]                    | enum            | Type of logs service remapper. Allowed enum values: `service-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 5                                  | object          | The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message.                                                                                                                                                                                                                                    | **Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.                                                       |
| Option 5             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 5             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 5             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 5             | type [*required*]                    | enum            | Type of logs message remapper. Allowed enum values: `message-remapper`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 6                                  | object          | The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.                                                                                           |
| Option 6             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 6             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 6             | override_on_conflict                      | boolean         | Override or not the target element if already set,                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 6             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 6             | source_type                               | string          | Defines if the sources are from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 6             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 6             | target [*required*]                  | string          | Final attribute or tag name to remap the sources to.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 6             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 6             | target_type                               | string          | Defines if the final attribute or tag name is from log `attribute` or `tag`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 6             | type [*required*]                    | enum            | Type of logs attribute remapper. Allowed enum values: `attribute-remapper`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 7                                  | object          | This processor extracts query parameters and other important parameters from a URL.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 7             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 7             | normalize_ending_slashes                  | boolean         | Normalize the ending slashes or not.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Option 7             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 7             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 7             | type [*required*]                    | enum            | Type of logs URL parser. Allowed enum values: `url-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 8                                  | object          | The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.                                                                                                                                                                                                                                                                                |
| Option 8             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | is_encoded                                | boolean         | Define if the source attribute is URL encoded or not.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Option 8             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 8             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 8             | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 8             | type [*required*]                    | enum            | Type of logs User-Agent parser. Allowed enum values: `user-agent-parser`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 9                                  | object          | Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log matching a provided search query. Use categories to create groups for an analytical view. For example, URL groups, machine groups, environments, and response time buckets.                                                                                                                                                           | **Notes**:                                                                                                                                                                                                             |
| Option 9             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | name                                      | string          | Value to assign to the target attribute.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 9             | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 9             | target [*required*]                  | string          | Name of the target attribute which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 9             | type [*required*]                    | enum            | Type of logs category processor. Allowed enum values: `category-processor`                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 10                                 | object          | Use the Arithmetic Processor to add a new attribute (without spaces or special characters in the new attribute name) to a log with the result of the provided formula. This enables you to remap different time attributes with different units into a single attribute, or to compute operations on attributes within the same log.                                                                                                                              | The formula can use parentheses and the basic arithmetic operators `-`, `+`, `*`, `/`.                                                                                                                                 | By default, the calculation is skipped if an attribute is missing. Select "Replace missing attribute by 0" to automatically populate missing attribute values with 0 to ensure that the calculation is done. An attribute is missing if it is not found in the log attributes, or if it cannot be converted to a number. | *Notes*:     |
| Option 10            | expression [*required*]              | string          | Arithmetic operation between one or more log attributes.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 10            | is_replace_missing                        | boolean         | If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.                                                                                                                                                                                                                                                                                                                                        |
| Option 10            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 10            | target [*required*]                  | string          | Name of the attribute that contains the result of the arithmetic operation.                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 10            | type [*required*]                    | enum            | Type of logs arithmetic processor. Allowed enum values: `arithmetic-processor`                                                                                                                                                                                                                                                                                                                                                                                    |
| processors           | Option 11                                 | object          | Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.                                                                                                                                                                                                                        | The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.                                                                                                                               | **Notes**:                                                                                                                                                                                                                                                                                                               |
| Option 11            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 11            | is_replace_missing                        | boolean         | If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.                                                                                                                                                                                                                                                                                                                   |
| Option 11            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 11            | target [*required*]                  | string          | The name of the attribute that contains the result of the template.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | template [*required*]                | string          | A formula with one or more attributes and raw text.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 11            | type [*required*]                    | enum            | Type of logs string builder processor. Allowed enum values: `string-builder-processor`                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 12                                 | object          | Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.                                                                                                                                                                                  | A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.                                                                                                          |
| Option 12            | filter                                    | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 12            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 12            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 12            | processors                                | [object]        | Ordered list of processors in this pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 12            | type [*required*]                    | enum            | Type of logs pipeline processor. Allowed enum values: `pipeline`                                                                                                                                                                                                                                                                                                                                                                                                  |
| processors           | Option 13                                 | object          | The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.                                                                                                                                                                                                                                                                                                  |
| Option 13            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 13            | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 13            | target [*required*]                  | string          | Name of the parent attribute that contains all the extracted details from the `sources`.                                                                                                                                                                                                                                                                                                                                                                          |
| Option 13            | type [*required*]                    | enum            | Type of GeoIP parser. Allowed enum values: `geo-ip-parser`                                                                                                                                                                                                                                                                                                                                                                                                        |
| processors           | Option 14                                 | object          | Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in the processors mapping table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines.                                     |
| Option 14            | default_lookup                            | string          | Value to set the target attribute if the source value is not found in the list.                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 14            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 14            | lookup_table [*required*]            | [string]        | Mapping table of values for the source attribute and their associated target attribute values, formatted as `["source_key1,target_value1", "source_key2,target_value2"]`                                                                                                                                                                                                                                                                                          |
| Option 14            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 14            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 14            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.                                                                                                                                                                                                                                                                                                                         |
| Option 14            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 15                                 | object          | **Note**: Reference Tables are in public beta. Use the Lookup Processor to define a mapping between a log attribute and a human readable value saved in a Reference Table. For example, you can use the Lookup Processor to map an internal service ID into a human readable service name. Alternatively, you could also use it to check if the MAC address that just attempted to connect to the production environment belongs to your list of stolen machines. |
| Option 15            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 15            | lookup_enrichment_table [*required*] | string          | Name of the Reference Table for the source attribute and their associated target attribute values.                                                                                                                                                                                                                                                                                                                                                                |
| Option 15            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 15            | source [*required*]                  | string          | Source attribute used to perform the lookup.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 15            | target [*required*]                  | string          | Name of the attribute that contains the corresponding value in the mapping list.                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 15            | type [*required*]                    | enum            | Type of logs lookup processor. Allowed enum values: `lookup-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
| processors           | Option 16                                 | object          | There are two ways to improve correlation between application traces and logs.                                                                                                                                                                                                                                                                                                                                                                                    | Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces) and by default log integrations take care of all the rest of the setup.     | Use the Trace remapper processor to define a log attribute as its associated trace ID.                                                                                                                                                                                                                                   |
| Option 16            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 16            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 16            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 16            | type [*required*]                    | enum            | Type of logs trace remapper. Allowed enum values: `trace-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                             |
| processors           | Option 17                                 | object          | There are two ways to define correlation between application spans and logs:                                                                                                                                                                                                                                                                                                                                                                                      | Follow the documentation on [how to inject a span ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces). Log integrations automatically handle all remaining setup steps by default. | Use the span remapper processor to define a log attribute as its associated span ID.                                                                                                                                                                                                                                     |
| Option 17            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 17            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 17            | sources                                   | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 17            | type [*required*]                    | enum            | Type of logs span remapper. Allowed enum values: `span-id-remapper`                                                                                                                                                                                                                                                                                                                                                                                               |
| processors           | Option 18                                 | object          | A processor for extracting, aggregating, or transforming values from JSON arrays within your logs. Supported operations are:                                                                                                                                                                                                                                                                                                                                      |
| Option 18            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 18            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | operation [*required*]               |  <oneOf>   | Configuration of the array processor operation to perform.                                                                                                                                                                                                                                                                                                                                                                                                        |
| operation            | Option 1                                  | object          | Operation that appends a value to a target array attribute.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | source [*required*]                  | string          | Attribute path containing the value to append.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Option 1             | target [*required*]                  | string          | Attribute path of the array to append to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Operation type. Allowed enum values: `append`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 2                                  | object          | Operation that computes the length of a `source` array and stores the result in the `target` attribute.                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | source [*required*]                  | string          | Attribute path of the array to measure.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | target [*required*]                  | string          | Attribute that receives the computed length.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 2             | type [*required*]                    | enum            | Operation type. Allowed enum values: `length`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| operation            | Option 3                                  | object          | Operation that finds an object in a `source` array using a `filter`, and then extracts a specific value into the `target` attribute.                                                                                                                                                                                                                                                                                                                              |
| Option 3             | filter [*required*]                  | string          | Filter condition expressed as `key:value` used to find the matching element.                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | source [*required*]                  | string          | Attribute path of the array to search into.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 3             | target [*required*]                  | string          | Attribute that receives the extracted value.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Option 3             | type [*required*]                    | enum            | Operation type. Allowed enum values: `select`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 3             | value_to_extract [*required*]        | string          | Key of the value to extract from the matching element.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 18            | type [*required*]                    | enum            | Type of logs array processor. Allowed enum values: `array-processor`                                                                                                                                                                                                                                                                                                                                                                                              |
| processors           | Option 19                                 | object          | The decoder processor decodes any source attribute containing a base64/base16-encoded UTF-8/ASCII string back to its original value, storing the result in a target attribute.                                                                                                                                                                                                                                                                                    |
| Option 19            | binary_to_text_encoding [*required*] | enum            | The encoding used to represent the binary data. Allowed enum values: `base64,base16`                                                                                                                                                                                                                                                                                                                                                                              |
| Option 19            | input_representation [*required*]    | enum            | The original representation of input string. Allowed enum values: `utf_8,integer`                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | is_enabled                                | boolean         | Whether the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 19            | name                                      | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 19            | source [*required*]                  | string          | Name of the log attribute with the encoded data.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Option 19            | target [*required*]                  | string          | Name of the log attribute that contains the decoded data.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option 19            | type [*required*]                    | enum            | Type of logs decoder processor. Allowed enum values: `decoder-processor`                                                                                                                                                                                                                                                                                                                                                                                          |
| processors           | Option 20                                 | object          | A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.                                                                                                                                                                                                                                                                                                                                         |
| Option 20            | is_enabled                                | boolean         | Whether or not the processor is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 20            | mappers [*required*]                 | [ <oneOf>] | The `LogsSchemaProcessor` `mappers`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 1                                  | object          | The schema remapper maps source log fields to their correct fields.                                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                    | string          | Name of the logs schema remapper.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1             | override_on_conflict                      | boolean         | Override or not the target element if already set.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Option 1             | preserve_source                           | boolean         | Remove or preserve the remapped source element.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Option 1             | sources [*required*]                 | [string]        | Array of source attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 1             | target [*required*]                  | string          | Target field to map log source field to.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 1             | target_format                             | enum            | If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified. Allowed enum values: `auto,string,integer,double`                                                                                                                         |
| Option 1             | type [*required*]                    | enum            | Type of logs schema remapper. Allowed enum values: `schema-remapper`                                                                                                                                                                                                                                                                                                                                                                                              |
| mappers              | Option 2                                  | object          | Use the Schema Category Mapper to categorize log event into enum fields. In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.                                                                                                                                                                                                                                                                                      | **Notes**:                                                                                                                                                                                                             |
| Option 2             | categories [*required*]              | [object]        | Array of filters to match or not a log and their corresponding `name` to assign a custom value to the log.                                                                                                                                                                                                                                                                                                                                                        |
| categories           | filter [*required*]                  | object          | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filter               | query                                     | string          | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| categories           | id [*required*]                      | int64           | ID to inject into the category.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| categories           | name [*required*]                    | string          | Value to assign to target schema field.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option 2             | fallback                                  | object          | Used to override hardcoded category values with a value pulled from a source attribute on the log.                                                                                                                                                                                                                                                                                                                                                                |
| fallback             | sources                                   | object          | Fallback sources used to populate value of field.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| additionalProperties | <any-key>                                 | [string]        |
| fallback             | values                                    | object          | Values that define when the fallback is used.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties | <any-key>                                 | string          |
| Option 2             | name [*required*]                    | string          | Name of the logs schema category mapper.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Option 2             | targets [*required*]                 | object          | Name of the target attributes which value is defined by the matching category.                                                                                                                                                                                                                                                                                                                                                                                    |
| targets              | id                                        | string          | ID of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| targets              | name                                      | string          | Name of the field to map log attributes to.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Option 2             | type [*required*]                    | enum            | Type of logs schema category mapper. Allowed enum values: `schema-category-mapper`                                                                                                                                                                                                                                                                                                                                                                                |
| Option 20            | name [*required*]                    | string          | Name of the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Option 20            | schema [*required*]                  | object          | Configuration of the schema data to use.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| schema               | class_name [*required*]              | string          | Class name of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| schema               | class_uid [*required*]               | int64           | Class UID of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | profiles                                  | [string]        | Optional list of profiles to modify the schema.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| schema               | schema_type [*required*]             | string          | Type of schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| schema               | version [*required*]                 | string          | Version of the schema to use.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Option 20            | type [*required*]                    | enum            | Type of logs schema processor. Allowed enum values: `schema-processor`                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | tags                                      | [string]        | A list of tags associated with the pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                      | type                                      | string          | Type of pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "description": "string",
  "filter": {
    "query": "source:python"
  },
  "id": "string",
  "is_enabled": false,
  "is_read_only": false,
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar",
        "support_rules": "rule_name_1 foo\nrule_name_2 bar"
      },
      "is_enabled": false,
      "name": "string",
      "samples": [],
      "source": "message",
      "type": "grok-parser"
    }
  ],
  "tags": [],
  "type": "pipeline"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport pipeline_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "",
  "processors": [
    {
      "grok": {
        "match_rules": "rule_name_1 foo\nrule_name_2 bar"
      }
    }
  ]
}
EOF

#####

```python
"""
Update a pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_grok_parser import LogsGrokParser
from datadog_api_client.v1.model.logs_grok_parser_rules import LogsGrokParserRules
from datadog_api_client.v1.model.logs_grok_parser_type import LogsGrokParserType
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="",
    processors=[
        LogsGrokParser(
            grok=LogsGrokParserRules(
                match_rules="rule_name_1 foo\nrule_name_2 bar",
                support_rules="rule_name_1 foo\nrule_name_2 bar",
            ),
            is_enabled=False,
            samples=[],
            source="message",
            type=LogsGrokParserType.GROK_PARSER,
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.update_logs_pipeline(pipeline_id="pipeline_id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a pipeline returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsPipelinesAPI.new

body = DatadogAPIClient::V1::LogsPipeline.new({
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "",
  processors: [
    DatadogAPIClient::V1::LogsGrokParser.new({
      grok: DatadogAPIClient::V1::LogsGrokParserRules.new({
        match_rules: 'rule_name_1 foo\nrule_name_2 bar',
        support_rules: 'rule_name_1 foo\nrule_name_2 bar',
      }),
      is_enabled: false,
      samples: [],
      source: "message",
      type: DatadogAPIClient::V1::LogsGrokParserType::GROK_PARSER,
    }),
  ],
  tags: [],
})
p api_instance.update_logs_pipeline("pipeline_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update a pipeline returns "OK" response

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
    body := datadogV1.LogsPipeline{
        Filter: &datadogV1.LogsFilter{
            Query: datadog.PtrString("source:python"),
        },
        Name: "",
        Processors: []datadogV1.LogsProcessor{
            datadogV1.LogsProcessor{
                LogsGrokParser: &datadogV1.LogsGrokParser{
                    Grok: datadogV1.LogsGrokParserRules{
                        MatchRules: `rule_name_1 foo
rule_name_2 bar`,
                        SupportRules: datadog.PtrString(`rule_name_1 foo
rule_name_2 bar`),
                    },
                    IsEnabled: datadog.PtrBool(false),
                    Samples:   []string{},
                    Source:    "message",
                    Type:      datadogV1.LOGSGROKPARSERTYPE_GROK_PARSER,
                }},
        },
        Tags: []string{},
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsPipelinesApi(apiClient)
    resp, r, err := api.UpdateLogsPipeline(ctx, "pipeline_id", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsPipelinesApi.UpdateLogsPipeline`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsPipelinesApi.UpdateLogsPipeline`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsPipelinesApi;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsGrokParser;
import com.datadog.api.client.v1.model.LogsGrokParserRules;
import com.datadog.api.client.v1.model.LogsGrokParserType;
import com.datadog.api.client.v1.model.LogsPipeline;
import com.datadog.api.client.v1.model.LogsProcessor;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsPipelinesApi apiInstance = new LogsPipelinesApi(defaultClient);

    LogsPipeline body =
        new LogsPipeline()
            .filter(new LogsFilter().query("source:python"))
            .name("")
            .processors(
                Collections.singletonList(
                    new LogsProcessor(
                        new LogsGrokParser()
                            .grok(
                                new LogsGrokParserRules()
                                    .matchRules("""
rule_name_1 foo
rule_name_2 bar
""")
                                    .supportRules("""
rule_name_1 foo
rule_name_2 bar
"""))
                            .isEnabled(false)
                            .source("message")
                            .type(LogsGrokParserType.GROK_PARSER))));

    try {
      LogsPipeline result = apiInstance.updateLogsPipeline("pipeline_id", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsPipelinesApi#updateLogsPipeline");
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
// Update a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_pipelines::LogsPipelinesAPI;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsGrokParser;
use datadog_api_client::datadogV1::model::LogsGrokParserRules;
use datadog_api_client::datadogV1::model::LogsGrokParserType;
use datadog_api_client::datadogV1::model::LogsPipeline;
use datadog_api_client::datadogV1::model::LogsProcessor;

#[tokio::main]
async fn main() {
    let body = LogsPipeline::new("".to_string())
        .filter(LogsFilter::new().query("source:python".to_string()))
        .processors(vec![LogsProcessor::LogsGrokParser(Box::new(
            LogsGrokParser::new(
                LogsGrokParserRules::new(
                    r#"rule_name_1 foo
rule_name_2 bar"#
                        .to_string(),
                )
                .support_rules(
                    r#"rule_name_1 foo
rule_name_2 bar"#
                        .to_string(),
                ),
                "message".to_string(),
                LogsGrokParserType::GROK_PARSER,
            )
            .is_enabled(false)
            .samples(vec![]),
        ))])
        .tags(vec![]);
    let configuration = datadog::Configuration::new();
    let api = LogsPipelinesAPI::with_config(configuration);
    let resp = api
        .update_logs_pipeline("pipeline_id".to_string(), body)
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Update a pipeline returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsPipelinesApi(configuration);

const params: v1.LogsPipelinesApiUpdateLogsPipelineRequest = {
  body: {
    filter: {
      query: "source:python",
    },
    name: "",
    processors: [
      {
        grok: {
          matchRules: "rule_name_1 foo\nrule_name_2 bar",
          supportRules: "rule_name_1 foo\nrule_name_2 bar",
        },
        isEnabled: false,
        samples: [],
        source: "message",
        type: "grok-parser",
      },
    ],
    tags: [],
  },
  pipelineId: "pipeline_id",
};

apiInstance
  .updateLogsPipeline(params)
  .then((data: v1.LogsPipeline) => {
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
