# Source: https://docs.datadoghq.com/api/latest/spans-metrics.md

---
title: Spans Metrics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Spans Metrics
---

# Spans Metrics

Manage configuration of [span-based metrics](https://app.datadoghq.com/apm/traces/generate-metrics) for your organization. See [Generate Metrics from Spans](https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/) for more information.

## Get all span-based metrics{% #get-all-span-based-metrics %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/apm/config/metrics |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/apm/config/metrics |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/apm/config/metrics      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/apm/config/metrics      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/apm/config/metrics     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/apm/config/metrics |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/apm/config/metrics |

### Overview

Get the list of configured span-based metrics with their definitions. This endpoint requires the `apm_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
All the available span-based metric objects.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | [object] | A list of span-based metric objects.                                                                                                       |
| data         | attributes          | object   | The object describing a Datadog span-based metric.                                                                                         |
| attributes   | compute             | object   | The compute rule to compute the span-based metric.                                                                                         |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the span-based metric will aggregate on (only used if the aggregation type is a "distribution").                     |
| attributes   | filter              | object   | The span-based metric filter. Spans matching this filter will be aggregated in this metric.                                                |
| filter       | query               | string   | The search query - following the span search syntax.                                                                                       |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the span-based metric will be aggregated over.                                                                       |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the span-based metric.                                                                                                         |
| data         | type                | enum     | The type of resource. The value should always be spans_metrics. Allowed enum values: `spans_metrics`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "compute": {
          "aggregation_type": "distribution",
          "include_percentiles": false,
          "path": "@duration"
        },
        "filter": {
          "query": "@http.status_code:200 service:my-service"
        },
        "group_by": [
          {
            "path": "resource_name",
            "tag_name": "resource_name"
          }
        ]
      },
      "id": "my.metric",
      "type": "spans_metrics"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/metrics" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all span-based metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.list_spans_metrics()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all span-based metrics returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansMetricsAPI.new
p api_instance.list_spans_metrics()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all span-based metrics returns "OK" response

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
    api := datadogV2.NewSpansMetricsApi(apiClient)
    resp, r, err := api.ListSpansMetrics(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SpansMetricsApi.ListSpansMetrics`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SpansMetricsApi.ListSpansMetrics`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all span-based metrics returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansMetricsApi;
import com.datadog.api.client.v2.model.SpansMetricsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansMetricsApi apiInstance = new SpansMetricsApi(defaultClient);

    try {
      SpansMetricsResponse result = apiInstance.listSpansMetrics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansMetricsApi#listSpansMetrics");
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
// Get all span-based metrics returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans_metrics::SpansMetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SpansMetricsAPI::with_config(configuration);
    let resp = api.list_spans_metrics().await;
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
 * Get all span-based metrics returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansMetricsApi(configuration);

apiInstance
  .listSpansMetrics()
  .then((data: v2.SpansMetricsResponse) => {
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

## Create a span-based metric{% #create-a-span-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/apm/config/metrics |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/apm/config/metrics |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/apm/config/metrics      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/apm/config/metrics      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/apm/config/metrics     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/apm/config/metrics |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/apm/config/metrics |

### Overview

Create a metric based on your ingested spans in your organization. Returns the span-based metric object from the request body when the request is successful. This endpoint requires the `apm_generate_metrics` permission.

### Request

#### Body Data (required)

The definition of the new span-based metric.

{% tab title="Model" %}

| Parent field | Field                              | Type     | Description                                                                                                                                |
| ------------ | ---------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]             | object   | The new span-based metric properties.                                                                                                      |
| data         | attributes [*required*]       | object   | The object describing the Datadog span-based metric to create.                                                                             |
| attributes   | compute [*required*]          | object   | The compute rule to compute the span-based metric.                                                                                         |
| compute      | aggregation_type [*required*] | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles                | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                               | string   | The path to the value the span-based metric will aggregate on (only used if the aggregation type is a "distribution").                     |
| attributes   | filter                             | object   | The span-based metric filter. Spans matching this filter will be aggregated in this metric.                                                |
| filter       | query                              | string   | The search query - following the span search syntax.                                                                                       |
| attributes   | group_by                           | [object] | The rules for the group by.                                                                                                                |
| group_by     | path [*required*]             | string   | The path to the value the span-based metric will be aggregated over.                                                                       |
| group_by     | tag_name                           | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id [*required*]               | string   | The name of the span-based metric.                                                                                                         |
| data         | type [*required*]             | enum     | The type of resource. The value should always be spans_metrics. Allowed enum values: `spans_metrics`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": false,
        "path": "@duration"
      },
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "group_by": [
        {
          "path": "resource_name",
          "tag_name": "resource_name"
        }
      ]
    },
    "id": "ExampleSpansMetric",
    "type": "spans_metrics"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The span-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | object   | The span-based metric properties.                                                                                                          |
| data         | attributes          | object   | The object describing a Datadog span-based metric.                                                                                         |
| attributes   | compute             | object   | The compute rule to compute the span-based metric.                                                                                         |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the span-based metric will aggregate on (only used if the aggregation type is a "distribution").                     |
| attributes   | filter              | object   | The span-based metric filter. Spans matching this filter will be aggregated in this metric.                                                |
| filter       | query               | string   | The search query - following the span search syntax.                                                                                       |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the span-based metric will be aggregated over.                                                                       |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the span-based metric.                                                                                                         |
| data         | type                | enum     | The type of resource. The value should always be spans_metrics. Allowed enum values: `spans_metrics`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": false,
        "path": "@duration"
      },
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "group_by": [
        {
          "path": "resource_name",
          "tag_name": "resource_name"
        }
      ]
    },
    "id": "my.metric",
    "type": "spans_metrics"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/metrics" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": false,
        "path": "@duration"
      },
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "group_by": [
        {
          "path": "resource_name",
          "tag_name": "resource_name"
        }
      ]
    },
    "id": "ExampleSpansMetric",
    "type": "spans_metrics"
  }
}
EOF

#####

```go
// Create a span-based metric returns "OK" response

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
    body := datadogV2.SpansMetricCreateRequest{
        Data: datadogV2.SpansMetricCreateData{
            Attributes: datadogV2.SpansMetricCreateAttributes{
                Compute: datadogV2.SpansMetricCompute{
                    AggregationType:    datadogV2.SPANSMETRICCOMPUTEAGGREGATIONTYPE_DISTRIBUTION,
                    IncludePercentiles: datadog.PtrBool(false),
                    Path:               datadog.PtrString("@duration"),
                },
                Filter: &datadogV2.SpansMetricFilter{
                    Query: datadog.PtrString("@http.status_code:200 service:my-service"),
                },
                GroupBy: []datadogV2.SpansMetricGroupBy{
                    {
                        Path:    "resource_name",
                        TagName: datadog.PtrString("resource_name"),
                    },
                },
            },
            Id:   "ExampleSpansMetric",
            Type: datadogV2.SPANSMETRICTYPE_SPANS_METRICS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewSpansMetricsApi(apiClient)
    resp, r, err := api.CreateSpansMetric(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SpansMetricsApi.CreateSpansMetric`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SpansMetricsApi.CreateSpansMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a span-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansMetricsApi;
import com.datadog.api.client.v2.model.SpansMetricCompute;
import com.datadog.api.client.v2.model.SpansMetricComputeAggregationType;
import com.datadog.api.client.v2.model.SpansMetricCreateAttributes;
import com.datadog.api.client.v2.model.SpansMetricCreateData;
import com.datadog.api.client.v2.model.SpansMetricCreateRequest;
import com.datadog.api.client.v2.model.SpansMetricFilter;
import com.datadog.api.client.v2.model.SpansMetricGroupBy;
import com.datadog.api.client.v2.model.SpansMetricResponse;
import com.datadog.api.client.v2.model.SpansMetricType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansMetricsApi apiInstance = new SpansMetricsApi(defaultClient);

    SpansMetricCreateRequest body =
        new SpansMetricCreateRequest()
            .data(
                new SpansMetricCreateData()
                    .attributes(
                        new SpansMetricCreateAttributes()
                            .compute(
                                new SpansMetricCompute()
                                    .aggregationType(SpansMetricComputeAggregationType.DISTRIBUTION)
                                    .includePercentiles(false)
                                    .path("@duration"))
                            .filter(
                                new SpansMetricFilter()
                                    .query("@http.status_code:200 service:my-service"))
                            .groupBy(
                                Collections.singletonList(
                                    new SpansMetricGroupBy()
                                        .path("resource_name")
                                        .tagName("resource_name"))))
                    .id("ExampleSpansMetric")
                    .type(SpansMetricType.SPANS_METRICS));

    try {
      SpansMetricResponse result = apiInstance.createSpansMetric(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansMetricsApi#createSpansMetric");
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
Create a span-based metric returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi
from datadog_api_client.v2.model.spans_metric_compute import SpansMetricCompute
from datadog_api_client.v2.model.spans_metric_compute_aggregation_type import SpansMetricComputeAggregationType
from datadog_api_client.v2.model.spans_metric_create_attributes import SpansMetricCreateAttributes
from datadog_api_client.v2.model.spans_metric_create_data import SpansMetricCreateData
from datadog_api_client.v2.model.spans_metric_create_request import SpansMetricCreateRequest
from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy
from datadog_api_client.v2.model.spans_metric_type import SpansMetricType

body = SpansMetricCreateRequest(
    data=SpansMetricCreateData(
        attributes=SpansMetricCreateAttributes(
            compute=SpansMetricCompute(
                aggregation_type=SpansMetricComputeAggregationType.DISTRIBUTION,
                include_percentiles=False,
                path="@duration",
            ),
            filter=SpansMetricFilter(
                query="@http.status_code:200 service:my-service",
            ),
            group_by=[
                SpansMetricGroupBy(
                    path="resource_name",
                    tag_name="resource_name",
                ),
            ],
        ),
        id="ExampleSpansMetric",
        type=SpansMetricType.SPANS_METRICS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.create_spans_metric(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a span-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansMetricsAPI.new

body = DatadogAPIClient::V2::SpansMetricCreateRequest.new({
  data: DatadogAPIClient::V2::SpansMetricCreateData.new({
    attributes: DatadogAPIClient::V2::SpansMetricCreateAttributes.new({
      compute: DatadogAPIClient::V2::SpansMetricCompute.new({
        aggregation_type: DatadogAPIClient::V2::SpansMetricComputeAggregationType::DISTRIBUTION,
        include_percentiles: false,
        path: "@duration",
      }),
      filter: DatadogAPIClient::V2::SpansMetricFilter.new({
        query: "@http.status_code:200 service:my-service",
      }),
      group_by: [
        DatadogAPIClient::V2::SpansMetricGroupBy.new({
          path: "resource_name",
          tag_name: "resource_name",
        }),
      ],
    }),
    id: "ExampleSpansMetric",
    type: DatadogAPIClient::V2::SpansMetricType::SPANS_METRICS,
  }),
})
p api_instance.create_spans_metric(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a span-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans_metrics::SpansMetricsAPI;
use datadog_api_client::datadogV2::model::SpansMetricCompute;
use datadog_api_client::datadogV2::model::SpansMetricComputeAggregationType;
use datadog_api_client::datadogV2::model::SpansMetricCreateAttributes;
use datadog_api_client::datadogV2::model::SpansMetricCreateData;
use datadog_api_client::datadogV2::model::SpansMetricCreateRequest;
use datadog_api_client::datadogV2::model::SpansMetricFilter;
use datadog_api_client::datadogV2::model::SpansMetricGroupBy;
use datadog_api_client::datadogV2::model::SpansMetricType;

#[tokio::main]
async fn main() {
    let body = SpansMetricCreateRequest::new(SpansMetricCreateData::new(
        SpansMetricCreateAttributes::new(
            SpansMetricCompute::new(SpansMetricComputeAggregationType::DISTRIBUTION)
                .include_percentiles(false)
                .path("@duration".to_string()),
        )
        .filter(
            SpansMetricFilter::new().query("@http.status_code:200 service:my-service".to_string()),
        )
        .group_by(vec![SpansMetricGroupBy::new("resource_name".to_string())
            .tag_name("resource_name".to_string())]),
        "ExampleSpansMetric".to_string(),
        SpansMetricType::SPANS_METRICS,
    ));
    let configuration = datadog::Configuration::new();
    let api = SpansMetricsAPI::with_config(configuration);
    let resp = api.create_spans_metric(body).await;
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
 * Create a span-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansMetricsApi(configuration);

const params: v2.SpansMetricsApiCreateSpansMetricRequest = {
  body: {
    data: {
      attributes: {
        compute: {
          aggregationType: "distribution",
          includePercentiles: false,
          path: "@duration",
        },
        filter: {
          query: "@http.status_code:200 service:my-service",
        },
        groupBy: [
          {
            path: "resource_name",
            tagName: "resource_name",
          },
        ],
      },
      id: "ExampleSpansMetric",
      type: "spans_metrics",
    },
  },
};

apiInstance
  .createSpansMetric(params)
  .then((data: v2.SpansMetricResponse) => {
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

## Get a span-based metric{% #get-a-span-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/apm/config/metrics/{metric_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/apm/config/metrics/{metric_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/apm/config/metrics/{metric_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |

### Overview

Get a specific span-based metric from your organization. This endpoint requires the `apm_read` permission.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                        |
| --------------------------- | ------ | ---------------------------------- |
| metric_id [*required*] | string | The name of the span-based metric. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The span-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | object   | The span-based metric properties.                                                                                                          |
| data         | attributes          | object   | The object describing a Datadog span-based metric.                                                                                         |
| attributes   | compute             | object   | The compute rule to compute the span-based metric.                                                                                         |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the span-based metric will aggregate on (only used if the aggregation type is a "distribution").                     |
| attributes   | filter              | object   | The span-based metric filter. Spans matching this filter will be aggregated in this metric.                                                |
| filter       | query               | string   | The search query - following the span search syntax.                                                                                       |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the span-based metric will be aggregated over.                                                                       |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the span-based metric.                                                                                                         |
| data         | type                | enum     | The type of resource. The value should always be spans_metrics. Allowed enum values: `spans_metrics`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": false,
        "path": "@duration"
      },
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "group_by": [
        {
          "path": "resource_name",
          "tag_name": "resource_name"
        }
      ]
    },
    "id": "my.metric",
    "type": "spans_metrics"
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
                  \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a span-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ID = environ["SPANS_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.get_spans_metric(
        metric_id=SPANS_METRIC_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a span-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansMetricsAPI.new

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ID = ENV["SPANS_METRIC_DATA_ID"]
p api_instance.get_spans_metric(SPANS_METRIC_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a span-based metric returns "OK" response

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
    // there is a valid "spans_metric" in the system
    SpansMetricDataID := os.Getenv("SPANS_METRIC_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewSpansMetricsApi(apiClient)
    resp, r, err := api.GetSpansMetric(ctx, SpansMetricDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SpansMetricsApi.GetSpansMetric`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SpansMetricsApi.GetSpansMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a span-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansMetricsApi;
import com.datadog.api.client.v2.model.SpansMetricResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansMetricsApi apiInstance = new SpansMetricsApi(defaultClient);

    // there is a valid "spans_metric" in the system
    String SPANS_METRIC_DATA_ID = System.getenv("SPANS_METRIC_DATA_ID");

    try {
      SpansMetricResponse result = apiInstance.getSpansMetric(SPANS_METRIC_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansMetricsApi#getSpansMetric");
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
// Get a span-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans_metrics::SpansMetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "spans_metric" in the system
    let spans_metric_data_id = std::env::var("SPANS_METRIC_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = SpansMetricsAPI::with_config(configuration);
    let resp = api.get_spans_metric(spans_metric_data_id.clone()).await;
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
 * Get a span-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansMetricsApi(configuration);

// there is a valid "spans_metric" in the system
const SPANS_METRIC_DATA_ID = process.env.SPANS_METRIC_DATA_ID as string;

const params: v2.SpansMetricsApiGetSpansMetricRequest = {
  metricId: SPANS_METRIC_DATA_ID,
};

apiInstance
  .getSpansMetric(params)
  .then((data: v2.SpansMetricResponse) => {
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

## Update a span-based metric{% #update-a-span-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/apm/config/metrics/{metric_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/apm/config/metrics/{metric_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/apm/config/metrics/{metric_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |

### Overview

Update a specific span-based metric from your organization. Returns the span-based metric object from the request body when the request is successful. This endpoint requires the `apm_generate_metrics` permission.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                        |
| --------------------------- | ------ | ---------------------------------- |
| metric_id [*required*] | string | The name of the span-based metric. |

### Request

#### Body Data (required)

New definition of the span-based metric.

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                                |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]       | object   | The new span-based metric properties.                                                                                                      |
| data         | attributes [*required*] | object   | The span-based metric properties that will be updated.                                                                                     |
| attributes   | compute                      | object   | The compute rule to compute the span-based metric.                                                                                         |
| compute      | include_percentiles          | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| attributes   | filter                       | object   | The span-based metric filter. Spans matching this filter will be aggregated in this metric.                                                |
| filter       | query                        | string   | The search query - following the span search syntax.                                                                                       |
| attributes   | group_by                     | [object] | The rules for the group by.                                                                                                                |
| group_by     | path [*required*]       | string   | The path to the value the span-based metric will be aggregated over.                                                                       |
| group_by     | tag_name                     | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | type [*required*]       | enum     | The type of resource. The value should always be spans_metrics. Allowed enum values: `spans_metrics`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "include_percentiles": false
      },
      "filter": {
        "query": "@http.status_code:200 service:my-service-updated"
      },
      "group_by": [
        {
          "path": "resource_name",
          "tag_name": "resource_name"
        }
      ]
    },
    "type": "spans_metrics"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The span-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|              | data                | object   | The span-based metric properties.                                                                                                          |
| data         | attributes          | object   | The object describing a Datadog span-based metric.                                                                                         |
| attributes   | compute             | object   | The compute rule to compute the span-based metric.                                                                                         |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                  |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`. |
| compute      | path                | string   | The path to the value the span-based metric will aggregate on (only used if the aggregation type is a "distribution").                     |
| attributes   | filter              | object   | The span-based metric filter. Spans matching this filter will be aggregated in this metric.                                                |
| filter       | query               | string   | The search query - following the span search syntax.                                                                                       |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                |
| group_by     | path                | string   | The path to the value the span-based metric will be aggregated over.                                                                       |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.                                        |
| data         | id                  | string   | The name of the span-based metric.                                                                                                         |
| data         | type                | enum     | The type of resource. The value should always be spans_metrics. Allowed enum values: `spans_metrics`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "compute": {
        "aggregation_type": "distribution",
        "include_percentiles": false,
        "path": "@duration"
      },
      "filter": {
        "query": "@http.status_code:200 service:my-service"
      },
      "group_by": [
        {
          "path": "resource_name",
          "tag_name": "resource_name"
        }
      ]
    },
    "id": "my.metric",
    "type": "spans_metrics"
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
                          \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "compute": {
        "include_percentiles": false
      },
      "filter": {
        "query": "@http.status_code:200 service:my-service-updated"
      },
      "group_by": [
        {
          "path": "resource_name",
          "tag_name": "resource_name"
        }
      ]
    },
    "type": "spans_metrics"
  }
}
EOF

#####

```go
// Update a span-based metric returns "OK" response

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
    // there is a valid "spans_metric" in the system
    SpansMetricDataID := os.Getenv("SPANS_METRIC_DATA_ID")

    body := datadogV2.SpansMetricUpdateRequest{
        Data: datadogV2.SpansMetricUpdateData{
            Attributes: datadogV2.SpansMetricUpdateAttributes{
                Compute: &datadogV2.SpansMetricUpdateCompute{
                    IncludePercentiles: datadog.PtrBool(false),
                },
                Filter: &datadogV2.SpansMetricFilter{
                    Query: datadog.PtrString("@http.status_code:200 service:my-service-updated"),
                },
                GroupBy: []datadogV2.SpansMetricGroupBy{
                    {
                        Path:    "resource_name",
                        TagName: datadog.PtrString("resource_name"),
                    },
                },
            },
            Type: datadogV2.SPANSMETRICTYPE_SPANS_METRICS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewSpansMetricsApi(apiClient)
    resp, r, err := api.UpdateSpansMetric(ctx, SpansMetricDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SpansMetricsApi.UpdateSpansMetric`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SpansMetricsApi.UpdateSpansMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a span-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansMetricsApi;
import com.datadog.api.client.v2.model.SpansMetricFilter;
import com.datadog.api.client.v2.model.SpansMetricGroupBy;
import com.datadog.api.client.v2.model.SpansMetricResponse;
import com.datadog.api.client.v2.model.SpansMetricType;
import com.datadog.api.client.v2.model.SpansMetricUpdateAttributes;
import com.datadog.api.client.v2.model.SpansMetricUpdateCompute;
import com.datadog.api.client.v2.model.SpansMetricUpdateData;
import com.datadog.api.client.v2.model.SpansMetricUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansMetricsApi apiInstance = new SpansMetricsApi(defaultClient);

    // there is a valid "spans_metric" in the system
    String SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY =
        System.getenv("SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY");
    String SPANS_METRIC_DATA_ID = System.getenv("SPANS_METRIC_DATA_ID");

    SpansMetricUpdateRequest body =
        new SpansMetricUpdateRequest()
            .data(
                new SpansMetricUpdateData()
                    .attributes(
                        new SpansMetricUpdateAttributes()
                            .compute(new SpansMetricUpdateCompute().includePercentiles(false))
                            .filter(
                                new SpansMetricFilter()
                                    .query("@http.status_code:200 service:my-service-updated"))
                            .groupBy(
                                Collections.singletonList(
                                    new SpansMetricGroupBy()
                                        .path("resource_name")
                                        .tagName("resource_name"))))
                    .type(SpansMetricType.SPANS_METRICS));

    try {
      SpansMetricResponse result = apiInstance.updateSpansMetric(SPANS_METRIC_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansMetricsApi#updateSpansMetric");
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
Update a span-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi
from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy
from datadog_api_client.v2.model.spans_metric_type import SpansMetricType
from datadog_api_client.v2.model.spans_metric_update_attributes import SpansMetricUpdateAttributes
from datadog_api_client.v2.model.spans_metric_update_compute import SpansMetricUpdateCompute
from datadog_api_client.v2.model.spans_metric_update_data import SpansMetricUpdateData
from datadog_api_client.v2.model.spans_metric_update_request import SpansMetricUpdateRequest

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY = environ["SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY"]
SPANS_METRIC_DATA_ID = environ["SPANS_METRIC_DATA_ID"]

body = SpansMetricUpdateRequest(
    data=SpansMetricUpdateData(
        attributes=SpansMetricUpdateAttributes(
            compute=SpansMetricUpdateCompute(
                include_percentiles=False,
            ),
            filter=SpansMetricFilter(
                query="@http.status_code:200 service:my-service-updated",
            ),
            group_by=[
                SpansMetricGroupBy(
                    path="resource_name",
                    tag_name="resource_name",
                ),
            ],
        ),
        type=SpansMetricType.SPANS_METRICS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.update_spans_metric(metric_id=SPANS_METRIC_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a span-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansMetricsAPI.new

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY = ENV["SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY"]
SPANS_METRIC_DATA_ID = ENV["SPANS_METRIC_DATA_ID"]

body = DatadogAPIClient::V2::SpansMetricUpdateRequest.new({
  data: DatadogAPIClient::V2::SpansMetricUpdateData.new({
    attributes: DatadogAPIClient::V2::SpansMetricUpdateAttributes.new({
      compute: DatadogAPIClient::V2::SpansMetricUpdateCompute.new({
        include_percentiles: false,
      }),
      filter: DatadogAPIClient::V2::SpansMetricFilter.new({
        query: "@http.status_code:200 service:my-service-updated",
      }),
      group_by: [
        DatadogAPIClient::V2::SpansMetricGroupBy.new({
          path: "resource_name",
          tag_name: "resource_name",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::SpansMetricType::SPANS_METRICS,
  }),
})
p api_instance.update_spans_metric(SPANS_METRIC_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update a span-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans_metrics::SpansMetricsAPI;
use datadog_api_client::datadogV2::model::SpansMetricFilter;
use datadog_api_client::datadogV2::model::SpansMetricGroupBy;
use datadog_api_client::datadogV2::model::SpansMetricType;
use datadog_api_client::datadogV2::model::SpansMetricUpdateAttributes;
use datadog_api_client::datadogV2::model::SpansMetricUpdateCompute;
use datadog_api_client::datadogV2::model::SpansMetricUpdateData;
use datadog_api_client::datadogV2::model::SpansMetricUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "spans_metric" in the system
    let spans_metric_data_id = std::env::var("SPANS_METRIC_DATA_ID").unwrap();
    let body = SpansMetricUpdateRequest::new(SpansMetricUpdateData::new(
        SpansMetricUpdateAttributes::new()
            .compute(SpansMetricUpdateCompute::new().include_percentiles(false))
            .filter(
                SpansMetricFilter::new()
                    .query("@http.status_code:200 service:my-service-updated".to_string()),
            )
            .group_by(vec![SpansMetricGroupBy::new("resource_name".to_string())
                .tag_name("resource_name".to_string())]),
        SpansMetricType::SPANS_METRICS,
    ));
    let configuration = datadog::Configuration::new();
    let api = SpansMetricsAPI::with_config(configuration);
    let resp = api
        .update_spans_metric(spans_metric_data_id.clone(), body)
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
 * Update a span-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansMetricsApi(configuration);

// there is a valid "spans_metric" in the system
const SPANS_METRIC_DATA_ID = process.env.SPANS_METRIC_DATA_ID as string;

const params: v2.SpansMetricsApiUpdateSpansMetricRequest = {
  body: {
    data: {
      attributes: {
        compute: {
          includePercentiles: false,
        },
        filter: {
          query: "@http.status_code:200 service:my-service-updated",
        },
        groupBy: [
          {
            path: "resource_name",
            tagName: "resource_name",
          },
        ],
      },
      type: "spans_metrics",
    },
  },
  metricId: SPANS_METRIC_DATA_ID,
};

apiInstance
  .updateSpansMetric(params)
  .then((data: v2.SpansMetricResponse) => {
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

## Delete a span-based metric{% #delete-a-span-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/apm/config/metrics/{metric_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/apm/config/metrics/{metric_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/apm/config/metrics/{metric_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/apm/config/metrics/{metric_id} |

### Overview

Delete a specific span-based metric from your organization. This endpoint requires the `apm_generate_metrics` permission.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                        |
| --------------------------- | ------ | ---------------------------------- |
| metric_id [*required*] | string | The name of the span-based metric. |

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
                  \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/config/metrics/${metric_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a span-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ID = environ["SPANS_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    api_instance.delete_spans_metric(
        metric_id=SPANS_METRIC_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a span-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SpansMetricsAPI.new

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ID = ENV["SPANS_METRIC_DATA_ID"]
api_instance.delete_spans_metric(SPANS_METRIC_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a span-based metric returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "spans_metric" in the system
    SpansMetricDataID := os.Getenv("SPANS_METRIC_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewSpansMetricsApi(apiClient)
    r, err := api.DeleteSpansMetric(ctx, SpansMetricDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SpansMetricsApi.DeleteSpansMetric`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a span-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SpansMetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SpansMetricsApi apiInstance = new SpansMetricsApi(defaultClient);

    // there is a valid "spans_metric" in the system
    String SPANS_METRIC_DATA_ID = System.getenv("SPANS_METRIC_DATA_ID");

    try {
      apiInstance.deleteSpansMetric(SPANS_METRIC_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpansMetricsApi#deleteSpansMetric");
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
// Delete a span-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_spans_metrics::SpansMetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "spans_metric" in the system
    let spans_metric_data_id = std::env::var("SPANS_METRIC_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = SpansMetricsAPI::with_config(configuration);
    let resp = api.delete_spans_metric(spans_metric_data_id.clone()).await;
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
 * Delete a span-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SpansMetricsApi(configuration);

// there is a valid "spans_metric" in the system
const SPANS_METRIC_DATA_ID = process.env.SPANS_METRIC_DATA_ID as string;

const params: v2.SpansMetricsApiDeleteSpansMetricRequest = {
  metricId: SPANS_METRIC_DATA_ID,
};

apiInstance
  .deleteSpansMetric(params)
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
