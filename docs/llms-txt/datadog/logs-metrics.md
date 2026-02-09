# Source: https://docs.datadoghq.com/api/latest/logs-metrics.md

---
title: Logs Metrics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Logs Metrics
---

# Logs Metrics

Manage configuration of [log-based metrics](https://app.datadoghq.com/logs/pipelines/generate-metrics) for your organization.

## Get all log-based metrics{% #get-all-log-based-metrics %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/metrics |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/metrics |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/metrics      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/metrics      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/metrics     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/metrics |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/metrics |

### Overview

Get the list of configured log-based metrics with their definitions. This endpoint requires the `logs_read_config` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
All the available log-based metric objects.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | [object] | A list of log-based metric objects.                                                                                                        |
| data         | attributes          | object   | The object describing a Datadog log-based metric.                                                                                          |
| attributes   | compute             | object   | The compute rule to compute the log-based metric.                                                                                          |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").                      |
| attributes   | filter              | object   | The log-based metric filter. Logs matching this filter will be aggregated in this metric.                                                  |
| filter       | query               | string   | The search query - following the log search syntax.                                                                                        |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the log-based metric will be aggregated over.                                                                        |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the log-based metric.                                                                                                          |
| data         | type                | enum     | The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "compute": {
          "aggregation_type": "distribution",
          "include_percentiles": true,
          "path": "@duration"
        },
        "filter": {
          "query": "service:web* AND @http.status_code:[200 TO 299]"
        },
        "group_by": [
          {
            "path": "@http.status_code",
            "tag_name": "status_code"
          }
        ]
      },
      "id": "logs.page.load.count",
      "type": "logs_metrics"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all log-based metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.list_logs_metrics()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all log-based metrics returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new
p api_instance.list_logs_metrics()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all log-based metrics returns "OK" response

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
	api := datadogV2.NewLogsMetricsApi(apiClient)
	resp, r, err := api.ListLogsMetrics(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsMetricsApi.ListLogsMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsMetricsApi.ListLogsMetrics`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all log-based metrics returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsMetricsApi;
import com.datadog.api.client.v2.model.LogsMetricsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsMetricsApi apiInstance = new LogsMetricsApi(defaultClient);

    try {
      LogsMetricsResponse result = apiInstance.listLogsMetrics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsMetricsApi#listLogsMetrics");
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
// Get all log-based metrics returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_metrics::LogsMetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsMetricsAPI::with_config(configuration);
    let resp = api.list_logs_metrics().await;
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
 * Get all log-based metrics returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsMetricsApi(configuration);

apiInstance
  .listLogsMetrics()
  .then((data: v2.LogsMetricsResponse) => {
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

## Create a log-based metric{% #create-a-log-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/config/metrics |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/config/metrics |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/config/metrics      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/config/metrics      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/config/metrics     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/config/metrics |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/config/metrics |

### Overview

Create a metric based on your ingested logs in your organization. Returns the log-based metric object from the request body when the request is successful. This endpoint requires the `logs_generate_metrics` permission.

### Request

#### Body Data (required)

The definition of the new log-based metric.

{% tab title="Model" %}

| Parent field | Field                              | Type     | Description                                                                                                                                |
| ------------ | ---------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]             | object   | The new log-based metric properties.                                                                                                       |
| data         | attributes [*required*]       | object   | The object describing the Datadog log-based metric to create.                                                                              |
| attributes   | compute [*required*]          | object   | The compute rule to compute the log-based metric.                                                                                          |
| compute      | aggregation_type [*required*] | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles                | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                               | string   | The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").                      |
| attributes   | filter                             | object   | The log-based metric filter. Logs matching this filter will be aggregated in this metric.                                                  |
| filter       | query                              | string   | The search query - following the log search syntax.                                                                                        |
| attributes   | group_by                           | [object] | The rules for the group by.                                                                                                                |
| group_by     | path [*required*]             | string   | The path to the value the log-based metric will be aggregated over.                                                                        |
| group_by     | tag_name                           | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id [*required*]               | string   | The name of the log-based metric.                                                                                                          |
| data         | type [*required*]             | enum     | The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "ExampleLogsMetric",
    "type": "logs_metrics",
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": true,
        "path": "@duration"
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The log-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | object   | The log-based metric properties.                                                                                                           |
| data         | attributes          | object   | The object describing a Datadog log-based metric.                                                                                          |
| attributes   | compute             | object   | The compute rule to compute the log-based metric.                                                                                          |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").                      |
| attributes   | filter              | object   | The log-based metric filter. Logs matching this filter will be aggregated in this metric.                                                  |
| filter       | query               | string   | The search query - following the log search syntax.                                                                                        |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the log-based metric will be aggregated over.                                                                        |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the log-based metric.                                                                                                          |
| data         | type                | enum     | The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": true,
        "path": "@duration"
      },
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]"
      },
      "group_by": [
        {
          "path": "@http.status_code",
          "tag_name": "status_code"
        }
      ]
    },
    "id": "logs.page.load.count",
    "type": "logs_metrics"
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

{% tab title="409" %}
Conflict
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "ExampleLogsMetric",
    "type": "logs_metrics",
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": true,
        "path": "@duration"
      }
    }
  }
}
EOF
                        
##### 

```go
// Create a log-based metric returns "OK" response

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
	body := datadogV2.LogsMetricCreateRequest{
		Data: datadogV2.LogsMetricCreateData{
			Id:   "ExampleLogsMetric",
			Type: datadogV2.LOGSMETRICTYPE_LOGS_METRICS,
			Attributes: datadogV2.LogsMetricCreateAttributes{
				Compute: datadogV2.LogsMetricCompute{
					AggregationType:    datadogV2.LOGSMETRICCOMPUTEAGGREGATIONTYPE_DISTRIBUTION,
					IncludePercentiles: datadog.PtrBool(true),
					Path:               datadog.PtrString("@duration"),
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsMetricsApi(apiClient)
	resp, r, err := api.CreateLogsMetric(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsMetricsApi.CreateLogsMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsMetricsApi.CreateLogsMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a log-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsMetricsApi;
import com.datadog.api.client.v2.model.LogsMetricCompute;
import com.datadog.api.client.v2.model.LogsMetricComputeAggregationType;
import com.datadog.api.client.v2.model.LogsMetricCreateAttributes;
import com.datadog.api.client.v2.model.LogsMetricCreateData;
import com.datadog.api.client.v2.model.LogsMetricCreateRequest;
import com.datadog.api.client.v2.model.LogsMetricResponse;
import com.datadog.api.client.v2.model.LogsMetricType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsMetricsApi apiInstance = new LogsMetricsApi(defaultClient);

    LogsMetricCreateRequest body =
        new LogsMetricCreateRequest()
            .data(
                new LogsMetricCreateData()
                    .id("ExampleLogsMetric")
                    .type(LogsMetricType.LOGS_METRICS)
                    .attributes(
                        new LogsMetricCreateAttributes()
                            .compute(
                                new LogsMetricCompute()
                                    .aggregationType(LogsMetricComputeAggregationType.DISTRIBUTION)
                                    .includePercentiles(true)
                                    .path("@duration"))));

    try {
      LogsMetricResponse result = apiInstance.createLogsMetric(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsMetricsApi#createLogsMetric");
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
Create a log-based metric returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi
from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
from datadog_api_client.v2.model.logs_metric_compute_aggregation_type import LogsMetricComputeAggregationType
from datadog_api_client.v2.model.logs_metric_create_attributes import LogsMetricCreateAttributes
from datadog_api_client.v2.model.logs_metric_create_data import LogsMetricCreateData
from datadog_api_client.v2.model.logs_metric_create_request import LogsMetricCreateRequest
from datadog_api_client.v2.model.logs_metric_type import LogsMetricType

body = LogsMetricCreateRequest(
    data=LogsMetricCreateData(
        id="ExampleLogsMetric",
        type=LogsMetricType.LOGS_METRICS,
        attributes=LogsMetricCreateAttributes(
            compute=LogsMetricCompute(
                aggregation_type=LogsMetricComputeAggregationType.DISTRIBUTION,
                include_percentiles=True,
                path="@duration",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.create_logs_metric(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a log-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new

body = DatadogAPIClient::V2::LogsMetricCreateRequest.new({
  data: DatadogAPIClient::V2::LogsMetricCreateData.new({
    id: "ExampleLogsMetric",
    type: DatadogAPIClient::V2::LogsMetricType::LOGS_METRICS,
    attributes: DatadogAPIClient::V2::LogsMetricCreateAttributes.new({
      compute: DatadogAPIClient::V2::LogsMetricCompute.new({
        aggregation_type: DatadogAPIClient::V2::LogsMetricComputeAggregationType::DISTRIBUTION,
        include_percentiles: true,
        path: "@duration",
      }),
    }),
  }),
})
p api_instance.create_logs_metric(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a log-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_metrics::LogsMetricsAPI;
use datadog_api_client::datadogV2::model::LogsMetricCompute;
use datadog_api_client::datadogV2::model::LogsMetricComputeAggregationType;
use datadog_api_client::datadogV2::model::LogsMetricCreateAttributes;
use datadog_api_client::datadogV2::model::LogsMetricCreateData;
use datadog_api_client::datadogV2::model::LogsMetricCreateRequest;
use datadog_api_client::datadogV2::model::LogsMetricType;

#[tokio::main]
async fn main() {
    let body = LogsMetricCreateRequest::new(LogsMetricCreateData::new(
        LogsMetricCreateAttributes::new(
            LogsMetricCompute::new(LogsMetricComputeAggregationType::DISTRIBUTION)
                .include_percentiles(true)
                .path("@duration".to_string()),
        ),
        "ExampleLogsMetric".to_string(),
        LogsMetricType::LOGS_METRICS,
    ));
    let configuration = datadog::Configuration::new();
    let api = LogsMetricsAPI::with_config(configuration);
    let resp = api.create_logs_metric(body).await;
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
 * Create a log-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsMetricsApi(configuration);

const params: v2.LogsMetricsApiCreateLogsMetricRequest = {
  body: {
    data: {
      id: "ExampleLogsMetric",
      type: "logs_metrics",
      attributes: {
        compute: {
          aggregationType: "distribution",
          includePercentiles: true,
          path: "@duration",
        },
      },
    },
  },
};

apiInstance
  .createLogsMetric(params)
  .then((data: v2.LogsMetricResponse) => {
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

## Get a log-based metric{% #get-a-log-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/metrics/{metric_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/metrics/{metric_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/metrics/{metric_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |

### Overview

Get a specific log-based metric from your organization. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| metric_id [*required*] | string | The name of the log-based metric. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The log-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | object   | The log-based metric properties.                                                                                                           |
| data         | attributes          | object   | The object describing a Datadog log-based metric.                                                                                          |
| attributes   | compute             | object   | The compute rule to compute the log-based metric.                                                                                          |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").                      |
| attributes   | filter              | object   | The log-based metric filter. Logs matching this filter will be aggregated in this metric.                                                  |
| filter       | query               | string   | The search query - following the log search syntax.                                                                                        |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the log-based metric will be aggregated over.                                                                        |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the log-based metric.                                                                                                          |
| data         | type                | enum     | The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": true,
        "path": "@duration"
      },
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]"
      },
      "group_by": [
        {
          "path": "@http.status_code",
          "tag_name": "status_code"
        }
      ]
    },
    "id": "logs.page.load.count",
    "type": "logs_metrics"
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a log-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ID = environ["LOGS_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.get_logs_metric(
        metric_id=LOGS_METRIC_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a log-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ID = ENV["LOGS_METRIC_DATA_ID"]
p api_instance.get_logs_metric(LOGS_METRIC_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a log-based metric returns "OK" response

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
	// there is a valid "logs_metric" in the system
	LogsMetricDataID := os.Getenv("LOGS_METRIC_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsMetricsApi(apiClient)
	resp, r, err := api.GetLogsMetric(ctx, LogsMetricDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsMetricsApi.GetLogsMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsMetricsApi.GetLogsMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a log-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsMetricsApi;
import com.datadog.api.client.v2.model.LogsMetricResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsMetricsApi apiInstance = new LogsMetricsApi(defaultClient);

    // there is a valid "logs_metric" in the system
    String LOGS_METRIC_DATA_ID = System.getenv("LOGS_METRIC_DATA_ID");

    try {
      LogsMetricResponse result = apiInstance.getLogsMetric(LOGS_METRIC_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsMetricsApi#getLogsMetric");
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
// Get a log-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_metrics::LogsMetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "logs_metric" in the system
    let logs_metric_data_id = std::env::var("LOGS_METRIC_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = LogsMetricsAPI::with_config(configuration);
    let resp = api.get_logs_metric(logs_metric_data_id.clone()).await;
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
 * Get a log-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsMetricsApi(configuration);

// there is a valid "logs_metric" in the system
const LOGS_METRIC_DATA_ID = process.env.LOGS_METRIC_DATA_ID as string;

const params: v2.LogsMetricsApiGetLogsMetricRequest = {
  metricId: LOGS_METRIC_DATA_ID,
};

apiInstance
  .getLogsMetric(params)
  .then((data: v2.LogsMetricResponse) => {
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

## Update a log-based metric{% #update-a-log-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/logs/config/metrics/{metric_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/logs/config/metrics/{metric_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/logs/config/metrics/{metric_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |

### Overview

Update a specific log-based metric from your organization. Returns the log-based metric object from the request body when the request is successful. This endpoint requires the `logs_generate_metrics` permission.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| metric_id [*required*] | string | The name of the log-based metric. |

### Request

#### Body Data (required)

New definition of the log-based metric.

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                                |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]       | object   | The new log-based metric properties.                                                                                                       |
| data         | attributes [*required*] | object   | The log-based metric properties that will be updated.                                                                                      |
| attributes   | compute                      | object   | The compute rule to compute the log-based metric.                                                                                          |
| compute      | include_percentiles          | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| attributes   | filter                       | object   | The log-based metric filter. Logs matching this filter will be aggregated in this metric.                                                  |
| filter       | query                        | string   | The search query - following the log search syntax.                                                                                        |
| attributes   | group_by                     | [object] | The rules for the group by.                                                                                                                |
| group_by     | path [*required*]       | string   | The path to the value the log-based metric will be aggregated over.                                                                        |
| group_by     | tag_name                     | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | type [*required*]       | enum     | The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`                                     |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "data": {
    "type": "logs_metrics",
    "attributes": {
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]-updated"
      }
    }
  }
}
```

##### 

```json
{
  "data": {
    "type": "logs_metrics",
    "attributes": {
      "compute": {
        "include_percentiles": false
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The log-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | object   | The log-based metric properties.                                                                                                           |
| data         | attributes          | object   | The object describing a Datadog log-based metric.                                                                                          |
| attributes   | compute             | object   | The compute rule to compute the log-based metric.                                                                                          |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").                      |
| attributes   | filter              | object   | The log-based metric filter. Logs matching this filter will be aggregated in this metric.                                                  |
| filter       | query               | string   | The search query - following the log search syntax.                                                                                        |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the log-based metric will be aggregated over.                                                                        |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the log-based metric.                                                                                                          |
| data         | type                | enum     | The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": true,
        "path": "@duration"
      },
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]"
      },
      "group_by": [
        {
          "path": "@http.status_code",
          "tag_name": "status_code"
        }
      ]
    },
    "id": "logs.page.load.count",
    "type": "logs_metrics"
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

{% tab title="404" %}
Not Found
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
                          \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "logs_metrics",
    "attributes": {
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]-updated"
      }
    }
  }
}
EOF
                        
##### 
                          \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "logs_metrics",
    "attributes": {
      "compute": {
        "include_percentiles": false
      }
    }
  }
}
EOF
                        
##### 

```go
// Update a log-based metric returns "OK" response

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
	// there is a valid "logs_metric" in the system
	LogsMetricDataID := os.Getenv("LOGS_METRIC_DATA_ID")

	body := datadogV2.LogsMetricUpdateRequest{
		Data: datadogV2.LogsMetricUpdateData{
			Type: datadogV2.LOGSMETRICTYPE_LOGS_METRICS,
			Attributes: datadogV2.LogsMetricUpdateAttributes{
				Filter: &datadogV2.LogsMetricFilter{
					Query: datadog.PtrString("service:web* AND @http.status_code:[200 TO 299]-updated"),
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsMetricsApi(apiClient)
	resp, r, err := api.UpdateLogsMetric(ctx, LogsMetricDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsMetricsApi.UpdateLogsMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsMetricsApi.UpdateLogsMetric`:\n%s\n", responseContent)
}
```

##### 

```go
// Update a log-based metric with include_percentiles field returns "OK" response

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
	// there is a valid "logs_metric_percentile" in the system
	LogsMetricPercentileDataID := os.Getenv("LOGS_METRIC_PERCENTILE_DATA_ID")

	body := datadogV2.LogsMetricUpdateRequest{
		Data: datadogV2.LogsMetricUpdateData{
			Type: datadogV2.LOGSMETRICTYPE_LOGS_METRICS,
			Attributes: datadogV2.LogsMetricUpdateAttributes{
				Compute: &datadogV2.LogsMetricUpdateCompute{
					IncludePercentiles: datadog.PtrBool(false),
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsMetricsApi(apiClient)
	resp, r, err := api.UpdateLogsMetric(ctx, LogsMetricPercentileDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsMetricsApi.UpdateLogsMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `LogsMetricsApi.UpdateLogsMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a log-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsMetricsApi;
import com.datadog.api.client.v2.model.LogsMetricFilter;
import com.datadog.api.client.v2.model.LogsMetricResponse;
import com.datadog.api.client.v2.model.LogsMetricType;
import com.datadog.api.client.v2.model.LogsMetricUpdateAttributes;
import com.datadog.api.client.v2.model.LogsMetricUpdateData;
import com.datadog.api.client.v2.model.LogsMetricUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsMetricsApi apiInstance = new LogsMetricsApi(defaultClient);

    // there is a valid "logs_metric" in the system
    String LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY =
        System.getenv("LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY");
    String LOGS_METRIC_DATA_ID = System.getenv("LOGS_METRIC_DATA_ID");

    LogsMetricUpdateRequest body =
        new LogsMetricUpdateRequest()
            .data(
                new LogsMetricUpdateData()
                    .type(LogsMetricType.LOGS_METRICS)
                    .attributes(
                        new LogsMetricUpdateAttributes()
                            .filter(
                                new LogsMetricFilter()
                                    .query(
                                        "service:web* AND @http.status_code:[200 TO"
                                            + " 299]-updated"))));

    try {
      LogsMetricResponse result = apiInstance.updateLogsMetric(LOGS_METRIC_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsMetricsApi#updateLogsMetric");
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
// Update a log-based metric with include_percentiles field returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsMetricsApi;
import com.datadog.api.client.v2.model.LogsMetricResponse;
import com.datadog.api.client.v2.model.LogsMetricType;
import com.datadog.api.client.v2.model.LogsMetricUpdateAttributes;
import com.datadog.api.client.v2.model.LogsMetricUpdateCompute;
import com.datadog.api.client.v2.model.LogsMetricUpdateData;
import com.datadog.api.client.v2.model.LogsMetricUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsMetricsApi apiInstance = new LogsMetricsApi(defaultClient);

    // there is a valid "logs_metric_percentile" in the system
    String LOGS_METRIC_PERCENTILE_DATA_ID = System.getenv("LOGS_METRIC_PERCENTILE_DATA_ID");

    LogsMetricUpdateRequest body =
        new LogsMetricUpdateRequest()
            .data(
                new LogsMetricUpdateData()
                    .type(LogsMetricType.LOGS_METRICS)
                    .attributes(
                        new LogsMetricUpdateAttributes()
                            .compute(new LogsMetricUpdateCompute().includePercentiles(false))));

    try {
      LogsMetricResponse result =
          apiInstance.updateLogsMetric(LOGS_METRIC_PERCENTILE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsMetricsApi#updateLogsMetric");
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
Update a log-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi
from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
from datadog_api_client.v2.model.logs_metric_type import LogsMetricType
from datadog_api_client.v2.model.logs_metric_update_attributes import LogsMetricUpdateAttributes
from datadog_api_client.v2.model.logs_metric_update_data import LogsMetricUpdateData
from datadog_api_client.v2.model.logs_metric_update_request import LogsMetricUpdateRequest

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY = environ["LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY"]
LOGS_METRIC_DATA_ID = environ["LOGS_METRIC_DATA_ID"]

body = LogsMetricUpdateRequest(
    data=LogsMetricUpdateData(
        type=LogsMetricType.LOGS_METRICS,
        attributes=LogsMetricUpdateAttributes(
            filter=LogsMetricFilter(
                query="service:web* AND @http.status_code:[200 TO 299]-updated",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.update_logs_metric(metric_id=LOGS_METRIC_DATA_ID, body=body)

    print(response)
```

##### 

```python
"""
Update a log-based metric with include_percentiles field returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi
from datadog_api_client.v2.model.logs_metric_type import LogsMetricType
from datadog_api_client.v2.model.logs_metric_update_attributes import LogsMetricUpdateAttributes
from datadog_api_client.v2.model.logs_metric_update_compute import LogsMetricUpdateCompute
from datadog_api_client.v2.model.logs_metric_update_data import LogsMetricUpdateData
from datadog_api_client.v2.model.logs_metric_update_request import LogsMetricUpdateRequest

# there is a valid "logs_metric_percentile" in the system
LOGS_METRIC_PERCENTILE_DATA_ID = environ["LOGS_METRIC_PERCENTILE_DATA_ID"]

body = LogsMetricUpdateRequest(
    data=LogsMetricUpdateData(
        type=LogsMetricType.LOGS_METRICS,
        attributes=LogsMetricUpdateAttributes(
            compute=LogsMetricUpdateCompute(
                include_percentiles=False,
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.update_logs_metric(metric_id=LOGS_METRIC_PERCENTILE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a log-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY = ENV["LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY"]
LOGS_METRIC_DATA_ID = ENV["LOGS_METRIC_DATA_ID"]

body = DatadogAPIClient::V2::LogsMetricUpdateRequest.new({
  data: DatadogAPIClient::V2::LogsMetricUpdateData.new({
    type: DatadogAPIClient::V2::LogsMetricType::LOGS_METRICS,
    attributes: DatadogAPIClient::V2::LogsMetricUpdateAttributes.new({
      filter: DatadogAPIClient::V2::LogsMetricFilter.new({
        query: "service:web* AND @http.status_code:[200 TO 299]-updated",
      }),
    }),
  }),
})
p api_instance.update_logs_metric(LOGS_METRIC_DATA_ID, body)
```

##### 

```ruby
# Update a log-based metric with include_percentiles field returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new

# there is a valid "logs_metric_percentile" in the system
LOGS_METRIC_PERCENTILE_DATA_ID = ENV["LOGS_METRIC_PERCENTILE_DATA_ID"]

body = DatadogAPIClient::V2::LogsMetricUpdateRequest.new({
  data: DatadogAPIClient::V2::LogsMetricUpdateData.new({
    type: DatadogAPIClient::V2::LogsMetricType::LOGS_METRICS,
    attributes: DatadogAPIClient::V2::LogsMetricUpdateAttributes.new({
      compute: DatadogAPIClient::V2::LogsMetricUpdateCompute.new({
        include_percentiles: false,
      }),
    }),
  }),
})
p api_instance.update_logs_metric(LOGS_METRIC_PERCENTILE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update a log-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_metrics::LogsMetricsAPI;
use datadog_api_client::datadogV2::model::LogsMetricFilter;
use datadog_api_client::datadogV2::model::LogsMetricType;
use datadog_api_client::datadogV2::model::LogsMetricUpdateAttributes;
use datadog_api_client::datadogV2::model::LogsMetricUpdateData;
use datadog_api_client::datadogV2::model::LogsMetricUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "logs_metric" in the system
    let logs_metric_data_id = std::env::var("LOGS_METRIC_DATA_ID").unwrap();
    let body = LogsMetricUpdateRequest::new(LogsMetricUpdateData::new(
        LogsMetricUpdateAttributes::new().filter(
            LogsMetricFilter::new()
                .query("service:web* AND @http.status_code:[200 TO 299]-updated".to_string()),
        ),
        LogsMetricType::LOGS_METRICS,
    ));
    let configuration = datadog::Configuration::new();
    let api = LogsMetricsAPI::with_config(configuration);
    let resp = api
        .update_logs_metric(logs_metric_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Update a log-based metric with include_percentiles field returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_metrics::LogsMetricsAPI;
use datadog_api_client::datadogV2::model::LogsMetricType;
use datadog_api_client::datadogV2::model::LogsMetricUpdateAttributes;
use datadog_api_client::datadogV2::model::LogsMetricUpdateCompute;
use datadog_api_client::datadogV2::model::LogsMetricUpdateData;
use datadog_api_client::datadogV2::model::LogsMetricUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "logs_metric_percentile" in the system
    let logs_metric_percentile_data_id = std::env::var("LOGS_METRIC_PERCENTILE_DATA_ID").unwrap();
    let body = LogsMetricUpdateRequest::new(LogsMetricUpdateData::new(
        LogsMetricUpdateAttributes::new()
            .compute(LogsMetricUpdateCompute::new().include_percentiles(false)),
        LogsMetricType::LOGS_METRICS,
    ));
    let configuration = datadog::Configuration::new();
    let api = LogsMetricsAPI::with_config(configuration);
    let resp = api
        .update_logs_metric(logs_metric_percentile_data_id.clone(), body)
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
 * Update a log-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsMetricsApi(configuration);

// there is a valid "logs_metric" in the system
const LOGS_METRIC_DATA_ID = process.env.LOGS_METRIC_DATA_ID as string;

const params: v2.LogsMetricsApiUpdateLogsMetricRequest = {
  body: {
    data: {
      type: "logs_metrics",
      attributes: {
        filter: {
          query: "service:web* AND @http.status_code:[200 TO 299]-updated",
        },
      },
    },
  },
  metricId: LOGS_METRIC_DATA_ID,
};

apiInstance
  .updateLogsMetric(params)
  .then((data: v2.LogsMetricResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Update a log-based metric with include_percentiles field returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsMetricsApi(configuration);

// there is a valid "logs_metric_percentile" in the system
const LOGS_METRIC_PERCENTILE_DATA_ID = process.env
  .LOGS_METRIC_PERCENTILE_DATA_ID as string;

const params: v2.LogsMetricsApiUpdateLogsMetricRequest = {
  body: {
    data: {
      type: "logs_metrics",
      attributes: {
        compute: {
          includePercentiles: false,
        },
      },
    },
  },
  metricId: LOGS_METRIC_PERCENTILE_DATA_ID,
};

apiInstance
  .updateLogsMetric(params)
  .then((data: v2.LogsMetricResponse) => {
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

## Delete a log-based metric{% #delete-a-log-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/logs/config/metrics/{metric_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/logs/config/metrics/{metric_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/logs/config/metrics/{metric_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/logs/config/metrics/{metric_id} |

### Overview

Delete a specific log-based metric from your organization. This endpoint requires the `logs_generate_metrics` permission.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| metric_id [*required*] | string | The name of the log-based metric. |

### Response

{% tab title="204" %}
OK
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a log-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ID = environ["LOGS_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    api_instance.delete_logs_metric(
        metric_id=LOGS_METRIC_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a log-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ID = ENV["LOGS_METRIC_DATA_ID"]
api_instance.delete_logs_metric(LOGS_METRIC_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a log-based metric returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "logs_metric" in the system
	LogsMetricDataID := os.Getenv("LOGS_METRIC_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewLogsMetricsApi(apiClient)
	r, err := api.DeleteLogsMetric(ctx, LogsMetricDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LogsMetricsApi.DeleteLogsMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a log-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsMetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsMetricsApi apiInstance = new LogsMetricsApi(defaultClient);

    // there is a valid "logs_metric" in the system
    String LOGS_METRIC_DATA_ID = System.getenv("LOGS_METRIC_DATA_ID");

    try {
      apiInstance.deleteLogsMetric(LOGS_METRIC_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsMetricsApi#deleteLogsMetric");
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
// Delete a log-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_metrics::LogsMetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "logs_metric" in the system
    let logs_metric_data_id = std::env::var("LOGS_METRIC_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = LogsMetricsAPI::with_config(configuration);
    let resp = api.delete_logs_metric(logs_metric_data_id.clone()).await;
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
 * Delete a log-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsMetricsApi(configuration);

// there is a valid "logs_metric" in the system
const LOGS_METRIC_DATA_ID = process.env.LOGS_METRIC_DATA_ID as string;

const params: v2.LogsMetricsApiDeleteLogsMetricRequest = {
  metricId: LOGS_METRIC_DATA_ID,
};

apiInstance
  .deleteLogsMetric(params)
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
