# Source: https://docs.datadoghq.com/api/latest/metrics

# Metrics
The metrics endpoint allows you to:
  * Post metrics data so it can be graphed on Datadog’s dashboards
  * Query metrics from any time period
  * Modify tag configurations for metrics
  * View tags and volumes for metrics


**Note** : A graph can only contain a set number of points and as the timeframe over which a metric is viewed increases, aggregation between points occurs to stay below that set number.
The Post, Patch, and Delete `manage_tags` API methods can only be performed by a user who has the `Manage Tags for Metrics` permission.
See the [Metrics page](https://docs.datadoghq.com/metrics/) for more information.
## [Create a tag configuration](https://docs.datadoghq.com/api/latest/metrics/#create-a-tag-configuration)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#create-a-tag-configuration-v2)


POST https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/tagshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/tags
### Overview
Create and define a list of queryable tag keys for an existing count/gauge/rate/distribution metric. Optionally, include percentile aggregations on any distribution metric. By setting `exclude_tags_mode` to true, the behavior is changed from an allow-list to a deny-list, and tags in the defined list are not queryable. Can only be used with application keys of users with the `Manage Tags for Metrics` permission. This endpoint requires the `metric_tags_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
data [_required_]
object
Object for a single metric to be configure tags on.
attributes
object
Object containing the definition of a metric tag configuration to be created.
aggregations
[object]
Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.
space [_required_]
enum
A space aggregation for use in query. Allowed enum values: `avg,max,min,sum`
time [_required_]
enum
A time aggregation for use in query. Allowed enum values: `avg,count,max,min,sum`
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags. Defaults to false. Requires `tags` property.
include_percentiles
boolean
Toggle to include/exclude percentiles for a distribution metric. Defaults to false. Can only be applied to metrics that have a `metric_type` of `distribution`.
metric_type [_required_]
enum
The metric's type. Allowed enum values: `gauge,count,rate,distribution`
default: `gauge`
tags [_required_]
[string]
A list of tag keys that will be queryable for your metric.
default: 
id [_required_]
string
The metric name for this resource.
type [_required_]
enum
The metric tag configuration resource type. Allowed enum values: `manage_tags`
default: `manage_tags`
```
{
  "data": {
    "type": "manage_tags",
    "id": "ExampleMetric",
    "attributes": {
      "tags": [
        "app",
        "datacenter"
      ],
      "metric_type": "gauge"
    }
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/metrics/#CreateTagConfiguration-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#CreateTagConfiguration-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#CreateTagConfiguration-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/metrics/#CreateTagConfiguration-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#CreateTagConfiguration-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object which includes a single metric’s tag configuration.
Field
Type
Description
data
object
Object for a single metric tag configuration.
attributes
object
Object containing the definition of a metric tag configuration attributes.
aggregations
[object]
Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.
space [_required_]
enum
A space aggregation for use in query. Allowed enum values: `avg,max,min,sum`
time [_required_]
enum
A time aggregation for use in query. Allowed enum values: `avg,count,max,min,sum`
created_at
date-time
Timestamp when the tag configuration was created.
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags. Defaults to false. Requires `tags` property.
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `metric_type` is `distribution`.
metric_type
enum
The metric's type. Allowed enum values: `gauge,count,rate,distribution`
default: `gauge`
modified_at
date-time
Timestamp when the tag configuration was last modified.
tags
[string]
List of tag keys on which to group.
id
string
The metric name for this resource.
type
enum
The metric tag configuration resource type. Allowed enum values: `manage_tags`
default: `manage_tags`
```
{
  "data": {
    "attributes": {
      "aggregations": [
        {
          "space": "sum",
          "time": "sum"
        }
      ],
      "created_at": "2020-03-25T09:48:37.463835Z",
      "exclude_tags_mode": false,
      "include_percentiles": true,
      "metric_type": "count",
      "modified_at": "2020-03-25T09:48:37.463835Z",
      "tags": [
        "app",
        "datacenter"
      ]
    },
    "id": "test.metric.latency",
    "type": "manage_tags"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Create a tag configuration returns "Created" response
Copy
```
                          # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/tags" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "manage_tags",
    "id": "ExampleMetric",
    "attributes": {
      "tags": [
        "app",
        "datacenter"
      ],
      "metric_type": "gauge"
    }
  }
}
EOF  

                        
```

#####  Create a tag configuration returns "Created" response
```
// Create a tag configuration returns "Created" response

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
	body := datadogV2.MetricTagConfigurationCreateRequest{
		Data: datadogV2.MetricTagConfigurationCreateData{
			Type: datadogV2.METRICTAGCONFIGURATIONTYPE_MANAGE_TAGS,
			Id:   "ExampleMetric",
			Attributes: &datadogV2.MetricTagConfigurationCreateAttributes{
				Tags: []string{
					"app",
					"datacenter",
				},
				MetricType: datadogV2.METRICTAGCONFIGURATIONMETRICTYPES_GAUGE,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.CreateTagConfiguration(ctx, "ExampleMetric", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.CreateTagConfiguration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.CreateTagConfiguration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a tag configuration returns "Created" response
```
// Create a tag configuration returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricTagConfigurationCreateAttributes;
import com.datadog.api.client.v2.model.MetricTagConfigurationCreateData;
import com.datadog.api.client.v2.model.MetricTagConfigurationCreateRequest;
import com.datadog.api.client.v2.model.MetricTagConfigurationMetricTypes;
import com.datadog.api.client.v2.model.MetricTagConfigurationResponse;
import com.datadog.api.client.v2.model.MetricTagConfigurationType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    MetricTagConfigurationCreateRequest body =
        new MetricTagConfigurationCreateRequest()
            .data(
                new MetricTagConfigurationCreateData()
                    .type(MetricTagConfigurationType.MANAGE_TAGS)
                    .id("ExampleMetric")
                    .attributes(
                        new MetricTagConfigurationCreateAttributes()
                            .tags(Arrays.asList("app", "datacenter"))
                            .metricType(MetricTagConfigurationMetricTypes.GAUGE)));

    try {
      MetricTagConfigurationResponse result =
          apiInstance.createTagConfiguration("ExampleMetric", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#createTagConfiguration");
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

#####  Create a tag configuration returns "Created" response
```
"""
Create a tag configuration returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_tag_configuration_create_attributes import (
    MetricTagConfigurationCreateAttributes,
)
from datadog_api_client.v2.model.metric_tag_configuration_create_data import MetricTagConfigurationCreateData
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequest
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes
from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

body = MetricTagConfigurationCreateRequest(
    data=MetricTagConfigurationCreateData(
        type=MetricTagConfigurationType.MANAGE_TAGS,
        id="ExampleMetric",
        attributes=MetricTagConfigurationCreateAttributes(
            tags=[
                "app",
                "datacenter",
            ],
            metric_type=MetricTagConfigurationMetricTypes.GAUGE,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_configuration(metric_name="ExampleMetric", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a tag configuration returns "Created" response
```
# Create a tag configuration returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

body = DatadogAPIClient::V2::MetricTagConfigurationCreateRequest.new({
  data: DatadogAPIClient::V2::MetricTagConfigurationCreateData.new({
    type: DatadogAPIClient::V2::MetricTagConfigurationType::MANAGE_TAGS,
    id: "ExampleMetric",
    attributes: DatadogAPIClient::V2::MetricTagConfigurationCreateAttributes.new({
      tags: [
        "app",
        "datacenter",
      ],
      metric_type: DatadogAPIClient::V2::MetricTagConfigurationMetricTypes::GAUGE,
    }),
  }),
})
p api_instance.create_tag_configuration("ExampleMetric", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a tag configuration returns "Created" response
```
// Create a tag configuration returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::model::MetricTagConfigurationCreateAttributes;
use datadog_api_client::datadogV2::model::MetricTagConfigurationCreateData;
use datadog_api_client::datadogV2::model::MetricTagConfigurationCreateRequest;
use datadog_api_client::datadogV2::model::MetricTagConfigurationMetricTypes;
use datadog_api_client::datadogV2::model::MetricTagConfigurationType;

#[tokio::main]
async fn main() {
    let body = MetricTagConfigurationCreateRequest::new(
        MetricTagConfigurationCreateData::new(
            "ExampleMetric".to_string(),
            MetricTagConfigurationType::MANAGE_TAGS,
        )
        .attributes(MetricTagConfigurationCreateAttributes::new(
            MetricTagConfigurationMetricTypes::GAUGE,
            vec!["app".to_string(), "datacenter".to_string()],
        )),
    );
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .create_tag_configuration("ExampleMetric".to_string(), body)
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

#####  Create a tag configuration returns "Created" response
```
/**
 * Create a tag configuration returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiCreateTagConfigurationRequest = {
  body: {
    data: {
      type: "manage_tags",
      id: "ExampleMetric",
      attributes: {
        tags: ["app", "datacenter"],
        metricType: "gauge",
      },
    },
  },
  metricName: "ExampleMetric",
};

apiInstance
  .createTagConfiguration(params)
  .then((data: v2.MetricTagConfigurationResponse) => {
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
## [Get active metrics list](https://docs.datadoghq.com/api/latest/metrics/#get-active-metrics-list)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/metrics/#get-active-metrics-list-v1)


GET https://api.ap1.datadoghq.com/api/v1/metricshttps://api.ap2.datadoghq.com/api/v1/metricshttps://api.datadoghq.eu/api/v1/metricshttps://api.ddog-gov.com/api/v1/metricshttps://api.datadoghq.com/api/v1/metricshttps://api.us3.datadoghq.com/api/v1/metricshttps://api.us5.datadoghq.com/api/v1/metrics
### Overview
Get the list of actively reporting metrics from a given time until now. This endpoint requires the `metrics_read` permission.
OAuth apps require the `metrics_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
from [_required_]
integer
Seconds since the Unix epoch.
host
string
Hostname for filtering the list of metrics returned. If set, metrics retrieved are those with the corresponding hostname tag.
tag_filter
string
Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions. Cannot be combined with other filters.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetrics-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetrics-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetrics-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetrics-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Object listing all metric names stored by Datadog since a given time.
Expand All
Field
Type
Description
from
string
Time when the metrics were active, seconds since the Unix epoch.
metrics
[string]
List of metric names.
```
{
  "from": "string",
  "metrics": []
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python-legacy)


#####  Get active metrics list
Copy
```
                  # Required query arguments  
export from="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/metrics?from=${from}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get active metrics list
```
"""
Get active metrics list returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_active_metrics(
        _from=9223372036854775807,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get active metrics list
```
# Get active metrics list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new
p api_instance.list_active_metrics(9223372036854775807)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get active metrics list
```
// Get active metrics list returns "OK" response

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
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.ListActiveMetrics(ctx, 9223372036854775807, *datadogV1.NewListActiveMetricsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListActiveMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListActiveMetrics`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get active metrics list
```
// Get active metrics list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.model.MetricsListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricsListResponse result = apiInstance.listActiveMetrics(9223372036854775807L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listActiveMetrics");
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

#####  Get active metrics list
```
from datadog import initialize, api
import time

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Taking the last 24hours
from_time = int(time.time()) - 60 * 60 * 24 * 1

result = api.Metric.list(from_time)

print(result)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get active metrics list
```
// Get active metrics list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::ListActiveMetricsOptionalParams;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .list_active_metrics(
            9223372036854775807,
            ListActiveMetricsOptionalParams::default(),
        )
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get active metrics list
```
/**
 * Get active metrics list returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiListActiveMetricsRequest = {
  from: 9223372036854775807,
};

apiInstance
  .listActiveMetrics(params)
  .then((data: v1.MetricsListResponse) => {
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
## [Query timeseries data across multiple products](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products-v2)


POST https://api.ap1.datadoghq.com/api/v2/query/timeserieshttps://api.ap2.datadoghq.com/api/v2/query/timeserieshttps://api.datadoghq.eu/api/v2/query/timeserieshttps://api.ddog-gov.com/api/v2/query/timeserieshttps://api.datadoghq.com/api/v2/query/timeserieshttps://api.us3.datadoghq.com/api/v2/query/timeserieshttps://api.us5.datadoghq.com/api/v2/query/timeseries
### Overview
Query timeseries data across various data sources and process the data by applying formulas and functions. This endpoint requires the `timeseries_query` permission.
OAuth apps require the `timeseries_query` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
data [_required_]
object
A single timeseries query to be executed.
attributes [_required_]
object
The object describing a timeseries formula request.
formulas
[object]
List of formulas to be calculated and returned as responses.
formula [_required_]
string
Formula string, referencing one or more queries with their name property.
limit
object
Message for specifying limits to the number of values returned by a query. This limit is only for scalar queries and has no effect on timeseries queries.
count
int32
The number of results to which to limit.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
from [_required_]
int64
Start date (inclusive) of the query in milliseconds since the Unix epoch.
interval
int64
A time interval in milliseconds. May be overridden by a larger interval if the query would result in too many points for the specified timeframe. Defaults to a reasonable interval for the given timeframe.
queries [_required_]
[ <oneOf>]
List of queries to be run and used as inputs to the formulas.
Option 1
object
An individual timeseries metrics query.
data_source [_required_]
enum
A data source that is powered by the Metrics platform. Allowed enum values: `metrics,cloud_cost`
default: `metrics`
name
string
The variable name for use in formulas.
query [_required_]
string
A classic metrics query string.
Option 2
object
An individual timeseries events query.
compute [_required_]
object
The instructions for what to compute for this query.
aggregation [_required_]
enum
The type of aggregation that can be performed on events-based queries. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
default: `count`
interval
int64
Interval for compute in milliseconds.
metric
string
The "measure" attribute on which to perform the computation.
data_source [_required_]
enum
A data source that is powered by the Events Platform. Allowed enum values: `logs,rum,dora`
default: `logs`
group_by
[object]
The list of facets on which to split results.
facet [_required_]
string
The facet by which to split groups.
limit
int32
The maximum buckets to return for this group by. Note: at most 10000 buckets are allowed. If grouping by multiple facets, the product of limits must not exceed 10000.
default: `10`
sort
object
The dimension by which to sort a query's results.
aggregation [_required_]
enum
The type of aggregation that can be performed on events-based queries. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
default: `count`
metric
string
The metric's calculated value which should be used to define the sort order of a query's results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
type
enum
The type of sort to use on the calculated value. Allowed enum values: `alphabetical,measure`
indexes
[string]
The indexes in which to search.
name
string
The variable name for use in formulas.
search
object
Configuration of the search/filter for an events query.
query
string
The search/filter string for an events query.
to [_required_]
int64
End date (exclusive) of the query in milliseconds since the Unix epoch.
type [_required_]
enum
The type of the resource. The value should always be timeseries_request. Allowed enum values: `timeseries_request`
default: `timeseries_request`
```
{
  "data": {
    "attributes": {
      "formulas": [
        {
          "formula": "a",
          "limit": {
            "count": 10,
            "order": "desc"
          }
        }
      ],
      "from": 1636625471000,
      "interval": 5000,
      "queries": [
        {
          "data_source": "metrics",
          "query": "avg:datadog.estimated_usage.metrics.custom{*}",
          "name": "a"
        }
      ],
      "to": 1636629071000
    },
    "type": "timeseries_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#QueryTimeseriesData-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#QueryTimeseriesData-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/metrics/#QueryTimeseriesData-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#QueryTimeseriesData-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#QueryTimeseriesData-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


A message containing one response to a timeseries query made with timeseries formula query request.
Field
Type
Description
data
object
A message containing the response to a timeseries query.
attributes
object
The object describing a timeseries response.
series
[object]
Array of response series. The index here corresponds to the index in the `formulas` or `queries` array from the request.
group_tags
[string]
List of tags that apply to a single response value.
query_index
int32
The index of the query in the "formulas" array (or "queries" array if no "formulas" was specified).
unit
[object]
Detailed information about the unit. The first element describes the "primary unit" (for example, `bytes` in `bytes per second`). The second element describes the "per unit" (for example, `second` in `bytes per second`). If the second element is not present, the API returns null.
family
string
Unit family, allows for conversion between units of the same family, for scaling.
name
string
Unit name
plural
string
Plural form of the unit name.
scale_factor
double
Factor for scaling between units of the same family.
short_name
string
Abbreviation of the unit.
times
[integer]
Array of times, 1-1 match with individual values arrays.
values
[array]
Array of value-arrays. The index here corresponds to the index in the `formulas` or `queries` array from the request.
type
enum
The type of the resource. The value should always be timeseries_response. Allowed enum values: `timeseries_response`
default: `timeseries_response`
errors
string
The error generated by the request.
```
{
  "data": {
    "attributes": {
      "series": [
        {
          "group_tags": [
            "env:production"
          ],
          "query_index": 0,
          "unit": [
            {
              "family": "time",
              "name": "minute",
              "plural": "minutes",
              "scale_factor": 60,
              "short_name": "min"
            }
          ]
        }
      ],
      "times": [],
      "values": [
        1575317847,
        0.5
      ]
    },
    "type": "timeseries_response"
  },
  "errors": "string"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Timeseries cross product query returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/query/timeseries" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "formulas": [
        {
          "formula": "a",
          "limit": {
            "count": 10,
            "order": "desc"
          }
        }
      ],
      "from": 1636625471000,
      "interval": 5000,
      "queries": [
        {
          "data_source": "metrics",
          "query": "avg:datadog.estimated_usage.metrics.custom{*}",
          "name": "a"
        }
      ],
      "to": 1636629071000
    },
    "type": "timeseries_request"
  }
}
EOF  

                        
```

#####  Timeseries cross product query returns "OK" response
```
// Timeseries cross product query returns "OK" response

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
	body := datadogV2.TimeseriesFormulaQueryRequest{
		Data: datadogV2.TimeseriesFormulaRequest{
			Attributes: datadogV2.TimeseriesFormulaRequestAttributes{
				Formulas: []datadogV2.QueryFormula{
					{
						Formula: "a",
						Limit: &datadogV2.FormulaLimit{
							Count: datadog.PtrInt32(10),
							Order: datadogV2.QUERYSORTORDER_DESC.Ptr(),
						},
					},
				},
				From:     1636625471000,
				Interval: datadog.PtrInt64(5000),
				Queries: []datadogV2.TimeseriesQuery{
					datadogV2.TimeseriesQuery{
						MetricsTimeseriesQuery: &datadogV2.MetricsTimeseriesQuery{
							DataSource: datadogV2.METRICSDATASOURCE_METRICS,
							Query:      "avg:datadog.estimated_usage.metrics.custom{*}",
							Name:       datadog.PtrString("a"),
						}},
				},
				To: 1636629071000,
			},
			Type: datadogV2.TIMESERIESFORMULAREQUESTTYPE_TIMESERIES_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.QueryTimeseriesData(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.QueryTimeseriesData`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.QueryTimeseriesData`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Timeseries cross product query returns "OK" response
```
// Timeseries cross product query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.FormulaLimit;
import com.datadog.api.client.v2.model.MetricsDataSource;
import com.datadog.api.client.v2.model.MetricsTimeseriesQuery;
import com.datadog.api.client.v2.model.QueryFormula;
import com.datadog.api.client.v2.model.QuerySortOrder;
import com.datadog.api.client.v2.model.TimeseriesFormulaQueryRequest;
import com.datadog.api.client.v2.model.TimeseriesFormulaQueryResponse;
import com.datadog.api.client.v2.model.TimeseriesFormulaRequest;
import com.datadog.api.client.v2.model.TimeseriesFormulaRequestAttributes;
import com.datadog.api.client.v2.model.TimeseriesFormulaRequestType;
import com.datadog.api.client.v2.model.TimeseriesQuery;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    TimeseriesFormulaQueryRequest body =
        new TimeseriesFormulaQueryRequest()
            .data(
                new TimeseriesFormulaRequest()
                    .attributes(
                        new TimeseriesFormulaRequestAttributes()
                            .formulas(
                                Collections.singletonList(
                                    new QueryFormula()
                                        .formula("a")
                                        .limit(
                                            new FormulaLimit()
                                                .count(10)
                                                .order(QuerySortOrder.DESC))))
                            .from(1636625471000L)
                            .interval(5000L)
                            .queries(
                                Collections.singletonList(
                                    new TimeseriesQuery(
                                        new MetricsTimeseriesQuery()
                                            .dataSource(MetricsDataSource.METRICS)
                                            .query("avg:datadog.estimated_usage.metrics.custom{*}")
                                            .name("a"))))
                            .to(1636629071000L))
                    .type(TimeseriesFormulaRequestType.TIMESERIES_REQUEST));

    try {
      TimeseriesFormulaQueryResponse result = apiInstance.queryTimeseriesData(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#queryTimeseriesData");
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

#####  Timeseries cross product query returns "OK" response
```
"""
Timeseries cross product query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.formula_limit import FormulaLimit
from datadog_api_client.v2.model.metrics_data_source import MetricsDataSource
from datadog_api_client.v2.model.metrics_timeseries_query import MetricsTimeseriesQuery
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.timeseries_formula_query_request import TimeseriesFormulaQueryRequest
from datadog_api_client.v2.model.timeseries_formula_request import TimeseriesFormulaRequest
from datadog_api_client.v2.model.timeseries_formula_request_attributes import TimeseriesFormulaRequestAttributes
from datadog_api_client.v2.model.timeseries_formula_request_queries import TimeseriesFormulaRequestQueries
from datadog_api_client.v2.model.timeseries_formula_request_type import TimeseriesFormulaRequestType

body = TimeseriesFormulaQueryRequest(
    data=TimeseriesFormulaRequest(
        attributes=TimeseriesFormulaRequestAttributes(
            formulas=[
                QueryFormula(
                    formula="a",
                    limit=FormulaLimit(
                        count=10,
                        order=QuerySortOrder.DESC,
                    ),
                ),
            ],
            _from=1636625471000,
            interval=5000,
            queries=TimeseriesFormulaRequestQueries(
                [
                    MetricsTimeseriesQuery(
                        data_source=MetricsDataSource.METRICS,
                        query="avg:datadog.estimated_usage.metrics.custom{*}",
                        name="a",
                    ),
                ]
            ),
            to=1636629071000,
        ),
        type=TimeseriesFormulaRequestType.TIMESERIES_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_timeseries_data(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Timeseries cross product query returns "OK" response
```
# Timeseries cross product query returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

body = DatadogAPIClient::V2::TimeseriesFormulaQueryRequest.new({
  data: DatadogAPIClient::V2::TimeseriesFormulaRequest.new({
    attributes: DatadogAPIClient::V2::TimeseriesFormulaRequestAttributes.new({
      formulas: [
        DatadogAPIClient::V2::QueryFormula.new({
          formula: "a",
          limit: DatadogAPIClient::V2::FormulaLimit.new({
            count: 10,
            order: DatadogAPIClient::V2::QuerySortOrder::DESC,
          }),
        }),
      ],
      from: 1636625471000,
      interval: 5000,
      queries: [
        DatadogAPIClient::V2::MetricsTimeseriesQuery.new({
          data_source: DatadogAPIClient::V2::MetricsDataSource::METRICS,
          query: "avg:datadog.estimated_usage.metrics.custom{*}",
          name: "a",
        }),
      ],
      to: 1636629071000,
    }),
    type: DatadogAPIClient::V2::TimeseriesFormulaRequestType::TIMESERIES_REQUEST,
  }),
})
p api_instance.query_timeseries_data(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Timeseries cross product query returns "OK" response
```
// Timeseries cross product query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::model::FormulaLimit;
use datadog_api_client::datadogV2::model::MetricsDataSource;
use datadog_api_client::datadogV2::model::MetricsTimeseriesQuery;
use datadog_api_client::datadogV2::model::QueryFormula;
use datadog_api_client::datadogV2::model::QuerySortOrder;
use datadog_api_client::datadogV2::model::TimeseriesFormulaQueryRequest;
use datadog_api_client::datadogV2::model::TimeseriesFormulaRequest;
use datadog_api_client::datadogV2::model::TimeseriesFormulaRequestAttributes;
use datadog_api_client::datadogV2::model::TimeseriesFormulaRequestType;
use datadog_api_client::datadogV2::model::TimeseriesQuery;

#[tokio::main]
async fn main() {
    let body = TimeseriesFormulaQueryRequest::new(TimeseriesFormulaRequest::new(
        TimeseriesFormulaRequestAttributes::new(
            1636625471000,
            vec![TimeseriesQuery::MetricsTimeseriesQuery(Box::new(
                MetricsTimeseriesQuery::new(
                    MetricsDataSource::METRICS,
                    "avg:datadog.estimated_usage.metrics.custom{*}".to_string(),
                )
                .name("a".to_string()),
            ))],
            1636629071000,
        )
        .formulas(vec![QueryFormula::new("a".to_string())
            .limit(FormulaLimit::new().count(10).order(QuerySortOrder::DESC))])
        .interval(5000),
        TimeseriesFormulaRequestType::TIMESERIES_REQUEST,
    ));
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api.query_timeseries_data(body).await;
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

#####  Timeseries cross product query returns "OK" response
```
/**
 * Timeseries cross product query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiQueryTimeseriesDataRequest = {
  body: {
    data: {
      attributes: {
        formulas: [
          {
            formula: "a",
            limit: {
              count: 10,
              order: "desc",
            },
          },
        ],
        from: 1636625471000,
        interval: 5000,
        queries: [
          {
            dataSource: "metrics",
            query: "avg:datadog.estimated_usage.metrics.custom{*}",
            name: "a",
          },
        ],
        to: 1636629071000,
      },
      type: "timeseries_request",
    },
  },
};

apiInstance
  .queryTimeseriesData(params)
  .then((data: v2.TimeseriesFormulaQueryResponse) => {
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
## [Submit distribution points](https://docs.datadoghq.com/api/latest/metrics/#submit-distribution-points)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/metrics/#submit-distribution-points-v1)


POST https://api.ap1.datadoghq.com/api/v1/distribution_pointshttps://api.ap2.datadoghq.com/api/v1/distribution_pointshttps://api.datadoghq.eu/api/v1/distribution_pointshttps://api.ddog-gov.com/api/v1/distribution_pointshttps://api.datadoghq.com/api/v1/distribution_pointshttps://api.us3.datadoghq.com/api/v1/distribution_pointshttps://api.us5.datadoghq.com/api/v1/distribution_points
### Overview
The distribution points end-point allows you to post distribution data that can be graphed on Datadog’s dashboards.
### Arguments
#### Header Parameters
Name
Type
Description
Content-Encoding
string
HTTP header used to compress the media-type.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
series [_required_]
[object]
A list of distribution points series to submit to Datadog.
host
string
The name of the host that produced the distribution point metric.
metric [_required_]
string
The name of the distribution points metric.
points [_required_]
[array]
Points relating to the distribution point metric. All points must be tuples with timestamp and a list of values (cannot be a string). Timestamps should be in POSIX time in seconds.
tags
[string]
A list of tags associated with the distribution point metric.
type
enum
The type of the distribution point. Allowed enum values: `distribution`
default: `distribution`
#####  Submit deflate distribution points returns "Payload accepted" response
```
{
  "series": [
    {
      "metric": "system.load.1.dist",
      "points": [
        [
          1636629071,
          [
            1.0,
            2.0
          ]
        ]
      ]
    }
  ]
}
```

Copy
#####  Submit distribution points returns "Payload accepted" response
```
{
  "series": [
    {
      "metric": "system.load.1.dist",
      "points": [
        [
          1636629071,
          [
            1.0,
            2.0
          ]
        ]
      ]
    }
  ]
}
```

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/metrics/#SubmitDistributionPoints-202-v1)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#SubmitDistributionPoints-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#SubmitDistributionPoints-403-v1)
  * [408](https://docs.datadoghq.com/api/latest/metrics/#SubmitDistributionPoints-408-v1)
  * [413](https://docs.datadoghq.com/api/latest/metrics/#SubmitDistributionPoints-413-v1)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#SubmitDistributionPoints-429-v1)


Payload accepted
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


The payload accepted for intake.
Expand All
Field
Type
Description
status
string
The status of the intake payload.
```
{
  "status": "ok"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Request timeout
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Payload too large
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Submit deflate distribution points returns "Payload accepted" response
Copy
```
                          ## Dynamic Points
# Post time-series data that can be graphed on Datadog’s dashboards.
  
See one of the other client libraries for an example of sending deflate-compressed data.  
  

                        
```

#####  Submit distribution points returns "Payload accepted" response
Copy
```
                          ## Dynamic Points
# Post time-series data that can be graphed on Datadog’s dashboards.
  
# Template variables  
export NOW="$(date +%s)"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/distribution_points" \
-H "Accept: application/json" \
-H "Content-Type: text/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "series": [
    {
      "metric": "system.load.1.dist",
      "points": [[${NOW}, [1234.5]]]
    }
  ]
}

EOF  

                        
```

#####  Submit deflate distribution points returns "Payload accepted" response 
```
// Submit deflate distribution points returns "Payload accepted" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.DistributionPointsPayload{
		Series: []datadogV1.DistributionPointsSeries{
			{
				Metric: "system.load.1.dist",
				Points: [][]datadogV1.DistributionPointItem{
					{
						{DistributionPointTimestamp: datadog.PtrFloat64(float64(time.Now().Unix()))},
						{DistributionPointData: &[]float64{
							1.0,
							2.0,
						}},
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.SubmitDistributionPoints(ctx, body, *datadogV1.NewSubmitDistributionPointsOptionalParameters().WithContentEncoding(datadogV1.DISTRIBUTIONPOINTSCONTENTENCODING_DEFLATE))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.SubmitDistributionPoints`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.SubmitDistributionPoints`:\n%s\n", responseContent)
}

```

Copy
#####  Submit distribution points returns "Payload accepted" response 
```
// Submit distribution points returns "Payload accepted" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.DistributionPointsPayload{
		Series: []datadogV1.DistributionPointsSeries{
			{
				Metric: "system.load.1.dist",
				Points: [][]datadogV1.DistributionPointItem{
					{
						{DistributionPointTimestamp: datadog.PtrFloat64(float64(time.Now().Unix()))},
						{DistributionPointData: &[]float64{
							1.0,
							2.0,
						}},
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.SubmitDistributionPoints(ctx, body, *datadogV1.NewSubmitDistributionPointsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.SubmitDistributionPoints`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.SubmitDistributionPoints`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"


```

#####  Submit deflate distribution points returns "Payload accepted" response 
```
// Submit deflate distribution points returns "Payload accepted" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.api.MetricsApi.SubmitDistributionPointsOptionalParameters;
import com.datadog.api.client.v1.model.DistributionPointItem;
import com.datadog.api.client.v1.model.DistributionPointsContentEncoding;
import com.datadog.api.client.v1.model.DistributionPointsPayload;
import com.datadog.api.client.v1.model.DistributionPointsSeries;
import com.datadog.api.client.v1.model.IntakePayloadAccepted;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    DistributionPointsPayload body =
        new DistributionPointsPayload()
            .series(
                Collections.singletonList(
                    new DistributionPointsSeries()
                        .metric("system.load.1.dist")
                        .points(
                            Collections.singletonList(
                                Arrays.asList(
                                    new DistributionPointItem(
                                        Long.valueOf(
                                                OffsetDateTime.now().toInstant().getEpochSecond())
                                            .doubleValue()),
                                    new DistributionPointItem(Arrays.asList(1.0, 2.0)))))));

    try {
      IntakePayloadAccepted result =
          apiInstance.submitDistributionPoints(
              body,
              new SubmitDistributionPointsOptionalParameters()
                  .contentEncoding(DistributionPointsContentEncoding.DEFLATE));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#submitDistributionPoints");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Submit distribution points returns "Payload accepted" response 
```
// Submit distribution points returns "Payload accepted" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.model.DistributionPointItem;
import com.datadog.api.client.v1.model.DistributionPointsPayload;
import com.datadog.api.client.v1.model.DistributionPointsSeries;
import com.datadog.api.client.v1.model.IntakePayloadAccepted;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    DistributionPointsPayload body =
        new DistributionPointsPayload()
            .series(
                Collections.singletonList(
                    new DistributionPointsSeries()
                        .metric("system.load.1.dist")
                        .points(
                            Collections.singletonList(
                                Arrays.asList(
                                    new DistributionPointItem(
                                        Long.valueOf(
                                                OffsetDateTime.now().toInstant().getEpochSecond())
                                            .doubleValue()),
                                    new DistributionPointItem(Arrays.asList(1.0, 2.0)))))));

    try {
      IntakePayloadAccepted result = apiInstance.submitDistributionPoints(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#submitDistributionPoints");
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

#####  Submit deflate distribution points returns "Payload accepted" response 
```
"""
Submit deflate distribution points returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.distribution_point import DistributionPoint
from datadog_api_client.v1.model.distribution_points_content_encoding import DistributionPointsContentEncoding
from datadog_api_client.v1.model.distribution_points_payload import DistributionPointsPayload
from datadog_api_client.v1.model.distribution_points_series import DistributionPointsSeries

body = DistributionPointsPayload(
    series=[
        DistributionPointsSeries(
            metric="system.load.1.dist",
            points=[
                DistributionPoint(
                    [
                        datetime.now().timestamp(),
                        [1.0, 2.0],
                    ]
                ),
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_distribution_points(
        content_encoding=DistributionPointsContentEncoding.DEFLATE, body=body
    )

    print(response)

```

Copy
#####  Submit distribution points returns "Payload accepted" response 
```
"""
Submit distribution points returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.distribution_point import DistributionPoint
from datadog_api_client.v1.model.distribution_points_payload import DistributionPointsPayload
from datadog_api_client.v1.model.distribution_points_series import DistributionPointsSeries

body = DistributionPointsPayload(
    series=[
        DistributionPointsSeries(
            metric="system.load.1.dist",
            points=[
                DistributionPoint(
                    [
                        datetime.now().timestamp(),
                        [1.0, 2.0],
                    ]
                ),
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_distribution_points(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"


```

#####  Submit deflate distribution points returns "Payload accepted" response 
```
# Submit deflate distribution points returns "Payload accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new

body = DatadogAPIClient::V1::DistributionPointsPayload.new({
  series: [
    DatadogAPIClient::V1::DistributionPointsSeries.new({
      metric: "system.load.1.dist",
      points: [
        [
          Time.now,
          [
            1.0,
            2.0,
          ],
        ],
      ],
    }),
  ],
})
opts = {
  content_encoding: DistributionPointsContentEncoding::DEFLATE,
}
p api_instance.submit_distribution_points(body, opts)

```

Copy
#####  Submit distribution points returns "Payload accepted" response 
```
# Submit distribution points returns "Payload accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new

body = DatadogAPIClient::V1::DistributionPointsPayload.new({
  series: [
    DatadogAPIClient::V1::DistributionPointsSeries.new({
      metric: "system.load.1.dist",
      points: [
        [
          Time.now,
          [
            1.0,
            2.0,
          ],
        ],
      ],
    }),
  ],
})
p api_instance.submit_distribution_points(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Submit deflate distribution points returns "Payload accepted" response 
```
// Submit deflate distribution points returns "Payload accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;
use datadog_api_client::datadogV1::api_metrics::SubmitDistributionPointsOptionalParams;
use datadog_api_client::datadogV1::model::DistributionPointItem;
use datadog_api_client::datadogV1::model::DistributionPointsContentEncoding;
use datadog_api_client::datadogV1::model::DistributionPointsPayload;
use datadog_api_client::datadogV1::model::DistributionPointsSeries;

#[tokio::main]
async fn main() {
    let body = DistributionPointsPayload::new(vec![DistributionPointsSeries::new(
        "system.load.1.dist".to_string(),
        vec![vec![
            DistributionPointItem::DistributionPointTimestamp(1636629071.0 as f64),
            DistributionPointItem::DistributionPointData(vec![1.0, 2.0]),
        ]],
    )]);
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .submit_distribution_points(
            body,
            SubmitDistributionPointsOptionalParams::default()
                .content_encoding(DistributionPointsContentEncoding::DEFLATE),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Submit distribution points returns "Payload accepted" response 
```
// Submit distribution points returns "Payload accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;
use datadog_api_client::datadogV1::api_metrics::SubmitDistributionPointsOptionalParams;
use datadog_api_client::datadogV1::model::DistributionPointItem;
use datadog_api_client::datadogV1::model::DistributionPointsPayload;
use datadog_api_client::datadogV1::model::DistributionPointsSeries;

#[tokio::main]
async fn main() {
    let body = DistributionPointsPayload::new(vec![DistributionPointsSeries::new(
        "system.load.1.dist".to_string(),
        vec![vec![
            DistributionPointItem::DistributionPointTimestamp(1636629071.0 as f64),
            DistributionPointItem::DistributionPointData(vec![1.0, 2.0]),
        ]],
    )]);
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .submit_distribution_points(body, SubmitDistributionPointsOptionalParams::default())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run


```

#####  Submit deflate distribution points returns "Payload accepted" response 
```
/**
 * Submit deflate distribution points returns "Payload accepted" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiSubmitDistributionPointsRequest = {
  body: {
    series: [
      {
        metric: "system.load.1.dist",
        points: [[Math.round(new Date().getTime() / 1000), [1.0, 2.0]]],
      },
    ],
  },
  contentEncoding: "deflate",
};

apiInstance
  .submitDistributionPoints(params)
  .then((data: v1.IntakePayloadAccepted) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Submit distribution points returns "Payload accepted" response 
```
/**
 * Submit distribution points returns "Payload accepted" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiSubmitDistributionPointsRequest = {
  body: {
    series: [
      {
        metric: "system.load.1.dist",
        points: [[Math.round(new Date().getTime() / 1000), [1.0, 2.0]]],
      },
    ],
  },
};

apiInstance
  .submitDistributionPoints(params)
  .then((data: v1.IntakePayloadAccepted) => {
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
## [Submit metrics](https://docs.datadoghq.com/api/latest/metrics/#submit-metrics)
  * [v1](https://docs.datadoghq.com/api/latest/metrics/#submit-metrics-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#submit-metrics-v2)


POST https://api.ap1.datadoghq.com/api/v1/serieshttps://api.ap2.datadoghq.com/api/v1/serieshttps://api.datadoghq.eu/api/v1/serieshttps://api.ddog-gov.com/api/v1/serieshttps://api.datadoghq.com/api/v1/serieshttps://api.us3.datadoghq.com/api/v1/serieshttps://api.us5.datadoghq.com/api/v1/series
### Overview
The metrics end-point allows you to post time-series data that can be graphed on Datadog’s dashboards. The maximum payload size is 3.2 megabytes (3200000 bytes). Compressed payloads must have a decompressed size of less than 62 megabytes (62914560 bytes).
If you’re submitting metrics directly to the Datadog API without using DogStatsD, expect:
  * 64 bits for the timestamp
  * 64 bits for the value
  * 40 bytes for the metric names
  * 50 bytes for the timeseries
  * The full payload is approximately 100 bytes. However, with the DogStatsD API, compression is applied, which reduces the payload size.


### Arguments
#### Header Parameters
Name
Type
Description
Content-Encoding
string
HTTP header used to compress the media-type.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
series [_required_]
[object]
A list of timeseries to submit to Datadog.
host
string
The name of the host that produced the metric.
interval
int64
If the type of the metric is rate or count, define the corresponding interval in seconds.
metric [_required_]
string
The name of the timeseries.
points [_required_]
[array]
Points relating to a metric. All points must be tuples with timestamp and a scalar value (cannot be a string). Timestamps should be in POSIX time in seconds, and cannot be more than ten minutes in the future or more than one hour in the past.
tags
[string]
A list of tags associated with the metric.
type
string
The type of the metric. Valid types are "",`count`, `gauge`, and `rate`.
#####  Submit deflate metrics returns "Payload accepted" response
```
{
  "series": [
    {
      "metric": "system.load.1",
      "type": "gauge",
      "points": [
        [
          1636629071,
          1.1
        ]
      ],
      "tags": [
        "test:ExampleMetric"
      ]
    }
  ]
}
```

Copy
#####  Submit metrics returns "Payload accepted" response
```
{
  "series": [
    {
      "metric": "system.load.1",
      "type": "gauge",
      "points": [
        [
          1636629071,
          1.1
        ]
      ],
      "tags": [
        "test:ExampleMetric"
      ]
    }
  ]
}
```

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-202-v1)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-403-v1)
  * [408](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-408-v1)
  * [413](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-413-v1)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-429-v1)


Payload accepted
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


The payload accepted for intake.
Expand All
Field
Type
Description
status
string
The status of the intake payload.
```
{
  "status": "ok"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Request timeout
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Payload too large
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby-legacy)


#####  Submit deflate metrics returns "Payload accepted" response
Copy
```
                          ## Dynamic Points
# Post time-series data that can be graphed on Datadog’s dashboards.
  
See one of the other client libraries for an example of sending deflate-compressed data.  
  

                        
```

#####  Submit metrics returns "Payload accepted" response
Copy
```
                          ## Dynamic Points
# Post time-series data that can be graphed on Datadog’s dashboards.
  
# Template variables  
export NOW="$(date +%s)"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/series" \
-H "Accept: application/json" \
-H "Content-Type: text/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "series": [
    {
      "metric": "system.load.1",
      "points": [[${NOW}, 1234.5]]
    }
  ]
}

EOF  

                        
```

#####  Submit deflate metrics returns "Payload accepted" response 
```
// Submit deflate metrics returns "Payload accepted" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.MetricsPayload{
		Series: []datadogV1.Series{
			{
				Metric: "system.load.1",
				Type:   datadog.PtrString("gauge"),
				Points: [][]*float64{
					{
						datadog.PtrFloat64(float64(time.Now().Unix())),
						datadog.PtrFloat64(1.1),
					},
				},
				Tags: []string{
					"test:ExampleMetric",
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.SubmitMetrics(ctx, body, *datadogV1.NewSubmitMetricsOptionalParameters().WithContentEncoding(datadogV1.METRICCONTENTENCODING_DEFLATE))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.SubmitMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.SubmitMetrics`:\n%s\n", responseContent)
}

```

Copy
#####  Submit metrics returns "Payload accepted" response 
```
// Submit metrics returns "Payload accepted" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.MetricsPayload{
		Series: []datadogV1.Series{
			{
				Metric: "system.load.1",
				Type:   datadog.PtrString("gauge"),
				Points: [][]*float64{
					{
						datadog.PtrFloat64(float64(time.Now().Unix())),
						datadog.PtrFloat64(1.1),
					},
				},
				Tags: []string{
					"test:ExampleMetric",
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.SubmitMetrics(ctx, body, *datadogV1.NewSubmitMetricsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.SubmitMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.SubmitMetrics`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"


```

#####  Submit deflate metrics returns "Payload accepted" response 
```
// Submit deflate metrics returns "Payload accepted" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.api.MetricsApi.SubmitMetricsOptionalParameters;
import com.datadog.api.client.v1.model.IntakePayloadAccepted;
import com.datadog.api.client.v1.model.MetricContentEncoding;
import com.datadog.api.client.v1.model.MetricsPayload;
import com.datadog.api.client.v1.model.Series;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    MetricsPayload body =
        new MetricsPayload()
            .series(
                Collections.singletonList(
                    new Series()
                        .metric("system.load.1")
                        .type("gauge")
                        .points(
                            Collections.singletonList(
                                Arrays.asList(
                                    Long.valueOf(OffsetDateTime.now().toInstant().getEpochSecond())
                                        .doubleValue(),
                                    1.1)))
                        .tags(Collections.singletonList("test:ExampleMetric"))));

    try {
      IntakePayloadAccepted result =
          apiInstance.submitMetrics(
              body,
              new SubmitMetricsOptionalParameters().contentEncoding(MetricContentEncoding.DEFLATE));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#submitMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Submit metrics returns "Payload accepted" response 
```
// Submit metrics returns "Payload accepted" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.model.IntakePayloadAccepted;
import com.datadog.api.client.v1.model.MetricsPayload;
import com.datadog.api.client.v1.model.Series;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    MetricsPayload body =
        new MetricsPayload()
            .series(
                Collections.singletonList(
                    new Series()
                        .metric("system.load.1")
                        .type("gauge")
                        .points(
                            Collections.singletonList(
                                Arrays.asList(
                                    Long.valueOf(OffsetDateTime.now().toInstant().getEpochSecond())
                                        .doubleValue(),
                                    1.1)))
                        .tags(Collections.singletonList("test:ExampleMetric"))));

    try {
      IntakePayloadAccepted result = apiInstance.submitMetrics(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#submitMetrics");
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

#####  Submit metrics returns "Payload accepted" response
```
from datadog import initialize, api
import time

options = {
    'api_key': '<DATADOG_API_KEY>'
    ## EU costumers need to define 'api_host' as below
    #'api_host': 'https://api.datadoghq.eu/'
}

initialize(**options)

now = time.time()
future_10s = now + 10

# Submit a single point with a timestamp of `now`
api.Metric.send(metric='page.views', points=1000)

# Submit a point with a timestamp (must be current)
api.Metric.send(metric='my.pair', points=(now, 15))

# Submit multiple points.
api.Metric.send(
    metric='my.series',
    points=[
        (now, 15),
        (future_10s, 16)
    ]
)

# Submit a point with a host and tags.
api.Metric.send(
    metric='my.series',
    points=100,
    host="myhost.example.com",
    tags=["version:1"]
)

# Submit multiple metrics
api.Metric.send([{
    'metric': 'my.series',
    'points': 15
}, {
    'metric': 'my1.series',
    'points': 16
}])

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python "example.py"


```

#####  Submit deflate metrics returns "Payload accepted" response 
```
"""
Submit deflate metrics returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.metric_content_encoding import MetricContentEncoding
from datadog_api_client.v1.model.metrics_payload import MetricsPayload
from datadog_api_client.v1.model.point import Point
from datadog_api_client.v1.model.series import Series

body = MetricsPayload(
    series=[
        Series(
            metric="system.load.1",
            type="gauge",
            points=[
                Point(
                    [
                        datetime.now().timestamp(),
                        1.1,
                    ]
                ),
            ],
            tags=[
                "test:ExampleMetric",
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_metrics(content_encoding=MetricContentEncoding.DEFLATE, body=body)

    print(response)

```

Copy
#####  Submit metrics returns "Payload accepted" response 
```
"""
Submit metrics returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.metrics_payload import MetricsPayload
from datadog_api_client.v1.model.point import Point
from datadog_api_client.v1.model.series import Series

body = MetricsPayload(
    series=[
        Series(
            metric="system.load.1",
            type="gauge",
            points=[
                Point(
                    [
                        datetime.now().timestamp(),
                        1.1,
                    ]
                ),
            ],
            tags=[
                "test:ExampleMetric",
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_metrics(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"


```

#####  Submit metrics returns "Payload accepted" response
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'

dog = Dogapi::Client.new(api_key)

# Submit one metric value.
dog.emit_point('some.metric.name', 50.0, :host => "my_host.example.com")

# Submit multiple metric values
points = [
    [Time.now, 0],
    [Time.now + 10, 10.0],
    [Time.now + 20, 20.0]
]
dog.emit_points('some.metric.name', points, :tags => ["version:1"])

# Emit differents metrics in a single request to be more efficient
dog.batch_metrics do
  dog.emit_point('test.api.test_metric',10)
  dog.emit_point('test.api.this_other_metric', 1)
end

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Submit deflate metrics returns "Payload accepted" response 
```
# Submit deflate metrics returns "Payload accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new

body = DatadogAPIClient::V1::MetricsPayload.new({
  series: [
    DatadogAPIClient::V1::Series.new({
      metric: "system.load.1",
      type: "gauge",
      points: [
        [
          Time.now.to_f,
          1.1,
        ],
      ],
      tags: [
        "test:ExampleMetric",
      ],
    }),
  ],
})
opts = {
  content_encoding: MetricContentEncoding::DEFLATE,
}
p api_instance.submit_metrics(body, opts)

```

Copy
#####  Submit metrics returns "Payload accepted" response 
```
# Submit metrics returns "Payload accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new

body = DatadogAPIClient::V1::MetricsPayload.new({
  series: [
    DatadogAPIClient::V1::Series.new({
      metric: "system.load.1",
      type: "gauge",
      points: [
        [
          Time.now.to_f,
          1.1,
        ],
      ],
      tags: [
        "test:ExampleMetric",
      ],
    }),
  ],
})
p api_instance.submit_metrics(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Submit deflate metrics returns "Payload accepted" response 
```
// Submit deflate metrics returns "Payload accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;
use datadog_api_client::datadogV1::api_metrics::SubmitMetricsOptionalParams;
use datadog_api_client::datadogV1::model::MetricContentEncoding;
use datadog_api_client::datadogV1::model::MetricsPayload;
use datadog_api_client::datadogV1::model::Series;

#[tokio::main]
async fn main() {
    let body = MetricsPayload::new(vec![Series::new(
        "system.load.1".to_string(),
        vec![vec![Some(1636629071.0 as f64), Some(1.1 as f64)]],
    )
    .tags(vec!["test:ExampleMetric".to_string()])
    .type_("gauge".to_string())]);
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .submit_metrics(
            body,
            SubmitMetricsOptionalParams::default().content_encoding(MetricContentEncoding::DEFLATE),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Submit metrics returns "Payload accepted" response 
```
// Submit metrics returns "Payload accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;
use datadog_api_client::datadogV1::api_metrics::SubmitMetricsOptionalParams;
use datadog_api_client::datadogV1::model::MetricsPayload;
use datadog_api_client::datadogV1::model::Series;

#[tokio::main]
async fn main() {
    let body = MetricsPayload::new(vec![Series::new(
        "system.load.1".to_string(),
        vec![vec![Some(1636629071.0 as f64), Some(1.1 as f64)]],
    )
    .tags(vec!["test:ExampleMetric".to_string()])
    .type_("gauge".to_string())]);
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .submit_metrics(body, SubmitMetricsOptionalParams::default())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run


```

#####  Submit deflate metrics returns "Payload accepted" response 
```
/**
 * Submit deflate metrics returns "Payload accepted" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiSubmitMetricsRequest = {
  body: {
    series: [
      {
        metric: "system.load.1",
        type: "gauge",
        points: [[Math.round(new Date().getTime() / 1000), 1.1]],
        tags: ["test:ExampleMetric"],
      },
    ],
  },
  contentEncoding: "deflate",
};

apiInstance
  .submitMetrics(params)
  .then((data: v1.IntakePayloadAccepted) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Submit metrics returns "Payload accepted" response 
```
/**
 * Submit metrics returns "Payload accepted" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiSubmitMetricsRequest = {
  body: {
    series: [
      {
        metric: "system.load.1",
        type: "gauge",
        points: [[Math.round(new Date().getTime() / 1000), 1.1]],
        tags: ["test:ExampleMetric"],
      },
    ],
  },
};

apiInstance
  .submitMetrics(params)
  .then((data: v1.IntakePayloadAccepted) => {
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

POST https://api.ap1.datadoghq.com/api/v2/serieshttps://api.ap2.datadoghq.com/api/v2/serieshttps://api.datadoghq.eu/api/v2/serieshttps://api.ddog-gov.com/api/v2/serieshttps://api.datadoghq.com/api/v2/serieshttps://api.us3.datadoghq.com/api/v2/serieshttps://api.us5.datadoghq.com/api/v2/series
### Overview
The metrics end-point allows you to post time-series data that can be graphed on Datadog’s dashboards. The maximum payload size is 500 kilobytes (512000 bytes). Compressed payloads must have a decompressed size of less than 5 megabytes (5242880 bytes).
If you’re submitting metrics directly to the Datadog API without using DogStatsD, expect:
  * 64 bits for the timestamp
  * 64 bits for the value
  * 20 bytes for the metric names
  * 50 bytes for the timeseries
  * The full payload is approximately 100 bytes.


Host name is one of the resources in the Resources field.
### Arguments
#### Header Parameters
Name
Type
Description
Content-Encoding
string
HTTP header used to compress the media-type.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
series [_required_]
[object]
A list of timeseries to submit to Datadog.
interval
int64
If the type of the metric is rate or count, define the corresponding interval in seconds.
metadata
object
Metadata for the metric.
origin
object
Metric origin information.
metric_type
int32
The origin metric type code
product
int32
The origin product code
service
int32
The origin service code
metric [_required_]
string
The name of the timeseries.
points [_required_]
[object]
Points relating to a metric. All points must be objects with timestamp and a scalar value (cannot be a string). Timestamps should be in POSIX time in seconds, and cannot be more than ten minutes in the future or more than one hour in the past.
timestamp
int64
The timestamp should be in seconds and current. Current is defined as not more than 10 minutes in the future or more than 1 hour in the past.
value
double
The numeric value format should be a 64bit float gauge-type value.
resources
[object]
A list of resources to associate with this metric.
name
string
The name of the resource.
type
string
The type of the resource.
source_type_name
string
The source type name.
tags
[string]
A list of tags associated with the metric.
type
enum
The type of metric. The available types are `0` (unspecified), `1` (count), `2` (rate), and `3` (gauge). Allowed enum values: `0,1,2,3`
unit
string
The unit of point value.
#####  Submit metrics returns "Payload accepted" response
```
{
  "series": [
    {
      "metric": "system.load.1",
      "type": 0,
      "points": [
        {
          "timestamp": 1636629071,
          "value": 0.7
        }
      ],
      "resources": [
        {
          "name": "dummyhost",
          "type": "host"
        }
      ]
    }
  ]
}
```

Copy
#####  Submit metrics with compression returns "Payload accepted" response
```
{
  "series": [
    {
      "metric": "system.load.1",
      "type": 0,
      "points": [
        {
          "timestamp": 1636629071,
          "value": 0.7
        }
      ]
    }
  ]
}
```

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-403-v2)
  * [408](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-408-v2)
  * [413](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-413-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#SubmitMetrics-429-v2)


Payload accepted
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


The payload accepted for intake.
Expand All
Field
Type
Description
errors
[string]
A list of errors.
```
{
  "errors": []
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Request timeout
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Payload too large
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Submit metrics returns "Payload accepted" response
Copy
```
                          ## Dynamic Points
# Post time-series data that can be graphed on Datadog’s dashboards.
  
# Template variables  
export NOW="$(date +%s)"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/series" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "series": [
    {
      "metric": "system.load.1",
      "type": 0,
      "points": [
        {
          "timestamp": 1636629071,
          "value": 0.7
        }
      ],
      "resources": [
        {
          "name": "dummyhost",
          "type": "host"
        }
      ]
    }
  ]
}
EOF  

                        
```

#####  Submit metrics with compression returns "Payload accepted" response
Copy
```
                          ## Dynamic Points
# Post time-series data that can be graphed on Datadog’s dashboards.
  
See one of the other client libraries for an example of sending deflate-compressed data.  
  

                        
```

#####  Submit metrics returns "Payload accepted" response 
```
// Submit metrics returns "Payload accepted" response

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
	body := datadogV2.MetricPayload{
		Series: []datadogV2.MetricSeries{
			{
				Metric: "system.load.1",
				Type:   datadogV2.METRICINTAKETYPE_UNSPECIFIED.Ptr(),
				Points: []datadogV2.MetricPoint{
					{
						Timestamp: datadog.PtrInt64(time.Now().Unix()),
						Value:     datadog.PtrFloat64(0.7),
					},
				},
				Resources: []datadogV2.MetricResource{
					{
						Name: datadog.PtrString("dummyhost"),
						Type: datadog.PtrString("host"),
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.SubmitMetrics(ctx, body, *datadogV2.NewSubmitMetricsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.SubmitMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.SubmitMetrics`:\n%s\n", responseContent)
}

```

Copy
#####  Submit metrics with compression returns "Payload accepted" response 
```
// Submit metrics with compression returns "Payload accepted" response

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
	body := datadogV2.MetricPayload{
		Series: []datadogV2.MetricSeries{
			{
				Metric: "system.load.1",
				Type:   datadogV2.METRICINTAKETYPE_UNSPECIFIED.Ptr(),
				Points: []datadogV2.MetricPoint{
					{
						Timestamp: datadog.PtrInt64(time.Now().Unix()),
						Value:     datadog.PtrFloat64(0.7),
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.SubmitMetrics(ctx, body, *datadogV2.NewSubmitMetricsOptionalParameters().WithContentEncoding(datadogV2.METRICCONTENTENCODING_ZSTD1))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.SubmitMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.SubmitMetrics`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"


```

#####  Submit metrics returns "Payload accepted" response 
```
// Submit metrics returns "Payload accepted" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.IntakePayloadAccepted;
import com.datadog.api.client.v2.model.MetricIntakeType;
import com.datadog.api.client.v2.model.MetricPayload;
import com.datadog.api.client.v2.model.MetricPoint;
import com.datadog.api.client.v2.model.MetricResource;
import com.datadog.api.client.v2.model.MetricSeries;
import java.time.OffsetDateTime;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    MetricPayload body =
        new MetricPayload()
            .series(
                Collections.singletonList(
                    new MetricSeries()
                        .metric("system.load.1")
                        .type(MetricIntakeType.UNSPECIFIED)
                        .points(
                            Collections.singletonList(
                                new MetricPoint()
                                    .timestamp(OffsetDateTime.now().toInstant().getEpochSecond())
                                    .value(0.7)))
                        .resources(
                            Collections.singletonList(
                                new MetricResource().name("dummyhost").type("host")))));

    try {
      IntakePayloadAccepted result = apiInstance.submitMetrics(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#submitMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Submit metrics with compression returns "Payload accepted" response 
```
// Submit metrics with compression returns "Payload accepted" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.api.MetricsApi.SubmitMetricsOptionalParameters;
import com.datadog.api.client.v2.model.IntakePayloadAccepted;
import com.datadog.api.client.v2.model.MetricContentEncoding;
import com.datadog.api.client.v2.model.MetricIntakeType;
import com.datadog.api.client.v2.model.MetricPayload;
import com.datadog.api.client.v2.model.MetricPoint;
import com.datadog.api.client.v2.model.MetricSeries;
import java.time.OffsetDateTime;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    MetricPayload body =
        new MetricPayload()
            .series(
                Collections.singletonList(
                    new MetricSeries()
                        .metric("system.load.1")
                        .type(MetricIntakeType.UNSPECIFIED)
                        .points(
                            Collections.singletonList(
                                new MetricPoint()
                                    .timestamp(OffsetDateTime.now().toInstant().getEpochSecond())
                                    .value(0.7)))));

    try {
      IntakePayloadAccepted result =
          apiInstance.submitMetrics(
              body,
              new SubmitMetricsOptionalParameters().contentEncoding(MetricContentEncoding.ZSTD1));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#submitMetrics");
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

#####  Submit metrics returns "Payload accepted" response 
```
"""
Submit metrics returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_resource import MetricResource
from datadog_api_client.v2.model.metric_series import MetricSeries

body = MetricPayload(
    series=[
        MetricSeries(
            metric="system.load.1",
            type=MetricIntakeType.UNSPECIFIED,
            points=[
                MetricPoint(
                    timestamp=int(datetime.now().timestamp()),
                    value=0.7,
                ),
            ],
            resources=[
                MetricResource(
                    name="dummyhost",
                    type="host",
                ),
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_metrics(body=body)

    print(response)

```

Copy
#####  Submit metrics with compression returns "Payload accepted" response 
```
"""
Submit metrics with compression returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_content_encoding import MetricContentEncoding
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_series import MetricSeries

body = MetricPayload(
    series=[
        MetricSeries(
            metric="system.load.1",
            type=MetricIntakeType.UNSPECIFIED,
            points=[
                MetricPoint(
                    timestamp=int(datetime.now().timestamp()),
                    value=0.7,
                ),
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_metrics(content_encoding=MetricContentEncoding.ZSTD1, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"


```

#####  Submit metrics returns "Payload accepted" response 
```
# Submit metrics returns "Payload accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

body = DatadogAPIClient::V2::MetricPayload.new({
  series: [
    DatadogAPIClient::V2::MetricSeries.new({
      metric: "system.load.1",
      type: DatadogAPIClient::V2::MetricIntakeType::UNSPECIFIED,
      points: [
        DatadogAPIClient::V2::MetricPoint.new({
          timestamp: Time.now.to_i,
          value: 0.7,
        }),
      ],
      resources: [
        DatadogAPIClient::V2::MetricResource.new({
          name: "dummyhost",
          type: "host",
        }),
      ],
    }),
  ],
})
p api_instance.submit_metrics(body)

```

Copy
#####  Submit metrics with compression returns "Payload accepted" response 
```
# Submit metrics with compression returns "Payload accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

body = DatadogAPIClient::V2::MetricPayload.new({
  series: [
    DatadogAPIClient::V2::MetricSeries.new({
      metric: "system.load.1",
      type: DatadogAPIClient::V2::MetricIntakeType::UNSPECIFIED,
      points: [
        DatadogAPIClient::V2::MetricPoint.new({
          timestamp: Time.now.to_i,
          value: 0.7,
        }),
      ],
    }),
  ],
})
opts = {
  content_encoding: MetricContentEncoding::ZSTD1,
}
p api_instance.submit_metrics(body, opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"


```

#####  Submit metrics returns "Payload accepted" response 
```
// Submit metrics returns "Payload accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::api_metrics::SubmitMetricsOptionalParams;
use datadog_api_client::datadogV2::model::MetricIntakeType;
use datadog_api_client::datadogV2::model::MetricPayload;
use datadog_api_client::datadogV2::model::MetricPoint;
use datadog_api_client::datadogV2::model::MetricResource;
use datadog_api_client::datadogV2::model::MetricSeries;

#[tokio::main]
async fn main() {
    let body = MetricPayload::new(vec![MetricSeries::new(
        "system.load.1".to_string(),
        vec![MetricPoint::new().timestamp(1636629071).value(0.7 as f64)],
    )
    .resources(vec![MetricResource::new()
        .name("dummyhost".to_string())
        .type_("host".to_string())])
    .type_(MetricIntakeType::UNSPECIFIED)]);
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .submit_metrics(body, SubmitMetricsOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Submit metrics with compression returns "Payload accepted" response 
```
// Submit metrics with compression returns "Payload accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::api_metrics::SubmitMetricsOptionalParams;
use datadog_api_client::datadogV2::model::MetricContentEncoding;
use datadog_api_client::datadogV2::model::MetricIntakeType;
use datadog_api_client::datadogV2::model::MetricPayload;
use datadog_api_client::datadogV2::model::MetricPoint;
use datadog_api_client::datadogV2::model::MetricSeries;

#[tokio::main]
async fn main() {
    let body = MetricPayload::new(vec![MetricSeries::new(
        "system.load.1".to_string(),
        vec![MetricPoint::new().timestamp(1636629071).value(0.7 as f64)],
    )
    .type_(MetricIntakeType::UNSPECIFIED)]);
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .submit_metrics(
            body,
            SubmitMetricsOptionalParams::default().content_encoding(MetricContentEncoding::ZSTD1),
        )
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run


```

#####  Submit metrics returns "Payload accepted" response 
```
/**
 * Submit metrics returns "Payload accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiSubmitMetricsRequest = {
  body: {
    series: [
      {
        metric: "system.load.1",
        type: 0,
        points: [
          {
            timestamp: Math.round(new Date().getTime() / 1000),
            value: 0.7,
          },
        ],
        resources: [
          {
            name: "dummyhost",
            type: "host",
          },
        ],
      },
    ],
  },
};

apiInstance
  .submitMetrics(params)
  .then((data: v2.IntakePayloadAccepted) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Submit metrics with compression returns "Payload accepted" response 
```
/**
 * Submit metrics with compression returns "Payload accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiSubmitMetricsRequest = {
  body: {
    series: [
      {
        metric: "system.load.1",
        type: 0,
        points: [
          {
            timestamp: Math.round(new Date().getTime() / 1000),
            value: 0.7,
          },
        ],
      },
    ],
  },
  contentEncoding: "zstd1",
};

apiInstance
  .submitMetrics(params)
  .then((data: v2.IntakePayloadAccepted) => {
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
## [Get metric metadata](https://docs.datadoghq.com/api/latest/metrics/#get-metric-metadata)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/metrics/#get-metric-metadata-v1)


GET https://api.ap1.datadoghq.com/api/v1/metrics/{metric_name}https://api.ap2.datadoghq.com/api/v1/metrics/{metric_name}https://api.datadoghq.eu/api/v1/metrics/{metric_name}https://api.ddog-gov.com/api/v1/metrics/{metric_name}https://api.datadoghq.com/api/v1/metrics/{metric_name}https://api.us3.datadoghq.com/api/v1/metrics/{metric_name}https://api.us5.datadoghq.com/api/v1/metrics/{metric_name}
### Overview
Get metadata about a specific metric. This endpoint requires the `metrics_read` permission.
OAuth apps require the `metrics_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
Name of the metric for which to get metadata.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#GetMetricMetadata-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#GetMetricMetadata-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#GetMetricMetadata-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#GetMetricMetadata-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Object with all metric related metadata.
Expand All
Field
Type
Description
description
string
Metric description.
integration
string
Name of the integration that sent the metric if applicable.
per_unit
string
Per unit of the metric such as `second` in `bytes per second`.
short_name
string
A more human-readable and abbreviated version of the metric name.
statsd_interval
int64
StatsD flush interval of the metric in seconds if applicable.
type
string
Metric type such as `gauge` or `rate`.
unit
string
Primary unit of the metric such as `byte` or `operation`.
```
{
  "description": "string",
  "integration": "string",
  "per_unit": "second",
  "short_name": "string",
  "statsd_interval": "integer",
  "type": "count",
  "unit": "byte"
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python-legacy)


#####  Get metric metadata
Copy
```
                  # Path parameters  
export metric_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/metrics/${metric_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get metric metadata
```
"""
Get metric metadata returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.get_metric_metadata(
        metric_name="metric_name",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get metric metadata
```
# Get metric metadata returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new
p api_instance.get_metric_metadata("metric_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get metric metadata
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Get metadata on metric
result = dog.get_metadata('system.net.bytes_sent')
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get metric metadata
```
// Get metric metadata returns "OK" response

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
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.GetMetricMetadata(ctx, "metric_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.GetMetricMetadata`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.GetMetricMetadata`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get metric metadata
```
// Get metric metadata returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.model.MetricMetadata;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricMetadata result = apiInstance.getMetricMetadata("metric_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getMetricMetadata");
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

#####  Get metric metadata
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

metric = 'system.cpu.idle'

api.Metadata.get(metric_name=metric)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get metric metadata
```
// Get metric metadata returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api.get_metric_metadata("metric_name".to_string()).await;
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

#####  Get metric metadata
```
/**
 * Get metric metadata returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiGetMetricMetadataRequest = {
  metricName: "metric_name",
};

apiInstance
  .getMetricMetadata(params)
  .then((data: v1.MetricMetadata) => {
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
## [List tag configuration by name](https://docs.datadoghq.com/api/latest/metrics/#list-tag-configuration-by-name)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#list-tag-configuration-by-name-v2)


GET https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/tagshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/tags
### Overview
Returns the tag configuration for the given metric name. This endpoint requires the `metrics_read` permission.
OAuth apps require the `metrics_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurationByName-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurationByName-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurationByName-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurationByName-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object which includes a single metric’s tag configuration.
Field
Type
Description
data
object
Object for a single metric tag configuration.
attributes
object
Object containing the definition of a metric tag configuration attributes.
aggregations
[object]
Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.
space [_required_]
enum
A space aggregation for use in query. Allowed enum values: `avg,max,min,sum`
time [_required_]
enum
A time aggregation for use in query. Allowed enum values: `avg,count,max,min,sum`
created_at
date-time
Timestamp when the tag configuration was created.
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags. Defaults to false. Requires `tags` property.
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `metric_type` is `distribution`.
metric_type
enum
The metric's type. Allowed enum values: `gauge,count,rate,distribution`
default: `gauge`
modified_at
date-time
Timestamp when the tag configuration was last modified.
tags
[string]
List of tag keys on which to group.
id
string
The metric name for this resource.
type
enum
The metric tag configuration resource type. Allowed enum values: `manage_tags`
default: `manage_tags`
```
{
  "data": {
    "attributes": {
      "aggregations": [
        {
          "space": "sum",
          "time": "sum"
        }
      ],
      "created_at": "2020-03-25T09:48:37.463835Z",
      "exclude_tags_mode": false,
      "include_percentiles": true,
      "metric_type": "count",
      "modified_at": "2020-03-25T09:48:37.463835Z",
      "tags": [
        "app",
        "datacenter"
      ]
    },
    "id": "test.metric.latency",
    "type": "manage_tags"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  List tag configuration by name
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/tags" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List tag configuration by name
```
"""
List tag configuration by name returns "Success" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = environ["METRIC_TAG_CONFIGURATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tag_configuration_by_name(
        metric_name=METRIC_TAG_CONFIGURATION_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List tag configuration by name
```
# List tag configuration by name returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = ENV["METRIC_TAG_CONFIGURATION_DATA_ID"]
p api_instance.list_tag_configuration_by_name(METRIC_TAG_CONFIGURATION_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List tag configuration by name
```
// List tag configuration by name returns "Success" response

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
	// there is a valid "metric_tag_configuration" in the system
	MetricTagConfigurationDataID := os.Getenv("METRIC_TAG_CONFIGURATION_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.ListTagConfigurationByName(ctx, MetricTagConfigurationDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListTagConfigurationByName`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListTagConfigurationByName`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List tag configuration by name
```
// List tag configuration by name returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricTagConfigurationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    // there is a valid "metric_tag_configuration" in the system
    String METRIC_TAG_CONFIGURATION_DATA_ID = System.getenv("METRIC_TAG_CONFIGURATION_DATA_ID");

    try {
      MetricTagConfigurationResponse result =
          apiInstance.listTagConfigurationByName(METRIC_TAG_CONFIGURATION_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listTagConfigurationByName");
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

#####  List tag configuration by name
```
// List tag configuration by name returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "metric_tag_configuration" in the system
    let metric_tag_configuration_data_id =
        std::env::var("METRIC_TAG_CONFIGURATION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .list_tag_configuration_by_name(metric_tag_configuration_data_id.clone())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List tag configuration by name
```
/**
 * List tag configuration by name returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

// there is a valid "metric_tag_configuration" in the system
const METRIC_TAG_CONFIGURATION_DATA_ID = process.env
  .METRIC_TAG_CONFIGURATION_DATA_ID as string;

const params: v2.MetricsApiListTagConfigurationByNameRequest = {
  metricName: METRIC_TAG_CONFIGURATION_DATA_ID,
};

apiInstance
  .listTagConfigurationByName(params)
  .then((data: v2.MetricTagConfigurationResponse) => {
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
## [Query scalar data across multiple products](https://docs.datadoghq.com/api/latest/metrics/#query-scalar-data-across-multiple-products)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#query-scalar-data-across-multiple-products-v2)


POST https://api.ap1.datadoghq.com/api/v2/query/scalarhttps://api.ap2.datadoghq.com/api/v2/query/scalarhttps://api.datadoghq.eu/api/v2/query/scalarhttps://api.ddog-gov.com/api/v2/query/scalarhttps://api.datadoghq.com/api/v2/query/scalarhttps://api.us3.datadoghq.com/api/v2/query/scalarhttps://api.us5.datadoghq.com/api/v2/query/scalar
### Overview
Query scalar values (as seen on Query Value, Table, and Toplist widgets). Multiple data sources are supported with the ability to process the data using formulas and functions. This endpoint requires the `timeseries_query` permission.
OAuth apps require the `timeseries_query` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
data [_required_]
object
A single scalar query to be executed.
attributes [_required_]
object
The object describing a scalar formula request.
formulas
[object]
List of formulas to be calculated and returned as responses.
formula [_required_]
string
Formula string, referencing one or more queries with their name property.
limit
object
Message for specifying limits to the number of values returned by a query. This limit is only for scalar queries and has no effect on timeseries queries.
count
int32
The number of results to which to limit.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
from [_required_]
int64
Start date (inclusive) of the query in milliseconds since the Unix epoch.
queries [_required_]
[ <oneOf>]
List of queries to be run and used as inputs to the formulas.
Option 1
object
An individual scalar metrics query.
aggregator [_required_]
enum
The type of aggregation that can be performed on metrics-based queries. Allowed enum values: `avg,min,max,sum,last,percentile,mean,l2norm,area`
default: `avg`
data_source [_required_]
enum
A data source that is powered by the Metrics platform. Allowed enum values: `metrics,cloud_cost`
default: `metrics`
name
string
The variable name for use in formulas.
query [_required_]
string
A classic metrics query string.
Option 2
object
An individual scalar events query.
compute [_required_]
object
The instructions for what to compute for this query.
aggregation [_required_]
enum
The type of aggregation that can be performed on events-based queries. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
default: `count`
interval
int64
Interval for compute in milliseconds.
metric
string
The "measure" attribute on which to perform the computation.
data_source [_required_]
enum
A data source that is powered by the Events Platform. Allowed enum values: `logs,rum,dora`
default: `logs`
group_by
[object]
The list of facets on which to split results.
facet [_required_]
string
The facet by which to split groups.
limit
int32
The maximum buckets to return for this group by. Note: at most 10000 buckets are allowed. If grouping by multiple facets, the product of limits must not exceed 10000.
default: `10`
sort
object
The dimension by which to sort a query's results.
aggregation [_required_]
enum
The type of aggregation that can be performed on events-based queries. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
default: `count`
metric
string
The metric's calculated value which should be used to define the sort order of a query's results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
type
enum
The type of sort to use on the calculated value. Allowed enum values: `alphabetical,measure`
indexes
[string]
The indexes in which to search.
name
string
The variable name for use in formulas.
search
object
Configuration of the search/filter for an events query.
query
string
The search/filter string for an events query.
to [_required_]
int64
End date (exclusive) of the query in milliseconds since the Unix epoch.
type [_required_]
enum
The type of the resource. The value should always be scalar_request. Allowed enum values: `scalar_request`
default: `scalar_request`
```
{
  "data": {
    "attributes": {
      "formulas": [
        {
          "formula": "a",
          "limit": {
            "count": 10,
            "order": "desc"
          }
        }
      ],
      "from": 1636625471000,
      "queries": [
        {
          "aggregator": "avg",
          "data_source": "metrics",
          "query": "avg:system.cpu.user{*}",
          "name": "a"
        }
      ],
      "to": 1636629071000
    },
    "type": "scalar_request"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#QueryScalarData-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#QueryScalarData-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/metrics/#QueryScalarData-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#QueryScalarData-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#QueryScalarData-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


A message containing one or more responses to scalar queries.
Field
Type
Description
data
object
A message containing the response to a scalar query.
attributes
object
The object describing a scalar response.
columns
[ <oneOf>]
List of response columns, each corresponding to an individual formula or query in the request and with values in parallel arrays matching the series list.
Option 1
object
A column containing the tag keys and values in a group.
name
string
The name of the tag key or group.
type
enum
The type of column present for groups. Allowed enum values: `group`
default: `group`
values
[array]
The array of tag values for each group found for the results of the formulas or queries.
Option 2
object
A column containing the numerical results for a formula or query.
meta
object
Metadata for the resulting numerical values.
unit
[object]
Detailed information about the unit. First element describes the "primary unit" (for example, `bytes` in `bytes per second`). The second element describes the "per unit" (for example, `second` in `bytes per second`). If the second element is not present, the API returns null.
family
string
Unit family, allows for conversion between units of the same family, for scaling.
name
string
Unit name
plural
string
Plural form of the unit name.
scale_factor
double
Factor for scaling between units of the same family.
short_name
string
Abbreviation of the unit.
name
string
The name referencing the formula or query for this column.
type
enum
The type of column present for numbers. Allowed enum values: `number`
default: `number`
values
[number]
The array of numerical values for one formula or query.
type
enum
The type of the resource. The value should always be scalar_response. Allowed enum values: `scalar_response`
default: `scalar_response`
errors
string
An error generated when processing a request.
```
{
  "data": {
    "attributes": {
      "columns": [
        {
          "name": "env",
          "type": "group",
          "values": [
            [
              "staging"
            ]
          ]
        }
      ]
    },
    "type": "scalar_response"
  },
  "errors": "string"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Scalar cross product query returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/query/scalar" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "formulas": [
        {
          "formula": "a",
          "limit": {
            "count": 10,
            "order": "desc"
          }
        }
      ],
      "from": 1636625471000,
      "queries": [
        {
          "aggregator": "avg",
          "data_source": "metrics",
          "query": "avg:system.cpu.user{*}",
          "name": "a"
        }
      ],
      "to": 1636629071000
    },
    "type": "scalar_request"
  }
}
EOF  

                        
```

#####  Scalar cross product query returns "OK" response
```
// Scalar cross product query returns "OK" response

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
	body := datadogV2.ScalarFormulaQueryRequest{
		Data: datadogV2.ScalarFormulaRequest{
			Attributes: datadogV2.ScalarFormulaRequestAttributes{
				Formulas: []datadogV2.QueryFormula{
					{
						Formula: "a",
						Limit: &datadogV2.FormulaLimit{
							Count: datadog.PtrInt32(10),
							Order: datadogV2.QUERYSORTORDER_DESC.Ptr(),
						},
					},
				},
				From: 1636625471000,
				Queries: []datadogV2.ScalarQuery{
					datadogV2.ScalarQuery{
						MetricsScalarQuery: &datadogV2.MetricsScalarQuery{
							Aggregator: datadogV2.METRICSAGGREGATOR_AVG,
							DataSource: datadogV2.METRICSDATASOURCE_METRICS,
							Query:      "avg:system.cpu.user{*}",
							Name:       datadog.PtrString("a"),
						}},
				},
				To: 1636629071000,
			},
			Type: datadogV2.SCALARFORMULAREQUESTTYPE_SCALAR_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.QueryScalarData(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.QueryScalarData`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.QueryScalarData`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Scalar cross product query returns "OK" response
```
// Scalar cross product query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.FormulaLimit;
import com.datadog.api.client.v2.model.MetricsAggregator;
import com.datadog.api.client.v2.model.MetricsDataSource;
import com.datadog.api.client.v2.model.MetricsScalarQuery;
import com.datadog.api.client.v2.model.QueryFormula;
import com.datadog.api.client.v2.model.QuerySortOrder;
import com.datadog.api.client.v2.model.ScalarFormulaQueryRequest;
import com.datadog.api.client.v2.model.ScalarFormulaQueryResponse;
import com.datadog.api.client.v2.model.ScalarFormulaRequest;
import com.datadog.api.client.v2.model.ScalarFormulaRequestAttributes;
import com.datadog.api.client.v2.model.ScalarFormulaRequestType;
import com.datadog.api.client.v2.model.ScalarQuery;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    ScalarFormulaQueryRequest body =
        new ScalarFormulaQueryRequest()
            .data(
                new ScalarFormulaRequest()
                    .attributes(
                        new ScalarFormulaRequestAttributes()
                            .formulas(
                                Collections.singletonList(
                                    new QueryFormula()
                                        .formula("a")
                                        .limit(
                                            new FormulaLimit()
                                                .count(10)
                                                .order(QuerySortOrder.DESC))))
                            .from(1636625471000L)
                            .queries(
                                Collections.singletonList(
                                    new ScalarQuery(
                                        new MetricsScalarQuery()
                                            .aggregator(MetricsAggregator.AVG)
                                            .dataSource(MetricsDataSource.METRICS)
                                            .query("avg:system.cpu.user{*}")
                                            .name("a"))))
                            .to(1636629071000L))
                    .type(ScalarFormulaRequestType.SCALAR_REQUEST));

    try {
      ScalarFormulaQueryResponse result = apiInstance.queryScalarData(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#queryScalarData");
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

#####  Scalar cross product query returns "OK" response
```
"""
Scalar cross product query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.formula_limit import FormulaLimit
from datadog_api_client.v2.model.metrics_aggregator import MetricsAggregator
from datadog_api_client.v2.model.metrics_data_source import MetricsDataSource
from datadog_api_client.v2.model.metrics_scalar_query import MetricsScalarQuery
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.scalar_formula_query_request import ScalarFormulaQueryRequest
from datadog_api_client.v2.model.scalar_formula_request import ScalarFormulaRequest
from datadog_api_client.v2.model.scalar_formula_request_attributes import ScalarFormulaRequestAttributes
from datadog_api_client.v2.model.scalar_formula_request_queries import ScalarFormulaRequestQueries
from datadog_api_client.v2.model.scalar_formula_request_type import ScalarFormulaRequestType

body = ScalarFormulaQueryRequest(
    data=ScalarFormulaRequest(
        attributes=ScalarFormulaRequestAttributes(
            formulas=[
                QueryFormula(
                    formula="a",
                    limit=FormulaLimit(
                        count=10,
                        order=QuerySortOrder.DESC,
                    ),
                ),
            ],
            _from=1636625471000,
            queries=ScalarFormulaRequestQueries(
                [
                    MetricsScalarQuery(
                        aggregator=MetricsAggregator.AVG,
                        data_source=MetricsDataSource.METRICS,
                        query="avg:system.cpu.user{*}",
                        name="a",
                    ),
                ]
            ),
            to=1636629071000,
        ),
        type=ScalarFormulaRequestType.SCALAR_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_scalar_data(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Scalar cross product query returns "OK" response
```
# Scalar cross product query returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

body = DatadogAPIClient::V2::ScalarFormulaQueryRequest.new({
  data: DatadogAPIClient::V2::ScalarFormulaRequest.new({
    attributes: DatadogAPIClient::V2::ScalarFormulaRequestAttributes.new({
      formulas: [
        DatadogAPIClient::V2::QueryFormula.new({
          formula: "a",
          limit: DatadogAPIClient::V2::FormulaLimit.new({
            count: 10,
            order: DatadogAPIClient::V2::QuerySortOrder::DESC,
          }),
        }),
      ],
      from: 1636625471000,
      queries: [
        DatadogAPIClient::V2::MetricsScalarQuery.new({
          aggregator: DatadogAPIClient::V2::MetricsAggregator::AVG,
          data_source: DatadogAPIClient::V2::MetricsDataSource::METRICS,
          query: "avg:system.cpu.user{*}",
          name: "a",
        }),
      ],
      to: 1636629071000,
    }),
    type: DatadogAPIClient::V2::ScalarFormulaRequestType::SCALAR_REQUEST,
  }),
})
p api_instance.query_scalar_data(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Scalar cross product query returns "OK" response
```
// Scalar cross product query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::model::FormulaLimit;
use datadog_api_client::datadogV2::model::MetricsAggregator;
use datadog_api_client::datadogV2::model::MetricsDataSource;
use datadog_api_client::datadogV2::model::MetricsScalarQuery;
use datadog_api_client::datadogV2::model::QueryFormula;
use datadog_api_client::datadogV2::model::QuerySortOrder;
use datadog_api_client::datadogV2::model::ScalarFormulaQueryRequest;
use datadog_api_client::datadogV2::model::ScalarFormulaRequest;
use datadog_api_client::datadogV2::model::ScalarFormulaRequestAttributes;
use datadog_api_client::datadogV2::model::ScalarFormulaRequestType;
use datadog_api_client::datadogV2::model::ScalarQuery;

#[tokio::main]
async fn main() {
    let body = ScalarFormulaQueryRequest::new(ScalarFormulaRequest::new(
        ScalarFormulaRequestAttributes::new(
            1636625471000,
            vec![ScalarQuery::MetricsScalarQuery(Box::new(
                MetricsScalarQuery::new(
                    MetricsAggregator::AVG,
                    MetricsDataSource::METRICS,
                    "avg:system.cpu.user{*}".to_string(),
                )
                .name("a".to_string()),
            ))],
            1636629071000,
        )
        .formulas(vec![QueryFormula::new("a".to_string())
            .limit(FormulaLimit::new().count(10).order(QuerySortOrder::DESC))]),
        ScalarFormulaRequestType::SCALAR_REQUEST,
    ));
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api.query_scalar_data(body).await;
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

#####  Scalar cross product query returns "OK" response
```
/**
 * Scalar cross product query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiQueryScalarDataRequest = {
  body: {
    data: {
      attributes: {
        formulas: [
          {
            formula: "a",
            limit: {
              count: 10,
              order: "desc",
            },
          },
        ],
        from: 1636625471000,
        queries: [
          {
            aggregator: "avg",
            dataSource: "metrics",
            query: "avg:system.cpu.user{*}",
            name: "a",
          },
        ],
        to: 1636629071000,
      },
      type: "scalar_request",
    },
  },
};

apiInstance
  .queryScalarData(params)
  .then((data: v2.ScalarFormulaQueryResponse) => {
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
## [Edit metric metadata](https://docs.datadoghq.com/api/latest/metrics/#edit-metric-metadata)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/metrics/#edit-metric-metadata-v1)


PUT https://api.ap1.datadoghq.com/api/v1/metrics/{metric_name}https://api.ap2.datadoghq.com/api/v1/metrics/{metric_name}https://api.datadoghq.eu/api/v1/metrics/{metric_name}https://api.ddog-gov.com/api/v1/metrics/{metric_name}https://api.datadoghq.com/api/v1/metrics/{metric_name}https://api.us3.datadoghq.com/api/v1/metrics/{metric_name}https://api.us5.datadoghq.com/api/v1/metrics/{metric_name}
### Overview
Edit metadata of a specific metric. Find out more about [supported types](https://docs.datadoghq.com/developers/metrics). This endpoint requires the `metrics_metadata_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
Name of the metric for which to edit metadata.
### Request
#### Body Data (required)
New metadata.
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Expand All
Field
Type
Description
description
string
Metric description.
integration
string
Name of the integration that sent the metric if applicable.
per_unit
string
Per unit of the metric such as `second` in `bytes per second`.
short_name
string
A more human-readable and abbreviated version of the metric name.
statsd_interval
int64
StatsD flush interval of the metric in seconds if applicable.
type
string
Metric type such as `gauge` or `rate`.
unit
string
Primary unit of the metric such as `byte` or `operation`.
```
{
  "description": "string",
  "per_unit": "second",
  "short_name": "string",
  "statsd_interval": "integer",
  "type": "count",
  "unit": "byte"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#UpdateMetricMetadata-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#UpdateMetricMetadata-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#UpdateMetricMetadata-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#UpdateMetricMetadata-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#UpdateMetricMetadata-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Object with all metric related metadata.
Expand All
Field
Type
Description
description
string
Metric description.
integration
string
Name of the integration that sent the metric if applicable.
per_unit
string
Per unit of the metric such as `second` in `bytes per second`.
short_name
string
A more human-readable and abbreviated version of the metric name.
statsd_interval
int64
StatsD flush interval of the metric in seconds if applicable.
type
string
Metric type such as `gauge` or `rate`.
unit
string
Primary unit of the metric such as `byte` or `operation`.
```
{
  "description": "string",
  "integration": "string",
  "per_unit": "second",
  "short_name": "string",
  "statsd_interval": "integer",
  "type": "count",
  "unit": "byte"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Edit metric metadata
Copy
```
                  # Path parameters  
export metric_name="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/metrics/${metric_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Edit metric metadata
```
"""
Edit metric metadata returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.metric_metadata import MetricMetadata

body = MetricMetadata(
    per_unit="second",
    type="count",
    unit="byte",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_metric_metadata(metric_name="metric_name", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit metric metadata
```
# Edit metric metadata returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new

body = DatadogAPIClient::V1::MetricMetadata.new({
  per_unit: "second",
  type: "count",
  unit: "byte",
})
p api_instance.update_metric_metadata("metric_name", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit metric metadata
```
// Edit metric metadata returns "OK" response

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
	body := datadogV1.MetricMetadata{
		PerUnit: datadog.PtrString("second"),
		Type:    datadog.PtrString("count"),
		Unit:    datadog.PtrString("byte"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.UpdateMetricMetadata(ctx, "metric_name", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.UpdateMetricMetadata`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.UpdateMetricMetadata`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit metric metadata
```
// Edit metric metadata returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.model.MetricMetadata;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    MetricMetadata body = new MetricMetadata().perUnit("second").type("count").unit("byte");

    try {
      MetricMetadata result = apiInstance.updateMetricMetadata("metric_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#updateMetricMetadata");
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

#####  Edit metric metadata
```
// Edit metric metadata returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;
use datadog_api_client::datadogV1::model::MetricMetadata;

#[tokio::main]
async fn main() {
    let body = MetricMetadata::new()
        .per_unit("second".to_string())
        .type_("count".to_string())
        .unit("byte".to_string());
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .update_metric_metadata("metric_name".to_string(), body)
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

#####  Edit metric metadata
```
/**
 * Edit metric metadata returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiUpdateMetricMetadataRequest = {
  body: {
    perUnit: "second",
    type: "count",
    unit: "byte",
  },
  metricName: "metric_name",
};

apiInstance
  .updateMetricMetadata(params)
  .then((data: v1.MetricMetadata) => {
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
## [Update a tag configuration](https://docs.datadoghq.com/api/latest/metrics/#update-a-tag-configuration)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#update-a-tag-configuration-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/tagshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/tags
### Overview
Update the tag configuration of a metric or percentile aggregations of a distribution metric or custom aggregations of a count, rate, or gauge metric. By setting `exclude_tags_mode` to true the behavior is changed from an allow-list to a deny-list, and tags in the defined list will not be queryable. Can only be used with application keys from users with the `Manage Tags for Metrics` permission. This endpoint requires a tag configuration to be created first. This endpoint requires the `metric_tags_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
data [_required_]
object
Object for a single tag configuration to be edited.
attributes
object
Object containing the definition of a metric tag configuration to be updated.
aggregations
[object]
Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.
space [_required_]
enum
A space aggregation for use in query. Allowed enum values: `avg,max,min,sum`
time [_required_]
enum
A time aggregation for use in query. Allowed enum values: `avg,count,max,min,sum`
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags. Defaults to false. Requires `tags` property.
include_percentiles
boolean
Toggle to include/exclude percentiles for a distribution metric. Defaults to false. Can only be applied to metrics that have a `metric_type` of `distribution`.
tags
[string]
A list of tag keys that will be queryable for your metric.
default: 
id [_required_]
string
The metric name for this resource.
type [_required_]
enum
The metric tag configuration resource type. Allowed enum values: `manage_tags`
default: `manage_tags`
```
{
  "data": {
    "type": "manage_tags",
    "id": "test.metric.latency",
    "attributes": {
      "tags": [
        "app"
      ]
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#UpdateTagConfiguration-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#UpdateTagConfiguration-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#UpdateTagConfiguration-403-v2)
  * [422](https://docs.datadoghq.com/api/latest/metrics/#UpdateTagConfiguration-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#UpdateTagConfiguration-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object which includes a single metric’s tag configuration.
Field
Type
Description
data
object
Object for a single metric tag configuration.
attributes
object
Object containing the definition of a metric tag configuration attributes.
aggregations
[object]
Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.
space [_required_]
enum
A space aggregation for use in query. Allowed enum values: `avg,max,min,sum`
time [_required_]
enum
A time aggregation for use in query. Allowed enum values: `avg,count,max,min,sum`
created_at
date-time
Timestamp when the tag configuration was created.
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags. Defaults to false. Requires `tags` property.
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `metric_type` is `distribution`.
metric_type
enum
The metric's type. Allowed enum values: `gauge,count,rate,distribution`
default: `gauge`
modified_at
date-time
Timestamp when the tag configuration was last modified.
tags
[string]
List of tag keys on which to group.
id
string
The metric name for this resource.
type
enum
The metric tag configuration resource type. Allowed enum values: `manage_tags`
default: `manage_tags`
```
{
  "data": {
    "attributes": {
      "aggregations": [
        {
          "space": "sum",
          "time": "sum"
        }
      ],
      "created_at": "2020-03-25T09:48:37.463835Z",
      "exclude_tags_mode": false,
      "include_percentiles": true,
      "metric_type": "count",
      "modified_at": "2020-03-25T09:48:37.463835Z",
      "tags": [
        "app",
        "datacenter"
      ]
    },
    "id": "test.metric.latency",
    "type": "manage_tags"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Unprocessable Entity
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Update a tag configuration returns "OK" response
Copy
```
                          # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/tags" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "manage_tags",
    "id": "test.metric.latency",
    "attributes": {
      "tags": [
        "app"
      ]
    }
  }
}
EOF  

                        
```

#####  Update a tag configuration returns "OK" response
```
// Update a tag configuration returns "OK" response

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
	// there is a valid "metric_tag_configuration" in the system
	MetricTagConfigurationDataID := os.Getenv("METRIC_TAG_CONFIGURATION_DATA_ID")

	body := datadogV2.MetricTagConfigurationUpdateRequest{
		Data: datadogV2.MetricTagConfigurationUpdateData{
			Type: datadogV2.METRICTAGCONFIGURATIONTYPE_MANAGE_TAGS,
			Id:   MetricTagConfigurationDataID,
			Attributes: &datadogV2.MetricTagConfigurationUpdateAttributes{
				Tags: []string{
					"app",
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.UpdateTagConfiguration(ctx, MetricTagConfigurationDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.UpdateTagConfiguration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.UpdateTagConfiguration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a tag configuration returns "OK" response
```
// Update a tag configuration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricTagConfigurationResponse;
import com.datadog.api.client.v2.model.MetricTagConfigurationType;
import com.datadog.api.client.v2.model.MetricTagConfigurationUpdateAttributes;
import com.datadog.api.client.v2.model.MetricTagConfigurationUpdateData;
import com.datadog.api.client.v2.model.MetricTagConfigurationUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    // there is a valid "metric_tag_configuration" in the system
    String METRIC_TAG_CONFIGURATION_DATA_ID = System.getenv("METRIC_TAG_CONFIGURATION_DATA_ID");

    MetricTagConfigurationUpdateRequest body =
        new MetricTagConfigurationUpdateRequest()
            .data(
                new MetricTagConfigurationUpdateData()
                    .type(MetricTagConfigurationType.MANAGE_TAGS)
                    .id(METRIC_TAG_CONFIGURATION_DATA_ID)
                    .attributes(
                        new MetricTagConfigurationUpdateAttributes()
                            .tags(Collections.singletonList("app"))));

    try {
      MetricTagConfigurationResponse result =
          apiInstance.updateTagConfiguration(METRIC_TAG_CONFIGURATION_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#updateTagConfiguration");
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

#####  Update a tag configuration returns "OK" response
```
"""
Update a tag configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType
from datadog_api_client.v2.model.metric_tag_configuration_update_attributes import (
    MetricTagConfigurationUpdateAttributes,
)
from datadog_api_client.v2.model.metric_tag_configuration_update_data import MetricTagConfigurationUpdateData
from datadog_api_client.v2.model.metric_tag_configuration_update_request import MetricTagConfigurationUpdateRequest

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = environ["METRIC_TAG_CONFIGURATION_DATA_ID"]

body = MetricTagConfigurationUpdateRequest(
    data=MetricTagConfigurationUpdateData(
        type=MetricTagConfigurationType.MANAGE_TAGS,
        id=METRIC_TAG_CONFIGURATION_DATA_ID,
        attributes=MetricTagConfigurationUpdateAttributes(
            tags=[
                "app",
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_tag_configuration(metric_name=METRIC_TAG_CONFIGURATION_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a tag configuration returns "OK" response
```
# Update a tag configuration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = ENV["METRIC_TAG_CONFIGURATION_DATA_ID"]

body = DatadogAPIClient::V2::MetricTagConfigurationUpdateRequest.new({
  data: DatadogAPIClient::V2::MetricTagConfigurationUpdateData.new({
    type: DatadogAPIClient::V2::MetricTagConfigurationType::MANAGE_TAGS,
    id: METRIC_TAG_CONFIGURATION_DATA_ID,
    attributes: DatadogAPIClient::V2::MetricTagConfigurationUpdateAttributes.new({
      tags: [
        "app",
      ],
    }),
  }),
})
p api_instance.update_tag_configuration(METRIC_TAG_CONFIGURATION_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a tag configuration returns "OK" response
```
// Update a tag configuration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::model::MetricTagConfigurationType;
use datadog_api_client::datadogV2::model::MetricTagConfigurationUpdateAttributes;
use datadog_api_client::datadogV2::model::MetricTagConfigurationUpdateData;
use datadog_api_client::datadogV2::model::MetricTagConfigurationUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "metric_tag_configuration" in the system
    let metric_tag_configuration_data_id =
        std::env::var("METRIC_TAG_CONFIGURATION_DATA_ID").unwrap();
    let body = MetricTagConfigurationUpdateRequest::new(
        MetricTagConfigurationUpdateData::new(
            metric_tag_configuration_data_id.clone(),
            MetricTagConfigurationType::MANAGE_TAGS,
        )
        .attributes(MetricTagConfigurationUpdateAttributes::new().tags(vec!["app".to_string()])),
    );
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .update_tag_configuration(metric_tag_configuration_data_id.clone(), body)
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

#####  Update a tag configuration returns "OK" response
```
/**
 * Update a tag configuration returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

// there is a valid "metric_tag_configuration" in the system
const METRIC_TAG_CONFIGURATION_DATA_ID = process.env
  .METRIC_TAG_CONFIGURATION_DATA_ID as string;

const params: v2.MetricsApiUpdateTagConfigurationRequest = {
  body: {
    data: {
      type: "manage_tags",
      id: METRIC_TAG_CONFIGURATION_DATA_ID,
      attributes: {
        tags: ["app"],
      },
    },
  },
  metricName: METRIC_TAG_CONFIGURATION_DATA_ID,
};

apiInstance
  .updateTagConfiguration(params)
  .then((data: v2.MetricTagConfigurationResponse) => {
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
## [Delete a tag configuration](https://docs.datadoghq.com/api/latest/metrics/#delete-a-tag-configuration)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#delete-a-tag-configuration-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/tagshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/tagshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/tagshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/tags
### Overview
Deletes a metric’s tag configuration. Can only be used with application keys from users with the `Manage Tags for Metrics` permission. This endpoint requires the `metric_tags_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Response
  * [204](https://docs.datadoghq.com/api/latest/metrics/#DeleteTagConfiguration-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#DeleteTagConfiguration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#DeleteTagConfiguration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#DeleteTagConfiguration-429-v2)


No Content
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Delete a tag configuration
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/tags" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a tag configuration
```
"""
Delete a tag configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    api_instance.delete_tag_configuration(
        metric_name="ExampleMetric",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a tag configuration
```
# Delete a tag configuration returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new
api_instance.delete_tag_configuration("ExampleMetric")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a tag configuration
```
// Delete a tag configuration returns "No Content" response

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
	api := datadogV2.NewMetricsApi(apiClient)
	r, err := api.DeleteTagConfiguration(ctx, "ExampleMetric")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.DeleteTagConfiguration`: %v\n", err)
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

#####  Delete a tag configuration
```
// Delete a tag configuration returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      apiInstance.deleteTagConfiguration("ExampleMetric");
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#deleteTagConfiguration");
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

#####  Delete a tag configuration
```
// Delete a tag configuration returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .delete_tag_configuration("ExampleMetric".to_string())
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

#####  Delete a tag configuration
```
/**
 * Delete a tag configuration returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiDeleteTagConfigurationRequest = {
  metricName: "ExampleMetric",
};

apiInstance
  .deleteTagConfiguration(params)
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
## [Search metrics](https://docs.datadoghq.com/api/latest/metrics/#search-metrics)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/metrics/#search-metrics-v1)


GET https://api.ap1.datadoghq.com/api/v1/searchhttps://api.ap2.datadoghq.com/api/v1/searchhttps://api.datadoghq.eu/api/v1/searchhttps://api.ddog-gov.com/api/v1/searchhttps://api.datadoghq.com/api/v1/searchhttps://api.us3.datadoghq.com/api/v1/searchhttps://api.us5.datadoghq.com/api/v1/search
### Overview
**Note** : This endpoint is deprecated. Use `/api/v2/metrics` instead.
Search for metrics from the last 24 hours in Datadog.
This endpoint requires the `metrics_read` permission.
OAuth apps require the `metrics_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
q [_required_]
string
Query string to search metrics upon. Can optionally be prefixed with `metrics:`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListMetrics-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#ListMetrics-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListMetrics-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListMetrics-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Object containing the list of metrics matching the search query.
Field
Type
Description
results
object
Search result.
metrics
[string]
List of metrics that match the search query.
```
{
  "results": {
    "metrics": []
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby-legacy)


#####  Search metrics
Copy
```
                  # Required query arguments  
export q="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/search?q=${q}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Search metrics
```
"""
Search metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_metrics(
        q="q",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search metrics
```
# Search metrics returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new
p api_instance.list_metrics("q")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search metrics
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.search("metrics:test")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search metrics
```
// Search metrics returns "OK" response

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
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.ListMetrics(ctx, "q")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListMetrics`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Search metrics
```
// Search metrics returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.model.MetricSearchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricSearchResponse result = apiInstance.listMetrics("q");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listMetrics");
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

#####  Search metrics
```
// Search metrics returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api.list_metrics("q".to_string()).await;
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

#####  Search metrics
```
/**
 * Search metrics returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiListMetricsRequest = {
  q: "q",
};

apiInstance
  .listMetrics(params)
  .then((data: v1.MetricSearchResponse) => {
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
## [Get a list of metrics](https://docs.datadoghq.com/api/latest/metrics/#get-a-list-of-metrics)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#get-a-list-of-metrics-v2)


GET https://api.ap1.datadoghq.com/api/v2/metricshttps://api.ap2.datadoghq.com/api/v2/metricshttps://api.datadoghq.eu/api/v2/metricshttps://api.ddog-gov.com/api/v2/metricshttps://api.datadoghq.com/api/v2/metricshttps://api.us3.datadoghq.com/api/v2/metricshttps://api.us5.datadoghq.com/api/v2/metrics
### Overview
Returns all metrics that can be configured in the Metrics Summary page or with Metrics without Limits™ (matching additional filters if specified). Optionally, paginate by using the `page[cursor]` and/or `page[size]` query parameters. To fetch the first page, pass in a query parameter with either a valid `page[size]` or an empty cursor like `page[cursor]=`. To fetch the next page, pass in the `next_cursor` value from the response as the new `page[cursor]` value. Once the `meta.pagination.next_cursor` value is null, all pages have been retrieved. This endpoint requires the `metrics_read` permission.
OAuth apps require the `metrics_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter[configured]
boolean
Filter custom metrics that have configured tags.
filter[tags_configured]
string
Filter tag configurations by configured tags.
filter[metric_type]
enum
Filter metrics by metric type.  
Allowed enum values: `non_distribution, distribution`
filter[include_percentiles]
boolean
Filter distributions with additional percentile aggregations enabled or disabled.
filter[queried]
boolean
(Preview) Filter custom metrics that have or have not been queried in the specified window[seconds]. If no window is provided or the window is less than 2 hours, a default of 2 hours will be applied.
filter[tags]
string
Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions. Can only be combined with the filter[queried] filter.
filter[related_assets]
boolean
(Preview) Filter metrics that are used in dashboards, monitors, notebooks, SLOs.
window[seconds]
integer
The number of seconds of look back (from now) to apply to a filter[tag] or filter[queried] query. Default value is 3600 (1 hour), maximum value is 2,592,000 (30 days).
page[size]
integer
Maximum number of results returned.
page[cursor]
string
String to query the next page of results. This key is provided with each valid response from the API in `meta.pagination.next_cursor`. Once the `meta.pagination.next_cursor` key is null, all pages have been retrieved.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurations-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurations-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurations-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListTagConfigurations-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object that includes metrics and metric tag configurations.
Field
Type
Description
data
[ <oneOf>]
Array of metrics and metric tag configurations.
Option 1
object
Object for a single metric tag configuration.
id
string
The metric name for this resource.
type
enum
The metric resource type. Allowed enum values: `metrics`
default: `metrics`
Option 2
object
Object for a single metric tag configuration.
attributes
object
Object containing the definition of a metric tag configuration attributes.
aggregations
[object]
Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.
space [_required_]
enum
A space aggregation for use in query. Allowed enum values: `avg,max,min,sum`
time [_required_]
enum
A time aggregation for use in query. Allowed enum values: `avg,count,max,min,sum`
created_at
date-time
Timestamp when the tag configuration was created.
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags. Defaults to false. Requires `tags` property.
include_percentiles
boolean
Toggle to include or exclude percentile aggregations for distribution metrics. Only present when the `metric_type` is `distribution`.
metric_type
enum
The metric's type. Allowed enum values: `gauge,count,rate,distribution`
default: `gauge`
modified_at
date-time
Timestamp when the tag configuration was last modified.
tags
[string]
List of tag keys on which to group.
id
string
The metric name for this resource.
type
enum
The metric tag configuration resource type. Allowed enum values: `manage_tags`
default: `manage_tags`
links
object
Pagination links. Only present if pagination query parameters were provided.
first
string
Link to the first page.
last
string
Link to the last page.
next
string
Link to the next page.
prev
string
Link to previous page.
self
string
Link to current page.
meta
object
Response metadata object.
pagination
object
Paging attributes. Only present if pagination query parameters were provided.
cursor
string
The cursor used to get the current results, if any.
limit
int32
Number of results returned
next_cursor
string
The cursor used to get the next results, if any.
type
enum
Type of metric pagination. Allowed enum values: `cursor_limit`
default: `cursor_limit`
```
{
  "data": [
    {
      "id": "test.metric.latency",
      "type": "metrics"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "pagination": {
      "cursor": "string",
      "limit": "integer",
      "next_cursor": "string",
      "type": "cursor_limit"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Get a list of metrics
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of metrics
```
"""
Get a list of metrics returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tag_configurations()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of metrics
```
# Get a list of metrics returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new
p api_instance.list_tag_configurations()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of metrics
```
// Get a list of metrics returns "Success" response

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
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.ListTagConfigurations(ctx, *datadogV2.NewListTagConfigurationsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListTagConfigurations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListTagConfigurations`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of metrics
```
// Get a list of metrics returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricsAndMetricTagConfigurationsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricsAndMetricTagConfigurationsResponse result = apiInstance.listTagConfigurations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listTagConfigurations");
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

#####  Get a list of metrics
```
// Get a list of metrics returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::ListTagConfigurationsOptionalParams;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .list_tag_configurations(ListTagConfigurationsOptionalParams::default())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a list of metrics
```
/**
 * Get a list of metrics returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

apiInstance
  .listTagConfigurations()
  .then((data: v2.MetricsAndMetricTagConfigurationsResponse) => {
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
## [Query timeseries points](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-points)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-points-v1)


GET https://api.ap1.datadoghq.com/api/v1/queryhttps://api.ap2.datadoghq.com/api/v1/queryhttps://api.datadoghq.eu/api/v1/queryhttps://api.ddog-gov.com/api/v1/queryhttps://api.datadoghq.com/api/v1/queryhttps://api.us3.datadoghq.com/api/v1/queryhttps://api.us5.datadoghq.com/api/v1/query
### Overview
Query timeseries points. This endpoint requires the `timeseries_query` permission.
OAuth apps require the `timeseries_query` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
from [_required_]
integer
Start of the queried time period, seconds since the Unix epoch.
to [_required_]
integer
End of the queried time period, seconds since the Unix epoch.
query [_required_]
string
Query string.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#QueryMetrics-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#QueryMetrics-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#QueryMetrics-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#QueryMetrics-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response Object that includes your query and the list of metrics retrieved.
Field
Type
Description
error
string
Message indicating the errors if status is not `ok`.
from_date
int64
Start of requested time window, milliseconds since Unix epoch.
group_by
[string]
List of tag keys on which to group.
message
string
Message indicating `success` if status is `ok`.
query
string
Query string
res_type
string
Type of response.
series
[object]
List of timeseries queried.
aggr
string
Aggregation type.
display_name
string
Display name of the metric.
end
int64
End of the time window, milliseconds since Unix epoch.
expression
string
Metric expression.
interval
int64
Number of milliseconds between data samples.
length
int64
Number of data samples.
metric
string
Metric name.
pointlist
[array]
List of points of the timeseries in milliseconds.
query_index
int64
The index of the series' query within the request.
scope
string
Metric scope, comma separated list of tags.
start
int64
Start of the time window, milliseconds since Unix epoch.
tag_set
[string]
Unique tags identifying this series.
unit
[object]
Detailed information about the metric unit. The first element describes the "primary unit" (for example, `bytes` in `bytes per second`). The second element describes the "per unit" (for example, `second` in `bytes per second`). If the second element is not present, the API returns null.
family
string
Unit family, allows for conversion between units of the same family, for scaling.
name
string
Unit name
plural
string
Plural form of the unit name.
scale_factor
double
Factor for scaling between units of the same family.
short_name
string
Abbreviation of the unit.
status
string
Status of the query.
to_date
int64
End of requested time window, milliseconds since Unix epoch.
```
{
  "error": "string",
  "from_date": "integer",
  "group_by": [],
  "message": "string",
  "query": "string",
  "res_type": "time_series",
  "series": [
    {
      "aggr": "avg",
      "display_name": "system.cpu.idle",
      "end": "integer",
      "expression": "system.cpu.idle{host:foo,env:test}",
      "interval": "integer",
      "length": "integer",
      "metric": "system.cpu.idle",
      "pointlist": [
        [
          1681683300000,
          77.62145685254418
        ]
      ],
      "query_index": "integer",
      "scope": "host:foo,env:test",
      "start": "integer",
      "tag_set": [],
      "unit": [
        {
          "family": "time",
          "name": "minute",
          "plural": "minutes",
          "scale_factor": 60,
          "short_name": "min"
        }
      ]
    }
  ],
  "status": "ok",
  "to_date": "integer"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python-legacy)


#####  Query timeseries points
Copy
```
                  # Required query arguments  
export from="CHANGE_ME"  
export to="CHANGE_ME"  
export query="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/query?from=${from}&to=${to}&query=${query}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Query timeseries points
```
"""
Query timeseries points returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_metrics(
        _from=int((datetime.now() + relativedelta(days=-1)).timestamp()),
        to=int(datetime.now().timestamp()),
        query="system.cpu.idle{*}",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Query timeseries points
```
# Query timeseries points returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MetricsAPI.new
p api_instance.query_metrics((Time.now + -1 * 86400).to_i, Time.now.to_i, "system.cpu.idle{*}")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Query timeseries points
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Get points from the last hour
from = Time.now - 3600
to = Time.now
query = 'system.cpu.idle{*}by{host}'

dog.get_points(query, from, to)
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Query timeseries points
```
// Query timeseries points returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMetricsApi(apiClient)
	resp, r, err := api.QueryMetrics(ctx, time.Now().AddDate(0, 0, -1).Unix(), time.Now().Unix(), "system.cpu.idle{*}")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.QueryMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.QueryMetrics`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Query timeseries points
```
// Query timeseries points returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MetricsApi;
import com.datadog.api.client.v1.model.MetricsQueryResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricsQueryResponse result =
          apiInstance.queryMetrics(
              OffsetDateTime.now().plusDays(-1).toInstant().getEpochSecond(),
              OffsetDateTime.now().toInstant().getEpochSecond(),
              "system.cpu.idle{*}");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#queryMetrics");
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

#####  Query timeseries points
```
from datadog import initialize, api
import time

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

now = int(time.time())

query = 'system.cpu.idle{*}by{host}'
print(api.Metric.query(start=now - 3600, end=now, query=query))

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Query timeseries points
```
// Query timeseries points returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .query_metrics(1636542671, 1636629071, "system.cpu.idle{*}".to_string())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Query timeseries points
```
/**
 * Query timeseries points returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MetricsApi(configuration);

const params: v1.MetricsApiQueryMetricsRequest = {
  from: Math.round(
    new Date(new Date().getTime() + -1 * 86400 * 1000).getTime() / 1000
  ),
  to: Math.round(new Date().getTime() / 1000),
  query: "system.cpu.idle{*}",
};

apiInstance
  .queryMetrics(params)
  .then((data: v1.MetricsQueryResponse) => {
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
## [List tags by metric name](https://docs.datadoghq.com/api/latest/metrics/#list-tags-by-metric-name)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#list-tags-by-metric-name-v2)


GET https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/all-tagshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/all-tagshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/all-tagshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/all-tagshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/all-tagshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/all-tagshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/all-tags
### Overview
View indexed tag key-value pairs for a given metric name over the previous hour. This endpoint requires the `metrics_read` permission.
OAuth apps require the `metrics_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#metrics) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListTagsByMetricName-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#ListTagsByMetricName-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListTagsByMetricName-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#ListTagsByMetricName-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListTagsByMetricName-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object that includes a single metric’s indexed tags.
Field
Type
Description
data
object
Object for a single metric's indexed tags.
attributes
object
Object containing the definition of a metric's tags.
tags
[string]
List of indexed tag value pairs.
id
string
The metric name for this resource.
type
enum
The metric resource type. Allowed enum values: `metrics`
default: `metrics`
```
{
  "data": {
    "attributes": {
      "tags": [
        "sport:golf",
        "sport:football",
        "animal:dog"
      ]
    },
    "id": "test.metric.latency",
    "type": "metrics"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  List tags by metric name
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/all-tags" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List tags by metric name
```
"""
List tags by metric name returns "Success" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = environ["METRIC_TAG_CONFIGURATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tags_by_metric_name(
        metric_name=METRIC_TAG_CONFIGURATION_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List tags by metric name
```
# List tags by metric name returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = ENV["METRIC_TAG_CONFIGURATION_DATA_ID"]
p api_instance.list_tags_by_metric_name(METRIC_TAG_CONFIGURATION_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List tags by metric name
```
// List tags by metric name returns "Success" response

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
	// there is a valid "metric_tag_configuration" in the system
	MetricTagConfigurationDataID := os.Getenv("METRIC_TAG_CONFIGURATION_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.ListTagsByMetricName(ctx, MetricTagConfigurationDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListTagsByMetricName`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListTagsByMetricName`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List tags by metric name
```
// List tags by metric name returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricAllTagsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    // there is a valid "metric_tag_configuration" in the system
    String METRIC_TAG_CONFIGURATION_DATA_ID = System.getenv("METRIC_TAG_CONFIGURATION_DATA_ID");

    try {
      MetricAllTagsResponse result =
          apiInstance.listTagsByMetricName(METRIC_TAG_CONFIGURATION_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listTagsByMetricName");
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

#####  List tags by metric name
```
// List tags by metric name returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "metric_tag_configuration" in the system
    let metric_tag_configuration_data_id =
        std::env::var("METRIC_TAG_CONFIGURATION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .list_tags_by_metric_name(metric_tag_configuration_data_id.clone())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List tags by metric name
```
/**
 * List tags by metric name returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

// there is a valid "metric_tag_configuration" in the system
const METRIC_TAG_CONFIGURATION_DATA_ID = process.env
  .METRIC_TAG_CONFIGURATION_DATA_ID as string;

const params: v2.MetricsApiListTagsByMetricNameRequest = {
  metricName: METRIC_TAG_CONFIGURATION_DATA_ID,
};

apiInstance
  .listTagsByMetricName(params)
  .then((data: v2.MetricAllTagsResponse) => {
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
## [List active tags and aggregations](https://docs.datadoghq.com/api/latest/metrics/#list-active-tags-and-aggregations)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#list-active-tags-and-aggregations-v2)


GET https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/active-configurationshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/active-configurationshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/active-configurationshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/active-configurationshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/active-configurationshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/active-configurationshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/active-configurations
### Overview
List tags and aggregations that are actively queried on dashboards, notebooks, monitors, the Metrics Explorer, and using the API for a given metric name. This endpoint requires the `metrics_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
#### Query Strings
Name
Type
Description
window[seconds]
integer
The number of seconds of look back (from now). Default value is 604,800 (1 week), minimum value is 7200 (2 hours), maximum value is 2,630,000 (1 month).
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetricConfigurations-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetricConfigurations-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetricConfigurations-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetricConfigurations-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListActiveMetricConfigurations-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object that includes a single metric’s actively queried tags and aggregations.
Field
Type
Description
data
object
Object for a single metric's actively queried tags and aggregations.
attributes
object
Object containing the definition of a metric's actively queried tags and aggregations.
active_aggregations
[object]
List of aggregation combinations that have been actively queried.
space [_required_]
enum
A space aggregation for use in query. Allowed enum values: `avg,max,min,sum`
time [_required_]
enum
A time aggregation for use in query. Allowed enum values: `avg,count,max,min,sum`
active_tags
[string]
List of tag keys that have been actively queried.
id
string
The metric name for this resource.
type
enum
The metric actively queried configuration resource type. Allowed enum values: `actively_queried_configurations`
default: `actively_queried_configurations`
```
{
  "data": {
    "attributes": {
      "active_aggregations": [
        {
          "space": "sum",
          "time": "sum"
        }
      ],
      "active_tags": [
        "app",
        "datacenter"
      ]
    },
    "id": "test.metric.latency",
    "type": "actively_queried_configurations"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  List active tags and aggregations
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/active-configurations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List active tags and aggregations
```
"""
List active tags and aggregations returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_active_metric_configurations(
        metric_name="static_test_metric_donotdelete",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List active tags and aggregations
```
# List active tags and aggregations returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new
p api_instance.list_active_metric_configurations("static_test_metric_donotdelete")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List active tags and aggregations
```
// List active tags and aggregations returns "Success" response

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
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.ListActiveMetricConfigurations(ctx, "static_test_metric_donotdelete", *datadogV2.NewListActiveMetricConfigurationsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListActiveMetricConfigurations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListActiveMetricConfigurations`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List active tags and aggregations
```
// List active tags and aggregations returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricSuggestedTagsAndAggregationsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricSuggestedTagsAndAggregationsResponse result =
          apiInstance.listActiveMetricConfigurations("static_test_metric_donotdelete");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listActiveMetricConfigurations");
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

#####  List active tags and aggregations
```
// List active tags and aggregations returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::ListActiveMetricConfigurationsOptionalParams;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .list_active_metric_configurations(
            "static_test_metric_donotdelete".to_string(),
            ListActiveMetricConfigurationsOptionalParams::default(),
        )
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

#####  List active tags and aggregations
```
/**
 * List active tags and aggregations returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiListActiveMetricConfigurationsRequest = {
  metricName: "static_test_metric_donotdelete",
};

apiInstance
  .listActiveMetricConfigurations(params)
  .then((data: v2.MetricSuggestedTagsAndAggregationsResponse) => {
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
## [List distinct metric volumes by metric name](https://docs.datadoghq.com/api/latest/metrics/#list-distinct-metric-volumes-by-metric-name)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#list-distinct-metric-volumes-by-metric-name-v2)


GET https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/volumeshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/volumeshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/volumeshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/volumeshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/volumeshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/volumeshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/volumes
### Overview
View distinct metrics volumes for the given metric name.
Custom metrics generated in-app from other products will return `null` for ingested volumes.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListVolumesByMetricName-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#ListVolumesByMetricName-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListVolumesByMetricName-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#ListVolumesByMetricName-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListVolumesByMetricName-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object which includes a single metric’s volume.
Field
Type
Description
data
<oneOf>
Possible response objects for a metric's volume.
Option 1
object
Object for a single metric's distinct volume.
attributes
object
Object containing the definition of a metric's distinct volume.
distinct_volume
int64
Distinct volume for the given metric.
id
string
The metric name for this resource.
type
enum
The metric distinct volume type. Allowed enum values: `distinct_metric_volumes`
default: `distinct_metric_volumes`
Option 2
object
Object for a single metric's ingested and indexed volume.
attributes
object
Object containing the definition of a metric's ingested and indexed volume.
indexed_volume
int64
Indexed volume for the given metric.
ingested_volume
int64
Ingested volume for the given metric.
id
string
The metric name for this resource.
type
enum
The metric ingested and indexed volume type. Allowed enum values: `metric_volumes`
default: `metric_volumes`
```
{
  "data": {
    "attributes": {
      "distinct_volume": 10
    },
    "id": "test.metric.latency",
    "type": "distinct_metric_volumes"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  List distinct metric volumes by metric name
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/volumes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List distinct metric volumes by metric name
```
"""
List distinct metric volumes by metric name returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_volumes_by_metric_name(
        metric_name="static_test_metric_donotdelete",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List distinct metric volumes by metric name
```
# List distinct metric volumes by metric name returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new
p api_instance.list_volumes_by_metric_name("static_test_metric_donotdelete")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List distinct metric volumes by metric name
```
// List distinct metric volumes by metric name returns "Success" response

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
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.ListVolumesByMetricName(ctx, "static_test_metric_donotdelete")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListVolumesByMetricName`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListVolumesByMetricName`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List distinct metric volumes by metric name
```
// List distinct metric volumes by metric name returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricVolumesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricVolumesResponse result =
          apiInstance.listVolumesByMetricName("static_test_metric_donotdelete");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listVolumesByMetricName");
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

#####  List distinct metric volumes by metric name
```
// List distinct metric volumes by metric name returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .list_volumes_by_metric_name("static_test_metric_donotdelete".to_string())
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

#####  List distinct metric volumes by metric name
```
/**
 * List distinct metric volumes by metric name returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiListVolumesByMetricNameRequest = {
  metricName: "static_test_metric_donotdelete",
};

apiInstance
  .listVolumesByMetricName(params)
  .then((data: v2.MetricVolumesResponse) => {
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
## [Configure tags for multiple metrics](https://docs.datadoghq.com/api/latest/metrics/#configure-tags-for-multiple-metrics)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#configure-tags-for-multiple-metrics-v2)


POST https://api.ap1.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.ap2.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.datadoghq.eu/api/v2/metrics/config/bulk-tagshttps://api.ddog-gov.com/api/v2/metrics/config/bulk-tagshttps://api.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.us3.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.us5.datadoghq.com/api/v2/metrics/config/bulk-tags
### Overview
Create and define a list of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics. Metrics are selected by passing a metric name prefix. Use the Delete method of this API path to remove tag configurations. Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app. If multiple calls include the same metric, the last configuration applied (not by submit order) is used, do not expect deterministic ordering of concurrent calls. The `exclude_tags_mode` value will set all metrics that match the prefix to the same exclusion state, metric tag configurations do not support mixed inclusion and exclusion for tags on the same metric. Can only be used with application keys of users with the `Manage Tags for Metrics` permission. This endpoint requires the `metric_tags_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
data [_required_]
object
Request object to bulk configure tags for metrics matching the given prefix.
attributes
object
Optional parameters for bulk creating metric tag configurations.
emails
[string]
A list of account emails to notify when the configuration is applied.
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags. Defaults to false.
include_actively_queried_tags_window
double
When provided, all tags that have been actively queried are configured (and, therefore, remain queryable) for each metric that matches the given prefix. Minimum value is 1 second, and maximum value is 7,776,000 seconds (90 days).
override_existing_configurations
boolean
When set to true, the configuration overrides any existing configurations for the given metric with the new set of tags in this configuration request. If false, old configurations are kept and are merged with the set of tags in this configuration request. Defaults to true.
tags
[string]
A list of tag names to apply to the configuration.
id [_required_]
string
A text prefix to match against metric names.
type [_required_]
enum
The metric bulk configure tags resource. Allowed enum values: `metric_bulk_configure_tags`
default: `metric_bulk_configure_tags`
```
{
  "data": {
    "attributes": {
      "emails": [
        "string"
      ],
      "tags": [
        "test",
        "examplemetric"
      ]
    },
    "id": "system.load.1",
    "type": "metric_bulk_configure_tags"
  }
}
```

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/metrics/#CreateBulkTagsMetricsConfiguration-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#CreateBulkTagsMetricsConfiguration-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#CreateBulkTagsMetricsConfiguration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#CreateBulkTagsMetricsConfiguration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#CreateBulkTagsMetricsConfiguration-429-v2)


Accepted
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Wrapper for a single bulk tag configuration status response.
Field
Type
Description
data
object
The status of a request to bulk configure metric tags. It contains the fields from the original request for reference.
attributes
object
Optional attributes for the status of a bulk tag configuration request.
emails
[string]
A list of account emails to notify when the configuration is applied.
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags.
status
string
The status of the request.
tags
[string]
A list of tag names to apply to the configuration.
id [_required_]
string
A text prefix to match against metric names.
type [_required_]
enum
The metric bulk configure tags resource. Allowed enum values: `metric_bulk_configure_tags`
default: `metric_bulk_configure_tags`
```
{
  "data": {
    "attributes": {
      "emails": [
        "sue@example.com",
        "bob@example.com"
      ],
      "exclude_tags_mode": false,
      "status": "Accepted",
      "tags": [
        "host",
        "pod_name",
        "is_shadow"
      ]
    },
    "id": "kafka.lag",
    "type": "metric_bulk_configure_tags"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Configure tags for multiple metrics returns "Accepted" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/config/bulk-tags" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "emails": [
        "string"
      ],
      "tags": [
        "test",
        "examplemetric"
      ]
    },
    "id": "system.load.1",
    "type": "metric_bulk_configure_tags"
  }
}
EOF  

                        
```

#####  Configure tags for multiple metrics returns "Accepted" response
```
// Configure tags for multiple metrics returns "Accepted" response

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
	// there is a valid "user" in the system
	UserDataAttributesEmail := os.Getenv("USER_DATA_ATTRIBUTES_EMAIL")

	body := datadogV2.MetricBulkTagConfigCreateRequest{
		Data: datadogV2.MetricBulkTagConfigCreate{
			Attributes: &datadogV2.MetricBulkTagConfigCreateAttributes{
				Emails: []string{
					UserDataAttributesEmail,
				},
				Tags: []string{
					"test",
					"examplemetric",
				},
			},
			Id:   "system.load.1",
			Type: datadogV2.METRICBULKCONFIGURETAGSTYPE_BULK_MANAGE_TAGS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.CreateBulkTagsMetricsConfiguration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.CreateBulkTagsMetricsConfiguration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.CreateBulkTagsMetricsConfiguration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Configure tags for multiple metrics returns "Accepted" response
```
// Configure tags for multiple metrics returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricBulkConfigureTagsType;
import com.datadog.api.client.v2.model.MetricBulkTagConfigCreate;
import com.datadog.api.client.v2.model.MetricBulkTagConfigCreateAttributes;
import com.datadog.api.client.v2.model.MetricBulkTagConfigCreateRequest;
import com.datadog.api.client.v2.model.MetricBulkTagConfigResponse;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ATTRIBUTES_EMAIL = System.getenv("USER_DATA_ATTRIBUTES_EMAIL");

    MetricBulkTagConfigCreateRequest body =
        new MetricBulkTagConfigCreateRequest()
            .data(
                new MetricBulkTagConfigCreate()
                    .attributes(
                        new MetricBulkTagConfigCreateAttributes()
                            .emails(Collections.singletonList(USER_DATA_ATTRIBUTES_EMAIL))
                            .tags(Arrays.asList("test", "examplemetric")))
                    .id("system.load.1")
                    .type(MetricBulkConfigureTagsType.BULK_MANAGE_TAGS));

    try {
      MetricBulkTagConfigResponse result = apiInstance.createBulkTagsMetricsConfiguration(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#createBulkTagsMetricsConfiguration");
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

#####  Configure tags for multiple metrics returns "Accepted" response
```
"""
Configure tags for multiple metrics returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_bulk_configure_tags_type import MetricBulkConfigureTagsType
from datadog_api_client.v2.model.metric_bulk_tag_config_create import MetricBulkTagConfigCreate
from datadog_api_client.v2.model.metric_bulk_tag_config_create_attributes import MetricBulkTagConfigCreateAttributes
from datadog_api_client.v2.model.metric_bulk_tag_config_create_request import MetricBulkTagConfigCreateRequest
from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList

# there is a valid "user" in the system
USER_DATA_ATTRIBUTES_EMAIL = environ["USER_DATA_ATTRIBUTES_EMAIL"]

body = MetricBulkTagConfigCreateRequest(
    data=MetricBulkTagConfigCreate(
        attributes=MetricBulkTagConfigCreateAttributes(
            emails=MetricBulkTagConfigEmailList(
                [
                    USER_DATA_ATTRIBUTES_EMAIL,
                ]
            ),
            tags=MetricBulkTagConfigTagNameList(
                [
                    "test",
                    "examplemetric",
                ]
            ),
        ),
        id="system.load.1",
        type=MetricBulkConfigureTagsType.BULK_MANAGE_TAGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_bulk_tags_metrics_configuration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Configure tags for multiple metrics returns "Accepted" response
```
# Configure tags for multiple metrics returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

# there is a valid "user" in the system
USER_DATA_ATTRIBUTES_EMAIL = ENV["USER_DATA_ATTRIBUTES_EMAIL"]

body = DatadogAPIClient::V2::MetricBulkTagConfigCreateRequest.new({
  data: DatadogAPIClient::V2::MetricBulkTagConfigCreate.new({
    attributes: DatadogAPIClient::V2::MetricBulkTagConfigCreateAttributes.new({
      emails: [
        USER_DATA_ATTRIBUTES_EMAIL,
      ],
      tags: [
        "test",
        "examplemetric",
      ],
    }),
    id: "system.load.1",
    type: DatadogAPIClient::V2::MetricBulkConfigureTagsType::BULK_MANAGE_TAGS,
  }),
})
p api_instance.create_bulk_tags_metrics_configuration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Configure tags for multiple metrics returns "Accepted" response
```
// Configure tags for multiple metrics returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::model::MetricBulkConfigureTagsType;
use datadog_api_client::datadogV2::model::MetricBulkTagConfigCreate;
use datadog_api_client::datadogV2::model::MetricBulkTagConfigCreateAttributes;
use datadog_api_client::datadogV2::model::MetricBulkTagConfigCreateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_attributes_email = std::env::var("USER_DATA_ATTRIBUTES_EMAIL").unwrap();
    let body = MetricBulkTagConfigCreateRequest::new(
        MetricBulkTagConfigCreate::new(
            "system.load.1".to_string(),
            MetricBulkConfigureTagsType::BULK_MANAGE_TAGS,
        )
        .attributes(
            MetricBulkTagConfigCreateAttributes::new()
                .emails(vec![user_data_attributes_email.clone()])
                .tags(vec!["test".to_string(), "examplemetric".to_string()]),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api.create_bulk_tags_metrics_configuration(body).await;
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

#####  Configure tags for multiple metrics returns "Accepted" response
```
/**
 * Configure tags for multiple metrics returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ATTRIBUTES_EMAIL = process.env
  .USER_DATA_ATTRIBUTES_EMAIL as string;

const params: v2.MetricsApiCreateBulkTagsMetricsConfigurationRequest = {
  body: {
    data: {
      attributes: {
        emails: [USER_DATA_ATTRIBUTES_EMAIL],
        tags: ["test", "examplemetric"],
      },
      id: "system.load.1",
      type: "metric_bulk_configure_tags",
    },
  },
};

apiInstance
  .createBulkTagsMetricsConfiguration(params)
  .then((data: v2.MetricBulkTagConfigResponse) => {
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
## [Delete tags for multiple metrics](https://docs.datadoghq.com/api/latest/metrics/#delete-tags-for-multiple-metrics)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#delete-tags-for-multiple-metrics-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.ap2.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.datadoghq.eu/api/v2/metrics/config/bulk-tagshttps://api.ddog-gov.com/api/v2/metrics/config/bulk-tagshttps://api.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.us3.datadoghq.com/api/v2/metrics/config/bulk-tagshttps://api.us5.datadoghq.com/api/v2/metrics/config/bulk-tags
### Overview
Delete all custom lists of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics. Metrics are selected by passing a metric name prefix. Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app. Can only be used with application keys of users with the `Manage Tags for Metrics` permission. This endpoint requires the `metric_tags_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Field
Type
Description
data [_required_]
object
Request object to bulk delete all tag configurations for metrics matching the given prefix.
attributes
object
Optional parameters for bulk deleting metric tag configurations.
emails
[string]
A list of account emails to notify when the configuration is applied.
id [_required_]
string
A text prefix to match against metric names.
type [_required_]
enum
The metric bulk configure tags resource. Allowed enum values: `metric_bulk_configure_tags`
default: `metric_bulk_configure_tags`
```
{
  "data": {
    "attributes": {
      "emails": [
        "sue@example.com",
        "bob@example.com"
      ]
    },
    "id": "kafka.lag",
    "type": "metric_bulk_configure_tags"
  }
}
```

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/metrics/#DeleteBulkTagsMetricsConfiguration-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#DeleteBulkTagsMetricsConfiguration-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#DeleteBulkTagsMetricsConfiguration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#DeleteBulkTagsMetricsConfiguration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#DeleteBulkTagsMetricsConfiguration-429-v2)


Accepted
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Wrapper for a single bulk tag configuration status response.
Field
Type
Description
data
object
The status of a request to bulk configure metric tags. It contains the fields from the original request for reference.
attributes
object
Optional attributes for the status of a bulk tag configuration request.
emails
[string]
A list of account emails to notify when the configuration is applied.
exclude_tags_mode
boolean
When set to true, the configuration will exclude the configured tags and include any other submitted tags. When set to false, the configuration will include the configured tags and exclude any other submitted tags.
status
string
The status of the request.
tags
[string]
A list of tag names to apply to the configuration.
id [_required_]
string
A text prefix to match against metric names.
type [_required_]
enum
The metric bulk configure tags resource. Allowed enum values: `metric_bulk_configure_tags`
default: `metric_bulk_configure_tags`
```
{
  "data": {
    "attributes": {
      "emails": [
        "sue@example.com",
        "bob@example.com"
      ],
      "exclude_tags_mode": false,
      "status": "Accepted",
      "tags": [
        "host",
        "pod_name",
        "is_shadow"
      ]
    },
    "id": "kafka.lag",
    "type": "metric_bulk_configure_tags"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Delete tags for multiple metrics
Copy
```
                  # Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/config/bulk-tags" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "kafka.lag",
    "type": "metric_bulk_configure_tags"
  }
}
EOF  

                
```

#####  Delete tags for multiple metrics
```
"""
Delete tags for multiple metrics returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_bulk_configure_tags_type import MetricBulkConfigureTagsType
from datadog_api_client.v2.model.metric_bulk_tag_config_delete import MetricBulkTagConfigDelete
from datadog_api_client.v2.model.metric_bulk_tag_config_delete_attributes import MetricBulkTagConfigDeleteAttributes
from datadog_api_client.v2.model.metric_bulk_tag_config_delete_request import MetricBulkTagConfigDeleteRequest
from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList

body = MetricBulkTagConfigDeleteRequest(
    data=MetricBulkTagConfigDelete(
        attributes=MetricBulkTagConfigDeleteAttributes(
            emails=MetricBulkTagConfigEmailList(
                [
                    "sue@example.com",
                    "bob@example.com",
                ]
            ),
        ),
        id="kafka.lag",
        type=MetricBulkConfigureTagsType.BULK_MANAGE_TAGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.delete_bulk_tags_metrics_configuration(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete tags for multiple metrics
```
# Delete tags for multiple metrics returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new

body = DatadogAPIClient::V2::MetricBulkTagConfigDeleteRequest.new({
  data: DatadogAPIClient::V2::MetricBulkTagConfigDelete.new({
    attributes: DatadogAPIClient::V2::MetricBulkTagConfigDeleteAttributes.new({
      emails: [
        "sue@example.com",
        "bob@example.com",
      ],
    }),
    id: "kafka.lag",
    type: DatadogAPIClient::V2::MetricBulkConfigureTagsType::BULK_MANAGE_TAGS,
  }),
})
p api_instance.delete_bulk_tags_metrics_configuration(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete tags for multiple metrics
```
// Delete tags for multiple metrics returns "Accepted" response

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
	body := datadogV2.MetricBulkTagConfigDeleteRequest{
		Data: datadogV2.MetricBulkTagConfigDelete{
			Attributes: &datadogV2.MetricBulkTagConfigDeleteAttributes{
				Emails: []string{
					"sue@example.com",
					"bob@example.com",
				},
			},
			Id:   "kafka.lag",
			Type: datadogV2.METRICBULKCONFIGURETAGSTYPE_BULK_MANAGE_TAGS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.DeleteBulkTagsMetricsConfiguration(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.DeleteBulkTagsMetricsConfiguration`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.DeleteBulkTagsMetricsConfiguration`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete tags for multiple metrics
```
// Delete tags for multiple metrics returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricBulkConfigureTagsType;
import com.datadog.api.client.v2.model.MetricBulkTagConfigDelete;
import com.datadog.api.client.v2.model.MetricBulkTagConfigDeleteAttributes;
import com.datadog.api.client.v2.model.MetricBulkTagConfigDeleteRequest;
import com.datadog.api.client.v2.model.MetricBulkTagConfigResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    MetricBulkTagConfigDeleteRequest body =
        new MetricBulkTagConfigDeleteRequest()
            .data(
                new MetricBulkTagConfigDelete()
                    .attributes(
                        new MetricBulkTagConfigDeleteAttributes()
                            .emails(Arrays.asList("sue@example.com", "bob@example.com")))
                    .id("kafka.lag")
                    .type(MetricBulkConfigureTagsType.BULK_MANAGE_TAGS));

    try {
      MetricBulkTagConfigResponse result = apiInstance.deleteBulkTagsMetricsConfiguration(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#deleteBulkTagsMetricsConfiguration");
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

#####  Delete tags for multiple metrics
```
// Delete tags for multiple metrics returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;
use datadog_api_client::datadogV2::model::MetricBulkConfigureTagsType;
use datadog_api_client::datadogV2::model::MetricBulkTagConfigDelete;
use datadog_api_client::datadogV2::model::MetricBulkTagConfigDeleteAttributes;
use datadog_api_client::datadogV2::model::MetricBulkTagConfigDeleteRequest;

#[tokio::main]
async fn main() {
    let body = MetricBulkTagConfigDeleteRequest::new(
        MetricBulkTagConfigDelete::new(
            "kafka.lag".to_string(),
            MetricBulkConfigureTagsType::BULK_MANAGE_TAGS,
        )
        .attributes(MetricBulkTagConfigDeleteAttributes::new().emails(vec![
            "sue@example.com".to_string(),
            "bob@example.com".to_string(),
        ])),
    );
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api.delete_bulk_tags_metrics_configuration(body).await;
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

#####  Delete tags for multiple metrics
```
/**
 * Delete tags for multiple metrics returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiDeleteBulkTagsMetricsConfigurationRequest = {
  body: {
    data: {
      attributes: {
        emails: ["sue@example.com", "bob@example.com"],
      },
      id: "kafka.lag",
      type: "metric_bulk_configure_tags",
    },
  },
};

apiInstance
  .deleteBulkTagsMetricsConfiguration(params)
  .then((data: v2.MetricBulkTagConfigResponse) => {
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
## [Tag Configuration Cardinality Estimator](https://docs.datadoghq.com/api/latest/metrics/#tag-configuration-cardinality-estimator)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#tag-configuration-cardinality-estimator-v2)


GET https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/estimatehttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/estimatehttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/estimatehttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/estimatehttps://api.datadoghq.com/api/v2/metrics/{metric_name}/estimatehttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/estimatehttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/estimate
### Overview
Returns the estimated cardinality for a metric with a given tag, percentile and number of aggregations configuration using Metrics without Limits™.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
#### Query Strings
Name
Type
Description
filter[groups]
string
Filtered tag keys that the metric is configured to query with.
filter[hours_ago]
integer
The number of hours of look back (from now) to estimate cardinality with. If unspecified, it defaults to 0 hours.
filter[num_aggregations]
integer
Deprecated. Number of aggregations has no impact on volume.
filter[pct]
boolean
A boolean, for distribution metrics only, to estimate cardinality if the metric includes additional percentile aggregators.
filter[timespan_h]
integer
A window, in hours, from the look back to estimate cardinality with. The minimum and default is 1 hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#EstimateMetricsOutputSeries-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#EstimateMetricsOutputSeries-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#EstimateMetricsOutputSeries-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#EstimateMetricsOutputSeries-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#EstimateMetricsOutputSeries-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object that includes metric cardinality estimates.
Field
Type
Description
data
object
Object for a metric cardinality estimate.
attributes
object
Object containing the definition of a metric estimate attribute.
estimate_type
enum
Estimate type based on the queried configuration. By default, `count_or_gauge` is returned. `distribution` is returned for distribution metrics without percentiles enabled. Lastly, `percentile` is returned if `filter[pct]=true` is queried with a distribution metric. Allowed enum values: `count_or_gauge,distribution,percentile`
default: `count_or_gauge`
estimated_at
date-time
Timestamp when the cardinality estimate was requested.
estimated_output_series
int64
Estimated cardinality of the metric based on the queried configuration.
id
string
The metric name for this resource.
type
enum
The metric estimate resource type. Allowed enum values: `metric_cardinality_estimate`
default: `metric_cardinality_estimate`
```
{
  "data": {
    "attributes": {
      "estimate_type": "distribution",
      "estimated_at": "2022-04-27T09:48:37.463835Z",
      "estimated_output_series": 50
    },
    "id": "test.metric.latency",
    "type": "metric_cardinality_estimate"
  }
}
```

Copy
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Tag Configuration Cardinality Estimator
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/estimate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Tag Configuration Cardinality Estimator
```
"""
Tag Configuration Cardinality Estimator returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.estimate_metrics_output_series(
        metric_name="system.cpu.idle",
        filter_groups="app,host",
        filter_num_aggregations=4,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Tag Configuration Cardinality Estimator
```
# Tag Configuration Cardinality Estimator returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new
opts = {
  filter_groups: "app,host",
  filter_num_aggregations: 4,
}
p api_instance.estimate_metrics_output_series("system.cpu.idle", opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Tag Configuration Cardinality Estimator
```
// Tag Configuration Cardinality Estimator returns "Success" response

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
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.EstimateMetricsOutputSeries(ctx, "system.cpu.idle", *datadogV2.NewEstimateMetricsOutputSeriesOptionalParameters().WithFilterGroups("app,host").WithFilterNumAggregations(4))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.EstimateMetricsOutputSeries`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.EstimateMetricsOutputSeries`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Tag Configuration Cardinality Estimator
```
// Tag Configuration Cardinality Estimator returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.api.MetricsApi.EstimateMetricsOutputSeriesOptionalParameters;
import com.datadog.api.client.v2.model.MetricEstimateResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricEstimateResponse result =
          apiInstance.estimateMetricsOutputSeries(
              "system.cpu.idle",
              new EstimateMetricsOutputSeriesOptionalParameters()
                  .filterGroups("app,host")
                  .filterNumAggregations(4));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#estimateMetricsOutputSeries");
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

#####  Tag Configuration Cardinality Estimator
```
// Tag Configuration Cardinality Estimator returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::EstimateMetricsOutputSeriesOptionalParams;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .estimate_metrics_output_series(
            "system.cpu.idle".to_string(),
            EstimateMetricsOutputSeriesOptionalParams::default()
                .filter_groups("app,host".to_string())
                .filter_num_aggregations(4),
        )
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

#####  Tag Configuration Cardinality Estimator
```
/**
 * Tag Configuration Cardinality Estimator returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiEstimateMetricsOutputSeriesRequest = {
  metricName: "system.cpu.idle",
  filterGroups: "app,host",
  filterNumAggregations: 4,
};

apiInstance
  .estimateMetricsOutputSeries(params)
  .then((data: v2.MetricEstimateResponse) => {
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
## [Related Assets to a Metric](https://docs.datadoghq.com/api/latest/metrics/#related-assets-to-a-metric)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#related-assets-to-a-metric-v2)


GET https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/assetshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/assetshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/assetshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/assetshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/assetshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/assetshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/assets
### Overview
Returns dashboards, monitors, notebooks, and SLOs that a metric is stored in, if any. Updated every 24 hours.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#ListMetricAssets-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#ListMetricAssets-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#ListMetricAssets-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#ListMetricAssets-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#ListMetricAssets-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object that includes related dashboards, monitors, notebooks, and SLOs.
Field
Type
Description
data
object
Metric assets response data.
id [_required_]
string
The metric name for this resource.
relationships
object
Relationships to assets related to the metric.
dashboards
object
An object containing the list of dashboards that can be referenced in the `included` data.
data
[object]
A list of dashboards that can be referenced in the `included` data.
id
string
The related dashboard's ID.
type
enum
Dashboard resource type. Allowed enum values: `dashboards`
monitors
object
A object containing the list of monitors that can be referenced in the `included` data.
data
[object]
A list of monitors that can be referenced in the `included` data.
id
string
The related monitor's ID.
type
enum
Monitor resource type. Allowed enum values: `monitors`
notebooks
object
An object containing the list of notebooks that can be referenced in the `included` data.
data
[object]
A list of notebooks that can be referenced in the `included` data.
id
string
The related notebook's ID.
type
enum
Notebook resource type. Allowed enum values: `notebooks`
slos
object
An object containing a list of SLOs that can be referenced in the `included` data.
data
[object]
A list of SLOs that can be referenced in the `included` data.
id
string
The SLO ID.
type
enum
SLO resource type. Allowed enum values: `slos`
type [_required_]
enum
The metric resource type. Allowed enum values: `metrics`
default: `metrics`
included
[ <oneOf>]
Array of objects related to the metric assets.
Option 1
object
A dashboard object with title and popularity.
attributes
object
Attributes related to the dashboard, including title, popularity, and url.
popularity
double
Value from 0 to 5 that ranks popularity of the dashboard.
tags
[string]
List of tag keys used in the asset.
title
string
Title of the asset.
url
string
URL path of the asset.
id [_required_]
string
The related dashboard's ID.
type [_required_]
enum
Dashboard resource type. Allowed enum values: `dashboards`
Option 2
object
A monitor object with title.
attributes
object
Assets related to the object, including title, url, and tags.
tags
[string]
List of tag keys used in the asset.
title
string
Title of the asset.
url
string
URL path of the asset.
id [_required_]
string
The related monitor's ID.
type [_required_]
enum
Monitor resource type. Allowed enum values: `monitors`
Option 3
object
A notebook object with title.
attributes
object
Assets related to the object, including title, url, and tags.
tags
[string]
List of tag keys used in the asset.
title
string
Title of the asset.
url
string
URL path of the asset.
id [_required_]
string
The related notebook's ID.
type [_required_]
enum
Notebook resource type. Allowed enum values: `notebooks`
Option 4
object
A SLO object with title.
attributes
object
Assets related to the object, including title, url, and tags.
tags
[string]
List of tag keys used in the asset.
title
string
Title of the asset.
url
string
URL path of the asset.
id [_required_]
string
The SLO ID.
type [_required_]
enum
SLO resource type. Allowed enum values: `slos`
```
{
  "data": {
    "id": "test.metric.latency",
    "relationships": {
      "dashboards": {
        "data": [
          {
            "id": "xxx-yyy-zzz",
            "type": "dashboards"
          }
        ]
      },
      "monitors": {
        "data": [
          {
            "id": "1775073",
            "type": "monitors"
          }
        ]
      },
      "notebooks": {
        "data": [
          {
            "id": "12345",
            "type": "notebooks"
          }
        ]
      },
      "slos": {
        "data": [
          {
            "id": "9ffef113b389520db54391d67d652dfb",
            "type": "slos"
          }
        ]
      }
    },
    "type": "metrics"
  },
  "included": [
    {
      "attributes": {
        "popularity": "number",
        "tags": [
          "env",
          "service",
          "host",
          "datacenter"
        ],
        "title": "string",
        "url": "string"
      },
      "id": "xxx-yyy-zzz",
      "type": "dashboards"
    }
  ]
}
```

Copy
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
API error response.
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Related Assets to a Metric
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/assets" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Related Assets to a Metric
```
"""
Related Assets to a Metric returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_metric_assets(
        metric_name="system.cpu.user",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Related Assets to a Metric
```
# Related Assets to a Metric returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new
p api_instance.list_metric_assets("system.cpu.user")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Related Assets to a Metric
```
// Related Assets to a Metric returns "Success" response

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
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.ListMetricAssets(ctx, "system.cpu.user")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.ListMetricAssets`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.ListMetricAssets`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Related Assets to a Metric
```
// Related Assets to a Metric returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricAssetsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricAssetsResponse result = apiInstance.listMetricAssets("system.cpu.user");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#listMetricAssets");
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

#####  Related Assets to a Metric
```
// Related Assets to a Metric returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api.list_metric_assets("system.cpu.user".to_string()).await;
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

#####  Related Assets to a Metric
```
/**
 * Related Assets to a Metric returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiListMetricAssetsRequest = {
  metricName: "system.cpu.user",
};

apiInstance
  .listMetricAssets(params)
  .then((data: v2.MetricAssetsResponse) => {
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
## [Get tag key cardinality details](https://docs.datadoghq.com/api/latest/metrics/#get-tag-key-cardinality-details)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/metrics/#get-tag-key-cardinality-details-v2)


GET https://api.ap1.datadoghq.com/api/v2/metrics/{metric_name}/tag-cardinalitieshttps://api.ap2.datadoghq.com/api/v2/metrics/{metric_name}/tag-cardinalitieshttps://api.datadoghq.eu/api/v2/metrics/{metric_name}/tag-cardinalitieshttps://api.ddog-gov.com/api/v2/metrics/{metric_name}/tag-cardinalitieshttps://api.datadoghq.com/api/v2/metrics/{metric_name}/tag-cardinalitieshttps://api.us3.datadoghq.com/api/v2/metrics/{metric_name}/tag-cardinalitieshttps://api.us5.datadoghq.com/api/v2/metrics/{metric_name}/tag-cardinalities
### Overview
Returns the cardinality details of tags for a specific metric. This endpoint requires the `metrics_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
metric_name [_required_]
string
The name of the metric.
### Response
  * [200](https://docs.datadoghq.com/api/latest/metrics/#GetMetricTagCardinalityDetails-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/metrics/#GetMetricTagCardinalityDetails-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/metrics/#GetMetricTagCardinalityDetails-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/metrics/#GetMetricTagCardinalityDetails-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/metrics/#GetMetricTagCardinalityDetails-429-v2)


Success
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


Response object that includes an array of objects representing the cardinality details of a metric’s tags.
Field
Type
Description
data
[object]
A list of tag cardinalities associated with the given metric.
attributes
object
An object containing properties related to the tag key
cardinality_delta
int64
This describes the recent change in the tag keys cardinality
id
string
The name of the tag key.
type
string
This describes the endpoint action.
default: `tag_cardinality`
meta
object
Response metadata object.
metric_name
string
The name of metric for which the tag cardinalities are returned. This matches the metric name provided in the request.
```
{
  "data": [
    {
      "attributes": {
        "cardinality_delta": "integer"
      },
      "id": "string",
      "type": "string"
    }
  ],
  "meta": {
    "metric_name": "string"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/metrics/)
  * [Example](https://docs.datadoghq.com/api/latest/metrics/)


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
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/metrics/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/metrics/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/metrics/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/metrics/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/metrics/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/metrics/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/metrics/?code-lang=typescript)


#####  Get tag key cardinality details
Copy
```
                  # Path parameters  
export metric_name="dist.http.endpoint.request"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/metrics/${metric_name}/tag-cardinalities" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get tag key cardinality details
```
"""
Get tag key cardinality details returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.get_metric_tag_cardinality_details(
        metric_name="metric_name",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get tag key cardinality details
```
# Get tag key cardinality details returns "Success" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MetricsAPI.new
p api_instance.get_metric_tag_cardinality_details("metric_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get tag key cardinality details
```
// Get tag key cardinality details returns "Success" response

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
	api := datadogV2.NewMetricsApi(apiClient)
	resp, r, err := api.GetMetricTagCardinalityDetails(ctx, "metric_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MetricsApi.GetMetricTagCardinalityDetails`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MetricsApi.GetMetricTagCardinalityDetails`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get tag key cardinality details
```
// Get tag key cardinality details returns "Success" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MetricsApi;
import com.datadog.api.client.v2.model.MetricTagCardinalitiesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MetricsApi apiInstance = new MetricsApi(defaultClient);

    try {
      MetricTagCardinalitiesResponse result =
          apiInstance.getMetricTagCardinalityDetails("dist.http.endpoint.request");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getMetricTagCardinalityDetails");
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

#####  Get tag key cardinality details
```
// Get tag key cardinality details returns "Success" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_metrics::MetricsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MetricsAPI::with_config(configuration);
    let resp = api
        .get_metric_tag_cardinality_details("metric_name".to_string())
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

#####  Get tag key cardinality details
```
/**
 * Get tag key cardinality details returns "Success" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MetricsApi(configuration);

const params: v2.MetricsApiGetMetricTagCardinalityDetailsRequest = {
  metricName: "metric_name",
};

apiInstance
  .getMetricTagCardinalityDetails(params)
  .then((data: v2.MetricTagCardinalitiesResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2acd63f6-6e49-43e3-af1c-ff70bd439b42&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4a9fc478-4f3f-4485-9e3a-ae35804a236e&pt=Metrics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmetrics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2acd63f6-6e49-43e3-af1c-ff70bd439b42&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4a9fc478-4f3f-4485-9e3a-ae35804a236e&pt=Metrics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmetrics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=acb6f3e5-2482-4b8e-aaa5-e7d9c6955245&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Metrics&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmetrics%2F&r=&lt=33234&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=222373)
