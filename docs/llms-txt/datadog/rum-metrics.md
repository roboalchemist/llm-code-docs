# Source: https://docs.datadoghq.com/api/latest/rum-metrics.md

---
title: Rum Metrics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Rum Metrics
---

# Rum Metrics

Manage configuration of [rum-based metrics](https://app.datadoghq.com/rum/generate-metrics) for your organization.

## Get all rum-based metrics{% #get-all-rum-based-metrics %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/config/metrics |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/config/metrics |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/config/metrics      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/config/metrics      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/config/metrics     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/config/metrics |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/config/metrics |

### Overview

Get the list of configured rum-based metrics with their definitions.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
All the available rum-based metric objects.

| Parent field | Field               | Type     | Description                                                                                                                                 |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                | [object] | A list of rum-based metric objects.                                                                                                         |
| data         | attributes          | object   | The object describing a Datadog rum-based metric.                                                                                           |
| attributes   | compute             | object   | The compute rule to compute the rum-based metric.                                                                                           |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                   |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when `aggregation_type` is `distribution`.      |
| compute      | path                | string   | The path to the value the rum-based metric will aggregate on. Only present when `aggregation_type` is `distribution`.                       |
| attributes   | event_type          | enum     | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`                              |
| attributes   | filter              | object   | The rum-based metric filter. RUM events matching this filter will be aggregated in this metric.                                             |
| filter       | query               | string   | The search query - following the RUM search syntax.                                                                                         |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                 |
| group_by     | path                | string   | The path to the value the rum-based metric will be aggregated over.                                                                         |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, `path` is used as the tag name.                                                     |
| attributes   | uniqueness          | object   | The rule to count updatable events. Is only set if `event_type` is `session` or `view`.                                                     |
| uniqueness   | when                | enum     | When to count updatable events. `match` when the event is first seen, or `end` when the event is complete. Allowed enum values: `match,end` |
| data         | id                  | string   | The name of the rum-based metric.                                                                                                           |
| data         | type                | enum     | The type of the resource. The value should always be rum_metrics. Allowed enum values: `rum_metrics`                                        |

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
        "event_type": "session",
        "filter": {
          "query": "service:web* AND @http.status_code:[200 TO 299]"
        },
        "group_by": [
          {
            "path": "@http.status_code",
            "tag_name": "status_code"
          }
        ],
        "uniqueness": {
          "when": "match"
        }
      },
      "id": "rum.sessions.webui.count",
      "type": "rum_metrics"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/config/metrics" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all rum-based metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    response = api_instance.list_rum_metrics()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all rum-based metrics returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumMetricsAPI.new
p api_instance.list_rum_metrics()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all rum-based metrics returns "OK" response

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
	api := datadogV2.NewRumMetricsApi(apiClient)
	resp, r, err := api.ListRumMetrics(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumMetricsApi.ListRumMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumMetricsApi.ListRumMetrics`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all rum-based metrics returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumMetricsApi;
import com.datadog.api.client.v2.model.RumMetricsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumMetricsApi apiInstance = new RumMetricsApi(defaultClient);

    try {
      RumMetricsResponse result = apiInstance.listRumMetrics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumMetricsApi#listRumMetrics");
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
// Get all rum-based metrics returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_metrics::RumMetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumMetricsAPI::with_config(configuration);
    let resp = api.list_rum_metrics().await;
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
 * Get all rum-based metrics returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumMetricsApi(configuration);

apiInstance
  .listRumMetrics()
  .then((data: v2.RumMetricsResponse) => {
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

## Create a rum-based metric{% #create-a-rum-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/rum/config/metrics |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/rum/config/metrics |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/rum/config/metrics      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/rum/config/metrics      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/rum/config/metrics     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/rum/config/metrics |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/rum/config/metrics |

### Overview

Create a metric based on your organization's RUM data. Returns the rum-based metric object from the request body when the request is successful.

### Request

#### Body Data (required)

The definition of the new rum-based metric.

{% tab title="Model" %}

| Parent field | Field                              | Type     | Description                                                                                                                                 |
| ------------ | ---------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]             | object   | The new rum-based metric properties.                                                                                                        |
| data         | attributes [*required*]       | object   | The object describing the Datadog rum-based metric to create.                                                                               |
| attributes   | compute [*required*]          | object   | The compute rule to compute the rum-based metric.                                                                                           |
| compute      | aggregation_type [*required*] | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                   |
| compute      | include_percentiles                | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when `aggregation_type` is `distribution`.      |
| compute      | path                               | string   | The path to the value the rum-based metric will aggregate on. Only present when `aggregation_type` is `distribution`.                       |
| attributes   | event_type [*required*]       | enum     | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`                              |
| attributes   | filter                             | object   | The rum-based metric filter. Events matching this filter will be aggregated in this metric.                                                 |
| filter       | query [*required*]            | string   | The search query - following the RUM search syntax.                                                                                         |
| attributes   | group_by                           | [object] | The rules for the group by.                                                                                                                 |
| group_by     | path [*required*]             | string   | The path to the value the rum-based metric will be aggregated over.                                                                         |
| group_by     | tag_name                           | string   | Eventual name of the tag that gets created. By default, `path` is used as the tag name.                                                     |
| attributes   | uniqueness                         | object   | The rule to count updatable events. Is only set if `event_type` is `sessions` or `views`.                                                   |
| uniqueness   | when [*required*]             | enum     | When to count updatable events. `match` when the event is first seen, or `end` when the event is complete. Allowed enum values: `match,end` |
| data         | id [*required*]               | string   | The name of the rum-based metric.                                                                                                           |
| data         | type [*required*]             | enum     | The type of the resource. The value should always be rum_metrics. Allowed enum values: `rum_metrics`                                        |

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
      "event_type": "session",
      "filter": {
        "query": "@service:web-ui"
      },
      "group_by": [
        {
          "path": "@browser.name",
          "tag_name": "browser_name"
        }
      ],
      "uniqueness": {
        "when": "match"
      }
    },
    "id": "examplerummetric",
    "type": "rum_metrics"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
The rum-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                 |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                | object   | The rum-based metric properties.                                                                                                            |
| data         | attributes          | object   | The object describing a Datadog rum-based metric.                                                                                           |
| attributes   | compute             | object   | The compute rule to compute the rum-based metric.                                                                                           |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                   |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when `aggregation_type` is `distribution`.      |
| compute      | path                | string   | The path to the value the rum-based metric will aggregate on. Only present when `aggregation_type` is `distribution`.                       |
| attributes   | event_type          | enum     | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`                              |
| attributes   | filter              | object   | The rum-based metric filter. RUM events matching this filter will be aggregated in this metric.                                             |
| filter       | query               | string   | The search query - following the RUM search syntax.                                                                                         |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                 |
| group_by     | path                | string   | The path to the value the rum-based metric will be aggregated over.                                                                         |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, `path` is used as the tag name.                                                     |
| attributes   | uniqueness          | object   | The rule to count updatable events. Is only set if `event_type` is `session` or `view`.                                                     |
| uniqueness   | when                | enum     | When to count updatable events. `match` when the event is first seen, or `end` when the event is complete. Allowed enum values: `match,end` |
| data         | id                  | string   | The name of the rum-based metric.                                                                                                           |
| data         | type                | enum     | The type of the resource. The value should always be rum_metrics. Allowed enum values: `rum_metrics`                                        |

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
      "event_type": "session",
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]"
      },
      "group_by": [
        {
          "path": "@http.status_code",
          "tag_name": "status_code"
        }
      ],
      "uniqueness": {
        "when": "match"
      }
    },
    "id": "rum.sessions.webui.count",
    "type": "rum_metrics"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/config/metrics" \
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
        "include_percentiles": true,
        "path": "@duration"
      },
      "event_type": "session",
      "filter": {
        "query": "@service:web-ui"
      },
      "group_by": [
        {
          "path": "@browser.name",
          "tag_name": "browser_name"
        }
      ],
      "uniqueness": {
        "when": "match"
      }
    },
    "id": "examplerummetric",
    "type": "rum_metrics"
  }
}
EOF
                        
##### 

```go
// Create a rum-based metric returns "Created" response

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
	body := datadogV2.RumMetricCreateRequest{
		Data: datadogV2.RumMetricCreateData{
			Attributes: datadogV2.RumMetricCreateAttributes{
				Compute: datadogV2.RumMetricCompute{
					AggregationType:    datadogV2.RUMMETRICCOMPUTEAGGREGATIONTYPE_DISTRIBUTION,
					IncludePercentiles: datadog.PtrBool(true),
					Path:               datadog.PtrString("@duration"),
				},
				EventType: datadogV2.RUMMETRICEVENTTYPE_SESSION,
				Filter: &datadogV2.RumMetricFilter{
					Query: "@service:web-ui",
				},
				GroupBy: []datadogV2.RumMetricGroupBy{
					{
						Path:    "@browser.name",
						TagName: datadog.PtrString("browser_name"),
					},
				},
				Uniqueness: &datadogV2.RumMetricUniqueness{
					When: datadogV2.RUMMETRICUNIQUENESSWHEN_WHEN_MATCH,
				},
			},
			Id:   "examplerummetric",
			Type: datadogV2.RUMMETRICTYPE_RUM_METRICS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumMetricsApi(apiClient)
	resp, r, err := api.CreateRumMetric(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumMetricsApi.CreateRumMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumMetricsApi.CreateRumMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a rum-based metric returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumMetricsApi;
import com.datadog.api.client.v2.model.RumMetricCompute;
import com.datadog.api.client.v2.model.RumMetricComputeAggregationType;
import com.datadog.api.client.v2.model.RumMetricCreateAttributes;
import com.datadog.api.client.v2.model.RumMetricCreateData;
import com.datadog.api.client.v2.model.RumMetricCreateRequest;
import com.datadog.api.client.v2.model.RumMetricEventType;
import com.datadog.api.client.v2.model.RumMetricFilter;
import com.datadog.api.client.v2.model.RumMetricGroupBy;
import com.datadog.api.client.v2.model.RumMetricResponse;
import com.datadog.api.client.v2.model.RumMetricType;
import com.datadog.api.client.v2.model.RumMetricUniqueness;
import com.datadog.api.client.v2.model.RumMetricUniquenessWhen;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumMetricsApi apiInstance = new RumMetricsApi(defaultClient);

    RumMetricCreateRequest body =
        new RumMetricCreateRequest()
            .data(
                new RumMetricCreateData()
                    .attributes(
                        new RumMetricCreateAttributes()
                            .compute(
                                new RumMetricCompute()
                                    .aggregationType(RumMetricComputeAggregationType.DISTRIBUTION)
                                    .includePercentiles(true)
                                    .path("@duration"))
                            .eventType(RumMetricEventType.SESSION)
                            .filter(new RumMetricFilter().query("@service:web-ui"))
                            .groupBy(
                                Collections.singletonList(
                                    new RumMetricGroupBy()
                                        .path("@browser.name")
                                        .tagName("browser_name")))
                            .uniqueness(
                                new RumMetricUniqueness().when(RumMetricUniquenessWhen.WHEN_MATCH)))
                    .id("examplerummetric")
                    .type(RumMetricType.RUM_METRICS));

    try {
      RumMetricResponse result = apiInstance.createRumMetric(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumMetricsApi#createRumMetric");
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
Create a rum-based metric returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi
from datadog_api_client.v2.model.rum_metric_compute import RumMetricCompute
from datadog_api_client.v2.model.rum_metric_compute_aggregation_type import RumMetricComputeAggregationType
from datadog_api_client.v2.model.rum_metric_create_attributes import RumMetricCreateAttributes
from datadog_api_client.v2.model.rum_metric_create_data import RumMetricCreateData
from datadog_api_client.v2.model.rum_metric_create_request import RumMetricCreateRequest
from datadog_api_client.v2.model.rum_metric_event_type import RumMetricEventType
from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy
from datadog_api_client.v2.model.rum_metric_type import RumMetricType
from datadog_api_client.v2.model.rum_metric_uniqueness import RumMetricUniqueness
from datadog_api_client.v2.model.rum_metric_uniqueness_when import RumMetricUniquenessWhen

body = RumMetricCreateRequest(
    data=RumMetricCreateData(
        attributes=RumMetricCreateAttributes(
            compute=RumMetricCompute(
                aggregation_type=RumMetricComputeAggregationType.DISTRIBUTION,
                include_percentiles=True,
                path="@duration",
            ),
            event_type=RumMetricEventType.SESSION,
            filter=RumMetricFilter(
                query="@service:web-ui",
            ),
            group_by=[
                RumMetricGroupBy(
                    path="@browser.name",
                    tag_name="browser_name",
                ),
            ],
            uniqueness=RumMetricUniqueness(
                when=RumMetricUniquenessWhen.WHEN_MATCH,
            ),
        ),
        id="examplerummetric",
        type=RumMetricType.RUM_METRICS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    response = api_instance.create_rum_metric(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a rum-based metric returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumMetricsAPI.new

body = DatadogAPIClient::V2::RumMetricCreateRequest.new({
  data: DatadogAPIClient::V2::RumMetricCreateData.new({
    attributes: DatadogAPIClient::V2::RumMetricCreateAttributes.new({
      compute: DatadogAPIClient::V2::RumMetricCompute.new({
        aggregation_type: DatadogAPIClient::V2::RumMetricComputeAggregationType::DISTRIBUTION,
        include_percentiles: true,
        path: "@duration",
      }),
      event_type: DatadogAPIClient::V2::RumMetricEventType::SESSION,
      filter: DatadogAPIClient::V2::RumMetricFilter.new({
        query: "@service:web-ui",
      }),
      group_by: [
        DatadogAPIClient::V2::RumMetricGroupBy.new({
          path: "@browser.name",
          tag_name: "browser_name",
        }),
      ],
      uniqueness: DatadogAPIClient::V2::RumMetricUniqueness.new({
        _when: DatadogAPIClient::V2::RumMetricUniquenessWhen::WHEN_MATCH,
      }),
    }),
    id: "examplerummetric",
    type: DatadogAPIClient::V2::RumMetricType::RUM_METRICS,
  }),
})
p api_instance.create_rum_metric(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a rum-based metric returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_metrics::RumMetricsAPI;
use datadog_api_client::datadogV2::model::RumMetricCompute;
use datadog_api_client::datadogV2::model::RumMetricComputeAggregationType;
use datadog_api_client::datadogV2::model::RumMetricCreateAttributes;
use datadog_api_client::datadogV2::model::RumMetricCreateData;
use datadog_api_client::datadogV2::model::RumMetricCreateRequest;
use datadog_api_client::datadogV2::model::RumMetricEventType;
use datadog_api_client::datadogV2::model::RumMetricFilter;
use datadog_api_client::datadogV2::model::RumMetricGroupBy;
use datadog_api_client::datadogV2::model::RumMetricType;
use datadog_api_client::datadogV2::model::RumMetricUniqueness;
use datadog_api_client::datadogV2::model::RumMetricUniquenessWhen;

#[tokio::main]
async fn main() {
    let body = RumMetricCreateRequest::new(RumMetricCreateData::new(
        RumMetricCreateAttributes::new(
            RumMetricCompute::new(RumMetricComputeAggregationType::DISTRIBUTION)
                .include_percentiles(true)
                .path("@duration".to_string()),
            RumMetricEventType::SESSION,
        )
        .filter(RumMetricFilter::new("@service:web-ui".to_string()))
        .group_by(vec![
            RumMetricGroupBy::new("@browser.name".to_string()).tag_name("browser_name".to_string())
        ])
        .uniqueness(RumMetricUniqueness::new(
            RumMetricUniquenessWhen::WHEN_MATCH,
        )),
        "examplerummetric".to_string(),
        RumMetricType::RUM_METRICS,
    ));
    let configuration = datadog::Configuration::new();
    let api = RumMetricsAPI::with_config(configuration);
    let resp = api.create_rum_metric(body).await;
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
 * Create a rum-based metric returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumMetricsApi(configuration);

const params: v2.RumMetricsApiCreateRumMetricRequest = {
  body: {
    data: {
      attributes: {
        compute: {
          aggregationType: "distribution",
          includePercentiles: true,
          path: "@duration",
        },
        eventType: "session",
        filter: {
          query: "@service:web-ui",
        },
        groupBy: [
          {
            path: "@browser.name",
            tagName: "browser_name",
          },
        ],
        uniqueness: {
          when: "match",
        },
      },
      id: "examplerummetric",
      type: "rum_metrics",
    },
  },
};

apiInstance
  .createRumMetric(params)
  .then((data: v2.RumMetricResponse) => {
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

## Get a rum-based metric{% #get-a-rum-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/config/metrics/{metric_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/config/metrics/{metric_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/config/metrics/{metric_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |

### Overview

Get a specific rum-based metric from your organization.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| metric_id [*required*] | string | The name of the rum-based metric. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The rum-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                 |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                | object   | The rum-based metric properties.                                                                                                            |
| data         | attributes          | object   | The object describing a Datadog rum-based metric.                                                                                           |
| attributes   | compute             | object   | The compute rule to compute the rum-based metric.                                                                                           |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                   |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when `aggregation_type` is `distribution`.      |
| compute      | path                | string   | The path to the value the rum-based metric will aggregate on. Only present when `aggregation_type` is `distribution`.                       |
| attributes   | event_type          | enum     | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`                              |
| attributes   | filter              | object   | The rum-based metric filter. RUM events matching this filter will be aggregated in this metric.                                             |
| filter       | query               | string   | The search query - following the RUM search syntax.                                                                                         |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                 |
| group_by     | path                | string   | The path to the value the rum-based metric will be aggregated over.                                                                         |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, `path` is used as the tag name.                                                     |
| attributes   | uniqueness          | object   | The rule to count updatable events. Is only set if `event_type` is `session` or `view`.                                                     |
| uniqueness   | when                | enum     | When to count updatable events. `match` when the event is first seen, or `end` when the event is complete. Allowed enum values: `match,end` |
| data         | id                  | string   | The name of the rum-based metric.                                                                                                           |
| data         | type                | enum     | The type of the resource. The value should always be rum_metrics. Allowed enum values: `rum_metrics`                                        |

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
      "event_type": "session",
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]"
      },
      "group_by": [
        {
          "path": "@http.status_code",
          "tag_name": "status_code"
        }
      ],
      "uniqueness": {
        "when": "match"
      }
    },
    "id": "rum.sessions.webui.count",
    "type": "rum_metrics"
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
                  \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a rum-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = environ["RUM_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    response = api_instance.get_rum_metric(
        metric_id=RUM_METRIC_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get a rum-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumMetricsAPI.new

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = ENV["RUM_METRIC_DATA_ID"]
p api_instance.get_rum_metric(RUM_METRIC_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get a rum-based metric returns "OK" response

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
	// there is a valid "rum_metric" in the system
	RumMetricDataID := os.Getenv("RUM_METRIC_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumMetricsApi(apiClient)
	resp, r, err := api.GetRumMetric(ctx, RumMetricDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumMetricsApi.GetRumMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumMetricsApi.GetRumMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get a rum-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumMetricsApi;
import com.datadog.api.client.v2.model.RumMetricResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumMetricsApi apiInstance = new RumMetricsApi(defaultClient);

    // there is a valid "rum_metric" in the system
    String RUM_METRIC_DATA_ID = System.getenv("RUM_METRIC_DATA_ID");

    try {
      RumMetricResponse result = apiInstance.getRumMetric(RUM_METRIC_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumMetricsApi#getRumMetric");
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
// Get a rum-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_metrics::RumMetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "rum_metric" in the system
    let rum_metric_data_id = std::env::var("RUM_METRIC_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RumMetricsAPI::with_config(configuration);
    let resp = api.get_rum_metric(rum_metric_data_id.clone()).await;
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
 * Get a rum-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumMetricsApi(configuration);

// there is a valid "rum_metric" in the system
const RUM_METRIC_DATA_ID = process.env.RUM_METRIC_DATA_ID as string;

const params: v2.RumMetricsApiGetRumMetricRequest = {
  metricId: RUM_METRIC_DATA_ID,
};

apiInstance
  .getRumMetric(params)
  .then((data: v2.RumMetricResponse) => {
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

## Update a rum-based metric{% #update-a-rum-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/rum/config/metrics/{metric_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/rum/config/metrics/{metric_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/rum/config/metrics/{metric_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |

### Overview

Update a specific rum-based metric from your organization. Returns the rum-based metric object from the request body when the request is successful.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| metric_id [*required*] | string | The name of the rum-based metric. |

### Request

#### Body Data (required)

New definition of the rum-based metric.

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                            |
| ------------ | ---------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | The new rum-based metric properties.                                                                                                   |
| data         | attributes [*required*] | object   | The rum-based metric properties that will be updated.                                                                                  |
| attributes   | compute                      | object   | The compute rule to compute the rum-based metric.                                                                                      |
| compute      | include_percentiles          | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when `aggregation_type` is `distribution`. |
| attributes   | filter                       | object   | The rum-based metric filter. Events matching this filter will be aggregated in this metric.                                            |
| filter       | query [*required*]      | string   | The search query - following the RUM search syntax.                                                                                    |
| attributes   | group_by                     | [object] | The rules for the group by.                                                                                                            |
| group_by     | path [*required*]       | string   | The path to the value the rum-based metric will be aggregated over.                                                                    |
| group_by     | tag_name                     | string   | Eventual name of the tag that gets created. By default, `path` is used as the tag name.                                                |
| data         | id                           | string   | The name of the rum-based metric.                                                                                                      |
| data         | type [*required*]       | enum     | The type of the resource. The value should always be rum_metrics. Allowed enum values: `rum_metrics`                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "rum.sessions.webui.count",
    "type": "rum_metrics",
    "attributes": {
      "compute": {
        "include_percentiles": false
      },
      "filter": {
        "query": "@service:rum-config"
      },
      "group_by": [
        {
          "path": "@browser.version",
          "tag_name": "browser_version"
        }
      ]
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The rum-based metric object.

| Parent field | Field               | Type     | Description                                                                                                                                 |
| ------------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                | object   | The rum-based metric properties.                                                                                                            |
| data         | attributes          | object   | The object describing a Datadog rum-based metric.                                                                                           |
| attributes   | compute             | object   | The compute rule to compute the rum-based metric.                                                                                           |
| compute      | aggregation_type    | enum     | The type of aggregation to use. Allowed enum values: `count,distribution`                                                                   |
| compute      | include_percentiles | boolean  | Toggle to include or exclude percentile aggregations for distribution metrics. Only present when `aggregation_type` is `distribution`.      |
| compute      | path                | string   | The path to the value the rum-based metric will aggregate on. Only present when `aggregation_type` is `distribution`.                       |
| attributes   | event_type          | enum     | The type of RUM events to filter on. Allowed enum values: `session,view,action,error,resource,long_task,vital`                              |
| attributes   | filter              | object   | The rum-based metric filter. RUM events matching this filter will be aggregated in this metric.                                             |
| filter       | query               | string   | The search query - following the RUM search syntax.                                                                                         |
| attributes   | group_by            | [object] | The rules for the group by.                                                                                                                 |
| group_by     | path                | string   | The path to the value the rum-based metric will be aggregated over.                                                                         |
| group_by     | tag_name            | string   | Eventual name of the tag that gets created. By default, `path` is used as the tag name.                                                     |
| attributes   | uniqueness          | object   | The rule to count updatable events. Is only set if `event_type` is `session` or `view`.                                                     |
| uniqueness   | when                | enum     | When to count updatable events. `match` when the event is first seen, or `end` when the event is complete. Allowed enum values: `match,end` |
| data         | id                  | string   | The name of the rum-based metric.                                                                                                           |
| data         | type                | enum     | The type of the resource. The value should always be rum_metrics. Allowed enum values: `rum_metrics`                                        |

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
      "event_type": "session",
      "filter": {
        "query": "service:web* AND @http.status_code:[200 TO 299]"
      },
      "group_by": [
        {
          "path": "@http.status_code",
          "tag_name": "status_code"
        }
      ],
      "uniqueness": {
        "when": "match"
      }
    },
    "id": "rum.sessions.webui.count",
    "type": "rum_metrics"
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
                          \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "rum.sessions.webui.count",
    "type": "rum_metrics",
    "attributes": {
      "compute": {
        "include_percentiles": false
      },
      "filter": {
        "query": "@service:rum-config"
      },
      "group_by": [
        {
          "path": "@browser.version",
          "tag_name": "browser_version"
        }
      ]
    }
  }
}
EOF
                        
##### 

```go
// Update a rum-based metric returns "OK" response

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
	// there is a valid "rum_metric" in the system
	RumMetricDataID := os.Getenv("RUM_METRIC_DATA_ID")

	body := datadogV2.RumMetricUpdateRequest{
		Data: datadogV2.RumMetricUpdateData{
			Id:   datadog.PtrString(RumMetricDataID),
			Type: datadogV2.RUMMETRICTYPE_RUM_METRICS,
			Attributes: datadogV2.RumMetricUpdateAttributes{
				Compute: &datadogV2.RumMetricUpdateCompute{
					IncludePercentiles: datadog.PtrBool(false),
				},
				Filter: &datadogV2.RumMetricFilter{
					Query: "@service:rum-config",
				},
				GroupBy: []datadogV2.RumMetricGroupBy{
					{
						Path:    "@browser.version",
						TagName: datadog.PtrString("browser_version"),
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumMetricsApi(apiClient)
	resp, r, err := api.UpdateRumMetric(ctx, RumMetricDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumMetricsApi.UpdateRumMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumMetricsApi.UpdateRumMetric`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update a rum-based metric returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumMetricsApi;
import com.datadog.api.client.v2.model.RumMetricFilter;
import com.datadog.api.client.v2.model.RumMetricGroupBy;
import com.datadog.api.client.v2.model.RumMetricResponse;
import com.datadog.api.client.v2.model.RumMetricType;
import com.datadog.api.client.v2.model.RumMetricUpdateAttributes;
import com.datadog.api.client.v2.model.RumMetricUpdateCompute;
import com.datadog.api.client.v2.model.RumMetricUpdateData;
import com.datadog.api.client.v2.model.RumMetricUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumMetricsApi apiInstance = new RumMetricsApi(defaultClient);

    // there is a valid "rum_metric" in the system
    String RUM_METRIC_DATA_ID = System.getenv("RUM_METRIC_DATA_ID");

    RumMetricUpdateRequest body =
        new RumMetricUpdateRequest()
            .data(
                new RumMetricUpdateData()
                    .id(RUM_METRIC_DATA_ID)
                    .type(RumMetricType.RUM_METRICS)
                    .attributes(
                        new RumMetricUpdateAttributes()
                            .compute(new RumMetricUpdateCompute().includePercentiles(false))
                            .filter(new RumMetricFilter().query("@service:rum-config"))
                            .groupBy(
                                Collections.singletonList(
                                    new RumMetricGroupBy()
                                        .path("@browser.version")
                                        .tagName("browser_version")))));

    try {
      RumMetricResponse result = apiInstance.updateRumMetric(RUM_METRIC_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumMetricsApi#updateRumMetric");
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
Update a rum-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi
from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy
from datadog_api_client.v2.model.rum_metric_type import RumMetricType
from datadog_api_client.v2.model.rum_metric_update_attributes import RumMetricUpdateAttributes
from datadog_api_client.v2.model.rum_metric_update_compute import RumMetricUpdateCompute
from datadog_api_client.v2.model.rum_metric_update_data import RumMetricUpdateData
from datadog_api_client.v2.model.rum_metric_update_request import RumMetricUpdateRequest

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = environ["RUM_METRIC_DATA_ID"]

body = RumMetricUpdateRequest(
    data=RumMetricUpdateData(
        id=RUM_METRIC_DATA_ID,
        type=RumMetricType.RUM_METRICS,
        attributes=RumMetricUpdateAttributes(
            compute=RumMetricUpdateCompute(
                include_percentiles=False,
            ),
            filter=RumMetricFilter(
                query="@service:rum-config",
            ),
            group_by=[
                RumMetricGroupBy(
                    path="@browser.version",
                    tag_name="browser_version",
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    response = api_instance.update_rum_metric(metric_id=RUM_METRIC_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update a rum-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumMetricsAPI.new

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = ENV["RUM_METRIC_DATA_ID"]

body = DatadogAPIClient::V2::RumMetricUpdateRequest.new({
  data: DatadogAPIClient::V2::RumMetricUpdateData.new({
    id: RUM_METRIC_DATA_ID,
    type: DatadogAPIClient::V2::RumMetricType::RUM_METRICS,
    attributes: DatadogAPIClient::V2::RumMetricUpdateAttributes.new({
      compute: DatadogAPIClient::V2::RumMetricUpdateCompute.new({
        include_percentiles: false,
      }),
      filter: DatadogAPIClient::V2::RumMetricFilter.new({
        query: "@service:rum-config",
      }),
      group_by: [
        DatadogAPIClient::V2::RumMetricGroupBy.new({
          path: "@browser.version",
          tag_name: "browser_version",
        }),
      ],
    }),
  }),
})
p api_instance.update_rum_metric(RUM_METRIC_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update a rum-based metric returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_metrics::RumMetricsAPI;
use datadog_api_client::datadogV2::model::RumMetricFilter;
use datadog_api_client::datadogV2::model::RumMetricGroupBy;
use datadog_api_client::datadogV2::model::RumMetricType;
use datadog_api_client::datadogV2::model::RumMetricUpdateAttributes;
use datadog_api_client::datadogV2::model::RumMetricUpdateCompute;
use datadog_api_client::datadogV2::model::RumMetricUpdateData;
use datadog_api_client::datadogV2::model::RumMetricUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "rum_metric" in the system
    let rum_metric_data_id = std::env::var("RUM_METRIC_DATA_ID").unwrap();
    let body = RumMetricUpdateRequest::new(
        RumMetricUpdateData::new(
            RumMetricUpdateAttributes::new()
                .compute(RumMetricUpdateCompute::new().include_percentiles(false))
                .filter(RumMetricFilter::new("@service:rum-config".to_string()))
                .group_by(vec![RumMetricGroupBy::new("@browser.version".to_string())
                    .tag_name("browser_version".to_string())]),
            RumMetricType::RUM_METRICS,
        )
        .id(rum_metric_data_id.clone()),
    );
    let configuration = datadog::Configuration::new();
    let api = RumMetricsAPI::with_config(configuration);
    let resp = api
        .update_rum_metric(rum_metric_data_id.clone(), body)
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
 * Update a rum-based metric returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumMetricsApi(configuration);

// there is a valid "rum_metric" in the system
const RUM_METRIC_DATA_ID = process.env.RUM_METRIC_DATA_ID as string;

const params: v2.RumMetricsApiUpdateRumMetricRequest = {
  body: {
    data: {
      id: RUM_METRIC_DATA_ID,
      type: "rum_metrics",
      attributes: {
        compute: {
          includePercentiles: false,
        },
        filter: {
          query: "@service:rum-config",
        },
        groupBy: [
          {
            path: "@browser.version",
            tagName: "browser_version",
          },
        ],
      },
    },
  },
  metricId: RUM_METRIC_DATA_ID,
};

apiInstance
  .updateRumMetric(params)
  .then((data: v2.RumMetricResponse) => {
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

## Delete a rum-based metric{% #delete-a-rum-based-metric %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/rum/config/metrics/{metric_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/rum/config/metrics/{metric_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/rum/config/metrics/{metric_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/rum/config/metrics/{metric_id} |

### Overview

Delete a specific rum-based metric from your organization.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| metric_id [*required*] | string | The name of the rum-based metric. |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport metric_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/config/metrics/${metric_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a rum-based metric returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = environ["RUM_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    api_instance.delete_rum_metric(
        metric_id=RUM_METRIC_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a rum-based metric returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumMetricsAPI.new

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = ENV["RUM_METRIC_DATA_ID"]
api_instance.delete_rum_metric(RUM_METRIC_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a rum-based metric returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "rum_metric" in the system
	RumMetricDataID := os.Getenv("RUM_METRIC_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumMetricsApi(apiClient)
	r, err := api.DeleteRumMetric(ctx, RumMetricDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumMetricsApi.DeleteRumMetric`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a rum-based metric returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumMetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumMetricsApi apiInstance = new RumMetricsApi(defaultClient);

    // there is a valid "rum_metric" in the system
    String RUM_METRIC_DATA_ID = System.getenv("RUM_METRIC_DATA_ID");

    try {
      apiInstance.deleteRumMetric(RUM_METRIC_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumMetricsApi#deleteRumMetric");
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
// Delete a rum-based metric returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_metrics::RumMetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "rum_metric" in the system
    let rum_metric_data_id = std::env::var("RUM_METRIC_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = RumMetricsAPI::with_config(configuration);
    let resp = api.delete_rum_metric(rum_metric_data_id.clone()).await;
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
 * Delete a rum-based metric returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumMetricsApi(configuration);

// there is a valid "rum_metric" in the system
const RUM_METRIC_DATA_ID = process.env.RUM_METRIC_DATA_ID as string;

const params: v2.RumMetricsApiDeleteRumMetricRequest = {
  metricId: RUM_METRIC_DATA_ID,
};

apiInstance
  .deleteRumMetric(params)
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
