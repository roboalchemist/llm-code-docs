# Source: https://docs.datadoghq.com/api/latest/logs-metrics/

# Logs Metrics
Manage configuration of [log-based metrics](https://app.datadoghq.com/logs/pipelines/generate-metrics) for your organization.
## [Get all log-based metrics](https://docs.datadoghq.com/api/latest/logs-metrics/#get-all-log-based-metrics)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-metrics/#get-all-log-based-metrics-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/metricshttps://api.ap2.datadoghq.com/api/v2/logs/config/metricshttps://api.datadoghq.eu/api/v2/logs/config/metricshttps://api.ddog-gov.com/api/v2/logs/config/metricshttps://api.datadoghq.com/api/v2/logs/config/metricshttps://api.us3.datadoghq.com/api/v2/logs/config/metricshttps://api.us5.datadoghq.com/api/v2/logs/config/metrics
### Overview
Get the list of configured log-based metrics with their definitions. This endpoint requires the `logs_read_config` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-metrics/#ListLogsMetrics-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-metrics/#ListLogsMetrics-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-metrics/#ListLogsMetrics-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


All the available log-based metric objects.
Field
Type
Description
data
[object]
A list of log-based metric objects.
attributes
object
The object describing a Datadog log-based metric.
compute
object
The compute rule to compute the log-based metric.
aggregation_type
enum
The type of aggregation to use. Allowed enum values: `count,distribution`
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`.
path
string
The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").
filter
object
The log-based metric filter. Logs matching this filter will be aggregated in this metric.
query
string
The search query - following the log search syntax.
group_by
[object]
The rules for the group by.
path
string
The path to the value the log-based metric will be aggregated over.
tag_name
string
Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
id
string
The name of the log-based metric.
type
enum
The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`
default: `logs_metrics`
```
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

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=typescript)


#####  Get all log-based metrics
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all log-based metrics
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all log-based metrics
```
# Get all log-based metrics returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new
p api_instance.list_logs_metrics()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all log-based metrics
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all log-based metrics
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get all log-based metrics
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get all log-based metrics
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a log-based metric](https://docs.datadoghq.com/api/latest/logs-metrics/#create-a-log-based-metric)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-metrics/#create-a-log-based-metric-v2)


POST https://api.ap1.datadoghq.com/api/v2/logs/config/metricshttps://api.ap2.datadoghq.com/api/v2/logs/config/metricshttps://api.datadoghq.eu/api/v2/logs/config/metricshttps://api.ddog-gov.com/api/v2/logs/config/metricshttps://api.datadoghq.com/api/v2/logs/config/metricshttps://api.us3.datadoghq.com/api/v2/logs/config/metricshttps://api.us5.datadoghq.com/api/v2/logs/config/metrics
### Overview
Create a metric based on your ingested logs in your organization. Returns the log-based metric object from the request body when the request is successful. This endpoint requires the `logs_generate_metrics` permission.
### Request
#### Body Data (required)
The definition of the new log-based metric.
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


Field
Type
Description
data [_required_]
object
The new log-based metric properties.
attributes [_required_]
object
The object describing the Datadog log-based metric to create.
compute [_required_]
object
The compute rule to compute the log-based metric.
aggregation_type [_required_]
enum
The type of aggregation to use. Allowed enum values: `count,distribution`
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`.
path
string
The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").
filter
object
The log-based metric filter. Logs matching this filter will be aggregated in this metric.
query
string
The search query - following the log search syntax.
default: `*`
group_by
[object]
The rules for the group by.
path [_required_]
string
The path to the value the log-based metric will be aggregated over.
tag_name
string
Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
id [_required_]
string
The name of the log-based metric.
type [_required_]
enum
The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`
default: `logs_metrics`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-metrics/#CreateLogsMetric-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-metrics/#CreateLogsMetric-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-metrics/#CreateLogsMetric-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/logs-metrics/#CreateLogsMetric-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-metrics/#CreateLogsMetric-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


The log-based metric object.
Field
Type
Description
data
object
The log-based metric properties.
attributes
object
The object describing a Datadog log-based metric.
compute
object
The compute rule to compute the log-based metric.
aggregation_type
enum
The type of aggregation to use. Allowed enum values: `count,distribution`
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`.
path
string
The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").
filter
object
The log-based metric filter. Logs matching this filter will be aggregated in this metric.
query
string
The search query - following the log search syntax.
group_by
[object]
The rules for the group by.
path
string
The path to the value the log-based metric will be aggregated over.
tag_name
string
Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
id
string
The name of the log-based metric.
type
enum
The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`
default: `logs_metrics`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=typescript)


#####  Create a log-based metric returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics" \
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

                        
```

#####  Create a log-based metric returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a log-based metric returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a log-based metric returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a log-based metric returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a log-based metric returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a log-based metric returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a log-based metric](https://docs.datadoghq.com/api/latest/logs-metrics/#get-a-log-based-metric)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-metrics/#get-a-log-based-metric-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.ap2.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.datadoghq.eu/api/v2/logs/config/metrics/{metric_id}https://api.ddog-gov.com/api/v2/logs/config/metrics/{metric_id}https://api.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.us3.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.us5.datadoghq.com/api/v2/logs/config/metrics/{metric_id}
### Overview
Get a specific log-based metric from your organization. This endpoint requires the `logs_read_config` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_id [_required_]
string
The name of the log-based metric.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-metrics/#GetLogsMetric-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-metrics/#GetLogsMetric-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-metrics/#GetLogsMetric-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-metrics/#GetLogsMetric-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


The log-based metric object.
Field
Type
Description
data
object
The log-based metric properties.
attributes
object
The object describing a Datadog log-based metric.
compute
object
The compute rule to compute the log-based metric.
aggregation_type
enum
The type of aggregation to use. Allowed enum values: `count,distribution`
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`.
path
string
The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").
filter
object
The log-based metric filter. Logs matching this filter will be aggregated in this metric.
query
string
The search query - following the log search syntax.
group_by
[object]
The rules for the group by.
path
string
The path to the value the log-based metric will be aggregated over.
tag_name
string
Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
id
string
The name of the log-based metric.
type
enum
The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`
default: `logs_metrics`
```
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

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=typescript)


#####  Get a log-based metric
Copy
```
                  # Path parameters  
export metric_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a log-based metric
```
# Get a log-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ID = ENV["LOGS_METRIC_DATA_ID"]
p api_instance.get_logs_metric(LOGS_METRIC_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a log-based metric](https://docs.datadoghq.com/api/latest/logs-metrics/#update-a-log-based-metric)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-metrics/#update-a-log-based-metric-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.ap2.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.datadoghq.eu/api/v2/logs/config/metrics/{metric_id}https://api.ddog-gov.com/api/v2/logs/config/metrics/{metric_id}https://api.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.us3.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.us5.datadoghq.com/api/v2/logs/config/metrics/{metric_id}
### Overview
Update a specific log-based metric from your organization. Returns the log-based metric object from the request body when the request is successful. This endpoint requires the `logs_generate_metrics` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_id [_required_]
string
The name of the log-based metric.
### Request
#### Body Data (required)
New definition of the log-based metric.
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


Field
Type
Description
data [_required_]
object
The new log-based metric properties.
attributes [_required_]
object
The log-based metric properties that will be updated.
compute
object
The compute rule to compute the log-based metric.
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`.
filter
object
The log-based metric filter. Logs matching this filter will be aggregated in this metric.
query
string
The search query - following the log search syntax.
default: `*`
group_by
[object]
The rules for the group by.
path [_required_]
string
The path to the value the log-based metric will be aggregated over.
tag_name
string
Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
type [_required_]
enum
The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`
default: `logs_metrics`
#####  Update a log-based metric returns "OK" response
```
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

Copy
#####  Update a log-based metric with include_percentiles field returns "OK" response
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-metrics/#UpdateLogsMetric-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-metrics/#UpdateLogsMetric-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-metrics/#UpdateLogsMetric-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-metrics/#UpdateLogsMetric-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-metrics/#UpdateLogsMetric-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


The log-based metric object.
Field
Type
Description
data
object
The log-based metric properties.
attributes
object
The object describing a Datadog log-based metric.
compute
object
The compute rule to compute the log-based metric.
aggregation_type
enum
The type of aggregation to use. Allowed enum values: `count,distribution`
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `aggregation_type` is `distribution`.
path
string
The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").
filter
object
The log-based metric filter. Logs matching this filter will be aggregated in this metric.
query
string
The search query - following the log search syntax.
group_by
[object]
The rules for the group by.
path
string
The path to the value the log-based metric will be aggregated over.
tag_name
string
Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
id
string
The name of the log-based metric.
type
enum
The type of the resource. The value should always be logs_metrics. Allowed enum values: `logs_metrics`
default: `logs_metrics`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=typescript)


#####  Update a log-based metric returns "OK" response
Copy
```
                          # Path parameters  
export metric_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
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

                        
```

#####  Update a log-based metric with include_percentiles field returns "OK" response
Copy
```
                          # Path parameters  
export metric_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
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

                        
```

#####  Update a log-based metric returns "OK" response 
```
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

Copy
#####  Update a log-based metric with include_percentiles field returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a log-based metric returns "OK" response 
```
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

Copy
#####  Update a log-based metric with include_percentiles field returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a log-based metric returns "OK" response 
```
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

Copy
#####  Update a log-based metric with include_percentiles field returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a log-based metric returns "OK" response 
```
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

Copy
#####  Update a log-based metric with include_percentiles field returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a log-based metric returns "OK" response 
```
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

Copy
#####  Update a log-based metric with include_percentiles field returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a log-based metric returns "OK" response 
```
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

Copy
#####  Update a log-based metric with include_percentiles field returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete a log-based metric](https://docs.datadoghq.com/api/latest/logs-metrics/#delete-a-log-based-metric)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-metrics/#delete-a-log-based-metric-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.ap2.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.datadoghq.eu/api/v2/logs/config/metrics/{metric_id}https://api.ddog-gov.com/api/v2/logs/config/metrics/{metric_id}https://api.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.us3.datadoghq.com/api/v2/logs/config/metrics/{metric_id}https://api.us5.datadoghq.com/api/v2/logs/config/metrics/{metric_id}
### Overview
Delete a specific log-based metric from your organization. This endpoint requires the `logs_generate_metrics` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_id [_required_]
string
The name of the log-based metric.
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-metrics/#DeleteLogsMetric-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-metrics/#DeleteLogsMetric-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-metrics/#DeleteLogsMetric-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-metrics/#DeleteLogsMetric-429-v2)


OK
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-metrics/?code-lang=typescript)


#####  Delete a log-based metric
Copy
```
                  # Path parameters  
export metric_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/metrics/${metric_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a log-based metric
```
# Delete a log-based metric returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsMetricsAPI.new

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ID = ENV["LOGS_METRIC_DATA_ID"]
api_instance.delete_logs_metric(LOGS_METRIC_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete a log-based metric
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=5e9e70e3-641d-43b8-a0e4-9a19b0bbbadf&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d26e35da-5fae-450c-983a-4246a23ddd6a&pt=Logs%20Metrics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-metrics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=5e9e70e3-641d-43b8-a0e4-9a19b0bbbadf&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d26e35da-5fae-450c-983a-4246a23ddd6a&pt=Logs%20Metrics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-metrics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
Feedback
## Was this page helpful?
Yes 🎉
No 👎
Next
![](https://survey-images.hotjar.com/surveys/logo/90f40352a7464c849f5ce82ccd0e758d)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=839fbc45-1e3c-482f-a54f-4e463c9c7a6c&bo=2&sid=c4ba0d50f0bf11f09afde9c0412ba014&vid=c4ba67e0f0bf11f099fcdb9b6c7a6b3e&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Logs%20Metrics&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-metrics%2F&r=&lt=1167&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=874204)
