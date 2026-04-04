# Source: https://docs.datadoghq.com/api/latest/service-level-objectives

# Service Level Objectives
[Service Level Objectives](https://docs.datadoghq.com/monitors/service_level_objectives/#configuration) (or SLOs) are a key part of the site reliability engineering toolkit. SLOs provide a framework for defining clear targets around application performance, which ultimately help teams provide a consistent customer experience, balance feature development with platform stability, and improve communication with internal and external users.
## [Create an SLO object](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-an-slo-object)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-an-slo-object-v1)


POST https://api.ap1.datadoghq.com/api/v1/slohttps://api.ap2.datadoghq.com/api/v1/slohttps://api.datadoghq.eu/api/v1/slohttps://api.ddog-gov.com/api/v1/slohttps://api.datadoghq.com/api/v1/slohttps://api.us3.datadoghq.com/api/v1/slohttps://api.us5.datadoghq.com/api/v1/slo
### Overview
Create a service level objective object. This endpoint requires the `slos_write` permission.
OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Request
#### Body Data (required)
Service level objective request object.
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


Field
Type
Description
description
string
A user-defined description of the service level objective.
Always included in service level objective responses (but may be `null`). Optional in create/update requests.
groups
[string]
A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.
Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one.
monitor_ids
[integer]
A list of monitor IDs that defines the scope of a monitor service level objective. **Required if type is`monitor`**.
name [_required_]
string
The name of the service level objective object.
query
object
A metric-based SLO. **Required if type is`metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.
denominator [_required_]
string
A Datadog metric query for total (valid) events.
numerator [_required_]
string
A Datadog metric query for good events.
sli_specification
<oneOf>
A generic SLI specification. This is currently used for time-slice SLOs only.
Option 1
object
A time-slice SLI specification.
time_slice [_required_]
object
The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.
comparator [_required_]
enum
The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`
query [_required_]
object
The queries and formula used to calculate the SLI value.
formulas [_required_]
[object]
A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.
formula [_required_]
string
The formula string, which is an expression involving named queries.
queries [_required_]
[ <oneOf>]
A list of queries that are used to calculate the SLI value.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
query_interval_seconds
enum
The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`
threshold [_required_]
double
The threshold value to which each SLI value will be compared.
tags
[string]
A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.
target_threshold
double
The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.
thresholds [_required_]
[object]
The thresholds (timeframes and associated targets) for this service level objective object.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
timeframe
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
type [_required_]
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
warning_threshold
double
The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.
#####  Create a time-slice SLO object returns "OK" response
```
{
  "type": "time_slice",
  "description": "string",
  "name": "Example-Service-Level-Objective",
  "sli_specification": {
    "time_slice": {
      "query": {
        "formulas": [
          {
            "formula": "query1"
          }
        ],
        "queries": [
          {
            "data_source": "metrics",
            "name": "query1",
            "query": "trace.servlet.request{env:prod}"
          }
        ]
      },
      "comparator": ">",
      "threshold": 5
    }
  },
  "tags": [
    "env:prod"
  ],
  "thresholds": [
    {
      "target": 97.0,
      "target_display": "97.0",
      "timeframe": "7d",
      "warning": 98,
      "warning_display": "98.0"
    }
  ],
  "timeframe": "7d",
  "target_threshold": 97.0,
  "warning_threshold": 98
}
```

Copy
#####  Create an SLO object returns "OK" response
```
{
  "type": "metric",
  "description": "string",
  "groups": [
    "env:test",
    "role:mysql"
  ],
  "monitor_ids": [],
  "name": "Example-Service-Level-Objective",
  "query": {
    "denominator": "sum:httpservice.hits{!code:3xx}.as_count()",
    "numerator": "sum:httpservice.hits{code:2xx}.as_count()"
  },
  "tags": [
    "env:prod",
    "app:core"
  ],
  "thresholds": [
    {
      "target": 97.0,
      "target_display": "97.0",
      "timeframe": "7d",
      "warning": 98,
      "warning_display": "98.0"
    }
  ],
  "timeframe": "7d",
  "target_threshold": 97.0,
  "warning_threshold": 98
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLO-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLO-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLO-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLO-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A response with one or more service level objective.
Field
Type
Description
data
[object]
An array of service level objective objects.
created_at
int64
Creation timestamp (UNIX time in seconds)
Always included in service level objective responses.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
A user-defined description of the service level objective.
Always included in service level objective responses (but may be `null`). Optional in create/update requests.
groups
[string]
A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.
Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one.
id
string
A unique identifier for the service level objective object.
Always included in service level objective responses.
modified_at
int64
Modification timestamp (UNIX time in seconds)
Always included in service level objective responses.
monitor_ids
[integer]
A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is`monitor`**.
monitor_tags
[string]
The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field).
name [_required_]
string
The name of the service level objective object.
query
object
A metric-based SLO. **Required if type is`metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.
denominator [_required_]
string
A Datadog metric query for total (valid) events.
numerator [_required_]
string
A Datadog metric query for good events.
sli_specification
<oneOf>
A generic SLI specification. This is currently used for time-slice SLOs only.
Option 1
object
A time-slice SLI specification.
time_slice [_required_]
object
The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.
comparator [_required_]
enum
The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`
query [_required_]
object
The queries and formula used to calculate the SLI value.
formulas [_required_]
[object]
A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.
formula [_required_]
string
The formula string, which is an expression involving named queries.
queries [_required_]
[ <oneOf>]
A list of queries that are used to calculate the SLI value.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
query_interval_seconds
enum
The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`
threshold [_required_]
double
The threshold value to which each SLI value will be compared.
tags
[string]
A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.
target_threshold
double
The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.
thresholds [_required_]
[object]
The thresholds (timeframes and associated targets) for this service level objective object.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
timeframe
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
type [_required_]
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
warning_threshold
double
The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.
errors
[string]
An array of error messages. Each endpoint documents how/whether this field is used.
metadata
object
The metadata object containing additional information about the list of SLOs.
page
object
The object containing information about the pages of the list of SLOs.
total_count
int64
The total number of resources that could be retrieved ignoring the parameters and filters in the request.
total_filtered_count
int64
The total number of resources that match the parameters and filters in the request. This attribute can be used by a client to determine the total number of pages.
```
{
  "data": [
    {
      "created_at": "integer",
      "creator": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "description": "string",
      "groups": [
        "env:prod",
        "role:mysql"
      ],
      "id": "string",
      "modified_at": "integer",
      "monitor_ids": [],
      "monitor_tags": [],
      "name": "Custom Metric SLO",
      "query": {
        "denominator": "sum:my.custom.metric{*}.as_count()",
        "numerator": "sum:my.custom.metric{type:good}.as_count()"
      },
      "sli_specification": {
        "time_slice": {
          "comparator": ">",
          "query": {
            "formulas": [
              {
                "formula": "query1 - default_zero(query2)"
              }
            ],
            "queries": [
              []
            ]
          },
          "query_interval_seconds": 300,
          "threshold": 5
        }
      },
      "tags": [
        "env:prod",
        "app:core"
      ],
      "target_threshold": 99.9,
      "thresholds": [
        {
          "target": 99.9,
          "target_display": "99.9",
          "timeframe": "30d",
          "warning": 90,
          "warning_display": "90.0"
        }
      ],
      "timeframe": "30d",
      "type": "metric",
      "warning_threshold": 99.95
    }
  ],
  "errors": [],
  "metadata": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby-legacy)


#####  Create a time-slice SLO object returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "type": "time_slice",
  "description": "string",
  "name": "Example-Service-Level-Objective",
  "sli_specification": {
    "time_slice": {
      "query": {
        "formulas": [
          {
            "formula": "query1"
          }
        ],
        "queries": [
          {
            "data_source": "metrics",
            "name": "query1",
            "query": "trace.servlet.request{env:prod}"
          }
        ]
      },
      "comparator": ">",
      "threshold": 5
    }
  },
  "tags": [
    "env:prod"
  ],
  "thresholds": [
    {
      "target": 97.0,
      "target_display": "97.0",
      "timeframe": "7d",
      "warning": 98,
      "warning_display": "98.0"
    }
  ],
  "timeframe": "7d",
  "target_threshold": 97.0,
  "warning_threshold": 98
}
EOF  

                        
```

#####  Create an SLO object returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "type": "metric",
  "description": "string",
  "groups": [
    "env:test",
    "role:mysql"
  ],
  "monitor_ids": [],
  "name": "Example-Service-Level-Objective",
  "query": {
    "denominator": "sum:httpservice.hits{!code:3xx}.as_count()",
    "numerator": "sum:httpservice.hits{code:2xx}.as_count()"
  },
  "tags": [
    "env:prod",
    "app:core"
  ],
  "thresholds": [
    {
      "target": 97.0,
      "target_display": "97.0",
      "timeframe": "7d",
      "warning": 98,
      "warning_display": "98.0"
    }
  ],
  "timeframe": "7d",
  "target_threshold": 97.0,
  "warning_threshold": 98
}
EOF  

                        
```

#####  Create a time-slice SLO object returns "OK" response 
```
// Create a time-slice SLO object returns "OK" response

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
	body := datadogV1.ServiceLevelObjectiveRequest{
		Type:        datadogV1.SLOTYPE_TIME_SLICE,
		Description: *datadog.NewNullableString(datadog.PtrString("string")),
		Name:        "Example-Service-Level-Objective",
		SliSpecification: &datadogV1.SLOSliSpec{
			SLOTimeSliceSpec: &datadogV1.SLOTimeSliceSpec{
				TimeSlice: datadogV1.SLOTimeSliceCondition{
					Query: datadogV1.SLOTimeSliceQuery{
						Formulas: []datadogV1.SLOFormula{
							{
								Formula: "query1",
							},
						},
						Queries: []datadogV1.SLODataSourceQueryDefinition{
							datadogV1.SLODataSourceQueryDefinition{
								FormulaAndFunctionMetricQueryDefinition: &datadogV1.FormulaAndFunctionMetricQueryDefinition{
									DataSource: datadogV1.FORMULAANDFUNCTIONMETRICDATASOURCE_METRICS,
									Name:       "query1",
									Query:      "trace.servlet.request{env:prod}",
								}},
						},
					},
					Comparator: datadogV1.SLOTIMESLICECOMPARATOR_GREATER,
					Threshold:  5,
				},
			}},
		Tags: []string{
			"env:prod",
		},
		Thresholds: []datadogV1.SLOThreshold{
			{
				Target:         97.0,
				TargetDisplay:  datadog.PtrString("97.0"),
				Timeframe:      datadogV1.SLOTIMEFRAME_SEVEN_DAYS,
				Warning:        datadog.PtrFloat64(98),
				WarningDisplay: datadog.PtrString("98.0"),
			},
		},
		Timeframe:        datadogV1.SLOTIMEFRAME_SEVEN_DAYS.Ptr(),
		TargetThreshold:  datadog.PtrFloat64(97.0),
		WarningThreshold: datadog.PtrFloat64(98),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.CreateSLO(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.CreateSLO`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.CreateSLO`:\n%s\n", responseContent)
}

```

Copy
#####  Create an SLO object returns "OK" response 
```
// Create an SLO object returns "OK" response

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
	body := datadogV1.ServiceLevelObjectiveRequest{
		Type:        datadogV1.SLOTYPE_METRIC,
		Description: *datadog.NewNullableString(datadog.PtrString("string")),
		Groups: []string{
			"env:test",
			"role:mysql",
		},
		MonitorIds: []int64{},
		Name:       "Example-Service-Level-Objective",
		Query: &datadogV1.ServiceLevelObjectiveQuery{
			Denominator: "sum:httpservice.hits{!code:3xx}.as_count()",
			Numerator:   "sum:httpservice.hits{code:2xx}.as_count()",
		},
		Tags: []string{
			"env:prod",
			"app:core",
		},
		Thresholds: []datadogV1.SLOThreshold{
			{
				Target:         97.0,
				TargetDisplay:  datadog.PtrString("97.0"),
				Timeframe:      datadogV1.SLOTIMEFRAME_SEVEN_DAYS,
				Warning:        datadog.PtrFloat64(98),
				WarningDisplay: datadog.PtrString("98.0"),
			},
		},
		Timeframe:        datadogV1.SLOTIMEFRAME_SEVEN_DAYS.Ptr(),
		TargetThreshold:  datadog.PtrFloat64(97.0),
		WarningThreshold: datadog.PtrFloat64(98),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.CreateSLO(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.CreateSLO`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.CreateSLO`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a time-slice SLO object returns "OK" response 
```
// Create a time-slice SLO object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.FormulaAndFunctionMetricDataSource;
import com.datadog.api.client.v1.model.FormulaAndFunctionMetricQueryDefinition;
import com.datadog.api.client.v1.model.SLODataSourceQueryDefinition;
import com.datadog.api.client.v1.model.SLOFormula;
import com.datadog.api.client.v1.model.SLOListResponse;
import com.datadog.api.client.v1.model.SLOSliSpec;
import com.datadog.api.client.v1.model.SLOThreshold;
import com.datadog.api.client.v1.model.SLOTimeSliceComparator;
import com.datadog.api.client.v1.model.SLOTimeSliceCondition;
import com.datadog.api.client.v1.model.SLOTimeSliceQuery;
import com.datadog.api.client.v1.model.SLOTimeSliceSpec;
import com.datadog.api.client.v1.model.SLOTimeframe;
import com.datadog.api.client.v1.model.SLOType;
import com.datadog.api.client.v1.model.ServiceLevelObjectiveRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    ServiceLevelObjectiveRequest body =
        new ServiceLevelObjectiveRequest()
            .type(SLOType.TIME_SLICE)
            .description("string")
            .name("Example-Service-Level-Objective")
            .sliSpecification(
                new SLOSliSpec(
                    new SLOTimeSliceSpec()
                        .timeSlice(
                            new SLOTimeSliceCondition()
                                .query(
                                    new SLOTimeSliceQuery()
                                        .formulas(
                                            Collections.singletonList(
                                                new SLOFormula().formula("query1")))
                                        .queries(
                                            Collections.singletonList(
                                                new SLODataSourceQueryDefinition(
                                                    new FormulaAndFunctionMetricQueryDefinition()
                                                        .dataSource(
                                                            FormulaAndFunctionMetricDataSource
                                                                .METRICS)
                                                        .name("query1")
                                                        .query(
                                                            "trace.servlet.request{env:prod}")))))
                                .comparator(SLOTimeSliceComparator.GREATER)
                                .threshold(5.0))))
            .tags(Collections.singletonList("env:prod"))
            .thresholds(
                Collections.singletonList(
                    new SLOThreshold()
                        .target(97.0)
                        .targetDisplay("97.0")
                        .timeframe(SLOTimeframe.SEVEN_DAYS)
                        .warning(98.0)
                        .warningDisplay("98.0")))
            .timeframe(SLOTimeframe.SEVEN_DAYS)
            .targetThreshold(97.0)
            .warningThreshold(98.0);

    try {
      SLOListResponse result = apiInstance.createSLO(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#createSLO");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create an SLO object returns "OK" response 
```
// Create an SLO object returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.SLOListResponse;
import com.datadog.api.client.v1.model.SLOThreshold;
import com.datadog.api.client.v1.model.SLOTimeframe;
import com.datadog.api.client.v1.model.SLOType;
import com.datadog.api.client.v1.model.ServiceLevelObjectiveQuery;
import com.datadog.api.client.v1.model.ServiceLevelObjectiveRequest;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    ServiceLevelObjectiveRequest body =
        new ServiceLevelObjectiveRequest()
            .type(SLOType.METRIC)
            .description("string")
            .groups(Arrays.asList("env:test", "role:mysql"))
            .name("Example-Service-Level-Objective")
            .query(
                new ServiceLevelObjectiveQuery()
                    .denominator("sum:httpservice.hits{!code:3xx}.as_count()")
                    .numerator("sum:httpservice.hits{code:2xx}.as_count()"))
            .tags(Arrays.asList("env:prod", "app:core"))
            .thresholds(
                Collections.singletonList(
                    new SLOThreshold()
                        .target(97.0)
                        .targetDisplay("97.0")
                        .timeframe(SLOTimeframe.SEVEN_DAYS)
                        .warning(98.0)
                        .warningDisplay("98.0")))
            .timeframe(SLOTimeframe.SEVEN_DAYS)
            .targetThreshold(97.0)
            .warningThreshold(98.0);

    try {
      SLOListResponse result = apiInstance.createSLO(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#createSLO");
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

#####  Create an SLO object returns "OK" response
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Create a new SLO
thresholds = [
  {"timeframe": "7d", "target": 95},
  {"timeframe": "30d", "target": 95, "warning": 97},
]
tags = ["app:webserver", "frontend"]
api.ServiceLevelObjective.create(
    type="metric",
    name="Custom Metric SLO",
    description="SLO tracking custom service SLO",
    query={
        "numerator": "sum:my.custom.metric{type:good}.as_count()",
        "denominator": "sum:my.custom.metric{*}.as_count()"
    },
    tags=tags,
    thresholds=thresholds
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Create a time-slice SLO object returns "OK" response 
```
"""
Create a time-slice SLO object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.service_level_objective_request import ServiceLevelObjectiveRequest
from datadog_api_client.v1.model.slo_formula import SLOFormula
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_time_slice_comparator import SLOTimeSliceComparator
from datadog_api_client.v1.model.slo_time_slice_condition import SLOTimeSliceCondition
from datadog_api_client.v1.model.slo_time_slice_query import SLOTimeSliceQuery
from datadog_api_client.v1.model.slo_time_slice_spec import SLOTimeSliceSpec
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

body = ServiceLevelObjectiveRequest(
    type=SLOType.TIME_SLICE,
    description="string",
    name="Example-Service-Level-Objective",
    sli_specification=SLOTimeSliceSpec(
        time_slice=SLOTimeSliceCondition(
            query=SLOTimeSliceQuery(
                formulas=[
                    SLOFormula(
                        formula="query1",
                    ),
                ],
                queries=[
                    FormulaAndFunctionMetricQueryDefinition(
                        data_source=FormulaAndFunctionMetricDataSource.METRICS,
                        name="query1",
                        query="trace.servlet.request{env:prod}",
                    ),
                ],
            ),
            comparator=SLOTimeSliceComparator.GREATER,
            threshold=5.0,
        ),
    ),
    tags=[
        "env:prod",
    ],
    thresholds=[
        SLOThreshold(
            target=97.0,
            target_display="97.0",
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=98.0,
            warning_display="98.0",
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=97.0,
    warning_threshold=98.0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo(body=body)

    print(response)

```

Copy
#####  Create an SLO object returns "OK" response 
```
"""
Create an SLO object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
from datadog_api_client.v1.model.service_level_objective_request import ServiceLevelObjectiveRequest
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

body = ServiceLevelObjectiveRequest(
    type=SLOType.METRIC,
    description="string",
    groups=[
        "env:test",
        "role:mysql",
    ],
    monitor_ids=[],
    name="Example-Service-Level-Objective",
    query=ServiceLevelObjectiveQuery(
        denominator="sum:httpservice.hits{!code:3xx}.as_count()",
        numerator="sum:httpservice.hits{code:2xx}.as_count()",
    ),
    tags=[
        "env:prod",
        "app:core",
    ],
    thresholds=[
        SLOThreshold(
            target=97.0,
            target_display="97.0",
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=98.0,
            warning_display="98.0",
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=97.0,
    warning_threshold=98.0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an SLO object returns "OK" response
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Create a new SLO
thresholds = [
  { timeframe: '7d', target: 95 },
  { timeframe: '30d', target: 95, warning: 97 }
]
tags = ['app:webserver', 'frontend']
dog.create_service_level_objective(
  type: 'metric',
  name: 'Custom Metric SLO',
  description: 'SLO tracking custom service SLO',
  numerator: 'sum:my.custom.metric{type:good}.as_count()',
  denominator: 'sum:my.custom.metric{*}.as_count()',
  tags: tags,
  thresholds: thresholds
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a time-slice SLO object returns "OK" response 
```
# Create a time-slice SLO object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

body = DatadogAPIClient::V1::ServiceLevelObjectiveRequest.new({
  type: DatadogAPIClient::V1::SLOType::TIME_SLICE,
  description: "string",
  name: "Example-Service-Level-Objective",
  sli_specification: DatadogAPIClient::V1::SLOTimeSliceSpec.new({
    time_slice: DatadogAPIClient::V1::SLOTimeSliceCondition.new({
      query: DatadogAPIClient::V1::SLOTimeSliceQuery.new({
        formulas: [
          DatadogAPIClient::V1::SLOFormula.new({
            formula: "query1",
          }),
        ],
        queries: [
          DatadogAPIClient::V1::FormulaAndFunctionMetricQueryDefinition.new({
            data_source: DatadogAPIClient::V1::FormulaAndFunctionMetricDataSource::METRICS,
            name: "query1",
            query: "trace.servlet.request{env:prod}",
          }),
        ],
      }),
      comparator: DatadogAPIClient::V1::SLOTimeSliceComparator::GREATER,
      threshold: 5,
    }),
  }),
  tags: [
    "env:prod",
  ],
  thresholds: [
    DatadogAPIClient::V1::SLOThreshold.new({
      target: 97.0,
      target_display: "97.0",
      timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
      warning: 98,
      warning_display: "98.0",
    }),
  ],
  timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
  target_threshold: 97.0,
  warning_threshold: 98,
})
p api_instance.create_slo(body)

```

Copy
#####  Create an SLO object returns "OK" response 
```
# Create an SLO object returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

body = DatadogAPIClient::V1::ServiceLevelObjectiveRequest.new({
  type: DatadogAPIClient::V1::SLOType::METRIC,
  description: "string",
  groups: [
    "env:test",
    "role:mysql",
  ],
  monitor_ids: [],
  name: "Example-Service-Level-Objective",
  query: DatadogAPIClient::V1::ServiceLevelObjectiveQuery.new({
    denominator: "sum:httpservice.hits{!code:3xx}.as_count()",
    numerator: "sum:httpservice.hits{code:2xx}.as_count()",
  }),
  tags: [
    "env:prod",
    "app:core",
  ],
  thresholds: [
    DatadogAPIClient::V1::SLOThreshold.new({
      target: 97.0,
      target_display: "97.0",
      timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
      warning: 98,
      warning_display: "98.0",
    }),
  ],
  timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
  target_threshold: 97.0,
  warning_threshold: 98,
})
p api_instance.create_slo(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a time-slice SLO object returns "OK" response 
```
// Create a time-slice SLO object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;
use datadog_api_client::datadogV1::model::FormulaAndFunctionMetricDataSource;
use datadog_api_client::datadogV1::model::FormulaAndFunctionMetricQueryDefinition;
use datadog_api_client::datadogV1::model::SLODataSourceQueryDefinition;
use datadog_api_client::datadogV1::model::SLOFormula;
use datadog_api_client::datadogV1::model::SLOSliSpec;
use datadog_api_client::datadogV1::model::SLOThreshold;
use datadog_api_client::datadogV1::model::SLOTimeSliceComparator;
use datadog_api_client::datadogV1::model::SLOTimeSliceCondition;
use datadog_api_client::datadogV1::model::SLOTimeSliceQuery;
use datadog_api_client::datadogV1::model::SLOTimeSliceSpec;
use datadog_api_client::datadogV1::model::SLOTimeframe;
use datadog_api_client::datadogV1::model::SLOType;
use datadog_api_client::datadogV1::model::ServiceLevelObjectiveRequest;

#[tokio::main]
async fn main() {
    let body = ServiceLevelObjectiveRequest::new(
        "Example-Service-Level-Objective".to_string(),
        vec![SLOThreshold::new(97.0, SLOTimeframe::SEVEN_DAYS)
            .target_display("97.0".to_string())
            .warning(98.0 as f64)
            .warning_display("98.0".to_string())],
        SLOType::TIME_SLICE,
    )
    .description(Some("string".to_string()))
    .sli_specification(SLOSliSpec::SLOTimeSliceSpec(Box::new(
        SLOTimeSliceSpec::new(SLOTimeSliceCondition::new(
            SLOTimeSliceComparator::GREATER,
            SLOTimeSliceQuery::new(
                vec![SLOFormula::new("query1".to_string())],
                vec![
                    SLODataSourceQueryDefinition::FormulaAndFunctionMetricQueryDefinition(
                        Box::new(FormulaAndFunctionMetricQueryDefinition::new(
                            FormulaAndFunctionMetricDataSource::METRICS,
                            "query1".to_string(),
                            "trace.servlet.request{env:prod}".to_string(),
                        )),
                    ),
                ],
            ),
            5.0,
        )),
    )))
    .tags(vec!["env:prod".to_string()])
    .target_threshold(97.0 as f64)
    .timeframe(SLOTimeframe::SEVEN_DAYS)
    .warning_threshold(98.0 as f64);
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.create_slo(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create an SLO object returns "OK" response 
```
// Create an SLO object returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;
use datadog_api_client::datadogV1::model::SLOThreshold;
use datadog_api_client::datadogV1::model::SLOTimeframe;
use datadog_api_client::datadogV1::model::SLOType;
use datadog_api_client::datadogV1::model::ServiceLevelObjectiveQuery;
use datadog_api_client::datadogV1::model::ServiceLevelObjectiveRequest;

#[tokio::main]
async fn main() {
    let body = ServiceLevelObjectiveRequest::new(
        "Example-Service-Level-Objective".to_string(),
        vec![SLOThreshold::new(97.0, SLOTimeframe::SEVEN_DAYS)
            .target_display("97.0".to_string())
            .warning(98.0 as f64)
            .warning_display("98.0".to_string())],
        SLOType::METRIC,
    )
    .description(Some("string".to_string()))
    .groups(vec!["env:test".to_string(), "role:mysql".to_string()])
    .monitor_ids(vec![])
    .query(ServiceLevelObjectiveQuery::new(
        "sum:httpservice.hits{!code:3xx}.as_count()".to_string(),
        "sum:httpservice.hits{code:2xx}.as_count()".to_string(),
    ))
    .tags(vec!["env:prod".to_string(), "app:core".to_string()])
    .target_threshold(97.0 as f64)
    .timeframe(SLOTimeframe::SEVEN_DAYS)
    .warning_threshold(98.0 as f64);
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.create_slo(body).await;
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

#####  Create a time-slice SLO object returns "OK" response 
```
/**
 * Create a time-slice SLO object returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

const params: v1.ServiceLevelObjectivesApiCreateSLORequest = {
  body: {
    type: "time_slice",
    description: "string",
    name: "Example-Service-Level-Objective",
    sliSpecification: {
      timeSlice: {
        query: {
          formulas: [
            {
              formula: "query1",
            },
          ],
          queries: [
            {
              dataSource: "metrics",
              name: "query1",
              query: "trace.servlet.request{env:prod}",
            },
          ],
        },
        comparator: ">",
        threshold: 5,
      },
    },
    tags: ["env:prod"],
    thresholds: [
      {
        target: 97.0,
        targetDisplay: "97.0",
        timeframe: "7d",
        warning: 98,
        warningDisplay: "98.0",
      },
    ],
    timeframe: "7d",
    targetThreshold: 97.0,
    warningThreshold: 98,
  },
};

apiInstance
  .createSLO(params)
  .then((data: v1.SLOListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create an SLO object returns "OK" response 
```
/**
 * Create an SLO object returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

const params: v1.ServiceLevelObjectivesApiCreateSLORequest = {
  body: {
    type: "metric",
    description: "string",
    groups: ["env:test", "role:mysql"],
    monitorIds: [],
    name: "Example-Service-Level-Objective",
    query: {
      denominator: "sum:httpservice.hits{!code:3xx}.as_count()",
      numerator: "sum:httpservice.hits{code:2xx}.as_count()",
    },
    tags: ["env:prod", "app:core"],
    thresholds: [
      {
        target: 97.0,
        targetDisplay: "97.0",
        timeframe: "7d",
        warning: 98,
        warningDisplay: "98.0",
      },
    ],
    timeframe: "7d",
    targetThreshold: 97.0,
    warningThreshold: 98,
  },
};

apiInstance
  .createSLO(params)
  .then((data: v1.SLOListResponse) => {
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
## [Search for SLOs](https://docs.datadoghq.com/api/latest/service-level-objectives/#search-for-slos)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#search-for-slos-v1)


GET https://api.ap1.datadoghq.com/api/v1/slo/searchhttps://api.ap2.datadoghq.com/api/v1/slo/searchhttps://api.datadoghq.eu/api/v1/slo/searchhttps://api.ddog-gov.com/api/v1/slo/searchhttps://api.datadoghq.com/api/v1/slo/searchhttps://api.us3.datadoghq.com/api/v1/slo/searchhttps://api.us5.datadoghq.com/api/v1/slo/search
### Overview
Get a list of service level objective objects for your organization. This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
query
string
The query string to filter results based on SLO names. Some examples of queries include `service:<service-name>` and `<slo-name>`.
page[size]
integer
The number of files to return in the response `[default=10]`.
page[number]
integer
The identifier of the first page to return. This parameter is used for the pagination feature `[default=0]`.
include_facets
boolean
Whether or not to return facet information in the response `[default=false]`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#SearchSLO-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#SearchSLO-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#SearchSLO-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#SearchSLO-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A search SLO response containing results from the search query.
Field
Type
Description
data
object
Data from search SLO response.
attributes
object
Attributes
facets
object
Facets
all_tags
[object]
All tags associated with an SLO.
count
int64
Count
name
string
Facet
creator_name
[object]
Creator of an SLO.
count
int64
Count
name
string
Facet
env_tags
[object]
Tags with the `env` tag key.
count
int64
Count
name
string
Facet
service_tags
[object]
Tags with the `service` tag key.
count
int64
Count
name
string
Facet
slo_type
[object]
Type of SLO.
count
int64
Count
name
double
Facet
target
[object]
SLO Target
count
int64
Count
name
double
Facet
team_tags
[object]
Tags with the `team` tag key.
count
int64
Count
name
string
Facet
timeframe
[object]
Timeframes of SLOs.
count
int64
Count
name
string
Facet
slos
[object]
SLOs
data
object
A service level objective ID and attributes.
attributes
object
A service level objective object includes a service level indicator, thresholds for one or more timeframes, and metadata (`name`, `description`, and `tags`).
all_tags
[string]
A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty).
created_at
int64
Creation timestamp (UNIX time in seconds)
Always included in service level objective responses.
creator
object
The creator of the SLO
email
string
Email of the creator.
id
int64
User ID of the creator.
name
string
Name of the creator.
description
string
A user-defined description of the service level objective.
Always included in service level objective responses (but may be `null`). Optional in create/update requests.
env_tags
[string]
Tags with the `env` tag key.
groups
[string]
A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective. Included in service level objective responses if it is not empty.
modified_at
int64
Modification timestamp (UNIX time in seconds)
Always included in service level objective responses.
monitor_ids
[integer]
A list of monitor ids that defines the scope of a monitor service level objective.
name
string
The name of the service level objective object.
overall_status
[object]
calculated status and error budget remaining.
error
string
Error message if SLO status or error budget could not be calculated.
error_budget_remaining
double
Remaining error budget of the SLO in percentage.
indexed_at
int64
timestamp (UNIX time in seconds) of when the SLO status and error budget were calculated.
raw_error_budget_remaining
object
Error budget remaining for an SLO.
unit
string
Error budget remaining unit.
value
double
Error budget remaining value.
span_precision
int64
The amount of decimal places the SLI value is accurate to.
state
enum
State of the SLO. Allowed enum values: `breached,warning,ok,no_data`
status
double
The status of the SLO.
target
double
The target of the SLO.
timeframe
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
query
object
A metric-based SLO. **Required if type is`metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.
denominator
string
A Datadog metric query for total (valid) events.
metrics
[string]
Metric names used in the query's numerator and denominator. This field will return null and will be implemented in the next version of this endpoint.
numerator
string
A Datadog metric query for good events.
service_tags
[string]
Tags with the `service` tag key.
slo_type
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
status
object
Status of the SLO's primary timeframe.
calculation_error
string
Error message if SLO status or error budget could not be calculated.
error_budget_remaining
double
Remaining error budget of the SLO in percentage.
indexed_at
int64
timestamp (UNIX time in seconds) of when the SLO status and error budget were calculated.
raw_error_budget_remaining
object
Error budget remaining for an SLO.
unit
string
Error budget remaining unit.
value
double
Error budget remaining value.
sli
double
The current service level indicator (SLI) of the SLO, also known as 'status'. This is a percentage value from 0-100 (inclusive).
span_precision
int64
The number of decimal places the SLI value is accurate to.
state
enum
State of the SLO. Allowed enum values: `breached,warning,ok,no_data`
team_tags
[string]
Tags with the `team` tag key.
thresholds
[object]
The thresholds (timeframes and associated targets) for this service level objective object.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Allowed enum values: `7d,30d,90d`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
id
string
A unique identifier for the service level objective object.
Always included in service level objective responses.
type
string
The type of the object, must be `slo`.
type
string
Type of service level objective result.
links
object
Pagination links.
first
string
Link to last page.
last
string
Link to first page.
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
Searches metadata returned by the API.
pagination
object
Pagination metadata returned by the API.
first_number
int64
The first number.
last_number
int64
The last number.
next_number
int64
The next number.
number
int64
The page number.
prev_number
int64
The previous page number.
size
int64
The size of the response.
total
int64
The total number of SLOs in the response.
type
string
Type of pagination.
```
{
  "data": {
    "attributes": {
      "facets": {
        "all_tags": [
          {
            "count": "integer",
            "name": "string"
          }
        ],
        "creator_name": [
          {
            "count": "integer",
            "name": "string"
          }
        ],
        "env_tags": [
          {
            "count": "integer",
            "name": "string"
          }
        ],
        "service_tags": [
          {
            "count": "integer",
            "name": "string"
          }
        ],
        "slo_type": [
          {
            "count": "integer",
            "name": "number"
          }
        ],
        "target": [
          {
            "count": "integer",
            "name": "number"
          }
        ],
        "team_tags": [
          {
            "count": "integer",
            "name": "string"
          }
        ],
        "timeframe": [
          {
            "count": "integer",
            "name": "string"
          }
        ]
      },
      "slos": [
        {
          "data": {
            "attributes": {
              "all_tags": [
                "env:prod",
                "app:core"
              ],
              "created_at": "integer",
              "creator": {
                "email": "string",
                "id": "integer",
                "name": "string"
              },
              "description": "string",
              "env_tags": [],
              "groups": [
                "env:prod",
                "role:mysql"
              ],
              "modified_at": "integer",
              "monitor_ids": [],
              "name": "Custom Metric SLO",
              "overall_status": [
                {
                  "error": "string",
                  "error_budget_remaining": 100,
                  "indexed_at": 1662496260,
                  "raw_error_budget_remaining": {
                    "unit": "requests",
                    "value": 60
                  },
                  "span_precision": 2,
                  "state": "ok",
                  "status": 100,
                  "target": 99,
                  "timeframe": "30d"
                }
              ],
              "query": {
                "denominator": "sum:my.custom.metric{*}.as_count()",
                "metrics": [
                  "my.custom.metric",
                  "my.other.custom.metric"
                ],
                "numerator": "sum:my.custom.metric{type:good}.as_count()"
              },
              "service_tags": [],
              "slo_type": "metric",
              "status": {
                "calculation_error": "string",
                "error_budget_remaining": 100,
                "indexed_at": 1662496260,
                "raw_error_budget_remaining": {
                  "unit": "requests",
                  "value": 60
                },
                "sli": 100,
                "span_precision": 2,
                "state": "ok"
              },
              "team_tags": [],
              "thresholds": [
                {
                  "target": 99.9,
                  "target_display": "99.9",
                  "timeframe": "30d",
                  "warning": 90,
                  "warning_display": "90.0"
                }
              ]
            },
            "id": "string",
            "type": "string"
          }
        }
      ]
    },
    "type": ""
  },
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "pagination": {
      "first_number": "integer",
      "last_number": "integer",
      "next_number": "integer",
      "number": "integer",
      "prev_number": "integer",
      "size": "integer",
      "total": "integer",
      "type": "string"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)


#####  Search for SLOs
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/search" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Search for SLOs
```
"""
Search for SLOs returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_NAME = environ["SLO_DATA_0_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.search_slo(
        query=SLO_DATA_0_NAME,
        page_size=20,
        page_number=0,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search for SLOs
```
# Search for SLOs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_NAME = ENV["SLO_DATA_0_NAME"]
opts = {
  query: SLO_DATA_0_NAME,
  page_size: 20,
  page_number: 0,
}
p api_instance.search_slo(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search for SLOs
```
// Search for SLOs returns "OK" response

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
	// there is a valid "slo" in the system
	SloData0Name := os.Getenv("SLO_DATA_0_NAME")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.SearchSLO(ctx, *datadogV1.NewSearchSLOOptionalParameters().WithQuery(SloData0Name).WithPageSize(20).WithPageNumber(0))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.SearchSLO`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.SearchSLO`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Search for SLOs
```
// Search for SLOs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi.SearchSLOOptionalParameters;
import com.datadog.api.client.v1.model.SearchSLOResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_NAME = System.getenv("SLO_DATA_0_NAME");

    try {
      SearchSLOResponse result =
          apiInstance.searchSLO(
              new SearchSLOOptionalParameters()
                  .query(SLO_DATA_0_NAME)
                  .pageSize(20L)
                  .pageNumber(0L));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#searchSLO");
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

#####  Search for SLOs
```
// Search for SLOs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::SearchSLOOptionalParams;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_name = std::env::var("SLO_DATA_0_NAME").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api
        .search_slo(
            SearchSLOOptionalParams::default()
                .query(slo_data_0_name.clone())
                .page_size(20)
                .page_number(0),
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

#####  Search for SLOs
```
/**
 * Search for SLOs returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_NAME = process.env.SLO_DATA_0_NAME as string;

const params: v1.ServiceLevelObjectivesApiSearchSLORequest = {
  query: SLO_DATA_0_NAME,
  pageSize: 20,
  pageNumber: 0,
};

apiInstance
  .searchSLO(params)
  .then((data: v1.SearchSLOResponse) => {
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
## [Get all SLOs](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-all-slos)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-all-slos-v1)


GET https://api.ap1.datadoghq.com/api/v1/slohttps://api.ap2.datadoghq.com/api/v1/slohttps://api.datadoghq.eu/api/v1/slohttps://api.ddog-gov.com/api/v1/slohttps://api.datadoghq.com/api/v1/slohttps://api.us3.datadoghq.com/api/v1/slohttps://api.us5.datadoghq.com/api/v1/slo
### Overview
Get a list of service level objective objects for your organization. This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
ids
string
A comma separated list of the IDs of the service level objectives objects.
query
string
The query string to filter results based on SLO names.
tags_query
string
The query string to filter results based on a single SLO tag.
metrics_query
string
The query string to filter results based on SLO numerator and denominator.
limit
integer
The number of SLOs to return in the response.
offset
integer
The specific offset to use as the beginning of the returned response.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#ListSLOs-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#ListSLOs-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#ListSLOs-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#ListSLOs-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#ListSLOs-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A response with one or more service level objective.
Field
Type
Description
data
[object]
An array of service level objective objects.
created_at
int64
Creation timestamp (UNIX time in seconds)
Always included in service level objective responses.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
A user-defined description of the service level objective.
Always included in service level objective responses (but may be `null`). Optional in create/update requests.
groups
[string]
A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.
Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one.
id
string
A unique identifier for the service level objective object.
Always included in service level objective responses.
modified_at
int64
Modification timestamp (UNIX time in seconds)
Always included in service level objective responses.
monitor_ids
[integer]
A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is`monitor`**.
monitor_tags
[string]
The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field).
name [_required_]
string
The name of the service level objective object.
query
object
A metric-based SLO. **Required if type is`metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.
denominator [_required_]
string
A Datadog metric query for total (valid) events.
numerator [_required_]
string
A Datadog metric query for good events.
sli_specification
<oneOf>
A generic SLI specification. This is currently used for time-slice SLOs only.
Option 1
object
A time-slice SLI specification.
time_slice [_required_]
object
The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.
comparator [_required_]
enum
The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`
query [_required_]
object
The queries and formula used to calculate the SLI value.
formulas [_required_]
[object]
A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.
formula [_required_]
string
The formula string, which is an expression involving named queries.
queries [_required_]
[ <oneOf>]
A list of queries that are used to calculate the SLI value.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
query_interval_seconds
enum
The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`
threshold [_required_]
double
The threshold value to which each SLI value will be compared.
tags
[string]
A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.
target_threshold
double
The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.
thresholds [_required_]
[object]
The thresholds (timeframes and associated targets) for this service level objective object.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
timeframe
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
type [_required_]
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
warning_threshold
double
The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.
errors
[string]
An array of error messages. Each endpoint documents how/whether this field is used.
metadata
object
The metadata object containing additional information about the list of SLOs.
page
object
The object containing information about the pages of the list of SLOs.
total_count
int64
The total number of resources that could be retrieved ignoring the parameters and filters in the request.
total_filtered_count
int64
The total number of resources that match the parameters and filters in the request. This attribute can be used by a client to determine the total number of pages.
```
{
  "data": [
    {
      "created_at": "integer",
      "creator": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "description": "string",
      "groups": [
        "env:prod",
        "role:mysql"
      ],
      "id": "string",
      "modified_at": "integer",
      "monitor_ids": [],
      "monitor_tags": [],
      "name": "Custom Metric SLO",
      "query": {
        "denominator": "sum:my.custom.metric{*}.as_count()",
        "numerator": "sum:my.custom.metric{type:good}.as_count()"
      },
      "sli_specification": {
        "time_slice": {
          "comparator": ">",
          "query": {
            "formulas": [
              {
                "formula": "query1 - default_zero(query2)"
              }
            ],
            "queries": [
              []
            ]
          },
          "query_interval_seconds": 300,
          "threshold": 5
        }
      },
      "tags": [
        "env:prod",
        "app:core"
      ],
      "target_threshold": 99.9,
      "thresholds": [
        {
          "target": 99.9,
          "target_display": "99.9",
          "timeframe": "30d",
          "warning": 90,
          "warning_display": "90.0"
        }
      ],
      "timeframe": "30d",
      "type": "metric",
      "warning_threshold": 99.95
    }
  ],
  "errors": [],
  "metadata": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python-legacy)


#####  Get all SLOs
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all SLOs
```
"""
Get all SLOs returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.list_slos(
        ids=SLO_DATA_0_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all SLOs
```
# Get all SLOs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
opts = {
  ids: SLO_DATA_0_ID,
}
p api_instance.list_slos(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all SLOs
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Search with a list of IDs
slo_ids = ['<YOUR_SLO_ID>']
dog.search_service_level_objective(slo_ids: slo_ids, offset: 0)

# Search with a query on your SLO Name.
query = 'my team'
dog.search_service_level_objective(query: query, offset: 0)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all SLOs
```
// Get all SLOs returns "OK" response

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
	// there is a valid "slo" in the system
	SloData0ID := os.Getenv("SLO_DATA_0_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.ListSLOs(ctx, *datadogV1.NewListSLOsOptionalParameters().WithIds(SloData0ID))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.ListSLOs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.ListSLOs`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all SLOs
```
// Get all SLOs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi.ListSLOsOptionalParameters;
import com.datadog.api.client.v1.model.SLOListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");

    try {
      SLOListResponse result =
          apiInstance.listSLOs(new ListSLOsOptionalParameters().ids(SLO_DATA_0_ID));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#listSLOs");
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

#####  Get all SLOs
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Search with a list of IDs
slo_ids = ["<YOUR_SLO_ID>", "<YOUR_SLO_ID>"]

api.ServiceLevelObjective.get_all(ids=slo_ids, offset=0)

# Search with a query on your SLO Name.
query = "my team"

api.ServiceLevelObjective.get_all(query=query, offset=0)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get all SLOs
```
// Get all SLOs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ListSLOsOptionalParams;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api
        .list_slos(ListSLOsOptionalParams::default().ids(slo_data_0_id.clone()))
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

#####  Get all SLOs
```
/**
 * Get all SLOs returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;

const params: v1.ServiceLevelObjectivesApiListSLOsRequest = {
  ids: SLO_DATA_0_ID,
};

apiInstance
  .listSLOs(params)
  .then((data: v1.SLOListResponse) => {
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
## [Update an SLO](https://docs.datadoghq.com/api/latest/service-level-objectives/#update-an-slo)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#update-an-slo-v1)


PUT https://api.ap1.datadoghq.com/api/v1/slo/{slo_id}https://api.ap2.datadoghq.com/api/v1/slo/{slo_id}https://api.datadoghq.eu/api/v1/slo/{slo_id}https://api.ddog-gov.com/api/v1/slo/{slo_id}https://api.datadoghq.com/api/v1/slo/{slo_id}https://api.us3.datadoghq.com/api/v1/slo/{slo_id}https://api.us5.datadoghq.com/api/v1/slo/{slo_id}
### Overview
Update the specified service level objective object. This endpoint requires the `slos_write` permission.
OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
slo_id [_required_]
string
The ID of the service level objective object.
### Request
#### Body Data (required)
The edited service level objective request object.
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


Field
Type
Description
created_at
int64
Creation timestamp (UNIX time in seconds)
Always included in service level objective responses.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
A user-defined description of the service level objective.
Always included in service level objective responses (but may be `null`). Optional in create/update requests.
groups
[string]
A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.
Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one.
id
string
A unique identifier for the service level objective object.
Always included in service level objective responses.
modified_at
int64
Modification timestamp (UNIX time in seconds)
Always included in service level objective responses.
monitor_ids
[integer]
A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is`monitor`**.
monitor_tags
[string]
The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field).
name [_required_]
string
The name of the service level objective object.
query
object
A metric-based SLO. **Required if type is`metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.
denominator [_required_]
string
A Datadog metric query for total (valid) events.
numerator [_required_]
string
A Datadog metric query for good events.
sli_specification
<oneOf>
A generic SLI specification. This is currently used for time-slice SLOs only.
Option 1
object
A time-slice SLI specification.
time_slice [_required_]
object
The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.
comparator [_required_]
enum
The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`
query [_required_]
object
The queries and formula used to calculate the SLI value.
formulas [_required_]
[object]
A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.
formula [_required_]
string
The formula string, which is an expression involving named queries.
queries [_required_]
[ <oneOf>]
A list of queries that are used to calculate the SLI value.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
query_interval_seconds
enum
The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`
threshold [_required_]
double
The threshold value to which each SLI value will be compared.
tags
[string]
A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.
target_threshold
double
The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.
thresholds [_required_]
[object]
The thresholds (timeframes and associated targets) for this service level objective object.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
timeframe
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
type [_required_]
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
warning_threshold
double
The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.
```
{
  "type": "metric",
  "name": "Custom Metric SLO",
  "thresholds": [
    {
      "target": 97.0,
      "timeframe": "7d",
      "warning": 98.0
    }
  ],
  "timeframe": "7d",
  "target_threshold": 97.0,
  "warning_threshold": 98,
  "query": {
    "numerator": "sum:httpservice.hits{code:2xx}.as_count()",
    "denominator": "sum:httpservice.hits{!code:3xx}.as_count()"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#UpdateSLO-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#UpdateSLO-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#UpdateSLO-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#UpdateSLO-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#UpdateSLO-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A response with one or more service level objective.
Field
Type
Description
data
[object]
An array of service level objective objects.
created_at
int64
Creation timestamp (UNIX time in seconds)
Always included in service level objective responses.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
A user-defined description of the service level objective.
Always included in service level objective responses (but may be `null`). Optional in create/update requests.
groups
[string]
A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.
Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one.
id
string
A unique identifier for the service level objective object.
Always included in service level objective responses.
modified_at
int64
Modification timestamp (UNIX time in seconds)
Always included in service level objective responses.
monitor_ids
[integer]
A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is`monitor`**.
monitor_tags
[string]
The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field).
name [_required_]
string
The name of the service level objective object.
query
object
A metric-based SLO. **Required if type is`metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.
denominator [_required_]
string
A Datadog metric query for total (valid) events.
numerator [_required_]
string
A Datadog metric query for good events.
sli_specification
<oneOf>
A generic SLI specification. This is currently used for time-slice SLOs only.
Option 1
object
A time-slice SLI specification.
time_slice [_required_]
object
The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.
comparator [_required_]
enum
The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`
query [_required_]
object
The queries and formula used to calculate the SLI value.
formulas [_required_]
[object]
A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.
formula [_required_]
string
The formula string, which is an expression involving named queries.
queries [_required_]
[ <oneOf>]
A list of queries that are used to calculate the SLI value.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
query_interval_seconds
enum
The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`
threshold [_required_]
double
The threshold value to which each SLI value will be compared.
tags
[string]
A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.
target_threshold
double
The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.
thresholds [_required_]
[object]
The thresholds (timeframes and associated targets) for this service level objective object.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
timeframe
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
type [_required_]
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
warning_threshold
double
The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.
errors
[string]
An array of error messages. Each endpoint documents how/whether this field is used.
metadata
object
The metadata object containing additional information about the list of SLOs.
page
object
The object containing information about the pages of the list of SLOs.
total_count
int64
The total number of resources that could be retrieved ignoring the parameters and filters in the request.
total_filtered_count
int64
The total number of resources that match the parameters and filters in the request. This attribute can be used by a client to determine the total number of pages.
```
{
  "data": [
    {
      "created_at": "integer",
      "creator": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "description": "string",
      "groups": [
        "env:prod",
        "role:mysql"
      ],
      "id": "string",
      "modified_at": "integer",
      "monitor_ids": [],
      "monitor_tags": [],
      "name": "Custom Metric SLO",
      "query": {
        "denominator": "sum:my.custom.metric{*}.as_count()",
        "numerator": "sum:my.custom.metric{type:good}.as_count()"
      },
      "sli_specification": {
        "time_slice": {
          "comparator": ">",
          "query": {
            "formulas": [
              {
                "formula": "query1 - default_zero(query2)"
              }
            ],
            "queries": [
              []
            ]
          },
          "query_interval_seconds": 300,
          "threshold": 5
        }
      },
      "tags": [
        "env:prod",
        "app:core"
      ],
      "target_threshold": 99.9,
      "thresholds": [
        {
          "target": 99.9,
          "target_display": "99.9",
          "timeframe": "30d",
          "warning": 90,
          "warning_display": "90.0"
        }
      ],
      "timeframe": "30d",
      "type": "metric",
      "warning_threshold": 99.95
    }
  ],
  "errors": [],
  "metadata": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)


#####  Update an SLO returns "OK" response
Copy
```
                          # Path parameters  
export slo_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "type": "metric",
  "name": "Custom Metric SLO",
  "thresholds": [
    {
      "target": 97.0,
      "timeframe": "7d",
      "warning": 98.0
    }
  ],
  "timeframe": "7d",
  "target_threshold": 97.0,
  "warning_threshold": 98,
  "query": {
    "numerator": "sum:httpservice.hits{code:2xx}.as_count()",
    "denominator": "sum:httpservice.hits{!code:3xx}.as_count()"
  }
}
EOF  

                        
```

#####  Update an SLO returns "OK" response
```
// Update an SLO returns "OK" response

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
	// there is a valid "slo" in the system
	SloData0ID := os.Getenv("SLO_DATA_0_ID")
	SloData0Name := os.Getenv("SLO_DATA_0_NAME")

	body := datadogV1.ServiceLevelObjective{
		Type: datadogV1.SLOTYPE_METRIC,
		Name: SloData0Name,
		Thresholds: []datadogV1.SLOThreshold{
			{
				Target:    97.0,
				Timeframe: datadogV1.SLOTIMEFRAME_SEVEN_DAYS,
				Warning:   datadog.PtrFloat64(98.0),
			},
		},
		Timeframe:        datadogV1.SLOTIMEFRAME_SEVEN_DAYS.Ptr(),
		TargetThreshold:  datadog.PtrFloat64(97.0),
		WarningThreshold: datadog.PtrFloat64(98),
		Query: &datadogV1.ServiceLevelObjectiveQuery{
			Numerator:   "sum:httpservice.hits{code:2xx}.as_count()",
			Denominator: "sum:httpservice.hits{!code:3xx}.as_count()",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.UpdateSLO(ctx, SloData0ID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.UpdateSLO`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.UpdateSLO`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update an SLO returns "OK" response
```
// Update an SLO returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.SLOListResponse;
import com.datadog.api.client.v1.model.SLOThreshold;
import com.datadog.api.client.v1.model.SLOTimeframe;
import com.datadog.api.client.v1.model.SLOType;
import com.datadog.api.client.v1.model.ServiceLevelObjective;
import com.datadog.api.client.v1.model.ServiceLevelObjectiveQuery;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");
    String SLO_DATA_0_NAME = System.getenv("SLO_DATA_0_NAME");

    ServiceLevelObjective body =
        new ServiceLevelObjective()
            .type(SLOType.METRIC)
            .name(SLO_DATA_0_NAME)
            .thresholds(
                Collections.singletonList(
                    new SLOThreshold()
                        .target(97.0)
                        .timeframe(SLOTimeframe.SEVEN_DAYS)
                        .warning(98.0)))
            .timeframe(SLOTimeframe.SEVEN_DAYS)
            .targetThreshold(97.0)
            .warningThreshold(98.0)
            .query(
                new ServiceLevelObjectiveQuery()
                    .numerator("sum:httpservice.hits{code:2xx}.as_count()")
                    .denominator("sum:httpservice.hits{!code:3xx}.as_count()"));

    try {
      SLOListResponse result = apiInstance.updateSLO(SLO_DATA_0_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#updateSLO");
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

#####  Update an SLO returns "OK" response
```
"""
Update an SLO returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.service_level_objective import ServiceLevelObjective
from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]
SLO_DATA_0_NAME = environ["SLO_DATA_0_NAME"]

body = ServiceLevelObjective(
    type=SLOType.METRIC,
    name=SLO_DATA_0_NAME,
    thresholds=[
        SLOThreshold(
            target=97.0,
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=98.0,
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=97.0,
    warning_threshold=98.0,
    query=ServiceLevelObjectiveQuery(
        numerator="sum:httpservice.hits{code:2xx}.as_count()",
        denominator="sum:httpservice.hits{!code:3xx}.as_count()",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.update_slo(slo_id=SLO_DATA_0_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update an SLO returns "OK" response
```
# Update an SLO returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
SLO_DATA_0_NAME = ENV["SLO_DATA_0_NAME"]

body = DatadogAPIClient::V1::ServiceLevelObjective.new({
  type: DatadogAPIClient::V1::SLOType::METRIC,
  name: SLO_DATA_0_NAME,
  thresholds: [
    DatadogAPIClient::V1::SLOThreshold.new({
      target: 97.0,
      timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
      warning: 98.0,
    }),
  ],
  timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
  target_threshold: 97.0,
  warning_threshold: 98,
  query: DatadogAPIClient::V1::ServiceLevelObjectiveQuery.new({
    numerator: "sum:httpservice.hits{code:2xx}.as_count()",
    denominator: "sum:httpservice.hits{!code:3xx}.as_count()",
  }),
})
p api_instance.update_slo(SLO_DATA_0_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update an SLO returns "OK" response
```
// Update an SLO returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;
use datadog_api_client::datadogV1::model::SLOThreshold;
use datadog_api_client::datadogV1::model::SLOTimeframe;
use datadog_api_client::datadogV1::model::SLOType;
use datadog_api_client::datadogV1::model::ServiceLevelObjective;
use datadog_api_client::datadogV1::model::ServiceLevelObjectiveQuery;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let slo_data_0_name = std::env::var("SLO_DATA_0_NAME").unwrap();
    let body = ServiceLevelObjective::new(
        slo_data_0_name.clone(),
        vec![SLOThreshold::new(97.0, SLOTimeframe::SEVEN_DAYS).warning(98.0 as f64)],
        SLOType::METRIC,
    )
    .query(ServiceLevelObjectiveQuery::new(
        "sum:httpservice.hits{!code:3xx}.as_count()".to_string(),
        "sum:httpservice.hits{code:2xx}.as_count()".to_string(),
    ))
    .target_threshold(97.0 as f64)
    .timeframe(SLOTimeframe::SEVEN_DAYS)
    .warning_threshold(98.0 as f64);
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.update_slo(slo_data_0_id.clone(), body).await;
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

#####  Update an SLO returns "OK" response
```
/**
 * Update an SLO returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;
const SLO_DATA_0_NAME = process.env.SLO_DATA_0_NAME as string;

const params: v1.ServiceLevelObjectivesApiUpdateSLORequest = {
  body: {
    type: "metric",
    name: SLO_DATA_0_NAME,
    thresholds: [
      {
        target: 97.0,
        timeframe: "7d",
        warning: 98.0,
      },
    ],
    timeframe: "7d",
    targetThreshold: 97.0,
    warningThreshold: 98,
    query: {
      numerator: "sum:httpservice.hits{code:2xx}.as_count()",
      denominator: "sum:httpservice.hits{!code:3xx}.as_count()",
    },
  },
  sloId: SLO_DATA_0_ID,
};

apiInstance
  .updateSLO(params)
  .then((data: v1.SLOListResponse) => {
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
## [Get an SLO's details](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-an-slos-details)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-an-slos-details-v1)


GET https://api.ap1.datadoghq.com/api/v1/slo/{slo_id}https://api.ap2.datadoghq.com/api/v1/slo/{slo_id}https://api.datadoghq.eu/api/v1/slo/{slo_id}https://api.ddog-gov.com/api/v1/slo/{slo_id}https://api.datadoghq.com/api/v1/slo/{slo_id}https://api.us3.datadoghq.com/api/v1/slo/{slo_id}https://api.us5.datadoghq.com/api/v1/slo/{slo_id}
### Overview
Get a service level objective object. This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
slo_id [_required_]
string
The ID of the service level objective object.
#### Query Strings
Name
Type
Description
with_configured_alert_ids
boolean
Get the IDs of SLO monitors that reference this SLO.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLO-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLO-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLO-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLO-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A service level objective response containing a single service level objective.
Field
Type
Description
data
object
A service level objective object includes a service level indicator, thresholds for one or more timeframes, and metadata (`name`, `description`, `tags`, etc.).
configured_alert_ids
[integer]
A list of SLO monitors IDs that reference this SLO. This field is returned only when `with_configured_alert_ids` parameter is true in query.
created_at
int64
Creation timestamp (UNIX time in seconds)
Always included in service level objective responses.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
A user-defined description of the service level objective.
Always included in service level objective responses (but may be `null`). Optional in create/update requests.
groups
[string]
A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.
Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one.
id
string
A unique identifier for the service level objective object.
Always included in service level objective responses.
modified_at
int64
Modification timestamp (UNIX time in seconds)
Always included in service level objective responses.
monitor_ids
[integer]
A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is`monitor`**.
monitor_tags
[string]
The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field).
name
string
The name of the service level objective object.
query
object
A metric-based SLO. **Required if type is`metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.
denominator [_required_]
string
A Datadog metric query for total (valid) events.
numerator [_required_]
string
A Datadog metric query for good events.
sli_specification
<oneOf>
A generic SLI specification. This is currently used for time-slice SLOs only.
Option 1
object
A time-slice SLI specification.
time_slice [_required_]
object
The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.
comparator [_required_]
enum
The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`
query [_required_]
object
The queries and formula used to calculate the SLI value.
formulas [_required_]
[object]
A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.
formula [_required_]
string
The formula string, which is an expression involving named queries.
queries [_required_]
[ <oneOf>]
A list of queries that are used to calculate the SLI value.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
query_interval_seconds
enum
The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`
threshold [_required_]
double
The threshold value to which each SLI value will be compared.
tags
[string]
A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.
target_threshold
double
The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.
thresholds
[object]
The thresholds (timeframes and associated targets) for this service level objective object.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
timeframe
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
type
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
warning_threshold
double
The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.
errors
[string]
An array of error messages. Each endpoint documents how/whether this field is used.
```
{
  "data": {
    "configured_alert_ids": [
      123,
      456,
      789
    ],
    "created_at": "integer",
    "creator": {
      "email": "string",
      "handle": "string",
      "name": "string"
    },
    "description": "string",
    "groups": [
      "env:prod",
      "role:mysql"
    ],
    "id": "string",
    "modified_at": "integer",
    "monitor_ids": [],
    "monitor_tags": [],
    "name": "Custom Metric SLO",
    "query": {
      "denominator": "sum:my.custom.metric{*}.as_count()",
      "numerator": "sum:my.custom.metric{type:good}.as_count()"
    },
    "sli_specification": {
      "time_slice": {
        "comparator": ">",
        "query": {
          "formulas": [
            {
              "formula": "query1 - default_zero(query2)"
            }
          ],
          "queries": [
            []
          ]
        },
        "query_interval_seconds": 300,
        "threshold": 5
      }
    },
    "tags": [
      "env:prod",
      "app:core"
    ],
    "target_threshold": 99.9,
    "thresholds": [
      {
        "target": 99.9,
        "target_display": "99.9",
        "timeframe": "30d",
        "warning": 90,
        "warning_display": "90.0"
      }
    ],
    "timeframe": "30d",
    "type": "metric",
    "warning_threshold": 99.95
  },
  "errors": []
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python-legacy)


#####  Get an SLO's details
Copy
```
                  # Path parameters  
export slo_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an SLO's details
```
"""
Get an SLO's details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo(
        slo_id=SLO_DATA_0_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get an SLO's details
```
# Get an SLO's details returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.get_slo(SLO_DATA_0_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get an SLO's details
```
# This is not currently available for the Ruby API.
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get an SLO's details
```
// Get an SLO's details returns "OK" response

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
	// there is a valid "slo" in the system
	SloData0ID := os.Getenv("SLO_DATA_0_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.GetSLO(ctx, SloData0ID, *datadogV1.NewGetSLOOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.GetSLO`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.GetSLO`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get an SLO's details
```
// Get an SLO's details returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.SLOResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");

    try {
      SLOResponse result = apiInstance.getSLO(SLO_DATA_0_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#getSLO");
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

#####  Get an SLO's details
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_id = '<YOUR_SLO_ID>'

initialize(**options)

api.ServiceLevelObjective.get(slo_id)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get an SLO's details
```
// Get an SLO's details returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::GetSLOOptionalParams;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api
        .get_slo(slo_data_0_id.clone(), GetSLOOptionalParams::default())
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

#####  Get an SLO's details
```
/**
 * Get an SLO's details returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;

const params: v1.ServiceLevelObjectivesApiGetSLORequest = {
  sloId: SLO_DATA_0_ID,
};

apiInstance
  .getSLO(params)
  .then((data: v1.SLOResponse) => {
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
## [Delete an SLO](https://docs.datadoghq.com/api/latest/service-level-objectives/#delete-an-slo)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#delete-an-slo-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/slo/{slo_id}https://api.ap2.datadoghq.com/api/v1/slo/{slo_id}https://api.datadoghq.eu/api/v1/slo/{slo_id}https://api.ddog-gov.com/api/v1/slo/{slo_id}https://api.datadoghq.com/api/v1/slo/{slo_id}https://api.us3.datadoghq.com/api/v1/slo/{slo_id}https://api.us5.datadoghq.com/api/v1/slo/{slo_id}
### Overview
Permanently delete the specified service level objective object.
If an SLO is used in a dashboard, the `DELETE /v1/slo/` endpoint returns a 409 conflict error because the SLO is referenced in a dashboard.
This endpoint requires the `slos_write` permission.
OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
slo_id [_required_]
string
The ID of the service level objective.
#### Query Strings
Name
Type
Description
force
string
Delete the monitor even if it’s referenced by other resources (for example SLO, composite monitor).
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLO-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLO-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLO-404-v1)
  * [409](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLO-409-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLO-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A response list of all service level objective deleted.
Field
Type
Description
data
[string]
An array containing the ID of the deleted service level objective object.
errors
object
An dictionary containing the ID of the SLO as key and a deletion error as value.
<any-key>
string
Error preventing the SLO deletion.
```
{
  "data": [],
  "errors": {
    "<any-key>": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A response list of all service level objective deleted.
Field
Type
Description
data
[string]
An array containing the ID of the deleted service level objective object.
errors
object
An dictionary containing the ID of the SLO as key and a deletion error as value.
<any-key>
string
Error preventing the SLO deletion.
```
{
  "data": [],
  "errors": {
    "<any-key>": "string"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python-legacy)


#####  Delete an SLO
Copy
```
                  # Path parameters  
export slo_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an SLO
```
"""
Delete an SLO returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.delete_slo(
        slo_id=SLO_DATA_0_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete an SLO
```
# Delete an SLO returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.delete_slo(SLO_DATA_0_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an SLO
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'
slo_id  = '<YOUR_SLO_ID>'

dog = Dogapi::Client.new(api_key, app_key)

dog.delete_service_level_objective(slo_id)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete an SLO
```
// Delete an SLO returns "OK" response

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
	// there is a valid "slo" in the system
	SloData0ID := os.Getenv("SLO_DATA_0_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.DeleteSLO(ctx, SloData0ID, *datadogV1.NewDeleteSLOOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.DeleteSLO`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.DeleteSLO`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete an SLO
```
// Delete an SLO returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.SLODeleteResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");

    try {
      SLODeleteResponse result = apiInstance.deleteSLO(SLO_DATA_0_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#deleteSLO");
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

#####  Delete an SLO
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_id = '<YOUR_SLO_ID>'

initialize(**options)

api.ServiceLevelObjective.delete(slo_id)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Delete an SLO
```
// Delete an SLO returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::DeleteSLOOptionalParams;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api
        .delete_slo(slo_data_0_id.clone(), DeleteSLOOptionalParams::default())
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

#####  Delete an SLO
```
/**
 * Delete an SLO returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;

const params: v1.ServiceLevelObjectivesApiDeleteSLORequest = {
  sloId: SLO_DATA_0_ID,
};

apiInstance
  .deleteSLO(params)
  .then((data: v1.SLODeleteResponse) => {
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
## [Get an SLO's history](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-an-slos-history)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-an-slos-history-v1)


GET https://api.ap1.datadoghq.com/api/v1/slo/{slo_id}/historyhttps://api.ap2.datadoghq.com/api/v1/slo/{slo_id}/historyhttps://api.datadoghq.eu/api/v1/slo/{slo_id}/historyhttps://api.ddog-gov.com/api/v1/slo/{slo_id}/historyhttps://api.datadoghq.com/api/v1/slo/{slo_id}/historyhttps://api.us3.datadoghq.com/api/v1/slo/{slo_id}/historyhttps://api.us5.datadoghq.com/api/v1/slo/{slo_id}/history
### Overview
Get a specific SLO’s history, regardless of its SLO type.
The detailed history data is structured according to the source data type. For example, metric data is included for event SLOs that use the metric source, and monitor SLO types include the monitor transition history.
**Note:** There are different response formats for event based and time based SLOs. Examples of both are shown.
This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
slo_id [_required_]
string
The ID of the service level objective object.
#### Query Strings
Name
Type
Description
from_ts [_required_]
integer
The `from` timestamp for the query window in epoch seconds.
to_ts [_required_]
integer
The `to` timestamp for the query window in epoch seconds.
target
number
The SLO target. If `target` is passed in, the response will include the remaining error budget and a timeframe value of `custom`.
apply_correction
boolean
Defaults to `true`. If any SLO corrections are applied and this parameter is set to `false`, then the corrections will not be applied and the SLI values will not be affected.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOHistory-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOHistory-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOHistory-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOHistory-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOHistory-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A service level objective history response.
Field
Type
Description
data
object
An array of service level objective objects.
from_ts
int64
The `from` timestamp in epoch seconds.
group_by
[string]
For `metric` based SLOs where the query includes a group-by clause, this represents the list of grouping parameters.
This is not included in responses for `monitor` based SLOs.
groups
[object]
For grouped SLOs, this represents SLI data for specific groups.
This is not included in the responses for `metric` based SLOs.
error_budget_remaining
object
A mapping of threshold `timeframe` to the remaining error budget.
<any-key>
double
Remaining error budget.
errors
[object]
An array of error objects returned while querying the history data for the service level objective.
error_message [_required_]
string
A message with more details about the error.
error_type [_required_]
string
Type of the error.
group
string
For groups in a grouped SLO, this is the group name.
history
[array]
The state transition history for the monitor. It is represented as an array of pairs. Each pair is an array containing the timestamp of the transition as an integer in Unix epoch format in the first element, and the state as an integer in the second element. An integer value of `0` for state means uptime, `1` means downtime, and `2` means no data. Periods of no data are counted either as uptime or downtime depending on monitor settings. See [SLO documentation](https://docs.datadoghq.com/service_management/service_level_objectives/monitor/#missing-data) for detailed information.
monitor_modified
int64
For `monitor` based SLOs, this is the last modified timestamp in epoch seconds of the monitor.
monitor_type
string
For `monitor` based SLOs, this describes the type of monitor.
name
string
For groups in a grouped SLO, this is the group name. For monitors in a multi-monitor SLO, this is the monitor name.
precision
double
**DEPRECATED** : The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp. Use `span_precision` instead.
preview
boolean
For `monitor` based SLOs, when `true` this indicates that a replay is in progress to give an accurate uptime calculation.
sli_value
double
The current SLI value of the SLO over the history window.
span_precision
double
The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp.
uptime
double
**DEPRECATED** : Use `sli_value` instead.
monitors
[object]
For multi-monitor SLOs, this represents SLI data for specific monitors.
This is not included in the responses for `metric` based SLOs.
error_budget_remaining
object
A mapping of threshold `timeframe` to the remaining error budget.
<any-key>
double
Remaining error budget.
errors
[object]
An array of error objects returned while querying the history data for the service level objective.
error_message [_required_]
string
A message with more details about the error.
error_type [_required_]
string
Type of the error.
group
string
For groups in a grouped SLO, this is the group name.
history
[array]
The state transition history for the monitor. It is represented as an array of pairs. Each pair is an array containing the timestamp of the transition as an integer in Unix epoch format in the first element, and the state as an integer in the second element. An integer value of `0` for state means uptime, `1` means downtime, and `2` means no data. Periods of no data are counted either as uptime or downtime depending on monitor settings. See [SLO documentation](https://docs.datadoghq.com/service_management/service_level_objectives/monitor/#missing-data) for detailed information.
monitor_modified
int64
For `monitor` based SLOs, this is the last modified timestamp in epoch seconds of the monitor.
monitor_type
string
For `monitor` based SLOs, this describes the type of monitor.
name
string
For groups in a grouped SLO, this is the group name. For monitors in a multi-monitor SLO, this is the monitor name.
precision
double
**DEPRECATED** : The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp. Use `span_precision` instead.
preview
boolean
For `monitor` based SLOs, when `true` this indicates that a replay is in progress to give an accurate uptime calculation.
sli_value
double
The current SLI value of the SLO over the history window.
span_precision
double
The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp.
uptime
double
**DEPRECATED** : Use `sli_value` instead.
overall
object
An object that holds an SLI value and its associated data. It can represent an SLO's overall SLI value. This can also represent the SLI value for a specific monitor in multi-monitor SLOs, or a group in grouped SLOs.
error_budget_remaining
object
A mapping of threshold `timeframe` to the remaining error budget.
<any-key>
double
Remaining error budget.
errors
[object]
An array of error objects returned while querying the history data for the service level objective.
error_message [_required_]
string
A message with more details about the error.
error_type [_required_]
string
Type of the error.
group
string
For groups in a grouped SLO, this is the group name.
history
[array]
The state transition history for `monitor` or `time-slice` SLOs. It is represented as an array of pairs. Each pair is an array containing the timestamp of the transition as an integer in Unix epoch format in the first element, and the state as an integer in the second element. An integer value of `0` for state means uptime, `1` means downtime, and `2` means no data. Periods of no data count as uptime in time-slice SLOs, while for monitor SLOs, no data is counted either as uptime or downtime depending on monitor settings. See [SLO documentation](https://docs.datadoghq.com/service_management/service_level_objectives/monitor/#missing-data) for detailed information.
monitor_modified
int64
For `monitor` based SLOs, this is the last modified timestamp in epoch seconds of the monitor.
monitor_type
string
For `monitor` based SLOs, this describes the type of monitor.
name
string
For groups in a grouped SLO, this is the group name. For monitors in a multi-monitor SLO, this is the monitor name.
precision
object
A mapping of threshold `timeframe` to number of accurate decimals, regardless of the from && to timestamp.
<any-key>
double
The number of accurate decimals.
preview
boolean
For `monitor` based SLOs, when `true` this indicates that a replay is in progress to give an accurate uptime calculation.
sli_value
double
The current SLI value of the SLO over the history window.
span_precision
double
The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp.
uptime
double
**DEPRECATED** : Use `sli_value` instead.
series
object
A `metric` based SLO history response.
This is not included in responses for `monitor` based SLOs.
denominator [_required_]
object
A representation of `metric` based SLO timeseries for the provided queries. This is the same response type from `batch_query` endpoint.
count [_required_]
int64
Count of submitted metrics.
metadata
object
Query metadata.
aggr
string
**DEPRECATED** : Query aggregator function.
expression
string
**DEPRECATED** : Query expression.
metric
string
**DEPRECATED** : Query metric used.
query_index
int64
**DEPRECATED** : Query index from original combined query.
scope
string
**DEPRECATED** : Query scope.
unit
[object]
An array of metric units that contains up to two unit objects. For example, bytes represents one unit object and bytes per second represents two unit objects. If a metric query only has one unit object, the second array element is null.
family
string
The family of metric unit, for example `bytes` is the family for `kibibyte`, `byte`, and `bit` units.
id
int64
The ID of the metric unit.
name
string
The unit of the metric, for instance `byte`.
plural
string
The plural Unit of metric, for instance `bytes`.
scale_factor
double
The scale factor of metric unit, for instance `1.0`.
short_name
string
A shorter and abbreviated version of the metric unit, for instance `B`.
sum [_required_]
double
Total sum of the query.
values [_required_]
[number]
The query values for each metric.
interval [_required_]
int64
The aggregated query interval for the series data. It's implicit based on the query time window.
message
string
Optional message if there are specific query issues/warnings.
numerator [_required_]
object
A representation of `metric` based SLO timeseries for the provided queries. This is the same response type from `batch_query` endpoint.
count [_required_]
int64
Count of submitted metrics.
metadata
object
Query metadata.
aggr
string
**DEPRECATED** : Query aggregator function.
expression
string
**DEPRECATED** : Query expression.
metric
string
**DEPRECATED** : Query metric used.
query_index
int64
**DEPRECATED** : Query index from original combined query.
scope
string
**DEPRECATED** : Query scope.
unit
[object]
An array of metric units that contains up to two unit objects. For example, bytes represents one unit object and bytes per second represents two unit objects. If a metric query only has one unit object, the second array element is null.
family
string
The family of metric unit, for example `bytes` is the family for `kibibyte`, `byte`, and `bit` units.
id
int64
The ID of the metric unit.
name
string
The unit of the metric, for instance `byte`.
plural
string
The plural Unit of metric, for instance `bytes`.
scale_factor
double
The scale factor of metric unit, for instance `1.0`.
short_name
string
A shorter and abbreviated version of the metric unit, for instance `B`.
sum [_required_]
double
Total sum of the query.
values [_required_]
[number]
The query values for each metric.
query [_required_]
string
The combined numerator and denominator query CSV.
res_type [_required_]
string
The series result type. This mimics `batch_query` response type.
resp_version [_required_]
int64
The series response version type. This mimics `batch_query` response type.
times [_required_]
[number]
An array of query timestamps in EPOCH milliseconds.
thresholds
object
mapping of string timeframe to the SLO threshold.
<any-key>
object
SLO thresholds (target and optionally warning) for a single time window.
target [_required_]
double
The target value for the service level indicator within the corresponding timeframe.
target_display
string
A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).
Always included in service level objective responses. Ignored in create/update requests.
timeframe [_required_]
enum
The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`
warning
double
The warning value for the service level objective.
warning_display
string
A string representation of the warning target (see the description of the `target_display` field for details).
Included in service level objective responses if a warning target exists. Ignored in create/update requests.
to_ts
int64
The `to` timestamp in epoch seconds.
type
enum
The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`
type_id
enum
A numeric representation of the type of the service level objective (`0` for monitor, `1` for metric). Always included in service level objective responses. Ignored in create/update requests. Allowed enum values: `0,1,2`
errors
[object]
A list of errors while querying the history data for the service level objective.
error
string
Human readable error.
```
{
  "data": {
    "from_ts": 1615323990,
    "group_by": [],
    "groups": [
      {
        "error_budget_remaining": {
          "<any-key>": "number"
        },
        "errors": [
          {
            "error_message": "",
            "error_type": ""
          }
        ],
        "group": "name",
        "history": [
          [
            1579212382,
            0
          ]
        ],
        "monitor_modified": 1615867200,
        "monitor_type": "string",
        "name": "string",
        "precision": 2,
        "preview": true,
        "sli_value": 99.99,
        "span_precision": 2,
        "uptime": 99.99
      }
    ],
    "monitors": [
      {
        "error_budget_remaining": {
          "<any-key>": "number"
        },
        "errors": [
          {
            "error_message": "",
            "error_type": ""
          }
        ],
        "group": "name",
        "history": [
          [
            1579212382,
            0
          ]
        ],
        "monitor_modified": 1615867200,
        "monitor_type": "string",
        "name": "string",
        "precision": 2,
        "preview": true,
        "sli_value": 99.99,
        "span_precision": 2,
        "uptime": 99.99
      }
    ],
    "overall": {
      "error_budget_remaining": {
        "<any-key>": "number"
      },
      "errors": [
        {
          "error_message": "",
          "error_type": ""
        }
      ],
      "group": "name",
      "history": [
        [
          1579212382,
          0
        ]
      ],
      "monitor_modified": 1615867200,
      "monitor_type": "string",
      "name": "string",
      "precision": {
        "<any-key>": "number"
      },
      "preview": true,
      "sli_value": 99.99,
      "span_precision": 2,
      "uptime": 99.99
    },
    "series": {
      "denominator": {
        "count": 0,
        "metadata": {
          "aggr": "string",
          "expression": "string",
          "metric": "string",
          "query_index": "integer",
          "scope": "string",
          "unit": [
            {
              "family": "bytes",
              "id": 2,
              "name": "byte",
              "plural": "bytes",
              "scale_factor": 1,
              "short_name": "B"
            }
          ]
        },
        "sum": 0,
        "values": [
          []
        ]
      },
      "interval": 0,
      "message": "",
      "numerator": {
        "count": 0,
        "metadata": {
          "aggr": "string",
          "expression": "string",
          "metric": "string",
          "query_index": "integer",
          "scope": "string",
          "unit": [
            {
              "family": "bytes",
              "id": 2,
              "name": "byte",
              "plural": "bytes",
              "scale_factor": 1,
              "short_name": "B"
            }
          ]
        },
        "sum": 0,
        "values": [
          []
        ]
      },
      "query": "",
      "res_type": "",
      "resp_version": 0,
      "times": [
        []
      ]
    },
    "thresholds": {
      "<any-key>": {
        "target": 99.9,
        "target_display": "99.9",
        "timeframe": "30d",
        "warning": 90,
        "warning_display": "90.0"
      }
    },
    "to_ts": 1615928790,
    "type": "metric",
    "type_id": 0
  },
  "errors": [
    {
      "error": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python-legacy)


#####  Get an SLO's history
Copy
```
                  # Path parameters  
export slo_id="CHANGE_ME"  
# Required query arguments  
export from_ts="CHANGE_ME"  
export to_ts="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}/history?from_ts=${from_ts}&to_ts=${to_ts}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an SLO's history
```
"""
Get an SLO's history returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_history(
        slo_id=SLO_DATA_0_ID,
        from_ts=int((datetime.now() + relativedelta(days=-1)).timestamp()),
        to_ts=int(datetime.now().timestamp()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get an SLO's history
```
# Get an SLO's history returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.get_slo_history(SLO_DATA_0_ID, (Time.now + -1 * 86400).to_i, Time.now.to_i)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get an SLO's history
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'
slo_id  = '<YOUR_SLO_ID>'

dog = Dogapi::Client.new(api_key, app_key)

to_ts = 1_571_320_613
from_ts = to_ts - 60 * 60 * 24 * 30

dog.get_service_level_objective_history(slo_id, from_ts, to_ts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get an SLO's history
```
// Get an SLO's history returns "OK" response

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
	// there is a valid "slo" in the system
	SloData0ID := os.Getenv("SLO_DATA_0_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.GetSLOHistory(ctx, SloData0ID, time.Now().AddDate(0, 0, -1).Unix(), time.Now().Unix(), *datadogV1.NewGetSLOHistoryOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.GetSLOHistory`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.GetSLOHistory`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get an SLO's history
```
// Get an SLO's history returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.SLOHistoryResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");

    try {
      SLOHistoryResponse result =
          apiInstance.getSLOHistory(
              SLO_DATA_0_ID,
              OffsetDateTime.now().plusDays(-1).toInstant().getEpochSecond(),
              OffsetDateTime.now().toInstant().getEpochSecond());
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#getSLOHistory");
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

#####  Get an SLO's history
```
from datadog import initialize, api
import time

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_id = '<YOUR_SLO_ID>'

initialize(**options)

to_ts = int(time.time())
from_ts = to_ts - 60*60*24*30

api.ServiceLevelObjective.history(slo_id, from_ts=from_ts, to_ts=to_ts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get an SLO's history
```
// Get an SLO's history returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::GetSLOHistoryOptionalParams;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api
        .get_slo_history(
            slo_data_0_id.clone(),
            1636542671,
            1636629071,
            GetSLOHistoryOptionalParams::default(),
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

#####  Get an SLO's history
```
/**
 * Get an SLO's history returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;

const params: v1.ServiceLevelObjectivesApiGetSLOHistoryRequest = {
  sloId: SLO_DATA_0_ID,
  fromTs: Math.round(
    new Date(new Date().getTime() + -1 * 86400 * 1000).getTime() / 1000
  ),
  toTs: Math.round(new Date().getTime() / 1000),
};

apiInstance
  .getSLOHistory(params)
  .then((data: v1.SLOHistoryResponse) => {
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
## [Get Corrections For an SLO](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-corrections-for-an-slo)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-corrections-for-an-slo-v1)


GET https://api.ap1.datadoghq.com/api/v1/slo/{slo_id}/correctionshttps://api.ap2.datadoghq.com/api/v1/slo/{slo_id}/correctionshttps://api.datadoghq.eu/api/v1/slo/{slo_id}/correctionshttps://api.ddog-gov.com/api/v1/slo/{slo_id}/correctionshttps://api.datadoghq.com/api/v1/slo/{slo_id}/correctionshttps://api.us3.datadoghq.com/api/v1/slo/{slo_id}/correctionshttps://api.us5.datadoghq.com/api/v1/slo/{slo_id}/corrections
### Overview
Get corrections applied to an SLO This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
slo_id [_required_]
string
The ID of the service level objective object.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOCorrections-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOCorrections-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOCorrections-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOCorrections-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOCorrections-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A list of SLO correction objects.
Field
Type
Description
data
[object]
The list of SLO corrections objects.
attributes
object
The attribute object associated with the SLO correction.
category
enum
Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`
created_at
int64
The epoch timestamp of when the correction was created at.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
Description of the correction being made.
duration
int64
Length of time (in seconds) for a specified `rrule` recurring SLO correction.
end
int64
Ending time of the correction in epoch seconds.
modified_at
int64
The epoch timestamp of when the correction was modified at.
modifier
object
Modifier of the object.
email
string
Email of the Modifier.
handle
string
Handle of the Modifier.
name
string
Name of the Modifier.
rrule
string
The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`.
slo_id
string
ID of the SLO that this correction applies to.
start
int64
Starting time of the correction in epoch seconds.
timezone
string
The timezone to display in the UI for the correction times (defaults to "UTC").
id
string
The ID of the SLO correction.
type
enum
SLO correction resource type. Allowed enum values: `correction`
default: `correction`
meta
object
Object describing meta attributes of response.
page
object
Pagination object.
total_count
int64
Total count.
total_filtered_count
int64
Total count of elements matched by the filter.
```
{
  "data": [
    {
      "attributes": {
        "category": "Scheduled Maintenance",
        "created_at": "integer",
        "creator": {
          "email": "string",
          "handle": "string",
          "name": "string"
        },
        "description": "string",
        "duration": 3600,
        "end": "integer",
        "modified_at": "integer",
        "modifier": {
          "email": "string",
          "handle": "string",
          "name": "string"
        },
        "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5",
        "slo_id": "string",
        "start": "integer",
        "timezone": "string"
      },
      "id": "string",
      "type": "correction"
    }
  ],
  "meta": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)


#####  Get Corrections For an SLO
Copy
```
                  # Path parameters  
export slo_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}/corrections" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Corrections For an SLO
```
"""
Get Corrections For an SLO returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_corrections(
        slo_id=SLO_DATA_0_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get Corrections For an SLO
```
# Get Corrections For an SLO returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.get_slo_corrections(SLO_DATA_0_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get Corrections For an SLO
```
// Get Corrections For an SLO returns "OK" response

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
	// there is a valid "slo" in the system
	SloData0ID := os.Getenv("SLO_DATA_0_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.GetSLOCorrections(ctx, SloData0ID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.GetSLOCorrections`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.GetSLOCorrections`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get Corrections For an SLO
```
// Get Corrections For an SLO returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.SLOCorrectionListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");

    try {
      SLOCorrectionListResponse result = apiInstance.getSLOCorrections(SLO_DATA_0_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#getSLOCorrections");
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

#####  Get Corrections For an SLO
```
// Get Corrections For an SLO returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.get_slo_corrections(slo_data_0_id.clone()).await;
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

#####  Get Corrections For an SLO
```
/**
 * Get Corrections For an SLO returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;

const params: v1.ServiceLevelObjectivesApiGetSLOCorrectionsRequest = {
  sloId: SLO_DATA_0_ID,
};

apiInstance
  .getSLOCorrections(params)
  .then((data: v1.SLOCorrectionListResponse) => {
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
## [Check if SLOs can be safely deleted](https://docs.datadoghq.com/api/latest/service-level-objectives/#check-if-slos-can-be-safely-deleted)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#check-if-slos-can-be-safely-deleted-v1)


GET https://api.ap1.datadoghq.com/api/v1/slo/can_deletehttps://api.ap2.datadoghq.com/api/v1/slo/can_deletehttps://api.datadoghq.eu/api/v1/slo/can_deletehttps://api.ddog-gov.com/api/v1/slo/can_deletehttps://api.datadoghq.com/api/v1/slo/can_deletehttps://api.us3.datadoghq.com/api/v1/slo/can_deletehttps://api.us5.datadoghq.com/api/v1/slo/can_delete
### Overview
Check if an SLO can be safely deleted. For example, assure an SLO can be deleted without disrupting a dashboard. This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
ids [_required_]
string
A comma separated list of the IDs of the service level objectives objects.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#CheckCanDeleteSLO-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#CheckCanDeleteSLO-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#CheckCanDeleteSLO-403-v1)
  * [409](https://docs.datadoghq.com/api/latest/service-level-objectives/#CheckCanDeleteSLO-409-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#CheckCanDeleteSLO-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A service level objective response containing the requested object.
Field
Type
Description
data
object
An array of service level objective objects.
ok
[string]
An array of SLO IDs that can be safely deleted.
errors
object
A mapping of SLO id to it's current usages.
<any-key>
string
Description of the service level objective reference.
```
{
  "data": {
    "ok": []
  },
  "errors": {
    "<any-key>": "string"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


A service level objective response containing the requested object.
Field
Type
Description
data
object
An array of service level objective objects.
ok
[string]
An array of SLO IDs that can be safely deleted.
errors
object
A mapping of SLO id to it's current usages.
<any-key>
string
Description of the service level objective reference.
```
{
  "data": {
    "ok": []
  },
  "errors": {
    "<any-key>": "string"
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python-legacy)


#####  Check if SLOs can be safely deleted
Copy
```
                  # Required query arguments  
export ids="id1, id2, id3"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/can_delete?ids=${ids}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Check if SLOs can be safely deleted
```
"""
Check if SLOs can be safely deleted returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.check_can_delete_slo(
        ids="ids",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Check if SLOs can be safely deleted
```
# Check if SLOs can be safely deleted returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new
p api_instance.check_can_delete_slo("ids")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Check if SLOs can be safely deleted
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

slo_ids = ['<YOUR_SLO_ID>']
dog.can_delete_service_level_objective(slo_ids)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Check if SLOs can be safely deleted
```
// Check if SLOs can be safely deleted returns "OK" response

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
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.CheckCanDeleteSLO(ctx, "ids")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.CheckCanDeleteSLO`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.CheckCanDeleteSLO`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Check if SLOs can be safely deleted
```
// Check if SLOs can be safely deleted returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.CheckCanDeleteSLOResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    try {
      CheckCanDeleteSLOResponse result = apiInstance.checkCanDeleteSLO("id1, id2, id3");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#checkCanDeleteSLO");
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

#####  Check if SLOs can be safely deleted
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_ids = ['<YOUR_SLO_ID>']

initialize(**options)

api.ServiceLevelObjective.can_delete(slo_ids)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Check if SLOs can be safely deleted
```
// Check if SLOs can be safely deleted returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.check_can_delete_slo("ids".to_string()).await;
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

#####  Check if SLOs can be safely deleted
```
/**
 * Check if SLOs can be safely deleted returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

const params: v1.ServiceLevelObjectivesApiCheckCanDeleteSLORequest = {
  ids: "ids",
};

apiInstance
  .checkCanDeleteSLO(params)
  .then((data: v1.CheckCanDeleteSLOResponse) => {
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
## [Bulk Delete SLO Timeframes](https://docs.datadoghq.com/api/latest/service-level-objectives/#bulk-delete-slo-timeframes)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#bulk-delete-slo-timeframes-v1)


POST https://api.ap1.datadoghq.com/api/v1/slo/bulk_deletehttps://api.ap2.datadoghq.com/api/v1/slo/bulk_deletehttps://api.datadoghq.eu/api/v1/slo/bulk_deletehttps://api.ddog-gov.com/api/v1/slo/bulk_deletehttps://api.datadoghq.com/api/v1/slo/bulk_deletehttps://api.us3.datadoghq.com/api/v1/slo/bulk_deletehttps://api.us5.datadoghq.com/api/v1/slo/bulk_delete
### Overview
Delete (or partially delete) multiple service level objective objects.
This endpoint facilitates deletion of one or more thresholds for one or more service level objective objects. If all thresholds are deleted, the service level objective object is deleted as well.
This endpoint requires the `slos_write` permission.
OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Request
#### Body Data (required)
Delete multiple service level objective objects request body.
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


Expand All
Field
Type
Description
<any-key>
[string]
An array of all SLO timeframes.
```
{
  "id1": [
    "7d",
    "30d"
  ],
  "id2": [
    "7d",
    "30d"
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLOTimeframeInBulk-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLOTimeframeInBulk-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLOTimeframeInBulk-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#DeleteSLOTimeframeInBulk-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


The bulk partial delete service level objective object endpoint response.
This endpoint operates on multiple service level objective objects, so it may be partially successful. In such cases, the “data” and “error” fields in this response indicate which deletions succeeded and failed.
Field
Type
Description
data
object
An array of service level objective objects.
deleted
[string]
An array of service level objective object IDs that indicates which objects that were completely deleted.
updated
[string]
An array of service level objective object IDs that indicates which objects that were modified (objects for which at least one threshold was deleted, but that were not completely deleted).
errors
[object]
Array of errors object returned.
id [_required_]
string
The ID of the service level objective object associated with this error.
message [_required_]
string
The error message.
timeframe [_required_]
enum
The timeframe of the threshold associated with this error or "all" if all thresholds are affected. Allowed enum values: `7d,30d,90d,all`
```
{
  "data": {
    "deleted": [],
    "updated": []
  },
  "errors": [
    {
      "id": "",
      "message": "",
      "timeframe": "30d"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python-legacy)


#####  Bulk Delete SLO Timeframes
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/bulk_delete" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "id1": [
    "7d",
    "30d"
  ],
  "id2": [
    "7d",
    "30d"
  ]
}
EOF  

                
```

#####  Bulk Delete SLO Timeframes
```
"""
Bulk Delete SLO Timeframes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.slo_bulk_delete import SLOBulkDelete
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe

body = SLOBulkDelete(
    id1=[
        SLOTimeframe.SEVEN_DAYS,
        SLOTimeframe.THIRTY_DAYS,
    ],
    id2=[
        SLOTimeframe.SEVEN_DAYS,
        SLOTimeframe.THIRTY_DAYS,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.delete_slo_timeframe_in_bulk(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Bulk Delete SLO Timeframes
```
# Bulk Delete SLO Timeframes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

body = {
  id1: [
    DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
    DatadogAPIClient::V1::SLOTimeframe::THIRTY_DAYS,
  ], id2: [
    DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
    DatadogAPIClient::V1::SLOTimeframe::THIRTY_DAYS,
  ],
}
p api_instance.delete_slo_timeframe_in_bulk(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Bulk Delete SLO Timeframes
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

slo_id_one = '<YOUR_FIRST_SLO_ID>'.freeze
slo_id_two = '<YOUR_SECOND_SLO_ID>'.freeze

dog = Dogapi::Client.new(api_key, app_key)

# Delete multiple timeframes
thresholds = {
  slo_id_one => %w[7d],
  slo_id_two => %w[7d 30d]
}
dog.delete_timeframes_service_level_objective(thresholds)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Bulk Delete SLO Timeframes
```
// Bulk Delete SLO Timeframes returns "OK" response

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
	body := map[string][]datadogV1.SLOTimeframe{
		"id1": []datadogV1.SLOTimeframe{
			datadogV1.SLOTIMEFRAME_SEVEN_DAYS,
			datadogV1.SLOTIMEFRAME_THIRTY_DAYS,
		},
		"id2": []datadogV1.SLOTimeframe{
			datadogV1.SLOTIMEFRAME_SEVEN_DAYS,
			datadogV1.SLOTIMEFRAME_THIRTY_DAYS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.DeleteSLOTimeframeInBulk(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.DeleteSLOTimeframeInBulk`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.DeleteSLOTimeframeInBulk`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Bulk Delete SLO Timeframes
```
// Bulk Delete SLO Timeframes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.SLOBulkDeleteResponse;
import com.datadog.api.client.v1.model.SLOTimeframe;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    Map<String, List<SLOTimeframe>> body =
        Map.ofEntries(
            Map.entry("id1", Arrays.asList(SLOTimeframe.SEVEN_DAYS, SLOTimeframe.THIRTY_DAYS)),
            Map.entry("id2", Arrays.asList(SLOTimeframe.SEVEN_DAYS, SLOTimeframe.THIRTY_DAYS)));

    try {
      SLOBulkDeleteResponse result = apiInstance.deleteSLOTimeframeInBulk(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceLevelObjectivesApi#deleteSLOTimeframeInBulk");
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

#####  Bulk Delete SLO Timeframes
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_id_1 = '<YOUR_SLO_ID>'
slo_id_2 = '<YOUR_SLO_ID>'

initialize(**options)

delete_timeframes = {
  slo_id_1: ["7d"]
  slo_id_2: ["7d", "30d"]
}

api.ServiceLevelObjective.bulk_delete(delete_timeframes)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Bulk Delete SLO Timeframes
```
// Bulk Delete SLO Timeframes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;
use datadog_api_client::datadogV1::model::SLOTimeframe;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = BTreeMap::from([
        (
            "id1".to_string(),
            vec![SLOTimeframe::SEVEN_DAYS, SLOTimeframe::THIRTY_DAYS],
        ),
        (
            "id2".to_string(),
            vec![SLOTimeframe::SEVEN_DAYS, SLOTimeframe::THIRTY_DAYS],
        ),
    ]);
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.delete_slo_timeframe_in_bulk(body).await;
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

#####  Bulk Delete SLO Timeframes
```
/**
 * Bulk Delete SLO Timeframes returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

const params: v1.ServiceLevelObjectivesApiDeleteSLOTimeframeInBulkRequest = {
  body: {
    id1: ["7d", "30d"],
    id2: ["7d", "30d"],
  },
};

apiInstance
  .deleteSLOTimeframeInBulk(params)
  .then((data: v1.SLOBulkDeleteResponse) => {
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
## [Create a new SLO report](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-a-new-slo-report)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-a-new-slo-report-v2)


**Note** : This feature is in private beta. To request access, use the request access form in the [Service Level Objectives](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-csv-export) docs.
POST https://api.ap1.datadoghq.com/api/v2/slo/reporthttps://api.ap2.datadoghq.com/api/v2/slo/reporthttps://api.datadoghq.eu/api/v2/slo/reporthttps://api.ddog-gov.com/api/v2/slo/reporthttps://api.datadoghq.com/api/v2/slo/reporthttps://api.us3.datadoghq.com/api/v2/slo/reporthttps://api.us5.datadoghq.com/api/v2/slo/report
### Overview
Create a job to generate an SLO report. The report job is processed asynchronously and eventually results in a CSV report being available for download.
Check the status of the job and download the CSV report using the returned `report_id`.
This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Request
#### Body Data (required)
Create SLO report job request body.
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


Field
Type
Description
data [_required_]
object
The data portion of the SLO report request.
attributes [_required_]
object
The attributes portion of the SLO report request.
from_ts [_required_]
int64
The `from` timestamp for the report in epoch seconds.
interval
enum
The frequency at which report data is to be generated. Allowed enum values: `daily,weekly,monthly`
query [_required_]
string
The query string used to filter SLO results. Some examples of queries include `service:<service-name>` and `slo-name`.
timezone
string
The timezone used to determine the start and end of each interval. For example, weekly intervals start at 12am on Sunday in the specified timezone.
to_ts [_required_]
int64
The `to` timestamp for the report in epoch seconds.
```
{
  "data": {
    "attributes": {
      "from_ts": 1633173071,
      "to_ts": 1636629071,
      "query": "slo_type:metric \"SLO Reporting Test\"",
      "interval": "monthly",
      "timezone": "America/New_York"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLOReportJob-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLOReportJob-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLOReportJob-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#CreateSLOReportJob-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


The SLO report response.
Field
Type
Description
data
object
The data portion of the SLO report response.
id
string
The ID of the report job.
type
string
The type of ID.
```
{
  "data": {
    "id": "dc8d92aa-e0af-11ee-af21-1feeaccaa3a3",
    "type": "report_id"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)


#####  Create a new SLO report returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/slo/report" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "from_ts": 1633173071,
      "to_ts": 1636629071,
      "query": "slo_type:metric \"SLO Reporting Test\"",
      "interval": "monthly",
      "timezone": "America/New_York"
    }
  }
}
EOF  

                        
```

#####  Create a new SLO report returns "OK" response
```
// Create a new SLO report returns "OK" response

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
	body := datadogV2.SloReportCreateRequest{
		Data: datadogV2.SloReportCreateRequestData{
			Attributes: datadogV2.SloReportCreateRequestAttributes{
				FromTs:   time.Now().AddDate(0, 0, -40).Unix(),
				ToTs:     time.Now().Unix(),
				Query:    `slo_type:metric "SLO Reporting Test"`,
				Interval: datadogV2.SLOREPORTINTERVAL_MONTHLY.Ptr(),
				Timezone: datadog.PtrString("America/New_York"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateSLOReportJob", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.CreateSLOReportJob(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.CreateSLOReportJob`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.CreateSLOReportJob`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a new SLO report returns "OK" response
```
// Create a new SLO report returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v2.model.SLOReportInterval;
import com.datadog.api.client.v2.model.SLOReportPostResponse;
import com.datadog.api.client.v2.model.SloReportCreateRequest;
import com.datadog.api.client.v2.model.SloReportCreateRequestAttributes;
import com.datadog.api.client.v2.model.SloReportCreateRequestData;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createSLOReportJob", true);
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    SloReportCreateRequest body =
        new SloReportCreateRequest()
            .data(
                new SloReportCreateRequestData()
                    .attributes(
                        new SloReportCreateRequestAttributes()
                            .fromTs(OffsetDateTime.now().plusDays(-40).toInstant().getEpochSecond())
                            .toTs(OffsetDateTime.now().toInstant().getEpochSecond())
                            .query("""
slo_type:metric "SLO Reporting Test"
""")
                            .interval(SLOReportInterval.MONTHLY)
                            .timezone("America/New_York")));

    try {
      SLOReportPostResponse result = apiInstance.createSLOReportJob(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#createSLOReportJob");
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

#####  Create a new SLO report returns "OK" response
```
"""
Create a new SLO report returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v2.model.slo_report_create_request import SloReportCreateRequest
from datadog_api_client.v2.model.slo_report_create_request_attributes import SloReportCreateRequestAttributes
from datadog_api_client.v2.model.slo_report_create_request_data import SloReportCreateRequestData
from datadog_api_client.v2.model.slo_report_interval import SLOReportInterval

body = SloReportCreateRequest(
    data=SloReportCreateRequestData(
        attributes=SloReportCreateRequestAttributes(
            from_ts=int((datetime.now() + relativedelta(days=-40)).timestamp()),
            to_ts=int(datetime.now().timestamp()),
            query='slo_type:metric "SLO Reporting Test"',
            interval=SLOReportInterval.MONTHLY,
            timezone="America/New_York",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_slo_report_job"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo_report_job(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a new SLO report returns "OK" response
```
# Create a new SLO report returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_slo_report_job".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceLevelObjectivesAPI.new

body = DatadogAPIClient::V2::SloReportCreateRequest.new({
  data: DatadogAPIClient::V2::SloReportCreateRequestData.new({
    attributes: DatadogAPIClient::V2::SloReportCreateRequestAttributes.new({
      from_ts: (Time.now + -40 * 86400).to_i,
      to_ts: Time.now.to_i,
      query: 'slo_type:metric "SLO Reporting Test"',
      interval: DatadogAPIClient::V2::SLOReportInterval::MONTHLY,
      timezone: "America/New_York",
    }),
  }),
})
p api_instance.create_slo_report_job(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a new SLO report returns "OK" response
```
// Create a new SLO report returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_level_objectives::ServiceLevelObjectivesAPI;
use datadog_api_client::datadogV2::model::SLOReportInterval;
use datadog_api_client::datadogV2::model::SloReportCreateRequest;
use datadog_api_client::datadogV2::model::SloReportCreateRequestAttributes;
use datadog_api_client::datadogV2::model::SloReportCreateRequestData;

#[tokio::main]
async fn main() {
    let body = SloReportCreateRequest::new(SloReportCreateRequestData::new(
        SloReportCreateRequestAttributes::new(
            1633173071,
            r#"slo_type:metric "SLO Reporting Test""#.to_string(),
            1636629071,
        )
        .interval(SLOReportInterval::MONTHLY)
        .timezone("America/New_York".to_string()),
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateSLOReportJob", true);
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.create_slo_report_job(body).await;
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

#####  Create a new SLO report returns "OK" response
```
/**
 * Create a new SLO report returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createSLOReportJob"] = true;
const apiInstance = new v2.ServiceLevelObjectivesApi(configuration);

const params: v2.ServiceLevelObjectivesApiCreateSLOReportJobRequest = {
  body: {
    data: {
      attributes: {
        fromTs: Math.round(
          new Date(new Date().getTime() + -40 * 86400 * 1000).getTime() / 1000
        ),
        toTs: Math.round(new Date().getTime() / 1000),
        query: `slo_type:metric "SLO Reporting Test"`,
        interval: "monthly",
        timezone: "America/New_York",
      },
    },
  },
};

apiInstance
  .createSLOReportJob(params)
  .then((data: v2.SLOReportPostResponse) => {
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
## [Get SLO report status](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-slo-report-status)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-slo-report-status-v2)


**Note** : This feature is in private beta. To request access, use the request access form in the [Service Level Objectives](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-csv-export) docs.
GET https://api.ap1.datadoghq.com/api/v2/slo/report/{report_id}/statushttps://api.ap2.datadoghq.com/api/v2/slo/report/{report_id}/statushttps://api.datadoghq.eu/api/v2/slo/report/{report_id}/statushttps://api.ddog-gov.com/api/v2/slo/report/{report_id}/statushttps://api.datadoghq.com/api/v2/slo/report/{report_id}/statushttps://api.us3.datadoghq.com/api/v2/slo/report/{report_id}/statushttps://api.us5.datadoghq.com/api/v2/slo/report/{report_id}/status
### Overview
Get the status of the SLO report job.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
report_id [_required_]
string
The ID of the report job.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReportJobStatus-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReportJobStatus-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReportJobStatus-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReportJobStatus-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReportJobStatus-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


The SLO report status response.
Field
Type
Description
data
object
The data portion of the SLO report status response.
attributes
object
The attributes portion of the SLO report status response.
status
enum
The status of the SLO report job. Allowed enum values: `in_progress,completed,completed_with_errors,failed`
id
string
The ID of the report job.
type
string
The type of ID.
```
{
  "data": {
    "attributes": {
      "status": "completed"
    },
    "id": "dc8d92aa-e0af-11ee-af21-1feeaccaa3a3",
    "type": "report_id"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)


#####  Get SLO report status
Copy
```
                  # Path parameters  
export report_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/slo/report/${report_id}/status" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get SLO report status
```
"""
Get SLO report status returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "report" in the system
REPORT_DATA_ID = environ["REPORT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_slo_report_job_status"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_report_job_status(
        report_id=REPORT_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get SLO report status
```
# Get SLO report status returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_slo_report_job_status".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceLevelObjectivesAPI.new

# there is a valid "report" in the system
REPORT_DATA_ID = ENV["REPORT_DATA_ID"]
p api_instance.get_slo_report_job_status(REPORT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get SLO report status
```
// Get SLO report status returns "OK" response

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
	// there is a valid "report" in the system
	ReportDataID := os.Getenv("REPORT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetSLOReportJobStatus", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.GetSLOReportJobStatus(ctx, ReportDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.GetSLOReportJobStatus`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.GetSLOReportJobStatus`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get SLO report status
```
// Get SLO report status returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v2.model.SLOReportStatusGetResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getSLOReportJobStatus", true);
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    // there is a valid "report" in the system
    String REPORT_DATA_ID = System.getenv("REPORT_DATA_ID");

    try {
      SLOReportStatusGetResponse result = apiInstance.getSLOReportJobStatus(REPORT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#getSLOReportJobStatus");
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

#####  Get SLO report status
```
// Get SLO report status returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "report" in the system
    let report_data_id = std::env::var("REPORT_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetSLOReportJobStatus", true);
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api.get_slo_report_job_status(report_data_id.clone()).await;
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

#####  Get SLO report status
```
/**
 * Get SLO report status returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getSLOReportJobStatus"] = true;
const apiInstance = new v2.ServiceLevelObjectivesApi(configuration);

// there is a valid "report" in the system
const REPORT_DATA_ID = process.env.REPORT_DATA_ID as string;

const params: v2.ServiceLevelObjectivesApiGetSLOReportJobStatusRequest = {
  reportId: REPORT_DATA_ID,
};

apiInstance
  .getSLOReportJobStatus(params)
  .then((data: v2.SLOReportStatusGetResponse) => {
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
## [Get SLO report](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-slo-report)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-slo-report-v2)


**Note** : This feature is in private beta. To request access, use the request access form in the [Service Level Objectives](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-csv-export) docs.
GET https://api.ap1.datadoghq.com/api/v2/slo/report/{report_id}/downloadhttps://api.ap2.datadoghq.com/api/v2/slo/report/{report_id}/downloadhttps://api.datadoghq.eu/api/v2/slo/report/{report_id}/downloadhttps://api.ddog-gov.com/api/v2/slo/report/{report_id}/downloadhttps://api.datadoghq.com/api/v2/slo/report/{report_id}/downloadhttps://api.us3.datadoghq.com/api/v2/slo/report/{report_id}/downloadhttps://api.us5.datadoghq.com/api/v2/slo/report/{report_id}/download
### Overview
Download an SLO report. This can only be performed after the report job has completed.
Reports are not guaranteed to exist indefinitely. Datadog recommends that you download the report as soon as it is available.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
report_id [_required_]
string
The ID of the report job.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReport-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReport-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReport-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReport-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objectives/#GetSLOReport-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objectives/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objectives/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objectives/?code-lang=typescript)


#####  Get SLO report
Copy
```
                  # Path parameters  
export report_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/slo/report/${report_id}/download" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get SLO report
```
"""
Get SLO report returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi

configuration = Configuration()
configuration.unstable_operations["get_slo_report"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_report(
        report_id="9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get SLO report
```
# Get SLO report returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_slo_report".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceLevelObjectivesAPI.new
p api_instance.get_slo_report("9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get SLO report
```
// Get SLO report returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.GetSLOReport", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceLevelObjectivesApi(apiClient)
	resp, r, err := api.GetSLOReport(ctx, "9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.GetSLOReport`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.GetSLOReport`:\n%s\n", resp)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get SLO report
```
// Get SLO report returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceLevelObjectivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getSLOReport", true);
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    try {
      String result = apiInstance.getSLOReport("9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#getSLOReport");
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

#####  Get SLO report
```
// Get SLO report returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetSLOReport", true);
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api
        .get_slo_report("9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f".to_string())
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

#####  Get SLO report
```
/**
 * Get SLO report returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getSLOReport"] = true;
const apiInstance = new v2.ServiceLevelObjectivesApi(configuration);

const params: v2.ServiceLevelObjectivesApiGetSLOReportRequest = {
  reportId: "9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f",
};

apiInstance
  .getSLOReport(params)
  .then((data: string) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=123ba612-2eed-4200-81dc-6ea11c312473&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2ffdaa14-0623-445e-9f19-d0fec4c34cb3&pt=Service%20Level%20Objectives&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-level-objectives%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=123ba612-2eed-4200-81dc-6ea11c312473&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2ffdaa14-0623-445e-9f19-d0fec4c34cb3&pt=Service%20Level%20Objectives&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-level-objectives%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=024537a3-b549-45e5-8a80-2116ef2e82c3&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Service%20Level%20Objectives&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-level-objectives%2F&r=&lt=12673&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=842901)
